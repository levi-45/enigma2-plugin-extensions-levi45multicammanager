#!/bin/sh
#DESCRIPTION=This script created by Levi45
###############################################################################
rm -R /usr/bin/scam
rm -R /usr/camscript/SCam-*.sh
###############################################################################
# Download and install Scam
PLUGIN_FOLDER=/usr/lib/enigma2/python/Plugins/Extensions/Manager/emu
    . $PLUGIN_FOLDER/functions.sh
download_file scam.tar.gz
chmod a+x -R /usr/camscript/*.sh
sync
echo "#########################################################"
echo "#                             Levi45                    #"
echo "#########################################################"
echo "#              Scam INSTALLED SUCCESSFULLY              #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
