# Beispiel: Produktidee „MeisterOffert" — Sequenz `ideenfindung`

Dieses Beispiel zeigt, dass DENKHUT-6 nicht nur für **Entscheidungen** taugt,
sondern auch für die **Ideen- und Produktentwicklung**. Statt eine bestehende
Option zu bewerten, wird hier eine Produktidee von der Vision bis zur konkreten
MVP-Empfehlung durchgespielt.

> Das Schwester-Beispiel [`../4-tage-woche/`](../4-tage-woche/) zeigt den
> **Entscheidungs**-Use-Case (Sequenz `entscheidung`): einführen / nicht
> einführen / Pilot. Dort steht eine fertige Option zur Bewertung an. Hier
> dagegen wird etwas **Neues erschaffen**.

## Thema

**MeisterOffert** — eine KI-gestützte SaaS-App, die kleine Handwerksbetriebe bei
der Angebotserstellung unterstützt: Sprachaufnahme vor Ort beim Kunden →
automatischer Angebotsentwurf mit Positionen, Mengen und Preisen.

## Warum die Sequenz `ideenfindung`?

```
blau → weiss → gruen → rot → gelb → schwarz → blau
```

Bei der Ideenfindung ist die Reihenfolge bewusst anders als bei einer
Entscheidung:

- **Grün steht früh und breit.** Nach einer schlanken Faktenbasis (Weiß) wird
  zuerst divergent gedacht: Produktzuschnitte, MVP-Varianten,
  Geschäftsmodelle, ungewöhnliche Ansätze. Es geht um Menge und Vielfalt an
  Optionen, noch ohne Bewertung. Das ist das Herzstück dieser Sequenz.
- **Rot kommt VOR Gelb/Schwarz.** Bei neuen Ideen zählt die **frühe
  emotionale Resonanz**: Begeistert die Idee die Zielgruppe? Schreckt sie ab?
  Diese Bauchreaktion je Stakeholder wird *vor* der rationalen Nutzen-/
  Risiko-Analyse eingefangen, weil sie sonst von Pro/Contra-Argumenten
  überlagert würde. Rot begründet dabei bewusst nicht — es misst nur Stimmung.
- **Gelb und Schwarz danach (parallel).** Erst wenn die Ideen und die Stimmung
  dazu stehen, prüfen Gelb (Nutzen) und Schwarz (Risiken) **dasselbe
  Top-Idee-Set** parallel und unabhängig voneinander.
- **Blau klammert.** Der Blaue Hut eröffnet (Vision/Rahmen) und schließt
  (Synthese → klare MVP-Empfehlung).

## Dateien & Lesart

Die Dateinamen folgen dem **Inhaltstyp**, nicht der Sequenzposition — identisch
zum Schwester-Beispiel. Rot bleibt daher Datei `50`, obwohl es in dieser
Sequenz *vor* Gelb (`30`) und Schwarz (`40`) lief. Die **tatsächliche
Reihenfolge** steht im [`protokoll.md`](protokoll.md).

| Datei | Hut | Inhalt |
|-------|-----|--------|
| [`00-problem.md`](00-problem.md) | 🔵 Blau | Ideen-Brief: Vision, Ziel, Scope, Constraints, Stakeholder, Kriterien |
| [`10-weiss.md`](10-weiss.md) | ⚪ Weiß | Fakten/Annahmen/Wissenslücken zu Markt, Zielgruppe, Wettbewerb, Tech |
| [`20-gruen.md`](20-gruen.md) | 🟢 Grün | Ideen, Varianten, Kombinationen zum Produktzuschnitt |
| [`50-rot.md`](50-rot.md) | 🔴 Rot | Frühe Emotionen je Stakeholder zu den Ideen (Schritt 4!) |
| [`30-gelb.md`](30-gelb.md) | 🟡 Gelb | Nutzenpunkte zu den Top-Ideen |
| [`40-schwarz.md`](40-schwarz.md) | ⚫ Schwarz | Risiken zu den Top-Ideen |
| [`90-synthese.md`](90-synthese.md) | 🔵 Blau | MVP-Empfehlung, Pro/Contra, nächste Schritte |
| [`protokoll.md`](protokoll.md) | — | Audit-Protokoll mit der echten Schrittreihenfolge |

## ID-Konventionen

Jeder Eintrag hat eine stabile ID, die quer referenziert wird:

- **F1, F2, …** — Fakten/Annahmen/Wissenslücken (Weiß)
- **I1, I2, …** — Ideen (Grün)
- **E1, E2, …** — Emotionen (Rot), `bezug` zeigt auf `I*`
- **N1, N2, …** — Nutzenpunkte (Gelb), `bezug_idee` zeigt auf `I*`
- **R1, R2, …** — Risiken (Schwarz), `bezug_idee` zeigt auf `I*`

Die **Synthese** (Blau) baut ihr Pro aus den `N*`, ihr Contra aus den `R*` und
liest die Stimmung aus den `E*`. So bleibt die Argumentationskette von der
Idee bis zur Empfehlung lückenlos nachvollziehbar.

## Maschinenlesbarkeit

Jede Phasendatei endet mit einem ` ```json ```-Block` (Output-Envelope):
`hut`, `phase_nr`, `zusammenfassung`, `eintraege[]`, `offene_punkte[]`,
`konfidenz`. Damit ist jede Phase sowohl für Menschen lesbar als auch
maschinell auswertbar.
