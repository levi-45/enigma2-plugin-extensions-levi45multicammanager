#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/oscamde
rm -R /usr/camscript/OSCamDe-Mips_*.sh
###############################################################################
# Download and install OSCamDe
cd /tmp 
set -e
wget "http://levi45.spdns.eu/Addons/Multicam/Mips/oscamde.tar.gz"

tar -xzf oscamde.tar.gz -C /
set +e
rm -f oscamde.tar.gz
chmod 777 -R /usr/camscript/OSCamDe-Mips_*.sh
cd ..

sync
echo "#########################################################"
echo "#                             Levi45                    #"
echo "#########################################################"
echo "#              OSCamDe INSTALLED SUCCESSFULLY           #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
