"""
This module contains the EthernetFrame class used to parse Ethernet frames
"""

from struct import unpack

from LinkLayer.Protocols.Ethernet.constants import ETHERNET_HEADERS_FORMAT, ETHERNET_HEADERS_LENGTH
from LinkLayer.Identifiers.mac_address import MACAddress


class EthernetFrame:
    def __init__(self, buffer: bytes) -> None:
        """
        Initialize Ethernet Frame
        :param buffer: Buffer containing raw bytes of the Ethernet frame
        """
        headers: bytes
        self.payload: bytes
        headers, self.payload = buffer[:ETHERNET_HEADERS_LENGTH], buffer[ETHERNET_HEADERS_LENGTH:]

        dst: bytes
        src: bytes
        self.ethernet_type: int
        dst, src, self.ethernet_type = unpack(ETHERNET_HEADERS_FORMAT, headers)

        self.dst: MACAddress = MACAddress(dst)
        self.src: MACAddress = MACAddress(src)
