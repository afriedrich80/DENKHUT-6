---
name: denkhut-protokoll
description: Audit-Logging der "Denkspur" einer DENKHUT-6-Sitzung. Nutze dies, wenn ein "Protokoll" geführt, ein "Audit"-Trail erstellt, die "Denkspur" dokumentiert oder die Sitzung "nachvollziehbar"/revisionssicher gemacht werden soll.
---

# DENKHUT-6 · Protokoll (Audit-Trail)

Jede Sitzung erzeugt eine lückenlose **Denkspur**: Wer (welcher Hut) hat wann auf welcher Grundlage was beigetragen. Der Blaue Hut führt das Protokoll nach jeder Phase fort.

## Warum Logging
- **Governance & Nachvollziehbarkeit:** Eine Entscheidung lässt sich später bis auf die einzelnen Denkschritte zurückverfolgen – wer welche Fakten, Risiken und Chancen wann eingebracht hat.
- **Revisions-/MaRisk-Tauglichkeit:** Im regulierten Umfeld (z. B. Banken) müssen Entscheidungswege dokumentiert und prüfbar sein. Das Protokoll liefert genau diesen nachvollziehbaren Audit-Trail.
- **Iteration & Qualität:** Bei zweiten Runden ist sichtbar, welcher Befund welche Folge-Aktion ausgelöst hat.

## Aufbau eines Protokoll-Eintrags (Logeintrag)
Pro abgeschlossener Phase ein Eintrag mit den Feldern:

| Feld | Bedeutung |
|------|-----------|
| `schritt_nr` | Laufende Nummer der Phase (1, 2, 3 …) |
| `hut` | Welcher Hut aktiv war (weiss/rot/schwarz/gelb/gruen/blau) |
| `zeit` | Zeitstempel des Abschlusses |
| `input_referenz` | Worauf sich der Hut stützte (z. B. `00-problem.md`, `10-weiss.md`, `20-gruen.md`) |
| `output_referenz` | Wo das Ergebnis liegt (z. B. `30-gelb.md`) |

## Wann schreiben
**Nach jeder Phase** wird der Eintrag angehängt – unmittelbar nachdem der Hut-Output gesichert wurde. Bei parallel gespawnten Hüten (Gelb/Schwarz) je ein eigener Eintrag, mit identischer `input_referenz`, aber eigener `schritt_nr` und `output_referenz`.

## Ablage
Datei `protokoll.md` im Sitzungsordner `denkhut-sitzungen/<slug>/`. Struktur nach Vorlage `templates/sitzungsprotokoll.md`. Zu Sitzungsbeginn (Blau-Eröffnung) initialisieren, danach fortlaufend ergänzen.

## Beispiel
```markdown
# Protokoll · Sitzung: 4-tage-woche

| schritt_nr | hut     | zeit             | input_referenz            | output_referenz |
|------------|---------|------------------|---------------------------|-----------------|
| 1          | blau    | 2026-06-04 09:00 | –                         | 00-problem.md   |
| 2          | weiss   | 2026-06-04 09:12 | 00-problem.md             | 10-weiss.md     |
| 3          | gruen   | 2026-06-04 09:28 | 00-problem.md, 10-weiss.md| 20-gruen.md     |
| 4          | gelb    | 2026-06-04 09:41 | 10-weiss.md, 20-gruen.md  | 30-gelb.md      |
| 5          | schwarz | 2026-06-04 09:41 | 10-weiss.md, 20-gruen.md  | 40-schwarz.md   |
| 6          | rot     | 2026-06-04 09:55 | 20-gruen.md               | 50-rot.md       |
| 7          | blau    | 2026-06-04 10:10 | alle                      | 90-synthese.md  |
```
Schritte 4 und 5 (Gelb/Schwarz) liefen parallel – erkennbar an identischer `zeit` und `input_referenz`.
