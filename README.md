# Inductive Analog Switches

This library contains footprints and symbols for inductive analog keyboard
switches for use with the Texas Instruments LDC1312, LDC1314, LDC1612 and
LDC1614 inductance to digital converters.

Supported footprints for switches are currently PCB or plate mounted, LED or no
LED Cherry MX, Alps Matias or hybrid Cherry MX and Alps Matias.

## Requirements

- [KiCad](https://www.kicad.org/)
- [Python](https://www.python.org/)
  - `$ python -m pip install -r requirements.txt`

## Package

To generate the KiCad PCM package simply run the following command:

```sh
make
# Or:
make package
```

## Useful tools

- [Texas Instruments LDC Coil designer](https://webench.ti.com/wb5/LDC)

## Acknowledgements

A huge thank you goes out to
[keyswitch-kicad-library](https://github.com/perigoso/keyswitch-kicad-library)
from which i have borrowed some of the code to help generate the switch
footprints.

## Contributing

Contributions are very welcome! Just make sure to follow the rest of this
projects style as closely as possible and format with `make fmt`.

## License

[![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/)

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
