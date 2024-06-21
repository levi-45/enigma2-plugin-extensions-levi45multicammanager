#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# -------------------#
#  coded by Lululla  #
#   skin by MMark    #
#     update to      #
#       Levi45       #
#     18/04/2024     #
#      No Coppy      #
# -------------------#
from __future__ import print_function
from . import _, MYFTP
from . import Utils
from .Utils import RequestAgent
from .data.GetEcmInfo import GetEcmInfo
from Components.ActionMap import ActionMap, NumberActionMap
from Components.Button import Button
from Components.FileList import FileList
from Components.Label import Label
from Components.MenuList import MenuList
from Components.MultiContent import MultiContentEntryText
from Components.Pixmap import Pixmap
from Components.Sources.List import List
from Plugins.Plugin import PluginDescriptor
from Screens.ChoiceBox import ChoiceBox
from Screens.Console import Console
from Screens.InputBox import Input
from Screens.MessageBox import MessageBox
from Screens.Screen import Screen
from Tools.BoundFunction import boundFunction
from Tools.Directories import fileExists
from Tools.Directories import resolveFilename, SCOPE_PLUGINS
from Tools.LoadPixmap import LoadPixmap
from enigma import RT_HALIGN_LEFT, RT_VALIGN_CENTER
from enigma import eListboxPythonMultiContent
from enigma import eTimer
from enigma import gFont
from enigma import getDesktop
from os import mkdir, chmod
from time import sleep
from twisted.web.client import getPage
import codecs
import glob
import os
import re
import sys
import time

global active, skin_path, local, runningcam
active = False
_session = None

PY3 = sys.version_info.major >= 3
if PY3:
    unicode = str
    unichr = chr
    long = int
    PY3 = True

currversion = 'V.10.1-r22'
title_plug = 'Satellite-Forum.Com %s' % currversion
title_emu = 'Levi45 Emu Keys %s' % currversion
name_plug = 'Levi45 Multicam Manager'
name_plugemu = 'Levi45 Emu Keys'
plugin_foo = os.path.dirname(sys.modules[__name__].__file__)
res_plugin_foo = os.path.join(plugin_foo, 'res/')
logo = 'logo.png'
logoemu = 'logoemu.png'
keys = '/usr/keys'
camscript = '/usr/camscript'
data_path = os.path.join(plugin_foo, 'data')
FILE_XML = os.path.join(plugin_foo, 'Manager.xml')
ECM_INFO = '/tmp/ecm.info'
ereral = MYFTP.replace('+', '').replace('-', '')
FTPxx_XML = Utils.b64decoder(ereral)
_firstStarttvsman = True
local = True
ECM_INFO = '/tmp/ecm.info'
EMPTY_ECM_INFO = ('', '0', '0', '0')
old_ecm_time = time.time()
info = {}
ecm = ''
SOFTCAM = 0
CCCAMINFO = 1
OSCAMINFO = 2
global BlueAction
AgentRequest = RequestAgent()
runningcam = None


try:
    from .data.NcamInfo import NcamInfoMenu
except ImportError:
    pass

try:
    from .data.OScamInfo import OscamInfoMenu
except ImportError:
    pass

try:
    from .data.CCcamInfo import CCcamInfoMain
except ImportError:
    pass

try:
    if os.path.isfile(resolveFilename(SCOPE_PLUGINS, 'Extensions/CCcamInfo/plugin.pyc')):
        from Plugins.Extensions.CCcamInfo.plugin import CCcamInfoMain
except ImportError:
    pass

def checkdir():
    keys = '/usr/keys'
    camscript = '/usr/camscript'
    if not os.path.exists(keys):
        mkdir('/usr/keys')
    if not os.path.exists(camscript):
        mkdir('/usr/camscript')


checkdir()

skin_path = os.path.join(res_plugin_foo, "skins/hd/")
screenwidth = getDesktop(0).size()
if screenwidth.width() == 1920:
    skin_path = res_plugin_foo + 'skins/fhd/'
if screenwidth.width() == 2560:
    skin_path = res_plugin_foo + 'skins/uhd/'

if os.path.exists("/var/lib/dpkg/status"):
    skin_path = skin_path + 'dreamOs/'
if not os.path.exists('/etc/clist.list'):
    with open('/etc/clist.list', 'w'):
        print('/etc/clist.list as been create')
        os.system('chmod 755 /etc/clist.list &')


class m2list(MenuList):
    def __init__(self, list):
        MenuList.__init__(self, list, True, eListboxPythonMultiContent)
        if screenwidth.width() == 2560:
            self.l.setItemHeight(60)
            textfont = int(46)
            self.l.setFont(0, gFont('Regular', textfont))
        elif screenwidth.width() == 1920:
            self.l.setItemHeight(50)
            textfont = int(34)
            self.l.setFont(0, gFont('Regular', textfont))
        else:
            self.l.setItemHeight(50)
            textfont = int(22)
            self.l.setFont(0, gFont('Regular', textfont))


def show_list_1(h):
    res = [h]
    if screenwidth.width() == 2560:
        res.append(MultiContentEntryText(pos=(2, 0), size=(2000, 50), font=0, text=h, flags=RT_HALIGN_LEFT | RT_VALIGN_CENTER))
    elif screenwidth.width() == 1920:
        res.append(MultiContentEntryText(pos=(2, 0), size=(900, 40), font=0, text=h, flags=RT_HALIGN_LEFT | RT_VALIGN_CENTER))
    else:
        res.append(MultiContentEntryText(pos=(2, 0), size=(660, 40), font=0, text=h, flags=RT_HALIGN_LEFT | RT_VALIGN_CENTER))
    return res


def showlist(datal, list):
    icount = 0
    plist = []
    for line in datal:
        name = datal[icount]
        plist.append(show_list_1(name))
        icount = icount + 1
        list.setList(plist)


class Manager(Screen):

    def __init__(self, session):
        Screen.__init__(self, session)
        self.session = session
        global _session, BlueAction
        _session = session
        skin = os.path.join(skin_path, 'Manager.xml')
        with codecs.open(skin, "r", encoding="utf-8") as f:
            self.skin = f.read()
        self.namelist = []
        self.softcamslist = []
        try:
            self.oldService = self.session.nav.getCurrentlyPlayingServiceReference()
        except:
            self.oldService = self.session.nav.getCurrentlyPlayingServiceOrGroup()
        self["NumberActions"] = NumberActionMap(["NumberActions"], {'0': self.keyNumberGlobal,
                                                                    '1': self.keyNumberGlobal,
                                                                    '2': self.keyNumberGlobal,
                                                                    '8': self.keyNumberGlobal},)
        self['actions'] = ActionMap(['OkCancelActions',
                                     'ColorActions',
                                     'EPGSelectActions',
                                     'MenuActions'], {'ok': self.action,
                                                      'cancel': self.close,
                                                      'menu': self.configtv,
                                                      'blue': self.openemu,
                                                      # 'blue': self.Blue,
                                                      'yellow': self.download,
                                                      'green': self.action,
                                                      'info': self.cccam,
                                                      # 'info': self.CfgInfo,
                                                      'red': self.stop}, -1)
        self.setTitle(_(title_plug))
        self['title'] = Label('')
        self['key_green'] = Button(_('Start'))
        self['key_yellow'] = Button(_('Addons Panel'))
        self['key_red'] = Button(_('Stop'))
        self['key_blue'] = Button(_('Script Executor'))
        self['description'] = Label(title_plug)
        self['description'].setText(_('Scanning and retrieval list softcam ...'))
        self['info'] = Label('')
        # self['list'] = m2list([])
        self["list"] = List([])
        self.currCam = None
        self.currCam = self.readCurrent()
        self.readScripts()
        BlueAction = 'SOFTCAM'
        self.setBlueKey()
        self.timer = eTimer()
        try:
            self.timer_conn = self.timer.timeout.connect(self.cgdesc)
        except:
            self.timer.callback.append(self.cgdesc)
        self.timer.start(300, 1)
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
        global BlueAction, runningcam
        self.currCam = self.readCurrent()
        print('setBlueKey self.currCam=', self.currCam)
        self["info"].setText("Softcam")
        if self.currCam and self.currCam is not None or self.currCam != '':
            nim = str(self.currCam)
            if 'ccam' in nim.lower():
                runningcam = "cccam"
                if os.path.exists(data_path + '/CCcamInfo.pyo'):
                    BlueAction = 'CCCAMINFO'
                    self["info"].setText("Softcam")

                elif os.path.exists(data_path + '/CCcamInfo.pyc'):
                    BlueAction = 'CCCAMINFO'
                    self["info"].setText("Softcam")

            elif 'oscam' in nim.lower():
                runningcam = "oscam"
                if os.path.exists(data_path + "/OscamInfo.pyo"):
                    BlueAction = 'OSCAMINFO'
                    self["info"].setText("OSCAMINFO")

                elif os.path.exists(data_path + '/OScamInfo.pyc'):
                    BlueAction = 'OSCAMINFO'
                    self["info"].setText("OSCAMINFO")

            elif 'ncam' in nim.lower():
                runningcam = "ncam"
                if os.path.exists(data_path + "/NcamInfo.pyo"):
                    BlueAction = 'NCAMINFO'
                    self["info"].setText("NCAMINFO")

                elif os.path.exists(data_path + '/NcamInfo.pyc'):
                    BlueAction = 'NCAMINFO'
                    self["info"].setText("NCAMINFO")

        else:
            BlueAction = 'SOFTCAM'
            self["info"].setText("Softcam")
        print('Blue=', BlueAction)

    def ShowSoftcamCallback(self):
        pass

    def Blue(self):
        from Plugins.Extensions.Manager.levisemu import Levi45EmuKeysUpdater
        self.session.open(Levi45EmuKeysUpdater)

    def cccam(self):
        if BlueAction == 'CCCAMINFO':
            try:
                self.session.open(CCcamInfMain)
            except ImportError:
                pass

        if BlueAction == 'OSCAMINFO':
            try:
                from .data.OScamInfo import OscamInfoMenu
                # self.session.open(OscamInfoMenu)
                self.session.openWithCallback(self.ShowSoftcamCallback, OscamInfoMenu)
            except ImportError:
                pass

        if BlueAction == 'NCAMINFO':
            try:
                from .data.NcamInfo import NcamInfoMenu
                # self.session.open(NcamInfoMenu)
                self.session.openWithCallback(self.ShowSoftcamCallback, NcamInfoMenu)
            except ImportError:
                pass
        else:
            return

    def openemu(self):
        from Plugins.Extensions.Manager.levisemu import Levi45EmuKeysUpdater
        self.session.open(Levi45EmuKeysUpdater)

    def keyNumberGlobal(self, number):
        print('pressed', number)
        if number == 0:
            self.openemu()
        elif number == 1:
            self.CfgInfo()
        elif number == 2:
            self.cccam()
        elif number == 8:
            self.messagekd()
        else:
            return

    def setEcmInfo(self):
        try:
            self.ecminfo = GetEcmInfo()
            newEcmFound, ecmInfo = self.ecminfo.getEcm()
            if newEcmFound:
                self['info'].setText(''.join(ecmInfo))
            else:
                self.ecm()
        except Exception as e:
            print(e)

    def ecm(self):
        try:
            ecmf = ''
            if os.path.exists(ECM_INFO):
                try:
                    with open(ECM_INFO) as f:
                        self["info"].text = f.read()
                except IOError:
                    pass
            else:
                self['info'].setText(ecmf)
        except Exception as e:
            print('error ecm: ', e)

    def stopEcmInfoPollTimer(self):
        self.EcmInfoPollTimer.stop()

    def messagekd(self):
        self.session.openWithCallback(self.keysdownload, MessageBox, _('Update SoftcamKeys from google search?'), MessageBox.TYPE_YESNO)

    def keysdownload(self, result):
        if result:
            script = ('%s/auto' % plugin_foo)
            from os import access, X_OK
            if not access(script, X_OK):
                chmod(script, 493)
            import subprocess
            subprocess.check_output(['bash', script])
            self.session.open(MessageBox, _('SoftcamKeys Updated!'), MessageBox.TYPE_INFO, timeout=5)

    def CfgInfo(self):
        self.session.open(InfoCfg)

    def configtv(self):
        from Plugins.Extensions.Manager.data.datas import levi_config
        self.session.open(levi_config)

    def cgdesc(self):
        if len(self.namelist) >= 1:
            self['description'].setText(_('Select a cam to run ...'))
        else:
            self['description'].setText(_('Install Cam first!!!'))
            self.updateList()

    def getcont(self):
        cont = "Your Config':\n"
        arc = ''
        arkFull = ''
        libsssl = ''
        arcx = os.popen('uname -m').read().strip('\n\r')
        libs = os.popen('ls -l /usr/lib/libss*.*').read().strip('\n\r')
        if arcx:
            arc = arcx
            print('arc= ', arc)
        if self.arckget():
            print('arkget= ', arkFull)
            arkFull = self.arckget()
        if libs:
            libsssl = libs
        cont += ' ------------------------------------------ \n'
        cont += 'Cpu: %s\nArchitecture information: %s\nLibssl(oscam):\n%s' % (arc, arkFull, libsssl)
        cont += ' ------------------------------------------ \n'
        cont += ' Button Info for Other Info\n'
        return cont

    def arckget(self):
        zarcffll = 'by Lululla'
        try:
            zarcffll = os.popen('opkg print-architecture | grep -iE "arm|aarch64|mips|cortex|h4|sh_4"').read().strip('\n\r')
            return str(zarcffll)
        except Exception as e:
            print("Error ", e)

    def updateList(self):
        poPup = self.getcont()
        _session.open(MessageBox, poPup, MessageBox.TYPE_INFO, timeout=10)

    def openTest(self):
        pass

    def download(self):
        self.session.open(GetipklistTv)
        self.onShown.append(self.readScripts)

    def getLastIndex(self):
        a = 0
        if len(self.namelist) >= 0:
            for x in self.namelist[0]:
                if x == self.currCam:
                    return a
                a += 1
                print('aa=', a)
        # else:
            # return -1
        # return -1

    def action(self):
        i = len(self.softcamslist)
        if i < 1:
            return
        self.session.nav.stopService()
        self.last = self.getLastIndex()
        if self['list'].getCurrent():
            self.var = self['list'].getIndex()
            '''
            # self.var = self['list'].getSelectedIndex()
            # # self.var = self['list'].getSelectionIndex()
            # print('self var=== ', self.var)
            '''
            cmdx = 'chmod 755 /usr/camscript/*.*'  # + self.softcamslist[self.var][0] + '.sh'
            os.system(cmdx)
            curCam = self.readCurrent()
            if self.last is not None:
                try:
                    foldcurr = '/usr/bin/' + str(curCam)
                    foldscrpt = '/usr/camscript/' + str(curCam) + '.sh'
                    os.chmod(foldcurr, 0o755)
                    os.chmod(foldscrpt, 0o755)
                except OSError:
                    pass
            if self.last is not None:  # or self.last >= 1:
                if self.last == self.var:
                    self.cmd1 = '/usr/camscript/' + self.softcamslist[self.var][0] + '.sh' + ' cam_res &'
                    _session.open(MessageBox, _('Please wait..\nRESTART CAM'), MessageBox.TYPE_INFO, timeout=5)
                    os.system(self.cmd1)
                    sleep(1)
                else:
                    self.cmd1 = '/usr/camscript/' + self.softcamslist[self.last][0] + '.sh' + ' cam_down &'
                    _session.open(MessageBox, _('Please wait..\nSTOP & RESTART CAM'), MessageBox.TYPE_INFO, timeout=5)
                    os.system(self.cmd1)
                    sleep(1)
                    self.cmd1 = '/usr/camscript/' + self.softcamslist[self.var][0] + '.sh' + ' cam_up &'
                    os.system(self.cmd1)
            else:
                try:
                    self.cmd1 = '/usr/camscript/' + self.softcamslist[self.var][0] + '.sh' + ' cam_up &'
                    _session.open(MessageBox, _('Please wait..\nSTART UP CAM'), MessageBox.TYPE_INFO, timeout=5)
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
            self.session.nav.playService(self.oldService)
            self.EcmInfoPollTimer.start(200)
            self.readScripts()

    def writeFile(self):
        if self.currCam != '' or self.currCam is not None:
            print('self.currCam= 2 ', self.currCam)
            if sys.version_info[0] == 3:
                clist = open('/etc/clist.list', 'w', encoding='UTF-8')
            else:
                clist = open('/etc/clist.list', 'w')
            os.system('chmod 755 /etc/clist.list &')
            clist.write(str(self.currCam))
            clist.close()
        if sys.version_info[0] == 3:
            stcam = open('/etc/startcam.sh', 'w', encoding='UTF-8')
        else:
            stcam = open('/etc/startcam.sh', 'w')
        stcam.write('#!/bin/sh\n' + self.cmd1)
        stcam.close()
        os.system('chmod 755 /etc/startcam.sh &')
        return

    def stop(self):
        i = len(self.softcamslist)
        if i < 1:
            return
        global BlueAction
        print('Blue3=', BlueAction)
        if self.currCam != 'None' or self.currCam is not None:
            self.EcmInfoPollTimer.stop()
            self.last = self.getLastIndex()
            if self.last is not None:  # or self.currCam != 'no':
                self.cmd1 = '/usr/camscript/' + self.softcamslist[self.last][0] + '.sh' + ' cam_down &'
                os.system(self.cmd1)

                self.currCam = None
                self.writeFile()
                sleep(1)
                if os.path.exists(ECM_INFO):
                    os.remove(ECM_INFO)
                _session.open(MessageBox, _('Please wait..\nSTOP CAM'), MessageBox.TYPE_INFO, timeout=5)
                self['info'].setText('CAM STOPPED')
                try:
                    self.oldService = self.session.nav.getCurrentlyPlayingServiceReference()
                except:
                    self.oldService = self.session.nav.getCurrentlyPlayingServiceOrGroup()
                self.session.nav.stopService()
                BlueAction = 'SOFTCAM'
                self.readScripts()

    def readScripts(self):
        try:
            scriptlist = []
            pliste = []
            self.index = 0
            s = 0
            pathscript = '/usr/camscript/'
            for root, dirs, files in os.walk(pathscript):
                for name in files:
                    scriptlist.append(name)
                    s += 1
            i = len(self.softcamslist)
            del self.softcamslist[0:i]
            png1 = LoadPixmap(cached=True,
                              path=resolveFilename(SCOPE_PLUGINS,
                                                   "Extensions/Manager/res/img/{}".format('actcam.png')))
            png2 = LoadPixmap(cached=True,
                              path=resolveFilename(SCOPE_PLUGINS,
                                                   "Extensions/Manager/res/img/{}".format('defcam.png')))
            if s >= 1:
                for lines in scriptlist:
                    dat = pathscript + lines
                    if sys.version_info[0] == 3:
                        sfile = open(dat, 'r', encoding='UTF-8')
                    else:
                        sfile = open(dat, 'r')
                    for line in sfile:
                        if line[0:3] == 'OSD':
                            nam = line[5:len(line) - 2]
                            print('We are in Manager and cam is type  = ', nam)
                            if self.currCam != 'None' or self.currCam is not None:
                                if nam == self.currCam:
                                    self.softcamslist.append((nam,  png1, '(Active)'))
                                    pliste.append((nam, '(Active)'))
                                else:
                                    self.softcamslist.append((nam, png2, ''))
                                    pliste.append((nam, ''))
                            else:
                                self.softcamslist.append(nam, png2, '')
                                pliste.append(nam, '')
                            self.index += 1
                sfile.close()
                self.softcamslist.sort(key=lambda i: i[2], reverse=True)
                pliste.sort(key=lambda i: i[1], reverse=True)
                self.namelist = pliste
                self["list"].setList(self.softcamslist)
                self.setBlueKey()
        except Exception as e:
            print('error scriptlist: ', e)

    def readCurrent(self):
        currCam = None
        self.FilCurr = ''
        if fileExists('/etc/CurrentBhCamName'):
            self.FilCurr = '/etc/CurrentBhCamName'
        else:
            self.FilCurr = '/etc/clist.list'
        if os.stat(self.FilCurr).st_size > 0:
            try:
                if sys.version_info[0] == 3:
                    clist = open(self.FilCurr, 'r', encoding='UTF-8')
                else:
                    clist = open(self.FilCurr, 'r')
            except:
                return
            if clist is not None:
                for line in clist:
                    currCam = line
                clist.close()
        return currCam

    '''
    def autocam(self):
        current = None
        try:
            if sys.version_info[0] == 3:
                clist = open(self.FilCurr, 'r', encoding='UTF-8')
            else:
                clist = open(self.FilCurr, 'r')
            print('found list')
        except:
            return

        if clist is not None:
            for line in clist:
                current = line
            clist.close()
        print('current =', current)
        if os.path.isfile('/etc/autocam.txt') is False:
            if sys.version_info[0] == 3:
                alist = open('/etc/autocam.txt', 'w', encoding='UTF-8')
            else:
                alist = open('/etc/autocam.txt', 'w')
            alist.close()
        self.autoclean()
        if sys.version_info[0] == 3:
            alist = open('/etc/autocam.txt', 'a', encoding='UTF-8')
        else:
            alist = open('/etc/autocam.txt', 'a')
        alist.write(self.oldService.toString() + '\n')
        self.last = self.getLastIndex()
        alist.write(current + '\n')
        alist.close()
        _session.open(MessageBox, _('Autocam assigned to the current channel'), MessageBox.TYPE_INFO, timeout=5)
        return

    def autoclean(self):
        delemu = 'no'
        if os.path.isfile('/etc/autocam.txt') is False:
            return
        if sys.version_info[0] == 3:
            myfile = open('/etc/autocam.txt', 'r', encoding='UTF-8')
        else:
            myfile = open('/etc/autocam.txt', 'r')

        if sys.version_info[0] == 3:
            myfile2 = open('/etc/autocam2.txt', 'w', encoding='UTF-8')
        else:
            myfile2 = open('/etc/autocam2.txt', 'w')
        icount = 0
        for line in myfile.readlines():
            print('We are in Manager line, self.oldService.toString() =', line, self.oldService.toString())
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
        '''

    def cancel(self):
        self.close()


class GetipklistTv(Screen):

    def __init__(self, session):
        self.session = session
        skin = os.path.join(skin_path, 'GetipkTv.xml')
        with open(skin, 'r') as f:
            self.skin = f.read()
        Screen.__init__(self, session)
        self.names = []
        self.names_1 = []
        self.list = []
        self['text'] = m2list([])
        self.setTitle(_(title_plug))
        self['title'] = Label(_(title_plug))
        self['description'] = Label(_('Getting the list, please wait ...'))
        self['key_red'] = Button(_('Back'))
        self['key_green'] = Button(_('Load'))
        self['key_yellow'] = Button()
        self['key_blue'] = Button()
        self['key_green'].hide()
        if os.path.exists(FILE_XML):
            self['key_green'].show()
        self['key_yellow'].hide()
        self['key_blue'].hide()
        self.addon = 'emu'
        self.url = ''
        global local
        local = False
        self.icount = 0
        self.downloading = False
        self.xml = str(FTPxx_XML)
        self.timer = eTimer()
        if os.path.exists('/var/lib/dpkg/status'):
            self.timer_conn = self.timer.timeout.connect(self._gotPageLoad)
        else:
            self.timer.callback.append(self._gotPageLoad)
        self.timer.start(500, 1)
        self['actions'] = ActionMap(['OkCancelActions',
                                     'ColorActions'], {'ok': self.okClicked, 'cancel': self.close, 'green': self.loadpage}, -1)
        # self.onShown.append(self.get_list)

    def loadpage(self):
        global local
        if os.path.exists(FILE_XML):
            self.lists = []
            del self.names[:]
            del self.list[:]
            self["list"].l.setList(self.list)
            with open(FILE_XML, 'r') as f:
                self.xml = f.read()
                local = True
            self._gotPageLoad()

    def downloadxmlpage(self):
        url = str(FTPxx_XML)
        getPage(str.encode(url)).addCallback(self._gotPageLoad).addErrback(self.errorLoad)

    def errorLoad(self, error):
        print(str(error))
        self['description'].setText(_('Try again later ...'))
        self.downloading = False

    def _gotPageLoad(self):
        global local
        if local is False:
            self.xml = Utils.checkGZIP(self.xml)
        try:
            # regexC = '<plugins cont = "(.*?)"'
            regexC = '<plugins cont="(.*?)"'
            match = re.compile(regexC, re.DOTALL).findall(self.xml)
            for name in match:
                name = Utils.ensure_str(name)
                self.list.append(name)
                self['description'].setText(_('Please select ...'))
            showlist(self.list, self['text'])
            self.downloading = True
        except:
            self['description'].setText(_('Try again later ...'))
            pass

    def okClicked(self):
        i = len(self.list)
        if i < 0:
            return
        if self.downloading is True:
            try:
                idx = self["text"].getSelectedIndex()
                name = self.list[idx]
                self.session.open(GetipkTv, self.xml, name)
            except:
                return
        else:
            self.close()


class GetipkTv(Screen):
    def __init__(self, session, xmlparse, selection):
        self.session = session
        skin = os.path.join(skin_path, 'GetipkTv.xml')
        with codecs.open(skin, "r", encoding="utf-8") as f:
            self.skin = f.read()
        Screen.__init__(self, session)
        self.xmlparse = xmlparse
        self.selection = selection
        self['text'] = m2list([])
        self.list = []
        self.setTitle(_(title_plug))
        self['title'] = Label(_(title_plug))
        self['description'] = Label(_('Select and Install'))
        self['key_red'] = Button(_('Back'))
        self['key_green'] = Button()
        self['key_yellow'] = Button()
        self['key_blue'] = Button()
        self['key_green'].hide()
        self['key_yellow'].hide()
        self['key_blue'].hide()
        self['actions'] = ActionMap(['OkCancelActions'], {'ok': self.message, 'cancel': self.close}, -1)
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
        # regex = '<plugin name="(.*?)".*?url>"(.*?)"</url'
        match = re.compile(regex, re.DOTALL).findall(data1)
        for name, url in match:
            name = name.replace('_', ' ').replace('-', ' ')
            name = Utils.ensure_str(name)
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
        i = len(self.names)
        if i < 0:
            return
        self.session.openWithCallback(self.selclicked, MessageBox, _('Do you want to install?'), MessageBox.TYPE_YESNO)

    def selclicked(self, result):
        if result:
            idx = self["text"].getSelectedIndex()
            dom = self.names[idx]
            com = self.urls[idx]
            self.prombt(com, dom)

    def dowfil(self):
        self.dest = '/tmp/' + self.downplug
        if fileExists(self.dest):
            os.remove(self.dest)
        if PY3:
            import urllib.request as urllib2
            import http.cookiejar as cookielib
        else:
            import urllib2
            import cookielib
        headers = {'User-Agent': RequestAgent()}
        cookie_jar = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar))
        urllib2.install_opener(opener)
        try:
            req = urllib2.Request(self.com, data=None, headers=headers)
            handler = urllib2.urlopen(req, timeout=15)
            data = handler.read()
            with open(self.dest, 'wb') as f:
                f.write(data)
            print('MYDEBUG - download ok - URL: %s , filename: %s' % (self.com, self.dest))
        except:
            print('MYDEBUG - download failed - URL: %s , filename: %s' % (self.com, self.dest))
            self.dest = ''
        return self.dest

    def prombt(self, com, dom):
        try:
            self.com = str(com)
            self.dom = str(dom)
            self.timer = eTimer()
            extensionlist = self.com.split('.')
            extension = extensionlist[-1]
            self.downplug = self.com.split("/")[-1]
            down = self.dowfil()
            from os import popen
            cmd22 = 'find /usr/bin -name "wget"'
            res = popen(cmd22).read()
            if 'wget' not in res.lower():
                if os.path.exists('/var/lib/dpkg/info'):
                    cmd23 = 'apt-get update && apt-get install wget'
                else:
                    cmd23 = 'opkg update && opkg install wget'
                popen(cmd23)
            if self.com.find('.ipk') != -1:
                cmd = "opkg install --force-reinstall %s > /dev/null" % down
                self.session.open(Console, _('Downloading-installing: %s') % self.dom, [cmd], closeOnSuccess=False)

            if len(extensionlist) > 1:
                tar = extensionlist[-2]
            if extension in ["gz", "bz2"] and tar == "tar":
                self.command = ['']
                # self.dest = self.dowfil()
                if extension == "gz":
                    self.command = ["tar -xzvf " + down + " -C /"]
                elif extension == "bz2":
                    self.command = ["tar -xjvf " + down + " -C /"]
                cmd = "wget --no-cache --no-dns-cache -U '%s' -c '%s' -O '%s' --post-data='action=purge';%s > /dev/null" % (AgentRequest, str(self.com), down, self.command[0])
                if "https" in str(self.com):
                    cmd = "wget --no-check-certificate --no-cache --no-dns-cache -U '%s' -c '%s' -O '%s' --post-data='action=purge';%s > /dev/null" % (AgentRequest, str(self.com), down, self.command[0])
                self.session.open(Console, title='Installation %s' % self.dom, cmdlist=[cmd, 'sleep 5'])  # , finishedCallback=self.msgipkinst)

            if extension == 'deb':
                if not os.path.exists('/var/lib/dpkg/status'):
                    self.session.open(MessageBox, _('Unknow Image!'), MessageBox.TYPE_INFO, timeout=5)
                else:
                    cmd22 = 'find /usr/bin -name "wget"'
                    res = os.popen(cmd22).read()
                    if 'wget' not in res.lower():
                        cmd23 = 'apt-get update && apt-get install wget'
                        os.popen(cmd23)
                    cmd = 'dpkg -i %s' % down
                    self.session.open(Console, _('Downloading-installing: %s') % self.dom, [cmd], closeOnSuccess=False)

            if extension == 'zip':
                cmd = ["wget --no-cache --no-dns-cache -U '%s' -c '%s' -O '%s --post-data='action=purge' > /dev/null' " % (RequestAgent(), str(self.com), down)]
                self.session.open(Console, _('Downloading: %s') % self.dom, cmd, closeOnSuccess=False)
                self.session.open(MessageBox, _('Download file in /tmp successful!'), MessageBox.TYPE_INFO, timeout=5)
            self.timer.start(500, 1)
        except:
            self.mbox = self.session.open(MessageBox, _('Download failur!'), MessageBox.TYPE_INFO, timeout=5)
            # self.addondel()
            return

    def addondel(self):
        try:
            files = glob.glob('/tmp/download.*', recursive=False)
            for f in files:
                try:
                    os.remove(f)
                except OSError as e:
                    print('Error: %s : %s' % (f, e.strerror))
            self.mbox = self.session.open(MessageBox, _('All file Download are removed!'), MessageBox.TYPE_INFO, timeout=5)

        except Exception as e:
            print(e)


class InfoCfg(Screen):
    def __init__(self, session):
        self.session = session
        skin = os.path.join(skin_path, 'InfoCfg.xml')
        with codecs.open(skin, "r", encoding="utf-8") as f:
            self.skin = f.read()
        Screen.__init__(self, session)
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
        self['key_green'] = Button()
        self['key_yellow'] = Button()
        self['key_blue'] = Button()
        self['key_green'].hide()
        self['key_yellow'].hide()
        self['key_blue'].hide()
        self.setTitle(_(title_plug))

        self['title'] = Label(_(title_plug))
        self['description'] = Label(_('Path Configuration Folder'))
        self.onShown.append(self.updateList)

    def getcont(self):
        cont = " ---- Type Cam For Your Box--- \n"
        cont += "Config Softcam Manager(Oscam)':\n"
        cont += "Default folder:\n"
        cont += "etc/tuxbox/config\n"
        cont += ' ------------------------------------------ \n'
        cont += ' ---- Type Oscam For Your Box--- \n'
        arc = ''
        arkFull = ''
        libsssl = ''
        arcx = os.popen('uname -m').read().strip('\n\r')
        libs = os.popen('ls -l /usr/lib/libss*.*').read().strip('\n\r')
        if arcx:
            arc = arcx
            print('arc= ', arc)
        if self.arckget():
            print('arkget= ', arkFull)
            arkFull = self.arckget()
        if libs:
            libsssl = libs
        cont += ' ------------------------------------------ \n'
        cont += 'Cpu: %s\nArchitecture information: %s\nLibssl(oscam):\n%s\n' % (arc, arkFull, libsssl)
        cont += ' ------------------------------------------ \n'
        return cont

    def updateList(self):
        self['text'].setText(self.getcont())

    def arckget(self):
        zarcffll = 'by Lululla'
        try:
            if os.path.exists('/var/lib/dpkg/info'):
                zarcffll = os.popen('dpkg --print-architecture | grep -iE "arm|aarch64|mips|cortex|sh4|sh_4"').read().strip('\n\r')
            else:
                zarcffll = os.popen('opkg print-architecture | grep -iE "arm|aarch64|mips|cortex|h4|sh_4"').read().strip('\n\r')
            return str(zarcffll)
        except Exception as e:
            print("Error ", e)

    def Down(self):
        self['text'].pageDown()

    def Up(self):
        self['text'].pageUp()


class Ipkremove(Screen):

    def __init__(self, session, args=None):
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
                listc[icount] = (line, '')
                ebuf.append(listc[icount])
                icount += 1
            myfile.close()
            self.session.openWithCallback(self.test2, ChoiceBox, title='Please select ipkg to remove', list=ebuf)
            self.close()
        except:
            self.close()

    def test2(self, returnValue):
        if returnValue is None:
            return
        else:
            print('returnValue', returnValue)
            ipkname = returnValue[0]
            cmd = 'opkg remove ' + ipkname[:-1] + ' >/var/volatile/tmp/ipk.log'
            os.system(cmd)
            cmd = 'touch /etc/tmpfile'
            os.system(cmd)
            myfile = open('/var/lib/opkg/status', 'r')
            f = open('/etc/tmpfile', 'w')
            for line in myfile:
                if line != ipkname:
                    f.write(line)
            f.close()
            f = open('/etc/tmpfile', 'r+')
            f.close()
            f = open('/var/lib/opkg/status', 'r+')
            f.close()
            cmd = 'rm /var/lib/opkg/status'
            os.system(cmd)
            cmd = 'mv /etc/tmpfile /var/lib/opkg/status'
            os.system(cmd)
            f = open('/var/lib/opkg/status', 'r+')
            f.close()
        return

    def callback(self, answer):
        print('answer:', answer)

    def keyLeft(self):
        self['text'].left()

    def keyRight(self):
        self['text'].right()

    def ok(self):
        selection = self['list'].getSelection()
        if selection[1] is True:
            self['list'].changeDir(selection[0])
        else:
            self['pixmap'].instance.setPixmapFromFile(selection[0])

    def keyNumberGlobal(self, number):
        print('pressed', number)
        self['text'].number(number)


def startConfig(session, **kwargs):
    session.open(Manager)


def mainmenu(menu_id):
    if menu_id == "setup":
        return [(_("Levi45 Softcam Manager"), startConfig, "Levi45 Softcam Manager", 50)]
    else:
        return []


class AutoStartTimertvman:

    def __init__(self, session):
        self.session = session
        global _firstStarttvsman
        print("*** running AutoStartTimertvman ***")
        if _firstStarttvsman:
            self.runUpdate()

    def runUpdate(self):
        print("*** running update ***")
        try:
            from . import Update
            Update.upd_done()
            _firstStarttvsman = False
        except Exception as e:
            print('error manager', str(e))


def autostart(reason, session=None, **kwargs):
    """called with reason=1 to during shutdown, with reason=0 at startup?"""
    print('[Softcam] Started')
    global autoStartTimertvsman
    global _firstStarttvsman
    if reason == 0:
        print('reason 0')
        if session is not None:
            print('session none')
            try:
                print('ok started autostart')
                if fileExists('/etc/init.d/dccamd'):
                    os.system('mv /etc/init.d/dccamd /etc/init.d/dccamdOrig &')
                if fileExists('/usr/bin/dccamd'):
                    os.system("mv /usr/bin/dccamd /usr/bin/dccamdOrig &")
                os.system('ln -sf /usr/bin /var/bin')
                os.system('ln -sf /usr/keys /var/keys')
                os.system('ln -sf /usr/scce /var/scce')
                # os.system('ln -sf /usr/camscript /var/camscript')
                os.system('sleep 2')
                os.system('/etc/startcam.sh &')
                os.system('sleep 2')
                print("*** running autostart ***")
                _firstStarttvsman = True
                autoStartTimertvsman = AutoStartTimertvman(session)
            except:
                print('except autostart')
        else:
            print('pass autostart')
    return


def menu(menu_id, **kwargs):
    if menu_id == 'cam':
        return [(_(name_plug), boundFunction(main, showExtentionMenuOption=True), 'Levi45 Softcam Manager', -1)]
    else:
        return []


def main(session, **kwargs):
    try:
        session.open(Manager)
    except:
        pass


def main2(session, **kwargs):
    from . import levisemu
    session.open(levisemu.Levi45EmuKeysUpdater)


def menuemu(menu_id):
    if menu_id == 'mainmenu':
        return [(name_plugemu, main2, 'Levi45 Emu Keys Updater', 45)]
    else:
        return []


def StartSetup(menu_id):
    if menu_id == 'mainmenu':
        return [(name_plug, main, 'Levi45 Softcam Manager', 44)]
    else:
        return []


# plugin
mainDescriptor = PluginDescriptor(name=_(name_plug), where=[PluginDescriptor.WHERE_MENU], fnc=mainmenu)
extDescriptor = PluginDescriptor(name=_(name_plug), description=_(title_plug), where=[PluginDescriptor.WHERE_EXTENSIONSMENU], icon=logo, fnc=main)
plugDescriptor = PluginDescriptor(name=_(name_plug), description=_(title_plug), where=[PluginDescriptor.WHERE_PLUGINMENU], icon=logo, fnc=main)
menuDescriptor = PluginDescriptor(name=_(name_plug), description=_(title_plug), where=[PluginDescriptor.WHERE_MENU], icon=logo, fnc=StartSetup)
startDescriptor = PluginDescriptor(name=_(name_plug), description=_(title_plug), where=[PluginDescriptor.WHERE_AUTOSTART, PluginDescriptor.WHERE_SESSIONSTART], needsRestart=True, fnc=autostart)
# emu
mainemuDescriptor = PluginDescriptor(name=_(name_plugemu), description=_(title_emu), where=[PluginDescriptor.WHERE_MENU], icon=logoemu, fnc=menuemu)
plugemuDescriptor = PluginDescriptor(name=_(name_plugemu), description=_(title_emu), where=[PluginDescriptor.WHERE_PLUGINMENU], icon=logoemu, fnc=main2)
extemuDescriptor = PluginDescriptor(name=_(name_plugemu), description=_(title_emu), where=[PluginDescriptor.WHERE_EXTENSIONSMENU], icon=logoemu, fnc=main2)


def Plugins(**kwargs):
    logo = 'logo.png'
    logoemu = 'logoemu.png'
    if screenwidth.width() == 1920:
        logo = plugin_foo + '/res/pics/logo.png'
        logoemu = plugin_foo + '/res/pics/logoemu.png'
    result = []
    result.append(mainDescriptor)
    result.append(extDescriptor)
    result.append(plugDescriptor)
    result.append(startDescriptor)
    result.append(menuDescriptor)
    return result
