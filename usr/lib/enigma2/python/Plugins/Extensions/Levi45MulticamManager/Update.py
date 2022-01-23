import os, re, sys
from twisted.web.client import downloadPage
PY3 = sys.version_info.major >= 3
print("Update.*")
def upd_done():        
    print( "In upd_done")
    xfile ='http://levi45.spdns.eu/Addons/Multicam/Levi45MulticamManager/Levi45MulticamManager.tar'
    print('xfile: ', xfile)
    if PY3:
        xfile = b"http://levi45.spdns.eu/Addons/Multicam/Levi45MulticamManager/Levi45MulticamManager.tar"
    print("Update.py not in PY3")
    fdest = "/tmp/Levi45MulticamManager.tar"
    print("upd_done xfile =", xfile)
    downloadPage(xfile, fdest).addCallback(upd_last)

def upd_last(fplug): 
    cmd = "tar -xvf /tmp/Levi45MulticamManager.tar -C /"
    print( "cmd A =", cmd)
    os.system(cmd)
    pass

