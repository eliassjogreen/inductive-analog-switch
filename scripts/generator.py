from math import pi
import os

from KicadModTree.KicadFileHandler import KicadFileHandler

from inductor import Inductor
from switch import SwitchAlpsMatias, SwitchCherryMX, SwitchCherryMXAlpsMatias
from switch_inductive import SwitchInductive

if __name__ == "__main__":
  output_directory = "footprints/Button_Switch_Keyboard_Inductive.pretty"
  switches = []
  
  if not os.path.isdir(output_directory):
    os.mkdir(output_directory)

  for led in [True, False]:
    for switch_type in ["PCB", "Plate"]:
      switches.append(
          SwitchInductive(SwitchCherryMX(switch_type=switch_type),
                          Inductor(4.5, 3, pi / 4 if led else pi / 2, (0.1, 0.1)), led))
      switches.append(
          SwitchInductive(SwitchCherryMXAlpsMatias(switch_type=switch_type),
                          Inductor(4.5, 3, pi / 4 if led else pi / 2, (0.1, 0.1)), led))

  switches.append(
      SwitchInductive(SwitchAlpsMatias(), Inductor(4.5, 3, pi / 2)))

  for switch in switches:
    file_handler = KicadFileHandler(switch)
    file_handler.writeFile(
        os.path.join(output_directory, f"{switch.name}.kicad_mod"))
