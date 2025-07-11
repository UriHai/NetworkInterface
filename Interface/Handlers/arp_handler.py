"""
This module contains a handler for sending and receiving arp frames
"""

from LinkLayer.Identifiers.mac_address import MACAddress
from LinkLayer.Identifiers.constants import BROADCAST_MAC
from LinkLayer.Protocols.Ethernet.constants import ETHER_TYPE_ARP
from LinkLayer.Protocols.Ethernet.parser import EthernetFrame
from LinkLayer.Protocols.ARP.constants import ARP_OPERATION_REQUEST, ARP_OPERATION_REPLY
from LinkLayer.Protocols.ARP.parser import ARPFrame
from LinkLayer.Protocols.ARP.assembler import assemble_arp_frame
from NetworkLayer.Identifiers.ip_address import IPAddress


class ARPHandler:
    def __init__(self, interface) -> None:
        """
        Initialize EthernetHandler
        :param interface: The network interface that receives and sends frames
        """
        self.interface = interface

    def handle(self, ethernet_frame: EthernetFrame) -> None:
        """
        Handle inbound ARP frame
        :param ethernet_frame: The ethernet frame encapsulating the ARP frame
        """
        arp_frame: ARPFrame = ARPFrame(ethernet_frame.payload)
        src_ip: IPAddress = arp_frame.src_ip
        src_mac: MACAddress = arp_frame.src_mac
        self.interface.arp_cache.update_arp_cache(src_ip, src_mac)
        if ARP_OPERATION_REQUEST and arp_frame.dst_ip == self.interface.ip:
            self._send_arp_reply(src_mac, src_ip)

    def send_gratuitous_arp(self) -> None:
        """Send gratuitous ARP"""
        arp_frame: bytes = assemble_arp_frame(ARP_OPERATION_REQUEST, self.interface.mac, self.interface.ip,
                                              BROADCAST_MAC, self.interface.ip)
        self.interface.ethernet_handler.send(BROADCAST_MAC, ETHER_TYPE_ARP, arp_frame)

    def _send_arp_reply(self, dst_mac: MACAddress, dst_ip: IPAddress) -> None:
        """
        Send ARP reply
        :param dst_mac: Target MAC address
        :param dst_ip: Target IP address
        """
        arp_frame: bytes = assemble_arp_frame(ARP_OPERATION_REPLY, self.interface.mac, self.interface.ip, dst_mac,
                                              dst_ip)
        self.interface.ethernet_handler.send(dst_mac, ETHER_TYPE_ARP, arp_frame)

    def _send_arp_request(self, dst_ip: IPAddress) -> None:
        """
        Send ARP request
        :param dst_ip: Target IP address
        """
        arp_frame: bytes = assemble_arp_frame(ARP_OPERATION_REQUEST, self.interface.mac, self.interface.ip,
                                              BROADCAST_MAC, dst_ip)
        self.interface.ethernet_handler.send(BROADCAST_MAC, ETHER_TYPE_ARP, arp_frame)
