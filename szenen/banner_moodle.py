from manim import *

class MoodleBannerPNG(Scene):
    def construct(self):
        # 1. Tiefschwarzer Hintergrund
        self.camera.background_color = "#0b0c10"

        # 2. Koordinatensystem im typischen Manim-Stil (etwas breiter fürs Banner-Format)
        plane = NumberPlane(
            x_range=[-8, 8, 1],
            y_range=[-3, 3, 1],
            background_line_style={
                "stroke_color": WHITE,
                "stroke_opacity": 0.05,
                "stroke_width": 1,
            }
        ).add_coordinates()

        # 3. Funktion in Manim-Blau (#58C4DD)
        func = plane.plot(lambda x: np.sin(x), color="#58C4DD", stroke_width=4)
        func_label = MathTex(f"f(x) = \\sin(x)", color="#58C4DD").scale(0.8).to_corner(UR)

        # 4. Zweite Kurve in Kupfer/Orange (#CD853F)
        derivative = plane.plot(lambda x: np.cos(x), color="#CD853F", stroke_width=3)
        der_label = MathTex(f"f'(x) = \\cos(x)", color="#CD853F").scale(0.8).next_to(func_label, DOWN)

        # Alles direkt ohne Animation aufbauen (perfekt für ein Standbild)
        self.add(plane, func, func_label, derivative, der_label)
