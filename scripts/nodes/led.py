from KicadModTree.nodes.Node import Node
from KicadModTree.nodes.base import Pad, Text


class Led(Node):

  def __init__(self, pad_offset: int = 4):
    Node.__init__(self)

    # create pads
    self.append(
        Pad(
            number=pad_offset + 1,
            type=Pad.TYPE_THT,
            shape=Pad.SHAPE_RECT,
            at=[1.27, 5.08],
            size=1.905,
            drill=1,
            layers=["*.Cu", "B.Mask"],
        ))
    self.append(
        Pad(
            number=pad_offset + 2,
            type=Pad.TYPE_THT,
            shape=Pad.SHAPE_CIRCLE,
            at=[-1.27, 5.08],
            size=1.905,
            drill=1,
            layers=["*.Cu", "B.Mask"],
        ))

    # create silkscreen text
    self.append(Text(type="user", text="-", at=[1.27, 3.5], layer="F.SilkS"))
    self.append(Text(type="user", text="-", at=[1.27, 3.5], layer="B.SilkS"))
    self.append(Text(type="user", text="+", at=[-1.27, 3.5], layer="F.SilkS"))
    self.append(Text(type="user", text="+", at=[-1.27, 3.5], layer="B.SilkS"))
