# Lernapp: Bezirksvertretung Köln-Kalk

Diese kleine Lernapp vermittelt praxisnahes Wissen für (angehende) Bezirksvertreter*innen mit Fokus auf Köln-Kalk.

## Ich finde die Dateien nicht – Soforthilfe

Die Dateien liegen im Ordner:

- **`/workspace/Deep-Live-Cam/learning-app`**

Dort findest du:

- `index.html`  → **diese Datei im Browser öffnen**
- `README.md`
- `data/content.json`
- `data/quiz_forcechains.csv`
- `data/apps_script_forcechain_example.gs`

### Schritt-für-Schritt im Dateimanager

1. Öffne den Ordner **Deep-Live-Cam**.
2. Öffne den Unterordner **learning-app**.
3. Doppelklick auf **index.html**.

> Wenn du `index.html` nicht siehst, bist du im falschen Ordner. Suche nach **learning-app**.

## Für No‑Coder: So startest du die App in 30 Sekunden

1. Öffne den Ordner `learning-app`.
2. Mache einen **Doppelklick auf `index.html`**.
3. Die App startet direkt im Browser (Chrome/Edge/Firefox).

### Wo liegt die `index.html` genau?

- **Im Projektordner:** `learning-app/index.html`
- **Voller Pfad in dieser Umgebung:** `/workspace/Deep-Live-Cam/learning-app/index.html`

Wenn du im Dateimanager bist: Ordner `Deep-Live-Cam` öffnen → `learning-app` öffnen → `index.html` doppelklicken.

> Du brauchst dafür **kein Python**, **kein Terminal** und **keinen Server**.

## Inhalt

- **Geschäftsordnungs-Analyse (kompakt)**
- **Praxismodule** mit Tricks & Kniffen
- **Szenario-Training** für Sitzungen, Anträge und Bürgerdialog
- **Quiz mit Force-Ketten** (Fehlerkette Q001 → Q001a → Q001b)

## Optional (nur wenn du möchtest)

Wenn du später Inhalte austauschen willst, liegen Beispiele zusätzlich in:

- `data/content.json`
- `data/quiz_forcechains.csv`
- `data/apps_script_forcechain_example.gs`

## Hinweis zur Quellenlage

In dieser Ausführungsumgebung war kein externer Webzugriff auf städtische Seiten möglich.
Die Analyse ist daher als **strukturiertes Lernmodell** aufgebaut und muss vor realem Einsatz mit der aktuell gültigen Geschäftsordnung und Hauptsatzung der Stadt Köln gegengeprüft werden.


## Liegen die Dateien auf GitHub?

Kurz: **Nur wenn das Repository mit GitHub verbunden und die Commits gepusht wurden**.

Schnell prüfen:

1. `git remote -v` → zeigt eine GitHub-URL, wenn ein Remote gesetzt ist.
2. `git log --oneline -n 5` → zeigt die letzten Commits (inkl. Lernapp-Commit).
3. `git push` → lädt lokale Commits zu GitHub hoch (falls Remote vorhanden).

Wenn `git remote -v` **nichts** ausgibt, liegen die Dateien aktuell nur lokal auf deinem Rechner/Server.
