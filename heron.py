from manim import *

class DeducaoHeron(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # ── Cores (paleta do slide) ──────────────────────────────────────────
        TITULO_COR  = "#6B0033"
        TEXTO_COR   = "#1a1a1a"
        DEST_COR    = "#B03A2E"
        LABEL_COR   = "#1A5276"
        VERDE       = "#145A32"
        LARANJA     = "#E67E22"

        # ── Helpers de texto sem LaTeX ────────────────────────────────────────
        def fmt(s):
            return (s.replace("\\sqrt", "√")
                     .replace("\\cdot", "·")
                     .replace("\\Rightarrow", "⇒")
                     .replace("\\frac", "")
                     .replace("{", "").replace("}", "")
                     .replace("\\", ""))

        def T(s, cor=TEXTO_COR, sz=30):
            return Text(fmt(s), color=cor, font_size=sz)

        def ST(s, cor=TEXTO_COR, sz=25):
            return Text(fmt(s), color=cor, font_size=sz)

        # ════════════════════════════════════════════════════════════════════
        # CENA 0 – Título
        # ════════════════════════════════════════════════════════════════════
        titulo = Text("Fórmula de Heron", font_size=54,
                      color=TITULO_COR, weight=BOLD)
        sub    = Text("Dedução completa – Matemática 4",
                      font_size=28, color=TEXTO_COR)
        VGroup(titulo, sub).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(Write(titulo))
        self.play(FadeIn(sub, shift=UP*0.2))
        self.wait(1.5)
        self.play(FadeOut(titulo), FadeOut(sub))

        # ════════════════════════════════════════════════════════════════════
        # CENA 1 – Configuração do triângulo
        # ════════════════════════════════════════════════════════════════════
        sec = Text("1. Configuração do triângulo",
                   font_size=36, color=TITULO_COR)
        sec.to_edge(UP)
        self.play(Write(sec))

        # Vértices
        B = np.array([-3.2, -1.8, 0])
        C = np.array([ 3.2, -1.8, 0])
        A = np.array([ 0.0,  2.0, 0])
        H = np.array([ 0.0, -1.8, 0])   # pé da altitude

        tri = Polygon(A, B, C, color=TITULO_COR, stroke_width=2.5)
        tri.set_fill("#FAD7A0", opacity=0.25)

        # Rótulos dos vértices
        lA = Text("A", font_size=26, color=LABEL_COR).next_to(A, UP*0.4)
        lB = Text("B", font_size=26, color=LABEL_COR).next_to(B, LEFT*0.4)
        lC = Text("C", font_size=26, color=LABEL_COR).next_to(C, RIGHT*0.4)

        # Rótulos dos lados
        lc = Text("c", font_size=24, color=TEXTO_COR).move_to(
            (A + B) / 2 + np.array([-0.35, 0, 0]))
        lb = Text("b", font_size=24, color=TEXTO_COR).move_to(
            (A + C) / 2 + np.array([ 0.35, 0, 0]))
        la = Text("a", font_size=24, color=TEXTO_COR).move_to(
            (B + C) / 2 + np.array([ 0, -0.35, 0]))

        # Altitude h
        alt     = DashedLine(A, H, color=DEST_COR, dash_length=0.15)
        sq_mark = Square(side_length=0.18, color=DEST_COR,
                         stroke_width=1.5).move_to(H + np.array([0.09, 0.09, 0]))
        lh      = Text("h", font_size=24, color=DEST_COR).next_to(alt, RIGHT, buff=0.12)

        # x e a-x
        lx    = Text("x", font_size=22, color=LARANJA).move_to(
            (B + H) / 2 + np.array([0, -0.35, 0]))
        lax   = Text("a − x", font_size=22, color=LARANJA).move_to(
            (H + C) / 2 + np.array([0, -0.35, 0]))

        self.play(Create(tri))
        self.play(Write(lA), Write(lB), Write(lC))
        self.play(Write(lc), Write(lb), Write(la))
        self.play(Create(alt), Create(sq_mark), Write(lh))
        self.play(Write(lx), Write(lax))
        self.wait(1.5)

        self.play(FadeOut(sec))

        # ════════════════════════════════════════════════════════════════════
        # CENA 2 – Teorema de Pitágoras nos dois triângulos retângulos
        # ════════════════════════════════════════════════════════════════════
        sec2 = Text("2. Pitágoras nos triângulos AHB e AHC",
                    font_size=32, color=TITULO_COR).to_edge(UP)
        self.play(Write(sec2))

        eq_I  = ST("(I)  c² = h² + x²       ⇒   h² = c² − x²",
                   TEXTO_COR, 26)
        eq_II = ST("(II) b² = h² + (a − x)²", TEXTO_COR, 26)

        eqs = VGroup(eq_I, eq_II).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        eqs.to_edge(RIGHT, buff=0.5).shift(DOWN * 0.3)

        self.play(Write(eq_I))
        self.wait(0.6)
        self.play(Write(eq_II))
        self.wait(1.5)
        self.play(FadeOut(sec2))

        # ════════════════════════════════════════════════════════════════════
        # CENA 3 – Isolando x
        # ════════════════════════════════════════════════════════════════════
        sec3 = Text("3. Substituindo (I) em (II) e isolando x",
                    font_size=32, color=TITULO_COR).to_edge(UP)
        self.play(Write(sec3))

        steps = VGroup(
            ST("b² = c² − x² + (a − x)²",        TEXTO_COR, 26),
            ST("b² = c² − x² + a² − 2ax + x²",   TEXTO_COR, 26),
            ST("b² = c² + a² − 2ax",               TEXTO_COR, 26),
            ST("2ax = a² − b² + c²",               TEXTO_COR, 26),
            ST("x = (a² − b² + c²) / (2a)",        DEST_COR,  27),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        steps.to_edge(LEFT, buff=0.7).shift(DOWN * 0.3)

        for s in steps:
            self.play(Write(s))
            self.wait(0.45)
        self.wait(1)
        self.play(FadeOut(sec3))

        # ════════════════════════════════════════════════════════════════════
        # CENA 4 – Obtendo h²
        # ════════════════════════════════════════════════════════════════════
        self.play(*[FadeOut(m) for m in self.mobjects])

        sec4 = Text("4. Calculando h²  (substituindo x em (I))",
                    font_size=31, color=TITULO_COR).to_edge(UP)
        self.play(Write(sec4))

        h2_steps = VGroup(
            ST("h² = c² − x²",                              TEXTO_COR, 26),
            ST("h² = [4a²c² − (a² − b² + c²)²] / (4a²)",  TEXTO_COR, 25),
            ST("A² = (a·h/2)²  = a²h²/4",                   TEXTO_COR, 26),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        h2_steps.move_to(ORIGIN).shift(DOWN * 0.2)

        for s in h2_steps:
            self.play(Write(s))
            self.wait(0.6)
        self.wait(1)
        self.play(FadeOut(sec4))

        # ════════════════════════════════════════════════════════════════════
        # CENA 5 – Fatoração e semiperímetro
        # ════════════════════════════════════════════════════════════════════
        self.play(*[FadeOut(m) for m in self.mobjects])

        sec5 = Text("5. Fatoração usando diferença de quadrados",
                    font_size=31, color=TITULO_COR).to_edge(UP)
        self.play(Write(sec5))

        fat = VGroup(
            ST("(2ac)² − (a² − b² + c²)²  =",                TEXTO_COR, 24),
            ST("= [2ac + (a² − b² + c²)] · [2ac − (a² − b² + c²)]", TEXTO_COR, 22),
            ST("= [(a+c)² − b²] · [b² − (a−c)²]",             TEXTO_COR, 24),
            ST("= (a+c+b)(a+c−b) · (b+a−c)(b−a+c)",           TEXTO_COR, 24),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        fat.move_to(ORIGIN)

        for s in fat:
            self.play(Write(s))
            self.wait(0.5)
        self.wait(1)

        semi = ST("Semiperímetro:  p = (a + b + c) / 2", LABEL_COR, 27)
        semi.next_to(fat, DOWN, buff=0.45)
        self.play(Write(semi))
        self.wait(1)

        sub_p = ST("A² = p(p−a)(p−b)(p−c)", DEST_COR, 29)
        sub_p.next_to(semi, DOWN, buff=0.35)
        self.play(Write(sub_p))
        self.wait(1.5)
        self.play(FadeOut(sec5))

        # ════════════════════════════════════════════════════════════════════
        # CENA FINAL – Fórmula de Heron + exemplo numérico
        # ════════════════════════════════════════════════════════════════════
        self.play(*[FadeOut(m) for m in self.mobjects])

        sec_fin = Text("Fórmula de Heron", font_size=42,
                       color=TITULO_COR).to_edge(UP)
        self.play(Write(sec_fin))

        formula = Text("A = √[ p(p−a)(p−b)(p−c) ]",
                       font_size=42, color=VERDE)
        box = SurroundingRectangle(formula, color=VERDE,
                                   buff=0.25, corner_radius=0.12)
        formula.move_to(ORIGIN).shift(UP * 0.8)
        box.move_to(formula)

        self.play(Write(formula), Create(box))
        self.wait(0.8)

        nota = ST("Esta fórmula permite calcular a área de qualquer triângulo\n"
                  "conhecendo apenas as medidas dos três lados.",
                  TEXTO_COR, 24)
        nota.next_to(box, DOWN, buff=0.4)
        self.play(FadeIn(nota))
        self.wait(0.8)

        # Exemplo numérico (Observação 3 do slide)
        sep = Line(LEFT * 5.5, RIGHT * 5.5, color=TITULO_COR,
                   stroke_width=1.2).next_to(nota, DOWN, buff=0.35)
        self.play(Create(sep))

        ex_title = Text("Exemplo  (lados: 26 cm, 26 cm, 20 cm)",
                        font_size=24, color=LABEL_COR)
        ex_title.next_to(sep, DOWN, buff=0.2)
        self.play(Write(ex_title))

        ex_steps = VGroup(
            ST("p = (26 + 26 + 20) / 2 = 36", TEXTO_COR, 23),
            ST("A = √[36 · (36−26) · (36−26) · (36−20)]", TEXTO_COR, 23),
            ST("A = √[36 · 10 · 10 · 16]  =  √57600", TEXTO_COR, 23),
            ST("A = 240 cm²", VERDE, 26),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        ex_steps.next_to(ex_title, DOWN, buff=0.25).shift(RIGHT * 0.3)

        for s in ex_steps:
            self.play(Write(s))
            self.wait(0.45)

        self.wait(3)