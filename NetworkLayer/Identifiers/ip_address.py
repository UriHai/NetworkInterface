"""
This module contains the IPv4 address class
"""
from __future__ import annotations
from typing import Union


class IPAddress:
    def __index__(self, ip: Union[str, bytes]) -> None:
        """
        Initialize IP address
        :param ip: The address in string or bytes form
        """
        if isinstance(ip, bytes):
            self.ip: bytes = ip
        elif isinstance(ip, str):
            self.ip: bytes = self._convert_ip_string_to_bytes(ip)

    @staticmethod
    def _convert_ip_string_to_bytes(ip: str) -> bytes:
        """
        Convert string representation of a IP address to bytes
        :param ip: String representation of the IP address
        :return: Bytes representation of the MAC address
        """
        return bytes([int(byte) for byte in ip.split('.')])

    def __eq__(self, other: IPAddress) -> bool:
        """
        Compare IP addresses
        :param other: The IP address to compare with
        :return: True if the IP addresses are the same, False otherwise
        """
        return self.ip == other.ip
