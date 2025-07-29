# LanAccessWithZeroTier

## Access your LAN thru mobile phone/computer whatever you are using zero tier sofware defined nework in a LAN host.
```
/usr/bin/ip a
  enp0s3
  192.168.1.17/24
/usr/bin/ip r
  192.168.1.0/24
Create network
  Network ID: abcdefghi12345
/usr/bin/curl -s https://install.zerotier.com | sudo bash
/usr/sbin/zerotier-cli join abcdefghi12345
Authorize
/usr/bin/ip a
  ztnfahsfg3
  172.29.239.10/16
```
![ManagedRoutes,jpg](ManagedRoutes,jpg.JPG)
```
/usr/bin/nano /etc/sysctl.conf
  net.ipv4.ip_forward=1
/usr/bin/apt-get install iptables
PHY_IFACE=enp0s3; ZT_IFACE=ztnfahsfg3
iptables -t nat -A POSTROUTING -o $PHY_IFACE -j MASQUERADE
iptables -A FORWARD -i $PHY_IFACE -o $ZT_IFACE -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i $ZT_IFACE -o $PHY_IFACE -j ACCEPT
/usr/bin/apt-get update
/usr/bin/apt-get install iptables-persistent
bash -c iptables-save > /etc/iptables/rules.v4
shutdown -r 0

220MB RAM used
0% CPU
```
## Access your LAN thru mobile phone/computer whatever you are using zero tier sofware defined nework in a LAN docker.

## Web interface
```
apt-get update
apt-get install -y python3 python3-venv python3-pip
mkdir /var/www
cd /var/www
python3 -m venv venv
source venv/bin/activate
pip install Flask gunicorn nginx
rm /etc/nginx/sites-enabled/default

````

/etc/nginx/sites-available/LanAccessWithZeroTier

