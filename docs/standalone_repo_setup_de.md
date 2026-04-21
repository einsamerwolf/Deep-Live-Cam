# Aus Deep-Live-Cam in ein eigenes GitHub-Projekt auslagern

Franz, du hast recht: Wenn das ein eigenes Vorhaben ist, sollte es ein eigenes Repo sein.

## 1) Standalone-Projekt erzeugen

```bash
cd /workspace/Deep-Live-Cam
bash tools/bootstrap_kommunal_lernapp_repo.sh kommunal-forcechain-lernapp /workspace
```

Das erzeugt lokal ein neues Projekt unter:
- `/workspace/kommunal-forcechain-lernapp`

## 2) Prüfen, dass es wirklich separat ist

```bash
cd /workspace/kommunal-forcechain-lernapp
git status
python3 tools/quiz_forcechain_demo.py --answers A,A,B,A,A,A --expect-path Q001,Q001a,Q001b,Q002,Q002a
```

## 3) Auf GitHub unter eigenem Namen speichern

1. Neues leeres GitHub-Repo anlegen, z. B. `kommunal-forcechain-lernapp`.
2. Dann lokal:

```bash
cd /workspace/kommunal-forcechain-lernapp
git remote add origin <DEINE_GITHUB_URL>
git branch -M main
git push -u origin main
```

## 4) Optional: Deep-Live-Cam aufräumen

Wenn du die Dateien dort nicht mehr willst, kannst du sie danach aus Deep-Live-Cam löschen und separat weiterführen.
