#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /etc/tuxbox/config/ncam.*
###############################################################################
# Download and install Config
cd /tmp 
set -e
wget "http://levi45.spdns.eu/Addons/Multicam/Arm/ncamicamconfig.tar.gz"

tar -xzf ncamicamconfig.tar.gz -C /
set +e
rm -f ncamicamconfig.tar.gz
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
