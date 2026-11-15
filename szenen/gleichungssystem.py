from manim import *

class GleichungssystemAnimation(Scene):
    def construct(self):
        # Farbschema
        FARBE_I = BLUE
        FARBE_II = GREEN
        FARBE_III = RED
        FARBE_ERGEBNIS = YELLOW
        FARBE_HIGHLIGHT = ORANGE
        
        # ===== TEIL 1: Titel =====
        titel = Text("Lineares Gleichungssystem (3×3)", font_size=48, color=WHITE)
        titel.to_edge(UP, buff=0.5)
        self.play(Write(titel), run_time=1.5)
        self.wait(1)
        
        # ===== TEIL 2: Gleichungen als Matrix =====
        matrix_titel = Text("Als erweiterte Koeffizientenmatrix:", font_size=32, color=WHITE)
        matrix_titel.move_to(UP * 2.5)
        
        # Matrix erstellen
        matrix = Matrix(
            [
                [1, 2, 3, 13],
                [2, -1, 1, 6],
                [3, 1, -2, 1]
            ],
            element_to_mobject_config={"font_size": 36},
            left_bracket="(",
            right_bracket=")"
        )
        matrix.scale(0.9)
        matrix.move_to(ORIGIN)
        
        # Labels für die Matrix
        var_label = MathTex(r"x", r"y", r"z", r"= 13", font_size=32, color=WHITE)
        var_label.next_to(matrix, UP, buff=0.3)
        
        row_labels = VGroup(
            Text("I:", color=FARBE_I, font_size=28),
            Text("II:", color=FARBE_II, font_size=28),
            Text("III:", color=FARBE_III, font_size=28)
        )
        row_labels.arrange(DOWN, aligned_edge=LEFT, buff=0.8)
        row_labels.next_to(matrix, LEFT, buff=0.5)
        
        self.play(Write(matrix_titel), run_time=1)
        self.wait(0.5)
        
        self.play(
            Write(matrix),
            Write(row_labels),
            run_time=2
        )
        self.wait(1)
        
        # ===== TEIL 3: Gleichungen einzeln zeigen =====
        gleichung_titel = Text("Als Gleichungssystem:", font_size=32, color=WHITE)
        gleichung_titel.move_to(UP * 3)
        
        # Gleichungen mit mehr Abstand
        gleichung_I = MathTex(
            r"x + 2y + 3z = 13",
            color=FARBE_I,
            font_size=48
        ).move_to(UP * 1.8)
        
        gleichung_II = MathTex(
            r"2x - y + z = 6",
            color=FARBE_II,
            font_size=48
        ).move_to(UP * 0.3)
        
        gleichung_III = MathTex(
            r"3x + y - 2z = 1",
            color=FARBE_III,
            font_size=48
        ).move_to(DOWN * 1.2)
        
        # Labels
        label_I = Text("I:", color=FARBE_I, font_size=36)
        label_II = Text("II:", color=FARBE_II, font_size=36)
        label_III = Text("III:", color=FARBE_III, font_size=36)
        
        label_I.next_to(gleichung_I, LEFT, buff=0.8)
        label_II.next_to(gleichung_II, LEFT, buff=0.8)
        label_III.next_to(gleichung_III, LEFT, buff=0.8)
        
        # Matrix ausblenden, Gleichungen einblenden
        self.play(
            FadeOut(matrix),
            FadeOut(row_labels),
            FadeOut(matrix_titel),
            run_time=1
        )
        self.wait(0.5)
        
        self.play(Write(gleichung_titel), run_time=1)
        self.wait(0.5)
        
        self.play(
            Write(label_I),
            Write(gleichung_I),
            run_time=1.5
        )
        self.wait(0.5)
        
        self.play(
            Write(label_II),
            Write(gleichung_II),
            run_time=1.5
        )
        self.wait(0.5)
        
        self.play(
            Write(label_III),
            Write(gleichung_III),
            run_time=1.5
        )
        self.wait(1)
        
        # ===== TEIL 4: Erklärung des Verfahrens =====
        erklaerung = Text(
            "Gauß-Algorithmus:\nElimination der Variablen",
            font_size=36,
            color=WHITE
        ).to_edge(DOWN, buff=0.8)
        
        self.play(FadeIn(erklaerung, shift=UP*0.3), run_time=1)
        self.wait(2)
        self.play(FadeOut(erklaerung), run_time=0.5)
        
        # ===== TEIL 5: Schritt 1 - x aus II eliminieren =====
        schritt1_titel = Text(
            "Schritt 1: x aus Gleichung II eliminieren",
            font_size=32,
            color=FARBE_HIGHLIGHT
        ).to_edge(DOWN, buff=0.8)
        
        self.play(Write(schritt1_titel), run_time=1)
        self.wait(1)
        
        # Rechenschritt anzeigen
        rechnung_II = MathTex(
            r"\text{II} - 2 \cdot \text{I}",
            color=FARBE_HIGHLIGHT,
            font_size=40
        ).move_to(DOWN * 2.5)
        
        self.play(Write(rechnung_II), run_time=1)
        self.wait(0.5)
        
        # Detaillierte Rechnung
        detail_rechnung_II = MathTex(
            r"(2x - y + z) - 2(x + 2y + 3z) = 6 - 2 \cdot 13",
            color=WHITE,
            font_size=32
        ).move_to(DOWN * 3.2)
        
        self.play(Write(detail_rechnung_II), run_time=1.5)
        self.wait(1)
        
        detail_rechnung_II_2 = MathTex(
            r"2x - y + z - 2x - 4y - 6z = 6 - 26",
            color=WHITE,
            font_size=32
        ).move_to(DOWN * 3.2)
        
        self.play(Transform(detail_rechnung_II, detail_rechnung_II_2), run_time=1.5)
        self.wait(1)
        
        detail_rechnung_II_3 = MathTex(
            r"-5y - 5z = -20",
            color=FARBE_II,
            font_size=36
        ).move_to(DOWN * 3.2)
        
        self.play(Transform(detail_rechnung_II, detail_rechnung_II_3), run_time=1.5)
        self.wait(1)
        
        # Neue Gleichung II' erstellen
        gleichung_II_neu = MathTex(
            r"-5y - 5z = -20",
            color=FARBE_II,
            font_size=48
        )
        
        label_II_neu = Text("II':", color=FARBE_II, font_size=36)
        
        self.play(
            Transform(gleichung_II, gleichung_II_neu),
            Transform(label_II, label_II_neu),
            run_time=1.5
        )
        self.wait(1)
        
        # Hilfsrechnungen entfernen
        self.play(
            FadeOut(rechnung_II),
            FadeOut(detail_rechnung_II),
            FadeOut(schritt1_titel),
            run_time=0.8
        )
        self.wait(1)
        
        # ===== TEIL 6: Schritt 2 - x aus III eliminieren =====
        schritt2_titel = Text(
            "Schritt 2: x aus Gleichung III eliminieren",
            font_size=32,
            color=FARBE_HIGHLIGHT
        ).to_edge(DOWN, buff=0.8)
        
        self.play(Write(schritt2_titel), run_time=1)
        self.wait(1)
        
        rechnung_III = MathTex(
            r"\text{III} - 3 \cdot \text{I}",
            color=FARBE_HIGHLIGHT,
            font_size=40
        ).move_to(DOWN * 2.5)
        
        self.play(Write(rechnung_III), run_time=1)
        self.wait(0.5)
        
        detail_rechnung_III = MathTex(
            r"(3x + y - 2z) - 3(x + 2y + 3z) = 1 - 3 \cdot 13",
            color=WHITE,
            font_size=32
        ).move_to(DOWN * 3.2)
        
        self.play(Write(detail_rechnung_III), run_time=1.5)
        self.wait(1)
        
        detail_rechnung_III_2 = MathTex(
            r"3x + y - 2z - 3x - 6y - 9z = 1 - 39",
            color=WHITE,
            font_size=32
        ).move_to(DOWN * 3.2)
        
        self.play(Transform(detail_rechnung_III, detail_rechnung_III_2), run_time=1.5)
        self.wait(1)
        
        detail_rechnung_III_3 = MathTex(
            r"-5y - 11z = -38",
            color=FARBE_III,
            font_size=36
        ).move_to(DOWN * 3.2)
        
        self.play(Transform(detail_rechnung_III, detail_rechnung_III_3), run_time=1.5)
        self.wait(1)
        
        gleichung_III_neu = MathTex(
            r"-5y - 11z = -38",
            color=FARBE_III,
            font_size=48
        )
        
        label_III_neu = Text("III':", color=FARBE_III, font_size=36)
        
        self.play(
            Transform(gleichung_III, gleichung_III_neu),
            Transform(label_III, label_III_neu),
            run_time=1.5
        )
        self.wait(1)
        
        self.play(
            FadeOut(rechnung_III),
            FadeOut(detail_rechnung_III),
            FadeOut(schritt2_titel),
            run_time=0.8
        )
        self.wait(1)
        
        # ===== TEIL 7: Schritt 3 - y aus III' eliminieren =====
        schritt3_titel = Text(
            "Schritt 3: y aus Gleichung III' eliminieren",
            font_size=32,
            color=FARBE_HIGHLIGHT
        ).to_edge(DOWN, buff=0.8)
        
        self.play(Write(schritt3_titel), run_time=1)
        self.wait(1)
        
        rechnung_y = MathTex(
            r"\text{III}' - \text{II}'",
            color=FARBE_HIGHLIGHT,
            font_size=40
        ).move_to(DOWN * 2.5)
        
        self.play(Write(rechnung_y), run_time=1)
        self.wait(0.5)
        
        detail_rechnung_y = MathTex(
            r"(-5y - 11z) - (-5y - 5z) = -38 - (-20)",
            color=WHITE,
            font_size=32
        ).move_to(DOWN * 3.2)
        
        self.play(Write(detail_rechnung_y), run_time=1.5)
        self.wait(1)
        
        detail_rechnung_y_2 = MathTex(
            r"-5y - 11z + 5y + 5z = -38 + 20",
            color=WHITE,
            font_size=32
        ).move_to(DOWN * 3.2)
        
        self.play(Transform(detail_rechnung_y, detail_rechnung_y_2), run_time=1.5)
        self.wait(1)
        
        detail_rechnung_y_3 = MathTex(
            r"-6z = -18",
            color=FARBE_III,
            font_size=36
        ).move_to(DOWN * 3.2)
        
        self.play(Transform(detail_rechnung_y, detail_rechnung_y_3), run_time=1.5)
        self.wait(1)
        
        gleichung_III_final = MathTex(
            r"-6z = -18",
            color=FARBE_III,
            font_size=48
        )
        
        label_III_final = Text("III'':", color=FARBE_III, font_size=36)
        
        self.play(
            Transform(gleichung_III, gleichung_III_final),
            Transform(label_III, label_III_final),
            run_time=1.5
        )
        self.wait(1)
        
        self.play(
            FadeOut(rechnung_y),
            FadeOut(detail_rechnung_y),
            FadeOut(schritt3_titel),
            run_time=0.8
        )
        self.wait(1)
        
        # ===== TEIL 8: Stufenform erreicht =====
        stufenform_text = Text(
            "Stufenform erreicht!",
            font_size=36,
            color=FARBE_ERGEBNIS
        ).to_edge(DOWN, buff=0.8)
        
        self.play(Write(stufenform_text), run_time=1)
        self.wait(2)
        
        self.play(FadeOut(stufenform_text), run_time=0.8)
        self.wait(1)
        
        # ===== TEIL 9: Rückwärtseinsetzen - z berechnen =====
        rueckwaerts_titel = Text(
            "Rückwärtseinsetzen: z berechnen",
            font_size=32,
            color=FARBE_HIGHLIGHT
        ).to_edge(DOWN, buff=0.8)
        
        self.play(Write(rueckwaerts_titel), run_time=1)
        self.wait(1)
        
        # III'' hervorheben
        self.play(
            gleichung_III.animate.set_color(FARBE_ERGEBNIS).scale(1.2),
            label_III.animate.set_color(FARBE_ERGEBNIS).scale(1.2),
            run_time=1
        )
        self.wait(0.5)
        
        z_rechnung = MathTex(
            r"-6z = -18 \quad \mid : (-6)",
            color=WHITE,
            font_size=36
        ).move_to(DOWN * 3.2)
        
        self.play(Write(z_rechnung), run_time=1.5)
        self.wait(1)
        
        z_ergebnis = MathTex(
            r"z = 3",
            color=FARBE_ERGEBNIS,
            font_size=48
        ).move_to(DOWN * 3.2)
        
        self.play(Transform(z_rechnung, z_ergebnis), run_time=1.5)
        self.wait(1)
        
        self.play(
            FadeOut(z_rechnung),
            FadeOut(rueckwaerts_titel),
            gleichung_III.animate.set_color(FARBE_III).scale(1/1.2),
            label_III.animate.set_color(FARBE_III).scale(1/1.2),
            run_time=0.8
        )
        self.wait(1)
        
        # ===== TEIL 10: y berechnen =====
        y_titel = Text(
            "y berechnen aus Gleichung II'",
            font_size=32,
            color=FARBE_HIGHLIGHT
        ).to_edge(DOWN, buff=0.8)
        
        self.play(Write(y_titel), run_time=1)
        self.wait(1)
        
        self.play(
            gleichung_II.animate.set_color(FARBE_ERGEBNIS).scale(1.2),
            label_II.animate.set_color(FARBE_ERGEBNIS).scale(1.2),
            run_time=1
        )
        self.wait(0.5)
        
        y_rechnung_1 = MathTex(
            r"-5y - 5(3) = -20",
            color=WHITE,
            font_size=36
        ).move_to(DOWN * 3.2)
        
        self.play(Write(y_rechnung_1), run_time=1.5)
        self.wait(1)
        
        y_rechnung_2 = MathTex(
            r"-5y - 15 = -20 \quad \mid + 15",
            color=WHITE,
            font_size=36
        ).move_to(DOWN * 3.2)
        
        self.play(Transform(y_rechnung_1, y_rechnung_2), run_time=1.5)
        self.wait(1)
        
        y_rechnung_3 = MathTex(
            r"-5y = -5 \quad \mid : (-5)",
            color=WHITE,
            font_size=36
        ).move_to(DOWN * 3.2)
        
        self.play(Transform(y_rechnung_1, y_rechnung_3), run_time=1.5)
        self.wait(1)
        
        y_ergebnis = MathTex(
            r"y = 1",
            color=FARBE_ERGEBNIS,
            font_size=48
        ).move_to(DOWN * 3.2)
        
        self.play(Transform(y_rechnung_1, y_ergebnis), run_time=1.5)
        self.wait(1)
        
        self.play(
            FadeOut(y_rechnung_1),
            FadeOut(y_titel),
            gleichung_II.animate.set_color(FARBE_II).scale(1/1.2),
            label_II.animate.set_color(FARBE_II).scale(1/1.2),
            run_time=0.8
        )
        self.wait(1)
        
        # ===== TEIL 11: x berechnen =====
        x_titel = Text(
            "x berechnen aus Gleichung I",
            font_size=32,
            color=FARBE_HIGHLIGHT
        ).to_edge(DOWN, buff=0.8)
        
        self.play(Write(x_titel), run_time=1)
        self.wait(1)
        
        self.play(
            gleichung_I.animate.set_color(FARBE_ERGEBNIS).scale(1.2),
            label_I.animate.set_color(FARBE_ERGEBNIS).scale(1.2),
            run_time=1
        )
        self.wait(0.5)
        
        x_rechnung_1 = MathTex(
            r"x + 2(1) + 3(3) = 13",
            color=WHITE,
            font_size=36
        ).move_to(DOWN * 3.2)
        
        self.play(Write(x_rechnung_1), run_time=1.5)
        self.wait(1)
        
        x_rechnung_2 = MathTex(
            r"x + 2 + 9 = 13",
            color=WHITE,
            font_size=36
        ).move_to(DOWN * 3.2)
        
        self.play(Transform(x_rechnung_1, x_rechnung_2), run_time=1.5)
        self.wait(1)
        
        x_rechnung_3 = MathTex(
            r"x + 11 = 13 \quad \mid - 11",
            color=WHITE,
            font_size=36
        ).move_to(DOWN * 3.2)
        
        self.play(Transform(x_rechnung_1, x_rechnung_3), run_time=1.5)
        self.wait(1)
        
        x_ergebnis = MathTex(
            r"x = 2",
            color=FARBE_ERGEBNIS,
            font_size=48
        ).move_to(DOWN * 3.2)
        
        self.play(Transform(x_rechnung_1, x_ergebnis), run_time=1.5)
        self.wait(1)
        
        self.play(
            FadeOut(x_rechnung_1),
            FadeOut(x_titel),
            gleichung_I.animate.set_color(FARBE_I).scale(1/1.2),
            label_I.animate.set_color(FARBE_I).scale(1/1.2),
            run_time=0.8
        )
        self.wait(1)
        
        # ===== TEIL 12: Endergebnis =====
        self.play(
            FadeOut(gleichung_I),
            FadeOut(gleichung_II),
            FadeOut(gleichung_III),
            FadeOut(label_I),
            FadeOut(label_II),
            FadeOut(label_III),
            FadeOut(titel),
            FadeOut(gleichung_titel),
            run_time=1
        )
        self.wait(0.5)
        
        ergebnis_titel = Text(
            "Lösung des Gleichungssystems",
            font_size=40,
            color=WHITE
        ).to_edge(UP, buff=1)
        
        loesungsmenge = MathTex(
            r"\mathbb{L} = \{(2 \mid 1 \mid 3)\}",
            color=FARBE_ERGEBNIS,
            font_size=60
        )
        
        variablen = MathTex(
            r"x = 2, \quad y = 1, \quad z = 3",
            color=WHITE,
            font_size=48
        ).next_to(loesungsmenge, DOWN, buff=1)
        
        self.play(Write(ergebnis_titel), run_time=1)
        self.wait(0.5)
        
        self.play(Write(loesungsmenge), run_time=2)
        self.wait(1)
        
        self.play(Write(variablen), run_time=1.5)
        self.wait(1)
        
        # Box um das Ergebnis
        box = SurroundingRectangle(loesungsmenge, color=FARBE_ERGEBNIS, buff=0.3)
        self.play(Create(box), run_time=1)
        self.wait(2)
        
        # ===== TEIL 13: Probe =====
        self.play(
            FadeOut(loesungsmenge),
            FadeOut(variablen),
            FadeOut(box),
            FadeOut(ergebnis_titel),
            run_time=1
        )
        self.wait(0.5)
        
        probe_titel = Text(
            "Probe: Einsetzen in Gleichung III",
            font_size=32,
            color=FARBE_HIGHLIGHT
        ).to_edge(UP, buff=1)
        
        self.play(Write(probe_titel), run_time=1)
        self.wait(0.5)
        
        probe_rechnung = MathTex(
            r"3(2) + 1 - 2(3) = 6 + 1 - 6 = 1 \quad \checkmark",
            color=GREEN,
            font_size=48
        )
        
        self.play(Write(probe_rechnung), run_time=2)
        self.wait(2)
        
        # Ende
        self.play(
            *[FadeOut(mob) for mob in [probe_titel, probe_rechnung]],
            run_time=1
        )
        self.wait(1)
