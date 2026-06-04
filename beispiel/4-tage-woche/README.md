# Beispielsitzung: „Sollen wir eine 4-Tage-Woche einführen?"

Diese Sitzung zeigt einen **vollständigen Durchlauf** von DENKHUT-6 an einer realen
Geschäftsführungs-Frage: Soll ein mittelständisches Unternehmen (~120 Mitarbeitende)
eine 4-Tage-Woche einführen?

## Was dieses Beispiel zeigt

- Wie jeder Hut einen **eigenen, typisierten Output-Envelope** erzeugt.
- Wie spätere Hüte über IDs **rückbezogen** auf die Grün-Ideen arbeiten
  (`bezug_idee`, `basiert_auf`).
- Wie der blaue Hut am Ende alles zu einer **Entscheidungsvorlage (Synthese)**
  zusammenführt.
- Wie ein **Audit-Protokoll** die gesamte Denkspur nachvollziehbar macht.

## Gewählte Sequenz: `entscheidung` (Default)

```
blau → weiss → gruen → gelb → schwarz → rot → blau
```

Begründung: Erst Rahmen setzen (blau), dann Faktenbasis (weiss), dann Optionen
erzeugen (gruen), diese bewerten (gelb/schwarz), die emotionale Lage erfassen (rot)
und abschließend entscheiden (blau). Gelb und Schwarz wurden **parallel** auf
denselben Ideensatz angewendet.

## Dateien & Reihenfolge zum Nachvollziehen

| # | Datei | Hut | Inhalt |
|---|-------|-----|--------|
| 1 | `00-problem.md` | blau | Problem, Ziel, Scope, Constraints, Stakeholder, Kriterien, Sequenz |
| 2 | `10-weiss.md` | weiss | Fakten, Annahmen, Wissenslücken (F1…) |
| 3 | `20-gruen.md` | gruen | Lösungsideen (I1…) |
| 4 | `30-gelb.md` | gelb | Nutzenpunkte zu den Top-Ideen (N1…) |
| 5 | `40-schwarz.md` | schwarz | Risiken zu denselben Ideen (R1…) |
| 6 | `50-rot.md` | rot | Emotionen je Stakeholder (E1…) |
| 7 | `90-synthese.md` | blau | Entscheidungsvorlage / Synthese |
| – | `protokoll.md` | – | Audit-Protokoll der gesamten Denkspur |

## ID-Konventionen

- **F** = Fakt (weiss), **I** = Idee (gruen), **N** = Nutzen (gelb),
  **R** = Risiko (schwarz), **E** = Emotion (rot).
- Gelb, Schwarz und die Synthese verweisen per `bezug_idee` / `basiert_auf` auf
  die Grün-Ideen, sodass die Argumentationskette lückenlos bleibt.

## Stakeholder

Geschäftsführung · Mitarbeitende · Kunden · HR

## So liest man eine Phasendatei

Jede Datei besteht aus **lesbarem Markdown** (für Menschen) und einem abschließenden
` ```json `-Block (für Maschinen), der exakt dem Hut-Output-Envelope
(`schemas/hut-output.schema.json`) entspricht.
