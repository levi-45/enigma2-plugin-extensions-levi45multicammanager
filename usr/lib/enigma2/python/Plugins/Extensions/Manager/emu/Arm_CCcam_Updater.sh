#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/cccam
rm -R /usr/camscript/CCcam-Arm_*.sh
###############################################################################
# Download and install CCcam
cd /tmp 
set -e
wget "http://levi45.spdns.eu/Addons/Multicam/Arm/cccam.tar.gz"

tar -xzf cccam.tar.gz -C /
chmod 777 -R /usr/camscript/CCcam-Arm_*.sh
set +e
rm -f cccam.tar.gz
cd ..

sync
echo "#########################################################"
echo "#                           Levi45                      #"
echo "#########################################################"
echo "#               CCcam INSTALLED SUCCESSFULLY            #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
