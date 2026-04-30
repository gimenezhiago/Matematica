from manim import *

class DeducaoHeron(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Cores
        TITULO_COR   = "#6B0033"
        TEXTO_COR    = "#1a1a1a"
        DEST_COR     = "#B03A2E"
        LABEL_COR    = "#1A5276"
        VERDE        = "#145A32"

        # Função para simular fórmulas sem LaTeX
        def format_text(s):
            return (s.replace("\\", "")
                     .replace("sqrt", "√")
                     .replace("cdot", "·")
                     .replace("dfrac", "")
                     .replace("{", "(")
                     .replace("}", ")")
                     .replace("Rightarrow", "⇒")
                     .replace("text", "")
                    )

        def tex(s, cor=TEXTO_COR, sz=32):
            return Text(format_text(s), color=cor, font_size=sz)

        def stex(s, cor=TEXTO_COR, sz=28):
            return Text(format_text(s), color=cor, font_size=sz)

        # ─────────────────────────────
        # CENA 0 – Título
        # ─────────────────────────────
        titulo = Text("Fórmula de Heron", font_size=52, color=TITULO_COR, weight=BOLD)
        sub = Text("Dedução completa – Matemática 4", font_size=28, color=TEXTO_COR)

        VGroup(titulo, sub).arrange(DOWN).move_to(ORIGIN)

        self.play(Write(titulo))
        self.play(FadeIn(sub))
        self.wait(1)
        self.play(FadeOut(titulo), FadeOut(sub))

        # ─────────────────────────────
        # CENA 1 – Triângulo
        # ─────────────────────────────
        sec1 = Text("1. Configuração do triângulo", font_size=36, color=TITULO_COR)
        sec1.to_edge(UP)
        self.play(Write(sec1))

        B = np.array([-3, -1.5, 0])
        C = np.array([3, -1.5, 0])
        A = np.array([0, 2, 0])
        H = np.array([0, -1.5, 0])

        tri = Polygon(A, B, C, color=TITULO_COR)
        tri.set_fill("#FAD7A0", opacity=0.3)

        alt = DashedLine(A, H, color=DEST_COR)
        alt_lbl = tex("h", DEST_COR, 26).next_to(alt, RIGHT)

        self.play(Create(tri))
        self.play(Create(alt), Write(alt_lbl))
        self.wait(1)

        # ─────────────────────────────
        # CENA 2 – Pitágoras
        # ─────────────────────────────
        self.play(FadeOut(sec1))

        sec2 = Text("2. Pitágoras", font_size=34, color=TITULO_COR)
        sec2.to_edge(UP)
        self.play(Write(sec2))

        eq1 = tex("c^2 = h^2 + x^2", sz=30)
        eq2 = tex("b^2 = h^2 + (a-x)^2", sz=30)

        VGroup(eq1, eq2).arrange(DOWN).to_edge(RIGHT)

        self.play(Write(eq1))
        self.play(Write(eq2))
        self.wait(1)

        # ─────────────────────────────
        # CENA 3 – x
        # ─────────────────────────────
        self.play(FadeOut(sec2))

        sec3 = Text("3. Isolando x", font_size=34, color=TITULO_COR)
        sec3.to_edge(UP)
        self.play(Write(sec3))

        steps = VGroup(
            tex("b^2 = c^2 - x^2 + (a-x)^2"),
            tex("b^2 = c^2 + a^2 - 2ax"),
            tex("x = (a^2 - b^2 + c^2)/(2a)", DEST_COR)
        ).arrange(DOWN).to_edge(LEFT)

        for s in steps:
            self.play(Write(s))
            self.wait(0.5)

        # ─────────────────────────────
        # CENA FINAL – HERON
        # ─────────────────────────────
        self.play(*[FadeOut(m) for m in self.mobjects])

        sec4 = Text("Fórmula de Heron", font_size=40, color=TITULO_COR)
        sec4.to_edge(UP)
        self.play(Write(sec4))

        formula = tex("A = √(p(p-a)(p-b)(p-c))", VERDE, 40)
        formula.move_to(ORIGIN)

        self.play(Write(formula))
        self.wait(3)