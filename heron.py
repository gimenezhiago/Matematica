from manim import *

class DeducaoHeron(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # ── helpers de cor ──────────────────────────────────────────────
        TITULO_COR   = "#6B0033"
        TEXTO_COR    = "#1a1a1a"
        DEST_COR     = "#B03A2E"
        LABEL_COR    = "#1A5276"
        VERDE        = "#145A32"

        def tex(s, cor=TEXTO_COR, sz=32):
            return MathTex(s, color=cor, font_size=sz)

        def stex(s, cor=TEXTO_COR, sz=28):
            return MathTex(s, color=cor, font_size=sz)

        # ════════════════════════════════════════════════════════════════
        # CENA 0 – Título
        # ════════════════════════════════════════════════════════════════
        titulo = Text("Fórmula de Heron", font_size=52,
                      color=TITULO_COR, weight=BOLD)
        sub    = Text("Dedução completa  –  Matemática 4",
                      font_size=28, color=TEXTO_COR)
        VGroup(titulo, sub).arrange(DOWN, buff=0.35).move_to(ORIGIN)

        self.play(Write(titulo), run_time=1.5)
        self.play(FadeIn(sub, shift=UP*0.3))
        self.wait(1.5)
        self.play(FadeOut(titulo), FadeOut(sub))

        # ════════════════════════════════════════════════════════════════
        # CENA 1 – Triângulo ABC com altura h e pé H
        # ════════════════════════════════════════════════════════════════
        sec1 = Text("1. Configuração do triângulo",
                    font_size=36, color=TITULO_COR, weight=BOLD)
        sec1.to_edge(UP, buff=0.4)
        self.play(Write(sec1))

        # Vértices
        B = np.array([-3.2, -1.5, 0])
        C = np.array([ 3.2, -1.5, 0])
        A = np.array([-0.6,  1.8, 0])
        H = np.array([-0.6, -1.5, 0])   # pé da altitude

        tri = Polygon(A, B, C, color=TITULO_COR, stroke_width=2.5)
        tri.set_fill(color="#FAD7A0", opacity=0.25)

        # Altitude tracejada
        alt = DashedLine(A, H, color=DEST_COR, dash_length=0.12)
        alt_lbl = tex("h", cor=DEST_COR, sz=26).next_to(
            alt.get_center(), RIGHT, buff=0.12)

        # Rótulos dos vértices
        lA = Text("A", font_size=26, color=LABEL_COR).next_to(A, UP, buff=0.12)
        lB = Text("B", font_size=26, color=LABEL_COR).next_to(B, DL, buff=0.1)
        lC = Text("C", font_size=26, color=LABEL_COR).next_to(C, DR, buff=0.1)
        lH = Text("H", font_size=22, color=LABEL_COR).next_to(H, DOWN, buff=0.1)

        # Rótulos dos lados
        def mid(P, Q): return (P + Q) / 2

        la = stex("a", cor=LABEL_COR, sz=24).next_to(mid(B, C), DOWN,  buff=0.15)
        lb = stex("b", cor=LABEL_COR, sz=24).next_to(mid(A, C), RIGHT, buff=0.15)
        lc = stex("c", cor=LABEL_COR, sz=24).next_to(mid(A, B), LEFT,  buff=0.15)

        # Segmento x (BH) e (a-x) (HC)
        lx   = stex("x",     cor=VERDE, sz=22).next_to(mid(B, H), DOWN, buff=0.12)
        lax  = stex("a-x",   cor=VERDE, sz=22).next_to(mid(H, C), DOWN, buff=0.12)

        # Ângulo reto em H
        sq = Square(side_length=0.18, color=DEST_COR, stroke_width=1.5)
        sq.move_to(H + np.array([0.09, 0.09, 0]))

        self.play(Create(tri), run_time=1.2)
        self.play(*[Write(l) for l in [lA, lB, lC]])
        self.play(Create(alt), Write(alt_lbl), FadeIn(sq))
        self.play(Write(lH), Write(la), Write(lb), Write(lc),
                  Write(lx), Write(lax))
        self.wait(1.5)

        # ════════════════════════════════════════════════════════════════
        # CENA 2 – Pitágoras nos dois triângulos retângulos
        # ════════════════════════════════════════════════════════════════
        self.play(FadeOut(sec1))
        sec2 = Text("2. Pitágoras em AHB e AHC",
                    font_size=34, color=TITULO_COR, weight=BOLD)
        sec2.to_edge(UP, buff=0.4)
        self.play(Write(sec2))

        eq_I  = tex(r"\text{(I)}\quad c^2 = h^2 + x^2 \;\Rightarrow\; h^2 = c^2 - x^2",
                    cor=TEXTO_COR, sz=30)
        eq_II = tex(r"\text{(II)}\quad b^2 = h^2 + (a-x)^2",
                    cor=TEXTO_COR, sz=30)
        eqs = VGroup(eq_I, eq_II).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        eqs.to_edge(RIGHT, buff=0.5).shift(DOWN*0.3)

        self.play(Write(eq_I))
        self.wait(0.8)
        self.play(Write(eq_II))
        self.wait(1.5)

        # ════════════════════════════════════════════════════════════════
        # CENA 3 – Isolando x
        # ════════════════════════════════════════════════════════════════
        self.play(FadeOut(sec2))
        sec3 = Text("3. Isolando x  –  substituindo (I) em (II)",
                    font_size=32, color=TITULO_COR, weight=BOLD)
        sec3.to_edge(UP, buff=0.4)
        self.play(Write(sec3))

        steps3 = VGroup(
            tex(r"b^2 = c^2 - x^2 + (a-x)^2", sz=28),
            tex(r"b^2 = c^2 - x^2 + a^2 - 2ax + x^2", sz=28),
            tex(r"b^2 = c^2 + a^2 - 2ax", sz=28),
            tex(r"\Rightarrow\; x = \dfrac{a^2 - b^2 + c^2}{2a}", sz=30, cor=DEST_COR),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        steps3.next_to(sec3, DOWN, buff=0.55).to_edge(LEFT, buff=1.0)

        for s in steps3:
            self.play(Write(s), run_time=0.9)
            self.wait(0.5)
        self.wait(1.0)

        # ════════════════════════════════════════════════════════════════
        # CENA 4 – Calculando h²
        # ════════════════════════════════════════════════════════════════
        self.play(FadeOut(sec3), FadeOut(steps3),
                  FadeOut(tri), FadeOut(alt), FadeOut(alt_lbl), FadeOut(sq),
                  *[FadeOut(o) for o in [lA, lB, lC, lH, la, lb, lc, lx, lax]],
                  FadeOut(eq_I), FadeOut(eq_II))

        sec4 = Text("4. Calculando h²",
                    font_size=36, color=TITULO_COR, weight=BOLD)
        sec4.to_edge(UP, buff=0.4)
        self.play(Write(sec4))

        h2_eq = VGroup(
            tex(r"h^2 = c^2 - x^2 = c^2 - \left(\dfrac{a^2-b^2+c^2}{2a}\right)^{\!2}", sz=28),
            tex(r"h^2 = \dfrac{4a^2c^2 - (a^2-b^2+c^2)^2}{4a^2}", sz=30, cor=DEST_COR),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.55)
        h2_eq.next_to(sec4, DOWN, buff=0.6).to_edge(LEFT, buff=0.8)

        for s in h2_eq:
            self.play(Write(s), run_time=1.0)
            self.wait(0.6)
        self.wait(1.2)

        # ════════════════════════════════════════════════════════════════
        # CENA 5 – Diferença de quadrados
        # ════════════════════════════════════════════════════════════════
        self.play(FadeOut(sec4), FadeOut(h2_eq))
        sec5 = Text("5. Diferença de quadrados",
                    font_size=36, color=TITULO_COR, weight=BOLD)
        sec5.to_edge(UP, buff=0.4)
        self.play(Write(sec5))

        steps5 = VGroup(
            tex(r"4a^2c^2 - (a^2-b^2+c^2)^2 = (2ac)^2 - (a^2-b^2+c^2)^2", sz=25),
            tex(r"= \bigl[2ac+(a^2-b^2+c^2)\bigr]\cdot\bigl[2ac-(a^2-b^2+c^2)\bigr]", sz=25),
            tex(r"= \bigl[(a+c)^2-b^2\bigr]\cdot\bigl[b^2-(a-c)^2\bigr]", sz=25),
            tex(r"= (a+c+b)(a+c-b)\cdot(b+a-c)(b-a+c)", sz=25, cor=DEST_COR),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.38)
        steps5.next_to(sec5, DOWN, buff=0.5).to_edge(LEFT, buff=0.5)

        for s in steps5:
            self.play(Write(s), run_time=1.0)
            self.wait(0.5)
        self.wait(1.2)

        # ════════════════════════════════════════════════════════════════
        # CENA 6 – Semiperímetro p
        # ════════════════════════════════════════════════════════════════
        self.play(FadeOut(sec5), FadeOut(steps5))
        sec6 = Text("6. Semiperímetro  p",
                    font_size=36, color=TITULO_COR, weight=BOLD)
        sec6.to_edge(UP, buff=0.4)
        self.play(Write(sec6))

        sp_def = tex(r"p = \dfrac{a+b+c}{2}", sz=34, cor=TITULO_COR)
        sp_sub = VGroup(
            tex(r"a+b+c-2b = 2p - 2b \;=\; 2(p-b)", sz=28),
            tex(r"a+b+c-2a = 2(p-a)", sz=28),
            tex(r"a+b+c-2c = 2(p-c)", sz=28),
            tex(r"a+b+c    = 2p", sz=28),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        sp_def.next_to(sec6, DOWN, buff=0.5)
        sp_sub.next_to(sp_def, DOWN, buff=0.45).to_edge(LEFT, buff=0.9)

        self.play(Write(sp_def))
        self.wait(0.5)
        for s in sp_sub:
            self.play(Write(s), run_time=0.7)
            self.wait(0.3)
        self.wait(1.0)

        conclusion6 = tex(
            r"\Rightarrow\; 4a^2 h^2 = 16\,p(p-a)(p-b)(p-c)",
            sz=30, cor=DEST_COR)
        conclusion6.next_to(sp_sub, DOWN, buff=0.5).to_edge(LEFT, buff=0.9)
        self.play(Write(conclusion6))
        self.wait(1.5)

        # ════════════════════════════════════════════════════════════════
        # CENA 7 – Área e resultado final
        # ════════════════════════════════════════════════════════════════
        self.play(FadeOut(sec6), FadeOut(sp_def),
                  FadeOut(sp_sub), FadeOut(conclusion6))
        sec7 = Text("7. Área do triângulo",
                    font_size=36, color=TITULO_COR, weight=BOLD)
        sec7.to_edge(UP, buff=0.4)
        self.play(Write(sec7))

        area_steps = VGroup(
            tex(r"A = \dfrac{a \cdot h}{2}", sz=32),
            tex(r"A^2 = \dfrac{a^2 h^2}{4}", sz=32),
            tex(r"16\,A^2 = 4a^2 h^2 = 16\,p(p-a)(p-b)(p-c)", sz=30),
            tex(r"A^2 = p(p-a)(p-b)(p-c)", sz=32, cor=DEST_COR),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        area_steps.next_to(sec7, DOWN, buff=0.6).to_edge(LEFT, buff=1.2)

        for s in area_steps:
            self.play(Write(s), run_time=0.9)
            self.wait(0.5)
        self.wait(0.8)

        # Fórmula de Heron em destaque
        box = SurroundingRectangle(
            VGroup(
                tex(r"\boxed{\;A = \sqrt{p\,(p-a)(p-b)(p-c)}\;}",
                    sz=40, cor="#FFFFFF"),
            ),
            color=TITULO_COR, buff=0.35, corner_radius=0.15,
            stroke_width=3, fill_color=TITULO_COR, fill_opacity=0.90)

        heron_final = tex(r"A = \sqrt{p\,(p-a)(p-b)(p-c)}",
                          sz=42, cor="#FFFFFF")
        grp = VGroup(box, heron_final)
        grp.arrange(ORIGIN)
        box.move_to(heron_final)
        grp.next_to(area_steps, DOWN, buff=0.6)

        self.play(FadeIn(box), Write(heron_final), run_time=1.2)
        self.wait(0.6)

        label_heron = Text("Fórmula de Heron", font_size=22,
                           color=TITULO_COR, weight=BOLD)
        label_heron.next_to(grp, DOWN, buff=0.22)
        self.play(Write(label_heron))
        self.wait(2.5)

        # ════════════════════════════════════════════════════════════════
        # CENA BÔNUS – Exemplo numérico (lados 26, 26, 20)
        # ════════════════════════════════════════════════════════════════
        self.play(*[FadeOut(o) for o in self.mobjects])

        sec_ex = Text("Exemplo  –  lados 26, 26 e 20 cm",
                      font_size=36, color=TITULO_COR, weight=BOLD)
        sec_ex.to_edge(UP, buff=0.4)
        self.play(Write(sec_ex))

        ex_steps = VGroup(
            tex(r"p = \dfrac{26+26+20}{2} = 36", sz=30),
            tex(r"A = \sqrt{36 \cdot (36-26)(36-26)(36-20)}", sz=30),
            tex(r"A = \sqrt{36 \cdot 10 \cdot 10 \cdot 16}", sz=30),
            tex(r"A = \sqrt{57\,600}", sz=30),
            tex(r"A = 240 \text{ cm}^2", sz=34, cor=VERDE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.42)
        ex_steps.next_to(sec_ex, DOWN, buff=0.55).to_edge(LEFT, buff=1.2)

        for s in ex_steps:
            self.play(Write(s), run_time=0.8)
            self.wait(0.45)
        self.wait(2.0)