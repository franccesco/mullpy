"""Mullpy tests."""

from ipaddress import ip_address
from mullvad_python import __version__
from mullvad_python import Mullpy


# Initialize API handler
mullpy = Mullpy()


def test_version():
    """Test version."""
    assert __version__ == '0.1.0'


def test_request_to_api():
    """Get a dump of all information."""
    assert isinstance(mullpy.api_data, dict)


def test_information_requested():
    """Test values requested by API."""
    assert ip_address(mullpy.ip)
    assert mullpy.country
    assert mullpy.country
    assert mullpy.city
    assert mullpy.longitude
    assert mullpy.latitude
    if mullpy.exit_ip:
        assert mullpy.exit_ip
        assert mullpy.exit_hostname
    assert mullpy.blacklisted


def test_if_user_is_blacklisted():
    """Test if is_blacklisted returns bool."""
    assert isinstance(mullpy.is_blacklisted(), bool)


def test_blacklisted_information():
    """Test blacklisted information."""
    assert isinstance(mullpy.blacklist_information(), list)


def test_check_open_port():
    """Test if port is open or closed (True or False)."""
    assert isinstance(mullpy.check_port(8080), bool)
