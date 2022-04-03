#lululla 20/03/2022
from Components.ActionMap import ActionMap
from Components.MenuList import MenuList
from os import listdir
from Plugins.Plugin import PluginDescriptor
from Screens.Console import Console
from Screens.Screen import Screen
import os
import sys
plugin_foo = os.path.dirname(sys.modules[__name__].__file__)
emu_plugin = plugin_foo + '/emu/'
name_plugemu = 'Levi45 Emu Keys V.9.4'

from Components.MultiContent import MultiContentEntryText
from enigma import eListboxPythonMultiContent
from enigma import gFont

def getDesktopSize():
    from enigma import getDesktop
    s = getDesktop(0).size()
    return (s.width(), s.height())

def isFHD():
    desktopSize = getDesktopSize()
    return desktopSize[0] == 1920

def ulistEntry(download):
    res = [download]
    white = 16777215
    blue = 79488
    col = 16777215
    if isFHD():
        res.append(MultiContentEntryText(pos=(0, 0), size=(1200, 50), text=download, color=col, color_sel=white, backcolor_sel=blue))
    else:
        res.append(MultiContentEntryText(pos=(0, 0), size=(1000, 40), text=download, color=col, color_sel=white, backcolor_sel=blue))
    return res

def ulistx(data, list):
    icount = 0
    mlist = []
    for line in data:
        name = data[icount]
        mlist.append(ulistEntry(name))
        icount = icount + 1
    list.setList(mlist)

class M3UList(MenuList):
    def __init__(self, list):
        MenuList.__init__(self, list, False, eListboxPythonMultiContent)

        if isFHD():
            self.l.setItemHeight(50)
            self.l.setFont(0, gFont("Regular", 32))
        else:
            self.l.setItemHeight(40)
            self.l.setFont(0, gFont("Regular", 24))


class Levi45EmuKeysUpdater(Screen):
    if os.path.exists('/var/lib/dpkg/status'):
        skin = '\n        <screen name="Levi45 EmuKeys Updater" position="center,center" size="1280,720" title="Levi45 EmuKeys Updater" flags="wfNoBorder" backgroundColor="transparent">\n        <!-- /*ClockWidget-->\n        <eLabel position="264,51" zPosition="-1" size="340,320" backgroundColor="background" transparent="0" foregroundColor="background" />\n        <!-- /*ClockWidget-->\n        <widget source="global.CurrentTime" render="Label" position="436,411" size="187,80" font="Regular; 60" halign="left" backgroundColor="background" transparent="1" valign="top" foregroundColor="white">\n        <convert type="ClockToText">Default</convert>\n        </widget>\n        <widget source="global.CurrentTime" render="Label" position="290,450" size="148,29" font="Regular; 19" halign="right" backgroundColor="background" foregroundColor="white" transparent="1">\n        <convert type="ClockToText">Format:%e. %b</convert>\n        </widget>\n        <widget source="global.CurrentTime" render="Label" position="313,420" size="125,30" font="Regular; 19" halign="right" backgroundColor="background" foregroundColor="white" transparent="1">\n        <convert type="ClockToText">Format:%A</convert>\n        </widget>\n        <eLabel position="265,410" zPosition="-1" size="340,70" backgroundColor="background" transparent="0" foregroundColor="background" />\n        <!--ClockWidget */-->\n        <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Levi45MulticamManager/res/pics/hd/mcmaneger.png" transparent="1" position="310,85" size="256,256" alphatest="blend" />\n        <eLabel name="" position="628,50" zPosition="-11" size="446,432" backgroundColor="background" foregroundColor="background" />\n        <widget name="list" itemHeight="40" position="636,60" size="429,411" zPosition="1" scrollbarMode="showOnDemand" />\n         </screen>\n         '
    else:
        skin = '\n        <screen name="Levi45 EmuKeys Updater" position="center,center" size="1280,720" title="Levi45 EmuKeys Updater" flags="wfNoBorder" backgroundColor="transparent">\n        <!-- /*ClockWidget-->\n        <eLabel position="264,51" zPosition="-1" size="340,320" backgroundColor="background" transparent="0" foregroundColor="background" />\n        <!-- /*ClockWidget-->\n        <widget source="global.CurrentTime" render="Label" position="432,410" size="188,80" font="Regular; 60" halign="left" backgroundColor="background" transparent="1" valign="top" foregroundColor="white">\n        <convert type="ClockToText">Default</convert>\n        </widget>\n        <widget source="global.CurrentTime" render="Label" position="290,450" size="148,29" font="Regular; 19" halign="right" backgroundColor="background" foregroundColor="white" transparent="1">\n        <convert type="ClockToText">Format:%e. %b</convert>\n        </widget>\n        <widget source="global.CurrentTime" render="Label" position="313,420" size="125,30" font="Regular; 19" halign="right" backgroundColor="background" foregroundColor="white" transparent="1">\n        <convert type="ClockToText">Format:%A</convert>\n        </widget>\n        <eLabel position="265,410" zPosition="-1" size="340,70" backgroundColor="background" transparent="0" foregroundColor="background" />\n        <!--ClockWidget */-->\n        <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Levi45MulticamManager/res/pics/hd/mcmaneger.png" transparent="1" position="310,85" size="256,256" alphatest="blend" />\n        <eLabel name="" position="628,50" zPosition="-11" size="446,432" backgroundColor="background" foregroundColor="background" />\n        <widget name="list" itemHeight="50" font="Regular;28" position="636,60" size="429,411" zPosition="1" scrollbarMode="showOnDemand" />\n         </screen>\t\t\n         '

    def __init__(self, session, args = None):
        Screen.__init__(self, session)
        self.session = session
        self['list'] = M3UList([])
        self['actions'] = ActionMap(['OkCancelActions'], {'ok': self.run,
         'cancel': self.close}, -1)
        self.onLayoutFinish.append(self.loadScriptList)

    def loadScriptList(self):
        self.names = []
        self.urls = []
        for root, dirs, files in os.walk(emu_plugin):
            files.sort()
            for name in files:
                if ".sh" not in name:
                    continue
                url = name
                name = name.replace('.sh', '').replace('_',' ').upper()
                self.names.append(name)
                self.urls.append(url)
        ulistx(self.names, self["list"])

    def run(self):
        idx = self["list"].getSelectionIndex()
        if idx == -1 or idx ==None:
            return
        else:
            try:
                name = self.names[idx]
                dom = emu_plugin + self.urls[idx]
                print('dom -- ' , dom)
                from os import access, X_OK, chmod
                if not access(dom, X_OK):
                    chmod(dom, 0o0755)
                self.session.open(Console, name, cmdlist=[dom])
            except Exception as ex:
                print('error exception: ', str(ex))

def main2(session, **kwargs):
    session.open(Levi45EmuKeysUpdater)


def menu(menuid, **kwargs):
    if menuid == 'mainmenu':
        return [('Levi45 Emu Keys Updater',
          main,
          'Levi45 Emu Keys Updater',
          44)]
    return []


def Plugins(**kwargs):
    list = []
    logoemu = 'logoemu.png'
    if not os.path.isfile('/var/lib/dpkg/status'):
        logoemu = plugin_foo + '/res/pics/logoemu.png'
    list.append(PluginDescriptor(name=_(name_plugemu), description='Emu Keys', where=PluginDescriptor.WHERE_PLUGINMENU, icon=logoemu, fnc=main2))
    list.append(PluginDescriptor(name=_(name_plugemu), description='Emu Keys', where=PluginDescriptor.WHERE_EXTENSIONSMENU, icon=logoemu, fnc=main))
    return list
