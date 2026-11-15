from manim import *
import re

# === HIER DEIN LATEX-CODE REIN ===
LATEX_CODE = r"""
\begin{align*}
2\sin\left(\frac{\pi}{2}(x-1)\right) + 1 &= 0 \\[1ex]
\sin\left(\frac{\pi}{2}(x-1)\right) &= -\frac{1}{2} \\[1ex]
\frac{\pi}{2}(x_1-1) &= \arcsin\left(-\frac{1}{2}\right) = -\frac{\pi}{6} \\[1ex]
x_1 - 1 &= -\frac{1}{3} \implies x_1 = \frac{2}{3} \\[2ex]
\frac{\pi}{2}(x_2-1) &= \pi - \left(-\frac{\pi}{6}\right) = \frac{7\pi}{6} \\[1ex]
x_2 - 1 &= \frac{7}{3} \implies x_2 = \frac{10}{3} \\[2ex]
x &= \frac{2}{3} + 4k \quad \text{und} \quad x = \frac{10}{3} + 4k, \quad k \in \mathbb{Z}
\end{align*}
"""


class LaTeXScene(Scene):
    def construct(self):
        # LaTeX-Code parsen
        parsed = self.parse_latex(LATEX_CODE)
        
        # Titel
        title = Text(parsed["title"], font_size=48, color=BLUE)
        self.play(Write(title), run_time=1.5)
        self.wait(1)
        self.play(FadeOut(title))
        
        # Schritte animieren
        for i, step in enumerate(parsed["steps"], 1):
            step_title = Text(f"{i}. {step['heading']}", font_size=32, color=GREEN).to_edge(UP, buff=0.5)
            self.play(FadeIn(step_title), run_time=0.8)
            
            prev_eq = None
            for j, eq in enumerate(step["equations"]):
                math_eq = MathTex(eq, font_size=40)
                
                if prev_eq:
                    math_eq.next_to(prev_eq, DOWN, buff=0.5)
                else:
                    math_eq.move_to(ORIGIN)
                
                if j == len(step["equations"]) - 1:
                    math_eq.set_color(YELLOW)
                
                self.play(Write(math_eq), run_time=1.2)
                self.wait(0.8)
                prev_eq = math_eq
            
            self.wait(1.5)
            
            if i < len(parsed["steps"]):
                self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.8)
        
        # Ergebnis
        if parsed["result"]:
            result_title = Text("Ergebnis:", font_size=32, color=GREEN).to_edge(UP, buff=0.5)
            result = MathTex(parsed["result"], font_size=64, color=YELLOW)
            result.move_to(ORIGIN)
            
            self.play(*[FadeOut(mob) for mob in self.mobjects], FadeIn(result_title), run_time=0.8)
            self.play(Write(result), run_time=1.5)
            self.wait(3)
    
    def parse_latex(self, latex):
        """Parst LaTeX-Code in strukturierte Daten."""
        result = {"title": "", "steps": [], "result": ""}
        
        # Titel extrahieren
        title_match = re.search(r'\\section\*\{([^}]+)\}', latex)
        if title_match:
            result["title"] = title_match.group(1)
        
        # Schritte extrahieren
        step_pattern = r'\\textbf\{([^}]+)\}(.*?)(?=\\textbf\{|$)'
        steps = re.findall(step_pattern, latex, re.DOTALL)
        
        for heading, content in steps:
            # Gleichungen aus align*-Umgebung extrahieren
            align_match = re.search(r'\\begin\{align\*\}(.*?)\\end\{align\*\}', content, re.DOTALL)
            if align_match:
                eq_text = align_match.group(1).strip()
                equations = [eq.strip() for eq in eq_text.split('\\\\') if eq.strip()]
                
                result["steps"].append({
                    "heading": heading,
                    "equations": equations
                })
        
        # Ergebnis extrahieren (letzte \textbf{...} nach "Ergebnis")
        result_match = re.search(r'Ergebnis.*?\\textbf\{\$([^$]+)\$\}', latex, re.DOTALL)
        if result_match:
            result["result"] = result_match.group(1)
        
        return result
