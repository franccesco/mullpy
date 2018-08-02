"""TODO: CLI."""
import click
import argparse
from .api import Mullpi
from .banner import banner


@click.command()
@click.option('--verbose', '-v', is_flag=True)
def main(verbose):
    """TODO: CLI main."""
    mullpi = Mullpi()

    if mullpi.exit_ip:
        text_color = 'green'
    else:
        text_color = 'red'

    click.secho(banner, fg=text_color, bold=True)

    # Using Mullvad's exit IP?
    print('Using Mullvad:', end='\t')
    if mullpi.exit_ip:
        click.secho('True', fg=text_color, bold=True)
        print('Server Type:', end='\t')
        click.secho(mullpi.server_type, fg=text_color, bold=True)
    else:
        click.secho("FALSE. INSECURE CONNECTION!", fg=text_color, bold=True)

    # IP Address
    print('IP Address:', end='\t')
    click.secho(mullpi.ip, fg=text_color, bold=True)

    # Country / City
    print('Country:', end='\t')
    click.secho(f'{mullpi.city} / {mullpi.country}', fg=text_color, bold=True)

    # Longitude / Latitude
    longitude = click.style(str(mullpi.longitude), fg=text_color, bold=True)
    latitude = click.style(str(mullpi.latitud), fg=text_color, bold=True)
    print(f'Location:\t{longitude}, {latitude}')

    # Organization
    if mullpi.exit_ip:
        print('Organization:', end='\t')
        click.secho(mullpi.organization, fg=text_color, bold=True)

    # Blacklisted?
    print('Blacklisted: ', end='\t')
    if mullpi.is_blacklisted():
        click.secho('True', fg=text_color, bold=True)
    else:
        click.secho('False', fg=text_color, bold=True)
    print()

if __name__ == '__main__':
    main()
