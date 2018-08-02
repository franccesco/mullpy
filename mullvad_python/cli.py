"""Command Line Interface module."""
import click
from .api import Mullpy
from .banner import banner


def main():
    """CLI for Mullvad API."""
    mullpy = Mullpy()

    if mullpy.exit_ip:
        text_color = 'green'
    else:
        text_color = 'red'

    click.secho(banner, fg=text_color, bold=True)

    # Using Mullvad's exit IP?
    print('Using Mullvad:', end='\t')
    if mullpy.exit_ip:
        click.secho('True', fg=text_color, bold=True)
        print('Server Type:', end='\t')
        click.secho(mullpy.server_type, fg=text_color, bold=True)
    else:
        click.secho("FALSE. INSECURE CONNECTION!", fg=text_color, bold=True)

    # IP Address
    print('IP Address:', end='\t')
    click.secho(mullpy.ip, fg=text_color, bold=True)

    # Country / City
    print('Country:', end='\t')
    click.secho(f'{mullpy.city}, {mullpy.country}', fg=text_color, bold=True)

    # Longitude / Latitude
    print(f'Location:', end='\t')
    longitude, latitude = mullpy.longitude, mullpy.latitude
    click.secho(f'{longitude}, {latitude}', fg=text_color, bold=True)

    # Organization
    if mullpy.exit_ip:
        print('Organization:', end='\t')
        click.secho(mullpy.organization, fg=text_color, bold=True)

    # Blacklisted?
    print('Blacklisted: ', end='\t')
    if mullpy.is_blacklisted():
        click.secho('True', fg='red', bold=True)
    else:
        click.secho('False', fg='green', bold=True)
    print()
    exit(0)


if __name__ == '__main__':
    main()
