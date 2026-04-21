#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <new_repo_name> [target_parent_dir]"
  echo "Example: $0 kommunal-forcechain-lernapp /workspace"
  exit 1
fi

NEW_REPO_NAME="$1"
TARGET_PARENT="${2:-/workspace}"
SOURCE_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TARGET_DIR="${TARGET_PARENT%/}/${NEW_REPO_NAME}"

if [[ -e "$TARGET_DIR" ]]; then
  echo "Target already exists: $TARGET_DIR"
  echo "Bitte anderen Namen wählen oder Zielordner löschen."
  exit 2
fi

mkdir -p "$TARGET_DIR/docs/data" "$TARGET_DIR/tools"

cp "$SOURCE_ROOT/tools/quiz_forcechain_demo.py" "$TARGET_DIR/tools/"
cp "$SOURCE_ROOT/docs/data/quiz100_forcechains_demo.csv" "$TARGET_DIR/docs/data/"
cp "$SOURCE_ROOT/docs/forcechain_quickstart_de.md" "$TARGET_DIR/docs/"
cp "$SOURCE_ROOT/docs/kommunalpolitik_lernapp_pareto_plan.md" "$TARGET_DIR/docs/"

if [[ -f /mnt/data/quiz100_forcechains.csv ]]; then
  cp /mnt/data/quiz100_forcechains.csv "$TARGET_DIR/docs/data/"
fi

cat > "$TARGET_DIR/README.md" <<'README'
# Kommunal Force-Chain Lernapp (Standalone)

Dieses Repo wurde aus Deep-Live-Cam ausgelagert.

## Schnellstart

```bash
python3 tools/quiz_forcechain_demo.py --answers A,A,B,A,A,A
python3 tools/quiz_forcechain_demo.py --answers A,A,B,A,A,A --expect-path Q001,Q001a,Q001b,Q002,Q002a
```

## Eigene CSV testen

```bash
python3 tools/quiz_forcechain_demo.py --csv docs/data/quiz100_forcechains.csv --answers A,A,B,A,A,A
```
README

cat > "$TARGET_DIR/.gitignore" <<'GITIGNORE'
__pycache__/
*.pyc
.DS_Store
GITIGNORE

(
  cd "$TARGET_DIR"
  git init
  git add .
  git commit -m "Initial standalone commit: force-chain quiz demo"
)

echo "\nFertig. Neues Projekt erstellt unter: $TARGET_DIR"
echo "Nächster Schritt (GitHub):"
echo "  cd $TARGET_DIR"
echo "  git remote add origin <dein-github-repo-url>"
echo "  git branch -M main"
echo "  git push -u origin main"
