#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /etc/tuxbox/config/Oscamicam
###############################################################################
# Download and install Config
cd /tmp 
set -e
wget "http://levi45.spdns.eu/Addons/Multicam/Arm/oscamicamconfig.tar.gz"

tar -xzf oscamicamconfig.tar.gz -C /
set +e
rm -f oscamicamconfig.tar.gz
cd ..

sync
echo "#########################################################"
echo "#                           Levi45                      #"
echo "#########################################################"
echo "#               Config INSTALLED SUCCESSFULLY           #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
