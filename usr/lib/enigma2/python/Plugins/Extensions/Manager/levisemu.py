#!/usr/bin/python
# -*- coding: utf-8 -*-

# -------------------#
#  coded by Lululla  #
#   skin by MMark    #
#     update to      #
#       Levi45       #
#     08/07/2023     #
#      No Coppy      #
# -------------------#
from . import _
from Components.ActionMap import ActionMap
from Components.MenuList import MenuList
from Plugins.Plugin import PluginDescriptor
from Screens.Console import Console
from Screens.Screen import Screen
from Components.MultiContent import MultiContentEntryText
from enigma import eListboxPythonMultiContent
from enigma import gFont
from enigma import getDesktop
import os
import sys

plugin_foo = os.path.dirname(sys.modules[__name__].__file__)
emu_plugin = plugin_foo + '/emu/'
name_plugemu = 'Levi45 Emu Keys V.10.1-r15'
res_plugin_foo = os.path.join(plugin_foo, 'res/')
screenwidth = getDesktop(0).size()


def ulistEntry(download):
    res = [download]
    white = 16777215
    blue = 79488
    col = 16777215
    if screenwidth.width() == 2560:
        res.append(MultiContentEntryText(pos=(2, 0), size=(2000, 50), font=0, text=download, color=col, color_sel=white, backcolor_sel=blue))
    elif screenwidth.width() == 1920:
        res.append(MultiContentEntryText(pos=(2, 0), size=(900, 40), font=0, text=download, color=col, color_sel=white, backcolor_sel=blue))
    else:
        res.append(MultiContentEntryText(pos=(2, 0), size=(660, 40), font=0, text=download, color=col, color_sel=white, backcolor_sel=blue))
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
        if screenwidth.width() == 2560:
            self.l.setItemHeight(60)
            textfont = int(42)
            self.l.setFont(0, gFont('Regular', textfont))
        elif screenwidth.width() == 1920:
            self.l.setItemHeight(50)
            textfont = int(32)
            self.l.setFont(0, gFont('Regular', textfont))
        else:
            self.l.setItemHeight(40)
            textfont = int(24)
            self.l.setFont(0, gFont('Regular', textfont))


class Levi45EmuKeysUpdater(Screen):
    if os.path.exists('/var/lib/dpkg/status'):
        skin = '''
               <screen name="Levi45 EmuKeys Updater" position="center,center" size="1280,720" title="Levi45 EmuKeys Updater" flags="wfNoBorder" backgroundColor="transparent">
                    <eLabel position="264,51" zPosition="-1" size="340,320" backgroundColor="#10000000" transparent="0" foregroundColor="#10000000" />
                    <widget source="global.CurrentTime" render="Label" position="436,411" size="187,80" font="Regular; 50" halign="left" backgroundColor="#10000000" transparent="1" valign="top" foregroundColor="white">
                        <convert type="ClockToText">Default</convert>
                    </widget>
                    <widget source="global.CurrentTime" render="Label" position="290,450" size="148,29" font="Regular; 19" halign="right" backgroundColor="#10000000" foregroundColor="white" transparent="1">
                        <convert type="ClockToText">Format:%e. %b</convert>
                    </widget>
                    <widget source="global.CurrentTime" render="Label" position="313,420" size="125,30" font="Regular; 19" halign="right" backgroundColor="#10000000" foregroundColor="white" transparent="1">
                        <convert type="ClockToText">Format:%A</convert>
                    </widget>
                    <eLabel position="265,410" zPosition="-1" size="340,70" backgroundColor="#10000000" transparent="0" foregroundColor="#10000000" />
                    <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Manager/res/pics/hd/mcmaneger.png" transparent="1" position="340,100" size="256,256" alphatest="blend" />
                    <eLabel name="" position="628,50" zPosition="-11" size="653,432" backgroundColor="#10000000" foregroundColor="#10000000" />
                    <widget name="list" itemHeight="40" position="636,60" size="629,411" zPosition="1" scrollbarMode="showOnDemand" />
                </screen>'''
    else:
        skin = '''
                <screen name="Levi45 EmuKeys Updater" position="center,center" size="1280,720" title="Levi45 EmuKeys Updater" flags="wfNoBorder" backgroundColor="transparent">
                    <eLabel position="264,51" zPosition="-1" size="340,320" backgroundColor="#10000000" transparent="0" foregroundColor="#10000000" />
                    <widget source="global.CurrentTime" render="Label" position="436,411" size="187,80" font="Regular; 50" halign="left" backgroundColor="#10000000" transparent="1" valign="top" foregroundColor="white">
                        <convert type="ClockToText">Default</convert>
                    </widget>
                    <widget source="global.CurrentTime" render="Label" position="290,450" size="148,29" font="Regular; 19" halign="right" backgroundColor="#10000000" foregroundColor="white" transparent="1">
                        <convert type="ClockToText">Format:%e. %b</convert>
                    </widget>
                    <widget source="global.CurrentTime" render="Label" position="313,420" size="125,30" font="Regular; 19" halign="right" backgroundColor="#10000000" foregroundColor="white" transparent="1">
                        <convert type="ClockToText">Format:%A</convert>
                    </widget>
                    <eLabel position="265,410" zPosition="-1" size="340,70" backgroundColor="#10000000" transparent="0" foregroundColor="#10000000" />
                    <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Manager/res/pics/hd/mcmaneger.png" transparent="1" position="340,100" size="256,256" alphatest="blend" />
                    <eLabel name="" position="628,50" zPosition="-11" size="653,432" backgroundColor="#10000000" foregroundColor="#10000000" />
                    <widget name="list" itemHeight="40" font="Regular; 28" position="636,60" size="629,411" zPosition="1" scrollbarMode="showOnDemand" />
                </screen>'''

    def __init__(self, session, args=None):
        Screen.__init__(self, session)
        self.session = session
        self['list'] = M3UList([])
        self['actions'] = ActionMap(['OkCancelActions'], {'ok': self.run, 'cancel': self.close}, -1)
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
                name = name.replace('.sh', '').replace('_', ' ').upper()
                self.names.append(name)
                self.urls.append(url)
        ulistx(self.names, self["list"])

    def run(self):
        idx = self["list"].getSelectionIndex()
        if idx == -1 or idx is None:
            return
        else:
            try:
                name = self.names[idx]
                dom = emu_plugin + self.urls[idx]
                # print('dom -- ', dom)
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
        return [('Levi45 Emu Keys Updater', main2, 'Levi45 Emu Keys Updater', None)]
    else:
        return []


def Plugins(**kwargs):
    list = []
    logoemu = 'logoemu.png'
    if not os.path.isfile('/var/lib/dpkg/status'):
        logoemu = plugin_foo + '/res/pics/logoemu.png'
    list.append(PluginDescriptor(name=_(name_plugemu), description='Emu Keys', where=PluginDescriptor.WHERE_PLUGINMENU, icon=logoemu, fnc=main2))
    list.append(PluginDescriptor(name=_(name_plugemu), description='Emu Keys', where=PluginDescriptor.WHERE_EXTENSIONSMENU, icon=logoemu, fnc=main2))
    return list
