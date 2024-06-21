#!/bin/sh
#DESCRIPTION=This script created by Levi45\nPublic Ip
cd /tmp
if [ -f tmp/ip.txt ] ; then
	rm /tmp/ip.txt
fi
echo "Yuor IP address is:">/tmp/ip.txt
wget -q -O - http://icanhazip.com/ >> /tmp/ip.txt
echo >>/tmp/ip.txt
if [ -f /tmp/ip.txt ] ; then
	cat /tmp/ip.txt
fi
