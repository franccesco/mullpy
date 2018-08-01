from ipaddress import ip_address
from mullvad_info import __version__
from mullvad_info import Mapi


# Initialize API handler
mapi = Mapi()


def test_version():
    """Test version."""
    assert __version__ == '0.1.0'


def test_request_to_api():
    """Get a dump of all information."""
    assert isinstance(mapi.api_data, dict)


def test_information_requested():
    """Test values requested by API."""
    assert ip_address(mapi.ip)
    assert mapi.country
    assert mapi.country
    assert mapi.city
    assert mapi.longitude
    assert mapi.latitud
    assert mapi.exit_ip
    assert mapi.exit_hostname
    assert mapi.blacklisted


def test_if_user_is_blacklisted():
    """Test if is_blacklisted returns bool."""
    assert isinstance(mapi.is_blacklisted(), bool)


def test_blacklisted_information():
    """Test blacklisted information."""
    assert isinstance(mapi.blacklist_information(), list)


def test_check_open_port():
    """Test if port is open or closed (True or False)."""
    assert isinstance(mapi.check_port(8080), bool)
