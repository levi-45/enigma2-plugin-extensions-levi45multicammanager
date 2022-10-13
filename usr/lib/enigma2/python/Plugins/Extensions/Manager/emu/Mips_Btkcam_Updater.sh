#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/btkcam
rm -R /usr/camscript/BtkCam-Mips_*.sh
###############################################################################
# Download and install Btkcam
cd /tmp 
set -e
wget "http://levi45.spdns.eu/Addons/Multicam/Mips/btkcam.tar.gz"

tar -xzf btkcam.tar.gz -C /
set +e
rm -f btkcam.tar.gz
chmod 777 -R /usr/camscript/BtkCam-Mips_*.sh
cd ..

sync
echo "#########################################################"
echo "#                             Levi45                    #"
echo "#########################################################"
echo "#               Btkcam INSTALLED SUCCESSFULLY           #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
