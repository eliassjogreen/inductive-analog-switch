from KicadModTree.nodes.Footprint import Footprint
from KicadModTree.nodes.base import Text

from inductor import Inductor
from led import Led
from switch import Switch


class SwitchInductive(Footprint):

  def __init__(self,
               switch: Switch,
               inductor: Inductor,
               led: bool = False,
               text_offset: float = 8):
    Footprint.__init__(self, None)

    self.name = "SW_L_" + ("LED_" if led else "") + "Inductive_" + switch.switch_name.replace(
        " ", "_")
    self.description = switch.switch_name.capitalize(
    ) + " keyswitch with inductor" + (" and holes for an LED" if led else "")
    self.tags = switch.switch_name + " switch keyswitch keyboard inductive inductor" + (" LED" if led else "")

    self.append(switch)
    self.append(inductor)

    if led:
      self.append(Led())

    self.append(
        Text(type="reference",
             text="REF**",
             at=[0, -text_offset],
             layer="F.SilkS"))
    self.append(
        Text(type="value", text=self.name, at=[0, text_offset], layer="F.Fab"))
    self.append(Text(type="user", text="%R", at=[0, 0], layer="F.Fab"))
