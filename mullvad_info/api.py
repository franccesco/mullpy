"""TODO: api documentation."""

from requests import get as rget


class Mapi():
    """Todo: API."""

    def __init__(self):
        """TODO: initialization."""
        self.api_data = rget('https://am.i.mullvad.net/json').json()
        self.ip = self.api_data['ip']
        self.country = self.api_data['country']
        self.city = self.api_data['city']
        self.longitude = self.api_data['longitude']
        self.latitud = self.api_data['latitude']
        self.exit_ip = self.api_data['mullvad_exit_ip']
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

    def check_port(self, port):
        """Ony check if port is open."""
        req_port = rget(f'https://am.i.mullvad.net/port/{port}').json()
        is_open = req_port['reachable']
        return is_open
