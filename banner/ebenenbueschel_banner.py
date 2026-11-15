import matplotlib.pyplot as plt
import numpy as np

# 1. Bildgröße im exakten Seitenverhältnis festlegen (2234 x 432)
# Ändere die Höhe von 4.32 auf z. B. 2.50 (entspricht 250 Pixeln)
fig = plt.figure(figsize=(22.34, 2.50), facecolor='#1C1C1C')


# 2. Linke Seite: Nur noch das saubere 3D-Gleichungssystem ohne Überschrift
ax_text = fig.add_axes([0.05, 0.1, 0.35, 0.8], facecolor='#1C1C1C')
ax_text.axis('off')

lgs_text = (
    "$\t{I:   } 2x + y - z = 2$\n"
    "$\t{II:  } x - y + 2z = 4$\n"
    "$\t{III: } 3x + y + z = 7$"
)
# Text zentrierter und etwas größer platziert
ax_text.text(0.1, 0.35, lgs_text, fontsize=32, color='white', linespacing=1.8)

# 3. Rechte Seite: Größeres und weiter mittig platziertes 3D-Ebenenbüschel
# Position von [0.50, ...] auf [0.42, ...] verschoben und vergrößert
ax_graph = fig.add_axes([0.42, -0.2, 0.55, 1.4], projection='3d', facecolor='#1C1C1C')
ax_graph.set_facecolor('#1C1C1C')

# Gitter für die Ebenen berechnen
X, Y = np.meshgrid(np.linspace(-2, 4, 20), np.linspace(-2, 4, 20))

# Ebenengleichungen
Z1 = 2 * X + Y - 2
Z2 = (X - Y - 4) / -2
Z3 = 7 - 3 * X - Y

# Ebenen im Manim-Look zeichnen
ax_graph.plot_surface(X, Y, Z1, color='#58C4DD', alpha=0.5, rstride=100, cstride=100, linewidth=0.5, edgecolors='white') 
ax_graph.plot_surface(X, Y, Z2, color='#F3D146', alpha=0.4, rstride=100, cstride=100, linewidth=0.5, edgecolors='white') 
ax_graph.plot_surface(X, Y, Z3, color='#83C167', alpha=0.4, rstride=100, cstride=100, linewidth=0.5, edgecolors='white') 

# Schnittgerade leuchtend hervorheben
t = np.linspace(-2, 4, 100)
x_line = 2 + 1/3 * t
y_line = -2 + 5/3 * t
z_line = t
ax_graph.plot(x_line, y_line, z_line, color='#FC6262', linewidth=6, zorder=10)

# Achsenbegrenzungen & Ausblenden des Standardrahmens
ax_graph.set_xlim(-2, 4)
ax_graph.set_ylim(-2, 4)
ax_graph.set_zlim(-2, 6)
ax_graph.set_axis_off() 

# Blickwinkel leicht optimiert für die neue Position
ax_graph.view_init(elev=22, azim=30)

# 4. Bild speichern
plt.savefig('moodle_lgs_banner.png', dpi=100, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
print("Das optimierte 3D-Moodle-Banner wurde erfolgreich gespeichert!")
