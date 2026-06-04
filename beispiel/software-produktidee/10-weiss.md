# ⚪ Weiß — Fakten, Annahmen, Wissenslücken

Der weiße Hut sammelt nur Information — neutral, ohne Wertung und ohne Ideen.
Jeder Eintrag ist als **Fakt**, **Annahme** oder **Wissenslücke** markiert.

## Faktenlage

| ID | Aussage | Typ | Konfidenz |
|----|---------|-----|-----------|
| F1 | In Deutschland gibt es rund 1 Mio. Handwerksbetriebe, die große Mehrheit sind Kleinstbetriebe mit unter 10 Beschäftigten. | fakt | hoch |
| F2 | Angebotserstellung gilt in Befragungen als ungeliebte, oft abends/am Wochenende erledigte Bürotätigkeit. | annahme | mittel |
| F3 | Es existieren etablierte Handwerker-Software-Suiten (Auftragsabwicklung inkl. Angebote), aber kein verbreitetes Tool mit Sprache-zu-Angebot als Kern. | annahme | mittel |
| F4 | Moderne Speech-to-Text-Dienste erreichen bei deutscher Sprache in ruhiger Umgebung sehr hohe Genauigkeit; auf lauten Baustellen sinkt sie deutlich. | fakt | hoch |
| F5 | LLM-API-Kosten pro generiertem Angebotsentwurf liegen im niedrigen Cent- bis unteren zweistelligen Cent-Bereich — bei hohem Volumen relevant, aber kein K.-o. | annahme | mittel |
| F6 | Die tatsächliche Zahlungsbereitschaft kleiner Betriebe für ein reines Angebots-Tool (€/Monat) ist nicht belegt. | wissensluecke | niedrig |
| F7 | Verlässliche Preise und Mengen entstehen nur, wenn gewerkespezifische Stammdaten (Leistungspositionen, Einheitspreise) hinterlegt sind; diese unterscheiden sich je Gewerk und Region stark. | fakt | hoch |

## Notizen

- F1/F2 betreffen Marktgröße und Schmerzpunkt; F2 ist annahmebasiert, eine
  repräsentative Erhebung aus Problem-Interviews liegt nicht vor.
- F6 ist eine offene Wissenslücke zum Geschäftsmodell; validierte
  Pricing-Daten sind nicht erhoben.
- F4 und F7 betreffen die technische Machbarkeit und die Qualität des
  Kern-Workflows.

```json
{
  "hut": "weiss",
  "phase_nr": 2,
  "zusammenfassung": "Sieben Informationseinträge zu Markt (F1/F2), Wettbewerb (F3), Technik (F4/F5/F7) und Geschäftsmodell (F6). Marktgröße und Schmerzpunkt sind plausibel, aber die Zahlungsbereitschaft (F6) ist eine offene Wissenslücke, und die Angebotsqualität hängt an gewerkespezifischen Stammdaten (F7).",
  "eintraege": [
    {
      "id": "F1",
      "aussage": "In Deutschland gibt es rund 1 Mio. Handwerksbetriebe, überwiegend Kleinstbetriebe mit unter 10 Beschäftigten.",
      "typ": "fakt",
      "quelle": "Branchenstatistik Handwerk (ZDH/Statistisches Bundesamt, Größenordnung)",
      "konfidenz": "hoch"
    },
    {
      "id": "F2",
      "aussage": "Angebotserstellung gilt als ungeliebte Bürotätigkeit, die häufig abends oder am Wochenende erledigt wird.",
      "typ": "annahme",
      "quelle": "Qualitative Hinweise aus Branchenforen/Gesprächen, noch nicht repräsentativ belegt",
      "konfidenz": "mittel"
    },
    {
      "id": "F3",
      "aussage": "Es gibt etablierte Handwerker-Software-Suiten mit Angebotsmodul, aber kein verbreitetes Tool mit Sprache-zu-Angebot als Kernfunktion.",
      "typ": "annahme",
      "quelle": "Marktsichtung Wettbewerber, nicht abschließend recherchiert",
      "konfidenz": "mittel"
    },
    {
      "id": "F4",
      "aussage": "Speech-to-Text erreicht bei Deutsch in ruhiger Umgebung sehr hohe Genauigkeit; auf lauten Baustellen sinkt die Erkennungsrate deutlich.",
      "typ": "fakt",
      "quelle": "Allgemeiner Stand der Sprachtechnologie / Benchmarks",
      "konfidenz": "hoch"
    },
    {
      "id": "F5",
      "aussage": "LLM-API-Kosten pro Angebotsentwurf liegen im niedrigen Cent- bis unteren zweistelligen Cent-Bereich; bei hohem Volumen relevant, aber kein K.-o.-Kriterium.",
      "typ": "annahme",
      "quelle": "Überschlagsrechnung aktueller LLM-API-Preise, abhängig vom Modell",
      "konfidenz": "mittel"
    },
    {
      "id": "F6",
      "aussage": "Die tatsächliche Zahlungsbereitschaft kleiner Betriebe für ein reines Angebots-Tool (in EUR/Monat) ist nicht belegt.",
      "typ": "wissensluecke",
      "quelle": "Keine validierten Pricing-Daten vorhanden",
      "konfidenz": "niedrig"
    },
    {
      "id": "F7",
      "aussage": "Verlässliche Preise/Mengen entstehen nur mit gewerkespezifischen Stammdaten (Leistungspositionen, Einheitspreise), die je Gewerk und Region stark variieren.",
      "typ": "fakt",
      "quelle": "Branchenlogik Kalkulation/LV im Handwerk",
      "konfidenz": "hoch"
    }
  ],
  "offene_punkte": [
    "Fehlt: Daten zur Zahlungsbereitschaft (F6) aus Pricing-Test oder Interviews sind nicht erhoben.",
    "Offen: die Wettbewerbslandschaft (F3) ist nicht abschließend recherchiert.",
    "Offen: die Robustheit der Spracherkennung in Baustellenlärm (F4) ist praktisch nicht getestet."
  ],
  "konfidenz": "mittel"
}
```
