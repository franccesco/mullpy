"""Module to test for DNS leak in bash.ws."""
from os import system
from random import randint
from requests import get as rget


def do_fake_ping(bashws_id, count=3):
    """Do fake dns requests to provide to bash.ws."""
    api_domain = 'bash.ws'
    for ping_count in range(count):
        full_domain = f'{ping_count}.{bashws_id}.{api_domain}'
        system(f'ping -c 1 {full_domain} > /dev/null 2>&1')


def dnsleak_results():
    """Return a bool if dns leak results are positive or negative."""
    bashws_id = randint(1000000, 9999999)
    do_fake_ping(bashws_id)
    results = rget(f'https://bash.ws/dnsleak/test/{bashws_id}?json').json()
    if results[2]['ip'] == 'DNS is not leaking.':
        return False
    return True
