from Interface.interface import Interface
from LinkLayer.Identifiers.mac_address import MACAddress


def main():
    interface = Interface("Intel(R) Wi-Fi 6 AX200 160MHz")
    interface.ethernet_handler.send(MACAddress("11:11:11:11:11:11"), 0x800, b'abcdefg')
    interface.start()


if __name__ == '__main__':
    main()
