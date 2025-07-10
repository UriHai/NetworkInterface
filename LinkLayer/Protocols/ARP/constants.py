"""
This module contains constants for the ARP protocol
"""

from struct import calcsize

ARP_FORMAT: str = ">HHbbH6s4s6s4s"
ARP_LENGTH: int = calcsize(ARP_FORMAT)
HARDWARE_TYPE: int = 1
PROTOCOL_TYPE: int = 0x800
HARDWARE_SIZE: int = 6
PROTOCOL_SIZE: int = 4
