# Sprechtext: Bedingte Wahrscheinlichkeit (Baumdiagramm)

Szene: szenen/bedingte_wahrscheinlichkeit.py
Rendern: manim -qh szenen/bedingte_wahrscheinlichkeit.py BedingteWahrscheinlichkeit
Videolänge: ca. 57 Sekunden (mit den eingestellten run_time- und wait-Werten)

## Sprechtext mit Zeitmarken

**0:00 - Titel** (bis 0:04)
Bedingte Wahrscheinlichkeit. Heute schauen wir uns an, wie man Wahrscheinlichkeiten berechnet, wenn schon etwas passiert ist.

**0:04 - Aufgabe** (bis 0:08)
Stellt euch eine Urne vor: drei rote und zwei blaue Kugeln. Wir ziehen zwei Kugeln hintereinander, ohne zurückzulegen.

**0:08 - 1. Stufe** (bis 0:12)
Beim ersten Zug sind die Chancen klar: drei Fünftel für rot, zwei Fünftel für blau.

**0:12 - 2. Stufe** (bis 0:19)
Beim zweiten Zug wird es spannend: Nach dem ersten Zug fehlt ja schon eine Kugel. War die erste Kugel rot, sind nur noch zwei rote und zwei blaue in der Urne. War sie blau, sind es drei rote und nur noch eine blaue.

**0:19 - Hinweis** (bis 0:22)
Genau das ist der Kern der bedingten Wahrscheinlichkeit: Der zweite Zug hängt davon ab, was beim ersten passiert ist.

**0:22 - 1. Pfadregel** (bis 0:29)
Erste Pfadregel, die Produktregel: Um die Wahrscheinlichkeit eines kompletten Pfades zu bekommen, multiplizieren wir die Zahlen entlang des Pfades. Beispiel: erst blau, dann rot. Zwei Fünftel mal drei Viertel, das ergibt drei Zehntel.

**0:29 - Frage und Formel** (bis 0:36)
Jetzt die eigentliche Frage: Wie wahrscheinlich ist die zweite Kugel rot, wenn die erste blau war? Dafür gibt es die Formel: Wahrscheinlichkeit von blau und rot, geteilt durch die Wahrscheinlichkeit von blau.

**0:36 - Rechnung** (bis 0:41)
Wir setzen ein: drei Zehntel geteilt durch zwei Fünftel, also drei Zehntel mal fünf Halbe. Das ergibt drei Viertel. Und jetzt schaut auf den Baum: Die drei Viertel steht hier schon direkt am Ast. Das ist genau die bedingte Wahrscheinlichkeit.

**0:41 - 2. Pfadregel** (bis 0:49)
Zweite Pfadregel, die Summenregel: Wollen wir die Wahrscheinlichkeit, dass die zweite Kugel rot ist, egal was die erste war, dann addieren wir alle Pfade zu einem roten Endpunkt. Drei Fünftel mal zwei Viertel plus zwei Fünftel mal drei Viertel: drei Zehntel plus drei Zehntel, also drei Fünftel. Interessant: genau die gleiche Chance wie beim ersten Zug.

**0:49 - Zusammenfassung** (bis ca. 0:57)
Zum Abschluss: die Formel für bedingte Wahrscheinlichkeiten, die Produktregel entlang eines Pfades, die Summenregel über mehrere Pfade. Und merkt euch: Am Baum stehen die bedingten Wahrscheinlichkeiten direkt an den Ästen.

## Nach der Aufnahme: Ton und Video zusammenfügen

1. Sprechtext aufnehmen (z. B. in Audacity oder am Handy), als sprechtext.mp3 speichern
2. Zusammenfügen mit FFmpeg:

   ffmpeg -i bedingte_wahrscheinlichkeit.mp4 -i sprechtext.mp3 -c:v copy -map 0:v -map 1:a final.mp4

   (Das Video wird nicht neu kodiert, nur der Ton wird angehängt. Pfade ggf. anpassen.)

## Timing anpassen

Wenn deine Aufnahme länger dauert als die Szene: die self.wait(...)-Werte in der Szene erhöhen und neu rendern. Faustregel pro Absatz: ca. 1 Sekunde Puffer mehr als der Text braucht.

## Zeitmarken für H5P-Zwischenfragen

- 0:19: Was ändert sich im zweiten Zug, wenn die erste Kugel rot war?
- 0:36: Rechnet selbst: drei Zehntel geteilt durch zwei Fünftel. Was kommt raus?
- 0:48: Warum ist die Wahrscheinlichkeit für rot im zweiten Zug genauso groß wie im ersten?
