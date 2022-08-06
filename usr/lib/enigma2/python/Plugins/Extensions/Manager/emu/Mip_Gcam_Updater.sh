#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/gcam
rm -R /usr/camscript/GCam-Mips_*.sh
###############################################################################
# Download and install Gcam
cd /tmp 
set -e
wget "http://levi45.spdns.eu/Addons/Multicam/Mips/gcam.tar.gz"

tar -xzf gcam.tar.gz -C /
set +e
rm -f gcam.tar.gz
chmod 777 -R /usr/camscript/GCam-Mips_*.sh
cd ..

sync
echo "#########################################################"
echo "#                             Levi45                    #"
echo "#########################################################"
echo "#               Gcam INSTALLED SUCCESSFULLY             #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
