import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

import imageio_ffmpeg
plt.rcParams['animation.ffmpeg_path'] = imageio_ffmpeg.get_ffmpeg_exe()
# --- Konfiguration ---
FPS = 20                # Bilder pro Sekunde
TOTAL_FRAMES = 350      # Gesamtlänge des Videos (350 / 20 = 17,5 Sekunden)
DPI = 100               # Auflösung

# --- Figure und Axes erstellen ---
# Wir nutzen ein Layout mit links Text (Rechnung) und rechts Plot (Graphik)
fig = plt.figure(figsize=(12, 6), dpi=DPI)
fig.patch.set_facecolor('white')

# Linker Bereich für den Text (Rechnung)
ax_text = fig.add_axes([0.05, 0.1, 0.4, 0.8]) # [left, bottom, width, height]
ax_text.axis('off') # Keine Achsen anzeigen

# Rechter Bereich für den Plot (Graphik)
ax_plot = fig.add_axes([0.55, 0.1, 0.4, 0.8])
ax_plot.set_xlim(-1, 5)
ax_plot.set_ylim(-2, 6)
ax_plot.set_aspect('equal')
ax_plot.grid(True, linestyle='--', alpha=0.6)
ax_plot.axhline(0, color='black', linewidth=1.5)
ax_plot.axvline(0, color='black', linewidth=1.5)
ax_plot.set_xlabel('x', fontsize=14, loc='right')
ax_plot.set_ylabel('y', fontsize=14, rotation=0, loc='top')

# Daten für die Geraden
x_vals = np.linspace(-1, 5, 100)
y_g = 2 * x_vals - 1
y_h = -x_vals + 5

# Linien-Objekte initialisieren (noch leer)
line_g, = ax_plot.plot([], [], color='blue', linewidth=2.5, label='g: y = 2x - 1')
line_h, = ax_plot.plot([], [], color='red', linewidth=2.5, label='h: y = -x + 5')
point_s, = ax_plot.plot([], [], 'ko', markersize=8, label='S(2|3)')

ax_plot.legend(loc='upper left', fontsize=12)

# --- Animations-Funktion ---
def animate(frame):
    # 1. TEXT-BEREICH (Links) aktualisieren
    ax_text.clear()
    ax_text.axis('off')
    
    # Wir definieren die Schritte basierend auf dem Frame
    if frame < 50:
        text = "Aufgabe:\n\n$g: y = 2x - 1$\n$h: y = -x + 5$"
    elif frame < 100:
        text = "1. Gleichsetzen:\n\n$2x - 1 = -x + 5$"
    elif frame < 160:
        text = "2. Nach x auflösen:\n\n$2x - 1 = -x + 5 \quad | +x\n$ $3x - 1 = 5 \quad\quad\;\; | +1\n$ $3x = 6 \quad\quad\quad\;\;\; | :3\n$ $x = 2$"
    elif frame < 210:
        text = "3. y berechnen (Einsetzen):\n\n$y = 2 \cdot 2 - 1\n$ $y = 4 - 1\n$ $y = 3$"
    else:
        text = "Ergebnis:\n\nSchnittpunkt $S(2 \mid 3)$"

    # Text rendern (mathtext für Formeln)
    ax_text.text(0.1, 0.5, text, fontsize=20, verticalalignment='center', 
                 family='monospace', bbox=dict(facecolor='lightyellow', alpha=0.5, edgecolor='gray'))

    # 2. PLOT-BEREICH (Rechts) aktualisieren
    # Wir lassen die Geraden "wachsen", sobald die Rechnung fertig ist (ab Frame 210)
    if frame >= 210:
        # Berechnen, wie viel von der Linie schon gezeichnet ist
        progress = min((frame - 210) / 40.0, 1.0) 
        idx = int(len(x_vals) * progress)
        
        line_g.set_data(x_vals[:idx], y_g[:idx])
        line_h.set_data(x_vals[:idx], y_h[:idx])
        
    # Schnittpunkt erscheint ganz am Ende
    if frame >= 280:
        point_s.set_data([2], [3])
        
    return ax_text, line_g, line_h, point_s

# --- Video erstellen ---
print("Starte Animation... (Das kann einen Moment dauern)")
ani = animation.FuncAnimation(fig, animate, frames=TOTAL_FRAMES, interval=1000/FPS, blit=False)

# Speichern als MP4 (benötigt ffmpeg!)
# Falls ffmpeg nicht installiert ist, ändere den Dateinamen in 'schnittpunkt.gif'
output_file = 'schnittpunkt_interaktiv.mp4'
writer = animation.FFMpegWriter(fps=FPS, bitrate=1800)

try:
    ani.save(output_file, writer=writer)
    print(f"Erfolgreich gespeichert als: {output_file}")
except Exception as e:
    print(f"Fehler beim Speichern des MP4. Hast du ffmpeg installiert?")
    print("Alternativ: Ändere im Code die Endung auf .gif")
    # ani.save('schnittpunkt.gif', writer='pillow')

plt.close()
