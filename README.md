# btklog
[![Build Status](https://travis-ci.com/acikogun/btklog.svg?branch=master)](https://travis-ci.com/acikogun/btklog)
[![CodeFactor](https://www.codefactor.io/repository/github/acikogun/btklog/badge)](https://www.codefactor.io/repository/github/acikogun/btklog)
![PyPI](https://img.shields.io/pypi/v/btklog)

ISC DHCP sunucu IP dağıtım dosyalarından T.C. 5651 nolu yasaya uyumlu IP dağıtım kaydı üreten bir Python komut satırı programı.

### Örnek dhcpd.leases dosyası

```
# The format of this file is documented in the dhcpd.leases(5) manual page.
# This lease file was written by isc-dhcp-4.2.4-P2

server-duid "\000\001\000\001& eS\000\014)U\267\275";

lease 10.0.0.2 {
  starts 5 2020/04/10 08:27:36;
  ends 5 2020/04/10 10:57:36;
  cltt 5 2020/04/10 08:27:36;
  binding state active;
  next binding state free;
  rewind binding state free;
  hardware ethernet 00:50:56:3e:87:44;
  uid "\001\000PV>\207D";
}
lease 10.0.0.3 {
  starts 5 2020/04/10 08:27:39;
  ends 5 2020/04/10 10:57:39;
  cltt 5 2020/04/10 08:27:39;
  binding state active;
  next binding state free;
  rewind binding state free;
  hardware ethernet 00:0c:29:b6:53:f1;
  uid "\001\000\014)\266S\361";
}
```

### btklog tarafından oluşturulmuş 5651 nolu yasa uyumlu kaydı

```
IP Adresi           Kullanıma Başlama Zamanı     Kullanım Bitiş Zamanı      MAC Adresi
10.0.0.2            10.04.2020-08:27:36          10.04.2020-10:57:36        00-50-56-3e-87-44
10.0.0.3            10.04.2020-08:27:39          10.04.2020-10:57:39        00-0c-29-b6-53-f1
```


## Kurulum

pip ile kurulum

```bash
pip install btklog
```

Yardım menüsünü görüntüle

```bash
btklog --help
```


## Ayarlar

-k, --kaynak PATH - ISC DHCP sunucu uyumlu(dhcpd.leases) IP dağıtım dosyası.

- **BTKLOG_KAYNAK** ortam değişkeniyle de ayarlanabilir.
- Belirtilmezse, varsayılan olarak '/var/dhcpd/var/db/dhcpd.leases' dosyasını açmayı dener.

-h, --hedef PATH - 5651 uyumlu IP dağıtım kaydının oluşturulacağı dizin.

 - **BTKLOG_HEDEF** ortam değişkeniyle de ayarlanabilir.
 - Belirtilmezse, kayıt dosyası varsayılan olarak mevcut dizine oluşturulur.


## Örnekler

Mevcut dizindeki dhcpd.leases dosyasından /tmp dizinine kayıt oluştur.

```bash
btklog -k dhcpd.leases -h /tmp
```

Aynı örneği ortam değişkenlerini kullanarak yap.
(Betikler için daha uygun)

```bash
#/bin/sh

export BTKLOG_KAYNAK=dhcpd.leases
export BTKLOG_HEDEF=/tmp

btklog
```
