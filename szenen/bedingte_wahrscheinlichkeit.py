from manim import *
import numpy as np

class BedingteWahrscheinlichkeit(Scene):
    def construct(self):
        self.camera.background_color = "#1c1c1c"

        # Wasserzeichen
        watermark = Text("Mathe Schreck", font="Creepster", color="#644533", font_size=20)
        watermark.to_corner(DR, buff=0.5).set_opacity(0.6)
        self.add(watermark)

        # ========== 1. TITEL ==========
        title = Text("Bedingte Wahrscheinlichkeit", font_size=40)
        title_sub = Text("Pfadregeln am Baumdiagramm", font_size=26, color=YELLOW)
        title_group = VGroup(title, title_sub).arrange(DOWN, buff=0.3)
        title_group.to_edge(UP, buff=1.0)
        self.play(Write(title_group), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title_group), run_time=1.0)

        # ========== 2. AUFGABE ==========
        aufgabe = Text("Eine Urne enthält 3 rote und 2 blaue Kugeln.", font_size=26)
        aufgabe_sub = Text("Zwei Kugeln werden hintereinander ohne Zurücklegen gezogen.",
                           font_size=26, color=YELLOW)
        aufgabe_group = VGroup(aufgabe, aufgabe_sub).arrange(DOWN, buff=0.25)
        aufgabe_group.to_edge(UP, buff=1.0)
        self.play(Write(aufgabe_group), run_time=1.5)
        self.wait(2.0)
        self.play(FadeOut(aufgabe_group), run_time=0.5)

        # ========== 3. BAUMDIAGRAMM ==========
        ROT = RED
        BLAU = BLUE

        def knoten(position, farbe, name):
            dot = Dot(position, color=farbe, radius=0.09)
            label = Text(name, font_size=20, color=farbe)
            label.next_to(dot, DOWN, buff=0.15)
            return VGroup(dot, label)

        def ast(start, end, wkeit, farbe):
            pfeil = Arrow(start, end, color=farbe, buff=0.12, stroke_width=3)
            mitte = (np.array(start) + np.array(end)) / 2
            richtung = np.array(end) - np.array(start)
            senkrecht = np.array([-richtung[1], richtung[0], 0.0])
            senkrecht = senkrecht / np.linalg.norm(senkrecht) * 0.35
            label = MathTex(wkeit, font_size=30, color=farbe)
            label.move_to(mitte + senkrecht)
            return VGroup(pfeil, label)

        wurzel = Dot([-6.0, 0.6, 0], color=WHITE, radius=0.09)
        start_label = Text("Start", font_size=20)
        start_label.next_to(wurzel, LEFT, buff=0.15)

        p_rot1 = np.array([-3.4, 2.2, 0])
        p_blau1 = np.array([-3.4, -1.2, 0])
        p_rr = np.array([-0.8, 3.0, 0])
        p_rb = np.array([-0.8, 1.4, 0])
        p_br = np.array([-0.8, -0.4, 0])
        p_bb = np.array([-0.8, -2.0, 0])

        # --- 1. Stufe ---
        ast_rot1 = ast(wurzel.get_center(), p_rot1, r"\tfrac{3}{5}", ROT)
        ast_blau1 = ast(wurzel.get_center(), p_blau1, r"\tfrac{2}{5}", BLAU)
        k_rot1 = knoten(p_rot1, ROT, "rot")
        k_blau1 = knoten(p_blau1, BLAU, "blau")
        zug1 = Text("1. Zug", font_size=20, color=GREY_B).move_to([-4.7, 3.3, 0])

        self.play(FadeIn(wurzel), Write(start_label), run_time=0.8)
        self.play(Create(ast_rot1[0]), Write(ast_rot1[1]),
                  Create(ast_blau1[0]), Write(ast_blau1[1]), run_time=2.0)
        self.play(FadeIn(k_rot1), FadeIn(k_blau1), Write(zug1), run_time=0.8)
        self.wait(1.0)

        # --- 2. Stufe (ohne Zurücklegen!) ---
        ast_rr = ast(p_rot1, p_rr, r"\tfrac{2}{4}", ROT)
        ast_rb = ast(p_rot1, p_rb, r"\tfrac{2}{4}", BLAU)
        ast_br = ast(p_blau1, p_br, r"\tfrac{3}{4}", ROT)
        ast_bb = ast(p_blau1, p_bb, r"\tfrac{1}{4}", BLAU)
        k_rr = knoten(p_rr, ROT, "rot")
        k_rb = knoten(p_rb, BLAU, "blau")
        k_br = knoten(p_br, ROT, "rot")
        k_bb = knoten(p_bb, BLAU, "blau")
        zug2 = Text("2. Zug", font_size=20, color=GREY_B).move_to([-2.1, 3.3, 0])

        self.play(*[Create(a[0]) for a in [ast_rr, ast_rb, ast_br, ast_bb]], run_time=2.5)
        self.play(*[Write(a[1]) for a in [ast_rr, ast_rb, ast_br, ast_bb]], run_time=1.2)
        self.play(FadeIn(k_rr), FadeIn(k_rb), FadeIn(k_br), FadeIn(k_bb),
                  Write(zug2), run_time=0.8)
        self.wait(1.5)

        # --- Hinweis: Zusammensetzung ändert sich ---
        hinweis = Text("Nach dem 1. Zug fehlt eine Kugel: die Wahrscheinlichkeiten ändern sich!",
                       font_size=22, color=YELLOW)
        hinweis.to_edge(DOWN, buff=0.6)
        self.play(Write(hinweis), run_time=1.0)
        self.wait(2.0)
        self.play(FadeOut(hinweis), run_time=0.5)

        # ========== 4. 1. PFADREGEL (PRODUKTREGEL) ==========
        regel1_titel = Text("1. Pfadregel (Produktregel):", font_size=26, color=GREEN)
        regel1_text = Text("Wahrscheinlichkeiten entlang\neines Pfades multiplizieren.",
                           font_size=22, color=GREEN)
        regel1 = VGroup(regel1_titel, regel1_text).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        regel1.to_corner(UR, buff=0.5)

        self.play(Write(regel1_titel), run_time=0.8)
        self.play(Write(regel1_text), run_time=0.8)
        self.wait(0.5)

        # Pfad blau -> rot hervorheben
        box_blau1 = SurroundingRectangle(ast_blau1, color=YELLOW, buff=0.12)
        box_br = SurroundingRectangle(ast_br, color=YELLOW, buff=0.12)
        self.play(Create(box_blau1), Create(box_br), run_time=1.0)
        self.wait(0.5)

        prod = MathTex(r"P(\text{blau und rot})", r"= \frac{2}{5} \cdot \frac{3}{4} = \frac{3}{10}",
                       font_size=32)
        prod.move_to([3.6, 1.6, 0])
        self.play(Write(prod), run_time=1.5)
        self.wait(2.0)

        # ========== 5. BEDINGTE WAHRSCHEINLICHKEIT ==========
        frage = Text("Wie wahrscheinlich ist Kugel 2 rot,\nwenn Kugel 1 blau war?",
                     font_size=24, color=YELLOW)
        frage.move_to([3.6, 0.7, 0])
        self.play(Write(frage), run_time=1.0)
        self.wait(1.0)

        definition = MathTex(r"P(\text{rot}_2 \mid \text{blau}_1)",
                             r"= \frac{P(\text{blau}_1 \cap \text{rot}_2)}{P(\text{blau}_1)}",
                             font_size=30)
        definition.move_to([3.6, -0.4, 0])
        self.play(Write(definition), run_time=1.5)
        self.wait(1.0)

        rechnung_1 = MathTex(r"= \frac{\frac{2}{5} \cdot \frac{3}{4}}{\frac{2}{5}}",
                             font_size=32)
        rechnung_1.move_to([3.6, -1.3, 0])
        self.play(Write(rechnung_1), run_time=1.2)
        self.wait(1.0)

        rechnung_2 = MathTex(r"= \frac{\frac{3}{10}}{\frac{2}{5}} = \frac{3}{10} \cdot \frac{5}{2} = \frac{3}{4}",
                             font_size=32)
        rechnung_2.move_to([3.6, -2.2, 0])
        self.play(Write(rechnung_2), run_time=1.5)
        self.wait(1.0)

        am_ast = Text("Die 3/4 steht direkt am Baum!", font_size=22, color=ORANGE)
        am_ast.move_to([3.6, -3.0, 0])
        self.play(Write(am_ast), run_time=1.0)
        self.wait(2.0)

        # ========== 6. 2. PFADREGEL (SUMMENREGEL) ==========
        regel2_titel = Text("2. Pfadregel (Summenregel):", font_size=26, color=ORANGE)
        regel2_text = Text("Alle Pfade zum Ereignis addieren.", font_size=22, color=ORANGE)
        regel2 = VGroup(regel2_titel, regel2_text).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        regel2.to_corner(UR, buff=0.5)

        self.play(*[FadeOut(m) for m in [regel1, prod, frage, definition,
                                         rechnung_1, rechnung_2, am_ast]],
                  Write(regel2_titel), run_time=0.8)
        self.play(Write(regel2_text), run_time=0.8)

        # beide Pfade zu roten Endpunkten hervorheben
        box_rr = SurroundingRectangle(ast_rr, color=ORANGE, buff=0.12)
        self.play(Create(box_rr), run_time=0.8)

        summe_1 = MathTex(r"P(\text{rot}_2)", r"= \frac{3}{5} \cdot \frac{2}{4}",
                          r"+ \frac{2}{5} \cdot \frac{3}{4}", font_size=32)
        summe_1.move_to([3.6, 1.4, 0])
        self.play(Write(summe_1), run_time=1.5)

        summe_2 = MathTex(r"= \frac{3}{10} + \frac{3}{10} = \frac{3}{5}",
                          font_size=32, color=YELLOW)
        summe_2.move_to([3.6, 0.5, 0])
        self.play(Write(summe_2), run_time=1.5)
        self.wait(2.0)

        # ========== 7. ZUSAMMENFASSUNG ==========
        self.play(*[FadeOut(m) for m in self.mobjects if m != watermark], run_time=1.0)

        summary = VGroup(
            Text("Zusammenfassung", font_size=32, color=YELLOW),
            MathTex(r"P(B \mid A) = \frac{P(A \cap B)}{P(A)}", font_size=32),
            Text("1. Pfadregel: entlang eines Pfades multiplizieren", font_size=24),
            Text("2. Pfadregel: Pfade zum Ereignis addieren", font_size=24),
            Text("Bedingte Wahrscheinlichkeiten stehen direkt an den Ästen.", font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        summary.to_edge(LEFT, buff=1.0)
        self.play(Write(summary), run_time=2.5)
        self.wait(4.0)
