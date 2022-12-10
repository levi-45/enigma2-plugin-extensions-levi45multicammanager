#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/ncam
rm -R /usr/camscript/NCam-Arm_*.sh
###############################################################################
# Download and install Ncam
cd /tmp 
set -e
wget "http://levi45.spdns.eu/Addons/Multicam/Arm/ncam.tar.gz"

tar -xzf ncam.tar.gz -C /
set +e
chmod 777 -R /usr/camscript/NCam-Arm_*.sh
rm -f ncam.tar.gz
cd ..

sync
echo "#########################################################"
echo "#                           Levi45                      #"
echo "#########################################################"
echo "#               Ncam INSTALLED SUCCESSFULLY             #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
