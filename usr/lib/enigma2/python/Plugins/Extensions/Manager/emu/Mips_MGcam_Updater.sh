#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/mgcam
rm -R /usr/camscript/MgCam-Mips_*.sh
###############################################################################
# Download and install MGcam
cd /tmp 
set -e
wget "http://levi45.spdns.eu/Addons/Multicam/Mips/mgcam.tar.gz"

tar -xzf mgcam.tar.gz -C /
set +e
rm -f mgcam.tar.gz
chmod 777 -R /usr/camscript/MgCam-Mips_*.sh
cd ..

sync
echo "#########################################################"
echo "#                             Levi45                    #"
echo "#########################################################"
echo "#               MGcam  INSTALLED SUCCESSFULLY           #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
