"""
This module contains ARP frame assembler
"""

from struct import pack

from LinkLayer.Protocols.ARP.constants import ARP_FORMAT, HARDWARE_TYPE, PROTOCOL_TYPE, HARDWARE_SIZE, PROTOCOL_SIZE
from LinkLayer.Identifiers.mac_address import MACAddress
from NetworkLayer.Identifiers.ip_address import IPAddress


def assemble_arp_frame(operation: int, src_mac: MACAddress, src_ip: IPAddress, dst_mac: MACAddress,
                       dst_ip: IPAddress) -> bytes:
    """
    Assemble an ARP frame
    :param operation: Operation type (1 - request, 2- reply)
    :param src_mac: The source MAC address
    :param src_ip: The source IP address
    :param dst_mac: The target MAC address
    :param dst_ip: The target IP address
    :return: Bytes representation of the ARP frame
    """
    src_mac_bytes: bytes = src_mac.mac
    src_ip_bytes: bytes = src_ip.ip
    dst_mac_bytes: bytes = dst_mac.mac
    dst_ip_bytes: bytes = dst_ip.ip
    arp_frame: bytes = pack(ARP_FORMAT, HARDWARE_TYPE, PROTOCOL_TYPE, HARDWARE_SIZE, PROTOCOL_SIZE, operation,
                            src_mac_bytes, src_ip_bytes, dst_mac_bytes, dst_ip_bytes)
    return arp_frame
