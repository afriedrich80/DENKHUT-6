---
description: Startet eine 6-Denkhüte-Sitzung (DENKHUT-6). Ohne Thema führt der Skill interaktiv durch.
argument-hint: "[Thema/Fragestellung – optional]"
---

Du startest eine **DENKHUT-6**-Sitzung (De Bonos sechs Denkhüte) über den Skill `denkhut-6`.

**Fall A — der Nutzer hat ein Thema mitgegeben** (`$ARGUMENTS` ist NICHT leer):
Führe den Skill `denkhut-6` direkt für dieses Thema aus. Beginne mit der Blau-Eröffnung (Rahmen klären, ggf. 1–3 Rückfragen, Sequenz wählen, Sitzungsordner anlegen).

**Fall B — KEIN Thema mitgegeben** (`$ARGUMENTS` ist leer):
Starte **noch keine** Analyse. Gib zuerst diese kurze Begrüßung + Hilfestellung aus und **warte** auf die Antwort des Nutzers:

> 👒 **DENKHUT-6 — Denken mit den sechs Hüten**
> Ich betrachte deine Frage nacheinander aus sechs getrennten Perspektiven – Fakten (Weiß), Ideen (Grün), Nutzen (Gelb), Risiken (Schwarz), Gefühl (Rot) – und der Blaue Hut fasst alles zu einer klaren Empfehlung mit nächsten Schritten zusammen.
>
> **Womit sollen wir starten? Schreib einfach dein Anliegen**, z. B.:
> • **Entscheidung:** „Sollen wir eine 4-Tage-Woche einführen?"
> • **Idee / Produktidee:** „Idee: Nachbarschafts-Werkzeugverleih"
> • **Etwas bewerten:** „Bewerte meinen Plan, X zu tun"
> • **Schneller Check:** „Schnell-Review: sollen wir Tool Y kaufen?"
>
> Du kannst dazu sagen, ob es eine **Entscheidung, Ideenfindung, Bewertung** oder ein **schnelles Review** ist – sonst wähle ich die passende Sequenz selbst.

Sobald der Nutzer sein Anliegen nennt, führe den Skill `denkhut-6` damit aus (Blau-Eröffnung, ggf. 1–3 Rückfragen, dann die Hut-Phasen).

---
Hinweis zur Ausführung: Spawne die Fach-Hüte als echte Subagents über das Agent-Tool – Weiß vor den faktenbasierten Hüten (Grün/Gelb/Schwarz), Gelb und Schwarz parallel. Rot darf je nach Sequenz früher stehen.
