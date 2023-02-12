#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/oscamtr
rm -R /usr/camscript/OSicamPy3.9-Arm_*.sh
###############################################################################
# Download and install OSicamPy3.9
cd /tmp 
set -e
wget "http://levi45.spdns.eu/Addons/Multicam/Arm/oscamtr.tar.gz"

tar -xzf oscamtr.tar.gz -C /
set +e
chmod 777 -R /usr/camscript/OSicamPy3.9-Arm_*.sh
rm -f oscamtr.tar.gz
cd ..

sync
echo "#########################################################"
echo "#                           Levi45                      #"
echo "#########################################################"
echo "#              OSicamPy3.9 INSTALLED SUCCESSFULLY       #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
