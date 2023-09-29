#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/btkcam
rm -R /usr/camscript/BtkCam-*.sh
###############################################################################
# Download and install Btkcam
PLUGIN_FOLDER=/usr/lib/enigma2/python/Plugins/Extensions/Manager/emu
    . $PLUGIN_FOLDER/functions.sh
download_file btkcam.tar.gz
chmod a+x -R /usr/camscript/*.sh
sync
echo "#########################################################"
echo "#                             Levi45                    #"
echo "#########################################################"
echo "#               Btkcam INSTALLED SUCCESSFULLY           #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
