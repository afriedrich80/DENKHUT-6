# 🟢 Grün — Ideen & Optionen

Der grüne Hut erzeugt Möglichkeiten — ohne Bewertung. Bewusst werden sowohl
naheliegende als auch ungewöhnliche Varianten und Kombinationen gesammelt.

## Ideen

| ID | Titel | Typ | Baut auf |
|----|-------|-----|----------|
| I1 | Vollumstellung 4×38 h auf 4×34 h | neu | – |
| I2 | 6-Monats-Pilot in zwei Abteilungen | neu | – |
| I3 | Rollierender freier Tag (Team-Rotation) | neu | – |
| I4 | Pilot mit Rotationsmodell im Kundenservice | kombination | I2, I3 |
| I5 | Freitag als „Fokus-/Kurztag" statt freiem Tag | variante | I1 |
| I6 | Wahlmodell: 4-Tage-Woche optional pro MA | neu | – |
| I7 | Pilot + verbindliche Produktivitäts-Metriken | kombination | I2 |
| I8 | Stufenplan: erst 4,5 Tage, dann 4 Tage | variante | I1 |

## Beschreibungen

- **I1 – Vollumstellung:** Unternehmensweit von 5×38 h auf 4×34 h ohne Lohnkürzung;
  alle Mitarbeitenden arbeiten an vier festen Tagen bei gleichem Gehalt.
- **I2 – 6-Monats-Pilot:** Test in zwei freiwilligen Abteilungen, danach Auswertung
  und Go/No-Go.
- **I3 – Rollierender freier Tag:** Nicht alle frei am selben Tag; Teams verteilen
  den freien Tag über die Woche, sodass durchgehend besetzt bleibt.
- **I4 – Service-Rotationspilot:** Kombiniert Pilot (I2) mit Rotation (I3) speziell
  für den Kundenservice, um Erreichbarkeit Mo–Fr 08–18 Uhr zu sichern.
- **I5 – Fokus-Kurztag:** Statt freiem Tag ein verkürzter, meetingfreier Freitag;
  Variante von I1, bei der der fünfte Tag erhalten, aber verkürzt bleibt.
- **I6 – Wahlmodell:** Jede/r entscheidet individuell zwischen 4 und 5 Tagen;
  das Modell wird pro Mitarbeiter:in gewählt.
- **I7 – Pilot mit Metriken:** Pilot (I2) ergänzt um verbindliche Kennzahlen
  (Produktivität, Servicelevel, Zufriedenheit) als Entscheidungsgrundlage.
- **I8 – Stufenplan:** Schrittweise 5 → 4,5 → 4 Tage, um Organisation mitzunehmen.

```json
{
  "hut": "gruen",
  "phase_nr": 3,
  "zusammenfassung": "Acht Optionen von der Vollumstellung (I1) über pilothafte und rollierende Modelle (I2-I4, I7) bis zu Varianten mit verkürztem oder gestuftem Übergang (I5, I6, I8). Mehrere Ideen kombinieren Pilot und Rotation und beziehen die Service-Constraint aus F4 ein.",
  "eintraege": [
    {
      "id": "I1",
      "titel": "Vollumstellung 4×38 h auf 4×34 h",
      "beschreibung": "Unternehmensweite Umstellung von fünf auf vier Arbeitstage ohne Lohnkürzung; alle Mitarbeitenden arbeiten an vier festen Tagen bei gleichem Gehalt.",
      "typ": "neu",
      "basiert_auf": []
    },
    {
      "id": "I2",
      "titel": "6-Monats-Pilot in zwei Abteilungen",
      "beschreibung": "Befristeter Test in zwei freiwilligen Abteilungen mit anschließender Auswertung und Go/No-Go-Entscheidung.",
      "typ": "neu",
      "basiert_auf": []
    },
    {
      "id": "I3",
      "titel": "Rollierender freier Tag (Team-Rotation)",
      "beschreibung": "Der freie Tag wird innerhalb der Teams über die Woche verteilt, sodass das Unternehmen durchgehend besetzt bleibt.",
      "typ": "neu",
      "basiert_auf": []
    },
    {
      "id": "I4",
      "titel": "Pilot mit Rotationsmodell im Kundenservice",
      "beschreibung": "Kombination aus Pilot (I2) und Rotation (I3) speziell für den Kundenservice, um die Erreichbarkeit Mo-Fr 08-18 Uhr (F4) abzusichern.",
      "typ": "kombination",
      "basiert_auf": ["I2", "I3"]
    },
    {
      "id": "I5",
      "titel": "Freitag als Fokus-/Kurztag",
      "beschreibung": "Statt eines freien Tages ein verkürzter, meetingfreier Freitag. Variante der Vollumstellung (I1), bei der der fünfte Tag erhalten, aber verkürzt bleibt.",
      "typ": "variante",
      "basiert_auf": ["I1"]
    },
    {
      "id": "I6",
      "titel": "Wahlmodell: 4-Tage-Woche optional pro Mitarbeiter",
      "beschreibung": "Jede/r entscheidet individuell für 4 oder 5 Tage; das Arbeitszeitmodell wird pro Mitarbeiter:in gewählt.",
      "typ": "neu",
      "basiert_auf": []
    },
    {
      "id": "I7",
      "titel": "Pilot mit verbindlichen Produktivitäts-Metriken",
      "beschreibung": "Pilot (I2), ergänzt um verbindliche Kennzahlen für Produktivität, Servicelevel und Mitarbeiterzufriedenheit. Bezieht die Annahmen F3/F5 und die Wissenslücke F6 ein.",
      "typ": "kombination",
      "basiert_auf": ["I2"]
    },
    {
      "id": "I8",
      "titel": "Stufenplan 5 → 4,5 → 4 Tage",
      "beschreibung": "Schrittweise Reduktion über mehrere Quartale (5 → 4,5 → 4 Tage). Variante der Vollumstellung (I1) mit gestuftem Übergang.",
      "typ": "variante",
      "basiert_auf": ["I1"]
    }
  ],
  "offene_punkte": [
    "Kombinationen aus I3 (Rotation) und I8 (Stufenplan) sind noch nicht ausgearbeitet.",
    "Weitere Branchen-Analogien zu erprobten Arbeitszeitmodellen sind noch ungenutzt."
  ],
  "konfidenz": "hoch"
}
```
