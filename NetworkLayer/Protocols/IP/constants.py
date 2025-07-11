"""
This module contains constants for the IP protocol
"""

from struct import calcsize

IP_HEADERS_FORMAT: str = "> B B H H H B B H 4s 4s"
IP_HEADERS_LENGTH: int = calcsize(IP_HEADERS_FORMAT)

IP_VERSION_BITS_SHIFT: int = 4
IP_IHL_MASk: int = 0xf0
IP_DSCP_BITS_SHIFT: int = 2
IP_ECN_MASK: int = 3

