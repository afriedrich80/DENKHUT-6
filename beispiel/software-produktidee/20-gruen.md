# 🟢 Grün — Ideen & Optionen

Der grüne Hut erzeugt Möglichkeiten — ohne Bewertung. In der Ideenfindung steht
er **früh und breit**: Produktzuschnitte, Feature-Ideen, Geschäftsmodelle und
bewusst auch ungewöhnliche Ansätze. Bewertet wird hier nichts.

## Ideen

| ID | Titel | Typ | Baut auf |
|----|-------|-----|----------|
| I1 | Gewerke-Fokus-MVP: nur ein Gewerk (Sanitär/Bad) | neu | – |
| I2 | Sprach-Diktat → reiner Textentwurf (ohne Preise) | neu | – |
| I3 | Vollautomatik: Sprache → Positionen + Mengen + Preise | neu | – |
| I4 | „Co-Pilot": KI schlägt vor, Handwerker bestätigt Position für Position | variante | I3 |
| I5 | WhatsApp-Bot statt App: Sprachnachricht rein, PDF-Angebot raus | neu | – |
| I6 | Foto + Sprache kombiniert (Raum fotografieren, dazu sprechen) | kombination | I3 |
| I7 | Freemium + Pay-per-Angebot statt fixem Abo | neu | – |
| I8 | Stammdaten-Netzwerk: Betriebe teilen anonymisierte Preis-Benchmarks | neu | – |
| I9 | White-Label für Großhandel/Verbände als Vertriebskanal | variante | I1 |

## Beschreibungen

- **I1 – Gewerke-Fokus-MVP:** Statt „alle Gewerke" zuerst nur **ein** Gewerk
  (z. B. Sanitär/Bad) mit gepflegten Stammdaten. Begrenzt den Umfang der
  Stammdaten (F7) auf ein einzelnes Gewerk.
- **I2 – Reiner Textentwurf:** Die App diktiert nur eine strukturierte
  Leistungsbeschreibung als Text — **ohne** Preise; die Stammdaten-Frage (F7)
  bleibt zunächst außen vor.
- **I3 – Vollautomatik:** Der Vollausbau der Vision: Sprache → fertige Positionen,
  Mengen und Preise. Setzt vollständige Stammdaten (F7) und hohe
  Erkennungsqualität (F4) voraus.
- **I4 – Co-Pilot:** Variante von I3, bei der die KI Position für Position
  vorschlägt und der Handwerker jeweils bestätigt/korrigiert; der Nutzer geht
  Position für Position durch, dabei entstehen Korrekturdaten.
- **I5 – WhatsApp-Bot:** Kein App-Download nötig — der Handwerker schickt eine
  Sprachnachricht an eine WhatsApp-Nummer und bekommt das Angebot als PDF zurück;
  Ein- und Ausgabe laufen über einen bereits genutzten Messenger.
- **I6 – Foto + Sprache:** Kombination aus Bild und Sprache; ein Foto des Raums
  liefert Kontext (Größe, Zustand) zusätzlich zur Beschreibung.
- **I7 – Freemium + Pay-per-Angebot:** Geschäftsmodell-Variante: kostenlos starten,
  pro erzeugtem/versendetem Angebot zahlen — Abrechnung pro Angebot statt festem
  Abo (F6).
- **I8 – Stammdaten-Netzwerk:** Betriebe steuern anonymisierte Preisdaten bei und
  erhalten dafür regionale Preis-Benchmarks — die Stammdaten (F7) entstehen als
  Netzwerkeffekt über die Nutzerbasis.
- **I9 – White-Label:** Statt Direktvertrieb das Tool gebrandet über Großhandel
  oder Innungen/Verbände ausrollen — der Vertrieb läuft über bestehende Kanäle
  zur Zielgruppe.

```json
{
  "hut": "gruen",
  "phase_nr": 3,
  "zusammenfassung": "Neun Optionen von engem MVP-Fokus (I1, I2) über Ausbaustufen des Kern-Workflows (I3, I4, I6) und alternative Kanäle (I5, I9) bis zu Geschäftsmodell- und Netzwerk-Ideen (I7, I8). Mehrere Ideen beziehen die Stammdaten (F7) und die offene Zahlungsbereitschaft (F6) ein.",
  "eintraege": [
    {
      "id": "I1",
      "titel": "Gewerke-Fokus-MVP: nur ein Gewerk (Sanitär/Bad)",
      "beschreibung": "MVP zunächst nur für ein Gewerk mit gepflegten Stammdaten statt für alle Gewerke. Begrenzt den Umfang der Stammdaten (F7) auf ein einzelnes Gewerk.",
      "typ": "neu",
      "basiert_auf": []
    },
    {
      "id": "I2",
      "titel": "Sprach-Diktat zu reinem Textentwurf (ohne Preise)",
      "beschreibung": "Die App erzeugt nur eine strukturierte Leistungsbeschreibung als Text ohne Preise; die Stammdaten-Frage (F7) bleibt zunächst außen vor.",
      "typ": "neu",
      "basiert_auf": []
    },
    {
      "id": "I3",
      "titel": "Vollautomatik: Sprache zu Positionen + Mengen + Preisen",
      "beschreibung": "Vollausbau der Vision: aus der Sprachaufnahme entsteht ein fertiger Angebotsentwurf mit Positionen, Mengen und Preisen. Setzt vollständige Stammdaten (F7) und hohe Erkennungsqualität (F4) voraus.",
      "typ": "neu",
      "basiert_auf": []
    },
    {
      "id": "I4",
      "titel": "Co-Pilot: KI schlägt vor, Handwerker bestätigt je Position",
      "beschreibung": "Variante von I3, bei der die KI Position für Position vorschlägt und der Nutzer bestätigt/korrigiert; der Nutzer geht Position für Position durch, dabei entstehen Trainings-/Korrekturdaten.",
      "typ": "variante",
      "basiert_auf": ["I3"]
    },
    {
      "id": "I5",
      "titel": "WhatsApp-Bot statt App",
      "beschreibung": "Kein App-Download: Sprachnachricht an eine WhatsApp-Nummer rein, PDF-Angebot zurück. Ein- und Ausgabe laufen über einen bereits genutzten Messenger.",
      "typ": "neu",
      "basiert_auf": []
    },
    {
      "id": "I6",
      "titel": "Foto + Sprache kombiniert",
      "beschreibung": "Kombination aus Bild und Sprache: ein Foto des Raums liefert zusätzlichen Kontext (Größe, Zustand) zur gesprochenen Beschreibung.",
      "typ": "kombination",
      "basiert_auf": ["I3"]
    },
    {
      "id": "I7",
      "titel": "Freemium + Pay-per-Angebot statt fixem Abo",
      "beschreibung": "Geschäftsmodell-Variante: kostenlos starten, pro erzeugtem/versendetem Angebot zahlen. Abrechnung pro Angebot statt festem Abo (F6).",
      "typ": "neu",
      "basiert_auf": []
    },
    {
      "id": "I8",
      "titel": "Stammdaten-Netzwerk mit Preis-Benchmarks",
      "beschreibung": "Betriebe steuern anonymisierte Preisdaten bei und erhalten dafür regionale Benchmarks. Die Stammdaten (F7) entstehen als Netzwerkeffekt über die Nutzerbasis.",
      "typ": "neu",
      "basiert_auf": []
    },
    {
      "id": "I9",
      "titel": "White-Label über Großhandel/Verbände",
      "beschreibung": "Gebrandeter Ausroll über Großhandel oder Innungen/Verbände statt Direktvertrieb an Kleinstbetriebe. Variante des Fokus-MVP (I1) mit anderem Vertriebskanal.",
      "typ": "variante",
      "basiert_auf": ["I1"]
    }
  ],
  "offene_punkte": [
    "Kombinationen aus I6 (Foto + Sprache) und I8 (Stammdaten-Netzwerk) sind noch nicht ausgearbeitet.",
    "Weitere Vertriebs-Analogien jenseits von I9 (White-Label) sind noch ungenutzt.",
    "Varianten für weitere Gewerke neben dem Start-Gewerk (I1) sind noch offen."
  ],
  "konfidenz": "hoch"
}
```
