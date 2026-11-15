from manim import *
import numpy as np

class TrigonometrischeFunktionen(Scene):
    def construct(self):
        # 3b1b-Style: Schwarzer Hintergrund
        self.camera.background_color = "#1c1c1c"
        self.camera.pixel_width = 640
        self.camera.pixel_height = 480

        # ---------- ZENTRALER EINHEITSKREIS ----------
        axes_circle = Axes(
            x_range=[-1.5, 1.5, 0.5],
            y_range=[-1.5, 1.5, 0.5],
            x_length=2.8,
            y_length=2.8,
            axis_config={
                "color": "#585858",
                "stroke_width": 1.5,
                "include_ticks": False,
            },
            tips=True,
        )

        # Einheitskreis
        unit_circle = Circle(radius=1.4, color="#FFFF00", stroke_width=3)
        unit_circle.move_to(axes_center := [0, 0.3, 0])

        # Punkt auf dem Kreis (bei 60° = π/3)
        angle = PI / 3
        point = Dot(
            [1.4 * np.cos(angle), 0.3 + 1.4 * np.sin(angle), 0],
            color="#FFFF00",
            radius=0.08,
        )

        # Radius-Linie zum Punkt
        radius_line = Line(
            [0, 0.3, 0],
            [1.4 * np.cos(angle), 0.3 + 1.4 * np.sin(angle), 0],
            color="#FFFF00",
            stroke_width=2.5,
        )

        # Sinus-Linie (vertikal, rot)
        sin_line = Line(
            [1.4 * np.cos(angle), 0.3, 0],
            [1.4 * np.cos(angle), 0.3 + 1.4 * np.sin(angle), 0],
            color="#FF6B9D",
            stroke_width=2.5,
        )

        # Kosinus-Linie (horizontal, blau)
        cos_line = Line(
            [0, 0.3, 0],
            [1.4 * np.cos(angle), 0.3, 0],
            color="#58C4DD",
            stroke_width=2.5,
        )

        # Winkelbogen
        angle_arc = Arc(radius=0.35, start_angle=0, angle=angle, 
                       color="#FFFF00", stroke_width=2)
        angle_arc.move_arc_center_to([0, 0.3, 0])

        circle_group = VGroup(
            axes_circle, unit_circle, radius_line, 
            sin_line, cos_line, point, angle_arc
        )
        circle_group.move_to([0, 0.3, 0])

        # ---------- SINUSKURVE (oben links) ----------
        axes_sin = Axes(
            x_range=[0, 2 * PI, PI / 2],
            y_range=[-1.2, 1.2, 1],
            x_length=2.2,
            y_length=1.2,
            axis_config={"color": "#585858", "stroke_width": 1.5},
            tips=True,
        )
        sine = axes_sin.plot(np.sin, color="#FF6B9D", stroke_width=2.5)
        sin_group = VGroup(axes_sin, sine)
        sin_group.move_to([-4.5, 2.5, 0])

        # ---------- KOSINUSKURVE (oben rechts) ----------
        axes_cos = Axes(
            x_range=[0, 2 * PI, PI / 2],
            y_range=[-1.2, 1.2, 1],
            x_length=2.2,
            y_length=1.2,
            axis_config={"color": "#585858", "stroke_width": 1.5},
            tips=True,
        )
        cosine = axes_cos.plot(np.cos, color="#58C4DD", stroke_width=2.5)
        cos_group = VGroup(axes_cos, cosine)
        cos_group.move_to([4.5, 2.5, 0])

        # ---------- TANGENSKURVE (unten links) ----------
        axes_tan = Axes(
            x_range=[-PI / 2 + 0.3, PI / 2 - 0.3, PI / 4],
            y_range=[-2, 2, 1],
            x_length=2.2,
            y_length=1.2,
            axis_config={"color": "#585858", "stroke_width": 1.5},
            tips=True,
        )
        tangent = axes_tan.plot(np.tan, color="#C792EA", stroke_width=2.5,
                               discontinuities=[-PI / 2, PI / 2])
        tan_group = VGroup(axes_tan, tangent)
        tan_group.move_to([-4.5, -2.5, 0])

        # ---------- RECHTWINKLIGES DREIECK (unten rechts) ----------
        triangle = Polygon(
            [-0.8, -0.5, 0], [0.8, -0.5, 0], [-0.8, 0.5, 0],
            color="#95E1D3",
            stroke_width=2.5,
        )
        # rechter Winkel
        right_angle = Square(side_length=0.15, color="#95E1D3", stroke_width=1.5)
        right_angle.move_to([-0.72, -0.42, 0])

        # Winkelbogen
        angle_tri = Arc(radius=0.25, start_angle=0, 
                       angle=np.arctan(0.5 / 0.8),
                       color="#FFFF00", stroke_width=2)
        angle_tri.move_arc_center_to([0.8, -0.5, 0])

        # Seiten-Beschriftung als Symbole
        # Gegenkathete (a)
        side_a = MathTex(r"a", font_size=24, color="#FF6B9D")
        side_a.move_to([-1.0, 0.0, 0])

        # Ankathete (b)
        side_b = MathTex(r"b", font_size=24, color="#58C4DD")
        side_b.move_to([0.0, -0.7, 0])

        # Hypotenuse (c)
        side_c = MathTex(r"c", font_size=24, color="#FFFF00")
        side_c.move_to([0.15, 0.15, 0])

        triangle_group = VGroup(triangle, right_angle, angle_tri, side_a, side_b, side_c)
        triangle_group.move_to([4.5, -2.5, 0])

        # ---------- MATHE-SYMBOL (Bogenmaß π) ----------
        pi_symbol = MathTex(r"\pi", font_size=56, color="#FFFF00")
        pi_symbol.move_to([-2.5, -3.5, 0])

        # Winkel-Symbol θ
        theta = MathTex(r"\theta", font_size=40, color="#FFFF00")
        theta.move_to([2.5, -3.5, 0])

        # sin²+cos²=1 Identität
        identity = MathTex(r"\sin^2\theta + \cos^2\theta = 1", 
                          font_size=24, color="#AAAAAA")
        identity.move_to([0, -3.5, 0])

        # ---------- ALLES HINZUFÜGEN ----------
        self.add(circle_group)
        self.add(sin_group, cos_group, tan_group, triangle_group)
        self.add(pi_symbol, theta, identity)
