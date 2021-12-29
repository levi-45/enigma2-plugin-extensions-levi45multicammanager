#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/revoscam64
rm -R /usr/camscript/RevOscam64-Arm_*.sh
###############################################################################
# Download and install Revcam64
cd /tmp 
set -e
wget "http://levi45.spdns.eu/Addons/Multicam/Arm/revoscam64.tar.gz"

tar -xzf revoscam64.tar.gz -C /
set +e
chmod 777 -R /usr/camscript/RevOscam64-Arm_*.sh
rm -f revoscam64.tar.gz
cd ..

sync
echo "#########################################################"
echo "#                           Levi45                      #"
echo "#########################################################"
echo "#              Revcam64 INSTALLED SUCCESSFULLY          #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
