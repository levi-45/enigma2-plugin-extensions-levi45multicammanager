#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/oscampw
rm -R /usr/camscript/OSCamPw-Mips_*.sh
###############################################################################
# Download and install OscamPw
cd /tmp 
set -e
wget "http://levi45.spdns.eu/Addons/Multicam/Mips/oscampw.tar.gz"

tar -xzf oscampw.tar.gz -C /
set +e
rm -f oscampw.tar.gz
chmod 777 -R /usr/camscript/OSCamPw-Mips_*.sh
cd ..

sync
echo "#########################################################"
echo "#                             Levi45                    #"
echo "#########################################################"
echo "#              OscamPw INSTALLED SUCCESSFULLY           #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
