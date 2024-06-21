#!/bin/sh
#DESCRIPTION=This script created by Levi45\nInstall Icam Config
###############################################################################
rm -R /etc/tuxbox/config/Oscamicam
###############################################################################
# Download and install Config
PLUGIN_FOLDER=/usr/lib/enigma2/python/Plugins/Extensions/Manager/emu
    . $PLUGIN_FOLDER/functions.sh
download_file oscamicamconfig.tar.gz
sync
echo "#########################################################"
echo "#                           Levi45                      #"
echo "#########################################################"
echo "#               Config INSTALLED SUCCESSFULLY           #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
