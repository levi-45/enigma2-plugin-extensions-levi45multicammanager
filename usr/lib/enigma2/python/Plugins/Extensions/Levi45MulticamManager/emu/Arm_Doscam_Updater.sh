#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/doscam
rm -R /usr/camscript/DosCam-Arm_*.sh
###############################################################################
# Download and install Doscam
cd /tmp 
set -e
wget "http://levi45.spdns.eu/Addons/Multicam/Arm/doscam.tar.gz"

tar -xzf doscam.tar.gz -C /
set +e
chmod 777 -R /usr/camscript/DosCam-Arm_*.sh
rm -f doscam.tar.gz
cd ..

sync
echo "#########################################################"
echo "#                           Levi45                      #"
echo "#########################################################"
echo "#               Doscam INSTALLED SUCCESSFULLY           #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
