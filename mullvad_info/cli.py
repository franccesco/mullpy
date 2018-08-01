"""TODO: CLI."""
import click
import argparse
from .api import Mullpi


@click.command()
@click.option('--verbose', '-v', is_flag=True)
def main(verbose):
    """TODO: CLI main."""
    mullpi = Mullpi()

    # IP Address
    print('IP Address:', end='\t')
    click.secho(mullpi.ip, fg='green', bold=True)

    # Country / City
    print('Country:', end='\t')
    click.secho(f'{mullpi.city} / {mullpi.country}', fg='green', bold=True)

    # Longitude / Latitude
    longitude = click.style(str(mullpi.longitude), fg='green', bold=True)
    latitude = click.style(str(mullpi.latitud), fg='green', bold=True)
    print(f'Location:\t{longitude}, {latitude}')

    # Using Mullvad's exit IP?
    print('Using Mullvad:', end='\t')
    if mullpi.exit_ip:
        click.secho('True', fg='green', bold=True)
        print('Server Type:', end='\t')
        click.secho(mullpi.server_type, fg='green', bold=True)
    else:
        click.secho('False', fg='red', bold=True)

    # Organization
    print('Organization:', end='\t')
    click.secho(mullpi.organization, fg='green', bold=True)

    # Blacklisted?
    print('Blacklisted: ', end='\t')
    if mullpi.is_blacklisted():
        click.secho('True', fg='red', bold=True)
    else:
        click.secho('False', fg='green', bold=True)


if __name__ == '__main__':
    main()
