# DATENMODELL

> Technische Spezifikation der Datenstrukturen von DENKHUT-6. Maßgeblich für Agents, Skills und alle Outputs. Die formalen JSON-Schemas liegen in [`schemas/`](schemas/).

Alle Feldnamen sind **verbindlich** und exakt so zu verwenden. Enum-Werte sind kleingeschrieben und ohne Umlaut-Sonderbehandlung (z. B. `wissensluecke`).

## Hut-Output-Envelope

Jeder Hut-Subagent liefert genau diesen Umschlag zurück. Die eigentlichen Inhalte stehen in `eintraege[]` (je nach Hut vom passenden Eintrags-Typ).

| Feld | Typ | Beschreibung | erlaubte Werte |
|------|-----|--------------|----------------|
| `hut` | string | welcher Hut | `weiss`, `rot`, `schwarz`, `gelb`, `gruen`, `blau` |
| `phase_nr` | integer | Schrittnummer in der Sequenz | ≥ 0 |
| `zusammenfassung` | string | 1–3 Sätze Kernaussage des Huts | frei |
| `eintraege` | array | typisierte Beiträge (s. u.) | Fakt / Idee / Emotion / Nutzenpunkt / Risiko |
| `offene_punkte` | string[] | was offen bleibt / an Blau zurückgeht | frei |
| `konfidenz` | string | Selbsteinschätzung der Sicherheit | `hoch`, `mittel`, `niedrig` |

> Der Blaue Hut liefert statt `eintraege[]` ein `Synthese`-Objekt (s. u.), behält aber `hut`, `phase_nr`, `zusammenfassung`, `offene_punkte`, `konfidenz`.

## Entity: Fakt (Weißer Hut)

| Feld | Typ | Beschreibung | erlaubte Werte |
|------|-----|--------------|----------------|
| `id` | string | eindeutige ID (z. B. `F1`) | frei |
| `aussage` | string | die faktische Aussage | frei |
| `typ` | string | Faktenstatus | `fakt`, `annahme`, `wissensluecke` |
| `quelle` | string | Herkunft / Beleg (oder „—") | frei |
| `konfidenz` | string | Sicherheit der Aussage | `hoch`, `mittel`, `niedrig` |

## Entity: Idee (Grüner Hut)

| Feld | Typ | Beschreibung | erlaubte Werte |
|------|-----|--------------|----------------|
| `id` | string | eindeutige ID (z. B. `I1`) | frei |
| `titel` | string | Kurzbezeichnung | frei |
| `beschreibung` | string | Ausführung der Idee | frei |
| `typ` | string | Art der Idee | `neu`, `variante`, `kombination` |
| `basiert_auf` | string[] | IDs anderer Ideen/Fakten als Basis | IDs (oder leer) |

## Entity: Emotion (Roter Hut)

| Feld | Typ | Beschreibung | erlaubte Werte |
|------|-----|--------------|----------------|
| `id` | string | eindeutige ID (z. B. `E1`) | frei |
| `stakeholder` | string | wessen Gefühl | frei |
| `gefuehl` | string | das Gefühl (ohne Begründung) | frei |
| `intensitaet` | string | Stärke | `stark`, `mittel`, `schwach` |
| `richtung` | string | Tendenz | `positiv`, `negativ`, `gemischt` |
| `bezug` | string | worauf es sich bezieht (Idee/Thema) | frei |

## Entity: Nutzenpunkt (Gelber Hut)

| Feld | Typ | Beschreibung | erlaubte Werte |
|------|-----|--------------|----------------|
| `id` | string | eindeutige ID (z. B. `N1`) | frei |
| `nutzen` | string | der Vorteil / Wert | frei |
| `bezug_idee` | string | ID der betroffenen Idee | IDs |
| `bedingung` | string | Erfolgsbedingung für den Nutzen | frei |
| `wirkungshorizont` | string | wann der Nutzen wirkt | `kurz`, `mittel`, `lang` |

## Entity: Risiko (Schwarzer Hut)

| Feld | Typ | Beschreibung | erlaubte Werte |
|------|-----|--------------|----------------|
| `id` | string | eindeutige ID (z. B. `R1`) | frei |
| `risiko` | string | die Gefahr / Schwäche | frei |
| `bezug_idee` | string | ID der betroffenen Idee | IDs |
| `ursache` | string | Begründung / Ursache des Risikos | frei |
| `eintrittswahrscheinlichkeit` | string | wie wahrscheinlich | `hoch`, `mittel`, `niedrig` |
| `auswirkung` | string | wie schwer der Schaden | `hoch`, `mittel`, `niedrig` |
| `gegenmassnahme_moeglich` | boolean | ob eine Gegenmaßnahme denkbar ist | `true`, `false` |

## Entity: Synthese (Blauer Hut)

| Feld | Typ | Beschreibung | erlaubte Werte |
|------|-----|--------------|----------------|
| `problemklaerung` | string | präzise gefasstes Problem | frei |
| `fakten_kurz` | string[] | wichtigste Fakten | frei |
| `top_ideen` | string[] | beste Ideen (IDs/Titel) | frei |
| `pro` | string[] | zentrale Nutzenargumente | frei |
| `contra` | string[] | zentrale Gegenargumente | frei |
| `emotionale_signale` | string[] | relevante emotionale Reaktionen | frei |
| `empfehlung` | string | begründete Empfehlung | frei |
| `offene_risiken` | string[] | ungelöste Risiken | frei |
| `naechste_schritte` | string[] | konkrete nächste Schritte | frei |
| `iteration_noetig` | boolean | ob eine weitere Runde nötig ist | `true`, `false` |

## Entity: Logeintrag (Protokoll)

| Feld | Typ | Beschreibung | erlaubte Werte |
|------|-----|--------------|----------------|
| `schritt_nr` | integer | laufende Schrittnummer | ≥ 0 |
| `hut` | string | welcher Hut aktiv war | `weiss`, `rot`, `schwarz`, `gelb`, `gruen`, `blau` |
| `zeit` | string | Zeitstempel (ISO 8601) | frei |
| `input_referenz` | string | worauf der Hut sich stützte | frei |
| `output_referenz` | string | erzeugter Output (Datei/IDs) | frei |

## Entity: Sitzung (Container)

| Feld | Typ | Beschreibung | erlaubte Werte |
|------|-----|--------------|----------------|
| `sitzung_id` | string | eindeutige Sitzungs-ID | frei |
| `titel` | string | Titel der Sitzung | frei |
| `erstellt_am` | string | Zeitstempel (ISO 8601) | frei |
| `problem` | object | Problem-Objekt (s. u.) | — |
| `sequenz` | string[] | gewählte Hut-Reihenfolge | Hut-Namen |
| `fakten` | Fakt[] | gesammelte Fakten | — |
| `ideen` | Idee[] | gesammelte Ideen | — |
| `emotionen` | Emotion[] | gesammelte Emotionen | — |
| `nutzen` | Nutzenpunkt[] | gesammelte Nutzenpunkte | — |
| `risiken` | Risiko[] | gesammelte Risiken | — |
| `synthese` | Synthese | Schluss-Synthese | — |
| `protokoll` | Logeintrag[] | Ablaufprotokoll | — |

### Sub-Objekt: `problem`

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `beschreibung` | string | das Problem in Worten |
| `ziel` | string | angestrebtes Ergebnis |
| `scope` | string | Geltungsbereich / Abgrenzung |
| `constraints` | string[] | Rahmenbedingungen |
| `stakeholder` | string[] | beteiligte / betroffene Gruppen |
| `entscheidungskriterien` | string[] | woran die Entscheidung gemessen wird |

## Kontextflüsse: Wer liest welche Vor-Outputs

Der Blaue Hut gibt jedem Hut nur den jeweils **relevanten** Vor-Kontext. So bleibt jeder Modus fokussiert und unvoreingenommen.

| Hut | liest als Input | erzeugt |
|-----|-----------------|---------|
| 🔵 Blau (Start) | Roh-Thema des Nutzers | `problem`, `sequenz` |
| ⚪ Weiß | `problem` | `fakten[]` |
| 🟢 Grün | `problem`, `fakten[]` | `ideen[]` |
| 🟡 Gelb | `problem`, `ideen[]` (nicht Risiken!) | `nutzen[]` |
| ⚫ Schwarz | `problem`, `ideen[]` (nicht Nutzen!) | `risiken[]` |
| 🔴 Rot | `problem`, `ideen[]` (knapp; **keine** Pro/Contra) | `emotionen[]` |
| 🔵 Blau (Ende) | **alle** Outputs | `synthese`, `protokoll[]` |

**Wichtig:** Gelb und Schwarz erhalten dieselbe Idee-Liste, aber *nicht* die Ausgabe des jeweils anderen – sie urteilen unabhängig. Rot erhält bewusst keine Pro/Contra-Argumente, damit das Gefühl unverfälscht bleibt.

## Sequenzen

| Sequenz | Reihenfolge | Einsatz |
|---------|-------------|---------|
| `entscheidung` (Default) | blau → weiss → gruen → gelb → schwarz → rot → blau | umfassende Entscheidungen |
| `bewertung` | blau → rot → weiss → gelb → schwarz → gruen → blau | bestehende Option prüfen |
| `ideenfindung` | blau → weiss → gruen → rot → gelb → schwarz → blau | neue Lösungen suchen |
| `schnell-review` | blau → weiss → schwarz → gelb → blau | schnelle Plausibilitätsprüfung |

**Parallelität:** Weiß steht vor Grün/Gelb/Schwarz/Rot. Gelb und Schwarz laufen parallel. Blau steht immer zuerst und zuletzt.

## Ausgabe-Ordnerkonvention

Jede Sitzung wird unter `denkhut-sitzungen/<slug>/` abgelegt (`<slug>` = sprechender Kurzname des Themas):

```
denkhut-sitzungen/<slug>/
├── 00-problem.md      # Blau: Problemklärung
├── 10-weiss.md        # Weiß: Fakten
├── 20-gruen.md        # Grün: Ideen
├── 30-gelb.md         # Gelb: Nutzen
├── 40-schwarz.md      # Schwarz: Risiken
├── 50-rot.md          # Rot: Gefühle
├── 90-synthese.md     # Blau: Synthese & Entscheidung
└── protokoll.md       # vollständiges Ablaufprotokoll
```

Die Zehner-Nummerierung folgt der Default-Sequenz und lässt Platz für Iterationen. Generierte Sitzungen sind in `.gitignore` ausgeschlossen.

## Verweise

- Formale Schemas: [`schemas/`](schemas/)
- Output-Vorlagen: [`templates/`](templates/)
- Konzeptuelle, tool-neutrale Spec: [`CONVENTIONS.md`](CONVENTIONS.md)
