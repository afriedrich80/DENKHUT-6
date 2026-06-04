# 🔵 Blau — Eröffnung: Ideen-Brief

## Idee / Vision

**MeisterOffert** soll kleinen Handwerksbetrieben den lästigsten Teil ihres
Tages abnehmen: das abendliche Schreiben von Angeboten. Die Vision ist eine
KI-gestützte SaaS-App, in die der Handwerker **vor Ort beim Kunden eine
Sprachnotiz** spricht („Bad komplett neu, ca. 8 Quadratmeter, alte Fliesen raus,
neue Boden- und Wandfliesen, neues WC, Dusche bodengleich …"). Daraus erzeugt
die App automatisch einen **strukturierten Angebotsentwurf** mit Positionen,
Mengen und Preisen — den der Betrieb nur noch prüft, anpasst und versendet.

Statt zwei Stunden am Küchentisch entsteht das Angebot in Minuten. Der Betrieb
gewinnt Zeit, reagiert schneller als der Wettbewerb und verliert weniger Aufträge
durch verschleppte Angebote.

## Ziel

Eine durch alle sechs Denkhüte geprüfte **Produkt- und MVP-Empfehlung**: Welcher
Zuschnitt wird *zuerst* gebaut, was kommt später, und mit welchem
Geschäftsmodell startet MeisterOffert in den Markt? Inklusive konkreter nächster
Schritte (Validierung) und benannter offener Risiken.

## Scope

- **Im Scope:** Produktzuschnitt (MVP), Kern-Workflow Sprache → Angebotsentwurf,
  Zielgruppen-Fokus, Geschäftsmodell-/Pricing-Varianten, Differenzierung,
  grobe technische Machbarkeit, Time-to-Market.
- **Außerhalb des Scope:** Fertige UI-Designs, konkrete Tech-Stack-Wahl im
  Detail, Buchhaltung/Rechnungsstellung, Vertrieb über Großhandelsketten,
  internationale Expansion.

## Constraints

- **Kleines Bootstrap-Budget** (~80.000 € für die ersten 12 Monate, Gründerteam
  ohne VC-Runde). MVP muss schlank und schnell sein.
- **DSGVO**: Sprachaufnahmen und Kundendaten (Endkunden des Handwerkers) sind
  personenbezogen — Speicherung, Verarbeitung und ggf. US-LLM-Nutzung müssen
  rechtskonform sein.
- **Branchen-Spezifika**: Gewerke unterscheiden sich stark (Sanitär ≠ Elektro ≠
  Maler). Positions- und Preislogik ist je Gewerk verschieden.
- **Offline-/Baustellen-Realität**: Auf Baustellen ist die Netzabdeckung oft
  schlecht; laute Umgebung erschwert die Spracherkennung.
- **Geringe IT-Affinität** vieler Zielnutzer: Die App muss extrem einfach sein.

## Stakeholder

- **Handwerksbetriebe / Inhaber** — wollen Zeit sparen, mehr Aufträge gewinnen,
  zahlen aber ungern für Software; entscheiden über den Kauf.
- **Monteure / Gesellen** — bedienen die App vor Ort; müssen den Mehrwert
  spüren, sonst nutzen sie sie nicht.
- **Endkunden** (Auftraggeber des Handwerkers) — erleben schnellere, sauberere
  Angebote; ihre Daten werden verarbeitet.
- **Gründerteam / Investor** — Tragfähigkeit des Geschäftsmodells, Differenzierung,
  Time-to-Market, Kapitaleffizienz.

## Entscheidungskriterien

1. **Zahlungsbereitschaft** — Sind Betriebe bereit, monatlich für das Tool zu
   zahlen (Ziel-ARPU plausibel)?
2. **Technische Machbarkeit** — Liefert Sprache → strukturierter Entwurf eine
   Qualität, die im Alltag Zeit spart statt kostet?
3. **Differenzierung** — Klarer Vorsprung gegenüber bestehenden
   Handwerker-/Angebots-Tools?
4. **Time-to-Market** — Mit Bootstrap-Budget in vertretbarer Zeit zum
   zahlenden ersten Kunden?

## Gewählte Sequenz: `ideenfindung`

```
blau → weiss → gruen → rot → gelb → schwarz → blau
```

> In dieser Sequenz steht **Grün früh und breit** (Optionen erzeugen), und
> **Rot kommt vor Gelb/Schwarz** — die emotionale Erstresonanz auf die Ideen
> wird eingefangen, bevor rationale Nutzen-/Risikoanalyse einsetzt.

```json
{
  "hut": "blau",
  "phase_nr": 1,
  "zusammenfassung": "Eröffnung der Ideenfindung zur Produktidee MeisterOffert (KI-SaaS für Angebotserstellung im Handwerk via Sprachaufnahme). Vision, Ziel, Scope, Constraints, Stakeholder und Entscheidungskriterien sind gesetzt. Gewählt wird die Sequenz 'ideenfindung' mit Grün früh/breit und Rot vor Gelb/Schwarz.",
  "eintraege": [],
  "offene_punkte": [
    "Belastbare Zahlungsbereitschaft der Zielgruppe ist noch unbekannt (an Weiss/Validierung).",
    "Qualität der Sprache-zu-Angebot-Pipeline ist noch nicht erprobt (an Weiss/Tech-Spike)."
  ],
  "konfidenz": "hoch",
  "problem": {
    "beschreibung": "Wie sollte die Produktidee MeisterOffert (KI-gestützte Angebotserstellung für kleine Handwerksbetriebe via Sprachaufnahme vor Ort) zugeschnitten und als MVP gestartet werden?",
    "ziel": "Fundierte Produkt-/MVP-Empfehlung (welcher Zuschnitt zuerst, was später, welches Geschäftsmodell) inkl. nächster Validierungsschritte und offener Risiken.",
    "scope": "Produktzuschnitt/MVP, Kern-Workflow Sprache zu Angebotsentwurf, Zielgruppen-Fokus, Geschäftsmodell/Pricing, Differenzierung, grobe technische Machbarkeit, Time-to-Market. Nicht: fertige UI, Detail-Tech-Stack, Buchhaltung, Großhandels-Vertrieb, Internationalisierung.",
    "constraints": [
      "Kleines Bootstrap-Budget (~80.000 EUR / 12 Monate, keine VC-Runde)",
      "DSGVO-Konformität bei Sprachaufnahmen und Endkundendaten",
      "Branchen-Spezifika: Positions-/Preislogik je Gewerk verschieden",
      "Offline-/Baustellen-Realität: schlechtes Netz, laute Umgebung",
      "Geringe IT-Affinität der Zielnutzer - App muss extrem einfach sein"
    ],
    "stakeholder": ["Handwerksbetriebe/Inhaber", "Monteure/Gesellen", "Endkunden", "Gründerteam/Investor"],
    "entscheidungskriterien": [
      "Zahlungsbereitschaft der Betriebe (plausibler Ziel-ARPU)",
      "Technische Machbarkeit der Sprache-zu-Angebot-Pipeline",
      "Differenzierung gegenüber bestehenden Tools",
      "Time-to-Market mit Bootstrap-Budget"
    ]
  },
  "sequenz": ["blau", "weiss", "gruen", "rot", "gelb", "schwarz", "blau"]
}
```
