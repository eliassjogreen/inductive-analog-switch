# Example

This folder contains all of the relevant parts for an example PCB using the
inductive analog keyswitch footprints and symbols along with the LDC1314 or
LDC1614 inductance to digital converter. The example is a simple breakout board
for four switches and a SMD mounted LDC1314 IC.

## Requirements

- [KiCad](https://www.kicad.org/)
- [Python](https://www.python.org/)
- [Kikit](https://github.com/yaqwsx/KiKit)

## Fabrication

To generate gerbers for fabrication you will have to run one or all of the
makefile commands:

```sh
make
# Or one of the following:
make fab-jlcpcb
make fab-oshpark
make fab-pcbway
```

## License

[![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/)

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
