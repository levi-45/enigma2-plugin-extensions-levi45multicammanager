#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/oscamotr
rm -R /usr/camscript/OSicamPy3.10-Mips_*.sh
###############################################################################
# Download and install OSicamPy3.10
cd /tmp 
set -e
wget "http://levi45.spdns.eu/Addons/Multicam/Mips/oscamotr.tar.gz"

tar -xzf oscamotr.tar.gz -C /
set +e
rm -f oscamotr.tar.gz
chmod 777 -R /usr/camscript/OSicamPy3.10-Mips_*.sh
cd ..

sync
echo "#########################################################"
echo "#                             Levi45                    #"
echo "#########################################################"
echo "#              OSicamPy3.10 INSTALLED SUCCESSFULLY      #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
