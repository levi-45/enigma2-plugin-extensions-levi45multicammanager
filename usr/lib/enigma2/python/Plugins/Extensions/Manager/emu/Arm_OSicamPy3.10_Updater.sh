#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/oscamotr
rm -R /usr/camscript/OSicamPy3.10-Arm_*.sh
###############################################################################
# Download and install OSicamPy3.10
cd /tmp 
set -e
wget "http://levi45.spdns.eu/Addons/Multicam/Arm/oscamotr.tar.gz"

tar -xzf oscamotr.tar.gz -C /
set +e
chmod 777 -R /usr/camscript/OSicamPy3.10-Arm_*.sh
rm -f oscamotr.tar.gz
cd ..

sync
echo "#########################################################"
echo "#                           Levi45                      #"
echo "#########################################################"
echo "#              OSicamPy3.10 INSTALLED SUCCESSFULLY      #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
