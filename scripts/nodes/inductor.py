from math import cos, pi, sin
from typing import List, Tuple

from KicadModTree.nodes.Node import Node
from KicadModTree.nodes.base import Pad, Line

from nodes.util import frange


class Inductor(Node):
    def __init__(
        self,
        inner_diameter: float,
        windings: int,
        rotation: float = pi / 2,
        center: Tuple[float, float] = (0, 0),
        trace_width: float = 0.2,
        trace_space: float = 0.15,
        drill_size: float = 0.3,
        pad_size: float = 0.15,
        pad_offset: int = 2,
        pad_angle: float = pi / 4,
        segments: float = 50,
    ):
        Node.__init__(self)

        pitch = trace_width + trace_space
        resolution = pi * 2 / segments
        increase = pitch / segments
        pad_wire = drill_size + pitch

        radius = inner_diameter / 2

        front: List[Tuple[float, float]] = []
        back: List[Tuple[float, float]] = []

        # generate the points for the front windings
        for angle in frange(0, windings * 2 * pi, resolution):
            radius += increase
            front.append(
                (
                    cos(angle + rotation) * radius + center[0],
                    sin(angle + rotation) * radius + center[1],
                )
            )

        # generate the points for the back windings
        for angle in frange(0, windings * 2 * pi, resolution):
            radius -= increase
            back.append(
                (
                    cos(angle + rotation) * radius + center[0],
                    sin(angle + rotation) * radius + center[1],
                )
            )

        # generate a via as an unnamed through-hole pad which connects the two layers in the middle
        self.append(
            Pad(
                type=Pad.TYPE_THT,
                shape=Pad.SHAPE_CIRCLE,
                layers=["F.Cu", "B.Cu"],
                at=front[0],
                size=pad_size + drill_size,
                drill=drill_size,
            )
        )

        # generate connecting wires
        front.append(
            (
                cos(rotation + pad_angle) * pad_wire + front[-1][0],
                sin(rotation + pad_angle) * pad_wire + front[-1][1],
            )
        )
        back.insert(
            0,
            (
                cos(rotation - pad_angle) * pad_wire + back[0][0],
                sin(rotation - pad_angle) * pad_wire + back[0][1],
            ),
        )

        # generate pads
        self.append(
            Pad(
                number=pad_offset + 1,
                type=Pad.TYPE_THT,
                shape=Pad.SHAPE_CIRCLE,
                layers=["F.Cu", "B.Cu"],
                at=front[-1],
                size=pad_size + drill_size,
                drill=drill_size,
            )
        )
        self.append(
            Pad(
                number=pad_offset + 2,
                type=Pad.TYPE_THT,
                shape=Pad.SHAPE_CIRCLE,
                layers=["B.Cu", "F.Cu"],
                at=back[0],
                size=pad_size + drill_size,
                drill=drill_size,
            )
        )

        # create the lines for the front windings
        for index in range(1, len(front)):
            start = front[index - 1]
            end = front[index]
            self.append(Line(start=start, end=end, layer="F.Cu", width=trace_width))

        # create the lines for the back windings
        for index in range(1, len(back)):
            start = back[index - 1]
            end = back[index]
            self.append(Line(start=start, end=end, layer="B.Cu", width=trace_width))
