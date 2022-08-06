#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/gcam
rm -R /usr/camscript/GCam-Arm_*.sh
###############################################################################
# Download and install Gcam
cd /tmp 
set -e
wget "http://levi45.spdns.eu/Addons/Multicam/Arm/gcam.tar.gz"

tar -xzf gcam.tar.gz -C /
set +e
chmod 777 -R /usr/camscript/GCam-Arm_*.sh
rm -f gcam.tar.gz
cd ..

sync
echo "#########################################################"
echo "#                           Levi45                      #"
echo "#########################################################"
echo "#               Gcam INSTALLED SUCCESSFULLY             #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
