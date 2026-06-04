# ⚫ Schwarz — Risiken & Schwächen

Der schwarze Hut prüft kritisch: Wo kann es schiefgehen? Bewertet werden **dieselben
Top-Ideen** wie bei Gelb (**I1**, **I4**, **I7**), jeweils mit
**Eintrittswahrscheinlichkeit**, **Auswirkung** und der Frage, ob eine
**Gegenmaßnahme** möglich ist.

> Gelb und Schwarz liefen **parallel** auf demselben Ideensatz — bewusst, um Nutzen
> und Risiko jeder Idee direkt gegenüberstellen zu können.

## Risiken

| ID | Risiko | Idee | Eintritt | Auswirkung | Gegenmaßnahme? |
|----|--------|------|----------|-----------|----------------|
| R1 | Produktivität bricht ein, Tageskapazität nicht ausgleichbar | I1 | mittel | hoch | ja |
| R2 | Kundenabwanderung wg. schlechterer Erreichbarkeit | I1 | mittel | hoch | ja |
| R3 | Mehrkosten durch Neueinstellungen bei Kapazitätslücke | I1 | mittel | mittel | ja |
| R4 | Rotationsplanung im Service scheitert an Engpässen/Krankheit | I4 | hoch | mittel | ja |
| R5 | Pilot nicht repräsentativ → Fehlschluss bei Hochrechnung | I7 | mittel | mittel | ja |
| R6 | Neid/Ungleichbehandlung zwischen Pilot- und Nicht-Pilot-Teams | I7 | hoch | mittel | ja |
| R7 | Mehrarbeit verdichtet sich, Überlastung statt Entlastung | I1 | mittel | hoch | ja |

```json
{
  "hut": "schwarz",
  "phase_nr": 5,
  "zusammenfassung": "Sieben Risiken zu den Top-Ideen. Die Vollumstellung I1 trägt die schwersten Risiken (Produktivitätseinbruch R1, Kundenabwanderung R2, Überlastung R7 — je hohe Auswirkung). Beim Pilot dominieren Repräsentativitäts- (R5) und Fairness-Risiken (R6); die Service-Rotation I4 hat ein hohes, aber begrenzt schweres Engpassrisiko (R4). Alle Risiken sind grundsätzlich adressierbar.",
  "eintraege": [
    {
      "id": "R1",
      "risiko": "Die Produktivität bricht ein, weil die wegfallende Tageskapazität nicht ausgeglichen werden kann.",
      "bezug_idee": "I1",
      "ursache": "Die in F5 angenommene Produktivitätssteigerung von 8-12 % je Tag wird nicht erreicht.",
      "eintrittswahrscheinlichkeit": "mittel",
      "auswirkung": "hoch",
      "gegenmassnahme_moeglich": true
    },
    {
      "id": "R2",
      "risiko": "Kunden wandern ab, weil Ansprechpartner schlechter erreichbar sind.",
      "bezug_idee": "I1",
      "ursache": "Wissenslücke F6: Reaktion der Kunden auf veränderte Verfügbarkeit ist unbekannt.",
      "eintrittswahrscheinlichkeit": "mittel",
      "auswirkung": "hoch",
      "gegenmassnahme_moeglich": true
    },
    {
      "id": "R3",
      "risiko": "Mehrkosten durch zusätzliche Einstellungen, um Kapazitätslücken zu schließen.",
      "bezug_idee": "I1",
      "ursache": "Verdichtung gelingt nur teilweise (F3 ist nur eine Annahme).",
      "eintrittswahrscheinlichkeit": "mittel",
      "auswirkung": "mittel",
      "gegenmassnahme_moeglich": true
    },
    {
      "id": "R4",
      "risiko": "Die Rotationsplanung im Kundenservice scheitert an Engpässen und Krankheitsausfällen.",
      "bezug_idee": "I4",
      "ursache": "Bei 35 Servicekräften und fester 08-18-Uhr-Abdeckung (F4) ist die Planung anfällig.",
      "eintrittswahrscheinlichkeit": "hoch",
      "auswirkung": "mittel",
      "gegenmassnahme_moeglich": true
    },
    {
      "id": "R5",
      "risiko": "Der Pilot ist nicht repräsentativ, sodass die Hochrechnung auf das Gesamtunternehmen zu Fehlschlüssen führt.",
      "bezug_idee": "I7",
      "ursache": "Freiwillige Pilotabteilungen sind tendenziell motivierter als der Durchschnitt.",
      "eintrittswahrscheinlichkeit": "mittel",
      "auswirkung": "mittel",
      "gegenmassnahme_moeglich": true
    },
    {
      "id": "R6",
      "risiko": "Neid und wahrgenommene Ungleichbehandlung zwischen Pilot- und Nicht-Pilot-Teams.",
      "bezug_idee": "I7",
      "ursache": "Nur ein Teil der Belegschaft profitiert zunächst vom neuen Modell.",
      "eintrittswahrscheinlichkeit": "hoch",
      "auswirkung": "mittel",
      "gegenmassnahme_moeglich": true
    },
    {
      "id": "R7",
      "risiko": "Die Arbeit verdichtet sich so stark, dass Überlastung statt Entlastung entsteht.",
      "bezug_idee": "I1",
      "ursache": "Gleiche Aufgabenmenge auf vier statt fünf Tagen ohne echte Prozessverschlankung.",
      "eintrittswahrscheinlichkeit": "mittel",
      "auswirkung": "hoch",
      "gegenmassnahme_moeglich": true
    }
  ],
  "offene_punkte": [
    "R1, R2 und R7 sind die K.-o.-Risiken der Vollumstellung und sprechen für einen vorgeschalteten Pilot.",
    "R6 (Fairness) erfordert von Beginn an transparente Kommunikation und einen klaren Ausrollpfad."
  ],
  "konfidenz": "mittel"
}
```
