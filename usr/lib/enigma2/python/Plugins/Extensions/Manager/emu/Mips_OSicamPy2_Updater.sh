#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/oscampw
rm -R /usr/camscript/OSicamPy2-Mips_*.sh
###############################################################################
# Download and install OSicamPy2
cd /tmp 
set -e
wget "http://levi45.spdns.eu/Addons/Multicam/Mips/oscampw.tar.gz"

tar -xzf oscampw.tar.gz -C /
set +e
rm -f oscampw.tar.gz
chmod 777 -R /usr/camscript/OSicamPy2-Mips_*.sh
cd ..

sync
echo "#########################################################"
echo "#                             Levi45                    #"
echo "#########################################################"
echo "#              OSicamPy2 INSTALLED SUCCESSFULLY         #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
