#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/oscampw
rm -R /usr/camscript/OSicamPy2-Arm_*.sh
###############################################################################
# Download and install OSicamPy2
cd /tmp 
set -e
wget "http://levi45.spdns.eu/Addons/Multicam/Arm/oscampw.tar.gz"

tar -xzf oscampw.tar.gz -C /
set +e
chmod 777 -R /usr/camscript/OSicamPy2-Arm_*.sh
rm -f oscampw.tar.gz
cd ..

sync
echo "#########################################################"
echo "#                           Levi45                      #"
echo "#########################################################"
echo "#              OSicamPy2 INSTALLED SUCCESSFULLY         #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
