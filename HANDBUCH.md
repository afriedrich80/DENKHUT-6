# HANDBUCH

> Ausführliche Bedienungsanleitung für DENKHUT-6. Für die Theorie siehe [METHODIK.md](METHODIK.md), für die Datenstrukturen [DATENMODELL.md](DATENMODELL.md).

## Inhalt

1. [Installation Schritt für Schritt](#1-installation-schritt-für-schritt)
2. [Eine Sitzung durchführen](#2-eine-sitzung-durchführen)
3. [Die Sequenzen – und wann welche](#3-die-sequenzen--und-wann-welche)
4. [Einzelne Hüte gezielt aufrufen](#4-einzelne-hüte-gezielt-aufrufen)
5. [Iteration](#5-iteration)
6. [Tipps für gute Sitzungen](#6-tipps-für-gute-sitzungen)
7. [FAQ](#7-faq)
8. [Troubleshooting](#8-troubleshooting)

---

## 1. Installation Schritt für Schritt

**Empfohlen: Installation aus GitHub (zwei getrennte Befehle).** Nacheinander in Claude Code eingeben – ersten Befehl, Enter, kurz warten, dann den zweiten. **Nicht** beide in dieselbe Zeile, kein `→`/`…`:

```
/plugin marketplace add https://github.com/afriedrich80/DENKHUT-6.git
```

```
/plugin install denkhut-6@denkhut-6
```

Anschließend `/reload-plugins` oder Claude Code neu starten. Spätere Updates: `/plugin marketplace update denkhut-6`.

> **Kein GitHub-Account nötig.** Das Repo ist öffentlich; der Zugriff läuft anonym über HTTPS – ohne Login, ohne SSH-Key. Immer die vollständige `https://…git`-URL verwenden (nicht den Kurznamen `afriedrich80/DENKHUT-6`): der Kurzname kann lokal auf SSH auflösen und mit `Host key verification failed` scheitern. (Wer bewusst SSH will: einmalig `ssh -T git@github.com`, Fingerprint bestätigen.)

Claude Code lädt damit automatisch:
- die Subagents aus `agents/` (sechs Hüte),
- die Skills aus `skills/` (`denkhut-6`, `denkhut-sequenz`, `denkhut-protokoll`),
- den Slash-Command aus `commands/denkhut.md` → `/denkhut-6:denkhut`.

> Plugin-Skills sind **namespaced** mit `denkhut-6:`. Der Aufruf lautet daher `/denkhut-6:denkhut <Thema>` (nicht `/denkhut-6`). Alternativ triggert Claude den Orchestrator per natürlicher Sprache automatisch.

**Test.** Rufe `/denkhut-6:denkhut Test-Thema` auf. Der Blaue Hut sollte mit der Problemklärung antworten. Beim ersten Lauf entsteht `denkhut-sitzungen/` im Arbeitsverzeichnis (in `.gitignore` ausgeschlossen).

**Ohne Git / offline / hinter Firewall.** Repo als ZIP herunterladen (GitHub „Code → Download ZIP" oder eine Release-ZIP), entpacken, dann `claude --plugin-dir ./DENKHUT-6` starten – oder den Ordner als lokalen Marketplace registrieren: `/plugin marketplace add /pfad/zu/DENKHUT-6` → `/plugin install denkhut-6@denkhut-6`. Beides braucht weder Git noch GitHub-Konto.

**Als persönliche Dateien.** Die Ordner `agents/`, `skills/`, `commands/` nach `~/.claude/` bzw. `<projekt>/.claude/` kopieren – dann ohne Namespace als `/denkhut`.

---

## 2. Eine Sitzung durchführen

### Aufruf

```
/denkhut-6:denkhut Sollen wir auf die 4-Tage-Woche umstellen?
```

### Was dann passiert

1. **🔵 Blau (Start)** klärt das Problem: Beschreibung, Ziel, Scope, Constraints, Stakeholder, Entscheidungskriterien. Er wählt die Sequenz (Default: `entscheidung`).
2. **⚪ Weiß** trägt Fakten zusammen und markiert Annahmen und Wissenslücken.
3. **🟢 Grün** erzeugt Ideen und Varianten – ohne zu bewerten.
4. **🟡 Gelb** und **⚫ Schwarz** prüfen die Ideen parallel auf Nutzen bzw. Risiko.
5. **🔴 Rot** fängt die emotionale Reaktion der Stakeholder ein – ohne Begründung.
6. **🔵 Blau (Ende)** verdichtet alles zur Synthese mit Empfehlung und nächsten Schritten.

Jeder Schritt wird in `denkhut-sitzungen/<slug>/` als eigene Datei abgelegt und im `protokoll.md` mitgeschrieben.

### Beispieldialog (gekürzt)

```
Du:  /denkhut-6:denkhut Sollen wir auf die 4-Tage-Woche umstellen?

🔵 Blau: Ich fasse das Problem: Soll Firma X die Regelarbeitszeit von 5 auf
         4 Tage senken? Ziel: Produktivität und Zufriedenheit halten oder
         steigern. Stakeholder: Belegschaft, Führung, Kunden. Kriterien:
         Output, Fluktuation, Kosten. Sequenz: entscheidung. Ich starte Weiß.

⚪ Weiß: F1 (fakt) Pilotstudien zeigen oft stabile Produktivität, Quelle: Branchenreports.
         F2 (annahme) Kundenerreichbarkeit Fr. könnte leiden.
         F3 (wissensluecke) Eigene Auslastung pro Wochentag unbekannt.

🟢 Grün: I1 (neu) Voller Lohnausgleich, Fr. frei.
         I2 (variante) Rollierende freie Tage statt fixem Freitag.
         I3 (kombination) 4-Tage-Woche + Kern-Erreichbarkeit per Bereitschaft.

🟡 Gelb: N1 Attraktivität als Arbeitgeber (Idee I1, Bedingung: Output stabil, lang).
⚫ Schwarz: R1 Kundenerreichbarkeit Fr. (Idee I1, Ursache: niemand da,
         Eintritt: mittel, Auswirkung: hoch, Gegenmaßnahme möglich: ja → I3).

🔴 Rot: E1 Belegschaft: Begeisterung (stark, positiv). 
        E2 Führung: Sorge um Verlässlichkeit (mittel, negativ).

🔵 Blau: Empfehlung: Pilot mit Variante I3 (rollierend + Bereitschaft) über
         3 Monate, KPIs Output & Fluktuation. Offenes Risiko: Fr.-Erreichbarkeit.
         Nächste Schritte: Auslastungsdaten erheben (schließt F3). iteration_noetig: true.
```

---

## 3. Die Sequenzen – und wann welche

| Sequenz | Reihenfolge | Wann verwenden |
|---------|-------------|----------------|
| **entscheidung** (Default) | blau → weiss → gruen → gelb → schwarz → rot → blau | Du musst eine echte Entscheidung treffen und willst alle Aspekte. |
| **bewertung** | blau → rot → weiss → gelb → schwarz → gruen → blau | Es gibt schon eine konkrete Option, die geprüft werden soll. Rot zuerst macht den Bauch sichtbar. |
| **ideenfindung** | blau → weiss → gruen → rot → gelb → schwarz → blau | Du suchst neue Lösungen; Grün steht im Zentrum. |
| **schnell-review** | blau → weiss → gelb → schwarz → blau | Schnelle Plausibilitätsprüfung bei geringem Risiko (ohne Grün/Rot); Gelb vor Schwarz. |

Sequenz explizit wählen: Sag es dem Blauen Hut, z. B. „nutze die Sequenz *bewertung*" oder „mach ein schnell-review".

---

## 4. Einzelne Hüte gezielt aufrufen

Du musst nicht immer die volle Sequenz fahren. Beispiele:

- „Setz den **schwarzen Hut** auf für diesen Plan." → nur Risiken.
- „**Grüner Hut**: gib mir 10 Alternativen." → nur Ideen.
- „Nur **Weiß**: was wissen wir, was fehlt?" → Faktenlage.

Der jeweilige Hut-Subagent läuft dann allein und liefert seinen Output-Envelope. Der Blaue Hut kann auf Wunsch trotzdem ein kurzes Protokoll führen.

---

## 5. Iteration

Schließt der Blaue Hut mit `iteration_noetig: true`, lohnt eine weitere Runde. Typische Auslöser:

- **Offene Wissenslücken** (Weiß): erst Daten beschaffen, dann erneut bewerten.
- **Risiko mit Gegenmaßnahme** (Schwarz): Grün soll die Gegenmaßnahme als neue Variante ausarbeiten.
- **Starke negative Emotion** (Rot): Ursache klären, bevor entschieden wird.

Für die nächste Runde nennst du dem Blauen Hut das offene Element; er ruft gezielt die nötigen Hüte erneut auf. Iterationen werden im selben Sitzungsordner mit erhöhter Schrittnummer protokolliert.

---

## 6. Tipps für gute Sitzungen

- **Schwarz nicht übergewichten.** Kritik ist bequem. Gib Gelb genauso viel Raum, sonst stirbt jede Idee.
- **Rot ohne Begründung.** Lass Gefühle stehen, ohne sie zu „rechtfertigen". Genau das ist ihr Wert.
- **Grün nicht sofort bewerten.** Erst alle Ideen sammeln, dann Gelb/Schwarz. Bewertung im Grün-Schritt würgt Kreativität ab.
- **Weiß ehrlich halten.** Markiere Annahmen klar als Annahme, nicht als Fakt.
- **Blau diszipliniert moderieren.** Der Blaue Hut diskutiert nicht inhaltlich mit – er steuert.
- **Stakeholder benennen.** Rot wird viel nützlicher, wenn klar ist, *wessen* Gefühl gemeint ist.
- **Kleines Problem, kleine Sequenz.** Für Triviales reicht `schnell-review`.

---

## 7. FAQ

**F: Sind die Hüte echte Subagents oder nur Prompts in einem Kontext?**
A: Echte Claude-Code-Subagents mit isoliertem Kontext (Definitionen in `agents/`). Der Blaue Hut ruft sie über das Agent-Tool auf.

**F: Warum laufen Gelb und Schwarz parallel?**
A: Sie hängen nicht voneinander ab – beide prüfen dieselben Ideen, aber unabhängig. Parallelität spart Zeit und verhindert, dass eine Sicht die andere beeinflusst.

**F: Kann ich die Sequenz selbst festlegen?**
A: Ja. Nenne dem Blauen Hut eine der vier Sequenzen oder eine eigene Reihenfolge.

**F: Wo landen die Ergebnisse?**
A: In `denkhut-sitzungen/<slug>/` mit einer Markdown-Datei pro Schritt plus `protokoll.md`.

**F: Warum darf der rote Hut nicht begründen?**
A: Weil Gefühle keine Argumente sind. Die Methode macht implizite Widerstände nur sichtbar, wenn sie unbegründet genannt werden dürfen.

**F: Darf der schwarze Hut Lösungen vorschlagen?**
A: Nein. Schwarz nennt nur begründete Risiken. Lösungen sind Sache des Grünen Huts in der nächsten Runde.

**F: Was, wenn es schlicht keine Fakten gibt?**
A: Der weiße Hut trägt sie als `wissensluecke` ein. Das ist ein gültiges und oft wertvolles Ergebnis.

**F: Wie viele Ideen soll Grün liefern?**
A: So viele wie möglich, ohne zu bewerten. Lieber zehn rohe Ideen als zwei „sichere".

**F: Kann ich das Framework außerhalb von Claude Code nutzen?**
A: Ja – siehe [CONVENTIONS.md](CONVENTIONS.md) für die tool-neutrale Spec.

**F: Muss ich immer alle sechs Hüte verwenden?**
A: Nein. Einzelne Hüte (Abschnitt 4) oder kurze Sequenzen (`schnell-review`) sind legitim.

---

## 8. Troubleshooting

| Symptom | Ursache | Abhilfe |
|---------|---------|---------|
| `/denkhut-6:denkhut` wird nicht erkannt | Plugin nicht installiert oder nicht geladen | `/plugin install denkhut-6@denkhut-6`, dann `/reload-plugins`; Claude-Code-Version aktualisieren |
| Hut antwortet im falschen Modus (z. B. Weiß wertet) | Vor-Kontext zu breit mitgegeben | Blauer Hut soll nur den relevanten Kontext reichen (siehe DATENMODELL §Kontextflüsse) |
| Schwarz dominiert die Synthese | Schwarz-Übergewicht | Gelb gleich gewichten; Schwarz auf begründete Risiken begrenzen |
| Keine Dateien in `denkhut-sitzungen/` | Schreibrechte oder `.gitignore`-Verwirrung | Arbeitsverzeichnis und Rechte prüfen; `.gitignore` schließt nur das Committen aus, nicht das Schreiben |
| Synthese ohne Empfehlung | Sequenz abgebrochen, Blau-Ende fehlt | Sitzung bis zum letzten Blau-Schritt durchlaufen lassen |
| Rot liefert Begründungen | Rotem Hut wurden Pro/Contra mitgegeben | Rot nur Problem + Ideen knapp reichen, keine Argumente |

Vollständige Beispielsitzung zum Nachvollziehen: [`beispiel/4-tage-woche/`](beispiel/4-tage-woche/).
