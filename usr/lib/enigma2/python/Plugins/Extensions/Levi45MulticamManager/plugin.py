#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#--------------------#
#  coded by Lululla  #
#   skin by MMark    #
#     update to      #
#       Levi45       #
#     12/12/2021     #
#      No Coppy      #
#--------------------#
from __future__ import print_function
from . import _
from Components.ActionMap import ActionMap, NumberActionMap
from Components.Button import Button
from Components.FileList import FileList
from Components.Label import Label
from Components.MenuList import MenuList
from Components.MultiContent import MultiContentEntryText, MultiContentEntryPixmapAlphaTest
from Components.Pixmap import Pixmap
from Components.PluginComponent import plugins
from Components.Sources.List import List
from Components.Sources.StaticText import StaticText
from Plugins.Plugin import PluginDescriptor
from Screens.ChoiceBox import ChoiceBox
from Screens.Console import Console
from Screens.MessageBox import MessageBox
from Screens.PluginBrowser import PluginBrowser
from Screens.Screen import Screen
from Screens.Standby import TryQuitMainloop
from ServiceReference import ServiceReference
from Tools import Notifications
from Tools.BoundFunction import boundFunction
from Tools.Directories import *
from Tools.Directories import fileExists, copyfile
from Tools.Directories import resolveFilename, SCOPE_PLUGINS
from Tools.LoadPixmap import LoadPixmap
from enigma import *
from enigma import RT_HALIGN_LEFT, RT_HALIGN_RIGHT, RT_HALIGN_CENTER, RT_VALIGN_CENTER
from enigma import eListboxPythonMultiContent
from enigma import eTimer, ePicLoad, loadPNG
from enigma import gFont
from os import path, listdir, remove, mkdir, chmod, walk
from random import choice
from time import sleep
from twisted.web.client import getPage
from xml.dom import Node, minidom
import base64
import glob
import os
import sys
import time
import re
import six
import ssl
from Plugins.Extensions.Levi45MulticamManager.data.GetEcmInfo import GetEcmInfo
from sys import version_info
try:
    from Plugins.Extensions.Levi45MulticamManager.Utils import *
except:
    from . import Utils
from six.moves.urllib.request import urlopen
from six.moves.urllib.request import Request
from six.moves.urllib.error import HTTPError, URLError
from six.moves.urllib.request import urlretrieve
global active, MYFTP

currversion = '9.2'
title_plug = 'Levi45 Multicam Manager V. %s' % currversion
name_plug = 'Levi45 Multicam Manager'
name_plugemu = 'Levi45 Emu Keys'
plugin_foo = os.path.dirname(sys.modules[__name__].__file__)
res_plugin_foo = plugin_foo + '/res/'
MYFTP = 'aHR0cDovL2+xldmk0NS5zcGRu+cy5ldS9-BZGRv+bnMvTXVsdGljYW+0vYW-Rkb25z+Ln-htbA=='
MYFTP = MYFTP.replace('+', '').replace('-', '')
FTP_XML= b64decoder(MYFTP)
iconpic = plugin_foo + '/logo.png'
keys = '/usr/keys'
camscript = '/usr/camscript'
data_path = plugin_foo + '/data'
ECM_INFO = '/tmp/ecm.info'
EMPTY_ECM_INFO = ('',
 '0',
 '0',
 '0')
old_ecm_time = time.time()
info = {}
ecm = ''
data = EMPTY_ECM_INFO
active = False
SOFTCAM = 0
CCCAMINFO = 1
OSCAMINFO = 2

def __createdir(list):
    dir = ''
    for line in list[1:].split('/'):
        dir += '/' + line
        if not os.path.exists(dir):
            try:
                mkdir(dir)
            except:
                print('Mkdir Failed', dir)

def checkdir():
    if not os.path.exists(keys):
        __createdir('/usr/keys')
    if not os.path.exists(camscript):
        __createdir('/usr/camscript')
checkdir()


def readCurrent_1():
    currCam = ''
    FilCurr = ''
    if fileExists('/etc/CurrentBhCamName'):
        FilCurr = '/etc/CurrentBhCamName'
    else:
        FilCurr = '/etc/clist.list'
    try:
        clist = open(FilCurr, 'r')
    except:
        return

    if clist is not None:
        for line in clist:
            currCam = line

        clist.close()
    return currCam

if isFHD():
    skin_path = res_plugin_foo + 'skins/fhd/'
else:
    skin_path = res_plugin_foo + 'skins/hd/'
if DreamOS():
    skin_path = skin_path + 'dreamOs/'

def show_list(h):
    png1 = plugin_foo + '/res/img/actcam.png'
    png2 = plugin_foo + '/res/img/defcam.png'
    cond = readCurrent_1()
    if isFHD():
        res = [h]
        if cond == h:
            active = True
            res.append(MultiContentEntryPixmapAlphaTest(pos=(10, 12), size=(43, 24), png=loadPNG(png1)))
            res.append(MultiContentEntryText(pos=(70, 3), size=(800, 48), font=8, text=h + ' (Active)', color=11403008, flags=RT_HALIGN_LEFT))
        else:
            res.append(MultiContentEntryPixmapAlphaTest(pos=(10, 12), size=(43, 24), png=loadPNG(png2)))
            res.append(MultiContentEntryText(pos=(70, 3), size=(800, 48), font=8, text=h, flags=RT_HALIGN_LEFT))
        return res
    else:
        res = [h]
        if cond == h:
            active = True
            res.append(MultiContentEntryText(pos=(70, 4), size=(406, 40), font=4, text=h + ' (Active)', color=11403008, flags=RT_HALIGN_LEFT))
            res.append(MultiContentEntryPixmapAlphaTest(pos=(2, 8), size=(43, 24), png=loadPNG(png1)))
        else:
            res.append(MultiContentEntryText(pos=(70, 4), size=(406, 40), font=4, text=h, flags=RT_HALIGN_LEFT))
            res.append(MultiContentEntryPixmapAlphaTest(pos=(2, 8), size=(43, 24), png=loadPNG(png2)))
        return res


def showlist(datal, list):
    icount = 0
    plist = []
    for line in datal:
        name = datal[icount]
        plist.append(show_list_1(name))
        icount = icount + 1
        list.setList(plist)


def show_list_1(h):
    if isFHD():
        res = [h]
        res.append(MultiContentEntryText(pos=(2, 2), size=(1000, 40), font=8, text=h, flags=RT_HALIGN_LEFT))
    else:
        res = [h]
        res.append(MultiContentEntryText(pos=(2, 2), size=(800, 30), font=3, text=h, flags=RT_HALIGN_LEFT))
    return res


class m2list(MenuList):

    def __init__(self, list):
        MenuList.__init__(self, list, False, eListboxPythonMultiContent)
        self.l.setFont(0, gFont('Regular', 16))
        self.l.setFont(1, gFont('Regular', 20))
        self.l.setFont(2, gFont('Regular', 22))
        self.l.setFont(3, gFont('Regular', 24))
        self.l.setFont(4, gFont('Regular', 26))
        self.l.setFont(5, gFont('Regular', 28))
        self.l.setFont(6, gFont('Regular', 30))
        self.l.setFont(7, gFont('Regular', 32))
        self.l.setFont(8, gFont('Regular', 34))
        if isFHD():
            self.l.setItemHeight(50)
        else:
            self.l.setItemHeight(45)


class Levi45MulticamManager(Screen):

    def __init__(self, session, args = False):
        self.session = session
        skin = skin_path + '/Levi45MulticamManager.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        self.index = 0
        self.emulist = []
        self.namelist = []
        self.softcamslist = []
        self.ecminfo = GetEcmInfo()
        try:
            self.oldService = self.session.nav.getCurrentlyPlayingServiceReference()
        except:
            self.oldService = self.session.nav.getCurrentlyPlayingServiceOrGroup()

        self['actions'] = ActionMap(['OkCancelActions',
         'ColorActions',
         'SetupActions',
         'MenuActions',
         'NumberActions'], {'ok': self.action,
         'cancel': self.close,
         '0': self.openemu,
         '1': self.cccam,
         '2': self.oscam,
         'menu': self.configtv,
         'blue': self.Blue,
         'yellow': self.download,
         'green': self.action,
         'info': self.CfgInfo,
         'red': self.stop}, -1)
        self.setTitle(_(title_plug))
        self['title'] = Label(_(title_plug))
        self['key_green'] = Button(_('Start'))
        self['key_yellow'] = Button(_('Download'))
        self['key_red'] = Button(_('Stop'))
        self['key_blue'] = Button(_('Softcam'))
        self['desc'] = Label()
        self['desc'].setText(_('Scanning and retrieval list softcam ...'))
        self['info'] = Label('')
        self['list'] = m2list([])
        self.currCam = self.readCurrent()
        self.readScripts()
        self.BlueAction = SOFTCAM
        self.timer = eTimer()
        try:
            self.timer_conn = self.timer.timeout.connect(self.cgdesc)
        except:
            self.timer.callback.append(self.cgdesc)
        self.timer.start(800, 1)
        self.EcmInfoPollTimer = eTimer()
        try:
            self.EcmInfoPollTimer_conn = self.EcmInfoPollTimer.timeout.connect(self.setEcmInfo)
        except:
            self.EcmInfoPollTimer.callback.append(self.setEcmInfo)

        self.EcmInfoPollTimer.start(200)
        self.onShown.append(self.ecm)
        self.onShown.append(self.setBlueKey)
        self.onHide.append(self.stopEcmInfoPollTimer)

    def setBlueKey(self):
        if self.currCam == 'no':
            self['key_blue'].setText(_('Softcam'))
        if self.currCam is not None:
            print('self.currCam: ', self.currCam)
            if 'ccam' in self.currCam.lower():
                if os.path.exists(resolveFilename(SCOPE_PLUGINS, 'Extensions/CCcamInfo')):
                    self.BlueAction = CCCAMINFO
                    self['key_blue'].setText(_('CCcamInfo'))
            elif 'oscam' in self.currCam.lower():
                if os.path.exists(resolveFilename(SCOPE_PLUGINS, 'Extensions/OscamStatus')):
                    self.BlueAction = OSCAMINFO
                    self['key_blue'].setText(_('OscamInfo'))
            else:
                self.BlueAction = SOFTCAM
                self['key_blue'].setText(_('SOFTCAM'))
        else:
            self.BlueAction = SOFTCAM
            self['key_blue'].setText(_('SOFTCAM'))
        return

    def ShowSoftcamCallback(self):
        pass

    def Blue(self):
        if self.BlueAction == CCCAMINFO:
            if os.path.exists(resolveFilename(SCOPE_PLUGINS, 'Extensions/CCcamInfo')):
                from Plugins.Extensions.CCcamInfo.plugin import CCcamInfoMain
                self.session.openWithCallback(self.ShowSoftcamCallback, CCcamInfoMain)
        elif self.BlueAction == OSCAMINFO:
            if os.path.exists(resolveFilename(SCOPE_PLUGINS, 'Extensions/OscamStatus')):
                from Plugins.Extensions.OscamStatus.plugin import OscamStatus
                self.session.openWithCallback(self.ShowSoftcamCallback, OscamStatus)
        else:
            self.BlueAction == SOFTCAM
            self.messagekd()

    def cccam(self):
        if 'ccam' in self.currCam.lower() and self.currCam != 'no':
            if os.path.exists(resolveFilename(SCOPE_PLUGINS, 'Extensions/CCcamInfo')):
                from Plugins.Extensions.CCcamInfo.plugin import CCcamInfoMain
                self.session.openWithCallback(self.ShowSoftcamCallback, CCcamInfoMain)

    def oscam(self):
        if 'oscam' in self.currCam.lower() and self.currCam != 'no':
            if os.path.exists(resolveFilename(SCOPE_PLUGINS, 'Extensions/OscamStatus')):
                from Plugins.Extensions.OscamStatus.plugin import OscamStatus
                self.session.openWithCallback(self.ShowSoftcamCallback, OscamStatus)

    def setEcmInfo(self):
        self.ecminfo = GetEcmInfo()
        newEcmFound, ecmInfo = self.ecminfo.getEcm()
        if newEcmFound:
            self['info'].setText(''.join(ecmInfo))
        else:
            self.ecm()

    def ecm(self):
        ecmf = ''
        if os.path.isfile('/tmp/ecm.info'):
            myfile = open('/tmp/ecm.info')
            for line in myfile.readlines():
                print('line: ', line)
                ecmf = ecmf + line
                print('ecmf + line: ', ecmf)
                self['info'].setText(ecmf)

        else:
            self['info'].setText(ecmf)

    def stopEcmInfoPollTimer(self):
        self.EcmInfoPollTimer.stop()

    def messagekd(self):
        self.session.openWithCallback(self.keysdownload, MessageBox, _('Update SoftcamKeys from google search?'), MessageBox.TYPE_YESNO)

    def keysdownload(self, result):
        if result:
            script = '%s/auto' % plugin_foo
            from os import access, X_OK, chmod
            if not access(script, X_OK):
                chmod(script, 493)
            self.prombt('sh %s' % script)

    def prombt(self, com):
        self.session.open(Console, _('Update Softcam.key: %s') % com, ['%s' % com])

    def CfgInfo(self):
        self.session.open(InfoCfg)

    def openemu(self):
        from Plugins.Extensions.Levi45MulticamManager.levisemu import Levi45EmuKeysUpdater
        self.session.openWithCallback(self.close, Levi45EmuKeysUpdater)

    def configtv(self):
        from Plugins.Extensions.Levi45MulticamManager.data.datas import tv_config
        self.session.open(tv_config)

    def cgdesc(self):
        self['desc'].setText(_('Select a cam to run ...'))

    def openTest(self):
        pass

    def download(self):
        self.session.open(GetipklistTv)
        self.onShown.append(self.readScripts)

    def getLastIndex(self):
        a = 0
        if len(self.namelist) > 0:
            for x in self.namelist:
                if x == self.currCam:
                    return a
                a += 1

        else:
            return -1
        return -1

    def action(self):
        self.session.nav.stopService()
        msg = []
        self.last = self.getLastIndex()
        self.var = self['list'].getSelectionIndex()
        if self.last > -1:
            if self.last == self.var:
                self.cmd1 = '/usr/camscript/' + self.softcamslist[self.var][0] + '.sh' + ' cam_res &'
                msg.append(_('RESTART CAM '))
                os.system(self.cmd1)
                sleep(1)
            else:
                self.cmd1 = '/usr/camscript/' + self.softcamslist[self.last][0] + '.sh' + ' cam_down &'
                msg.append(_('STOP & RESTART CAM '))
                os.system(self.cmd1)
                sleep(1)
                self.cmd1 = '/usr/camscript/' + self.softcamslist[self.var][0] + '.sh' + ' cam_up &'
                os.system(self.cmd1)
        else:
            try:
                self.cmd1 = '/usr/camscript/' + self.softcamslist[self.var][0] + '.sh' + ' cam_up &'
                msg.append(_('UP CAM 2'))
                os.system(self.cmd1)
                sleep(1)
            except:
                self.close()

        if self.last != self.var:
            try:
                self.currCam = self.softcamslist[self.var][0]
                self.writeFile()
            except:
                self.close()

        msg = (' %s ' % _('and')).join(msg)
        self.mbox = self.session.open(MessageBox, _('Please wait, %s.') % msg, MessageBox.TYPE_INFO, timeout=5)
        self.session.nav.playService(self.oldService)
        self.EcmInfoPollTimer = eTimer()
        try:
            self.EcmInfoPollTimer_conn = self.EcmInfoPollTimer.timeout.connect(self.setEcmInfo)
        except:
            self.EcmInfoPollTimer.callback.append(self.setEcmInfo)

        self.EcmInfoPollTimer.start(200)
        self.readScripts()

    def writeFile(self):
        if self.currCam is not None:
            clist = open('/etc/clist.list', 'w')
            clist.write(self.currCam)
            clist.close()
        stcam = open('/etc/startcam.sh', 'w')
        stcam.write('#!/bin/sh\n' + self.cmd1)
        stcam.close()
        os.system('chmod 755 /etc/startcam.sh &')
        return

    def stop(self):
        self.EcmInfoPollTimer.stop()
        last = self.getLastIndex()
        if last > -1:
            self.cmd1 = '/usr/camscript/' + self.softcamslist[last][0] + ' cam_down &'
            os.system(self.cmd1)
        else:
            return
        self.currCam = 'no'
        self.writeFile()
        sleep(1)
        self['info'].setText('CAM STOPPED')
        try:
            self.oldService = self.session.nav.getCurrentlyPlayingServiceReference()
        except:
            self.oldService = self.session.nav.getCurrentlyPlayingServiceOrGroup()

        self.session.nav.stopService()
        self.readScripts()

    def readScripts(self):
        self.index = 0
        self.indexto = ''
        scriptlist = []
        pliste = []
        path = '/usr/camscript/'
        for root, dirs, files in os.walk(path):
            for name in files:
                scriptlist.append(name)

        self.emulist = scriptlist
        i = len(self.softcamslist)
        del self.softcamslist[0:i]
        for lines in scriptlist:
            dat = path + lines
            sfile = open(dat, 'r')
            for line in sfile:
                if line[0:3] == 'OSD':
                    nam = line[5:len(line) - 2]
                    print('We are in Levi45MulticamManager and cam is type  = ', nam)
                    if self.currCam is not None:
                        if nam == self.currCam:
                            self.softcamslist.append(show_list(nam))
                        else:
                            self.softcamslist.append(show_list(nam))
                            self.index += 1
                    else:
                        self.softcamslist.append(show_list(nam))
                        self.index += 1
                    pliste.append(nam)

            sfile.close()
            self['list'].l.setList(self.softcamslist)
            self.namelist = pliste

        return

    def readCurrent(self):
        currCam = ''
        FilCurr = ''
        if fileExists('/etc/CurrentBhCamName'):
            FilCurr = '/etc/CurrentBhCamName'
        else:
            FilCurr = '/etc/clist.list'
        try:
            clist = open(FilCurr, 'r')
        except:
            return

        if clist is not None:
            for line in clist:
                currCam = line

            clist.close()
        return currCam

    def autocam(self):
        current = None
        try:
            clist = open('/etc/clist.list', 'r')
            print('found list')
        except:
            return

        if clist is not None:
            for line in clist:
                current = line

            clist.close()
        print('current =', current)
        if os.path.isfile('/etc/autocam.txt') is False:
            alist = open('/etc/autocam.txt', 'w')
            alist.close()
        self.autoclean()
        alist = open('/etc/autocam.txt', 'a')
        alist.write(self.oldService.toString() + '\n')
        self.last = self.getLastIndex()
        alist.write(current + '\n')
        alist.close()
        self.session.openWithCallback(self.callback, MessageBox, _('Autocam assigned to the current channel'), type=1, timeout=10)
        return

    def autoclean(self):
        delemu = 'no'
        if os.path.isfile('/etc/autocam.txt') is False:
            return
        myfile = open('/etc/autocam.txt', 'r')
        myfile2 = open('/etc/autocam2.txt', 'w')
        icount = 0
        for line in myfile.readlines():
            print('We are in Levi45MulticamManager line, self.oldService.toString() =', line, self.oldService.toString())
            if line[:-1] == self.oldService.toString():
                delemu = 'yes'
                icount = icount + 1
                continue
            if delemu == 'yes':
                delemu = 'no'
                icount = icount + 1
                continue
            myfile2.write(line)
            icount = icount + 1
        myfile.close()
        myfile2.close()
        os.system('rm /etc/autocam.txt')
        os.system('cp /etc/autocam2.txt /etc/autocam.txt')


class GetipklistTv(Screen):

    def __init__(self, session):
        self.session = session
        skin = skin_path + '/GetipklistTv.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        self.names = []
        self.names_1 = []
        self.list = []
        self['text'] = m2list([])
        self.setTitle(_(title_plug))
        self['title'] = Label(_(title_plug))
        self['desc2'] = Label(_('Getting the list, please wait ...'))
        self['key_red'] = Button(_('Back'))
        self['key_green'] = Button(_(''))
        self['key_yellow'] = Button(_(''))
        self['key_blue'] = Button(_(''))
        self['key_green'].hide()
        self['key_yellow'].hide()
        self['key_blue'].hide()
        self.addon = 'emu'
        self.icount = 0
        self.downloading = False
        self.timer = eTimer()
        if os.path.exists('/var/lib/dpkg/status'):
            self.timer_conn = self.timer.timeout.connect(self.downloadxmlpage)
        else:
            self.timer.callback.append(self.downloadxmlpage)
        self.timer.start(500, 1)
        self['actions'] = ActionMap(['SetupActions', 'ColorActions'], {'ok': self.okClicked,
         'cancel': self.close}, -1)
        # self.onShown.append(self.get_list)

    def downloadxmlpage(self):
        # MYFTP = MYFTP.replace('+', '').replace('-', '')
        # FTP_XML= b64decoder(FTP_XML)
        url = str(FTP_XML)
        if six.PY3:
            url = six.binary_type(url, encoding='utf-8')
        print('url softcam: ', url)
        getPage(url).addCallback(self._gotPageLoad).addErrback(self.errorLoad)

    def errorLoad(self, error):
        print(str(error))
        self['desc2'].setText(_('Try again later ...'))
        self.downloading = False

    def _gotPageLoad(self, data):
        self.xml = str(data)
        if six.PY3:
            self.xml = six.ensure_str(data)
        try:
            regexC = '<plugins cont="(.*?)"'
            match = re.compile(regexC, re.DOTALL).findall(self.xml)
            for name in match:
                name = checkStr(name)
                self.list.append(name)
                self['desc2'].setText(_('Please select ...'))
            showlist(self.list, self['text'])
            self.downloading = True
        except:
            self['desc2'].setText(_('Try again later ...'))
            pass

    def okClicked(self):
        if self.downloading == True:
            try:
                idx = self["text"].getSelectionIndex()
                name = self.list[idx]
                self.session.open(GetipkTv, self.xml, name)
            except:
                return
        else:
            self.close()

class GetipkTv(Screen):
    def __init__(self, session, xmlparse, selection):
        self.session = session
        skin = skin_path + '/GetipkTv.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        self.xmlparse = xmlparse
        self.selection = selection
        self['text'] = m2list([])
        self.list = []
        self.setTitle(_(title_plug))
        self['title'] = Label(_(title_plug))
        self['desc'] = Label(_('Select and Install'))
        self['key_red'] = Button(_('Back'))
        self['key_green'] = Button(_(''))
        self['key_yellow'] = Button(_(''))
        self['key_blue'] = Button(_(''))
        self['key_green'].hide()
        self['key_yellow'].hide()
        self['key_blue'].hide()
        self['actions'] = ActionMap(['SetupActions'], {'ok': self.message,
         'cancel': self.close}, -1)
        self.onLayoutFinish.append(self.start)

    def start(self):
        xmlparse = self.xmlparse
        n1 = xmlparse.find(self.selection, 0)
        n2 = xmlparse.find("</plugins>", n1)
        data1 = xmlparse[n1:n2]
        self.names = []
        self.urls = []
        items = []
        regex = '<plugin name="(.*?)".*?url>(.*?)</url'
        # regex = '<plugin name = "(.*?)".*?url>(.*?)</url'
        match = re.compile(regex,re.DOTALL).findall(data1)
        for name, url in match:
            name = name.replace('_',' ').replace('-',' ')
            name = checkStr(name)
            item = name + "###" + url
            items.append(item)
        items.sort()
        for item in items:
            name = item.split('###')[0]
            url = item.split('###')[1]
            self.names.append(name)
            self.urls.append(url)
        showlist(self.names, self['text'])

    def message(self):
        self.session.openWithCallback(self.selclicked, MessageBox, _('Do you want to install?'), MessageBox.TYPE_YESNO)

    def selclicked(self, result):
        if result:
            idx = self["text"].getSelectionIndex()
            dom = self.names[idx]
            com = self.urls[idx]
            self.prombt(com, dom)

    def prombt(self, com, dom):
        try:
            useragent = "--header='User-Agent: QuickTime/7.6.2 (qtver=7.6.2;os=Windows NT 5.1Service Pack 3)'"
            self.com = str(com)
            self.dom = str(dom)
            print('self.com---------------', self.com)
            print('self.dom---------------', self.dom)
            ipkpth = '/var/volatile/tmp'
            destipk = ipkpth + '/download.ipk'
            desttar = ipkpth + '/download.tar.gz'
            destdeb = ipkpth + '/download.deb'
            self.timer = eTimer()
            self.timer.start(1500, 1)
            if self.com.find('.ipk') != -1:
                if fileExists(destipk):
                    os.remove(destipk)
                os.system('wget %s -c %s -O %s > /dev/null' % (useragent, self.com, destipk))
                cmd0 = 'opkg install --force-overwrite ' + destipk
                self.session.open(Console, title='IPK Installation', cmdlist=[cmd0, 'sleep 5'])
            if self.com.find('.tar.gz') != -1:
                if fileExists(desttar):
                    os.remove(desttar)
                os.system('wget %s -c %s -O %s > /dev/null' % (useragent, self.com, desttar))
                cmd0 = 'tar -xzvf ' + desttar + ' -C /'
                self.session.open(Console, title='TAR GZ Installation', cmdlist=[cmd0, 'sleep 5'])
            if self.com.find('.deb') != -1:
                if fileExists(destdeb):
                    os.remove(destdeb)
                if DreamOS():
                    os.system('wget %s -c %s -O %s > /dev/null' % (useragent, self.com, destdeb))
                    cmd0 = 'dpkg -i ' + destdeb
                    self.session.open(Console, title='DEB Installation', cmdlist=[cmd0, 'sleep 5'])
                else:
                    self.mbox = self.session.open(MessageBox, _('Unknow Image!'), MessageBox.TYPE_INFO, timeout=5)
        except:
            self.mbox = self.session.open(MessageBox, _('Download failur!'), MessageBox.TYPE_INFO, timeout=5)
            # self.addondel()
            return

    def addondel(self):
        try:
            files = glob.glob('/var/volatile/tmp/download.*', recursive=False)
            for f in files:
                try:
                    os.remove(f)
                except OSError as e:
                    print('Error: %s : %s' % (f, e.strerror))

        except Exception as e:
            print(e)
        # return
        # self.mbox = self.session.open(MessageBox, _('All file Download are removed!'), MessageBox.TYPE_INFO, timeout=5)


class InfoCfg(Screen):

    def __init__(self, session):
        self.session = session
        skin = skin_path + '/InfoCfg.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        info = ''
        self.list = []
        self['text'] = Label('')
        self['actions'] = ActionMap(['WizardActions',
         'OkCancelActions',
         'DirectionActions',
         'ColorActions'], {'ok': self.close,
         'back': self.close,
         'cancel': self.close,
         'red': self.close}, -1)
        self['key_red'] = Button(_('Back'))
        self['key_green'] = Button(_(''))
        self['key_yellow'] = Button(_(''))
        self['key_blue'] = Button(_(''))
        self['key_green'].hide()
        self['key_yellow'].hide()
        self['key_blue'].hide()
        self.setTitle(_(title_plug))
        self['title'] = Label(_(title_plug))
        self['desc'] = Label(_('Path Configuration Folder'))
        self.onShown.append(self.updateList)

    def getcont(self):
        cont = "Config Levi45 Softcam Manager' :\n"
        cont += 'cccam_221\n'
        cont += '/etc/cccam.cfg\n'
        cont += 'cccam_230\n'
        cont += '/usr/cfmngr/cccam/cccam.cfg\n'
        cont += 'doscam_0.30\n'
        cont += '/usr/cfmngr/doscam/doscam.cfg\n'
        cont += 'oscam/powervu/svn_yy.xx\n'
        cont += '/usr/cfmngr/oscam/oscam.server\n'
        cont += 'oscamymod_yy.xx\n'
        cont += '/usr/cfmngr/oscamymod/oscam.server\n'
        cont += 'wicardd_19\n'
        cont += '/usr/cfmngr/wicardd/wicardd.conf\n'
        cont += 'mgcamd_1.38d\n'
        cont += '/usr/keys/cccamd.list \n'
        return cont

    def updateList(self):
        self['text'].setText(self.getcont())


class Ipkremove(Screen):

    def __init__(self, session, args = None):
        Screen.__init__(self, session)
        self['list'] = FileList('/', matchingPattern='^.*\\.(png|avi|mp3|mpeg|ts)')
        self['pixmap'] = Pixmap()
        self['text'] = Input('1234', maxSize=True, type=Input.NUMBER)
        self['actions'] = NumberActionMap(['WizardActions', 'InputActions'], {'ok': self.ok,
         'back': self.close,
         'left': self.keyLeft,
         'right': self.keyRight,
         '1': self.keyNumberGlobal,
         '2': self.keyNumberGlobal,
         '3': self.keyNumberGlobal,
         '4': self.keyNumberGlobal,
         '5': self.keyNumberGlobal,
         '6': self.keyNumberGlobal,
         '7': self.keyNumberGlobal,
         '8': self.keyNumberGlobal,
         '9': self.keyNumberGlobal,
         '0': self.keyNumberGlobal}, -1)
        self.onShown.append(self.openTest)

    def openTest(self):
        try:
            myfile = open('/var/lib/opkg/status', 'r+')
            icount = 0
            listc = []
            ebuf = []
            for line in myfile:
                listc.append(icount)
                listc[icount] = (_(line), '')
                ebuf.append(listc[icount])
                icount = icount + 1

            myfile.close()
            ipkres = self.session.openWithCallback(self.test2, ChoiceBox, title='Please select ipkg to remove', list=ebuf)
            self.close()
        except:
            self.close()

    def test2(self, returnValue):
        if returnValue is None:
            return
        else:
            print('returnValue', returnValue)
            nos = len
            emuname = ''
            ipkname = returnValue[0]
            print('ipkname =', ipkname)
            cmd = 'ipkg remove ' + ipkname[:-1] + ' >/var/volatile/tmp/ipk.log'
            print(cmd)
            os.system(cmd)
            cmd = 'touch /etc/tmpfile'
            os.system(cmd)
            myfile = open('/var/lib/opkg/status', 'r')
            f = open('/etc/tmpfile', 'w')
            icount = 0
            for line in myfile:
                if line != ipkname:
                    print('myfile line=', line)
                    f.write(line)

            f.close()
            f = open('/etc/tmpfile', 'r+')
            f2 = f.readlines()
            print('/etc/tmpfile', f2)
            f.close()
            f = open('/var/lib/opkg/status', 'r+')
            f2 = f.readlines()
            print('/var/lib/opkg/status', f2)
            f.close()
            cmd = 'rm /var/lib/opkg/status'
            os.system(cmd)
            cmd = 'mv /etc/tmpfile /var/lib/opkg/status'
            os.system(cmd)
            f = open('/var/lib/opkg/status', 'r+')
            f2 = f.readlines()
            print('/var/lib/opkg/status 2', f2)
            f.close()
            return
            return

    def callback(self, answer):
        print('answer:', answer)

    def keyLeft(self):
        self['text'].left()

    def keyRight(self):
        self['text'].right()

    def ok(self):
        selection = self['list'].getSelection()
        if selection[1] == True:
            self['list'].changeDir(selection[0])
        else:
            self['pixmap'].instance.setPixmapFromFile(selection[0])

    def keyNumberGlobal(self, number):
        print('pressed', number)
        self['text'].number(number)


def startConfig(session, **kwargs):
    session.open(Levi45MulticamManager)


def autostart(reason, session = None, **kwargs):
    """called with reason=1 to during shutdown, with reason=0 at startup?"""
    print('[Softcam] Started')
    if reason == 0:
        print('reason 0')
        if session is not None:
            print('session none')
            try:
                os.system('mv /usr/bin/dccamd /usr/bin/dccamdOrig &')
                os.system('ln -sf /usr/bin /var/bin')
                os.system('ln -sf /usr/keys /var/keys')
                os.system('ln -sf /usr/scce /var/scce')
                os.system('ln -sf /usr/camscript /var/camscript')
                os.system('sleep 2')
                os.system('/etc/startcam.sh &')
                os.system('sleep 2')
                print('ok started autostart')
            except:
                print('except autostart')

        else:
            print('pass autostart')
    return


def menu(menuid, **kwargs):
    if menuid == 'cam':
        return [(_(name_plug),
          boundFunction(main, showExtentionMenuOption=True),
          'Levi45 Softcam Manager',
          -1)]
    return []


def main(session, **kwargs):
    try:
        from Plugins.Extensions.Levi45MulticamManager.Update import upd_done
        upd_done()
    except:
        pass
    session.open(Levi45MulticamManager)

def main2(session, **kwargs):
    from Plugins.Extensions.Levi45MulticamManager.levisemu import Levi45EmuKeysUpdater
    session.open(Levi45EmuKeysUpdater)


def mainmenu(menuid):
    if menuid != 'setup':
        return []
    else:
        return [(_('Levi45 Softcam Manager'),
          startConfig,
          'Levi45 Softcam Manager',
          None)]
        # return None


def menuemu(menuid):
    if menuid == 'mainmenu':
        return [(name_plugemu,
          main2,
          'Levi45 Emu Keys Updater',
          45)]
    return []


def StartSetup(menuid):
    if menuid == 'mainmenu':
        return [(name_plug,
          main,
          'Levi45 Softcam Manager',
          44)]
    else:
        return []


def Plugins(**kwargs):
    iconpic = 'logo.png'
    iconpic2 = 'logoemu.png'
    if isFHD():
        iconpic = plugin_foo + '/res/pics/logo.png'
        iconpic2 = plugin_foo + '/res/pics/logoemu.png'
    return [PluginDescriptor(name=_(name_plug), where=[PluginDescriptor.WHERE_MENU], fnc=mainmenu),
     PluginDescriptor(name=_(name_plugemu), description='Levi45 Emu Keys Updater V.9.2', where=[PluginDescriptor.WHERE_PLUGINMENU], icon=iconpic2, fnc=main2),
     PluginDescriptor(name=_(name_plugemu), description='Levi45 Emu Keys Updater V.9.2', where=[PluginDescriptor.WHERE_EXTENSIONSMENU], icon=iconpic2, fnc=main2),
     PluginDescriptor(name=_(name_plugemu), description='Levi45 Emu Keys Updater V.9.2', where=[PluginDescriptor.WHERE_MENU], icon=iconpic2, fnc=menuemu),
     PluginDescriptor(name=_(name_plug), description=_(title_plug), where=[PluginDescriptor.WHERE_AUTOSTART, PluginDescriptor.WHERE_SESSIONSTART], needsRestart=True, fnc=autostart),
     PluginDescriptor(name=_(name_plug), description=_(title_plug), where=[PluginDescriptor.WHERE_MENU], icon=iconpic, fnc=StartSetup),
     PluginDescriptor(name=_(name_plug), description=_(title_plug), where=[PluginDescriptor.WHERE_PLUGINMENU], icon=iconpic, fnc=main),
     PluginDescriptor(name=_(name_plug), description=_(title_plug), where=[PluginDescriptor.WHERE_EXTENSIONSMENU], icon=iconpic2, fnc=main)]


