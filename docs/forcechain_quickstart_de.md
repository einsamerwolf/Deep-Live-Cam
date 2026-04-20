# Force-Ketten lokal testen (Schritt für Schritt)

Franz, so bekommst du die Demo in wenigen Minuten zum Laufen und prüfst objektiv, ob die Kette korrekt funktioniert.

## 1) In den Projektordner wechseln

```bash
cd /workspace/Deep-Live-Cam
```

## 2) Python-Version prüfen

```bash
python3 --version
```

Erwartung: Python 3.x.

## 3) Schneller Durchlauf mit Demo-Daten

```bash
python3 tools/quiz_forcechain_demo.py --answers A,A,B,A,A,A
```

Warum diese Antwortfolge?
- `Q001`: A = falsch -> Sprung zu `Q001a`
- `Q001a`: A = falsch -> Sprung zu `Q001b`
- `Q001b`: B = richtig -> zurück in den normalen Flow (`Q002`)

## 4) Ergebnis maschinell verifizieren (wichtig)

```bash
python3 tools/quiz_forcechain_demo.py \
  --answers A,A,B,A,A,A \
  --expect-path Q001,Q001a,Q001b,Q002,Q002a
```

Wenn alles stimmt, endet der Befehl mit:
- `Pfadprüfung: OK -> ...`
- Exit-Code `0`

Wenn der Pfad falsch ist, zeigt das Tool `Pfadprüfung: FEHLER` und endet mit Exit-Code `1`.

## 5) Deine eigene CSV testen

```bash
python3 tools/quiz_forcechain_demo.py \
  --csv /mnt/data/quiz100_forcechains.csv \
  --answers A,A,B,A,A,A
```

Optional mit Sollpfad:

```bash
python3 tools/quiz_forcechain_demo.py \
  --csv /mnt/data/quiz100_forcechains.csv \
  --answers A,A,B,A,A,A \
  --expect-path Q001,Q001a,Q001b,Q002,Q002a
```

## 6) Direkt in einer Alternativfrage starten (force_id-Verhalten)

```bash
python3 tools/quiz_forcechain_demo.py --start-id Q001a --answers A,B
```

Das simuliert den Fall, dass dein Backend bereits `force_id=Q001a` gesetzt hat.

## 7) Häufige Fehler und klare Lösung

- **Fehler:** `CSV-Header unvollständig`
  - **Lösung:** Header muss genau so heißen:
    - `question_id,prompt,option_a,option_b,option_c,correct_option,alt_question_id`
- **Fehler:** `ValueError: 'D' is not in list`
  - **Lösung:** Antworten nur A/B/C verwenden.
- **Fehler:** Kein Sprung zur Alternative
  - **Lösung:** Prüfe in der CSV, ob `alt_question_id` exakt auf existierende `question_id` zeigt.

## 8) Was als "bestanden" gilt

Du hast die Demo korrekt validiert, wenn:
1. Falsche Antworten bei Primärfragen in `alt_question_id` springen.
2. Nach Ende der Kette (z. B. `Q001b` ohne `alt_question_id`) wieder normal weitergegangen wird.
3. `--expect-path` mit Exit-Code 0 bestätigt.
