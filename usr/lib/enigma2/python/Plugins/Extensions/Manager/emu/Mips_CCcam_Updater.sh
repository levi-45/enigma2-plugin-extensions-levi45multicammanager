#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/cccam
rm -R /usr/camscript/CCcam-Mips_*.sh
###############################################################################
# Download and install CCcam
cd /tmp 
set -e
wget "http://levi45.spdns.eu/Addons/Multicam/Mips/cccam.tar.gz"

tar -xzf cccam.tar.gz -C /
set +e
rm -f cccam.tar.gz
chmod 777 -R /usr/camscript/CCcam-Mips_*.sh
cd ..

sync
echo "#########################################################"
echo "#                             Levi45                    #"
echo "#########################################################"
echo "#               CCcam INSTALLED SUCCESSFULLY            #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
