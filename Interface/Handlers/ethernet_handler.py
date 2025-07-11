"""This module contains the EthernetHandler class that can handle and send Ethernet frames"""

from LinkLayer.Identifiers.constants import BROADCAST_MAC
from LinkLayer.Identifiers.mac_address import MACAddress
from LinkLayer.Protocols.Ethernet.assembler import assemble_ethernet_frame
from LinkLayer.Protocols.Ethernet.parser import EthernetFrame
from LinkLayer.Protocols.Ethernet.constants import ETHER_TYPE_ARP


class EthernetHandler:
    def __init__(self, interface) -> None:
        """
        Initialize EthernetHandler
        :param interface: The network interface that receives and sends frames
        """
        self.interface = interface

    def send(self, dst_mac: MACAddress, protocol_type: int, payload: bytes) -> None:
        """
        Send an Ethernet frame
        :param dst_mac: The target MAC address
        :param protocol_type: The protocol type
        :param payload: The payload of the frame
        """
        frame: bytes = assemble_ethernet_frame(dst_mac, self.interface.mac, protocol_type, payload)
        self.interface.sock.send(frame)

    def handle(self, payload: bytes) -> None:
        """
        Handle incoming Ethernet frame
        :param payload: Bytes representation of the frame
        """
        frame: EthernetFrame = EthernetFrame(payload)
        if not self._should_handle(frame):
            return
        if frame.ethernet_type == ETHER_TYPE_ARP:
            self.interface.arp_handler.handle(frame)

    def _should_handle(self, frame: EthernetFrame) -> bool:
        """
        Determine whether the Ethernet frame is addressed to this interface
        :param frame: The Ethernet frame
        :return: True if the frames was addressed to this interface, False otherwise
        """
        return (frame.dst == self.interface.mac or frame.dst == BROADCAST_MAC) and frame.src != self.interface.mac
