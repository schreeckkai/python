from manim import *
import numpy as np

# =====================================================
#  HIER DEN KURSNAMEN ANPASSEN, dann rendern mit:
#  manim -s --resolution 1280,720 .\szenen\kurstkarten.py KursKarte -o Sek12f.png
# =====================================================
KURSNAME = "Mathematik_Q1_Schreeck"

DUNKEL = "#0e1116"


# ---------- Bausteine ----------

def mini_graph(funktion, x_range, y_range, kurvenfarbe,
               x_length=3.0, y_length=1.6):
    ax = Axes(
        x_range=x_range, y_range=y_range,
        x_length=x_length, y_length=y_length,
        axis_config={"color": GREY_B, "stroke_width": 2,
                     "include_ticks": False},
    )
    graph = ax.plot(funktion, color=kurvenfarbe, stroke_width=3.5)
    return VGroup(ax, graph)


def einheitskreis(radius=0.8):
    winkel = 55 * DEGREES
    P = radius * np.array([np.cos(winkel), np.sin(winkel), 0])
    kreis = Circle(radius=radius, stroke_width=3, color=GREEN)
    r_linie = Line(ORIGIN, P, stroke_width=3, color=GREEN)
    bogen = Arc(radius=radius * 0.32, start_angle=0, angle=winkel,
                stroke_width=2.5, color=YELLOW)
    sinus = DashedLine(P, [P[0], 0, 0], stroke_width=2.5,
                       color=RED, dash_length=0.05)
    punkt = Dot(P, radius=0.05, color=YELLOW)
    return VGroup(kreis, r_linie, bogen, sinus, punkt)


def schraegbild_wuerfel(kante=1.1, tiefe=0.65):
    offset = tiefe * np.array([np.cos(45 * DEGREES),
                               np.sin(45 * DEGREES), 0])
    l2 = kante / 2
    v = [np.array([x * l2, y * l2, 0])
         for x, y in [(-1, -1), (1, -1), (1, 1), (-1, 1)]]
    h = [p + offset for p in v]
    g = VGroup()
    for i in range(4):
        g.add(Line(v[i], v[(i + 1) % 4], stroke_width=3))
        g.add(DashedLine(h[i], h[(i + 1) % 4],
                         stroke_width=2.5, dash_length=0.07))
        g.add(Line(v[i], h[i], stroke_width=3))
    return g.set_color(ORANGE)


# ---------- Szene (Bühne 16:9 = 14.2 x 8 Einheiten) ----------

class KursKarte(Scene):
    def construct(self):
        self.camera.background_color = DUNKEL

        grid = NumberPlane(
            x_range=[-7.5, 7.5, 1],
            y_range=[-4, 4, 1],
            background_line_style={"stroke_color": BLUE_E,
                                   "stroke_width": 1,
                                   "stroke_opacity": 0.15},
        )
        grid.axes.set_stroke(color=BLUE_E, width=1, opacity=0.25)

        # --- obere Reihe ---
        kubisch = mini_graph(lambda x: 0.3 * x**3 - 0.9 * x,
                             [-2.2, 2.2, 1], [-1.5, 1.5, 1], BLUE)
        kubisch.move_to([-5.6, 2.9, 0]).set_opacity(0.6)

        kreis = einheitskreis()
        kreis.move_to([-2.7, 2.9, 0]).set_opacity(0.55)

        wuerfel = schraegbild_wuerfel()
        wuerfel.move_to([2.7, 2.9, 0]).set_opacity(0.55)

        sinus = mini_graph(np.sin, [-7, 7, 3.5], [-1.6, 1.6, 1], RED)
        sinus.move_to([5.6, 2.9, 0]).set_opacity(0.6)

        # --- mittlere Reihe (neben dem Titel) ---
        matrix = MathTex(r"A=\begin{pmatrix}2&-1\\0&3\end{pmatrix}",
                         font_size=24)
        matrix.move_to([-5.9, 0.35, 0]).set_color(YELLOW).set_opacity(0.55)

        integral = MathTex(r"\int_{0}^{\pi}\sin(x)\,dx=2", font_size=22)
        integral.move_to([5.9, 0.35, 0]).set_color(GREEN).set_opacity(0.55)

        e_abl = MathTex(r"\tfrac{d}{dx}\,e^{x}=e^{x}", font_size=22)
        e_abl.move_to([-0.9, 1.55, 0]).set_color(BLUE).set_opacity(0.4)

        produkt = MathTex(r"(f\cdot g)'=f'\,g+f\,g'", font_size=20)
        produkt.move_to([1.5, -1.5, 0]).set_color("#FF69B4").set_opacity(0.4)

        # --- untere Reihe ---
        bino = BarChart(
            values=[1, 4, 6, 4, 1],
            y_range=[0, 7, 1],
            x_length=2.6, y_length=1.3,
            bar_colors=[TEAL], bar_width=0.4,
            bar_fill_opacity=0.55, bar_stroke_width=1,
            axis_config={"include_ticks": False, "include_numbers": False,
                         "stroke_width": 1.5, "color": GREY_B},
        )
        bino.move_to([-5.6, -2.9, 0]).set_opacity(0.6)

        glocke = mini_graph(lambda x: np.exp(-x**2 / 1.6),
                            [-3, 3, 1], [0, 1.15, 0.5], TEAL,
                            x_length=2.6, y_length=1.2)
        glocke.move_to([-2.0, -2.9, 0]).set_opacity(0.4)

        mitternacht = MathTex(
            r"x_{1,2}=\tfrac{-b\pm\sqrt{b^{2}-4ac}}{2a}", font_size=20)
        mitternacht.move_to([1.6, -2.9, 0]).set_color(ORANGE).set_opacity(0.45)

        gerade = MathTex(r"\vec{x}=\vec{a}+t\cdot\vec{b}", font_size=24)
        gerade.move_to([5.4, -2.9, 0]).set_color(BLUE).set_opacity(0.5)

        self.add(grid, kubisch, kreis, wuerfel, sinus, matrix, integral,
                 e_abl, produkt, bino, glocke, mitternacht, gerade)

        # --- Halo + Titel (Breite passt sich automatisch an) ---
        for breite, hoehe, op in [(11.5, 3.4, 0.12),
                                  (10, 2.8, 0.14),
                                  (8.5, 2.2, 0.16)]:
            halo = Ellipse(width=breite, height=hoehe)
            halo.set_stroke(width=0).set_fill(DUNKEL, opacity=op)
            halo.move_to([0, 0.35, 0])
            self.add(halo)

        titel = Text(KURSNAME, font_size=64, weight=BOLD, color=WHITE)
        if titel.width > 9.5:                      # lange Namen automatisch
            titel.scale(9.5 / titel.width)         # verkleinern
        akzent = Line(LEFT * (titel.width / 2 + 0.2),
                      RIGHT * (titel.width / 2 + 0.2), stroke_width=6)
        akzent.set_color([BLUE, TEAL, GREEN, YELLOW, RED])
        akzent.next_to(titel, DOWN, buff=0.3)
        VGroup(titel, akzent).move_to([0, 0.35, 0])

        self.add(titel, akzent)


if __name__ == "__main__":
    with tempconfig({
        "save_last_frame": True,
        "pixel_width": 1280,
        "pixel_height": 720,
        "background_color": DUNKEL,
    }):
        KursKarte().render()
