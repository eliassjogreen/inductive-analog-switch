# Borrowed code from https://github.com/perigoso/keyswitch-kicad-library
# by perigoso and contributors originally licensed under CC BY SA 4.0

from KicadModTree.nodes.Node import Node
from KicadModTree.nodes.base import Pad
from KicadModTree.nodes.specialized import RectLine, PolygoneLine

from nodes.util import offset_polyline


class Switch(Node):
    def __init__(self, switch_name: str):
        Node.__init__(self)
        self.switch_name = switch_name


class SwitchCherryMX(Switch):

    cherry_width = 14
    cherry_height = 14

    def __init__(self, switch_type: str, pad_offset: int = 0):
        Switch.__init__(self, "Cherry MX " + switch_type)

        # create fab outline
        self.append(
            RectLine(
                start=[-self.cherry_width / 2, -self.cherry_height / 2],
                end=[self.cherry_width / 2, self.cherry_height / 2],
                layer="F.Fab",
                cherry_width=0.1,
            )
        )

        # create silkscreen
        self.append(
            RectLine(
                start=[-self.cherry_width / 2, -self.cherry_height / 2],
                end=[self.cherry_width / 2, self.cherry_height / 2],
                layer="F.SilkS",
                cherry_width=0.12,
                offset=0.1,
            )
        )

        # create courtyard
        self.append(
            RectLine(
                start=[-self.cherry_width / 2, -self.cherry_height / 2],
                end=[self.cherry_width / 2, self.cherry_height / 2],
                layer="F.CrtYd",
                cherry_width=0.05,
                offset=0.25,
            )
        )

        # create pads
        self.append(
            Pad(
                number=pad_offset + 1,
                type=Pad.TYPE_THT,
                shape=Pad.SHAPE_CIRCLE,
                at=[-3.81, -2.54],
                size=[2.5, 2.5],
                drill=1.5,
                layers=["*.Cu", "B.Mask"],
            )
        )
        self.append(
            Pad(
                number=pad_offset + 2,
                type=Pad.TYPE_THT,
                shape=Pad.SHAPE_CIRCLE,
                at=[2.54, -5.08],
                size=[2.5, 2.5],
                drill=1.5,
                layers=["*.Cu", "B.Mask"],
            )
        )
        self.append(
            Pad(
                type=Pad.TYPE_NPTH,
                shape=Pad.SHAPE_CIRCLE,
                at=[0, 0],
                size=[4, 4],
                drill=4,
                layers=["*.Cu", "*.Mask"],
            )
        )

        if switch_type == "PCB":
            self.append(
                Pad(
                    type=Pad.TYPE_NPTH,
                    shape=Pad.SHAPE_CIRCLE,
                    at=[-5.08, 0],
                    size=[1.75, 1.75],
                    drill=1.75,
                    layers=["*.Cu", "*.Mask"],
                )
            )
            self.append(
                Pad(
                    type=Pad.TYPE_NPTH,
                    shape=Pad.SHAPE_CIRCLE,
                    at=[5.08, 0],
                    size=[1.75, 1.75],
                    drill=1.75,
                    layers=["*.Cu", "*.Mask"],
                )
            )


class SwitchAlpsMatias(Switch):
    def __init__(self, pad_offset: int = 0):
        Switch.__init__(self, "Alps Matias")

        # create fab outline
        self.append(
            RectLine(start=[-7.75, -6.4], end=[7.75, 6.4], layer="F.Fab", width=0.1)
        )

        # create silkscreen
        self.append(
            RectLine(
                start=[-7.75, -6.4],
                end=[7.75, 6.4],
                layer="F.SilkS",
                width=0.12,
                offset=0.1,
            )
        )

        # create courtyard
        self.append(
            RectLine(
                start=[-7.75, -6.4],
                end=[7.75, 6.4],
                layer="F.CrtYd",
                width=0.05,
                offset=0.25,
            )
        )

        # create pads
        self.append(
            Pad(
                number=pad_offset + 1,
                type=Pad.TYPE_THT,
                shape=Pad.SHAPE_CIRCLE,
                at=[-2.5, -4],
                size=[2.5, 2.5],
                drill=1.5,
                layers=["*.Cu", "B.Mask"],
            )
        )
        self.append(
            Pad(
                number=pad_offset + 2,
                type=Pad.TYPE_THT,
                shape=Pad.SHAPE_CIRCLE,
                at=[2.5, -4.5],
                size=[2.5, 2.5],
                drill=1.5,
                layers=["*.Cu", "B.Mask"],
            )
        )


class SwitchCherryMXAlpsMatias(Switch):

    cherry_width = 14
    cherry_height = 14
    alps_matias_width = 14
    alps_matias_height = 14

    def __init__(self, switch_type: str, pad_offset: int = 0):
        Switch.__init__(self, "Cherry MX Alps Matias " + switch_type)

        base_polyline = [
            [-self.cherry_width / 2, -self.cherry_height / 2],
            [self.cherry_width / 2, -self.cherry_height / 2],
            [self.cherry_width / 2, -self.alps_matias_height / 2],
            [self.alps_matias_width / 2, -self.alps_matias_height / 2],
            [self.alps_matias_width / 2, self.alps_matias_height / 2],
            [self.cherry_width / 2, self.alps_matias_height / 2],
            [self.cherry_width / 2, self.cherry_height / 2],
            [-self.cherry_width / 2, self.cherry_height / 2],
            [-self.cherry_width / 2, self.alps_matias_height / 2],
            [-self.alps_matias_width / 2, self.alps_matias_height / 2],
            [-self.alps_matias_width / 2, -self.alps_matias_height / 2],
            [-self.cherry_width / 2, -self.alps_matias_height / 2],
            [-self.cherry_width / 2, -self.cherry_height / 2],
        ]

        # create fab outline
        self.append(PolygoneLine(polygone=base_polyline, layer="F.Fab", width=0.1))

        # create silkscreen outline
        polyline = offset_polyline(base_polyline, 0.1)
        self.append(PolygoneLine(polygone=polyline, layer="F.SilkS", width=0.12))

        # create courtyard outline
        polyline = offset_polyline(base_polyline, 0.25)
        self.append(PolygoneLine(polygone=polyline, layer="F.CrtYd", width=0.05))

        # create pads
        self.append(
            Pad(
                number=pad_offset + 1,
                type=Pad.TYPE_THT,
                shape=Pad.SHAPE_CIRCLE,
                at=[-2.5, -4],
                size=[2.5, 2.5],
                drill=1.5,
                layers=["*.Cu", "B.Mask"],
            )
        )
        self.append(
            Pad(
                number=pad_offset + 1,
                type=Pad.TYPE_THT,
                shape=Pad.SHAPE_OVAL,
                at=[-3.81, -2.54],
                size=[4.46156, 2.5],
                rotation=48,
                offset=[0.980778, 0],
                drill=1.5,
                layers=["*.Cu", "B.Mask"],
            )
        )
        self.append(
            Pad(
                number=pad_offset + 2,
                type=Pad.TYPE_THT,
                shape=Pad.SHAPE_OVAL,
                at=[2.52, -4.79],
                size=[3.081378, 2.5],
                drill=[2.08137, 1.5],
                rotation=86,
                layers=["*.Cu", "B.Mask"],
            )
        )
        self.append(
            Pad(
                type=Pad.TYPE_NPTH,
                shape=Pad.SHAPE_CIRCLE,
                at=[0, 0],
                size=[4, 4],
                drill=4,
                layers=["*.Cu", "*.Mask"],
            )
        )

        if switch_type == "PCB":
            self.append(
                Pad(
                    type=Pad.TYPE_NPTH,
                    shape=Pad.SHAPE_CIRCLE,
                    at=[-5.08, 0],
                    size=[1.75, 1.75],
                    drill=1.75,
                    layers=["*.Cu", "*.Mask"],
                )
            )
            self.append(
                Pad(
                    type=Pad.TYPE_NPTH,
                    shape=Pad.SHAPE_CIRCLE,
                    at=[5.08, 0],
                    size=[1.75, 1.75],
                    drill=1.75,
                    layers=["*.Cu", "*.Mask"],
                )
            )
