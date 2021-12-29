#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/multics
rm -R /usr/camscript/MultiCS-Arm_*.sh
###############################################################################
# Download and install MultiCS
cd /tmp 
set -e
wget "http://levi45.spdns.eu/Addons/Multicam/Arm/multics.tar.gz"

tar -xzf multics.tar.gz -C /
set +e
chmod 777 -R /usr/camscript/MultiCS-Arm_*.sh
rm -f multics.tar.gz
cd ..

sync
echo "#########################################################"
echo "#                           Levi45                      #"
echo "#########################################################"
echo "#             MultiCS INSTALLED SUCCESSFULLY            #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
