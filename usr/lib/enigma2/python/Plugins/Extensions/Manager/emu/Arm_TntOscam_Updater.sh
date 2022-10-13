#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/tntoscam
rm -R /usr/camscript/TntOSCam-Arm_*.sh
###############################################################################
# Download and install TntOscam
cd /tmp 
set -e
wget "http://levi45.spdns.eu/Addons/Multicam/Arm/tntoscam.tar.gz"

tar -xzf tntoscam.tar.gz -C /
set +e
rm -f tntoscam.tar.gz
chmod 777 -R /usr/camscript/TntOSCam-Arm_*.sh
chmod 777 -R /usr/bin/tntoscam
cd ..

sync
echo "#########################################################"
echo "#                           Levi45                      #"
echo "#########################################################"
echo "#             TntOscam INSTALLED SUCCESSFULLY           #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
