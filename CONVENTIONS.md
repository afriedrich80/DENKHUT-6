# CONVENTIONS – Tool-neutrale Spezifikation

> Diese Spec beschreibt DENKHUT-6 **konzeptuell und implementierungsunabhängig**. Sie enthält keine Claude-Code-Spezifika und lässt sich mit jedem Agent-Runner, einer reinen API-Anbindung oder sogar manuell umsetzen. Für die Claude-Code-Umsetzung siehe README/HANDBUCH; für die Datenstrukturen DATENMODELL.md.

## 1. Grundmodell

Ein **Denksystem** besteht aus sieben Rollen: sechs **Hut-Rollen** (Denkmodi) und einer **Orchestrator-Rolle** (Blau). Jede Rolle ist eine reine Funktion: Sie nimmt einen definierten Eingabe-Kontext und liefert einen typisierten Ausgabe-Envelope. Rollen halten keinen geteilten Zustand; der Orchestrator ist die einzige Instanz, die alle Beiträge kennt und zusammenführt.

**Invariante:** Eine Hut-Rolle darf ausschließlich in ihrem Modus arbeiten. Ein faktenliefernder Hut wertet nicht; ein kritisierender Hut schlägt nicht vor. Diese Trennung ist die zentrale Designregel und muss durch die Implementierung erzwungen werden (separate Instruktion, isolierter Kontext).

## 2. Die Rollen

| Rolle | Modus | Darf | Darf nicht |
|-------|-------|------|------------|
| Weiß | Fakten & Information | Daten nennen, Fakt/Annahme/Lücke trennen, recherchieren | bewerten, urteilen |
| Rot | Gefühle & Intuition | Emotionen pro Stakeholder nennen | Gefühle begründen |
| Schwarz | Risiko & Kritik | begründete Risiken nennen | Lösungen vorschlagen |
| Gelb | Nutzen & Wert | Chancen, Werte, Erfolgsbedingungen nennen | Risiken nennen |
| Grün | Kreativität | Ideen, Varianten, Kombinationen erzeugen | Ideen bewerten |
| Blau | Prozess & Synthese | Problem klären, Sequenz steuern, zusammenfassen, entscheiden | inhaltlich mitargumentieren |

## 3. Ein-/Ausgaben je Rolle

Der Orchestrator reicht jeder Rolle nur den **minimal nötigen** Vor-Kontext.

| Rolle | Eingabe | Ausgabe |
|-------|---------|---------|
| Blau (Start) | Roh-Thema | Problem-Objekt, gewählte Sequenz |
| Weiß | Problem | Liste von Fakten |
| Grün | Problem, Fakten | Liste von Ideen |
| Gelb | Problem, Bewertungsgegenstand (Ideen **oder** vorgelegte Optionen) | Liste von Nutzenpunkten |
| Schwarz | Problem, Bewertungsgegenstand (Ideen **oder** vorgelegte Optionen) | Liste von Risiken |
| Rot | Problem, Bewertungsgegenstand (knapp) | Liste von Emotionen |
| Blau (Ende) | alle Ausgaben | Synthese, Protokoll |

Gelb und Schwarz erhalten denselben Bewertungsgegenstand, aber **nicht** die Ausgabe der jeweils anderen Rolle. Rot erhält **keine** Pro/Contra-Argumente.

**Bewertungsgegenstand:** In Sequenzen ohne vorgelagerten Grünen Hut (`bewertung`, `schnell-review`) registriert Blau die zu bewertenden Optionen bzw. den Vorschlag als Ideen-Einträge (`I1..`), auf die Gelb/Schwarz/Rot via `bezug_idee`/`bezug` verweisen. So bleibt die Referenzierung in jeder Sequenz identisch.

## 4. Output-Envelope

Jede Hut-Rolle liefert einheitlich:

```
{
  hut:              <weiss|rot|schwarz|gelb|gruen|blau>,
  phase_nr:         <ganzzahl>,
  zusammenfassung:  <text>,
  eintraege:        [ <typisierte Beiträge> ],
  offene_punkte:    [ <text> ],
  konfidenz:        <hoch|mittel|niedrig>
}
```

Blau hält `eintraege` leer (`[]`): die **Eröffnung** nutzt die Felder `problem` und `sequenz`, der **Abschluss** das Feld `synthese`. Die typisierten Beiträge (Fakt, Idee, Emotion, Nutzenpunkt, Risiko) und die `Synthese` sowie ihre Felder sind in [DATENMODELL.md](DATENMODELL.md) vollständig definiert und für jede Implementierung verbindlich.

## 5. Orchestrierungs-Workflow

1. **Problem fassen (Blau).** Orchestrator wandelt das Roh-Thema in ein Problem-Objekt mit Ziel, Scope, Constraints, Stakeholdern und Entscheidungskriterien.
2. **Sequenz wählen (Blau).** Eine der definierten Sequenzen (s. u.) oder eine begründete eigene.
3. **Hüte ausführen.** Der Orchestrator durchläuft die Sequenz, reicht jeder Rolle ihren Eingabe-Kontext und sammelt den Envelope ein.
4. **Parallelisieren.** Rollen ohne gegenseitige Abhängigkeit (Gelb, Schwarz) werden gleichzeitig ausgeführt.
5. **Synthese (Blau).** Alle Beiträge werden zu Empfehlung, offenen Risiken und nächsten Schritten verdichtet.
6. **Iterieren (Human-Gate).** Bei `iteration_noetig` **schlägt** Blau eine gezielte weitere Runde **vor** und holt die **Freigabe des Menschen** ein. Ohne Zustimmung endet der Prozess mit der Empfehlung. Es iteriert nichts automatisch; die Zahl der Durchläufe bestimmt der Mensch.

### Sequenzen

| Name | Reihenfolge |
|------|-------------|
| entscheidung (Default) | blau → weiss → gruen → gelb → schwarz → rot → blau |
| bewertung | blau → rot → weiss → gelb → schwarz → gruen → blau |
| ideenfindung | blau → weiss → gruen → rot → gelb → schwarz → blau |
| schnell-review | blau → weiss → gelb → schwarz → blau |

**Parallelitätsregeln:** Weiß steht vor den faktenbasierten Hüten (Grün/Gelb/Schwarz); Rot ist faktenunabhängig und darf je nach Sequenz früher stehen (z. B. `bewertung`: Rot vor Weiß). Gelb und Schwarz laufen parallel. Blau steht immer zuerst und zuletzt.

## 6. Governance und Logging

- **Protokollpflicht.** Jeder ausgeführte Schritt erzeugt einen Logeintrag mit `schritt_nr`, `hut`, `zeit`, `input_referenz`, `output_referenz`. Das Protokoll macht die Sitzung reproduzierbar und auditierbar.
- **Nachvollziehbarkeit.** Jeder Eintrag (Fakt, Idee, …) trägt eine stabile ID; spätere Rollen referenzieren diese IDs (`bezug_idee`, `basiert_auf`), sodass die Herkunft jeder Aussage rückverfolgbar ist.
- **Modus-Integrität.** Die Implementierung sollte Verstöße gegen die Modus-Trennung erkennen oder verhindern (z. B. ein wertender Satz im Weiß-Output). Mindestens muss der Orchestrator solche Fälle markieren.
- **Persistenz.** Sitzungen werden strukturiert abgelegt – eine Datei/ein Datensatz pro Schritt plus Protokoll. Die konkrete Ablageform ist implementierungsfrei; die Reihenfolge der Schritte muss erhalten bleiben.
- **Entscheidungstrennung.** Das System strukturiert das Denken und gibt eine **Empfehlung** – die Verantwortung für die Entscheidung bleibt beim Menschen.

## 7. Erweiterbarkeit

- **Neue Sequenzen** sind zulässig, solange die Parallelitätsregeln (Abschnitt 5) eingehalten werden.
- **Zusätzliche Stakeholder-Dimensionen** im roten Hut sind erlaubt, solange Gefühle unbegründet bleiben.
- **Recherche** ist allein dem weißen Hut vorbehalten und muss als Quelle im Fakt vermerkt werden.
- Die **Feldnamen und Enum-Werte** des Datenmodells sind nicht erweiterbar, ohne die Kompatibilität zu brechen – Erweiterungen erfolgen additiv über neue, klar benannte Felder.
