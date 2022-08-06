import os, re, sys
from twisted.web.client import downloadPage

PY3 = sys.version_info.major >= 3

from os.path import exists as file_exists
print("Update.*")
oldplug = '/usr/lib/enigma2/python/Plugins/Extensions/Levi45MulticamManager'

if file_exists(oldplug):
    cmd = "rm -rf %s > /dev/null 2>&1" %oldplug
    print( "cmd A =", cmd)
    os.system(cmd)

def upd_done():
    print( "In upd_done")
    xfile ='http://levi45.spdns.eu/Addons/Multicam/Levi45MulticamManager/Manager.tar'
    print('xfile: ', xfile)
    if PY3:
        xfile = b"http://levi45.spdns.eu/Addons/Multicam/Levi45MulticamManager/Manager.tar"
    print("Update.py not in PY3")
    fdest = "/tmp/Manager.tar"
    print("upd_done xfile =", xfile)
    downloadPage(xfile, fdest).addCallback(upd_last)



def upd_last(fplug): 
    cmd = "tar -xvf /tmp/Manager.tar -C /"
    print( "cmd A =", cmd)
    os.system(cmd)
    pass
    

