# 🔴 Rot — Emotionen & Bauchgefühl

Der rote Hut erfasst Gefühle **ohne Begründungspflicht** — pro Stakeholder, mit
**Intensität** und **Richtung**. Hier wird nicht argumentiert, sondern wahrgenommen.

## Emotionslage

| ID | Stakeholder | Gefühl | Intensität | Richtung | Bezug |
|----|-------------|--------|-----------|----------|-------|
| E1 | Mitarbeitende | Begeisterung | stark | positiv | freier Tag / Lebensqualität |
| E2 | Mitarbeitende | Sorge | mittel | negativ | Arbeitsverdichtung |
| E3 | Geschäftsführung | Zuversicht | mittel | gemischt | Wettbewerbsfähigkeit |
| E4 | Geschäftsführung | Nervosität | mittel | negativ | wirtschaftliches Risiko |
| E5 | Kunden | Skepsis | mittel | negativ | Erreichbarkeit |
| E6 | HR | Tatendrang | stark | positiv | Recruiting-Chance |
| E7 | HR | Respekt vor Aufwand | mittel | gemischt | Umsetzungskomplexität |

```json
{
  "hut": "rot",
  "phase_nr": 6,
  "zusammenfassung": "Die emotionale Lage ist gespalten, aber tendenziell vorwärtsgewandt: starke Begeisterung bei Mitarbeitenden (E1) und Tatendrang bei HR (E6) stehen einer mittleren Sorge vor Verdichtung (E2), unternehmerischer Nervosität (E4) und Kundenskepsis (E5) gegenüber. GF und HR fühlen gemischt.",
  "eintraege": [
    {
      "id": "E1",
      "stakeholder": "Mitarbeitende",
      "gefuehl": "Begeisterung",
      "intensitaet": "stark",
      "richtung": "positiv",
      "bezug": "Aussicht auf einen freien Tag und mehr Lebensqualität"
    },
    {
      "id": "E2",
      "stakeholder": "Mitarbeitende",
      "gefuehl": "Sorge",
      "intensitaet": "mittel",
      "richtung": "negativ",
      "bezug": "befürchtete Arbeitsverdichtung auf vier Tage"
    },
    {
      "id": "E3",
      "stakeholder": "Geschäftsführung",
      "gefuehl": "Zuversicht",
      "intensitaet": "mittel",
      "richtung": "gemischt",
      "bezug": "Stärkung der Wettbewerbsfähigkeit"
    },
    {
      "id": "E4",
      "stakeholder": "Geschäftsführung",
      "gefuehl": "Nervosität",
      "intensitaet": "mittel",
      "richtung": "negativ",
      "bezug": "wirtschaftliches Risiko der Umstellung"
    },
    {
      "id": "E5",
      "stakeholder": "Kunden",
      "gefuehl": "Skepsis",
      "intensitaet": "mittel",
      "richtung": "negativ",
      "bezug": "befürchtete schlechtere Erreichbarkeit"
    },
    {
      "id": "E6",
      "stakeholder": "HR",
      "gefuehl": "Tatendrang",
      "intensitaet": "stark",
      "richtung": "positiv",
      "bezug": "Chance für Recruiting und Arbeitgebermarke"
    },
    {
      "id": "E7",
      "stakeholder": "HR",
      "gefuehl": "Respekt vor dem Aufwand",
      "intensitaet": "mittel",
      "richtung": "gemischt",
      "bezug": "Komplexität der organisatorischen Umsetzung"
    }
  ],
  "offene_punkte": [
    "Die starke positive Erwartung der Mitarbeitenden (E1) erzeugt Druck: Ein Rückzug nach Ankündigung wäre demotivierend.",
    "Kundenskepsis (E5) sollte aktiv durch Kommunikation adressiert werden."
  ],
  "konfidenz": "mittel"
}
```
