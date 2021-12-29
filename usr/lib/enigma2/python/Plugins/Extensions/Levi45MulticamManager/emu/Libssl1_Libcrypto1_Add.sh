#!/bin/sh
#DESCRIPTION=Thanks @READ
#################################################################################
LINE="======================================================================="
######### checking Package: libssl & libcrypto ###########
if [ -f /etc/opkg/opkg.conf ] ; then
    images="OE2.0 IMAGES:"
    lib_files="/var/lib/opkg/status"
    list_files="/var/lib/opkg/info"
else
    echo "Sorry, your device does not have the proper Packages :("
fi
usrlibpath="/usr/lib/"
libpath="/lib/"
############################## libssl ####################
if grep -qs 'Package: libssl1.1' cat $lib_files ; then
    echo "$images libssl1.1"
    ln -s libssl.so.1.1 $usrlibpath/libssl.so.1.0.0 > /dev/null 2>&1
    ln -s libssl.so.1.1 $usrlibpath/libssl.so.0.9.8 > /dev/null 2>&1
    ln -s libssl.so.1.1 $usrlibpath/libssl.so.0.9.7 > /dev/null 2>&1
    ln -s $usrlibpath/libssl.so.1.1 $libpath/libssl.so.1.0.0 > /dev/null 2>&1
    ln -s $usrlibpath/libssl.so.1.1 $libpath/libssl.so.0.9.8 > /dev/null 2>&1
    ln -s $usrlibpath/libssl.so.1.1 $libpath/libssl.so.0.9.7 > /dev/null 2>&1
elif grep -qs 'Package: libssl1.0.2' cat $lib_files ; then
    echo "$images libssl.so.1.0.2"
    ln -s libssl.so.1.0.2 $usrlibpath/libssl.so.1.0.0 > /dev/null 2>&1
    ln -s libssl.so.1.0.2 $usrlibpath/libssl.so.0.9.8 > /dev/null 2>&1
    ln -s libssl.so.1.0.2 $usrlibpath/libssl.so.0.9.7 > /dev/null 2>&1
    ln -s $usrlibpath/libssl.so.1.0.2 $libpath/libssl.so.1.0.0 > /dev/null 2>&1
    ln -s $usrlibpath/libssl.so.1.0.2 $libpath/libssl.so.0.9.8 > /dev/null 2>&1
    ln -s $usrlibpath/libssl.so.1.0.2 $libpath/libssl.so.0.9.7 > /dev/null 2>&1
elif grep -qs 'Package: libssl1.0.0' cat $lib_files ; then
    echo "$images libssl.so.1.0.0"
    ln -s libssl.so.1.0.0 $usrlibpath/libssl.so.0.9.8 > /dev/null 2>&1
    ln -s libssl.so.1.0.0 $usrlibpath/libssl.so.0.9.7 > /dev/null 2>&1
    ln -s $usrlibpath/libssl.so.1.0.0 $libpath/libssl.so.0.9.8 > /dev/null 2>&1
    ln -s $usrlibpath/libssl.so.1.0.0 $libpath/libssl.so.0.9.7 > /dev/null 2>&1
elif grep -qs 'Package: libssl0.9.8' cat $lib_files ; then
    echo "$images libssl.so.0.9.8"
    ln -s libssl.so.0.9.8 $usrlibpath/libssl.so.0.9.7 > /dev/null 2>&1
    ln -s libssl.so.0.9.8 $usrlibpath/libssl.so.1.0.0 > /dev/null 2>&1
    ln -s $usrlibpath/libssl.so.0.9.8 $libpath/libssl.so.0.9.7 > /dev/null 2>&1
    ln -s $usrlibpath/libssl.so.0.9.8 $libpath/libssl.so.1.0.0 > /dev/null 2>&1
else ## Try to Download libssl from feed
    if [ -n "$(opkg list | grep libssl1.1)" ]; then
        echo "install libssl1.1"
        if [ -f /etc/apt/apt.conf ] ; then
            apt-get install --reinstall libssl1.1 > /dev/null 2>&1
            ln -s libssl.so.1.1 $usrlibpath/libssl.so.1.0.0 > /dev/null 2>&1
            ln -s libssl.so.1.1 $usrlibpath/libssl.so.0.9.8 > /dev/null 2>&1
            ln -s llibssl.so.1.1 $usrlibpath/libssl.so.0.9.7 > /dev/null 2>&1
            ln -s $usrlibpath/libssl.so.1.1 $libpath/libssl.so.1.0.0 > /dev/null 2>&1
            ln -s $usrlibpath/libssl.so.1.1 $libpath/libssl.so.0.9.8 > /dev/null 2>&1
            ln -s $usrlibpath/libssl.so.1.1 $libpath/libssl.so.0.9.7 > /dev/null 2>&1
        elif [ -f /etc/opkg/opkg.conf ] ; then
            opkg install --force-overwrite --force-depends libssl1.1 > /dev/null
            ln -s libssl.so.1.1 $usrlibpath/libssl.so.1.0.0 > /dev/null 2>&1
            ln -s libssl.so.1.1 $usrlibpath/libssl.so.0.9.8 > /dev/null 2>&1
            ln -s libssl.so.1.1 $usrlibpath/libssl.so.0.9.7 > /dev/null 2>&1
            ln -s $usrlibpath/libssl.so.1.1 $libpath/libssl.so.1.0.0 > /dev/null 2>&1
            ln -s $usrlibpath/libssl.so.1.1 $libpath/libssl.so.0.9.8 > /dev/null 2>&1
            ln -s $usrlibpath/libssl.so.1.1 $libpath/libssl.so.0.9.7 > /dev/null 2>&1
        fi
    elif [ -n "$(opkg list | grep libssl1.0.2)" ]; then
        echo "install libssl1.0.2"
        if [ -f /etc/apt/apt.conf ] ; then
            apt-get install --reinstall libssl1.0.2 > /dev/null 2>&1
            ln -s libssl.so.1.0.2 $usrlibpath/libssl.so.1.0.0 > /dev/null 2>&1
            ln -s libssl.so.1.0.2 $usrlibpath/libssl.so.0.9.8 > /dev/null 2>&1
            ln -s libssl.so.1.0.2 $usrlibpath/libssl.so.0.9.7 > /dev/null 2>&1
            ln -s $usrlibpath/libssl.so.1.0.2 $libpath/libssl.so.1.0.0 > /dev/null 2>&1
            ln -s $usrlibpath/libssl.so.1.0.2 $libpath/libssl.so.0.9.8 > /dev/null 2>&1
            ln -s $usrlibpath/libssl.so.1.0.2 $libpath/libssl.so.0.9.7 > /dev/null 2>&1
        elif [ -f /etc/opkg/opkg.conf ] ; then
            opkg install --force-overwrite --force-depends libssl1.0.2 > /dev/null
            ln -s libssl.so.1.0.2 $usrlibpath/libssl.so.1.0.0 > /dev/null 2>&1
            ln -s libssl.so.1.0.2 $usrlibpath/libssl.so.0.9.8 > /dev/null 2>&1
            ln -s libssl.so.1.0.2 $usrlibpath/libssl.so.0.9.7 > /dev/null 2>&1
            ln -s $usrlibpath/libssl.so.1.0.2 $libpath/libssl.so.1.0.0 > /dev/null 2>&1
            ln -s $usrlibpath/libssl.so.1.0.2 $libpath/libssl.so.0.9.8 > /dev/null 2>&1
            ln -s $usrlibpath/libssl.so.1.0.2 $libpath/libssl.so.0.9.7 > /dev/null 2>&1
        fi
    elif [ -n "$(opkg list | grep libssl1.0.0)" ]; then
        echo "install libssl1.0.0"
        if [ -f /etc/apt/apt.conf ] ; then
            apt-get install --reinstall libssl1.0.0 > /dev/null 2>&1
            ln -s libssl.so.1.0.0 $usrlibpath/libssl.so.0.9.8 > /dev/null 2>&1
            ln -s libssl.so.1.0.0 $usrlibpath/libssl.so.0.9.7 > /dev/null 2>&1
            ln -s $usrlibpath/libssl.so.1.0.0 $libpath/libssl.so.0.9.8 > /dev/null 2>&1
            ln -s $usrlibpath/libssl.so.1.0.0 $libpath/libssl.so.0.9.7 > /dev/null 2>&1
        elif [ -f /etc/opkg/opkg.conf ] ; then
            opkg install --force-overwrite --force-depends libssl1.0.0 > /dev/null
            ln -s libssl.so.1.0.0 $usrlibpath/libssl.so.0.9.8 > /dev/null 2>&1
            ln -s libssl.so.1.0.0 $usrlibpath/libssl.so.0.9.7 > /dev/null 2>&1
            ln -s $usrlibpath/libssl.so.1.0.0 $libpath/libssl.so.0.9.8 > /dev/null 2>&1
            ln -s $usrlibpath/libssl.so.1.0.0 $libpath/libssl.so.0.9.7 > /dev/null 2>&1
        fi
    elif [ -n "$(opkg list | grep libssl0.9.8)" ]; then
        echo "install libssl0.9.8"
        if [ -f /etc/apt/apt.conf ] ; then
            apt-get install --reinstall libssl0.9.8 > /dev/null 2>&1
            ln -s libssl.so.0.9.8 $usrlibpath/libssl.so.0.9.7 > /dev/null 2>&1
            ln -s libssl.so.0.9.8 $usrlibpath/libssl.so.1.0.0 > /dev/null 2>&1
            ln -s $usrlibpath/libssl.so.0.9.8 $libpath/libssl.so.0.9.7 > /dev/null 2>&1
            ln -s $usrlibpath/libssl.so.0.9.8 $libpath/libssl.so.1.0.0 > /dev/null 2>&1
        elif [ -f /etc/opkg/opkg.conf ] ; then
            opkg install --force-overwrite --force-depends libssl0.9.8 > /dev/null 2>&1
            ln -s libssl.so.0.9.8 $usrlibpath/libssl.so.0.9.7 > /dev/null 2>&1
            ln -s libssl.so.0.9.8 $usrlibpath/libssl.so.1.0.0 > /dev/null 2>&1
            ln -s $usrlibpath/libssl.so.0.9.8 $libpath/libssl.so.0.9.7 > /dev/null 2>&1
            ln -s $usrlibpath/libssl.so.0.9.8 $libpath/libssl.so.1.0.0 > /dev/null 2>&1
        fi
    else
        echo $LINE
        echo "ERROR: The libsslx.x.x file could not be loaded from the repository."
        echo $LINE
        exit 1
    fi
fi
############################## libcrypto ####################
if grep -qs 'Package: libcrypto1.1' cat $lib_files ; then
    echo "$images libcrypto1.1"
    ln -s libcrypto.so.1.1 $usrlibpath/libcrypto.so.1.0.0 > /dev/null 2>&1
    ln -s libcrypto.so.1.1 $usrlibpath/libcrypto.so.0.9.8 > /dev/null 2>&1
    ln -s libcrypto.so.1.1 $usrlibpath/libcrypto.so.0.9.7 > /dev/null 2>&1
    ln -s $usrlibpath/libcrypto.so.1.1 $libpath/libcrypto.so.1.0.0 > /dev/null 2>&1
    ln -s $usrlibpath/libcrypto.so.1.1 $libpath/libcrypto.so.0.9.8 > /dev/null 2>&1
    ln -s $usrlibpath/libcrypto.so.1.1 $libpath/libcrypto.so.0.9.7 > /dev/null 2>&1
elif grep -qs 'Package: libcrypto1.0.2' cat $lib_files ; then
    echo "$images libcrypto.so.1.0.2"
    ln -s libcrypto.so.1.0.2 $usrlibpath/libcrypto.so.1.0.0 > /dev/null 2>&1
    ln -s libcrypto.so.1.0.2 $usrlibpath/libcrypto.so.0.9.8 > /dev/null 2>&1
    ln -s libcrypto.so.1.0.2 $usrlibpath/libcrypto.so.0.9.7 > /dev/null 2>&1
    ln -s $usrlibpath/libcrypto.so.1.0.2 $libpath/libcrypto.so.1.0.0 > /dev/null 2>&1
    ln -s $usrlibpath/libcrypto.so.1.0.2 $libpath/libcrypto.so.0.9.8 > /dev/null 2>&1
    ln -s $usrlibpath/libcrypto.so.1.0.2 $libpath/libcrypto.so.0.9.7 > /dev/null 2>&1
elif grep -qs 'Package: libcrypto1.0.0' cat $lib_files ; then
    echo "$images libcrypto.so.1.0.0"
    ln -s libcrypto.so.1.0.0 $usrlibpath/libcrypto.so.0.9.8 > /dev/null 2>&1
    ln -s libcrypto.so.1.0.0 $usrlibpath/libcrypto.so.0.9.7 > /dev/null 2>&1
    ln -s $usrlibpath/libcrypto.so.1.0.0 $libpath/libcrypto.so.0.9.8 > /dev/null 2>&1
    ln -s $usrlibpath/libcrypto.so.1.0.0 $libpath/libcrypto.so.0.9.7 > /dev/null 2>&1
elif grep -qs 'Package: libcrypto0.9.8' cat $lib_files ; then
    echo "$images libcrypto.so.0.9.8"
    ln -s libcrypto.so.0.9.8 $usrlibpath/libcrypto.so.0.9.7 > /dev/null 2>&1
    ln -s libcrypto.so.0.9.8 $usrlibpath/libcrypto.so.1.0.0 > /dev/null 2>&1
    ln -s $usrlibpath/libcrypto.so.0.9.8 $libpath/libcrypto.so.0.9.7 > /dev/null 2>&1
    ln -s $usrlibpath/libcrypto.so.0.9.8 $libpath/libcrypto.so.1.0.0 > /dev/null 2>&1
else ## Try to Download libcrypto from feed
    if [ -n "$(opkg list | grep libcrypto1.1)" ]; then
        echo "install libcrypto1.1"
        if [ -f /etc/apt/apt.conf ] ; then
            apt-get install --reinstall libcrypto1.1 > /dev/null 2>&1
            ln -s libcrypto.so.1.1 $usrlibpath/libcrypto.so.1.0.0 > /dev/null 2>&1
            ln -s libcrypto.so.1.1 $usrlibpath/libcrypto.so.0.9.8 > /dev/null 2>&1
            ln -s libcrypto.so.1.1 $usrlibpath/libcrypto.so.0.9.7 > /dev/null 2>&1
            ln -s $usrlibpath/libcrypto.so.1.1 $libpath/libcrypto.so.1.0.0 > /dev/null 2>&1
            ln -s $usrlibpath/libcrypto.so.1.1 $libpath/libcrypto.so.0.9.8 > /dev/null 2>&1
            ln -s $usrlibpath/libcrypto.so.1.1 $libpath/libcrypto.so.0.9.7 > /dev/null 2>&1
        elif [ -f /etc/opkg/opkg.conf ] ; then
            opkg install --force-overwrite --force-depends libcrypto1.1 > /dev/null
            ln -s libcrypto.so.1.1 $usrlibpath/libcrypto.so.1.0.0 > /dev/null 2>&1
            ln -s libcrypto.so.1.1 $usrlibpath/libcrypto.so.0.9.8 > /dev/null 2>&1
            ln -s libcrypto.so.1.1 $usrlibpath/libcrypto.so.0.9.7 > /dev/null 2>&1
            ln -s $usrlibpath/libcrypto.so.1.1 $libpath/libcrypto.so.1.0.0 > /dev/null 2>&1
            ln -s $usrlibpath/libcrypto.so.1.1 $libpath/libcrypto.so.0.9.8 > /dev/null 2>&1
            ln -s $usrlibpath/libcrypto.so.1.1 $libpath/libcrypto.so.0.9.7 > /dev/null 2>&1
        fi
    elif [ -n "$(opkg list | grep libcrypto1.0.2)" ]; then
        echo "install libcrypto1.0.2"
        if [ -f /etc/apt/apt.conf ] ; then
            apt-get install --reinstall libcrypto1.0.2 > /dev/null 2>&1
            ln -s libcrypto.so.1.0.2 $usrlibpath/libcrypto.so.1.0.0 > /dev/null 2>&1
            ln -s libcrypto.so.1.0.2 $usrlibpath/libcrypto.so.0.9.8 > /dev/null 2>&1
            ln -s libcrypto.so.1.0.2 $usrlibpath/libcrypto.so.0.9.7 > /dev/null 2>&1
            ln -s $usrlibpath/libcrypto.so.1.0.2 $libpath/libcrypto.so.1.0.0 > /dev/null 2>&1
            ln -s $usrlibpath/libcrypto.so.1.0.2 $libpath/libcrypto.so.0.9.8 > /dev/null 2>&1
            ln -s $usrlibpath/libcrypto.so.1.0.2 $libpath/libcrypto.so.0.9.7 > /dev/null 2>&1
        elif [ -f /etc/opkg/opkg.conf ] ; then
            opkg install --force-overwrite --force-depends libcrypto1.0.2 > /dev/null
            ln -s libcrypto.so.1.0.2 $usrlibpath/libcrypto.so.1.0.0 > /dev/null 2>&1
            ln -s libcrypto.so.1.0.2 $usrlibpath/libcrypto.so.0.9.8 > /dev/null 2>&1
            ln -s libcrypto.so.1.0.2 $usrlibpath/libcrypto.so.0.9.7 > /dev/null 2>&1
            ln -s $usrlibpath/libcrypto.so.1.0.2 $libpath/libcrypto.so.1.0.0 > /dev/null 2>&1
            ln -s $usrlibpath/libcrypto.so.1.0.2 $libpath/libcrypto.so.0.9.8 > /dev/null 2>&1
            ln -s $usrlibpath/libcrypto.so.1.0.2 $libpath/libcrypto.so.0.9.7 > /dev/null 2>&1
        fi
    elif [ -n "$(opkg list | grep libcrypto1.0.0)" ]; then
        echo "install libcrypto1.0.0"
        if [ -f /etc/apt/apt.conf ] ; then
            apt-get install --reinstall libcrypto1.0.0 > /dev/null 2>&1
            ln -s libcrypto.so.1.0.0 $usrlibpath/libcrypto.so.0.9.8 > /dev/null 2>&1
            ln -s libcrypto.so.1.0.0 $usrlibpath/libcrypto.so.0.9.7 > /dev/null 2>&1
            ln -s $usrlibpath/libcrypto.so.1.0.0 $libpath/libcrypto.so.0.9.8 > /dev/null 2>&1
            ln -s $usrlibpath/libcrypto.so.1.0.0 $libpath/libcrypto.so.0.9.7 > /dev/null 2>&1
        elif [ -f /etc/opkg/opkg.conf ] ; then
            opkg install --force-overwrite --force-depends libcrypto1.0.0 > /dev/null
            ln -s libcrypto.so.1.0.0 $usrlibpath/libcrypto.so.0.9.8 > /dev/null 2>&1
            ln -s libcrypto.so.1.0.0 $usrlibpath/libcrypto.so.0.9.7 > /dev/null 2>&1
            ln -s $usrlibpath/libcrypto.so.1.0.0 $libpath/libcrypto.so.0.9.8 > /dev/null 2>&1
            ln -s $usrlibpath/libcrypto.so.1.0.0 $libpath/libcrypto.so.0.9.7 > /dev/null 2>&1
        fi
    elif [ -n "$(opkg list | grep libcrypto0.9.8)" ]; then
        echo "install libcrypto0.9.8"
        if [ -f /etc/apt/apt.conf ] ; then
            apt-get install --reinstall libcrypto0.9.8 > /dev/null 2>&1
            ln -s libcrypto.so.0.9.8 $usrlibpath/libcrypto.so.0.9.7 > /dev/null 2>&1
            ln -s libcrypto.so.0.9.8 $usrlibpath/libcrypto.so.1.0.0 > /dev/null 2>&1
            ln -s $usrlibpath/libcrypto.so.0.9.8 $libpath/libcrypto.so.0.9.7 > /dev/null 2>&1
            ln -s $usrlibpath/libcrypto.so.0.9.8 $libpath/libcrypto.so.1.0.0 > /dev/null 2>&1
        elif [ -f /etc/opkg/opkg.conf ] ; then
            opkg install --force-overwrite --force-depends libcrypto0.9.8 > /dev/null 2>&1
            ln -s libcrypto.so.0.9.8 $usrlibpath/libcrypto.so.0.9.7 > /dev/null 2>&1
            ln -s libcrypto.so.0.9.8 $usrlibpath/libcrypto.so.1.0.0 > /dev/null 2>&1
            ln -s $usrlibpath/libcrypto.so.0.9.8 $libpath/libcrypto.so.0.9.7 > /dev/null 2>&1
            ln -s $usrlibpath/libcrypto.so.0.9.8 $libpath/libcrypto.so.1.0.0 > /dev/null 2>&1
        fi
    else
        echo $LINE
        echo "ERROR: The libcryptox.x.x file could not be loaded from the repository."
        echo $LINE
        exit 1
    fi
fi

echo "#########################################################"
echo "#                           Levi45                      #"
echo "#########################################################"
echo "#               Lib Files INSTALLED SUCCESSFULLY        #"
echo "#########################################################"
echo "#                    SATELLITE-FORUM.COM                #"
echo "#########################################################"
exit 0
