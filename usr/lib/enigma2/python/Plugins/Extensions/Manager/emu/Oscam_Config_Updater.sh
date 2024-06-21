#!/bin/sh
#DESCRIPTION=This script created by Levi45\nInstall Oscam Config
###############################################################################
rm -R /etc/tuxbox/config/oscam.*
###############################################################################
# Download and install Config
PLUGIN_FOLDER=/usr/lib/enigma2/python/Plugins/Extensions/Manager/emu
    . $PLUGIN_FOLDER/functions.sh
download_file oscamconfig.tar.gz
sync
echo "#########################################################"
echo "#                           Levi45                      #"
echo "#########################################################"
echo "#               Config INSTALLED SUCCESSFULLY           #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
