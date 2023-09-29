#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/tntoscam
rm -R /usr/camscript/TntOSCam-Arm_*.sh
###############################################################################
# Download and install TntOscam
PLUGIN_FOLDER=/usr/lib/enigma2/python/Plugins/Extensions/Manager/emu
    . $PLUGIN_FOLDER/functions.sh
download_file tntoscam.tar.gz
chmod a+x -R /usr/camscript/*.sh
sync
echo "#########################################################"
echo "#                           Levi45                      #"
echo "#########################################################"
echo "#             TntOscam INSTALLED SUCCESSFULLY           #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
