#!/bin/sh
#DESCRIPTION=This script created by Levi45\nInstall *.tar - *.gz from /tmp
###############################################################################
# Installin File
cd /tmp 
tar -xzf *.tar.gz -C /
rm -f *.tar.gz
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
