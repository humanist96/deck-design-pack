#!/usr/bin/env python3
"""Install this pack's deck templates and brand presets into a ppt-master workspace.

Copies `decks/<id>/` and `brands/<id>/` into the workspace template library, then
writes both discovery indexes.

Why this script exists instead of just calling the workspace registrar: the stock
`register_template.py` rebuilds each deck index entry from scratch and drops the
`defaults` block that the Confirm UI reads to cascade a deck's Stage-1 anchors
(mode / visual_style / delivery_purpose). This installer sources that block from
each template's own `design_spec.md` frontmatter, so a deck keeps its anchors
however many times the index is rebuilt.

Usage
-----
    python3 install.py /path/to/ppt-master-workspace
    python3 install.py /path/to/workspace --only midnight-panel polarity
    python3 install.py /path/to/workspace --force      # overwrite existing ids
    python3 install.py /path/to/workspace --dry-run
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from collections import OrderedDict
from pathlib import Path

PACK_ROOT = Path(__file__).resolve().parent
TEMPLATES_SUBPATH = Path(".claude/skills/ppt-master/templates")

# Stage-1 anchor keys the Confirm UI honours; anything else is ignored there, so
# it is dropped here rather than written into the index.
ANCHOR_KEYS = ("mode", "visual_style", "delivery_purpose", "template_adherence")


class InstallError(RuntimeError):
    """Raised for any condition that must stop the install before writing."""


# --------------------------------------------------------------------------- #
# frontmatter
# --------------------------------------------------------------------------- #

def read_frontmatter(spec: Path) -> dict:
    """Parse the YAML frontmatter of a design_spec.md.

    Uses PyYAML when available and otherwise falls back to a small scalar/list
    reader plus a one-level nested-mapping reader, which is all this pack's
    frontmatter needs (`defaults:` is the only nested block).
    """
    text = spec.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, flags=re.S)
    if not match:
        raise InstallError(f"{spec}: missing YAML frontmatter")
    block = match.group(1)

    try:
        import yaml  # type: ignore
    except ImportError:
        pass
    else:
        data = yaml.safe_load(block)
        if not isinstance(data, dict):
            raise InstallError(f"{spec}: frontmatter is not a mapping")
        return data

    data: dict = {}
    current_key: str | None = None
    for raw_line in block.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        if raw_line.startswith((" ", "\t")):
            if current_key is None or ":" not in raw_line:
                continue
            sub_key, sub_val = raw_line.strip().split(":", 1)
            data.setdefault(current_key, {})
            if isinstance(data[current_key], dict):
                data[current_key][sub_key.strip()] = _scalar(sub_val)
            continue
        if ":" not in raw_line:
            continue
        key, val = raw_line.split(":", 1)
        current_key = key.strip()
        val = val.strip()
        data[current_key] = {} if val == "" else _scalar(val)
    return data


def _scalar(raw: str):
    val = raw.strip().strip('"').strip("'")
    if val.startswith("[") and val.endswith("]"):
        return [v.strip() for v in val[1:-1].split(",") if v.strip()]
    return val


def anchor_defaults(raw: object) -> "OrderedDict[str, str] | None":
    """Keep only the anchor keys the Confirm UI actually cascades."""
    if not isinstance(raw, dict):
        return None
    picked = OrderedDict(
        (key, str(raw[key]).strip())
        for key in ANCHOR_KEYS
        if isinstance(raw.get(key), str) and str(raw[key]).strip()
    )
    return picked or None


# --------------------------------------------------------------------------- #
# discovery
# --------------------------------------------------------------------------- #

def discover(kind: str, only: list[str] | None) -> list[tuple[str, Path]]:
    base = PACK_ROOT / ("decks" if kind == "deck" else "brands")
    if not base.is_dir():
        raise InstallError(f"pack directory missing: {base}")
    found = []
    for entry in sorted(base.iterdir()):
        spec = entry / "templates" / "design_spec.md"
        if entry.is_dir() and spec.is_file():
            found.append((entry.name, entry))
    if only:
        wanted = set(only)
        found = [item for item in found if item[0] in wanted]
        missing = wanted - {name for name, _ in found}
        if missing:
            raise InstallError(f"{kind}: unknown id(s) {sorted(missing)}")
    return found


def deck_entry(template_id: str, spec_dir: Path) -> "OrderedDict[str, object]":
    fm = read_frontmatter(spec_dir / "templates" / "design_spec.md")
    svg_count = len(list((spec_dir / "templates").glob("*.svg")))
    entry: "OrderedDict[str, object]" = OrderedDict(
        summary=str(fm.get("summary", "")).strip(),
        canvas_format=str(fm.get("canvas_format", "ppt169")),
        page_count=int(fm.get("page_count", svg_count)),
        primary_color=str(fm.get("primary_color", "")),
    )
    defaults = anchor_defaults(fm.get("defaults"))
    if defaults is not None:
        entry["defaults"] = defaults
    return entry


def brand_entry(template_id: str, spec_dir: Path) -> "OrderedDict[str, object]":
    fm = read_frontmatter(spec_dir / "templates" / "design_spec.md")
    return OrderedDict(
        summary=str(fm.get("summary", "")).strip(),
        primary_color=str(fm.get("primary_color", "")),
    )


# --------------------------------------------------------------------------- #
# install
# --------------------------------------------------------------------------- #

def install(workspace: Path, only: list[str] | None, force: bool, dry_run: bool) -> int:
    templates_root = workspace / TEMPLATES_SUBPATH
    if not templates_root.is_dir():
        raise InstallError(
            f"not a ppt-master workspace: {templates_root} does not exist"
        )

    plan: list[tuple[str, str, Path, Path]] = []
    for kind, index_name in (("deck", "decks_index.json"), ("brand", "brands_index.json")):
        target_root = templates_root / (index_name.split("_")[0])
        for template_id, src in discover(kind, only):
            dst = target_root / template_id
            if dst.exists() and not force:
                raise InstallError(
                    f"{kind} '{template_id}' already exists at {dst} — "
                    f"pass --force to replace it"
                )
            plan.append((kind, template_id, src, dst))

    if not plan:
        raise InstallError("nothing to install (check --only)")

    for kind, template_id, src, dst in plan:
        print(f"  {kind:5} {template_id:16} -> {dst}")
        if dry_run:
            continue
        if dst.exists():
            shutil.rmtree(dst)
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(src, dst)

    for kind, index_name, builder in (
        ("deck", "decks_index.json", deck_entry),
        ("brand", "brands_index.json", brand_entry),
    ):
        items = [item for item in plan if item[0] == kind]
        if not items:
            continue
        index_path = templates_root / index_name.split("_")[0] / index_name
        index = json.loads(index_path.read_text(encoding="utf-8")) if index_path.is_file() else {}
        for _, template_id, src, _dst in items:
            index[template_id] = builder(template_id, src)
        if dry_run:
            print(f"  would write {index_path} ({len(items)} entr{'y' if len(items)==1 else 'ies'})")
            continue
        index_path.parent.mkdir(parents=True, exist_ok=True)
        index_path.write_text(
            json.dumps(dict(sorted(index.items())), ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"  wrote {index_path}")

    return len(plan)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Install deck-design-pack templates into a ppt-master workspace."
    )
    parser.add_argument("workspace", type=Path, help="ppt-master workspace root")
    parser.add_argument("--only", nargs="+", metavar="ID", help="install only these ids")
    parser.add_argument("--force", action="store_true", help="replace existing ids")
    parser.add_argument("--dry-run", action="store_true", help="show the plan, write nothing")
    args = parser.parse_args()

    try:
        count = install(args.workspace.expanduser().resolve(), args.only, args.force, args.dry_run)
    except InstallError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    verb = "would install" if args.dry_run else "installed"
    print(f"\n{verb} {count} template workspace(s).")
    if not args.dry_run:
        print("Open the workspace in your agent and pick a deck at the Strategist confirmation step.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
