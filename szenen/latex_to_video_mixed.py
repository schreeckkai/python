from manim import *
import re

# === HIER DEIN LATEX-CODE REIN ===
LATEX_CODE = r"""
\section*{Definition: Lineare Funktion}

\textbf{Allgemeine Form}
Eine lineare Funktion hat die Form:
\begin{align*}
    f(x) = m \cdot x + b
\end{align*}

\textbf{Bedeutung der Parameter}
\begin{textblock}
m = Steigung der Geraden \\
b = y-Achsenabschnitt
\end{textblock}

\textbf{Beispiel}
\begin{align*}
    f(x) &= 2x + 3 \\
    m &= 2, \quad b = 3
\end{align*}

\textbf{Merke}
\begin{textblock}
Wenn m > 0, steigt die Gerade. \\
Wenn m < 0, fällt die Gerade.
\end{textblock}
"""


class LaTeXScene(Scene):
    def construct(self):
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
            
            prev_item = None
            for item in step["content"]:
                if item["type"] == "math":
                    math_eq = MathTex(item["text"], font_size=40)
                else:
                    math_eq = Text(item["text"], font_size=28)
                
                if prev_item:
                    math_eq.next_to(prev_item, DOWN, buff=0.5)
                else:
                    math_eq.move_to(ORIGIN)
                
                self.play(Write(math_eq), run_time=1.2)
                self.wait(0.8)
                prev_item = math_eq
            
            self.wait(1.5)
            
            if i < len(parsed["steps"]):
                self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.8)
    
    def parse_latex(self, latex):
        """Parst LaTeX-Code in strukturierte Daten."""
        result = {"title": "", "steps": []}
        
        # Titel extrahieren
        title_match = re.search(r'\\section\*\{([^}]+)\}', latex)
        if title_match:
            result["title"] = title_match.group(1)
        
        # Schritte extrahieren
        step_pattern = r'\\textbf\{([^}]+)\}(.*?)(?=\\textbf\{|$)'
        steps = re.findall(step_pattern, latex, re.DOTALL)
        
        for heading, content in steps:
            content_items = []
            
            # Mathematik-Blöcke (align*)
            align_matches = re.finditer(r'\\begin\{align\*\}(.*?)\\end\{align\*\}', content, re.DOTALL)
            align_positions = [(m.start(), m.end(), m.group(1)) for m in align_matches]
            
            # Text-Blöcke (textblock)
            text_matches = re.finditer(r'\\begin\{textblock\}(.*?)\\end\{textblock\}', content, re.DOTALL)
            text_positions = [(m.start(), m.end(), m.group(1)) for m in text_matches]
            
            # Alles kombinieren und sortieren
            all_blocks = []
            for start, end, text in align_positions:
                all_blocks.append((start, "math", text.strip()))
            for start, end, text in text_positions:
                all_blocks.append((start, "text", text.strip()))
            
            all_blocks.sort(key=lambda x: x[0])
            
            for _, block_type, block_text in all_blocks:
                if block_type == "math":
                    # Gleichungen aufteilen
                    equations = [eq.strip() for eq in block_text.split('\\\\') if eq.strip()]
                    for eq in equations:
                        content_items.append({"type": "math", "text": eq})
                else:
                    # Textzeilen aufteilen
                    lines = [line.strip() for line in block_text.split('\\\\') if line.strip()]
                    for line in lines:
                        content_items.append({"type": "text", "text": line})
            
            result["steps"].append({
                "heading": heading,
                "content": content_items
            })
        
        return result
