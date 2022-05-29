import json
from itertools import zip_longest

import matplotlib.pyplot as plt
import numpy as np

from ManimR import *
from object import *
from chanim import *

# with open("data/painting.json") as f:
#     jsonObject = json.load(f)
#
# data = jsonObject["series"]["Submitter"]
#
# wavenumber = []
# absorbance = []
# for key in data:
#     wavenumber.append(round(float(key), 8))
#     absorbance.append(max(round(data[key], 8), 0))
#
# wavenumber = np.array(wavenumber)
# absorbance = np.array(absorbance)
#
#
# fig, ax = plt.subplots()
# ax.plot(wavenumber, 10**(-absorbance)) # Transmitance = 10**(-absorbance)
# ax.invert_xaxis()
# # ax.set_ylim(0, 0.20)
# plt.show()


config.background_color = "#212121"


class Presentation(BetterScene):
    def construct(self):
        logo_upsud = SVGMobject("img/Logo.svg").set_fill("#63003C", opacity=1)

        # move logo_upsud to top left corner
        logo_upsud.scale(0.5)
        logo_upsud.to_edge(UL)
        logo_upsud.shift(0.2*UP)

        theme = Text("Thème 2022: La science dans l'art", font_size=35, font="Karla").shift(UP)
        title = Text("SPECTROSCOPIE INFRAROUGE", font_size=35, font="Karla").next_to(theme, DOWN, buff=0.3)

        alek = Text("Alexandre MENARD", font_size=20, font="Karla")
        golem = Text("Florent VIEILLEDENT", font_size=20, font="Karla")
        nilo = Text("Nilo RANCHY", font_size=20, font="Karla")
        name = VGroup(alek, golem, nilo).arrange(DOWN, buff=0.1).next_to(title, DOWN, buff=0.3)

        self.add(logo_upsud)
        self.add(theme)
        self.add(name)
        self.wait(5.2)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(logo_upsud, theme, title, alek, golem, nilo))


class Citation(BetterScene):
    def construct(self):
        citation1 = Text("\"Envisager l'art sous l'angle de ses matériaux", font="Karla", font_size=25)
        citation2 = Text("amène à privilégier les pratiques plus que la", font="Karla", font_size=25)
        citation3 = Text("considération des oeuvres closes et fermées\"", font="Karla", font_size=25)
        group = VGroup(citation1, citation2, citation3).arrange(DOWN, buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER/2)

        author = Text("-Florence de Mèredieu", color="#18a5d4", font="Karla", font_size=20, weight=BOLD)
        author.next_to(group, ORIGIN, aligned_edge=RIGHT).shift(DOWN)

        self.wait(0.1)
        self.play(Write(group), run_time=6)
        self.wait(2.5)
        self.play(Write(author)) # 9.6s
        self.wait(4.4)

        global_circle = Circle(radius=2.2, color=BLUE_B)
        title = Text("Oeuvre", font="Karla").next_to(global_circle, DOWN)
        little_circle = Circle(radius=0.8, color=BLUE_D).set_fill(BLUE_D, opacity=0.5)
        little_circle_reductrice = VGroup(*[Text(txt, font_size=14, font="Karla") for txt in ["Connaissances", "sur", "l'oeuvre"]]).move_to(little_circle).arrange(DOWN, buff=0.1)

        self.play(FadeOut(group, author), Create(global_circle), Create(little_circle), Create(little_circle_reductrice), Create(title))

        self.wait(1)
        self.play(Indicate(little_circle), Indicate(little_circle_reductrice))
        self.play(little_circle.animate.scale(1.5), little_circle_reductrice.animate.scale(1.5))
        self.wait(1)
        self.play(FadeOut(little_circle_reductrice, little_circle, global_circle, title))

        waiting_logo = WaitingLogo()
        self.play(FadeIn(waiting_logo))
        for anim in waiting_logo.wait(5, 6.5):
            self.play(anim)

        self.play(FadeOut(waiting_logo))
        spectroscopie = Text("Spectroscopie infrarouge", font="Karla", font_size=25).to_edge(UP).shift(1.5 * DOWN)
        arrow1 = Arrow(start=spectroscopie.get_center() + 0.5 * DOWN, end = spectroscopie.get_center() + 1.5 * DOWN)
        intermediaire = Text("Analyser et décrire la matière", font="Karla", font_size=25).next_to(arrow1, DOWN)
        arrow2 = Arrow(start=intermediaire.get_center() + 0.5 * DOWN, end=intermediaire.get_center() + 1.5 * DOWN)

        pos = arrow2.get_corner(DOWN) + 0.5 * DOWN
        carbon = Atom(0.4, GRAY, pos)
        ox1 = Atom(0.4, RED, pos + 2 * LEFT)
        ox2 = Atom(0.4, RED, pos + 2 * RIGHT)
        bound1 = Bound(carbon, ox1, 2).set_z_index(-1)
        bound2 = Bound(carbon, ox2, 2).set_z_index(-1)

        self.wait(1.5)
        self.play(Create(spectroscopie))
        self.wait(2.5)
        self.play(Create(arrow1), Create(intermediaire))
        self.wait(0.5)
        self.play(Create(arrow2))
        self.add(bound1, bound2, carbon, ox1, ox2)
        self.play(ox1.animate.shift(0.5 * LEFT), ox2.animate.shift(0.5 * RIGHT), run_time=0.75)
        self.play(ox1.animate.shift(RIGHT), ox2.animate.shift(LEFT), run_time=0.75)
        self.play(ox1.animate.shift(LEFT), ox2.animate.shift(RIGHT), run_time=0.75)
        self.play(ox1.animate.shift(0.5 * RIGHT), ox2.animate.shift(0.5 * LEFT), run_time=0.75)
        self.play(FadeOut(carbon, ox1, ox2, bound1, bound2, arrow1, arrow2, spectroscopie, intermediaire), FadeIn(waiting_logo))

        for anim in waiting_logo.wait(2, 3):
            self.play(anim)

        self.play(FadeOut(waiting_logo))


class GlobalView(BetterScene):
    def construct(self):
        self.next_section()

        spectrometer = Rectangle(BLUE_D, height=1, width=2)
        work = Line(3 * RIGHT + 2 * UP, 3 * RIGHT + 2 * DOWN, stroke_width=5).shift(1 * RIGHT)

        def draw_spectro_title():
            return Text("Spectromètre", font_size=18, font="Karla").move_to(spectrometer)

        spectrometer_title = always_redraw(draw_spectro_title)
        self.animate(CreateSimultaneous(spectrometer, work, spectrometer_title))

        self.play(spectrometer.animate.shift(3 * LEFT).scale(2.5), work.animate.shift(2* RIGHT).scale(2))

        photon1_out = Photon(spectrometer.get_corner(RIGHT) + 1 * UP, work.get_corner(LEFT),amplitude=0.1, color=RED, width=5, frequency=10)
        photon2_out = Photon(spectrometer.get_corner(RIGHT) + 0.5 * UP, work.get_corner(LEFT),amplitude=0.1, color=RED, width=5, frequency=15)
        photon3_out = Photon(spectrometer.get_corner(RIGHT), work.get_corner(LEFT),amplitude=0.1, color=RED, width=5, frequency=20)
        photon4_out = Photon(spectrometer.get_corner(RIGHT) - 0.5 * UP, work.get_corner(LEFT),amplitude=0.1, color=RED, width=5, frequency=25)
        photon5_out = Photon(spectrometer.get_corner(RIGHT) - 1 * UP, work.get_corner(LEFT),amplitude=0.1, color=RED, width=5, frequency=30)

        self.animate(CreateSimultaneous(photon1_out, photon2_out, photon3_out, photon4_out, photon5_out))

        self.wait(3.5)
        self.play(Indicate(photon1_out, scale_factor=1), Indicate(photon2_out, scale_factor=1), Indicate(photon3_out, scale_factor=1), Indicate(photon4_out, scale_factor=1), Indicate(photon5_out, scale_factor=1))

        frequency = np.array([2, 8, 15])
        length = distance_between_points(spectrometer.get_corner(RIGHT), work.get_corner(LEFT) )
        photon_backward = FunctionGraph(lambda x: np.sum(np.cos(frequency * x))/(10), x_range=[-length, 0]).move_to(spectrometer.get_corner(RIGHT), aligned_edge=LEFT).rotate(PI).set_color(RED)

        self.wait(2)
        self.play(FadeOut(photon1_out, photon2_out, photon3_out, photon4_out, photon5_out))
        self.play(Create(photon_backward), run_time=5)
        self.play(Indicate(photon_backward, scale_factor=1))

        new_signal = FunctionGraph(lambda x: np.sum(np.cos(frequency * x)) / (5), x_range=[-4, 4]).set_color(RED)
        signal_title = Text("Signal capté", font="Karla", font_size=25).next_to(new_signal, UP).shift(UP)

        self.wait(3)
        self.play(FadeOut(spectrometer, spectrometer_title, work), Transform(photon_backward, new_signal, replace_mobject_with_target_in_scene=True), Create(signal_title))

        self.wait(8)
        arrow = Arrow(start=1.5 * UP, end=ORIGIN)
        transformee = Text("Transformée de Fourier", font="Karla", font_size=20).next_to(arrow, RIGHT)

        self.play(new_signal.animate.next_to(arrow, UP), FadeOut(signal_title), run_time=0.5)
        self.play(Create(arrow), Write(transformee), run_time=0.5)
        self.wait(2)
        self.play(Indicate(new_signal))

        signal1 = FunctionGraph(lambda x: np.cos(2 * x) / 4, x_range=[-4, 4]).set_color(RED).shift(0.5 * DOWN)
        signal2 = FunctionGraph(lambda x: np.cos(8 * x) / 4, x_range=[-4, 4]).set_color(RED).shift(1.5 * DOWN)
        signal3 = FunctionGraph(lambda x: np.cos(15 * x) / 4, x_range=[-4, 4]).set_color(RED).shift(2.5 * DOWN)
        signal_group = VGroup(signal1, signal2, signal3)

        self.play(Transform(new_signal.copy(), signal_group, replace_mobject_with_target_in_scene=True))
        self.wait(0.5)
        self.play(Indicate(signal_group))

        self.wait(4.5)

        # Graphing

        wavenumber = np.loadtxt("data/wavenumber.txt")
        absorbance = np.loadtxt("data/absorbance.txt")

        ax = Axes(
            x_range=[wavenumber[-1], wavenumber[0], 1000],
            x_length=7,
            y_length=5,
            y_range=[0, 0.45, 0.2],
            tips=True,
            axis_config={"include_numbers": True},
            y_axis_config={"scaling": LinearBase()},
        ).shift(0.2 * UP)

        nu = MathTex(r"\nu (cm^{-1})").scale(0.4)
        A = MathTex(r"Absorbance").scale(0.4)
        labels = ax.get_axis_labels(x_label=nu, y_label=A).set_color(WHITE)
        graph = ax.plot_line_graph(wavenumber, absorbance, add_vertex_dots=False, stroke_width=2).set_color(WHITE).flip(
            UP)

        # Inverts DecimalNumber on x-axis
        x_axis: NumberLine = ax.get_axis(0)
        value: list[NumberLine] = x_axis.submobjects[2].submobjects
        new_pos = []
        for i in range(len(value)):
            new_pos.append(value[i].get_center())
        new_pos = new_pos[::-1]

        for i, val in enumerate(value):
            val.move_to(new_pos[i])

        graph_group = VGroup(ax, labels)
        self.play(FadeOut(new_signal, arrow, transformee, signal_group), Create(graph_group), Transform(signal1, graph, replace_mobject_with_target_in_scene=True))
        self.wait(4)
        self.play(FadeOut(graph_group, graph))


class VibrationMode(BetterScene):
    def construct(self):
        self.wait(3)
        original_compounds = PbMolecule()

        x_list = [-4, -4, 0, 0]
        y_list = [2, -2] * 2

        compounds = []
        for x, y in zip(x_list, y_list):
            molecule = PbMolecule([x, y, 0]).scale(0.7)
            compounds.append(molecule)

        compounds.append(PbMoleculeSide([4, 2, 0]))
        compounds.append(PbMoleculeSide([4, -2, 0]))

        self.play(FadeIn(original_compounds))

        self.wait(4)

        self.play(Transform(VGroup(original_compounds), VGroup(*compounds)))
        self.clear()
        self.add(*compounds)

        anim0 = compounds[0].stretching(0.1, UL, UR, 6, 6)
        anim1 = compounds[1].stretching(0.1, UL, UR, 6, 6, False)
        anim2 = compounds[2].scissoring(PI / 16, 6, 6)
        anim3 = compounds[3].scissoring(PI / 16, 6, 6, False)
        anim4 = compounds[4].wagging(0.1 * LEFT, 6, 6)
        anim5 = compounds[5].wagging(0.1 * LEFT, 6, 6, False)

        for i, (a0, a1, a2, a3, a4, a5) in enumerate(zip_longest(anim0, anim1, anim2, anim3, anim4, anim5)):
            if i == 1:
                self.play(*[Indicate(comp.dipolar_moment, scale_factor=1) for comp in compounds])
                self.animate_unpack(a0, a1, a2, a3, a4, a5)
            elif i == 3:
                self.play(*a0, *a1, *a2, *a3, *a4, *a5, *[Flash(comp, flash_radius=1.5) for comp in compounds[0:-1]])
            elif i == 5:
                self.play(*a0, *a1, *a2, *a3, *a4, *a5, Flash(compounds[-1], flash_radius=1.5))
            else:
                self.animate_unpack(a0, a1, a2, a3, a4, a5)

        abs = Text("Actif dans l'IR", font_size=20, font="Karla")
        equivalent = MathTex(r"\Leftrightarrow")
        dipolaire = Text("Variation du moment dipolaire", font_size=20, font="Karla")
        group1 = VGroup(abs, equivalent, dipolaire).arrange(RIGHT)

        self.play(FadeOut(*compounds), Write(group1))
        self.wait(2)
        self.play(FadeOut(group1))
        self.wait()


class Ressort(BetterScene):
    def construct(self) -> None:
        self.next_section(skip_animations=False)
        ax = Axes(
            x_range=[0, 5, 1],
            x_length=7,
            y_length=7,
            y_range=[-1, 6, 1],
            tips=True,
            axis_config={"include_numbers": False},
            y_axis_config={"scaling": LinearBase()},
        ).set_z_index(-1).shift(0.4 * UP)

        a, re = 7, 2
        lead = Atom(0.5, BLUE, ax.coords_to_point(0, 0, 0))

        oxygen = Atom(0.1, RED, ax.coords_to_point(re, 0, 0))
        bound = Bound(lead, oxygen, 1).set_z_index(-1)
        ressort = always_redraw(lambda: Spring(lead, oxygen, 11, 0.3))

        labels = ax.get_axis_labels(x_label='r', y_label='E').set_color(WHITE).set_z_index(-1)
        graph = ax.plot(lambda x: a * (x - re) ** 2, x_range=[1.15, 2.85], use_smoothing=True).set_z_index(-1)
        ep = MathTex(r"E_p = \frac{1}{2} k {{r^2}}").next_to(graph, UR).shift(0.5 * DOWN)

        self.wait()
        self.play(FadeIn(lead), FadeIn(oxygen), Create(bound))
        self.wait()
        self.play(Transform(bound, ressort, replace_mobject_with_target_in_scene=True))
        self.wait(0.5)
        self.play(Create(ax), Create(labels), Create(graph), Write(ep))
        self.wait(0.5)
        self.play(Indicate(ep.submobjects[-1]))
        self.wait(3)
        self.play(lead.animate.move_to(ax.coords_to_point(0, 3, 0)), oxygen.animate.move_to(ax.coords_to_point(re, 3, 0)))
        self.play(lead.animate.move_to(ax.coords_to_point(0, 1, 0)), oxygen.animate.move_to(ax.coords_to_point(re, 1, 0)))
        # 11s
        self.wait(1)
        x2, x1 = self.get_solution(1, re, a)
        amplitude_arrow_1 = DoubleArrow(start=ax.coords_to_point(x1, 1.6, 0), end=ax.coords_to_point(x2, 1.6, 0), buff=0.1)
        self.next_section(skip_animations=True)
        self.play(oxygen.animate.move_to(ax.coords_to_point(x1, 1, 0)), Create(amplitude_arrow_1), run_time=0.5)
        self.play(oxygen.animate.move_to(ax.coords_to_point(x2, 1, 0)), run_time=0.5)
        self.play(oxygen.animate.move_to(ax.coords_to_point(x1, 1, 0)), run_time=0.5)
        self.play(oxygen.animate.move_to(ax.coords_to_point(x2, 1, 0)), run_time=0.5)

        x2, x1 = self.get_solution(3, re, a)
        amplitude_arrow_2 = DoubleArrow(start=ax.coords_to_point(x1, 3.6, 0), end=ax.coords_to_point(x2, 3.6, 0), buff=0.1)
        self.play(lead.animate.move_to(ax.coords_to_point(0, 3, 0)), oxygen.animate.move_to(ax.coords_to_point(re, 3, 0)), Transform(amplitude_arrow_1, amplitude_arrow_2, replace_mobject_with_target_in_scene=True), run_time=0.25)
        self.play(oxygen.animate.move_to(ax.coords_to_point(x1, 3, 0)), run_time=0.5)
        self.play(oxygen.animate.move_to(ax.coords_to_point(x2, 3, 0)), run_time=0.5)
        self.play(oxygen.animate.move_to(ax.coords_to_point(x1, 3, 0)), run_time=0.5)
        self.play(oxygen.animate.move_to(ax.coords_to_point(x2, 3, 0)), run_time=0.5)

        self.next_section(skip_animations=True)

        self.wait()

        schrod_eq = MathTex(r"i \hbar \frac{\partial}{\partial t}\Psi(\mathbf{r},t) = \hat H \Psi(\mathbf{r},t)").to_edge(UR).shift(3 * DOWN)
        self.play(Write(schrod_eq), FadeOut(ep), FadeOut(amplitude_arrow_2))
        self.wait(3.5)

        energy_levels = VGroup()
        tex_levels = []
        tex = [f"E_p = \\frac{{\\hbar \\omega}}{{2}}", f"E_p = \\hbar \\omega", f"E_p = 3 \\frac{{\\hbar \\omega}}{{2}}", f"E_p =  2 \\hbar \\omega"]
        for E in range(1, 5):
            x1, x2 = self.get_solution(E, re, a)

            point1 = ax.coords_to_point(*[x1, E, 0])
            point2 = ax.coords_to_point(*[x2, E, 0])

            level_tex = MathTex(tex[E - 1]).scale(0.7).next_to(point2, RIGHT)
            tex_levels.append(level_tex)

            energy_levels.add(Line(point1, point2), level_tex)

        energy_levels.set_z_index(-1)
        self.play(Transform(schrod_eq, energy_levels, replace_mobject_with_target_in_scene=True))
        self.play(*[Indicate(obj) for obj in tex_levels])
        self.wait(2.5)
        self.play(FadeOut(lead, oxygen, ressort))

        arrows = VGroup()
        for E in range(2, 5):
            line = Arrow(start=ax.coords_to_point(re + 0.2 * (E - 3), 1, 0), end=ax.coords_to_point(re + 0.2 * (E - 3), E, 0), stroke_width=6, max_tip_length_to_length_ratio=0.25 / (E - 1))
            line.put_start_and_end_on(start=ax.coords_to_point(re + 0.2 * (E - 3), 1, 0), end=ax.coords_to_point(re + 0.2 * (E - 3), E, 0))
            arrows.add(line)

        self.play(Create(arrows))

        self.wait(5)
        self.play(FadeOut(arrows), FadeOut(*tex_levels))

        arrow_1_to_2 = Arrow(start=ax.coords_to_point(re, 1, 0), end=ax.coords_to_point(re, 2, 0), stroke_width=6, max_tip_length_to_length_ratio=0.25, buff=0.1)
        self.play(Create(arrow_1_to_2))

        brace_1_to_2 = BraceBetweenPoints(point_1=energy_levels.submobjects[1].get_corner(LEFT), point_2=energy_levels.submobjects[1].get_corner(LEFT) + 0.8 * UP)
        deltaE = MathTex(r"\Delta E = \frac{\hbar \omega}{2}").next_to(brace_1_to_2, RIGHT, buff=0).scale(0.7).shift(0.2 * LEFT)

        self.wait(2)

        self.play(Create(brace_1_to_2), Write(deltaE))
        self.wait()

        new_arrow = Arrow(start=ax.coords_to_point(re, 1, 0), end=ax.coords_to_point(re, 3, 0), stroke_width=6,
                             max_tip_length_to_length_ratio=0.25, buff=0.1)

        new_brace = BraceBetweenPoints(point_1=energy_levels.submobjects[1].get_corner(LEFT),
                                          point_2=energy_levels.submobjects[1].get_corner(LEFT) + 1.7 * UP).shift(0.2 * RIGHT)
        new_delta = MathTex(r"\Delta E = \hbar \omega").next_to(new_brace, RIGHT, buff=0).scale(
            0.7).shift(0.2 * LEFT)
        self.play(Transform(arrow_1_to_2, new_arrow), Transform(brace_1_to_2, new_brace), Transform(deltaE, new_delta))
        self.wait(2)
        self.play(FadeOut(*self.mobjects))
        self.wait(2)

    def get_solution(self, E, re, a):
        x2 = (2 * re + np.sqrt(4 * E / a)) / 2
        x1 = (2 * re - np.sqrt(4 * E / a)) / 2
        return x1, x2


class Conclusion(BetterScene):
    def construct(self):
        self.next_section(skip_animations=False)

        img = ImageMobject("L'ultimo_bacio_di_Giulietta_e_Romeo.jpg").scale_to_fit_height(4.6)
        title = Text("Francesco Hayez, L'ultimo bacio dato a Giulietta da Romeo, 1823", font="Karla",
                     font_size=18).next_to(img, DOWN)

        self.wait()
        self.play(FadeIn(img), Write(title))
        self.wait(2)

        wavenumber = np.loadtxt("data/wavenumber.txt")
        absorbance = np.loadtxt("data/absorbance.txt")

        ax = Axes(
            x_range=[wavenumber[-1], wavenumber[0], 1000],
            x_length=8,
            y_length=5,
            y_range=[0, 0.45, 0.2],
            tips=True,
            axis_config={"include_numbers": True},
            y_axis_config={"scaling": LinearBase()},
        ).shift(0.5 * UP)

        nu = MathTex(r"\nu (cm^{-1})").scale(0.4)
        A = MathTex(r"Absorbance").scale(0.4)
        labels = ax.get_axis_labels(x_label=nu, y_label=A).set_color(WHITE)
        graph = ax.plot_line_graph(wavenumber, absorbance, add_vertex_dots=False, stroke_width=2).set_color(WHITE).flip(
            UP)

        # Inverts DecimalNumber on x-axis
        x_axis: NumberLine = ax.get_axis(0)
        value: list[NumberLine] = x_axis.submobjects[2].submobjects
        new_pos = []
        for i in range(len(value)):
            new_pos.append(value[i].get_center())
        new_pos = new_pos[::-1]

        for i, val in enumerate(value):
            val.move_to(new_pos[i])

        graph_group = VGroup(ax, labels)

        self.play(FadeOut(img), Unwrite(title), run_time=0.75)
        self.play(Create(graph_group), Create(graph))

        self.wait(1)

        def get_real_pos(nu):
            return - nu + 5500

        ceton_ch2_pos = ax.coords_to_point(get_real_pos(4760), 0.04)
        linseed_pos = ax.coords_to_point(get_real_pos(4330), 0.12)
        ceton_pos = ax.coords_to_point(get_real_pos(1790), 0.45)

        circ1 = Circle(0.3, BLUE_D).move_to(ceton_ch2_pos)
        circ2 = Circle(0.3, BLUE_D).move_to(linseed_pos)
        circ3 = Circle(0.3, BLUE_D).move_to(ceton_pos)

        line_ceton_ch2 = Arrow(end=circ1.get_corner(UP), start=circ1.get_corner(UP) + 0.7 * UP, buff=0.2)
        line_ceton = Arrow(end=circ3.get_corner(RIGHT), start=circ3.get_corner(RIGHT) + RIGHT, buff=0.2)
        line_linseed = Arrow(end=circ2.get_corner(UP), start=circ2.get_corner(UP) + UP, buff=0.2)

        ceton1 = ChemObject("C=O")
        ch2 = ChemObject("CH_2")
        add = MathTex("+")
        ceton_ch2 = VGroup(ceton1, add, ch2).arrange(DOWN).scale(0.5).next_to(line_ceton_ch2, UP)
        ceton2 = ceton1.copy().next_to(line_ceton, RIGHT)
        linseed = Text("Huile  de  lin", font="Karla", font_size=17).next_to(line_linseed, UP)


        self.animate(CreateSimultaneous(circ1, circ3, line_ceton_ch2, line_ceton, ceton_ch2, ceton2))
        self.wait()
        self.animate(CreateSimultaneous(line_linseed, linseed, circ2))
        self.wait()

        molecule = ChemWithName(
            """CH_3-[1]-[2]=[3]-[5]-[3]=[5]-[6]-[5]=[6]-[7]-[6]-[7]-[6]-[7]-[1]-[2]-[1](=[7]O)-[2]O-[1]-[7](-[6]-[7]O-[6](=[5]O)-[7]-[6]-[7]-[1]-[7]-[1]-[7]-[1]=[2]-[3]-[2]=[1]-[7]-[6]-[7]-[6]-[7]CH_3)-[1]O-[7](=[6]O)-[1]-[7]-[1]-[7]-[1]-[7]-[1]-[2]=[3]-[5]-[3]-[5]-[3]-[5]-[3]-[2]-[1]CH_3""",
            "Huile de lin").scale_to_fit_height(5)

        self.play(FadeOut(ax, labels, circ1, circ2, circ3, line_ceton_ch2, line_ceton, ceton_ch2, ceton2,line_linseed, linseed, graph), molecule.creation_anim())
        self.wait()
        self.play(FadeOut(molecule))
        self.wait()

        self.next_section()

        img = ImageMobject("img.png")
        title = Text("Francesco Hayez, L'ultimo bacio dato a Giulietta da Romeo, 1823", font="Karla",
                     font_size=18).next_to(img, DOWN)
        self.play(FadeIn(img), Write(title))

        self.wait()

        menton = Circle(0.3, BLUE_D).move_to(2.4 * RIGHT+ 0.15 * UP)
        cou = Ellipse(width=0.4, height=1.1, stroke_color=BLUE_D).move_to(2.8 * RIGHT + 1.1 * DOWN).rotate(PI/20).shift(0.05 * RIGHT)

        self.play(Create(menton), Create(cou))
        self.wait()
        self.play(FadeOut(menton, cou, title, img))
        self.wait()

        waiting = WaitingLogo()
        self.play(FadeIn(waiting))

        for anim in waiting.wait(2, 2):
            self.play(anim)

        self.wait()
        self.play(FadeOut(waiting))
        self.wait()

class Oui(BetterScene):
    def construct(self):
        waiting = WaitingLogo()
        self.play(FadeIn(waiting))

        for anim in waiting.wait(2, 3):
            self.play(anim)

        self.wait()
        self.play(FadeOut(waiting))
        self.wait()

class Oui2(BetterScene):
    def construct(self):
        wavenumber = np.loadtxt("data/wavenumber.txt")
        absorbance = np.loadtxt("data/absorbance.txt")

        ax = Axes(
            x_range=[wavenumber[-1], wavenumber[0], 1000],
            x_length=8,
            y_length=5,
            y_range=[0, 0.45, 0.2],
            tips=True,
            axis_config={"include_numbers": True},
            y_axis_config={"scaling": LinearBase()},
        ).shift(0.5 * UP)

        nu = MathTex(r"\nu (cm^{-1})").scale(0.4)
        A = MathTex(r"Absorbance").scale(0.4)
        labels = ax.get_axis_labels(x_label=nu, y_label=A).set_color(WHITE)
        graph = ax.plot_line_graph(wavenumber, absorbance, add_vertex_dots=False, stroke_width=2).set_color(WHITE).flip(
            UP)

        # Inverts DecimalNumber on x-axis
        x_axis: NumberLine = ax.get_axis(0)
        value: list[NumberLine] = x_axis.submobjects[2].submobjects
        new_pos = []
        for i in range(len(value)):
            new_pos.append(value[i].get_center())
        new_pos = new_pos[::-1]

        for i, val in enumerate(value):
            val.move_to(new_pos[i])

        graph_group = VGroup(ax, labels)

        self.play(FadeOut(img), Unwrite(title), run_time=0.75)
        self.play(Create(graph_group), Create(graph))

        self.wait(1)

        def get_real_pos(nu):
            return - nu + 5500

        ceton_ch2_pos = ax.coords_to_point(get_real_pos(4760), 0.04)
        linseed_pos = ax.coords_to_point(get_real_pos(4330), 0.12)
        ceton_pos = ax.coords_to_point(get_real_pos(1790), 0.45)

        circ1 = Circle(0.3, BLUE_D).move_to(ceton_ch2_pos)
        circ2 = Circle(0.3, BLUE_D).move_to(linseed_pos)
        circ3 = Circle(0.3, BLUE_D).move_to(ceton_pos)

        line_ceton_ch2 = Arrow(end=circ1.get_corner(UP), start=circ1.get_corner(UP) + 0.7 * UP, buff=0.2)
        line_ceton = Arrow(end=circ3.get_corner(RIGHT), start=circ3.get_corner(RIGHT) + RIGHT, buff=0.2)
        line_linseed = Arrow(end=circ2.get_corner(UP), start=circ2.get_corner(UP) + UP, buff=0.2)

        ceton1 = ChemObject("C=O")
        ch2 = ChemObject("CH_2")
        add = MathTex("+")
        ceton_ch2 = VGroup(ceton1, add, ch2).arrange(DOWN).scale(0.5).next_to(line_ceton_ch2, UP)
        ceton2 = ceton1.copy().next_to(line_ceton, RIGHT)
        linseed = Text("Huile  de  lin", font="Karla", font_size=17).next_to(line_linseed, UP)

        self.animate(CreateSimultaneous(circ1, circ3, line_ceton_ch2, line_ceton, ceton_ch2, ceton2))
        self.wait()
        self.animate(CreateSimultaneous(line_linseed, linseed, circ2))
        self.wait()

        molecule = ChemWithName(
            """CH_3-[1]-[2]=[3]-[5]-[3]=[5]-[6]-[5]=[6]-[7]-[6]-[7]-[6]-[7]-[1]-[2]-[1](=[7]O)-[2]O-[1]-[7](-[6]-[7]O-[6](=[5]O)-[7]-[6]-[7]-[1]-[7]-[1]-[7]-[1]=[2]-[3]-[2]=[1]-[7]-[6]-[7]-[6]-[7]CH_3)-[1]O-[7](=[6]O)-[1]-[7]-[1]-[7]-[1]-[7]-[1]-[2]=[3]-[5]-[3]-[5]-[3]-[5]-[3]-[2]-[1]CH_3""",
            "Huile de lin").scale_to_fit_height(5)

        self.play(FadeOut(ax, labels, circ1, circ2, circ3, line_ceton_ch2, line_ceton, ceton_ch2, ceton2, line_linseed,
                          linseed, graph), molecule.creation_anim())
        self.wait()
        self.play(FadeOut(molecule))
        self.wait()

img = ImageMobject("img.png")
title = Text("Francesco Hayez, L'ultimo bacio dato a Giulietta da Romeo, 1823", font="Karla", font_size=18).next_to(img, DOWN)
#title = Text("Francesco Hayez, L'ultimo bacio dato a Giulietta da Romeo, 1823", font="Karla", font_size=18).next_to(img, DOWN)
dot = Dot(0.15 * UP + 2.35 * RIGHT)


molecule = ChemWithName("""CH_3-[1]-[2]=[3]-[5]-[3]=[5]-[6]-[5]=[6]-[7]-[6]-[7]-[6]-[7]-[1]-[2]-[1](=[7]O)-[2]O-[1]-[7](-[6]-[7]O-[6](=[5]O)-[7]-[6]-[7]-[1]-[7]-[1]-[7]-[1]=[2]-[3]-[2]=[1]-[7]-[6]-[7]-[6]-[7]CH_3)-[1]O-[7](=[6]O)-[1]-[7]-[1]-[7]-[1]-[7]-[1]-[2]=[3]-[5]-[3]-[5]-[3]-[5]-[3]-[2]-[1]CH_3""", "Huile de lin")
molecule.scale_to_fit_height(6)
