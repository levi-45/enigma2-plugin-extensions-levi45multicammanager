#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/oscamymod
rm -R /usr/camscript/OSCamYmod-Arm_*.sh
###############################################################################
# Download and install OscamYmod
cd /tmp 
set -e
wget "http://levi45.spdns.eu/Addons/Multicam/Arm/oscamymod.tar.gz"

tar -xzf oscamymod.tar.gz -C /
set +e
chmod 777 -R /usr/camscript/OSCamYmod-Arm_*.sh
rm -f oscamymod.tar.gz
cd ..

sync
echo "#########################################################"
echo "#                           Levi45                      #"
echo "#########################################################"
echo "#            OscamYmod INSTALLED SUCCESSFULLY           #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
