---
name: denkhut-sequenz
description: Wählt die passende Hut-Reihenfolge (Sequenz) für eine DENKHUT-6-Sitzung je nach Use-Case. Nutze dies, wenn unklar ist "welche Reihenfolge", "welche Sequenz", "welche Hüte zuerst" oder welcher Denk-Ablauf zur Aufgabe (Entscheidung, Bewertung, Ideenfindung, Schnell-Review) passt.
---

# DENKHUT-6 · Sequenzwahl

Die Reihenfolge der Hüte bestimmt das Ergebnis. De Bono nennt das den **Sequence Design**: Für jeden Aufgabentyp gibt es eine bewährte Abfolge. Dieser Skill liefert dem Blauen Hut (Orchestrator) die passende Sequenz.

## Die 4 Standard-Sequenzen

| Use-Case | Sequenz | Begründung |
|----------|---------|------------|
| **entscheidung** (Default) | blau → weiss → gruen → gelb → schwarz → rot → blau | Fakten zuerst, dann Optionen erzeugen, dann ausgewogen Nutzen vs. Risiken, am Ende Bauchgefühl als Korrektiv, Blau synthetisiert. Robuster Allzweck-Ablauf für Entscheidungen. |
| **bewertung** | blau → rot → weiss → gelb → schwarz → gruen → blau | Erst ungefiltertes Bauchgefühl zur bestehenden Sache, dann Fakten, dann Nutzen/Risiken; Grün spät, um konkrete Verbesserungen aus der Kritik abzuleiten. Für das Beurteilen eines vorliegenden Vorschlags. |
| **ideenfindung** | blau → weiss → gruen → rot → gelb → schwarz → blau | Faktenbasis, dann breite Ideengenerierung, dann Intuition zur Auswahl der vielversprechenden, erst danach Nutzen/Risiken – Kritik kommt bewusst spät, um Kreativität nicht früh abzuwürgen. |
| **schnell-review** | blau → weiss → gelb → schwarz → blau | Minimal-Ablauf: Fakten, dann Nutzen, dann Risiken (Gelb **vor** Schwarz, gern parallel), Synthese. Für schnelle Go/No-Go-Checks bei **geringem Risiko**; verzichtet bewusst auf Grün und Rot (kein kreatives und kein emotionales Korrektiv – daher nur für risikoarme Fälle). Schwarz bleibt mit Gelb gepaart, nie alleinige Stimme. |

## Auswahl-Heuristik
- **Es gibt mehrere Optionen und wir müssen wählen** → `entscheidung`.
- **Ein konkreter Vorschlag liegt vor und soll beurteilt werden** → `bewertung`.
- **Wir suchen neue Lösungen / das Lösungsfeld ist offen** → `ideenfindung`.
- **Schneller Check, wenig Zeit, geringes Risiko** → `schnell-review`.
- Im Zweifel: **`entscheidung`** (Default).

## Parallelitätsregeln (gelten in jeder Sequenz)
- **Blau** immer **zuerst** (Rahmen) und **zuletzt** (Synthese).
- **Weiß** steht vor den **faktenbasierten Hüten** (Grün/Gelb/Schwarz) – gemeinsame Faktenbasis. **Rot** ist faktenunabhängig und darf je nach Sequenz früher stehen (z. B. `bewertung`: Rot vor Weiß).
- **Gelb & Schwarz** dürfen **parallel** gespawnt werden (bewerten denselben Bewertungsgegenstand unabhängig).
- **Schwarz nie alleinige Stimme** – stets mit Gelb (und/oder Grün) gepaart.

Die parallele Ausführung verändert die *logische* Sequenz nicht: In der Reihenfolge benachbarte unabhängige Hüte (typisch Gelb/Schwarz) werden in EINER Nachricht zusammen über das Agent-Tool gespawnt.

## Bewertungsgegenstand bei Sequenzen ohne vorgelagertes Grün
In `bewertung` und `schnell-review` laufen Gelb/Schwarz (und ggf. Rot) **vor** dem Grünen Hut – es gibt also noch keine Grün-Ideen zu bewerten. Bewertungsgegenstand ist dann der **vorliegende Vorschlag bzw. die zu prüfenden Optionen**. Der Blaue Hut hält diese in der Eröffnung als Ideen-Einträge `I1..` fest, damit Gelb/Schwarz/Rot wie gewohnt über `bezug_idee`/`bezug` darauf verweisen. Ein später folgender Grüner Hut (z. B. in `bewertung`) vergibt fortlaufende IDs für neu erzeugte Verbesserungsideen.

## Anpassbarkeit
Die Sequenzen sind Vorlagen, keine Dogmen. Der Blaue Hut darf anpassen, wenn der Fall es verlangt – etwa eine zweite Grün-Runde nach kritischem Schwarz-Befund, oder Rot vorziehen, wenn die Stimmungslage das Hauptthema ist. Jede Abweichung wird im Protokoll begründet.
