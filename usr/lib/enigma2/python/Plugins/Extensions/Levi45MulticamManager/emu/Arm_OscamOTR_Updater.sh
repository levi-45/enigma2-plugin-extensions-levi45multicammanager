#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/oscamotr
rm -R /usr/camscript/OSCamOTR-Arm_*.sh
###############################################################################
# Download and install OscamOTR
cd /tmp 
set -e
wget "http://levi45.spdns.eu/Addons/Multicam/Arm/oscamotr.tar.gz"

tar -xzf oscamotr.tar.gz -C /
set +e
chmod 777 -R /usr/camscript/OSCamOTR-Arm_*.sh
rm -f oscamotr.tar.gz
cd ..

sync
echo "#########################################################"
echo "#                           Levi45                      #"
echo "#########################################################"
echo "#              OscamOTR INSTALLED SUCCESSFULLY          #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
