#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/multics
rm -R /usr/camscript/MultiCS-Mips_*.sh
###############################################################################
# Download and install MultiCS
cd /tmp 
set -e
wget "http://levi45.spdns.eu/Addons/Multicam/Mips/multics.tar.gz"

tar -xzf multics.tar.gz -C /
set +e
rm -f multics.tar.gz
chmod 777 -R /usr/camscript/MultiCS-Mips_*.sh
cd ..

sync
echo "#########################################################"
echo "#                             Levi45                    #"
echo "#########################################################"
echo "#             MultiCS INSTALLED SUCCESSFULLY            #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
