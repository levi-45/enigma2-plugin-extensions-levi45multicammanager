# Embedded file name: /usr/lib/enigma2/python/Plugins/Extensions/Levi45MulticamManager/levisemu.py
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
name_plugemu = 'Levi45 Emu Keys V.9.2'

class Levi45EmuKeysUpdater(Screen):
    if os.path.exists('/var/lib/dpkg/status'):
        skin = '\n        <screen name="Levi45 EmuKeys Updater" position="center,center" size="1280,720" title="Levi45 EmuKeys Updater" flags="wfNoBorder" backgroundColor="transparent">\n        <!-- /*ClockWidget-->\n        <eLabel position="264,51" zPosition="-1" size="340,320" backgroundColor="background" transparent="0" foregroundColor="background" />\n        <!-- /*ClockWidget-->\n        <widget source="global.CurrentTime" render="Label" position="450,405" size="169,80" font="Regular; 60" halign="left" backgroundColor="background" transparent="1" valign="top" foregroundColor="white">\n        <convert type="ClockToText">Default</convert>\n        </widget>\n        <widget source="global.CurrentTime" render="Label" position="290,450" size="148,29" font="Regular; 19" halign="right" backgroundColor="background" foregroundColor="white" transparent="1">\n        <convert type="ClockToText">Format:%e. %b</convert>\n        </widget>\n        <widget source="global.CurrentTime" render="Label" position="313,420" size="125,30" font="Regular; 19" halign="right" backgroundColor="background" foregroundColor="white" transparent="1">\n        <convert type="ClockToText">Format:%A</convert>\n        </widget>\n        <eLabel position="265,410" zPosition="-1" size="340,70" backgroundColor="background" transparent="0" foregroundColor="background" />\n        <!--ClockWidget */-->\n        <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Levi45MulticamManager/res/pics/hd/mcmaneger.png" transparent="1" position="310,85" size="256,256" alphatest="blend" />\n        <eLabel name="" position="628,50" zPosition="-11" size="446,432" backgroundColor="background" foregroundColor="background" />\n        <widget name="list" itemHeight="40" position="636,60" size="429,411" zPosition="1" scrollbarMode="showOnDemand" />\n         </screen>\n         '
    else:
        skin = '\n        <screen name="Levi45 EmuKeys Updater" position="center,center" size="1280,720" title="Levi45 EmuKeys Updater" flags="wfNoBorder" backgroundColor="transparent">\n        <!-- /*ClockWidget-->\n        <eLabel position="264,51" zPosition="-1" size="340,320" backgroundColor="background" transparent="0" foregroundColor="background" />\n        <!-- /*ClockWidget-->\n        <widget source="global.CurrentTime" render="Label" position="450,405" size="169,80" font="Regular; 60" halign="left" backgroundColor="background" transparent="1" valign="top" foregroundColor="white">\n        <convert type="ClockToText">Default</convert>\n        </widget>\n        <widget source="global.CurrentTime" render="Label" position="290,450" size="148,29" font="Regular; 19" halign="right" backgroundColor="background" foregroundColor="white" transparent="1">\n        <convert type="ClockToText">Format:%e. %b</convert>\n        </widget>\n        <widget source="global.CurrentTime" render="Label" position="313,420" size="125,30" font="Regular; 19" halign="right" backgroundColor="background" foregroundColor="white" transparent="1">\n        <convert type="ClockToText">Format:%A</convert>\n        </widget>\n        <eLabel position="265,410" zPosition="-1" size="340,70" backgroundColor="background" transparent="0" foregroundColor="background" />\n        <!--ClockWidget */-->\n        <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Levi45MulticamManager/res/pics/hd/mcmaneger.png" transparent="1" position="310,85" size="256,256" alphatest="blend" />\n        <eLabel name="" position="628,50" zPosition="-11" size="446,432" backgroundColor="background" foregroundColor="background" />\n        <widget name="list" itemHeight="50" font="Regular;28" position="636,60" size="429,411" zPosition="1" scrollbarMode="showOnDemand" />\n         </screen>\t\t\n         '

    def __init__(self, session, args = None):
        Screen.__init__(self, session)
        self.session = session
        self['list'] = MenuList([])
        self['actions'] = ActionMap(['OkCancelActions'], {'ok': self.run,
         'cancel': self.close}, -1)
        self.onLayoutFinish.append(self.loadScriptList)

    def loadScriptList(self):
        try:
            slist = listdir(emu_plugin)
            slist = [ x[:-3] for x in slist if x.endswith('.sh') ]
        except:
            slist = []

        slist.sort(reverse=False)
        self['list'].setList(slist)

    def run(self):
        try:
            script = self['list'].getCurrent()
        except:
            script = None

        if script is not None:
            title = script
            script = emu_plugin + '%s.sh' % script
            from os import access, X_OK, chmod
            if not access(script, X_OK):
                chmod(script, 493)
            self.session.open(Console, title, cmdlist=[script])
        return


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
    iconpic2 = 'logoemu.png'
    if not os.path.isfile('/var/lib/dpkg/status'):
        iconpic2 = plugin_foo + '/res/pics/logoemu.png'
    list.append(PluginDescriptor(name=_(name_plugemu), description='Emu Keys', where=PluginDescriptor.WHERE_PLUGINMENU, icon=iconpic2, fnc=main2))
    list.append(PluginDescriptor(name=_(name_plugemu), description='Emu Keys', where=PluginDescriptor.WHERE_EXTENSIONSMENU, icon=iconpic2, fnc=main))
    return list
