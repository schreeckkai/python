from manim import *
import numpy as np

class AbleitungGestrecktVerschoben(Scene):
    def construct(self):
        # Wasserzeichen
        watermark = Text("Mathe Schreck", font="Creepster", color="#644533", font_size=20)
        watermark.to_corner(DR, buff=0.5).set_opacity(0.6)
        self.add(watermark)

        # ========== 1. TITEL ==========
        title = Text("Ableitung von gestreckten und verschobenen", font_size=32)
        title_sub = Text("Sinus- und Cosinus-Funktionen", font_size=32, color=YELLOW)
        title_group = VGroup(title, title_sub).arrange(DOWN, buff=0.2)
        self.play(Write(title_group))
        self.wait(1.5)
        self.play(FadeOut(title_group))

        # ========== 2. ACHSEN ==========
        axes = Axes(
            x_range=[-1, 5, 1],
            y_range=[-7, 7, 1], # Erweitert auf 7, damit die Ableitungen (Amplitude 6) reinpassen
            axis_config={"color": BLUE},
            x_length=6.0,  
            y_length=6.0,
        )
        # Dynamisch am rechten Rand verankern, etwas nach unten geschoben
        axes.to_edge(RIGHT, buff=0.5).shift(DOWN * 0.5)

        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        self.play(Create(axes), Write(axes_labels))
        self.wait(1)

        # ========== 3. SINUS-FALL ==========
        f_graph = axes.plot(lambda x: 3 * np.sin(2*x - PI/2) + 1, color=GREEN)
        
        f_label = MathTex("f(x) = 3\\sin\\left(2x - \\frac{\\pi}{2}\\right) + 1", color=GREEN, font_size=28)
        # Fest in der oberen rechten Ecke platzieren (UR = Upper Right)
        f_label.to_corner(UR, buff=0.5)
        
        # run_time=4 sorgt für ein langsames, flüssiges Zeichnen des Graphen
        self.play(Create(f_graph, run_time=4), Write(f_label))
        self.wait(1)

        # --- Schritt 1 ---
        step1_text = Text("Schritt 1: Äußere Ableitung", font_size=24, color=YELLOW)
        rule1 = MathTex("(c \\cdot g)' = c \\cdot g'", color=YELLOW, font_size=26)
        f_strich_part1 = MathTex("f'(x) = 3 \\cdot \\cos\\left(2x - \\frac{\\pi}{2}\\right)", color=RED, font_size=26)
        
        step1_group = VGroup(step1_text, rule1, f_strich_part1).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        step1_group.to_corner(UL, buff=1.0)

        self.play(Write(step1_text), Write(rule1))
        self.wait(0.5)
        self.play(Write(f_strich_part1))
        self.wait(2)
        self.play(FadeOut(step1_group))

        # --- Schritt 2 ---
        step2_text = Text("Schritt 2: Innere Ableitung", font_size=24, color=ORANGE)
        rule2 = MathTex("g(x) = 2x - \\frac{\\pi}{2} \\Rightarrow g'(x) = 2", color=ORANGE, font_size=26)
        f_strich_part2 = MathTex("f'(x) = 3 \\cdot \\cos\\left(2x - \\frac{\\pi}{2}\\right) \\cdot 2", color=RED, font_size=26)
        
        step2_group = VGroup(step2_text, rule2, f_strich_part2).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        step2_group.to_corner(UL, buff=1.0)

        self.play(Write(step2_text), Write(rule2))
        self.wait(0.5)
        self.play(Write(f_strich_part2))
        self.wait(2)
        self.play(FadeOut(step2_group))

        # --- Schritt 3 ---
        step3_text = Text("Schritt 3: Zusammenfassen", font_size=24, color=GREEN)
        f_strich_final = MathTex("f'(x) = 6 \\cos\\left(2x - \\frac{\\pi}{2}\\right)", color=RED, font_size=30)
        
        step3_group = VGroup(step3_text, f_strich_final).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        step3_group.to_corner(UL, buff=1.0)

        self.play(Write(step3_text), Write(f_strich_final))
        self.wait(1)

        # Ableitungsgraph zeichnen
        f_strich_graph = axes.plot(lambda x: 6 * np.cos(2*x - PI/2), color=RED)
        
        # Neue Label-Position: Direkt unter der Ausgangsfunktion, linksbündig ausgerichtet
        f_strich_label = MathTex("f'(x) = 6\\cos\\left(2x - \\frac{\\pi}{2}\\right)", color=RED, font_size=28)
        f_strich_label.next_to(f_label, DOWN, buff=0.2).align_to(f_label, LEFT)

        # Langsames Einblenden der Ableitung
        self.play(Create(f_strich_graph, run_time=4), Write(f_strich_label))
        self.wait(2)

        # Alles außer Wasserzeichen und Achsen ausblenden
        self.play(*[FadeOut(obj) for obj in [f_graph, f_label, f_strich_graph, f_strich_label, step3_group]])

        # ========== 4. COSINUS-FALL ==========
        g_graph = axes.plot(lambda x: 2 * np.cos(3*x + PI/4) - 2, color=PURPLE)
        
        g_label = MathTex("g(x) = 2\\cos\\left(3x + \\frac{\\pi}{4}\\right) - 2", color=PURPLE, font_size=28)
        # Wieder fest in der oberen rechten Ecke platzieren
        g_label.to_corner(UR, buff=0.5)
        
        self.play(Create(g_graph, run_time=4), Write(g_label))
        self.wait(1)

        cos_text = Text("Ableitung der Cosinus-Funktion", font_size=24, color=PURPLE)
        cos_step1 = MathTex("\\text{1. Äußere: } 2 \\cdot (-\\sin(\\dots))", color=YELLOW, font_size=26)
        cos_step2 = MathTex("\\text{2. Innere: } \\cdot 3", color=ORANGE, font_size=26)
        cos_final = MathTex("g'(x) = -6\\sin\\left(3x + \\frac{\\pi}{4}\\right)", color=RED, font_size=30)

        cos_group = VGroup(cos_text, cos_step1, cos_step2, cos_final).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        cos_group.to_corner(UL, buff=1.0)

        self.play(Write(cos_group[0]))
        self.play(Write(cos_group[1]))
        self.play(Write(cos_group[2]))
        self.wait(1)
        self.play(Write(cos_group[3]))

        # Ableitungsgraph zeichnen
        g_strich_graph = axes.plot(lambda x: -6 * np.sin(3*x + PI/4), color=RED)
        
        # Neue Label-Position: Direkt unter g(x)
        g_strich_label = MathTex("g'(x) = -6\\sin\\left(3x + \\frac{\\pi}{4}\\right)", color=RED, font_size=28)
        g_strich_label.next_to(g_label, DOWN, buff=0.2).align_to(g_label, LEFT)
        
        self.play(Create(g_strich_graph, run_time=4), Write(g_strich_label))
        self.wait(2)

        self.play(*[FadeOut(obj) for obj in self.mobjects if obj != watermark])

        # ========== 5. ZUSAMMENFASSUNG ==========
        summary = VGroup(
            Text("Zusammenfassung", font_size=32, color=YELLOW),
            MathTex("\\text{Faktorregel: } (c \\cdot f)' = c \\cdot f'", font_size=28),
            MathTex("\\text{Kettenregel: } (f(g(x)))' = f'(g(x)) \\cdot g'(x)", font_size=28),
            MathTex("(\\sin(x))' = \\cos(x)", font_size=28),
            MathTex("(\\cos(x))' = -\\sin(x)", font_size=28),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        
        summary.move_to(ORIGIN)
        self.play(Write(summary))
        self.wait(4)
