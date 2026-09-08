# Install

## In this repository: nothing to install

The templates already live where the pipeline reads them —
`.claude/skills/ppt-master/templates/{decks,brands}/` — and are registered in both discovery
indexes. A clone is ready to use:

```bash
git clone https://github.com/humanist96/deck-design-pack.git
cd deck-design-pack
pip install -r requirements.txt
```

Open the folder in your agent and ask for a deck. Jump to [Using a template](#using-a-template).

## Requirements

- Python 3.10+ (`requirements.txt` covers the pipeline; `install.py` itself is standard-library only, and uses PyYAML if present)
- **Pretendard** installed on any machine that opens the exported decks — PPTX does not embed fonts. Bundled at `.claude/skills/ppt-master/assets/fonts/Pretendard/`
- **KoPub돋움체** (Bold/Medium) for decks exported from `koscom-chevron` — the TTFs ship in `.claude/skills/ppt-master/templates/decks/koscom-chevron/fonts/`

---

## Exporting the pack into another workspace

If you already run your own ppt-master workspace and want only these seven templates there,
`install.py` copies them across and merges that workspace's two discovery indexes:

```bash
python3 install.py /path/to/your/ppt-master-workspace
```

Expected output:

```
  deck  gradient-mesh    -> .../templates/decks/gradient-mesh
  ...
  brand signal-green     -> .../templates/brands/signal-green
  wrote .../templates/decks/decks_index.json
  wrote .../templates/brands/brands_index.json

installed 14 template workspace(s).
```

The target must be a directory containing `.claude/skills/ppt-master/templates/`. Pointing the
script at this repository is refused — the templates are already installed here.

### Options

| Flag | Effect |
|---|---|
| `--only <id> [<id>…]` | Install a subset instead of all seven |
| `--force` | Replace template ids that already exist (removes the old directory first) |
| `--dry-run` | Print the plan and index writes, change nothing |

The installer refuses to overwrite an existing id unless `--force` is given, and validates every id before writing anything — a bad `--only` argument aborts before the first copy.

### Manual export

If you prefer not to run the script, for each id:

1. Copy `.claude/skills/ppt-master/templates/decks/<id>/` into `<workspace>/.claude/skills/ppt-master/templates/decks/`
2. Copy `.claude/skills/ppt-master/templates/brands/<id>/` into `<workspace>/.claude/skills/ppt-master/templates/brands/`
3. Add an entry to that workspace's `decks_index.json` for each deck:

```json
"midnight-panel": {
  "summary": "…",
  "canvas_format": "ppt169",
  "page_count": 10,
  "primary_color": "#5E6AD2",
  "defaults": {
    "mode": "briefing",
    "visual_style": "dark-tech",
    "delivery_purpose": "balanced"
  }
}
```

4. Add an entry to `brands_index.json` for each brand preset (`summary` and `primary_color` only)

> **Do not** register these with `register_template.py`. It rebuilds each entry from scratch and drops the `defaults` block, which is what the Confirm UI reads to cascade a deck's Stage-1 anchors. Re-run `install.py --force` instead; it is idempotent.

---

## Verify

From this repository's root:

```bash
python3 .claude/skills/ppt-master/scripts/svg_quality_checker.py \
        .claude/skills/ppt-master/templates/decks/midnight-panel/templates \
        --template-mode --format ppt169
```

Expect `0 errors, 0 warnings`.

To produce a review PPTX of a template's full roster:

```bash
python3 .claude/skills/ppt-master/scripts/template_preview_pptx.py \
        .claude/skills/ppt-master/templates/decks/midnight-panel
```

Expect `10 slides, 1 master(s), 9 layout(s)`.

---

## Using a template

Open the repository in your agent and ask for a deck normally. At the Strategist confirmation step
each template appears as a card. Selecting it re-defaults the direction anchors the template
declares (mode, visual style, delivery purpose) — every field stays editable afterwards.

You can also name a template directly:

```
Use .claude/skills/ppt-master/templates/decks/midnight-panel/ and build a deck from <source>
```

### Adherence

| Value | Behaviour |
|---|---|
| `strict` | Keeps the prototype's Master/Layout/slot contract exactly. Every page maps to one template SVG. |
| `adaptive` *(default)* | Keeps the Master, may assign a new Layout key when a composition genuinely evolves. |

The six originals are verified under `strict` — a generated deck keeps the template's layout picker names in PowerPoint.

## Removing a template

```bash
rm -rf .claude/skills/ppt-master/templates/decks/<id>
rm -rf .claude/skills/ppt-master/templates/brands/<id>
```

Then delete the matching keys from `decks_index.json` and `brands_index.json`.
