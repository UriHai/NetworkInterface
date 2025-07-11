"""
This module contains parser for IP packets
"""

from typing import Union
from struct import unpack

from NetworkLayer.Protocols.IP.constants import IP_HEADERS_FORMAT, IP_HEADERS_LENGTH, IP_VERSION_BITS_SHIFT, \
    IP_IHL_MASk, IP_DSCP_BITS_SHIFT, IP_ECN_MASK
from NetworkLayer.Identifiers.ip_address import IPAddress


class IPPacket:
    def __init__(self, buffer: bytes) -> None:
        """
        Initialize IP packet
        :param buffer: buffer containing raw bytes of the ARP frame
        """
        headers: bytes = buffer[:IP_HEADERS_LENGTH]

        version_ihl: int
        dscp_ecn: int
        self.total_length: int
        flags_fragment_offset: int
        self.ttl: int
        self.protocol: int
        self.checksum: int
        src_ip: bytes
        dst_ip: bytes
        version_ihl, dscp_ecn, self.total_length, flags_fragment_offset, self.ttl, self.protocol, self.checksum, src_ip, dst_ip = unpack(
            IP_HEADERS_FORMAT, headers)

        self.version: int = version_ihl >> IP_VERSION_BITS_SHIFT
        self.ihl: int = version_ihl & IP_IHL_MASk
        self.dscp: int = dscp_ecn >> IP_DSCP_BITS_SHIFT
        self.ecn: int = dscp_ecn & IP_ECN_MASK
        self.src_ip: IPAddress = IPAddress(src_ip)
        self.dst_ip: IPAddress = IPAddress(dst_ip)
        self.options: Union[bytes, None] = None
        if self.ihl > IP_HEADERS_LENGTH:
            self.options = buffer[IP_HEADERS_LENGTH:self.ihl]

        self.payload: bytes = buffer[self.ihl:self.total_length]