import re

def parse_latex_to_steps(latex_code):
    """
    Parst LaTeX-Code und extrahiert strukturierte Schritte für Manim.
    """
    steps = []
    
    # Überschriften finden (\textbf{...} oder \subsection*{...})
    heading_pattern = r'(?:\\textbf\{([^}]+)\}|\\subsection\*\{([^}]+)\})'
    headings = re.findall(heading_pattern, latex_code)
    headings = [h[0] or h[1] for h in headings]
    
    # Gleichungsblöcke finden (\begin{align*}...\end{align*})
    align_pattern = r'\\begin\{align\*\}(.*?)\\end\{align\*\}'
    equations_blocks = re.findall(align_pattern, latex_code, re.DOTALL)
    
    # Einzelne Gleichungen aus den Blöcken extrahieren
    for i, heading in enumerate(headings):
        if i < len(equations_blocks):
            eq_text = equations_blocks[i].strip()
            eq_lines = [line.strip() for line in eq_text.split('\\\\') if line.strip()]
            
            equations = []
            for eq in eq_lines:
                eq = eq.strip()
                equations.append(eq)
            
            steps.append({
                "heading": heading,
                "equations": equations,
                "result": i == len(headings) - 1
            })
    
    # Endergebnis finden
    result_pattern = r'(?:Schnittpunkt.*?ist|Ergebnis.*?:)\s*\\textbf\{([^}]+)\}'
    result_match = re.search(result_pattern, latex_code)
    final_result = result_match.group(1) if result_match else None
    
    return {
        "title": extract_title(latex_code),
        "steps": steps,
        "final_result": final_result
    }


def extract_title(latex_code):
    """
    Extrahiert den Titel aus dem LaTeX-Code.
    """
    title_pattern = r'\\section\*\{([^}]+)\}'
    match = re.search(title_pattern, latex_code)
    return match.group(1) if match else "Mathematische Lösung"
