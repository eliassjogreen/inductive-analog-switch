all: fab

fab: fab-jlcpcb fab-oshpark fab-pcbway

fab-jlcpcb:
	kikit fab jlcpcb --no-drc example.kicad_pcb output/fab-jlcpcb/

fab-oshpark:
	kikit fab oshpark --no-drc example.kicad_pcb output/fab-oshpark/

fab-pcbway:
	kikit fab pcbway --no-drc example.kicad_pcb output/fab-pcbway/

clean:
	rm -rf output/
