# Manim-Apps für den Unterricht

Python-Animationen mit [Manim Community Edition](https://www.manim.community/) und matplotlib für den Mathe-Unterricht: Erklärvideos, Moodle-Banner und Kurskarten. Die fertigen MP4s lassen sich direkt in H5P Interactive Video (Moodle) einbetten.

## Setup (lokal, z. B. Visual Studio)

```bash
git clone https://github.com/schreeckkai/python.git
cd python
python -m venv .venv
.venv\\Scripts\\activate     # Windows
pip install -r requirements.txt
```

Zusätzlich nötig:
- **FFmpeg** (muss im PATH liegen; wird für MP4-Rendering benötigt)
- **LaTeX-Distribution** (z. B. [MiKTeX](https://miktex.org/)) für Formeln mit `MathTex`
- `verschieben_sinus_cosinus.py` erwartet MiKTeX unter `C:\\Users\\KaiSc\\AppData\\Local\\Programs\\MiKTeX\\miktex\\bin\\x64` (Pfad ggf. anpassen)

## Eine Szene rendern

```bash
# Video (Qualität: -ql 480p, -qm 720p, -qh 1080p, -qk 4K; -p öffnet automatisch)
manim -qh szenen/gleichungssystem.py GleichungssystemAnimation

# Standbild (Banner/Kurskarten, letztes Bild speichern)
manim -s --resolution 1920,480 szenen/kurs_banner.py KursBanner -o kurs_banner.png
```

## Struktur

```
szenen/      Manim-Szenen (eine Szene pro Datei)
  bedingte_wahrscheinlichkeit.py  Bedingte Wahrscheinlichkeit, Pfadregeln am Baumdiagramm
  ableiten_trig_funktionen.py     Ableitung gestreckter/verschobener Sinus-/Cosinus-Funktionen
  nullstellen_trig_funktionen.py  Nullstellen berechnen (2 Seiten)
  gleichungssystem.py             3x3-LGS per Gauß-Algorithmus (mit Rückwärtseinsetzen)
  schnittpunkt_geraden.py         Schnittpunkt zweier Geraden (rechnerisch + grafisch)
  verschieben_sinus_cosinus.py    Parameter b mit Einheitskreis und ValueTracker
  trigonometrische_funktionen.py  Übersicht Einheitskreis, sin/cos/tan, Dreieck
  funktionen_darstellung.py       Collage: Funktion, Ableitung, Integral
  wiederholung_grundlagen.py      Symbol-Collage für Wiederholungsstunde
  latex_to_video.py               LaTeX-Code -> Video (align*-Parser)
  latex_to_video_mixed.py         LaTeX-Code -> Video (Formeln + Fließtext)
  kurs_banner.py                  Kurs-Banner 1920x480 (Standbild)
  kurstkarten.py                  Kurskarte 1280x720, KURSNAME oben anpassen
  banner_moodle.py                Moodle-Banner (Standbild, sin/cos)
banner/      matplotlib-Scripts für Moodle-Bilder und Banner-PNGs
  ebenenbueschel_banner.py        3D-Ebenenbüschel + LGS (PNG)
  gleichungssysteme_banner.py     2x2-LGS + Schnittpunkt (PNG)
  schnittpunkt_video.py           Schnittpunkt-Video via matplotlib-Animation
sprechtexte/ Sprechtexte mit Zeitmarken passend zu den Szenen (für Erklärvideos mit Sprecher)
tools/       Hilfsskripte (LaTeX-Parser für die latex_to_video-Szenen)
sonstiges/   Sonstiges (z. B. turtle-Grafik)
media/       Render-Ausgabe von Manim (nicht committen, siehe .gitignore)
```

## Workflow: Manim -> Erklärvideo -> H5P Interactive Video

1. Szene in `szenen/` schreiben oder anpassen (passender Sprechtext in `sprechtexte/`)
2. Rendern: `manim -qh szenen/meine_szene.py MeineSzene`
3. Sprechtext aufnehmen (z. B. Audacity) und mit FFmpeg anhängen:
   `ffmpeg -i video.mp4 -i sprechtext.mp3 -c:v copy -map 0:v -map 1:a final.mp4`
4. In Moodle als **H5P Interactive Video** hochladen, Quizfragen an die Zeitmarken aus dem Sprechtext setzen
5. Nur Code committen; große Videos ggf. per Moodle oder als Release-Assets
