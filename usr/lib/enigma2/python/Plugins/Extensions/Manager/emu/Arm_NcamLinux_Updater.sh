#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/ncamlinux
rm -R /usr/camscript/NcamLinux-Arm_*.sh
###############################################################################
# Download and install NcamLinux
cd /tmp 
set -e
wget "http://levi45.spdns.eu/Addons/Multicam/Arm/ncamlinux.tar.gz"

tar -xzf ncamlinux.tar.gz -C /
set +e
chmod 777 -R /usr/camscript/NcamLinux-Arm_*.sh
rm -f ncamlinux.tar.gz
cd ..

sync
echo "#########################################################"
echo "#                           Levi45                      #"
echo "#########################################################"
echo "#              NcamLinux INSTALLED SUCCESSFULLY         #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
