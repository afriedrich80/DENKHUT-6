# 🔴 Rot — Emotionen & Resonanz

Der rote Hut fängt die **unmittelbare Bauchreaktion** je Stakeholder auf die
Ideen ein — Begeisterung, Skepsis, Unbehagen. **Ohne Begründung**: Rot erklärt
nicht, es misst nur Stimmung und Richtung. In der Sequenz `ideenfindung` steht
Rot bewusst **vor** Gelb und Schwarz, damit die ehrliche Erstresonanz nicht von
rationalen Argumenten überlagert wird.

> Bezug jeweils auf die Top-Ideen aus Grün: **I1** (Gewerke-Fokus-MVP),
> **I3** (Vollautomatik), **I5** (WhatsApp-Bot), **I7** (Freemium/Pay-per-Angebot).

## Stimmungsbild

| ID | Stakeholder | Gefühl | Intensität | Richtung | Bezug |
|----|-------------|--------|------------|----------|-------|
| E1 | Handwerksbetriebe/Inhaber | Erleichterung, „endlich nimmt mir das jemand ab" | stark | positiv | I3 |
| E2 | Handwerksbetriebe/Inhaber | Misstrauen gegenüber automatisch erzeugten Preisen | stark | negativ | I3 |
| E3 | Monteure/Gesellen | Begeisterung, „so einfach wie eine Sprachnachricht" | stark | positiv | I5 |
| E4 | Handwerksbetriebe/Inhaber | Sympathie für niedrige Einstiegshürde ohne Abo-Zwang | mittel | positiv | I7 |
| E5 | Gründerteam/Investor | Zuversicht, dass enger Fokus machbar wirkt | mittel | positiv | I1 |
| E6 | Gründerteam/Investor | Nervosität, ob ein einzelnes Gewerk groß genug ist | mittel | gemischt | I1 |
| E7 | Endkunden | Unbehagen, „rechnet mir eine KI das zu teuer/falsch?" | mittel | negativ | I3 |
| E8 | Monteure/Gesellen | Stolz, modern und schnell beim Kunden aufzutreten | mittel | positiv | I5 |

## Notiz

Das Stimmungsbild ist klar gespalten: **Der Workflow begeistert** (E1, E3, E8),
**die automatischen Preise machen Bauchschmerzen** (E2, E7). Das Geschäftsmodell
ohne Abo-Zwang (E4) und der enge Fokus (E5) treffen auf Zustimmung, begleitet von
Investoren-Nervosität zur Marktgröße (E6).

```json
{
  "hut": "rot",
  "phase_nr": 4,
  "zusammenfassung": "Acht emotionale Signale je Stakeholder zum Top-Idee-Set. Starke positive Resonanz auf den Sprach-Workflow und die einfache Bedienung (E1, E3, E8), aber starkes Misstrauen gegenüber automatisch erzeugten Preisen (E2, E7). Geschäftsmodell ohne Abo-Zwang (E4) und enger Fokus (E5) positiv, Investoren-Nervosität zur Marktgröße (E6).",
  "eintraege": [
    {
      "id": "E1",
      "stakeholder": "Handwerksbetriebe/Inhaber",
      "gefuehl": "Erleichterung, dass die ungeliebte Angebotsarbeit abgenommen wird",
      "intensitaet": "stark",
      "richtung": "positiv",
      "bezug": "I3"
    },
    {
      "id": "E2",
      "stakeholder": "Handwerksbetriebe/Inhaber",
      "gefuehl": "Misstrauen gegenüber automatisch erzeugten Preisen",
      "intensitaet": "stark",
      "richtung": "negativ",
      "bezug": "I3"
    },
    {
      "id": "E3",
      "stakeholder": "Monteure/Gesellen",
      "gefuehl": "Begeisterung über die Einfachheit wie bei einer Sprachnachricht",
      "intensitaet": "stark",
      "richtung": "positiv",
      "bezug": "I5"
    },
    {
      "id": "E4",
      "stakeholder": "Handwerksbetriebe/Inhaber",
      "gefuehl": "Sympathie für niedrige Einstiegshürde ohne Abo-Zwang",
      "intensitaet": "mittel",
      "richtung": "positiv",
      "bezug": "I7"
    },
    {
      "id": "E5",
      "stakeholder": "Gründerteam/Investor",
      "gefuehl": "Zuversicht, dass ein enger Fokus umsetzbar wirkt",
      "intensitaet": "mittel",
      "richtung": "positiv",
      "bezug": "I1"
    },
    {
      "id": "E6",
      "stakeholder": "Gründerteam/Investor",
      "gefuehl": "Nervosität, ob ein einzelnes Gewerk einen großen genug Markt bietet",
      "intensitaet": "mittel",
      "richtung": "gemischt",
      "bezug": "I1"
    },
    {
      "id": "E7",
      "stakeholder": "Endkunden",
      "gefuehl": "Unbehagen, eine KI könnte zu teuer oder falsch kalkulieren",
      "intensitaet": "mittel",
      "richtung": "negativ",
      "bezug": "I3"
    },
    {
      "id": "E8",
      "stakeholder": "Monteure/Gesellen",
      "gefuehl": "Stolz, modern und schnell beim Kunden aufzutreten",
      "intensitaet": "mittel",
      "richtung": "positiv",
      "bezug": "I5"
    }
  ],
  "offene_punkte": [
    "Das Preis-Misstrauen (E2, E7) ist das stärkste negative Signal und sollte den Produktzuschnitt beeinflussen.",
    "Investoren-Nervosität zur Marktgröße (E6) verweist auf die spätere Expansion über das erste Gewerk hinaus."
  ],
  "konfidenz": "mittel"
}
```
