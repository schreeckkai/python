from manim import *

class NullstellenBerechnung(Scene):
    def construct(self):
        # ===== SEITE 1: Erste Lösung x1 =====
        title1 = Text("1. Lösung berechnen", font_size=32, color=BLUE)
        title1.to_edge(UP, buff=0.3)
        
        eq1 = MathTex(r"2\sin\left(\frac{\pi}{2}(x-1)\right) + 1 = 0", font_size=28)
        eq2 = MathTex(r"\sin\left(\frac{\pi}{2}(x-1)\right) = -\frac{1}{2}", font_size=28)
        eq3 = MathTex(r"\frac{\pi}{2}(x_1-1) = \arcsin\left(-\frac{1}{2}\right) = -\frac{\pi}{6}", font_size=28)
        eq4 = MathTex(r"x_1 - 1 = -\frac{1}{3} \implies x_1 = \frac{2}{3}", font_size=28, color=YELLOW)
        
        seite1 = VGroup(eq1, eq2, eq3, eq4)
        seite1.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        
        # WICHTIG: Jetzt auch die Höhe begrenzen!
        seite1.scale_to_fit_width(11)
        seite1.scale_to_fit_height(5)  # Höhe auf 5 Einheiten begrenzen
        seite1.next_to(title1, DOWN, buff=0.5)
        
        self.play(Write(title1), run_time=1)
        self.wait(0.5)
        self.play(Write(eq1), run_time=1.5)
        self.wait(0.5)
        self.play(FadeIn(eq2, shift=DOWN*0.2), run_time=1)
        self.wait(0.5)
        self.play(FadeIn(eq3, shift=DOWN*0.2), run_time=1.5)
        self.wait(0.5)
        self.play(FadeIn(eq4, shift=DOWN*0.2), run_time=1)
        self.wait(2)
        
        # ===== SEITE 2: Zweite Lösung x2 + Ergebnis =====
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)
        
        title2 = Text("2. Lösung (Symmetrie) + Ergebnis", font_size=32, color=BLUE)
        title2.to_edge(UP, buff=0.3)
        
        eq5 = MathTex(r"\frac{\pi}{2}(x_2-1) = \pi - \left(-\frac{\pi}{6}\right) = \frac{7\pi}{6}", font_size=28, color=GREEN)
        eq6 = MathTex(r"x_2 - 1 = \frac{7}{3} \implies x_2 = \frac{10}{3}", font_size=28, color=GREEN)
        eq7 = MathTex(r"x = \frac{2}{3} + 4k \quad \text{und} \quad x = \frac{10}{3} + 4k, \quad k \in \mathbb{Z}", font_size=28, color=YELLOW)
        
        seite2 = VGroup(eq5, eq6, eq7)
        seite2.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        seite2.scale_to_fit_width(11)
        seite2.scale_to_fit_height(5)
        seite2.next_to(title2, DOWN, buff=0.5)
        
        self.play(Write(title2), run_time=1)
        self.wait(0.5)
        self.play(FadeIn(eq5, shift=DOWN*0.2), run_time=1.5)
        self.wait(0.5)
        self.play(FadeIn(eq6, shift=DOWN*0.2), run_time=1)
        self.wait(1)
        self.play(FadeIn(eq7, shift=DOWN*0.2), run_time=1.5)
        self.wait(3)
