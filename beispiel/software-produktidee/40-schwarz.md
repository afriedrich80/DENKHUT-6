# ⚫ Schwarz — Risiken & Bedenken

Der schwarze Hut sucht ausschließlich **Risiken, Schwächen und Gefahren** —
sachlich, mit Ursache, Eintrittswahrscheinlichkeit, Auswirkung und der Frage, ob
eine Gegenmaßnahme grundsätzlich möglich ist. Schwarz schlägt keine Lösungen vor
und nennt keinen Nutzen (das ist Gelb, parallel).

> Bewertet wird dasselbe Top-Idee-Set wie bei Gelb: **I1, I3, I5, I7**.

## Risiken

| ID | Risiko | Idee | EW | Auswirkung | Gegenmaßnahme? |
|----|--------|------|----|------------|----------------|
| R1 | Falsche Auto-Preise beschädigen Vertrauen / führen zu Fehlangeboten | I3 | hoch | hoch | ja |
| R2 | Spracherkennung versagt im Baustellenlärm | I3 | hoch | mittel | ja |
| R3 | Stammdatenpflege je Gewerk ist aufwändiger als gedacht | I1 | mittel | hoch | ja |
| R4 | Ein Gewerk allein ist ein zu kleiner Markt für Tragfähigkeit | I1 | mittel | hoch | ja |
| R5 | WhatsApp-Kanal birgt DSGVO-/Plattformabhängigkeits-Risiko | I5 | mittel | mittel | ja |
| R6 | Pay-per-Angebot erzeugt zu wenig/unkalkulierbaren Umsatz | I7 | mittel | mittel | ja |
| R7 | Etablierte Handwerker-Suiten kopieren das Sprach-Feature schnell | I3 | mittel | hoch | ja |

## Notiz

Die schwersten Risiken bündeln sich um die **Vollautomatik I3**: falsche Preise
(R1, deckt sich mit der Rot-Skepsis E2/E7) und Spracherkennung im Lärm (R2). Beim
Fokus-MVP I1 stehen Stammdatenaufwand (R3) und Marktgröße (R4, deckt sich mit E6)
im Vordergrund. R7 (Nachahmung durch etablierte Suiten) bedroht die
Differenzierung.

```json
{
  "hut": "schwarz",
  "phase_nr": 6,
  "zusammenfassung": "Sieben Risiken zum Top-Set. Schwerpunkt bei der Vollautomatik I3: falsche Auto-Preise (R1) und Spracherkennung im Baustellenlärm (R2). Beim Fokus-MVP I1: Stammdatenaufwand (R3) und zu kleiner Markt (R4). Dazu Kanal-/DSGVO-Risiko bei WhatsApp (R5), Umsatzunsicherheit bei Pay-per-Use (R6) und Nachahmung durch etablierte Suiten (R7). Alle Risiken sind grundsätzlich adressierbar.",
  "eintraege": [
    {
      "id": "R1",
      "risiko": "Automatisch erzeugte Preise sind falsch und führen zu Fehlangeboten oder Vertrauensverlust",
      "bezug_idee": "I3",
      "ursache": "Lücken/Ungenauigkeiten in Stammdaten und LLM-Interpretation der gesprochenen Beschreibung",
      "eintrittswahrscheinlichkeit": "hoch",
      "auswirkung": "hoch",
      "gegenmassnahme_moeglich": true
    },
    {
      "id": "R2",
      "risiko": "Spracherkennung versagt in lauter Baustellenumgebung",
      "bezug_idee": "I3",
      "ursache": "Umgebungslärm senkt die Erkennungsrate deutlich (F4)",
      "eintrittswahrscheinlichkeit": "hoch",
      "auswirkung": "mittel",
      "gegenmassnahme_moeglich": true
    },
    {
      "id": "R3",
      "risiko": "Pflege gewerkespezifischer Stammdaten ist deutlich aufwändiger als geplant",
      "bezug_idee": "I1",
      "ursache": "Positionen und Einheitspreise variieren stark je Gewerk und Region (F7)",
      "eintrittswahrscheinlichkeit": "mittel",
      "auswirkung": "hoch",
      "gegenmassnahme_moeglich": true
    },
    {
      "id": "R4",
      "risiko": "Ein einzelnes Start-Gewerk ist ein zu kleiner Markt für ein tragfähiges Geschäft",
      "bezug_idee": "I1",
      "ursache": "Enger Fokus begrenzt die adressierbare Nutzerbasis kurzfristig",
      "eintrittswahrscheinlichkeit": "mittel",
      "auswirkung": "hoch",
      "gegenmassnahme_moeglich": true
    },
    {
      "id": "R5",
      "risiko": "WhatsApp-Kanal bringt DSGVO- und Plattformabhängigkeits-Risiko",
      "bezug_idee": "I5",
      "ursache": "Verarbeitung personenbezogener Sprachdaten über eine Drittplattform mit eigenen Regeln/Gebühren",
      "eintrittswahrscheinlichkeit": "mittel",
      "auswirkung": "mittel",
      "gegenmassnahme_moeglich": true
    },
    {
      "id": "R6",
      "risiko": "Pay-per-Angebot erzeugt zu geringen oder schwer planbaren Umsatz",
      "bezug_idee": "I7",
      "ursache": "Unklares Angebotsvolumen je Betrieb (F6); Nutzer optimieren Kosten",
      "eintrittswahrscheinlichkeit": "mittel",
      "auswirkung": "mittel",
      "gegenmassnahme_moeglich": true
    },
    {
      "id": "R7",
      "risiko": "Etablierte Handwerker-Suiten kopieren das Sprach-Feature schnell",
      "bezug_idee": "I3",
      "ursache": "Geringe Eintrittsbarriere für Anbieter mit bestehender Nutzerbasis (F3)",
      "eintrittswahrscheinlichkeit": "mittel",
      "auswirkung": "hoch",
      "gegenmassnahme_moeglich": true
    }
  ],
  "offene_punkte": [
    "R1 ist das zentrale Risiko und korrespondiert mit der emotionalen Skepsis (E2, E7) - der Produktzuschnitt muss darauf antworten.",
    "R7 verlangt einen Burggraben (z. B. Stammdaten-Netzwerk I8) für nachhaltige Differenzierung."
  ],
  "konfidenz": "mittel"
}
```
