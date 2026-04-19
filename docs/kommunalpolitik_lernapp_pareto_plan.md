# Lernapp-Blueprint (Pareto) für kommunalpolitische Anfragen & Anträge

## 1) Harte Gegenposition zuerst

Die Idee "PDF/DOC scannen + sofort auf dem Handy lernen" klingt gut, ist aber in der Praxis oft zu groß als erster Schritt:

- OCR + semantische Extraktion + gutes Quiz-Design sind drei getrennte Probleme.
- Wenn du alles gleichzeitig baust, verlierst du Wochen an Technik statt Lernfortschritt.
- Pareto bedeutet hier: zuerst Lernwirkung sichern, dann Technik verfeinern.

## 2) Präzises 80/20-Ziel

**Lernziel in 6 Wochen:**
Du kannst aus 80 % der typischen kommunalen Vorgänge in <15 Minuten einen brauchbaren Entwurf für Anfrage oder Antrag erstellen.

**Nicht-Ziel am Anfang:**
Perfekte Vollautomatik für jedes beliebige Dokumentformat.

## 3) Was dein Inputtext richtig macht (und was fehlt)

### Stärken
- Klarer Fokus auf **Bürgernähe, Verständlichkeit, Wertekompass**.
- Gute Strukturbausteine (AIDA, klare Botschaft, Nutzen, Call-to-Action).
- Kettenlernen (Q -> Q001a -> Q001b) ist didaktisch stark.

### Lücken
- Keine harte Trennung zwischen **Anfrage-Logik** und **Antrag-Logik**.
- Kein Bewertungssystem (wann ist ein Entwurf "gut genug"?).
- Kein Minimal-Datenmodell für Dokumentanalyse.

## 4) Minimaler Produktkern (MVP)

### Funktionen, die du wirklich brauchst
1. **Dokumentimport** (PDF, DOCX)
2. **Text-Extraktion**
3. **Segmentierung** in Abschnitte (Problem, Fakten, Rechtsbezug, Forderung)
4. **Quiz mit Force-Ketten** für Wiederholung bei Fehlern
5. **2 Generatoren**:
   - Entwurf "Anfrage"
   - Entwurf "Antrag"

### Funktionen, die warten können
- Perfekte OCR für schlechte Scans
- Mehrsprachigkeit
- Komplexes Rollen-/Nutzer-Management
- Vollautomatische juristische Prüfung

## 5) Datenmodell (einfach und stabil)

```text
Document(id, title, source_type, raw_text)
Chunk(id, document_id, section_type, text)
Question(id, topic, level, prompt, answer_a, answer_b, answer_c, correct, alt_question_id)
Attempt(id, user_id, question_id, result, timestamp)
Template(id, type=[anfrage|antrag], skeleton)
Draft(id, user_id, template_id, input_chunks, output_text)
```

## 6) Lernlogik mit Force-Ketten (dein starker Hebel)

- Erste falsche Antwort -> alternative Frage A (`Q001a`)
- Zweite falsche Antwort -> alternative Frage B (`Q001b`)
- Danach Rückkehr in normalen Flow

**Regel:** gleiche Kompetenz, andere Formulierung.
So lernst du "Prinzip statt Auswendiglernen".

## 7) Prompt-/Textregeln für deinen Stil ("Franz-Stimme")

1. Klar, direkt, keine Behördenfloskeln.
2. Jede Aussage braucht Begründung oder Beispiel aus der Kommune.
3. Erst Einwand/Gegenargument, dann Position.
4. Keine künstliche Freundlichkeit.
5. Schluss immer mit konkreter nächster Handlung.

## 8) Schritt-für-Schritt-Umsetzung

### Schritt 1 (Woche 1): Lernkorpus bauen
- Sammle 30 echte Vorgänge (15 Anfragen, 15 Anträge).
- Markiere manuell pro Dokument:
  - Anlass
  - Rechts-/Sachbezug
  - Kernforderung
  - Begründung
  - erwartete Wirkung

### Schritt 2 (Woche 2): 80/20-Quiz erstellen
- 100 Fragen total:
  - 40 Strukturfragen
  - 30 Formulierungsfragen
  - 20 Rechts-/Prozessfragen
  - 10 typische Fehler
- Für 20 Kernfragen Force-Ketten hinzufügen.

### Schritt 3 (Woche 3): Import-Pipeline
- PDF: `pypdf` für digitale PDFs, OCR nur wenn nötig.
- DOCX: `python-docx`.
- Ergebnis als Chunks speichern.

### Schritt 4 (Woche 4): Generatoren
- Generator A: Anfrage (Fragenblock + Begründung + Bitte um Auskunft)
- Generator B: Antrag (Beschlussvorschlag + Begründung + Finanzierung/Umsetzung)
- Immer mit "Kritik-Check" vor Ausgabe:
  - unklare Begriffe?
  - unbelegte Behauptungen?
  - fehlender Nutzen für Bürger?

### Schritt 5 (Woche 5): Mobile Oberfläche
- Start simpel: Web-App (PWA) statt native App.
- 3 Screens genügen:
  1. Dokument hochladen
  2. Quiz trainieren
  3. Entwurf erzeugen

### Schritt 6 (Woche 6): Messung
- KPI 1: Trefferquote im Quiz (Ziel >75 %)
- KPI 2: Zeit bis erstem brauchbaren Entwurf
- KPI 3: Anzahl nötiger Korrekturschleifen

## 9) Qualitätscheckliste für jeden erzeugten Text

- Ist der Adressat klar benannt?
- Ist das Problem mit konkreten lokalen Fakten beschrieben?
- Ist die Forderung als prüfbarer Satz formuliert?
- Ist die Begründung logisch in Ursache -> Wirkung aufgebaut?
- Ist der Nutzen für Bürger explizit genannt?
- Gibt es eine realistische Umsetzungs-/Finanzierungsperspektive?

## 10) Realistische nächste Entscheidung (jetzt)

Entscheide zuerst nur diese drei Punkte:
1. **MVP nur Web-PWA?** (empfohlen)
2. **Nur digitale PDFs/DOCX in Phase 1?** (empfohlen)
3. **Start mit 30 Dokumenten statt 300?** (empfohlen)

Wenn du diese drei Entscheidungen triffst, ist das Projekt umsetzbar.
Wenn nicht, bleibt es wahrscheinlich eine Dauerbaustelle.

## 11) Soforttest lokal (5 Minuten)

### A) Demo ausführen

```bash
python3 tools/quiz_forcechain_demo.py --answers B,B,B,B,B,A
```

Was du sehen solltest:
- Bei `Q001` falsch -> Sprung zu `Q001a`
- Wieder falsch -> Sprung zu `Q001b`
- Danach normal weiter zu `Q002`

### B) Mit eigener CSV testen

```bash
python3 tools/quiz_forcechain_demo.py --csv /pfad/zu/deiner/quiz100_forcechains.csv
```

### C) Direkt in eine Alternative springen (wie `force_id`)

```bash
python3 tools/quiz_forcechain_demo.py --start-id Q001a --answers B,B
```

Damit kannst du die Force-Kette exakt so testen, wie sie später in Opal/Apps Script laufen soll.
