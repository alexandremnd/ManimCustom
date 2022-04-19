from __future__ import annotations
from typing import TYPE_CHECKING, Any, TypeVar
from manim import Mobject, Create, Animation, AnimationGroup, Uncreate

DEFAULT_ANIMATION_RUN_TIME = 1

if TYPE_CHECKING:
    from ManimR.better_scene import BetterScene


class CustomAnimation(object):
    def run_animation(self, scene: BetterScene) -> None:
        pass


class Add(CustomAnimation):
    def __init__(self, *args: Mobject) -> None:
        self.obj: tuple[Mobject] = args

    def run_animation(self, scene: BetterScene) -> None:
        for obj in self.obj:
            scene.add(obj)


class CreateOneByOne(CustomAnimation):
    def __init__(self, *args: Mobject, run_time: float = DEFAULT_ANIMATION_RUN_TIME, run_time_per_object: bool = False) -> None:
        self.obj: tuple[Mobject] = args
        self.run_time: float = run_time
        self.run_time_per_object: bool = run_time_per_object

    def run_animation(self, scene: BetterScene) -> None:
        for obj in self.obj:
            # If given run_time is for every object, we split time between each objects.
            time = self.run_time if self.run_time_per_object else self.run_time / len(self.obj)
            scene.play(Create(obj), run_time=time)


class CreateSimultaneous(CustomAnimation):
    def __init__(self, *args: Mobject, run_time: float = DEFAULT_ANIMATION_RUN_TIME) -> None:
        self.obj: tuple[Mobject] = args
        self.run_time: float = run_time

    def run_animation(self, scene: BetterScene) -> None:
        anim: tuple[Create] = tuple([Create(obj) for obj in self.obj])

        scene.play(*anim, run_time=self.run_time)

class UncreateMultiple(CustomAnimation):
    def __init__(self, *args: Mobject, run_time: float = DEFAULT_ANIMATION_RUN_TIME) -> None:
        self.obj: tuple[Mobject] = args
        self.run_time: float = run_time

    def run_animation(self, scene: BetterScene) -> None:
        anim: tuple[Uncreate] = tuple([Uncreate(obj) for obj in self.obj])

        scene.play(*anim, run_time=self.run_time)


class AnimationPacker(CustomAnimation):
    def __init__(self, *args: CustomAnimation | Animation, run_time: float = DEFAULT_ANIMATION_RUN_TIME) -> None:
        self.animations: tuple[CustomAnimation] = args
        self.run_time = run_time

    def run_animation(self, scene: BetterScene) -> None:
        for anim in self.animations:
            if isinstance(anim, (Animation, AnimationGroup)):
                scene.play(anim)
            elif isinstance(anim, CustomAnimation):
                anim.run_animation(scene)
