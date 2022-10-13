#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /etc/tuxbox/config/oscam.*
###############################################################################
# Download and install Config
cd /tmp 
set -e
wget "http://levi45.spdns.eu/Addons/Multicam/Arm/oscamconfig.tar.gz"

tar -xzf oscamconfig.tar.gz -C /
set +e
rm -f oscamconfig.tar.gz
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
