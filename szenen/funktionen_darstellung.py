from manim import *
import numpy as np

class FunktionenDarstellung(Scene):
    def construct(self):
        # 3b1b-Style: Schwarzer Hintergrund
        self.camera.background_color = "#1c1c1c"
        self.camera.pixel_width = 640
        self.camera.pixel_height = 480

        # ---------- ZENTRALES KOORDINATENSYSTEM ----------
        axes_main = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 4, 1],
            x_length=4,
            y_length=3,
            axis_config={
                "color": "#585858",
                "stroke_width": 2,
                "include_ticks": True,
            },
            tips=True,
        )

        # Parabel (quadratische Funktion) - zentral
        parabola = axes_main.plot(lambda x: x**2, color="#FFFF00", stroke_width=3)
        
        # Punkt auf der Parabel
        point = Dot(axes_main.c2p(1, 1), color="#FFFF00", radius=0.08)
        
        # Tangente am Punkt (zeigt Ableitung)
        tangent = Line(
            axes_main.c2p(0.3, 0.09),
            axes_main.c2p(1.7, 2.89),
            color="#58C4DD",
            stroke_width=2,
            stroke_opacity=0.8,
        )

        axes_group = VGroup(axes_main, parabola, point, tangent)
        axes_group.move_to([0, 0.3, 0])

        # ---------- LINEARE FUNCTION (oben links) ----------
        axes_linear = Axes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            x_length=1.8,
            y_length=1.5,
            axis_config={"color": "#585858", "stroke_width": 1.5},
            tips=True,
        )
        linear = axes_linear.plot(lambda x: 0.8*x, color="#58C4DD", stroke_width=2.5)
        linear_group = VGroup(axes_linear, linear)
        linear_group.move_to([-4.5, 2.5, 0])

        # ---------- SINUSFUNCTION (oben rechts) ----------
        axes_sin = Axes(
            x_range=[-2, 2, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=1.8,
            y_length=1.5,
            axis_config={"color": "#585858", "stroke_width": 1.5},
            tips=True,
        )
        sine = axes_sin.plot(lambda x: np.sin(x * PI), color="#FF6B9D", stroke_width=2.5)
        sin_group = VGroup(axes_sin, sine)
        sin_group.move_to([4.5, 2.5, 0])

        # ---------- KUBISCHE FUNCTION (unten links) ----------
        axes_cubic = Axes(
            x_range=[-1.5, 1.5, 1],
            y_range=[-2, 2, 1],
            x_length=1.8,
            y_length=1.5,
            axis_config={"color": "#585858", "stroke_width": 1.5},
            tips=True,
        )
        cubic = axes_cubic.plot(lambda x: x**3, color="#C792EA", stroke_width=2.5)
        cubic_group = VGroup(axes_cubic, cubic)
        cubic_group.move_to([-4.5, -2.5, 0])

        # ---------- EXPONENTIALFUNCTION (unten rechts) ----------
        axes_exp = Axes(
            x_range=[-2, 2, 1],
            y_range=[-0.5, 3, 1],
            x_length=1.8,
            y_length=1.5,
            axis_config={"color": "#585858", "stroke_width": 1.5},
            tips=True,
        )
        exp = axes_exp.plot(lambda x: np.exp(x) if x < 1.5 else np.exp(1.5), 
                           color="#95E1D3", stroke_width=2.5)
        exp_group = VGroup(axes_exp, exp)
        exp_group.move_to([4.5, -2.5, 0])

        # ---------- FUNKTIONSSCHREIBWEISE ----------
        # f(x) Symbol
        fx = MathTex(r"f(x)", font_size=36, color="#FFFF00")
        fx.move_to([-2.5, 3.5, 0])

        # Ableitung f'(x)
        fprime = MathTex(r"f'(x)", font_size=32, color="#58C4DD")
        fprime.move_to([2.5, 3.5, 0])

        # Integral
        integral = MathTex(r"\int f(x)\,dx", font_size=32, color="#C792EA")
        integral.move_to([-2.5, -3.5, 0])

        # Steigung m
        slope = MathTex(r"m = \frac{\Delta y}{\Delta x}", font_size=28, color="#FF6B9D")
        slope.move_to([2.5, -3.5, 0])

        # ---------- ALLES HINZUFÜGEN ----------
        self.add(axes_group)
        self.add(linear_group, sin_group, cubic_group, exp_group)
        self.add(fx, fprime, integral, slope)
