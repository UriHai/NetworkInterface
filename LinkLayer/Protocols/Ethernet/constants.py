"""
This module contains constants for the Ethernet protocol
"""

from struct import calcsize

ETHERNET_HEADERS_FORMAT: str = ">6s6sH"
ETHERNET_HEADERS_LENGTH: int = calcsize(ETHERNET_HEADERS_FORMAT)
