from ManimR import *
from object import *

class PbMolecule(VGroup):
    def __init__(self, position = ORIGIN):
        super().__init__()

        self.lead = Atom(0.5, YELLOW_D, 0.5 * DOWN)
        self.oxygen1 = Atom(0.4, RED, 0.5 * UP + LEFT)
        self.oxygen2 = Atom(0.4, RED, 0.5 * UP + RIGHT)
        self.h1 = Atom(0.2, WHITE, self.oxygen1.get_center() + 0.3 * UL)
        self.h2 = Atom(0.2, WHITE, self.oxygen2.get_center() + 0.3 * UR)

        self.alcool1 = VGroup(self.h1, self.oxygen1)
        self.alcool2 = VGroup(self.h2, self.oxygen2)

        self.bound_lead_ox1 = Bound(self.lead, self.oxygen1, 1)
        self.bound_lead_ox2 = Bound(self.lead, self.oxygen2, 1)

        self.dipolar_width = 1.5
        self.dipolar_moment = always_redraw(self.dipolar_redraw)

        self.add(self.bound_lead_ox1, self.bound_lead_ox2, self.alcool1, self.alcool2, self.lead, self.dipolar_moment)
        self.move_to(position)

    def dipolar_redraw(self):
        lead_pos = self.lead.get_center()
        positive_center = lead_pos
        negative_center = (self.alcool1.get_center() - lead_pos) + (self.alcool2.get_center() - lead_pos) + lead_pos

        arrow = Arrow(start=negative_center, end=positive_center, stroke_width=self.dipolar_width, buff=0.53, tip_length=0.2,
                      max_tip_length_to_length_ratio=0.5)
        mu = MathTex("\\vec{\\mu}").next_to(arrow, UP).scale(0.8)

        return VGroup(arrow, mu)

    def stretching(self, amplitude, delta1, delta2, count, run_time = 1, symetric = True):
        obj1_pos_i = self.alcool1.get_center()
        obj2_pos_i = self.alcool2.get_center()

        obj1_x1 = obj1_pos_i + amplitude * delta1
        obj1_x2 = obj1_pos_i - amplitude * delta1
        obj2_x1 = obj2_pos_i + amplitude * (delta2 if symetric else -delta2)
        obj2_x2 = obj2_pos_i - amplitude * (delta2 if symetric else -delta2)

        for i in range(count):
            pos1 = obj1_x1 if i % 2 == 0 else obj1_x2
            pos2 = obj2_x1 if i % 2 == 0 else obj2_x2
            anim1 = self.alcool1.animate(run_time=run_time/(count + 1)).move_to(pos1)
            anim2 = self.alcool2.animate(run_time=run_time/(count + 1)).move_to(pos2)
            yield anim1, anim2

        anim1 = self.alcool1.animate(run_time=run_time/(count + 1)).move_to(obj1_pos_i)
        anim2 = self.alcool2.animate(run_time=run_time / (count + 1)).move_to(obj2_pos_i)
        yield anim1, anim2

    def scissoring(self, amplitude, count, run_time = 1, symetric = True):
        run_time /= count + (0 if count % 2 == 0 else 1)

        for i in range(count):
            angle1 = amplitude if i % 2 == 0 else -amplitude
            angle2 = -amplitude if i % 2 == 0 else amplitude
            angle2 *= 1 if symetric else -1 # anti_symetric angle

            if i != 0 and not symetric:
                angle1 *= 2
                angle2 *= 2

            anim1 = self.alcool1.animate(run_time=run_time).rotate(angle=angle1, about_point=self.lead.get_center())
            anim2 = self.alcool2.animate(run_time=run_time).rotate(angle=angle2, about_point=self.lead.get_center())
            yield anim1, anim2

        if count % 2 != 0 and symetric:
            angle1 = -amplitude
            angle2 = amplitude if symetric else -amplitude
            anim1 = self.alcool1.animate(run_time=run_time).rotate(angle=angle1, about_point=self.lead.get_center())
            anim2 = self.alcool2.animate(run_time=run_time).rotate(angle=angle2, about_point=self.lead.get_center())
            yield anim1, anim2
        if not symetric:
            angle1 = amplitude * (1 if count % 2 == 0 else -1)
            angle2 = amplitude * (1 if count % 2 == 0 else -1)

            anim1 = self.alcool1.animate(run_time=run_time).rotate(angle=angle1, about_point=self.lead.get_center())
            anim2 = self.alcool2.animate(run_time=run_time).rotate(angle=angle2, about_point=self.lead.get_center())
            yield anim1, anim2

class PbMoleculeSide(VGroup):
    def __init__(self, position = ORIGIN):
        super().__init__()

        self.lead = Atom(0.5, YELLOW_D, 0.5 * DOWN)
        self.oxygen1 = Atom(0.2, RED, 0.5 * UP)
        self.h1 = Atom(0.1, WHITE, self.oxygen1.get_center() + 0.1 * UP)
        self.oxygen2 = Atom(0.4, RED, 0.5 * UP + OUT)
        self.h2 = Atom(0.2, WHITE, self.oxygen2.get_center() + 0.1 * UP)

        self.alcool1 = VGroup(self.h1, self.oxygen1)
        self.alcool2 = VGroup(self.h2, self.oxygen2)

        self.bound_lead_ox1 = Bound(self.lead, self.oxygen1, 1)
        self.bound_lead_ox2 = Bound(self.lead, self.oxygen2, 1)

        self.dipolar_width = 1.5
        self.dipolar_moment = always_redraw(self.dipolar_redraw)

        self.add(self.bound_lead_ox1, self.bound_lead_ox2, self.alcool1, self.alcool2, self.lead, self.dipolar_moment)
        self.move_to(position)

    def dipolar_redraw(self):
        lead_pos = self.lead.get_center()
        positive_center = lead_pos
        negative_center = (self.alcool1.get_center() - lead_pos) + (self.alcool2.get_center() - lead_pos) + lead_pos

        arrow = Arrow(start=negative_center + 0.2 * UP, end=positive_center, stroke_width=self.dipolar_width, buff=0.6, tip_length=0.2,
                      max_tip_length_to_length_ratio=0.5)
        mu = MathTex("\\vec{\\mu}").next_to(arrow, UP).scale(0.8)

        return VGroup(arrow, mu)

    def wagging(self, amplitude, count, run_time = 1, symetric = True):
        obj1_initial_pos = self.alcool1.get_center()
        obj2_initial_pos = self.alcool2.get_center()

        run_time /= (count + 1)
        obj1_x1 = self.alcool1.get_center() + amplitude
        obj1_x2 = self.alcool1.get_center() - amplitude

        obj2_x1 = self.alcool2.get_center() + (amplitude if symetric else -amplitude)
        obj2_x2 = self.alcool2.get_center() + (-amplitude if symetric else amplitude)

        for i in range(count):
            anim1 = self.alcool1.animate(run_time=run_time).move_to(obj1_x1 if i % 2 == 0 else obj1_x2)
            anim2 = self.alcool2.animate(run_time=run_time).move_to(obj2_x1 if i % 2 == 0 else obj2_x2)
            yield anim1, anim2

        anim1 = self.alcool1.animate(run_time=run_time).move_to(obj1_initial_pos)
        anim2 = self.alcool2.animate(run_time=run_time).move_to(obj2_initial_pos)
        yield anim1, anim2