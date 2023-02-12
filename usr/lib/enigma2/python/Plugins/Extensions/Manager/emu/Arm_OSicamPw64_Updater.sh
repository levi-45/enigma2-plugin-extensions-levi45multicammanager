#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/oscampw64
rm -R /usr/camscript/OSicamPw64-Arm_*.sh
###############################################################################
# Download and install OSicamPw64
cd /tmp 
set -e
wget "http://levi45.spdns.eu/Addons/Multicam/Arm/oscampw64.tar.gz"

tar -xzf oscampw64.tar.gz -C /
set +e
chmod 777 -R /usr/camscript/OSicamPw64-Arm_*.sh
rm -f oscampw64.tar.gz
cd ..

sync
echo "#########################################################"
echo "#                           Levi45                      #"
echo "#########################################################"
echo "#             OSicamPw64 INSTALLED SUCCESSFULLY         #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
