"""Module holding Mullpy class."""

from requests import get as rget
from .dns_leak import dnsleak_results


class Mullpy():
    """Mullpy class methods.
    Initialize requesting basic data about yourself to see if you're connected
    to Mullvad's servers.

    isblacklisted(): Return a bool if you're blacklisted.
    blacklist_information: Return information if you're blacklisted under
    Spamhouse or Project Honeypot.

    check_port(): Check if your port is reachable.
    """

    def __init__(self):
        """Request API data and initialize them."""
        self.api_data = rget('https://am.i.mullvad.net/json').json()
        self.ip = self.api_data['ip']
        self.country = self.api_data['country']
        self.city = self.api_data['city']
        self.longitude = self.api_data['longitude']
        self.latitude = self.api_data['latitude']
        self.exit_ip = self.api_data['mullvad_exit_ip']
        if self.exit_ip:
            self.exit_hostname = self.api_data['mullvad_exit_ip_hostname']
            self.organization = self.api_data['organization']
            self.server_type = self.api_data['mullvad_server_type']
        self.blacklisted = self.api_data['blacklisted']

    def is_blacklisted(self):
        """Return True or False if user is blacklisted."""
        is_blacklisted = self.blacklisted['blacklisted']
        return is_blacklisted

    def blacklist_information(self):
        """Return blacklisted information."""
        blacklist_info = self.blacklisted['results']
        return blacklist_info

    @staticmethod
    def is_leaking():
        """Check if user is leaking DNS data."""
        return dnsleak_results()

    @staticmethod
    def check_port(port):
        """Ony check if port is open."""
        req_port = rget(f'https://am.i.mullvad.net/port/{port}').json()
        is_open = req_port['reachable']
        return is_open
