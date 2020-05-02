#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import datetime
import click
from dhcp_leases import DhcpLeases


def align(s, offset):
    """Adds 'offset' times whitespaces end of the string 's'"""
    return s + (' ' * offset)


def date_format(date):
    """Converts datetime to '%d.%m.%Y-%H:%M:%S' formatted string"""
    return date.strftime("%d.%m.%Y-%H:%M:%S")


def ip_format(ip):
    """Aligns IP address by near column"""
    offset = 20 - len(ip)
    return align(ip, offset)


def mac_format(mac):
    """Converts double columns to dashes of a mac address"""
    return mac.replace(':', '-')


@click.command()
@click.option('-k', '--kaynak', default='/var/dhcpd/var/db/dhcpd.leases',
             envvar='BTKLOG_KAYNAK', type=click.Path(exists=True),
             help="""ISC DHCP sunucu uyumlu(dhcpd.leases) IP dağıtım dosyası.
             BTKLOG_KAYNAK ortam değişkeniyle de ayarlanabilir.""")
@click.option('-h', '--hedef', default='.',
             envvar='BTKLOG_HEDEF', type=click.Path(exists=True),
             help="""5651 uyumlu IP dağıtım kaydının oluşturulacağı dizin.
             BTKLOG_HEDEF ortam değişkeniyle de ayarlanabilir.""")
def btklog(kaynak, hedef):
    """
    ISC DHCP sunucu IP dağıtım dosyalarından T.C. 5651 nolu
    yasaya uyumlu IP dağıtım kaydı üreten bir komut satırı programı.
    """

    lease_file = DhcpLeases(kaynak)
    leases = lease_file.get()

    if leases:
        log_title="IP Adresi           Kullanıma Başlama Zamanı\
     Kullanım Bitiş Zamanı      MAC Adresi"

        current_time = datetime.datetime.now().strftime("%d.%m.%Y-%H.%M.%S")
        btklog_file = hedef + "/btklog-" + current_time + ".log"

        with open(btklog_file, 'w') as logstream:
            click.echo(log_title, logstream)

            for lease in leases:
                click.echo(ip_format(lease.ip), logstream, nl=False)
                click.echo(align(date_format(lease.start), 10), logstream, nl=False)
                click.echo(align(date_format(lease.end), 8), logstream, nl=False)
                click.echo(mac_format(lease.ethernet), logstream)

        click.echo(btklog_file + " dosyası oluşturuldu.")
