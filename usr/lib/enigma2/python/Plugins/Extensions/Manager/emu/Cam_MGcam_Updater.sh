#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/mgcam
rm -R /usr/camscript/MgCam-*.sh
###############################################################################
# Download and install MGcam
PLUGIN_FOLDER=/usr/lib/enigma2/python/Plugins/Extensions/Manager/emu
    . $PLUGIN_FOLDER/functions.sh
download_file mgcam.tar.gz
chmod a+x -R /usr/camscript/*.sh
sync
echo "#########################################################"
echo "#                           Levi45                      #"
echo "#########################################################"
echo "#               MGcam  INSTALLED SUCCESSFULLY           #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
