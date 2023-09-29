#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/revoscam
rm -R /usr/camscript/RevOscam-*.sh
###############################################################################
# Download and install Revcam
PLUGIN_FOLDER=/usr/lib/enigma2/python/Plugins/Extensions/Manager/emu
    . $PLUGIN_FOLDER/functions.sh
download_file revoscam.tar.gz
chmod a+x -R /usr/camscript/*.sh
sync
echo "#########################################################"
echo "#                           Levi45                      #"
echo "#########################################################"
echo "#               Revcam INSTALLED SUCCESSFULLY           #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
