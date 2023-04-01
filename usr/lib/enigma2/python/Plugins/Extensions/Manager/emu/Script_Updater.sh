#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/lib/enigma2/python/Plugins/Extensions/Manager/emu/*.sh
###############################################################################
# Download and install Script
cd /tmp 
set -e
wget "http://levi45.spdns.eu/Addons/Multicam/script.tar.gz"

tar -xzf script.tar.gz -C /
set +e
rm -f script.tar.gz
cd ..

sync
echo "#########################################################"
echo "#                           Levi45                      #"
echo "#########################################################"
echo "#                    All  Script Updated                #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0


