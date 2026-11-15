from manim import *
import numpy as np

class WiederholungGrundlagen(Scene):
    def construct(self):
        # 3b1b-Style: Schwarzer Hintergrund
        self.camera.background_color = "#1c1c1c"
        self.camera.pixel_width = 640
        self.camera.pixel_height = 480

        # ---------- ZENTRALES ELEMENT: Kreisförmige Pfeile ----------
        arc1 = Arc(radius=1.5, start_angle=PI * 0.2, angle=PI * 1.1, 
                   color="#FFFF00", stroke_width=5)
        arc2 = Arc(radius=1.5, start_angle=PI * 1.2, angle=PI * 1.1, 
                   color="#FFFF00", stroke_width=5)

        # Pfeilspitzen
        arrow1 = Triangle(fill_color="#FFFF00", fill_opacity=1, stroke_width=0)
        arrow1.scale(0.15)
        end_angle_1 = arc1.start_angle + arc1.angle
        arrow1.move_to(arc1.get_end())
        arrow1.rotate(end_angle_1 + PI/2)

        arrow2 = Triangle(fill_color="#FFFF00", fill_opacity=1, stroke_width=0)
        arrow2.scale(0.15)
        end_angle_2 = arc2.start_angle + arc2.angle
        arrow2.move_to(arc2.get_end())
        arrow2.rotate(end_angle_2 + PI/2)

        arrows_group = VGroup(arc1, arrow1, arc2, arrow2)
        arrows_group.move_to([0, 0, 0])

        # ---------- MITTELSTUFE SYMBOLE (im Kreis) ----------
        # Bruch
        fraction = MathTex(r"\frac{1}{2}", font_size=32, color=WHITE)
        fraction.move_to([0, 0.5, 0])

        # Wurzel
        sqrt = MathTex(r"\sqrt{9}", font_size=32, color=WHITE)
        sqrt.move_to([0, -0.5, 0])

        # ---------- UNTERSTUFE SYMBOLE (rundherum verteilt) ----------
        # Grundrechenarten
        plus = MathTex(r"+", font_size=48, color="#FFFF00")
        plus.move_to([-3.5, 2.0, 0])

        minus = MathTex(r"-", font_size=48, color="#FFFF00")
        minus.move_to([3.5, 2.0, 0])

        multiply = MathTex(r"\times", font_size=48, color="#FFFF00")
        multiply.move_to([-3.5, -2.0, 0])

        divide = MathTex(r"\div", font_size=48, color="#FFFF00")
        divide.move_to([3.5, -2.0, 0])

        # Geometrie-Symbole
        triangle = Triangle(color="#4A90E2", stroke_width=3)
        triangle.scale(0.4)
        triangle.move_to([-2.5, 2.5, 0])

        circle = Circle(color="#4A90E2", stroke_width=3)
        circle.scale(0.3)
        circle.move_to([2.5, 2.5, 0])

        square = Square(color="#4A90E2", stroke_width=3)
        square.scale(0.3)
        square.move_to([-2.5, -2.5, 0])

        # Einfache Gleichung
        equation = MathTex(r"a + b = c", font_size=28, color="#AAAAAA")
        equation.move_to([2.5, -2.5, 0])

        # Prozent
        percent = MathTex(r"\%", font_size=48, color="#FFFF00")
        percent.move_to([0, 3.0, 0])

        # Koordinatensymbol
        axes = Axes(
            x_range=[0, 1, 0.5],
            y_range=[0, 1, 0.5],
            x_length=0.8,
            y_length=0.8,
            axis_config={"color": "#4A90E2", "stroke_width": 2},
            tips=False,
        )
        axes.move_to([0, -3.0, 0])

        # Winkel
        angle_arc = Arc(radius=0.4, start_angle=0, angle=PI/3, 
                       color="#4A90E2", stroke_width=2)
        angle_line1 = Line([0, 0, 0], [0.6, 0, 0], color="#4A90E2", stroke_width=2)
        angle_line2 = Line([0, 0, 0], [0.3, 0.5, 0], color="#4A90E2", stroke_width=2)
        angle_group = VGroup(angle_line1, angle_line2, angle_arc)
        angle_group.move_to([-4.5, 0, 0])

        # Pi
        pi = MathTex(r"\pi", font_size=48, color="#FFFF00")
        pi.move_to([4.5, 0, 0])

        # ---------- ALLES HINZUFÜGEN ----------
        self.add(arrows_group, fraction, sqrt)
        self.add(plus, minus, multiply, divide)
        self.add(triangle, circle, square, equation)
        self.add(percent, axes, angle_group, pi)
