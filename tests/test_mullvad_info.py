from ipaddress import ip_address
from mullvad_info import __version__
from mullvad_info import Mullpi


# Initialize API handler
mullpi = Mullpi()


def test_version():
    """Test version."""
    assert __version__ == '0.1.0'


def test_request_to_api():
    """Get a dump of all information."""
    assert isinstance(mullpi.api_data, dict)


def test_information_requested():
    """Test values requested by API."""
    assert ip_address(mullpi.ip)
    assert mullpi.country
    assert mullpi.country
    assert mullpi.city
    assert mullpi.longitude
    assert mullpi.latitud
    if mullpi.exit_ip:
        assert mullpi.exit_ip
        assert mullpi.exit_hostname
    assert mullpi.blacklisted


def test_if_user_is_blacklisted():
    """Test if is_blacklisted returns bool."""
    assert isinstance(mullpi.is_blacklisted(), bool)


def test_blacklisted_information():
    """Test blacklisted information."""
    assert isinstance(mullpi.blacklist_information(), list)


def test_check_open_port():
    """Test if port is open or closed (True or False)."""
    assert isinstance(mullpi.check_port(8080), bool)
