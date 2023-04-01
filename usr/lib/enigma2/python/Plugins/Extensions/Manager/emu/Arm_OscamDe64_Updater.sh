#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/oscamde64
rm -R /usr/camscript/OSCamDe64-Arm_*.sh
###############################################################################
# Download and install OSCamDe64
cd /tmp 
set -e
wget "http://levi45.spdns.eu/Addons/Multicam/Arm/oscamde64.tar.gz"

tar -xzf oscamde64.tar.gz -C /
set +e
chmod 777 -R /usr/camscript/OSCamDe64-Arm_*.sh
rm -f oscamde64.tar.gz
cd ..

sync
echo "#########################################################"
echo "#                           Levi45                      #"
echo "#########################################################"
echo "#              OSCamDe64 INSTALLED SUCCESSFULLY         #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
