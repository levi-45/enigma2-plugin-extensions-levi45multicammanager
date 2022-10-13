#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/mgcam
rm -R /usr/camscript/MgCam-Arm_*.sh
###############################################################################
# Download and install MGcam
cd /tmp 
set -e
wget "http://levi45.spdns.eu/Addons/Multicam/Arm/mgcam.tar.gz"

tar -xzf mgcam.tar.gz -C /
set +e
chmod 777 -R /usr/camscript/MgCam-Arm_*.sh
rm -f mgcam.tar.gz
cd ..

sync
echo "#########################################################"
echo "#                           Levi45                      #"
echo "#########################################################"
echo "#               MGcam  INSTALLED SUCCESSFULLY           #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
