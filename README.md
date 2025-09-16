# Demo Repository zur Vorstellung von Git

> [!NOTE]
> Repository für das Modul **"Konzepte dynamischer Programmiersprachen"** (Python) des FOM WS25.

## Was ist Git?

Git ist eine Software zur Versionskontrolle von Dateien und wird vorallem in der Programmierung verwendet. Es ermöglicht das erstellen von Projekten, die Zusammenarbeit mit anderen Entwicklern und die parallele Arbeit an Features oder Bugfixes. Sie ist für alle gängigen Betriebssysteme verfügbar.

GitHub hingegen ist ein Cloudspeicher für solche Projekte und vereinfacht die Kollaboration durch ein benutzerfreundliches Interface und weiteren Funktionen.

## Wichtigste Befehle

Hier kommen noch einmal die wichtigsten git-Commands aus der Präsentation.
Für eine kurze und übersichtliche Zusammenfassung gibt es auch das [GIT CHEAT SHEET](https://education.github.com/git-cheat-sheet-education.pdf) zum herunterladen.
Außerdem könnt ihr euch eine komplette Liste _aller_ Befehle über den Command `git help` bzw. `git -h` ausgeben lassen oder die [offizielle git](https://git-scm.com/docs) Dokumentation aufrufen.

**Projekt anlegen oder herunterladen**
- Repository erstellen (lokal): `git init`
- Repositoy klonen: `git clone <repo.url> <file/path>`

**Mit Dateien arbeiten**
- Datei zur Versionskontrolle hinzufügen: `git add <file_name.py>`
- Snapshot erstellen: `git commit -m "Nachricht"`
- Letzte gespeicherte Version hochladen: `git push` (Main Branch)
  - oder auf einen bestimmten Branch hochladen: `git push origin <branch_name>`

**Kollaboration**
- Aktuelle Projektversion herunterladen und zusammenführen: `git pull`
  - nur herunterladen: `git fetch`
  - zusammenführen: `git merge`
- Bereits bestehende Datei verschieben: `git mv <old/file/path/file_name.py> <new/file/path>`
