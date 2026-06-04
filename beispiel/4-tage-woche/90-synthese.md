# 🔵 Blau — Abschluss: Synthese & Entscheidungsvorlage

Der blaue Hut führt alle Perspektiven zusammen und formuliert eine Empfehlung —
gemessen an den Entscheidungskriterien aus `00-problem.md`.

## Problemklärung

Die Frage „4-Tage-Woche ja/nein?" ist in dieser Schärfe nicht entscheidbar: Nutzen
(Recruiting, Bindung) und Risiken (Produktivität, Kundenabwanderung, Verdichtung)
sind real, aber die tragenden Annahmen (F3, F5) und die zentrale Wissenslücke (F6,
Kundenreaktion) sind unbelegt. Die eigentliche Entscheidung lautet daher: **Wie
testen wir das Modell risikoarm und datenbasiert, bevor wir unternehmensweit
umstellen?**

## Faktenlage (kurz)

- Externe Pilotdaten deuten auf stabile Produktivität (F1) — aber nicht branchenspezifisch.
- Fluktuation mit 14 % über Branchenschnitt (F2) → realer Handlungsdruck.
- Verdichtbarkeit (F3) und nötiger Produktivitätssprung (F5) sind **Annahmen**.
- Service-Erreichbarkeit Mo–Fr 08–18 Uhr ist harte Constraint (F4).
- Kundenreaktion ist **unbekannt** (F6).

## Top-Ideen

- **I7** — Pilot mit verbindlichen Produktivitäts-Metriken
- **I4** — Service-Rotationspilot (sichert Erreichbarkeit)
- **I1** — Vollumstellung (Zielbild, noch nicht jetzt)

## Pro / Contra

| Pro (Gelb) | Contra (Schwarz) |
|------------|------------------|
| N3: Pilot schließt Annahmen F3/F5 und Lücke F6 | R5: Pilot evtl. nicht repräsentativ |
| N4: Erreichbarkeit via Rotation gewahrt | R4: Rotationsplanung anfällig für Engpässe |
| N7: volle Reversibilität | R6: Neid zwischen Pilot-/Nicht-Pilot-Teams |
| N1/N5/N8: Recruiting, Bindung, Wettbewerb (bei I1) | R1/R2/R7: Produktivitätseinbruch, Kundenabwanderung, Überlastung (bei I1) |

## Emotionale Signale

- Mitarbeitende: starke Begeisterung (E1), zugleich Sorge vor Verdichtung (E2).
- GF: gemischt — Zuversicht (E3) und Nervosität (E4).
- Kunden: skeptisch bzgl. Erreichbarkeit (E5).
- HR: stark motiviert (E6), respektiert aber den Aufwand (E7).

## Empfehlung

**Keine sofortige Vollumstellung. Stattdessen 6-Monats-Pilot nach I7, kombiniert mit
dem Service-Rotationsmodell I4.** Damit werden die schweren I1-Risiken (R1, R2, R7)
vermieden, die positive Mitarbeiterstimmung (E1) genutzt und über verbindliche
Metriken (N3) eine belastbare Grundlage für die spätere Go/No-Go-Entscheidung zur
Vollumstellung (I1) geschaffen.

## Offene Risiken

- R5 (Repräsentativität): durch gemischte, nicht nur freiwillige Pilotteams mindern.
- R6 (Fairness): transparenter Ausrollpfad und offene Kommunikation von Beginn an.
- R4 (Service-Engpässe): Vertretungs- und Krankheitspuffer im Rotationsplan einplanen.

## Nächste Schritte

1. Pilot-Design festlegen: zwei gemischte Abteilungen inkl. Kundenservice, 6 Monate.
2. Metriken vorab definieren (Produktivität, Servicelevel, Reaktionszeit, Zufriedenheit, Fluktuation).
3. Rotationsplan für die 08–18-Uhr-Abdeckung ausarbeiten (I4) inkl. Puffer.
4. Kommunikationsplan für Mitarbeitende (E1/E2) und Kunden (E5) erstellen.
5. Go/No-Go-Kriterien und Auswertungstermin nach 6 Monaten verbindlich festhalten.

## Iteration nötig?

**Ja** — nach Abschluss des Pilots erfolgt ein zweiter DENKHUT-6-Durchlauf mit den
realen Pilotdaten, um über die Vollumstellung (I1) zu entscheiden.

```json
{
  "hut": "blau",
  "phase_nr": 7,
  "zusammenfassung": "Abschließende Synthese: Empfehlung für einen metrikgestützten 6-Monats-Pilot (I7) mit Service-Rotation (I4) statt sofortiger Vollumstellung (I1). Damit werden die schwersten Risiken vermieden und eine belastbare Datenbasis für eine spätere Entscheidung geschaffen.",
  "eintraege": [
    {
      "problemklaerung": "Nicht 'ob' die 4-Tage-Woche, sondern wie sie risikoarm und datenbasiert getestet wird, bevor unternehmensweit umgestellt wird. Tragende Annahmen (F3, F5) und die Wissenslücke zur Kundenreaktion (F6) sind unbelegt.",
      "fakten_kurz": [
        "Externe Pilotdaten deuten auf stabile Produktivität (F1), aber nicht branchenspezifisch.",
        "Fluktuation 14 % über Branchenschnitt (F2) → realer Handlungsdruck.",
        "Verdichtbarkeit (F3) und nötiger Produktivitätssprung (F5) sind nur Annahmen.",
        "Service-Erreichbarkeit Mo-Fr 08-18 Uhr ist harte Constraint (F4).",
        "Kundenreaktion ist unbekannt (F6)."
      ],
      "top_ideen": ["I7", "I4", "I1"],
      "pro": [
        "N3: Pilot schließt die Annahmen F3/F5 und die Wissenslücke F6.",
        "N4: Erreichbarkeit bleibt durch Rotation (I4) gewahrt.",
        "N7: Pilot ist voll reversibel, kein Gesichtsverlust.",
        "N1/N5/N8: Recruiting-, Bindungs- und Wettbewerbsvorteile bei späterer Vollumstellung (I1)."
      ],
      "contra": [
        "R1/R2/R7: Vollumstellung (I1) birgt Produktivitätseinbruch, Kundenabwanderung und Überlastung.",
        "R5: Pilot könnte nicht repräsentativ sein.",
        "R4: Rotationsplanung im Service ist engpassanfällig.",
        "R6: Neid zwischen Pilot- und Nicht-Pilot-Teams."
      ],
      "emotionale_signale": [
        "Mitarbeitende stark begeistert (E1), aber besorgt wegen Verdichtung (E2).",
        "Geschäftsführung gemischt: Zuversicht (E3) und Nervosität (E4).",
        "Kunden skeptisch bzgl. Erreichbarkeit (E5).",
        "HR stark motiviert (E6), respektiert den Aufwand (E7)."
      ],
      "empfehlung": "Keine sofortige Vollumstellung (I1). Stattdessen 6-Monats-Pilot nach I7, kombiniert mit dem Service-Rotationsmodell I4, mit verbindlichen Metriken als Grundlage für eine spätere Go/No-Go-Entscheidung.",
      "offene_risiken": [
        "R5 Repräsentativität: durch gemischte statt nur freiwillige Pilotteams mindern.",
        "R6 Fairness: transparenter Ausrollpfad und offene Kommunikation.",
        "R4 Service-Engpässe: Vertretungs- und Krankheitspuffer einplanen."
      ],
      "naechste_schritte": [
        "Pilot-Design festlegen: zwei gemischte Abteilungen inkl. Kundenservice, 6 Monate.",
        "Metriken vorab definieren (Produktivität, Servicelevel, Reaktionszeit, Zufriedenheit, Fluktuation).",
        "Rotationsplan für die 08-18-Uhr-Abdeckung ausarbeiten (I4) inkl. Puffer.",
        "Kommunikationsplan für Mitarbeitende (E1/E2) und Kunden (E5) erstellen.",
        "Go/No-Go-Kriterien und Auswertungstermin nach 6 Monaten verbindlich festhalten."
      ],
      "iteration_noetig": true
    }
  ],
  "offene_punkte": [
    "Zweiter DENKHUT-6-Durchlauf nach Pilotende mit realen Daten zur Entscheidung über I1."
  ],
  "konfidenz": "hoch"
}
```
