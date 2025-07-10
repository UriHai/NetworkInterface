"""
This module contains a parser for ARP frames
"""

from struct import unpack

from LinkLayer.Identifiers.mac_address import MACAddress
from LinkLayer.Protocols.ARP.constants import ARP_FORMAT
from NetworkLayer.Identifiers.ip_address import IPAddress


class ARPFrame:
    def __init__(self, buffer: bytes) -> None:
        """
        Initialize ARP Frame
        :param buffer: Buffer containing raw bytes of the ARP frame
        """
        # buffer = buffer[:ARP_LENGTH] TODO: I had an issue in the previous version that I solved with this line.
        #  Need to see if it recreates and understand it
        self.hardware_type: int
        self.protocol_type: int
        self.hardware_length: int
        self.protocol_length: int
        self.operation: int
        src_mac: bytes
        src_ip: bytes
        dst_mac: bytes
        dst_ip: bytes

        self.hardware_type, self.protocol_type, self.hardware_length, self.protocol_length, \
        self.operation, src_mac, src_ip, dst_mac, dst_ip = unpack(ARP_FORMAT, buffer)

        self.src_mac: MACAddress = MACAddress(src_mac)
        self.src_ip: IPAddress = IPAddress(src_ip)
        self.dst_mac: MACAddress = MACAddress(src_mac)
        self.dst_ip: IPAddress = IPAddress(dst_ip)
