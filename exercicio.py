from manim import *

class BandeiraBrasil(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # ── Cores ─────────────────────────────────────────────────────────
        TITULO_COR = "#6B0033"
        TEXTO_COR  = "#1a1a1a"
        DEST_COR   = "#B03A2E"
        LABEL_COR  = "#1A5276"
        VERDE_BR   = "#009C3B"   # verde da bandeira
        AMARELO_BR = "#FFDF00"   # amarelo da bandeira
        AZUL_BR    = "#002776"   # azul do círculo
        VERDE_ESC  = "#145A32"   # verde para respostas

        # ── Helper de texto ────────────────────────────────────────────────
        def T(s, cor=TEXTO_COR, sz=28):
            return Text(s, color=cor, font_size=sz)

        def ST(s, cor=TEXTO_COR, sz=24):
            return Text(s, color=cor, font_size=sz)

        # ════════════════════════════════════════════════════════════════════
        # CENA 0 – Título
        # ════════════════════════════════════════════════════════════════════
        titulo = Text("Bandeira do Brasil", font_size=50,
                      color=TITULO_COR, weight=BOLD)
        sub    = Text("(Unicamp-SP)  —  Geometria Plana",
                      font_size=26, color=TEXTO_COR)
        VGroup(titulo, sub).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(Write(titulo))
        self.play(FadeIn(sub))
        self.wait(1.5)
        self.play(FadeOut(titulo), FadeOut(sub))

        # ════════════════════════════════════════════════════════════════════
        # CENA 1 – Enunciado e diagrama da bandeira
        # ════════════════════════════════════════════════════════════════════
        sec1 = T("1. Enunciado e Dados", TITULO_COR, 34).to_edge(UP)
        self.play(Write(sec1))

        # ── Diagrama proporcional ──
        # Dimensões reais: 2,00 m × 1,40 m → escala ×2.2 → 4,40 × 3,08
        # Usaremos escala ×2 para caber: 4,0 × 2,8 … porém a cena é ±7×4
        # Escolhemos: rect 5.0 × 3.5  (ratio 10:7 ≈ 2:1.4 ✓)
        SCALE = 2.5          # 1 metro = 2.5 unidades Manim

        rw = 2.0 * SCALE     # 5.0
        rh = 1.4 * SCALE     # 3.5
        d  = 0.17 * SCALE    # distância dos vértices do losango ao ret = 0.425

        # Retângulo verde
        rect = Rectangle(width=rw, height=rh, color=VERDE_BR, stroke_width=2.5)
        rect.set_fill(VERDE_BR, opacity=0.85)
        rect.move_to(ORIGIN)

        # Vértices do losango (distam 17 cm = d de cada lado)
        # Losango: vértices no meio dos lados, deslocados d para dentro
        # Topo e base: distam d da borda vertical → x fixo, y ± (rh/2 - d)
        # Esq e Dir:   distam d da borda horizontal → y fixo, x ± (rw/2 - d)
        lTop  = np.array([ 0,       rh/2 - d, 0])
        lBot  = np.array([ 0,     -(rh/2 - d), 0])
        lLeft = np.array([-(rw/2 - d), 0,       0])
        lRig  = np.array([ rw/2 - d,  0,        0])

        losango = Polygon(lTop, lRig, lBot, lLeft,
                          color=AMARELO_BR, stroke_width=2)
        losango.set_fill(AMARELO_BR, opacity=0.90)

        # Círculo: raio 35 cm = 0.35*2.5 = 0.875
        r_circ = 0.35 * SCALE
        circ = Circle(radius=r_circ, color=AZUL_BR, stroke_width=2)
        circ.set_fill(AZUL_BR, opacity=0.90)
        circ.move_to(ORIGIN)

        # Montar em ordem (fundo → frente)
        self.play(FadeIn(rect))
        self.play(FadeIn(losango))
        self.play(FadeIn(circ))
        self.wait(0.5)

        # Cotas
        # Largura do retângulo
        arr_w = DoubleArrow(rect.get_corner(DL) + DOWN*0.35,
                            rect.get_corner(DR) + DOWN*0.35,
                            buff=0, color=LABEL_COR, tip_length=0.15, stroke_width=2)
        lbl_w = ST("2,00 m", LABEL_COR, 20).next_to(arr_w, DOWN, buff=0.1)

        # Altura do retângulo
        arr_h = DoubleArrow(rect.get_corner(DR) + RIGHT*0.35,
                            rect.get_corner(UR) + RIGHT*0.35,
                            buff=0, color=LABEL_COR, tip_length=0.15, stroke_width=2)
        lbl_h = ST("1,40 m", LABEL_COR, 20).next_to(arr_h, RIGHT, buff=0.1)

        # Distância d (seta do canto do ret ao vértice do losango – lado esq)
        p1 = rect.get_left()           # meio do lado esquerdo
        p2 = lLeft
        arr_d = DoubleArrow(p1, p2, buff=0, color=DEST_COR,
                            tip_length=0.12, stroke_width=1.8)
        lbl_d = ST("17 cm", DEST_COR, 18).next_to(arr_d, DOWN, buff=0.08)

        # Raio
        r_line = Line(ORIGIN, ORIGIN + RIGHT*r_circ, color=WHITE, stroke_width=2)
        lbl_r  = ST("r=35cm", WHITE, 18).move_to(
            ORIGIN + RIGHT*(r_circ/2) + UP*0.18)

        self.play(Create(arr_w), Write(lbl_w))
        self.play(Create(arr_h), Write(lbl_h))
        self.play(Create(arr_d), Write(lbl_d))
        self.play(Create(r_line), Write(lbl_r))
        self.wait(2)

        self.play(FadeOut(sec1))

        # ════════════════════════════════════════════════════════════════════
        # CENA 2 – Dados numéricos
        # ════════════════════════════════════════════════════════════════════
        self.play(*[FadeOut(m) for m in self.mobjects])

        sec2 = T("2. Organizando os Dados", TITULO_COR, 34).to_edge(UP)
        self.play(Write(sec2))

        dados = VGroup(
            ST("Retângulo:  comprimento = 2,00 m  |  largura = 1,40 m", TEXTO_COR, 25),
            ST("Vértices do losango distam 17 cm dos lados do retângulo", TEXTO_COR, 25),
            ST("Raio do círculo: r = 35 cm = 0,35 m", TEXTO_COR, 25),
            ST("π ≈ 22/7", TEXTO_COR, 25),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        dados.move_to(ORIGIN).shift(UP * 0.3)

        for d in dados:
            self.play(Write(d))
            self.wait(0.4)

        # Dimensões do losango
        sep = Line(LEFT*5, RIGHT*5, color=TITULO_COR, stroke_width=1).next_to(dados, DOWN, buff=0.3)
        self.play(Create(sep))

        dim_los = VGroup(
            ST("Diagonal maior do losango:", LABEL_COR, 24),
            ST("  D = 2,00 − 2×0,17 = 2,00 − 0,34 = 1,66 m", TEXTO_COR, 24),
            ST("Diagonal menor do losango:", LABEL_COR, 24),
            ST("  d = 1,40 − 2×0,17 = 1,40 − 0,34 = 1,06 m", TEXTO_COR, 24),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        dim_los.next_to(sep, DOWN, buff=0.25)

        for s in dim_los:
            self.play(Write(s))
            self.wait(0.35)

        self.wait(1.5)
        self.play(FadeOut(sec2))

        # ════════════════════════════════════════════════════════════════════
        # CENA 3 – Cálculo das áreas parciais
        # ════════════════════════════════════════════════════════════════════
        self.play(*[FadeOut(m) for m in self.mobjects])

        sec3 = T("3. Calculando as Áreas", TITULO_COR, 34).to_edge(UP)
        self.play(Write(sec3))

        areas = VGroup(
            ST("Área do retângulo (A_ret):", LABEL_COR, 26),
            ST("  A_ret = 2,00 × 1,40 = 2,80 m²", TEXTO_COR, 26),
            ST("Área do losango (A_los):", LABEL_COR, 26),
            ST("  A_los = (D × d) / 2 = (1,66 × 1,06) / 2", TEXTO_COR, 26),
            ST("  A_los = 1,7596 / 2 = 0,8798 m²", TEXTO_COR, 26),
            ST("Área do círculo (A_cir):", LABEL_COR, 26),
            ST("  A_cir = π × r² = (22/7) × (0,35)²", TEXTO_COR, 26),
            ST("  A_cir = (22/7) × 0,1225 = 2,695 / 7", TEXTO_COR, 26),
            ST("  A_cir = 0,385 m²", TEXTO_COR, 26),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        areas.move_to(ORIGIN).shift(DOWN * 0.2)

        for s in areas:
            self.play(Write(s))
            self.wait(0.30)

        self.wait(1.5)
        self.play(FadeOut(sec3))

        # ════════════════════════════════════════════════════════════════════
        # CENA 4 – Item (a): Área verde
        # ════════════════════════════════════════════════════════════════════
        self.play(*[FadeOut(m) for m in self.mobjects])

        sec4 = T("4. Item (a) – Área Verde", TITULO_COR, 34).to_edge(UP)
        self.play(Write(sec4))

        # Mini diagrama (retângulo + losango) para visualização
        sc = 1.4
        r2 = Rectangle(width=2*sc, height=1.4*sc, color=VERDE_BR,
                        stroke_width=2).set_fill(VERDE_BR, opacity=0.7)
        d2 = 0.17 * sc
        vT = np.array([ 0,     1.4*sc/2 - d2, 0])
        vB = np.array([ 0,   -(1.4*sc/2 - d2), 0])
        vL = np.array([-(2*sc/2 - d2), 0, 0])
        vR = np.array([ 2*sc/2 - d2,  0, 0])
        l2 = Polygon(vT, vR, vB, vL, color=AMARELO_BR,
                     stroke_width=2).set_fill(AMARELO_BR, opacity=0.85)
        diag = VGroup(r2, l2).shift(LEFT*3)
        self.play(FadeIn(diag))

        calc_a = VGroup(
            ST("A_verde = A_ret − A_losango", LABEL_COR, 26),
            ST("A_verde = 2,80 − 0,8798", TEXTO_COR, 26),
            ST("A_verde ≈ 1,9202 m²", DEST_COR, 28),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        calc_a.shift(RIGHT * 1.2 + DOWN * 0.2)

        for s in calc_a:
            self.play(Write(s))
            self.wait(0.5)

        # Caixa de resposta
        resp_a = T("Área verde ≈ 1,9202 m²", VERDE_ESC, 30)
        box_a  = SurroundingRectangle(resp_a, color=VERDE_ESC, buff=0.2,
                                      corner_radius=0.1)
        resp_a.next_to(calc_a, DOWN, buff=0.45)
        box_a.move_to(resp_a)
        self.play(Write(resp_a), Create(box_a))
        self.wait(2)
        self.play(FadeOut(sec4))

        # ════════════════════════════════════════════════════════════════════
        # CENA 5 – Item (b): Porcentagem amarela
        # ════════════════════════════════════════════════════════════════════
        self.play(*[FadeOut(m) for m in self.mobjects])

        sec5 = T("5. Item (b) – % Área Amarela", TITULO_COR, 34).to_edge(UP)
        self.play(Write(sec5))

        expl = ST("A região amarela = losango  SEM  o círculo",
                  LABEL_COR, 26).shift(UP * 1.8)
        self.play(Write(expl))

        calc_b = VGroup(
            ST("A_amarela = A_los − A_cir", LABEL_COR, 26),
            ST("A_amarela = 0,8798 − 0,385", TEXTO_COR, 26),
            ST("A_amarela = 0,4948 m²", TEXTO_COR, 26),
            ST("Porcentagem =  A_amarela / A_ret × 100", LABEL_COR, 26),
            ST("Porcentagem =  0,4948 / 2,80 × 100", TEXTO_COR, 26),
            ST("Porcentagem =  17,671...%", TEXTO_COR, 26),
            ST("Porcentagem ≈  17,67%", DEST_COR, 28),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        calc_b.move_to(ORIGIN).shift(DOWN * 0.1)

        for s in calc_b:
            self.play(Write(s))
            self.wait(0.35)

        resp_b = T("Área amarela ≈ 17,67% da bandeira", VERDE_ESC, 30)
        box_b  = SurroundingRectangle(resp_b, color=VERDE_ESC, buff=0.2,
                                      corner_radius=0.1)
        resp_b.next_to(calc_b, DOWN, buff=0.4)
        box_b.move_to(resp_b)
        self.play(Write(resp_b), Create(box_b))
        self.wait(2)
        self.play(FadeOut(sec5))

        # ════════════════════════════════════════════════════════════════════
        # CENA FINAL – Resumo
        # ════════════════════════════════════════════════════════════════════
        self.play(*[FadeOut(m) for m in self.mobjects])

        titulo_fin = T("Resumo das Respostas", TITULO_COR, 40).to_edge(UP)
        self.play(Write(titulo_fin))

        # Bandeira estilizada (mini)
        sc = 1.1
        rect_f = Rectangle(width=2*sc, height=1.4*sc).set_fill(VERDE_BR, 0.8)
        d_f = 0.17 * sc
        vT_f = np.array([ 0,   1.4*sc/2 - d_f, 0])
        vB_f = np.array([ 0, -(1.4*sc/2 - d_f), 0])
        vL_f = np.array([-(2*sc/2 - d_f), 0, 0])
        vR_f = np.array([ 2*sc/2 - d_f, 0,  0])
        los_f = Polygon(vT_f, vR_f, vB_f, vL_f).set_fill(AMARELO_BR, 0.9)
        cir_f = Circle(radius=0.35*sc).set_fill(AZUL_BR, 0.9)
        band = VGroup(rect_f, los_f, cir_f).shift(LEFT * 3.5)
        self.play(FadeIn(band))

        respostas = VGroup(
            ST("(a)  Área verde = A_ret − A_los", TEXTO_COR, 26),
            ST("     = 2,80 − 0,8798 ≈ 1,9202 m²", VERDE_ESC, 27),
            ST("(b)  % amarela = A_amarela / A_ret × 100", TEXTO_COR, 26),
            ST("     = 0,4948 / 2,80 × 100 ≈ 17,67%", VERDE_ESC, 27),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        respostas.shift(RIGHT * 1.4 + DOWN * 0.1)

        for s in respostas:
            self.play(Write(s))
            self.wait(0.5)

        self.wait(3)