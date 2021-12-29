#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/suposcam64
rm -R /usr/camscript/SupOscam64-Arm_*.sh
###############################################################################
# Download and install Supcam64
cd /tmp 
set -e
wget "http://levi45.spdns.eu/Addons/Multicam/Arm/suposcam64.tar.gz"

tar -xzf suposcam64.tar.gz -C /
set +e
chmod 777 -R /usr/camscript/SupOscam64-Arm_*.sh
rm -f suposcam64.tar.gz
cd ..

sync
echo "#########################################################"
echo "#                           Levi45                      #"
echo "#########################################################"
echo "#              Supcam64 INSTALLED SUCCESSFULLY          #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
