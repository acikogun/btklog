import click
from dhcp_leases import DhcpLeases


@click.command()
@click.option('-k', '--kaynak', default='/var/dhcpd/var/db/dhcpd.leases',
             envvar='BTKLOG_KAYNAK', type=click.Path(exists=True),
             help='ISC DHCP sunucu uyumlu(dhcpd.leases) IP dağıtım dosyası.')
@click.option('-h', '--hedef', default='.',
             envvar='BTKLOG_HEDEF', type=click.Path(exists=True),
             help='5651 uyumlu IP dağıtım kaydının oluşturulacağı dizin.')
def cli(kaynak, hedef):
    """
    ISC DHCP sunucu IP dağıtım dosyalarından T.C. 5651 nolu
    yasaya uyumlu IP dağıtım kaydı üreten bir komut satırı programı.
    """
