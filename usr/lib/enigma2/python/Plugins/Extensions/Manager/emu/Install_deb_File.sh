#!/bin/sh
#DESCRIPTION=This script created by Levi45\nInstall *.deb from /tmp
###############################################################################
# Installin File
cd /tmp 
dpkg -i --force-overwrite --force-downgrade /tmp/*.deb
rm -f *.deb
cd ..

sync
echo "#########################################################"
echo "#                           Levi45                      #"
echo "#########################################################"
echo "#                 FILE INSTALLED SUCCESSFULLY           #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
