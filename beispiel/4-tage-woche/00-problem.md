# 🔵 Blau — Eröffnung: Problemrahmen

## Problem

Die Geschäftsführung erwägt, für das gesamte Unternehmen (~120 Mitarbeitende, davon
ca. 35 in direktem Kundenkontakt) eine **4-Tage-Woche** einzuführen. Anlass sind
zunehmende Schwierigkeiten bei der Personalgewinnung, Hinweise auf Überlastung in
einzelnen Teams und ein gestiegenes Interesse an „New Work"-Modellen im Wettbewerb.
Unklar ist, ob das Modell ohne Lohnkürzung wirtschaftlich tragbar ist und ob die
Kundenbetreuung darunter leidet.

## Ziel

Eine fundierte, durch alle sechs Denkhüte geprüfte **Entscheidungsempfehlung**:
einführen / nicht einführen / als Pilot testen — inklusive konkreter nächster
Schritte und benannter offener Risiken.

## Scope

- **Im Scope:** Arbeitszeitmodell, Produktivität, Kundenbetreuung, Personalbindung
  und -gewinnung, grobe Kostenwirkung, Pilotierbarkeit.
- **Außerhalb des Scope:** Detaillierte arbeitsrechtliche Vertragsausgestaltung,
  Standortverlagerungen, Lohnstruktur-Reformen, IT-Tooling-Auswahl.

## Constraints

- Keine Lohnkürzung bei Reduktion der Wochenarbeitszeit (politische Vorgabe der GF).
- Kundenservicezeiten Mo–Fr 08–18 Uhr müssen erhalten bleiben.
- Entscheidung soll innerhalb von 8 Wochen fallen.
- Budget für externe Beratung max. 15.000 €.

## Stakeholder

- **Geschäftsführung** — Wirtschaftlichkeit, Wettbewerbsfähigkeit, Risiko.
- **Mitarbeitende** — Work-Life-Balance, Arbeitsdichte, Fairness.
- **Kunden** — Erreichbarkeit, gleichbleibende Servicequalität.
- **HR** — Recruiting, Umsetzbarkeit, rechtliche Korrektheit, Change-Begleitung.

## Entscheidungskriterien

1. Produktivität bleibt mindestens stabil (≤ 5 % Rückgang akzeptabel im Pilot).
2. Kundenservicezeiten und Reaktionszeiten bleiben gewahrt.
3. Kostenneutralität oder Refinanzierung binnen 12 Monaten plausibel.
4. Messbare Verbesserung bei Mitarbeiterbindung / Recruiting.
5. Umsetzbar ohne Verstoß gegen arbeitsrechtliche Vorgaben.

## Gewählte Sequenz: `entscheidung`

```
blau → weiss → gruen → gelb → schwarz → rot → blau
```

```json
{
  "hut": "blau",
  "phase_nr": 1,
  "zusammenfassung": "Eröffnung der Sitzung zur Frage einer unternehmensweiten 4-Tage-Woche. Problem, Ziel, Scope, Constraints, Stakeholder und Entscheidungskriterien sind gesetzt. Gewählt wird die Default-Sequenz 'entscheidung'.",
  "eintraege": [],
  "offene_punkte": [
    "Belastbare Produktivitätsdaten aus vergleichbaren Unternehmen fehlen noch (an Weiss).",
    "Genaue Kostenwirkung ohne Lohnkürzung ist noch nicht quantifiziert."
  ],
  "konfidenz": "hoch",
  "problem": {
    "beschreibung": "Soll das Unternehmen (~120 Mitarbeitende) eine 4-Tage-Woche ohne Lohnkürzung einführen, ohne Kundenbetreuung und Wirtschaftlichkeit zu gefährden?",
    "ziel": "Fundierte Entscheidungsempfehlung (einführen / nicht einführen / Pilot) inkl. nächster Schritte und offener Risiken.",
    "scope": "Arbeitszeitmodell, Produktivität, Kundenbetreuung, Personalbindung/-gewinnung, grobe Kostenwirkung, Pilotierbarkeit. Nicht: Vertragsdetails, Standorte, Lohnreform, Tool-Auswahl.",
    "constraints": [
      "Keine Lohnkürzung bei reduzierter Wochenarbeitszeit",
      "Kundenservicezeiten Mo-Fr 08-18 Uhr müssen erhalten bleiben",
      "Entscheidung innerhalb von 8 Wochen",
      "Beratungsbudget max. 15.000 EUR"
    ],
    "stakeholder": ["Geschäftsführung", "Mitarbeitende", "Kunden", "HR"],
    "entscheidungskriterien": [
      "Produktivität bleibt mindestens stabil (max. 5% Rückgang im Pilot)",
      "Kundenservicezeiten und Reaktionszeiten bleiben gewahrt",
      "Kostenneutralität oder Refinanzierung binnen 12 Monaten plausibel",
      "Messbare Verbesserung bei Mitarbeiterbindung/Recruiting",
      "Arbeitsrechtlich umsetzbar"
    ]
  },
  "sequenz": ["blau", "weiss", "gruen", "gelb", "schwarz", "rot", "blau"]
}
```
