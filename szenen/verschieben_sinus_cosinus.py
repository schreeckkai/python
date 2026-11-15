import os
import sys
from manim import *
import numpy as np

# --- Zwingt Manim, den lokalen MiKTeX-Pfad zu nutzen ---
possible_paths = [
    r"C:\Users\KaiSc\AppData\Local\Programs\MiKTeX\miktex\bin\x64",
    r"C:\Program Files\MiKTeX\miktex\bin\x64"
]
for path in possible_paths:
    if os.path.exists(path):
        os.environ["PATH"] = path + os.pathsep + os.environ["PATH"]
        break

class ParameterBAnimation(Scene):
    def construct(self):
        # 1. Koordinatensystem und Einheitskreis
        circle = Circle(radius=1.5, color=WHITE).shift(LEFT * 4 + DOWN * 0.8)
        
        # Achsen definieren
        axes = Axes(
            x_range=[0, 4 * PI + 0.5, PI],
            y_range=[-2, 2, 1],
            x_length=7,
            y_length=4,
            axis_config={"include_tip": True}
        ).shift(RIGHT * 2 + DOWN * 0.8)
        
        # --- Professionelle Achsenbeschriftung mit LaTeX ---
        x_labels = {
            PI: MathTex(r"\pi"),
            2 * PI: MathTex(r"2\pi"),
            3 * PI: MathTex(r"3\pi"),
            4 * PI: MathTex(r"4\pi")
        }
        y_labels = {
            -1: MathTex("-1"),
            1: MathTex("1")
        }
        axes.get_x_axis().add_labels(x_labels)
        axes.get_y_axis().add_labels(y_labels)

        self.play(Create(circle), Create(axes))
        
        # Ein zentraler Zeit-Tracker für die gesamte Animation
        t = ValueTracker(0.01)
        
        # Ausgelagerte Funktion zum Erstellen der Zeichen-Objekte
        def create_sine_tracker(b_val, color):
            dot = Dot(color=color, radius=0.1)
            dot.add_updater(lambda d: d.move_to(
                circle.get_center() + np.array([
                    1.5 * np.cos(b_val * t.get_value()), 
                    1.5 * np.sin(b_val * t.get_value()), 
                    0
                ])
            ))
            
            graph = VMobject(color=color, stroke_width=3)
            graph.add_updater(lambda g: g.become(
                axes.plot(lambda x: 1.5 * np.sin(b_val * x), x_range=[0.01, t.get_value()], color=color)
            ))
            
            line = Line(color=color, stroke_width=2, stroke_opacity=0.5)
            line.add_updater(lambda l: l.put_start_and_end_on(
                dot.get_center(),
                axes.c2p(t.get_value(), 1.5 * np.sin(b_val * t.get_value()))
            ))
                
            return dot, graph, line

        # Hilfsfunktion zum sauberen Löschen nach jedem Einzelschritt
        def cleanup_tracker(dot, graph, line):
            dot.clear_updaters()
            graph.clear_updaters()
            line.clear_updaters()
            self.play(FadeOut(dot), FadeOut(graph), FadeOut(line), run_time=0.5)

        # Die drei Formeln oben links aufbauen
        eq_1 = MathTex(r"f(x) = \sin(1 \cdot x)", color=RED).to_edge(UP, buff=0).shift(LEFT * 1)
        eq_2 = MathTex(r"f(x) = \sin(2 \cdot x)", color=GREEN).next_to(eq_1, DOWN, aligned_edge=LEFT)
        # 0{,}5 sorgt in LaTeX für das korrekte deutsche Komma ohne störendes Leerzeichen!
        eq_3 = MathTex(r"f(x) = \sin(0{,}5 \cdot x)", color=BLUE).next_to(eq_2, DOWN, aligned_edge=LEFT)

        # --- Schritt 1: b = 1 (Rot) ---
        t.set_value(0.01)
        dot_1, graph_1, line_1 = create_sine_tracker(1, RED)
        self.play(FadeIn(dot_1), Write(eq_1))
        self.add(graph_1, line_1)
        self.play(t.animate.set_value(4 * PI), run_time=4, rate_func=linear)
        cleanup_tracker(dot_1, graph_1, line_1)
        
        # --- Schritt 2: b = 2 (Grün) ---
        t.set_value(0.01)
        dot_2, graph_2, line_2 = create_sine_tracker(2, GREEN)
        self.play(FadeIn(dot_2), Write(eq_2))
        self.add(graph_2, line_2)
        self.play(t.animate.set_value(4 * PI), run_time=4, rate_func=linear)
        cleanup_tracker(dot_2, graph_2, line_2)

        # --- Schritt 3: b = 0.5 (Blau) ---
        t.set_value(0.01)
        dot_3, graph_3, line_3 = create_sine_tracker(0.5, BLUE)
        self.play(FadeIn(dot_3), Write(eq_3))
        self.add(graph_3, line_3)
        self.play(t.animate.set_value(4 * PI), run_time=4, rate_func=linear)
        cleanup_tracker(dot_3, graph_3, line_3)
        
        # --- Schritt 4: Das große Finale (Alle gemeinsam) ---
        t.set_value(0.01)
        d1, g1, l1 = create_sine_tracker(1, RED)
        d2, g2, l2 = create_sine_tracker(2, GREEN)
        d3, g3, l3 = create_sine_tracker(0.5, BLUE)
        
        self.play(FadeIn(d1), FadeIn(d2), FadeIn(d3))
        self.add(g1, l1, g2, l2, g3, l3)
        # Läuft etwas langsamer (6 Sekunden), damit die Schüler den Unterschied erkennen
        self.play(t.animate.set_value(4 * PI), run_time=6, rate_func=linear)
        
        # Am Ende die Verbindungslinien ausblenden, damit das Bild sauber bleibt
        l1.clear_updaters(); l2.clear_updaters(); l3.clear_updaters()
        self.play(FadeOut(l1), FadeOut(l2), FadeOut(l3))
        
        self.wait(3)

if __name__ == "__main__":
    os.system('manim -pqh szenen/verschieben_sinus_cosinus.py ParameterBAnimation')
