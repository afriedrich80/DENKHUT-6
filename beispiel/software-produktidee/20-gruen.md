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
  (z. B. Sanitär/Bad) mit sauber gepflegten Stammdaten. Reduziert die F7-Komplexität
  drastisch und macht den MVP überhaupt erst belastbar.
- **I2 – Reiner Textentwurf:** Die App diktiert nur eine strukturierte
  Leistungsbeschreibung als Text — **ohne** Preise. Niedrigste Hürde, schnellster
  Bau, umgeht F7 vorerst.
- **I3 – Vollautomatik:** Der Vollausbau der Vision: Sprache → fertige Positionen,
  Mengen und Preise. Maximaler Wow-Effekt, höchste Anforderung an Stammdaten (F7)
  und Erkennungsqualität (F4).
- **I4 – Co-Pilot:** Variante von I3, bei der die KI Position für Position
  vorschlägt und der Handwerker jeweils bestätigt/korrigiert. Mehr Kontrolle,
  weniger „Blackbox"-Gefühl, trainiert nebenbei die Daten.
- **I5 – WhatsApp-Bot:** Kein App-Download nötig — der Handwerker schickt eine
  Sprachnachricht an eine WhatsApp-Nummer und bekommt das Angebot als PDF zurück.
  Trifft die geringe IT-Affinität (Constraint) direkt.
- **I6 – Foto + Sprache:** Kombination aus Bild und Sprache; ein Foto des Raums
  liefert Kontext (Größe, Zustand) zusätzlich zur Beschreibung.
- **I7 – Freemium + Pay-per-Angebot:** Geschäftsmodell-Variante: kostenlos starten,
  pro erzeugtem/versendetem Angebot zahlen — senkt die Einstiegshürde bei
  unklarer Zahlungsbereitschaft (F6).
- **I8 – Stammdaten-Netzwerk:** Betriebe steuern anonymisierte Preisdaten bei und
  erhalten dafür regionale Preis-Benchmarks — adressiert F7 als Netzwerkeffekt
  und potenziellen Burggraben.
- **I9 – White-Label:** Statt Direktvertrieb das Tool gebrandet über Großhandel
  oder Innungen/Verbände ausrollen — löst das teure Vertriebsproblem an die
  Zielgruppe.

```json
{
  "hut": "gruen",
  "phase_nr": 3,
  "zusammenfassung": "Neun Optionen von engem MVP-Fokus (I1, I2) über Ausbaustufen des Kern-Workflows (I3, I4, I6) und alternative Kanäle (I5, I9) bis zu Geschäftsmodell- und Burggraben-Ideen (I7, I8). Mehrere Ideen adressieren gezielt die Stammdaten-Komplexität (F7) und die unklare Zahlungsbereitschaft (F6).",
  "eintraege": [
    {
      "id": "I1",
      "titel": "Gewerke-Fokus-MVP: nur ein Gewerk (Sanitär/Bad)",
      "beschreibung": "MVP zunächst nur für ein Gewerk mit sauber gepflegten Stammdaten statt für alle Gewerke. Reduziert die F7-Komplexität drastisch und macht Preise/Mengen belastbar.",
      "typ": "neu",
      "basiert_auf": []
    },
    {
      "id": "I2",
      "titel": "Sprach-Diktat zu reinem Textentwurf (ohne Preise)",
      "beschreibung": "Die App erzeugt nur eine strukturierte Leistungsbeschreibung als Text ohne Preise. Niedrigste technische Hürde, schnellster Bau, umgeht die Stammdaten-Problematik (F7) vorerst.",
      "typ": "neu",
      "basiert_auf": []
    },
    {
      "id": "I3",
      "titel": "Vollautomatik: Sprache zu Positionen + Mengen + Preisen",
      "beschreibung": "Vollausbau der Vision: aus der Sprachaufnahme entsteht ein fertiger Angebotsentwurf mit Positionen, Mengen und Preisen. Maximaler Wow-Effekt, höchste Anforderung an Stammdaten (F7) und Erkennungsqualität (F4).",
      "typ": "neu",
      "basiert_auf": []
    },
    {
      "id": "I4",
      "titel": "Co-Pilot: KI schlägt vor, Handwerker bestätigt je Position",
      "beschreibung": "Variante von I3, bei der die KI Position für Position vorschlägt und der Nutzer bestätigt/korrigiert. Mehr Kontrolle, weniger Blackbox-Gefühl, sammelt nebenbei Trainings-/Korrekturdaten.",
      "typ": "variante",
      "basiert_auf": ["I3"]
    },
    {
      "id": "I5",
      "titel": "WhatsApp-Bot statt App",
      "beschreibung": "Kein App-Download: Sprachnachricht an eine WhatsApp-Nummer rein, PDF-Angebot zurück. Adressiert die geringe IT-Affinität der Zielgruppe direkt.",
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
      "beschreibung": "Geschäftsmodell-Variante: kostenlos starten, pro erzeugtem/versendetem Angebot zahlen. Senkt die Einstiegshürde bei unklarer Zahlungsbereitschaft (F6).",
      "typ": "neu",
      "basiert_auf": []
    },
    {
      "id": "I8",
      "titel": "Stammdaten-Netzwerk mit Preis-Benchmarks",
      "beschreibung": "Betriebe steuern anonymisierte Preisdaten bei und erhalten dafür regionale Benchmarks. Adressiert F7 als Netzwerkeffekt und potenziellen Burggraben.",
      "typ": "neu",
      "basiert_auf": []
    },
    {
      "id": "I9",
      "titel": "White-Label über Großhandel/Verbände",
      "beschreibung": "Gebrandeter Ausroll über Großhandel oder Innungen/Verbände statt teurem Direktvertrieb an Kleinstbetriebe. Variante des Fokus-MVP (I1) mit anderem Vertriebskanal.",
      "typ": "variante",
      "basiert_auf": ["I1"]
    }
  ],
  "offene_punkte": [
    "Top-Idee-Set für Rot (Resonanz) und anschließend Gelb/Schwarz: I1, I3, I5, I7.",
    "I8 (Stammdaten-Netzwerk) ist strategisch interessant, aber erst ab kritischer Nutzerzahl relevant.",
    "I9 (White-Label) verschiebt das Geschäftsmodell stark und müsste separat bewertet werden."
  ],
  "konfidenz": "hoch"
}
```
