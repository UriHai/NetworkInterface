"""
This module contains Ethernet frame assembler
"""

from struct import pack

from LinkLayer.Protocols.Ethernet.constants import ETHERNET_HEADERS_FORMAT
from LinkLayer.Identifiers.mac_address import MACAddress


def assemble_ethernet_frame(dst: MACAddress, src: MACAddress, protocol_type: int, data: bytes) -> bytes:
    """
    Assemble an Ethernet frame
    :param dst: Target MAC address
    :param src: Source MAC address
    :param protocol_type: The protocol type
    :param data: The data to send
    :return: Bytes representation of the Ethernet frame
    """
    dst_bytes: bytes = dst.mac
    src_bytes: bytes = src.mac
    headers = pack(ETHERNET_HEADERS_FORMAT, dst_bytes, src_bytes, protocol_type)
    return headers + data
