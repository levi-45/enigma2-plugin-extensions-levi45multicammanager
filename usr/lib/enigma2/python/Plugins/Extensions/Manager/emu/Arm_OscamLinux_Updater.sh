#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/oscamlinux
rm -R /usr/camscript/OSCamLinux-Arm_*.sh
###############################################################################
# Download and install OSCamLinux
cd /tmp 
set -e
wget "http://levi45.spdns.eu/Addons/Multicam/Arm/oscamlinux.tar.gz"

tar -xzf oscamlinux.tar.gz -C /
set +e
chmod 777 -R /usr/camscript/OSCamLinux-Arm_*.sh
rm -f oscamlinux.tar.gz
cd ..

sync
echo "#########################################################"
echo "#                           Levi45                      #"
echo "#########################################################"
echo "#              OscamLinux INSTALLED SUCCESSFULLY        #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
