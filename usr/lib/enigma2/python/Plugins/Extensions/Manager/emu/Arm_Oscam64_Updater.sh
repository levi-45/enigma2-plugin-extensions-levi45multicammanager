#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/oscam64
rm -R /usr/camscript/OSCam64-Arm_*.sh
###############################################################################
# Download and install OSCam64
cd /tmp 
set -e
wget "http://levi45.spdns.eu/Addons/Multicam/Arm/oscam64.tar.gz"

tar -xzf oscam64.tar.gz -C /
set +e
chmod 777 -R /usr/camscript/OSCam64-Arm_*.sh
rm -f oscam64.tar.gz
cd ..

sync
echo "#########################################################"
echo "#                           Levi45                      #"
echo "#########################################################"
echo "#               OSCam64 INSTALLED SUCCESSFULLY          #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
