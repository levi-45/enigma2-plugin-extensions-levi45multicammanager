#!/bin/sh
#DESCRIPTION=This script created by Levi45\nInstall FULL CONFIG
###############################################################################
rm -R /etc/tuxbox/config
rm -R /etc/scam
rm -R /etc/CCcam.channelinfo
rm -R /etc/CCcam.providers
rm -R /etc/cs378x.cfg
rm -R /etc/ip2country.csv
rm -R /etc/multics.cfg
rm -R /etc/multics_bianca.css
rm -R /usr/keys
###############################################################################
# Download and install Config
PLUGIN_FOLDER=/usr/lib/enigma2/python/Plugins/Extensions/Manager/emu
    . $PLUGIN_FOLDER/functions.sh
download_file fullconfig.tar.gz
sync
echo "#########################################################"
echo "#                           Levi45                      #"
echo "#########################################################"
echo "#               Config INSTALLED SUCCESSFULLY           #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
