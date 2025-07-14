"""
This module contains an IP packet assembler
"""

from NetworkLayer.Protocols.IP.constants import, IP_HEADERS_LENGTH, IP_VERSION
from NetworkLayer.Identifiers.ip_address import IPAddress


def build_ip_packet(protocol: int, src_ip: IPAddress, dst_ip: IPAddress, payload: bytes) -> bytes:
    """
    Build an IPv4 packet
    :param protocol: IP protocol type
    :param src_ip: The source IP address
    :param dst_ip: The target IP address
    :param payload: The data of the packet
    :return: Bytes representation of the IP packet
    """
    ihl: int = IP_HEADERS_LENGTH
    version_ihl: int = (IP_VERSION << IP_BITS) + ihl
    dscp_ecn: int = IP_

    total_length: int = IP_HEADERS_LENGTH + len(data)
    headers: bytes = pack(IP_HEADERS_FORMAT, IP_VERSION_AND_IHL, IP_DSF, total_length, IP_IDENTIFICATION,
                          IP_FLAGS_AND_OFFSET, IP_TTL, ip_protocol, IP_HEADER_CHECKSUM,
                          convert_ip_string_to_bytes(src_ip), convert_ip_string_to_bytes(dst_ip))
    return headers + data
