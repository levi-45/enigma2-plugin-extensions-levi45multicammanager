#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/suposcam
rm -R /usr/camscript/SupOscam-Arm_*.sh
###############################################################################
# Download and install Supcam
cd /tmp 
set -e
wget "http://levi45.spdns.eu/Addons/Multicam/Arm/suposcam.tar.gz"

tar -xzf suposcam.tar.gz -C /
set +e
chmod 777 -R /usr/camscript/SupOscam-Arm_*.sh
rm -f suposcam.tar.gz
cd ..

sync
echo "#########################################################"
echo "#                           Levi45                      #"
echo "#########################################################"
echo "#               Supcam INSTALLED SUCCESSFULLY           #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
