from manim import *

class SchnittpunktZweierGeraden(Scene):
    def construct(self):
        # === TITEL ===
        title = Text("Schnittpunkt zweier Geraden", font_size=48, color=BLUE)
        self.play(Write(title), run_time=1.5)
        self.wait(1)
        self.play(FadeOut(title))
        
        # === AUFGABE ZEIGEN ===
        aufgabe_title = Text("Aufgabe:", font_size=36, color=YELLOW).to_edge(UP, buff=0.5)
        
        g_eq = MathTex(r"g:", r"y", r"=", r"2x", r"-", r"1", font_size=48)
        g_eq[0].set_color(BLUE)
        g_eq.move_to(UP * 1.5)
        
        h_eq = MathTex(r"h:", r"y", r"=", r"-x", r"+", r"5", font_size=48)
        h_eq[0].set_color(RED)
        h_eq.next_to(g_eq, DOWN, buff=0.8)
        
        self.play(Write(aufgabe_title), run_time=0.8)
        self.play(Write(g_eq), run_time=1)
        self.play(Write(h_eq), run_time=1)
        self.wait(2)
        
        # === SCHRITT 1: GLEICHSETZEN ===
        schritt1_title = Text("1. Gleichsetzen:", font_size=32, color=GREEN).to_edge(UP, buff=0.5)
        
        gleichung = MathTex(r"2x - 1", r"=", r"-x + 5", font_size=48)
        gleichung.move_to(ORIGIN)
        
        self.play(
            FadeOut(aufgabe_title),
            FadeOut(g_eq),
            FadeOut(h_eq),
            Write(schritt1_title),
            run_time=1
        )
        self.play(Write(gleichung), run_time=1.5)
        self.wait(2)
        
        # === SCHRITT 2: NACH X AUFLÖSEN ===
        schritt2_title = Text("2. Nach x auflösen:", font_size=32, color=GREEN).to_edge(UP, buff=0.5)
        
        # Erste Umformung
        step1 = MathTex(r"2x - 1 &= -x + 5", r"&\quad | +x", font_size=40)
        step1.move_to(UP * 1.5)
        
        step2 = MathTex(r"3x - 1 &= 5", r"&\quad | +1", font_size=40)
        step2.next_to(step1, DOWN, buff=0.5)
        
        step3 = MathTex(r"3x &= 6", r"&\quad | :3", font_size=40)
        step3.next_to(step2, DOWN, buff=0.5)
        
        step4 = MathTex(r"x &= 2", font_size=48, color=YELLOW)
        step4.next_to(step3, DOWN, buff=0.5)
        
        self.play(
            FadeOut(schritt1_title),
            FadeIn(schritt2_title),
            FadeOut(gleichung),
            run_time=1
        )
        
        self.play(Write(step1), run_time=1.2)
        self.wait(1)
        self.play(Write(step2), run_time=1.2)
        self.wait(1)
        self.play(Write(step3), run_time=1.2)
        self.wait(1)
        self.play(Write(step4), run_time=1.5)
        self.wait(2)
        
        # === SCHRITT 3: Y BERECHNEN ===
        schritt3_title = Text("3. y berechnen:", font_size=32, color=GREEN).to_edge(UP, buff=0.5)
        
        y_step1 = MathTex(r"y &= 2 \cdot 2 - 1", font_size=40)
        y_step1.move_to(UP * 1)
        
        y_step2 = MathTex(r"y &= 4 - 1", font_size=40)
        y_step2.next_to(y_step1, DOWN, buff=0.5)
        
        y_step3 = MathTex(r"y &= 3", font_size=48, color=YELLOW)
        y_step3.next_to(y_step2, DOWN, buff=0.5)
        
        self.play(
            FadeOut(schritt2_title),
            FadeIn(schritt3_title),
            *[FadeOut(obj) for obj in [step1, step2, step3, step4]],
            run_time=1
        )
        
        self.play(Write(y_step1), run_time=1)
        self.wait(0.8)
        self.play(Write(y_step2), run_time=1)
        self.wait(0.8)
        self.play(Write(y_step3), run_time=1.2)
        self.wait(2)
        
        # === ERGEBNIS ===
        ergebnis_title = Text("Ergebnis:", font_size=32, color=GREEN).to_edge(UP, buff=0.5)
        
        ergebnis = MathTex(r"S(2 \mid 3)", font_size=64, color=YELLOW)
        ergebnis.move_to(ORIGIN)
        
        self.play(
            FadeOut(schritt3_title),
            FadeIn(ergebnis_title),
            *[FadeOut(obj) for obj in [y_step1, y_step2, y_step3]],
            run_time=1
        )
        self.play(Write(ergebnis), run_time=1.5)
        self.wait(2)
        
        # === GRAPHISCHE DARSTELLUNG ===
        self.play(FadeOut(ergebnis_title), FadeOut(ergebnis), run_time=1)
        
        # Koordinatensystem erstellen
        axes = Axes(
            x_range=[-1, 5],
            y_range=[-2, 6],
            x_length=8,
            y_length=6,
            axis_config={"include_numbers": True},
        ).scale(0.7)
        
        axes_title = Text("Graphische Überprüfung:", font_size=32, color=GREEN).to_edge(UP, buff=0.3)
        
        self.play(Write(axes_title), Create(axes), run_time=1.5)
        
        # Geraden zeichnen
        g_graph = axes.plot(lambda x: 2*x - 1, x_range=[-0.5, 4], color=BLUE)
        g_label = MathTex(r"g: y = 2x - 1", color=BLUE, font_size=24).move_to(axes.c2p(3.5, 6))
        
        h_graph = axes.plot(lambda x: -x + 5, x_range=[0, 5], color=RED)
        h_label = MathTex(r"h: y = -x + 5", color=RED, font_size=24).move_to(axes.c2p(0.5, 4.5))
        
        self.play(Create(g_graph), Write(g_label), run_time=1.5)
        self.play(Create(h_graph), Write(h_label), run_time=1.5)
        self.wait(1)
        
        # Schnittpunkt markieren
        schnittpunkt_dot = Dot(axes.c2p(2, 3), color=YELLOW, radius=0.1)
        schnittpunkt_label = MathTex(r"S(2|3)", font_size=32, color=YELLOW).next_to(schnittpunkt_dot, UR, buff=0.2)
        
        self.play(FadeIn(schnittpunkt_dot, scale=2), Write(schnittpunkt_label), run_time=1.5)
        self.wait(3)
        
        # Ende
        self.play(*[FadeOut(mob) for mob in [axes_title, axes, g_graph, g_label, h_graph, h_label, schnittpunkt_dot, schnittpunkt_label]])

# Render-Befehl (stand versehentlich als Code am Dateiende und hätte den Import gebrochen):
# python -m manim -qm szenen/schnittpunkt_geraden.py SchnittpunktZweierGeraden
