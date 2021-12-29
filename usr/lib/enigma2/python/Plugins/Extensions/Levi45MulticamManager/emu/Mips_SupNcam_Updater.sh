#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/supncam
rm -R /usr/camscript/SupNcam-Mips_*.sh
###############################################################################
# Download and install Supcam
cd /tmp 
set -e
wget "http://levi45.spdns.eu/Addons/Multicam/Mips/supncam.tar.gz"

tar -xzf supncam.tar.gz -C /
set +e
rm -f supncam.tar.gz
chmod 777 -R /usr/camscript/SupNcam-Mips_*.sh
cd ..

sync
echo "#########################################################"
echo "#                             Levi45                    #"
echo "#########################################################"
echo "#               Supcam INSTALLED SUCCESSFULLY           #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
