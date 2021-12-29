#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/scam
rm -R /usr/camscript/SCam-Mips_*.sh
###############################################################################
# Download and install Scam
cd /tmp 
set -e
wget "http://levi45.spdns.eu/Addons/Multicam/Mips/scam.tar.gz"

tar -xzf scam.tar.gz -C /
set +e
rm -f scam.tar.gz
chmod 777 -R /usr/camscript/SCam-Mips_*.sh
cd ..

sync
echo "#########################################################"
echo "#                             Levi45                    #"
echo "#########################################################"
echo "#              Scam INSTALLED SUCCESSFULLY              #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
