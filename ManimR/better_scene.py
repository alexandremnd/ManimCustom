from __future__ import annotations
from manim import Scene, Animation, AnimationGroup, Mobject
from manim.mobject.mobject import _AnimationBuilder
from ManimR.animation import CustomAnimation

def replace(iterable, value_to_replace, new_value):
    if isinstance(iterable, list | tuple):
        replace(iterable, value_to_replace, new_value)
    else:
        for i in len(range(iterable)):
            if iterable[i] == value_to_replace:
                iterable[i] = new_value


class BetterScene(Scene):
    def __init__(self):
        super().__init__()

        # Used to track total time since the start
        self.current_time = 0

        def update_time(dt: float, obj=self) -> None:
            obj.current_time += dt

        self.add_updater(update_time)

    def animate(self, *animations) -> None:
        for anim in animations:
            if anim is None:
                continue
            if isinstance(anim, (Animation, AnimationGroup)):
                # Supports for basic manim behaviour with Animation
                self.play(anim)
            elif isinstance(anim, CustomAnimation):
                # Custom support for customised animation, allowing to create custom mobjects animation easily.
                anim.run_animation(self)
            elif isinstance(anim, _AnimationBuilder):
                # Supports for mobject.animate.action()
                self.play(anim.build())

    def animate_unpack(self, *animations) -> None:
        index_to_animate = []
        for i in range(len(animations)):
            if animations[i] is not None:
                index_to_animate.append(i)

        to_animate = []
        for index in index_to_animate:
            for elt in animations[index]:
                to_animate.append(elt)

        self.play(*to_animate)