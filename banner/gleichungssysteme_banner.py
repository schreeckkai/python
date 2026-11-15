import matplotlib.pyplot as plt
import numpy as np

# 1. Bildgröße im exakten Seitenverhältnis festlegen
fig = plt.figure(figsize=(22.34, 4.32), facecolor='#1C1C1C')

# 2. Linke Seite: Titel und Formel im Manim-Look (Matplotlib-kompatibles LaTeX)
ax_text = fig.add_axes([0, 0, 0.5, 1], facecolor='#1C1C1C')
ax_text.axis('off')
ax_text.text(0.1, 0.65, "Lineare Gleichungssysteme", fontsize=38, color='#50B4FF', weight='bold')

# Hier nutzen wir nun eine Matplotlib-kompatible geschweifte Klammer
lgs_text = "$\t{I: } 2x + y = 5$\n$\t{II: } x - y = 1$"
ax_text.text(0.2, 0.25, lgs_text, fontsize=32, color='white', linespacing=1.5)

# 3. Rechte Seite: Das Koordinatensystem
ax_graph = fig.add_axes([0.55, 0.15, 0.4, 0.7], facecolor='#1C1C1C')
x = np.linspace(-1, 5, 100)

# Graphen mit Manim-typischen Farben zeichnen
ax_graph.plot(x, 5 - 2*x, color='#58C4DD', linewidth=4)  # Hellblau
ax_graph.plot(x, x - 1, color='#F3D146', linewidth=4)    # Gelb
ax_graph.plot(2, 1, 'o', color='#FC6262', markersize=12) # Roter Schnittpunkt
ax_graph.text(2.3, 1.1, "P(2|1)", color='#FC6262', fontsize=22)

# Achsen stylen (Dunkler Hintergrund-Stil)
ax_graph.set_xlim(-1, 5)
ax_graph.set_ylim(-1, 4)
ax_graph.spines['left'].set_color('#888888')
ax_graph.spines['bottom'].set_color('#888888')
ax_graph.spines['top'].set_visible(False)
ax_graph.spines['right'].set_visible(False)
ax_graph.tick_params(colors='#888888', labelsize=18)
ax_graph.grid(True, color='#333333', linestyle=':')

# 4. Bild direkt abspeichern
plt.savefig('moodle_lgs_banner.png', dpi=100, bbox_inches='tight')
print("Das Moodle-Banner wurde erfolgreich als 'moodle_lgs_banner.png' gespeichert!")
