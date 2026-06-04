# 🟡 Gelb — Nutzen & Chancen

Der gelbe Hut sucht ausschließlich den **Nutzen**: Wert, Chance, positiver
Effekt — jeweils mit der **Bedingung**, unter der er eintritt, und dem
**Wirkungshorizont**. Risiken nennt Gelb nicht (das ist Schwarz, parallel).

> Bewertet wird dasselbe Top-Idee-Set wie bei Schwarz: **I1, I3, I5, I7**.

## Nutzenpunkte

| ID | Nutzen | Idee | Bedingung | Horizont |
|----|--------|------|-----------|----------|
| N1 | Drastische Zeitersparnis bei der Angebotserstellung | I3 | Erkennungs- & Preisqualität tragfähig | kurz |
| N2 | Belastbare Preise dank gepflegter Stammdaten | I1 | Stammdaten für ein Gewerk sauber gepflegt | kurz |
| N3 | Schnellster, billigster Markteintritt | I1 | Team diszipliniert auf ein Gewerk fokussiert | kurz |
| N4 | Niedrigste Adoptionshürde, keine App nötig | I5 | WhatsApp-Business-Anbindung DSGVO-konform lösbar | kurz |
| N5 | Mehr gewonnene Aufträge durch schnellere Angebote | I3 | Angebot binnen Minuten beim Endkunden | mittel |
| N6 | Niedrige Einstiegshürde steigert Nutzerzahl | I7 | Pay-per-Angebot-Abrechnung schlank umgesetzt | mittel |
| N7 | Umsatz skaliert mit Nutzung statt mit Verhandlung | I7 | Genug Angebotsvolumen je Betrieb | mittel |
| N8 | Skalierbare Vorlage für weitere Gewerke | I1 | Gewerk-1-Stammdatenmodell wiederverwendbar | lang |

## Notiz

Der größte kurzfristige Hebel liegt in der Kombination **I1 + I3**: ein eng
fokussierter Vollautomatik-Workflow, der durch saubere Stammdaten (N2) sofort
belastbar ist und Zeit spart (N1). I5 senkt die Adoptionshürde (N4), I7 öffnet
ein nutzungsbasiertes, mitwachsendes Modell (N6, N7).

```json
{
  "hut": "gelb",
  "phase_nr": 5,
  "zusammenfassung": "Acht Nutzenpunkte zum Top-Set. Kurzfristig dominieren Zeitersparnis (N1, I3), belastbare Preise durch Fokus (N2, I1) und schneller Markteintritt (N3, I1). Mittelfristig zahlen Adoptionshürde (N4, I5) und nutzungsbasiertes Modell (N6/N7, I7) ein; langfristig die Skalierung auf weitere Gewerke (N8, I1).",
  "eintraege": [
    {
      "id": "N1",
      "nutzen": "Drastische Zeitersparnis bei der Angebotserstellung (Stunden zu Minuten)",
      "bezug_idee": "I3",
      "bedingung": "Spracherkennung und automatische Preise erreichen alltagstaugliche Qualität",
      "wirkungshorizont": "kurz"
    },
    {
      "id": "N2",
      "nutzen": "Belastbare, vertrauenswürdige Preise im erzeugten Angebot",
      "bezug_idee": "I1",
      "bedingung": "Stammdaten (Positionen, Einheitspreise) für das eine Start-Gewerk sind sauber gepflegt",
      "wirkungshorizont": "kurz"
    },
    {
      "id": "N3",
      "nutzen": "Schnellster und kapitaleffizientester Markteintritt",
      "bezug_idee": "I1",
      "bedingung": "Team hält den Fokus diszipliniert auf ein Gewerk statt Feature-/Gewerk-Streuung",
      "wirkungshorizont": "kurz"
    },
    {
      "id": "N4",
      "nutzen": "Niedrigste Adoptionshürde, da kein App-Download und vertraute Bedienung",
      "bezug_idee": "I5",
      "bedingung": "WhatsApp-Business-Anbindung lässt sich DSGVO-konform und stabil umsetzen",
      "wirkungshorizont": "kurz"
    },
    {
      "id": "N5",
      "nutzen": "Mehr gewonnene Aufträge, weil das Angebot schneller beim Endkunden ist",
      "bezug_idee": "I3",
      "bedingung": "Angebot erreicht den Endkunden binnen Minuten statt Tagen",
      "wirkungshorizont": "mittel"
    },
    {
      "id": "N6",
      "nutzen": "Niedrige Einstiegshürde erhöht die Zahl aktivierter Betriebe",
      "bezug_idee": "I7",
      "bedingung": "Pay-per-Angebot-Abrechnung ist schlank und transparent umgesetzt",
      "wirkungshorizont": "mittel"
    },
    {
      "id": "N7",
      "nutzen": "Umsatz skaliert mit tatsächlicher Nutzung statt mit Vertriebsverhandlung",
      "bezug_idee": "I7",
      "bedingung": "Betriebe erzeugen genug Angebotsvolumen, damit Pay-per-Use sich lohnt",
      "wirkungshorizont": "mittel"
    },
    {
      "id": "N8",
      "nutzen": "Wiederverwendbare Vorlage zur Skalierung auf weitere Gewerke",
      "bezug_idee": "I1",
      "bedingung": "Das Stammdaten- und Workflow-Modell des ersten Gewerks ist übertragbar",
      "wirkungshorizont": "lang"
    }
  ],
  "offene_punkte": [
    "N2 und N8 hängen beide an der Qualität und Übertragbarkeit der Stammdaten (F7).",
    "N7 setzt ein ausreichendes Angebotsvolumen pro Betrieb voraus - noch unbestätigt (F6)."
  ],
  "konfidenz": "mittel"
}
```
