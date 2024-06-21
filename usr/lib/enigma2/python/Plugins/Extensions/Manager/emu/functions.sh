#!/bin/sh
#DESCRIPTION=This script created by Levi45\nInstall Update to /tmp
#by acypaczom 2023

download_file ()
{
z=$(uname -m)
case  $z  in
    *"arm"*)
	z=arm
	;;
    *"mips"*)
	z=mips
	;;
    *"aarch"*)
	z=aarch64
	;;
    *)
	echo "Unsupported platform"
	exit 1
	;;
esac
z=${z^}
FILE_TO_DOWNLOAD="http://levi45.spdns.eu/Addons/Multicam/$z/$1"
which curl 1>/dev/null 2>&1
if [ "$?" == "0" ] ; then
    curl --silent  --output /tmp/$(basename $FILE_TO_DOWNLOAD)  $FILE_TO_DOWNLOAD
else
    wget  --quiet --no-check-certificate  $FILE_TO_DOWNLOAD  --output-document=/tmp/$(basename $FILE_TO_DOWNLOAD)
fi
FILE_TO_DOWNLOAD="/tmp/$(basename $FILE_TO_DOWNLOAD)"
tar -xzf $FILE_TO_DOWNLOAD -C /
rm -f $FILE_TO_DOWNLOAD
}

