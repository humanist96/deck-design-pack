# Install

## Requirements

- A ppt-master-compatible workspace (a directory containing `.claude/skills/ppt-master/templates/`)
- Python 3.10+ (standard library only; PyYAML is used if present but not required)
- **Pretendard** installed on any machine that opens the exported decks — PPTX does not embed fonts

## Install

```bash
git clone https://github.com/humanist96/deck-design-pack.git
cd deck-design-pack
python3 install.py /path/to/your/ppt-master-workspace
```

Expected output:

```
  deck  gradient-mesh    -> .../templates/decks/gradient-mesh
  ...
  brand signal-green     -> .../templates/brands/signal-green
  wrote .../templates/decks/decks_index.json
  wrote .../templates/brands/brands_index.json

installed 12 template workspace(s).
```

## Options

| Flag | Effect |
|---|---|
| `--only <id> [<id>…]` | Install a subset instead of all six |
| `--force` | Replace template ids that already exist (removes the old directory first) |
| `--dry-run` | Print the plan and index writes, change nothing |

The installer refuses to overwrite an existing id unless `--force` is given, and validates every id before writing anything — a bad `--only` argument aborts before the first copy.

## Verify

```bash
python3 <workspace>/.claude/skills/ppt-master/scripts/svg_quality_checker.py \
        <workspace>/.claude/skills/ppt-master/templates/decks/midnight-panel/templates \
        --template-mode --format ppt169
```

Expect `0 errors, 0 warnings`.

To produce a review PPTX of a template's full roster:

```bash
python3 <workspace>/.claude/skills/ppt-master/scripts/template_preview_pptx.py \
        <workspace>/.claude/skills/ppt-master/templates/decks/midnight-panel
```

Expect `10 slides, 1 master(s), 9 layout(s)`.

## Manual install

If you prefer not to run the script:

1. Copy `decks/<id>/` into `<workspace>/.claude/skills/ppt-master/templates/decks/`
2. Copy `brands/<id>/` into `<workspace>/.claude/skills/ppt-master/templates/brands/`
3. Add an entry to `decks_index.json` for each deck:

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

> **Do not** register these with the workspace's own `register_template.py`. It rebuilds each entry from scratch and drops the `defaults` block, which is what the Confirm UI reads to cascade a deck's Stage-1 anchors. Re-run `install.py --force` instead; it is idempotent.

## Using a template

Once installed, open the workspace in your agent and ask for a deck normally. At the Strategist confirmation step the template appears as a card. Selecting it re-defaults the direction anchors the template declares (mode, visual style, delivery purpose) — every field stays editable afterwards.

You can also pass a workspace root directly:

```
Use .claude/skills/ppt-master/templates/decks/midnight-panel/ and build a deck from <source>
```

### Adherence

| Value | Behaviour |
|---|---|
| `strict` | Keeps the prototype's Master/Layout/slot contract exactly. Every page maps to one template SVG. |
| `adaptive` *(default)* | Keeps the Master, may assign a new Layout key when a composition genuinely evolves. |

All six templates are verified under `strict` — a generated deck keeps the template's layout picker names in PowerPoint.

## Uninstall

```bash
rm -rf <workspace>/.claude/skills/ppt-master/templates/decks/<id>
rm -rf <workspace>/.claude/skills/ppt-master/templates/brands/<id>
```

Then delete the matching keys from `decks_index.json` and `brands_index.json`.
