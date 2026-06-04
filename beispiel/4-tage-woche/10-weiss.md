# ⚪ Weiss — Fakten, Annahmen, Wissenslücken

Der weiße Hut sammelt ausschließlich Sachinformationen — neutral, ohne Wertung.
Jede Aussage ist als **Fakt**, **Annahme** oder **Wissenslücke** markiert und mit
einer Quelle versehen.

## Faktenlage

| ID | Typ | Aussage | Quelle | Konfidenz |
|----|-----|---------|--------|-----------|
| F1 | fakt | Mehrere Pilotprogramme (u. a. UK-4-Day-Week-Pilot 2022, 61 Firmen) berichten stabile oder leicht steigende Produktivität bei reduzierter Arbeitszeit. | Externe Studienlage / Branchenreports | mittel |
| F2 | fakt | Die durchschnittliche Fluktuation im Unternehmen liegt aktuell bei 14 % p. a., über dem Branchenschnitt von ~10 %. | Interne HR-Kennzahlen 2025 | hoch |
| F3 | annahme | Etwa 70 % der Tätigkeiten sind nicht zeitkritisch an alle fünf Werktage gebunden und ließen sich auf vier Tage verdichten. | Schätzung Teamleitungen | niedrig |
| F4 | fakt | 35 Mitarbeitende im Kundenservice müssen Mo–Fr 08–18 Uhr Erreichbarkeit absichern; das erfordert bei 4-Tage-Woche ein Schicht-/Rotationsmodell. | Interne Servicelevel-Vereinbarung | hoch |
| F5 | annahme | Eine Produktivitätssteigerung von 8–12 % je verbleibendem Arbeitstag wäre nötig, um die wegfallende Tageskapazität auszugleichen. | Interne Modellrechnung Controlling | mittel |
| F6 | wissensluecke | Es ist unbekannt, wie Kunden auf veränderte Ansprechpartner-Verfügbarkeit reagieren (Abwanderungsrisiko quantitativ unklar). | Keine Datenbasis vorhanden | niedrig |

```json
{
  "hut": "weiss",
  "phase_nr": 2,
  "zusammenfassung": "Sechs Sachaussagen zur 4-Tage-Woche: belastbare externe Produktivitätshinweise (F1) und harte interne Kennzahlen (F2, F4) stehen mehreren Annahmen (F3, F5) und einer zentralen Wissenslücke beim Kundenverhalten (F6) gegenüber.",
  "eintraege": [
    {
      "id": "F1",
      "aussage": "Mehrere Pilotprogramme (u. a. UK-4-Day-Week-Pilot 2022 mit 61 Firmen) berichten stabile oder leicht steigende Produktivität bei reduzierter Arbeitszeit.",
      "typ": "fakt",
      "quelle": "Externe Studienlage / Branchenreports",
      "konfidenz": "mittel"
    },
    {
      "id": "F2",
      "aussage": "Die durchschnittliche Fluktuation liegt aktuell bei 14 % p. a. und damit über dem Branchenschnitt von ca. 10 %.",
      "typ": "fakt",
      "quelle": "Interne HR-Kennzahlen 2025",
      "konfidenz": "hoch"
    },
    {
      "id": "F3",
      "aussage": "Rund 70 % der Tätigkeiten sind nicht zeitkritisch an alle fünf Werktage gebunden und ließen sich auf vier Tage verdichten.",
      "typ": "annahme",
      "quelle": "Schätzung der Teamleitungen",
      "konfidenz": "niedrig"
    },
    {
      "id": "F4",
      "aussage": "35 Mitarbeitende im Kundenservice müssen Mo-Fr 08-18 Uhr Erreichbarkeit absichern; eine 4-Tage-Woche erfordert dort ein Schicht-/Rotationsmodell.",
      "typ": "fakt",
      "quelle": "Interne Servicelevel-Vereinbarung",
      "konfidenz": "hoch"
    },
    {
      "id": "F5",
      "aussage": "Eine Produktivitätssteigerung von 8-12 % je verbleibendem Arbeitstag wäre nötig, um die wegfallende Tageskapazität auszugleichen.",
      "typ": "annahme",
      "quelle": "Interne Modellrechnung Controlling",
      "konfidenz": "mittel"
    },
    {
      "id": "F6",
      "aussage": "Es ist unbekannt, wie Kunden auf veränderte Ansprechpartner-Verfügbarkeit reagieren; das Abwanderungsrisiko ist quantitativ unklar.",
      "typ": "wissensluecke",
      "quelle": "Keine Datenbasis vorhanden",
      "konfidenz": "niedrig"
    }
  ],
  "offene_punkte": [
    "Offen: F3 und F5 sind Annahmen, empirische Belege liegen nicht vor.",
    "Fehlt: gemessene Daten zur Kundenreaktion (F6) sind nicht erhoben.",
    "Fehlt: branchenspezifische Vergleichsdaten statt allgemeiner Studienlage."
  ],
  "konfidenz": "mittel"
}
```
