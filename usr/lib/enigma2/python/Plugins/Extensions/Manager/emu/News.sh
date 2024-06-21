#!/bin/sh
#DESCRIPTION=This script created by Levi45\nNews From Server
###############################################################################
cd /tmp
rm -f /tmp/News.txt
wget http://levi45.spdns.eu/Addons/Multicam/News.txt -qO /tmp/News.txt > /dev/null 2>&1

if [ -f /tmp/News.txt ]; then 
		cat /tmp/News.txt
		echo
else
		echo
		echo "There Isin't Any News For Now Thank You"
		echo
fi

exit 0 
