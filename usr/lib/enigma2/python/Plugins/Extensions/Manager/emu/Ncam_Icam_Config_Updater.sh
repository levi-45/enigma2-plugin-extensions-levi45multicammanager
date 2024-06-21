#!/bin/sh
#DESCRIPTION=This script created by Levi45\nInstall Ncam Icam Config
###############################################################################
rm -R /etc/tuxbox/config/ncam.*
###############################################################################
# Download and install Config
PLUGIN_FOLDER=/usr/lib/enigma2/python/Plugins/Extensions/Manager/emu
    . $PLUGIN_FOLDER/functions.sh
download_file ncamicamconfig.tar.gz
sync
echo "#########################################################"
echo "#                           Levi45                      #"
echo "#########################################################"
echo "#               Config INSTALLED SUCCESSFULLY           #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
