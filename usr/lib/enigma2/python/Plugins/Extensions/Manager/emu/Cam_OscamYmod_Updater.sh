#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/oscamymod
rm -R /usr/camscript/OSCamYmod-*.sh
###############################################################################
# Download and install OscamYmod
PLUGIN_FOLDER=/usr/lib/enigma2/python/Plugins/Extensions/Manager/emu
    . $PLUGIN_FOLDER/functions.sh
download_file oscamymod.tar.gz
chmod a+x -R /usr/camscript/*.sh
sync
echo "#########################################################"
echo "#                           Levi45                      #"
echo "#########################################################"
echo "#            OscamYmod INSTALLED SUCCESSFULLY           #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
