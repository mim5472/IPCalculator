IP address calculator using Python3.7
How to use.
Download or clone:
https://github.com/mim5472/mim5472.git

chmod u+x /path/to/file/ipcalc.py

Usage:
$ ./ipcalc.py -h
usage: ipcalc.py [-h] [--newprefix NEWPREFIX] ipaddr

positional arguments:
  ipaddr                IP address e.g. 10.10.10.1, 10.10.10.1/24,
                        10.10.10.0/24.

optional arguments:
  -h, --help            show this help message and exit
  --newprefix NEWPREFIX
                        Break network into smaller networks. e.g. 29, 30.
