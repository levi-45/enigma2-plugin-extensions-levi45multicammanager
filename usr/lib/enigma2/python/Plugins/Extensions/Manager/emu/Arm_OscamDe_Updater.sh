#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/oscamde
rm -R /usr/camscript/OSCamDe-Arm_*.sh
###############################################################################
# Download and install OSCamDe
cd /tmp 
set -e
wget "http://levi45.spdns.eu/Addons/Multicam/Arm/oscamde.tar.gz"

tar -xzf oscamde.tar.gz -C /
set +e
chmod 777 -R /usr/camscript/OSCamDe-Arm_*.sh
rm -f oscamde.tar.gz
cd ..

sync
echo "#########################################################"
echo "#                           Levi45                      #"
echo "#########################################################"
echo "#              OscamDe INSTALLED SUCCESSFULLY           #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
