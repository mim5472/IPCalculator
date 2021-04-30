#!/usr/bin/env python3.7
import ipaddress
import socket
import argparse

# convert Decimal to binary format.
def dectobin(ip):
    ip = str(ip)
    ip_split = ip.split('.')
    ip_bin = []
    for i in ip_split:
        ip_bin.append('{:08b}'.format(int(i)))
    return ip_bin


# read argument parsed to the script
parser = argparse.ArgumentParser()
parser.add_argument("ipaddr", help="IP address e.g. 10.10.10.1, 10.10.10.1/24, 10.10.10.0/24")
args = parser.parse_args()

try:
    interface = ipaddress.IPv4Interface(args.ipaddr)
    ip_network = ipaddress.IPv4Network(interface.network)

    print('IP adddress\t\t\t: {}'.format(interface.ip))
    print('IP Netmask\t\t\t: {}'.format(interface.netmask))
    print('IP Hostmask\t\t\t: {}'.format(interface.hostmask))
    print('IP Network\t\t\t: {}'.format(interface.network))
    print('IP Prefix length\t\t: {}'.format(interface.with_prefixlen))
    print('IP Is Global\t\t\t: {}'.format(interface.is_global))
    print('IP Is Private\t\t\t: {}'.format(interface.is_private))
    print('IP Is Multicast\t\t\t: {}'.format(interface.is_multicast))
    print('IP Is Loopback\t\t\t: {}'.format(interface.is_loopback))
    print('IP Hex format\t\t\t: {}'.format(socket.inet_aton(str(interface.ip)).hex()))
    print('Binary format\t\t\t: {}'.format('.'.join(dectobin(interface.ip))))
    print('Decimal format\t\t\t: {}'.format(int(interface.ip)))
    print('Net Prefix Length\t\t: {}'.format(ip_network.prefixlen))
    print('Network address\t\t\t: {}'.format(ip_network.network_address))
    print('Broadcast address\t\t: {}'.format(ip_network.broadcast_address))

    if ip_network.num_addresses - 2 > 0:
        print('Total address\t\t\t: {}'.format(ip_network.num_addresses - 2))
    else:
        print('Total address\t\t\t: {}'.format('Host address'))
except ipaddress.AddressValueError:
    print('Not a valid IP address.')





