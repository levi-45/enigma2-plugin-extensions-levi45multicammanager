# #!/usr/bin/env python
# -*- coding: UTF-8 -*-

# --------------------#
#  coded by Lululla   #
#   skin by MMark     #
#     26/06/2024     #
#      No Coppy       #
# --------------------#
from __future__ import print_function
from Components.ActionMap import ActionMap
from Components.Button import Button
from Components.ConfigList import ConfigListScreen
from Components.Label import Label
from Components.config import ConfigNumber, ConfigSelection, ConfigYesNo
from Components.config import ConfigSubsection, ConfigPassword
from Components.config import config, ConfigText
from Components.config import getConfigListEntry, NoSave
from Screens.MessageBox import MessageBox
from Screens.Screen import Screen
from Screens.VirtualKeyBoard import VirtualKeyBoard
from Tools.Directories import fileExists
from Tools.Directories import resolveFilename, SCOPE_PLUGINS
from Components.Sources.StaticText import StaticText
from .. import _
from ..plugin import runningcam
from random import choice
from enigma import eTimer
from enigma import getDesktop
import os
import re
import ssl
import sys
import subprocess
import codecs
global skin_path
import base64
sss = 'aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L1U0ZU02RGpW'
PY3 = sys.version_info.major >= 3
if PY3:
    unicode = str
    unichr = chr
    long = int
    PY3 = True


def b64decoder(s):
    """Add missing padding to string and return the decoded base64 string."""
    import base64
    s = str(s).strip()
    try:
        outp = base64.b64decode(s)
        print('outp1 ', outp)
        if PY3:
            outp = outp.decode('utf-8')
            print('outp2 ', outp)
    except TypeError:
        padding = len(s) % 4
        if padding == 1:
            print("Invalid base64 string: {}".format(s))
            return ''
        elif padding == 2:
            s += b'=='
        elif padding == 3:
            s += b'='
        outp = base64.b64decode(s)
        print('outp1 ', outp)
        if PY3:
            outp = outp.decode('utf-8')
            print('outp2 ', outp)
    return outp


sl = 'slManager'
name_plug = 'Satellite-Forum.Com'
plugin_path = resolveFilename(SCOPE_PLUGINS, "Extensions/Manager/")
data_path = os.path.join(plugin_path, 'data/')
skin_path = plugin_path
sl2 = skin_path + sl + '.xml'
if os.path.exists(sl2):
    os.system('rm -rf ' + plugin_path + ' > /dev/null 2>&1')

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context


def checkStr(txt):
    if PY3:
        if isinstance(type(txt), type(bytes())):
            txt = txt.decode('utf-8')
    else:
        if isinstance(type(txt), type(unicode())):
            txt = txt.encode('utf-8')
    return txt


ListAgent = [
          'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15',
          'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14',
          'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13',
          'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13',
          'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13',
          'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13',
          'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1284.0 Safari/537.13',
          'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.8 (KHTML, like Gecko) Chrome/17.0.940.0 Safari/535.8',
          'Mozilla/6.0 (Windows NT 6.2; WOW64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1',
          'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1',
          'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1',
          'Mozilla/5.0 (Windows NT 6.1; rv:15.0) Gecko/20120716 Firefox/15.0a2',
          'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.16) Gecko/20120427 Firefox/15.0a1',
          'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1',
          'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:15.0) Gecko/20120910144328 Firefox/15.0.2',
          'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1',
          'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:9.0a2) Gecko/20111101 Firefox/9.0a2',
          'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110613 Firefox/6.0a2',
          'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110612 Firefox/6.0a2',
          'Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20110814 Firefox/6.0',
          'Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0',
          'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
          'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
          'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)',
          'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)',
          'Mozilla/4.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)',
          'Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)',
          'Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0;  it-IT)',
          'Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US)'
          'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; chromeframe/13.0.782.215)',
          'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; chromeframe/11.0.696.57)',
          'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0) chromeframe/10.0.648.205',
          'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.1; SV1; .NET CLR 2.8.52393; WOW64; en-US)',
          'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; chromeframe/11.0.696.57)',
          'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/4.0; GTB7.4; InfoPath.3; SV1; .NET CLR 3.1.76908; WOW64; en-US)',
          'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.2; SV1; .NET CLR 3.3.69573; WOW64; en-US)',
          'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)',
          'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; InfoPath.1; SV1; .NET CLR 3.8.36217; WOW64; en-US)',
          'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
          'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; it-IT)',
          'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)',
          'Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02',
          'Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00',
          'Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00',
          'Opera/12.0(Windows NT 5.2;U;en)Presto/22.9.168 Version/12.00',
          'Opera/12.0(Windows NT 5.1;U;en)Presto/22.9.168 Version/12.00',
          'Mozilla/5.0 (Windows NT 5.1) Gecko/20100101 Firefox/14.0 Opera/12.0',
          'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25',
          'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
          'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10',
          'Mozilla/5.0 (iPad; CPU OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko ) Version/5.1 Mobile/9B176 Safari/7534.48.3',
          ]


def RequestAgent():
    RandomAgent = choice(ListAgent)
    return RandomAgent


def getUrl(url):
    if sys.version_info.major == 3:
        import urllib.request as urllib2
    elif sys.version_info.major == 2:
        import urllib2
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14')
    r = urllib2.urlopen(req, None, 15)
    link = r.read()
    r.close()
    content = link
    if str(type(content)).find('bytes') != -1:
        try:
            content = content.decode("utf-8")
        except Exception as e:
            print("Error: %s." % str(e))
    return content


skin_path = os.path.join(plugin_path, 'res/skins/hd/')
res_plugin_path = os.path.join(plugin_path, "res/")
screenwidth = getDesktop(0).size()
if screenwidth.width() == 1920:
    skin_path = res_plugin_path + 'skins/fhd/'
if screenwidth.width() == 2560:
    skin_path = res_plugin_path + 'skins/uhd/'
if os.path.exists('/var/lib/dpkg/info'):
    skin_path = skin_path + 'dreamOs/'
if os.path.exists(sl2):
    os.system('rm -rf ' + plugin_path + ' > /dev/null 2>&1')


def cccamPath():
    import os
    cmd = 'find /usr -name "CCcam.cfg"'
    res = os.popen(cmd).read()
    if res == '':
        cmd = 'find /var -name "CCcam.cfg"'
        res = os.popen(cmd).read()
        if res == '':
            cmd = 'find /etc -name "CCcam.cfg"'
            res = os.popen(cmd).read()
            if res == '':
                try:
                    folders = os.listdir('/etc/tuxbox/')
                    for folder in folders:
                        if folder.startswith('oscam'):
                            cmd = 'find /etc/tuxbox/config/' + folder + ' -name "CCcam.cfg"'
                            res = os.popen(cmd).read()
                            return '/etc/tuxbox/config/' + folder + "CCcam.cfg"
                        if res == '':
                            return "/etc/CCcam.cfg"
                except:
                    return "/etc/CCcam.cfg"
            else:
                return "/etc/CCcam.cfg"
        else:
            return "/var/CCcam.cfg"
    else:
        return "/usr/CCcam.cfg"
    return "/etc/CCcam.cfg"


Serverlive = [
              ('aHR0cHM6Ly9ib3NzY2NjYW0uY28vVGVzdC5waHA=', 'Server01'),
              ('aHR0cHM6Ly9pcHR2LTE1ZGF5cy5ibG9nc3BvdC5jb20=', 'Server02'),
              ('aHR0cHM6Ly9jY2NhbWlhLmNvbS9mcmVlLWNjY2FtLw==', 'Server03'),
              ('aHR0cHM6Ly9jY2NhbS5uZXQvZnJlZWNjY2Ft', 'Server04'),
              ('aHR0cHM6Ly9jY2NhbXNhdGUuY29tL2ZyZWU=', 'Server05'),
              ('aHR0cHM6Ly9jY2NhbXguY29tL2ZyZWUtY2NjYW0=', 'Server06'),
              ('aHR0cHM6Ly9jY2NhbS1wcmVtaXVtLmNvL2ZyZWUtY2NjYW0v', 'Server07'),
              ('aHR0cHM6Ly93d3cuY2NjYW1iaXJkMi5jb20vZnJlZWNjY2FtLnBocA==', 'Server08'),
              ('aHR0cHM6Ly9jY2NhbWZyZWUuY28vZnJlZS9nZXQucGhw', 'Server9'),
              ('aHR0cHM6Ly9jY2NhbWZyZWkuY29tL2ZyZWUvZ2V0LnBocA==', 'Server10'),
              ('aHR0cHM6Ly9jY2NhbWlwdHYuY2x1Yi9mcmVlLWNjY2FtLw==', 'Server11'),
              ]

# cfgcam = [(cccamPath(), 'CCcam'),
cfgcam = [('/etc/CCcam.cfg', 'CCcam'),
          ('/etc/tuxbox/config/oscam.server', 'Oscam'),
          ('/etc/tuxbox/config/oscam-emu/oscam.server', 'oscam-emu'),
          ('/etc/tuxbox/config/ncam.server', 'Ncam'),
          ('/etc/tuxbox/config/gcam.server', 'Gcam'),
          ('/etc/tuxbox/config/Oscamicam/oscam.server', 'Oscamicam')]

config.plugins.Manager = ConfigSubsection()
config.plugins.Manager.active = ConfigYesNo(default=False)
config.plugins.Manager.Server = NoSave(ConfigSelection(choices=Serverlive))  # , default=Server1))
# config.plugins.Manager.cfgfile = NoSave(ConfigSelection(default='/etc/CCcam.cfg', choices=[('/etc/CCcam.cfg', _('CCcam')), ('/etc/tuxbox/config/oscam.server', _('Oscam')), ('/etc/tuxbox/config/ncam.server', _('Ncam'))]))
config.plugins.Manager.cfgfile = NoSave(ConfigSelection(choices=cfgcam))
config.plugins.Manager.hostaddress = NoSave(ConfigText(default='127.0.0.1'))
config.plugins.Manager.port = NoSave(ConfigNumber(default=15000))
config.plugins.Manager.user = NoSave(ConfigText(default='Enter Username', visible_width=50, fixed_size=False))
config.plugins.Manager.passw = NoSave(ConfigPassword(default='******', fixed_size=False, censor='*'))

# ===================================================
host = str(config.plugins.Manager.hostaddress.value)
port = str(config.plugins.Manager.port.value)
user = str(config.plugins.Manager.user.value)
password = str(config.plugins.Manager.passw.value)


def putlblcfg():
    global rstcfg
    global buttn
    global putlbl
    putlbl = config.plugins.Manager.cfgfile.getValue()
    buttn = ''
    if putlbl == '/etc/CCcam.cfg':
        buttn = _('Write') + ' CCcam'
        rstcfg = 'CCcam.cfg'
    elif putlbl == '/etc/tuxbox/config/oscam.server':
        buttn = _('Write') + ' Oscam'
        rstcfg = 'oscam.server'
    elif putlbl == '/etc/tuxbox/config/gcam.server':
        buttn = _('Write') + ' Gcam'
        rstcfg = 'gcam.server'
    elif putlbl == '/etc/tuxbox/config/oscam-emu/oscam.server':
        buttn = _('Write') + ' OscamEmu'
        rstcfg = 'oscam.server'
    elif putlbl == '/etc/tuxbox/config/Oscamicam/oscam.server':
        buttn = _('Write') + ' Oscamicam'
        rstcfg = 'oscam.server'
    elif putlbl == '/etc/tuxbox/config/ncam.server':
        buttn = _('Write') + ' Ncam'
        rstcfg = 'ncam.server'


putlblcfg()


class levi_config(Screen, ConfigListScreen):
    def __init__(self, session):
        Screen.__init__(self, session)
        self.session = session
        skin = os.path.join(skin_path, 'levi_config.xml')
        with codecs.open(skin, "r", encoding="utf-8") as f:
            self.skin = f.read()
        self.setup_title = (name_plug)
        self.onChangedEntry = []
        self.list = []
        ConfigListScreen.__init__(self, self.list, session=self.session, on_change=self.changedEntry)
        self['title'] = Label(_(name_plug))
        self['actions'] = ActionMap(['OkCancelActions',
                                     'DirectionActions',
                                     'setupActions',
                                     'ColorActions',
                                     'VirtualKeyboardActions',
                                     'MenuActions',
                                     'InfobarChannelSelection'], {'left': self.keyLeft,
                                                                  'right': self.keyRight,
                                                                  'ok': self.closex,
                                                                  'showVirtualKeyboard': self.KeyText,
                                                                  'green': self.green,
                                                                  'yellow': self.sendemm,
                                                                  'blue': self.resetcfg,
                                                                  'red': self.closex,
                                                                  'cancel': self.closex,
                                                                  'back': self.closex}, -1)
        self['key_red'] = Button(_('Back'))
        self['key_green'] = Button(_('Force Emm Send'))
        self['key_yellow'] = Button(_('Check Emm Send'))
        self["key_blue"] = Button(_(''))
        # self['key_green'].hide()
        # self['key_yellow'].hide()
        self['key_blue'].hide()
        self['info'] = Label('')
        self['description'] = Label('')
        self['description'].setText(_('Wait please...'))
        self.createSetup()
        if self.selectionChanged not in self["config"].onSelectionChanged:
            self["config"].onSelectionChanged.append(self.selectionChanged)
        self.selectionChanged()
        self.onLayoutFinish.append(self.layoutFinished)

    def layoutFinished(self):
        self.setTitle(self.setup_title)
        self['info'].setText(_('Select Your Choice'))

    def sendemm(self):
        if config.plugins.Manager.active.value is True:
            self.getcl()
        else:
            try:
                print('runningcam=', runningcam)
                if runningcam == None:
                    return
                # if runningcam == 'oscam' or runningcam == 'ncam':
                if runningcam == 'oscam':
                    cmd = 'ps -T'
                    res = os.popen(cmd).read()
                    print('res: ', res)
                    if 'oscam' in res.lower() or 'icam' in res.lower() or 'ncam' in res.lower() or 'gcam' in res.lower():
                        print('oscam exist')
                        msg = []
                        msg.append(_("\n....\n.....\n"))
                        self.cmd1 = '/usr/lib/enigma2/python/Plugins/Extensions/Manager/data/emm_sender.sh'  # '/usr/lib/enigma2/python/Plugins/Extensions/Manager/data/emm_sender.sh'
                        from os import access, X_OK
                        if not access(self.cmd1, X_OK):
                            os.chmod(self.cmd1, 493)
                        # os.system(self.cmd1)
                        import subprocess
                        # subprocess.check_output(['bash', self.cmd1])
                        try:
                            subprocess.check_output(['bash', self.cmd1])
                            self.session.open(MessageBox, _('Card Updated!'), MessageBox.TYPE_INFO, timeout=5)
                        except subprocess.CalledProcessError as e:
                            print(e.output)
                            self.session.open(MessageBox, _('Card Not Updated!'), MessageBox.TYPE_INFO, timeout=5)

                        os.system('sleep 5')
                        if not os.path.exists('/tmp/emm.txt'):
                            # import wget
                            outp = base64.b64decode(sss)
                            # url = str(outp)
                            cmmnd = "wget --no-check-certificate -U 'Enigma2 - tvmanager Plugin' -c 'https://pastebin.com/raw/U4eM6DjV' -O '/tmp/emm.txt'"
                            # wget.download(url, '/tmp/emm.txt')
                            os.system(cmmnd)
                        if os.path.exists('/tmp/emm.txt'):
                            msg.append(_("READ EMM....\n"))
                            with open('/tmp/emm.txt') as f:
                                f = f.read()
                                if f.startswith('82708'):
                                    msg.append(_("CURRENT EMM IS:\n"))
                                    msg.append(f)
                                    msg.append(_("\nCurrent Emm saved to /tmp/emm.txt"))
                                else:
                                    msg.append('No Emm Read!')
                            msg = (" %s " % _("\n")).join(msg)
                            self.session.open(MessageBox, _("Please wait, %s.") % msg, MessageBox.TYPE_INFO, timeout=10)
                        else:
                            self.session.open(MessageBox, _("File no exist /tmp/emm.txt"), MessageBox.TYPE_INFO, timeout=10)
                else:
                    self.session.openWithCallback(self.callMyMsg, MessageBox, _('The Cam is not active, send the command anyway?'), MessageBox.TYPE_YESNO)
            except Exception as e:
                print('error on emm', str(e))

    def callMyMsg(self, answer=None):
        if answer:
            msg = []
            msg.append(_("\n....\n.....\n"))
            self.cmd1 = '/usr/lib/enigma2/python/Plugins/Extensions/Manager/data/emm_sender.sh'
            from os import access, X_OK
            if not access(self.cmd1, X_OK):
                os.chmod(self.cmd1, 493)
            import subprocess
            try:
                subprocess.check_output(['bash', self.cmd1])
                self.session.open(MessageBox, _('Card Updated!'), MessageBox.TYPE_INFO, timeout=5)
            except subprocess.CalledProcessError as e:
                print(e.output)
                self.session.open(MessageBox, _('Card Not Updated!'), MessageBox.TYPE_INFO, timeout=5)
            os.system('sleep 5')
            if not os.path.exists('/tmp/emm.txt'):
                outp = base64.b64decode(sss)
                url = str(outp)
                # cmd = 'wget -q --no-use-server-timestamps --no-clobber --timeout=5' + url + ' -O /tmp/emm.txt'
                try:
                    # subprocess.check_output(['bash', cmd])
                    subprocess.call(["wget", "-q", "--no-use-server-timestamps", "--no-clobber", "--timeout=5", url, "-O", '/tmp/emm.txt'])
                except subprocess.CalledProcessError as e:
                    print(e.output)
            if os.path.exists('/tmp/emm.txt'):
                msg.append(_("READ EMM....\n"))
                with open('/tmp/emm.txt') as f:
                    f = f.read()
                    if f.startswith('82708'):
                        msg.append(_("CURRENT EMM IS:\n"))
                        msg.append(f)
                        msg.append(_("\nCurrent Emm saved to /tmp/emm.txt"))
                    else:
                        msg.append('No Emm')
                msg = (" %s " % _("\n")).join(msg)
                self.session.open(MessageBox, _("Please wait, %s.") % msg, MessageBox.TYPE_INFO, timeout=10)
            else:
                self.session.open(MessageBox, _("No Action!\nFile no exist /tmp/emm.txt"), MessageBox.TYPE_INFO, timeout=5)
        else:
            self.session.open(MessageBox, _("Command Cancelled"), MessageBox.TYPE_INFO, timeout=5)

    def closex(self):
        self.close()

    def resetcfg(self):
        if config.plugins.Manager.active.value is True:
            import shutil
            shutil.copy2(data_path + rstcfg, putlbl)
            os.system('chmod -R 755 %s' % putlbl)
            self.session.open(MessageBox, _('Reset') + ' ' + putlbl, type=MessageBox.TYPE_INFO, timeout=8)

    def showhide(self):
        if config.plugins.Manager.active.value is True:
            self['key_green'].setText(buttn)
            self['key_green'].show()
            self['key_yellow'].setText(_('Get Link'))
            self['key_yellow'].show()
            self['key_blue'].setText(_('Reset'))
            self['key_blue'].show()
        else:
            self['key_green'].setText('Force Emm Send')
            self['key_green'].show()
            self['key_yellow'].setText('Check Emm Send')
            self['key_blue'].setText('')
            self['key_blue'].hide()
        return

    def green(self):
        if config.plugins.Manager.active.value is True:
            if putlbl == '/etc/CCcam.cfg':
                self.CCcam()
            elif putlbl == '/etc/tuxbox/config/oscam.server':
                self.Oscam()
            elif putlbl == '/etc/tuxbox/config/oscam-emu/oscam.server':
                self.Oscam()
            elif putlbl == '/etc/tuxbox/config/Oscamicam/oscam.server':
                self.Oscam()
            elif putlbl == '/etc/tuxbox/config/ncam.server':
                self.Ncam()
            else:
                return
        else:
            if runningcam == 'oscam':                                     
                msg = []
                msg.append(_("\n....\n.....\n"))
                self.cmd1 = data_path + 'emm_sender.sh'
                from os import access, X_OK
                if not access(self.cmd1, X_OK):
                    os.chmod(self.cmd1, 493)
                import subprocess
                try:
                    subprocess.check_output(['bash', self.cmd1])
                except subprocess.CalledProcessError as e:
                    print(e.output)
                os.system('sleep 3')
                if os.path.exists('/tmp/emm.txt'):
                    msg.append(_("READ EMM....\n"))
                    with open('/tmp/emm.txt') as f:
                        f = f.read()
                        if f.startswith('82708'):
                            msg.append(_("CURRENT EMM IS:\n"))
                            msg.append(f)
                            msg.append(_("\nCurrent Emm saved to /tmp/emm.txt"))
                        else:
                            msg.append('No Emm')
                    msg = (" %s " % _("\n")).join(msg)
                    self.session.open(MessageBox, _("Please wait, %s.") % msg, MessageBox.TYPE_INFO, timeout=10)
                else:
                    self.session.open(MessageBox, _("No Action!\nFile no exist /tmp/emm.txt"), MessageBox.TYPE_INFO, timeout=5)
            else:
                self.session.open(MessageBox, _("No Action!\nOscam not active"), MessageBox.TYPE_INFO, timeout=5)

    def createSetup(self):
        self.editListEntry = None
        self.list = []
        self.list.append(getConfigListEntry(_('Activate Insert line in Config File:'), config.plugins.Manager.active, _('If Active: Download/Reset Server Config')))
        if config.plugins.Manager.active.value:
            self.list.append(getConfigListEntry(_('Server Config'), config.plugins.Manager.cfgfile, putlbl))
            self.list.append(getConfigListEntry(_('Server Link'), config.plugins.Manager.Server, _('Select Get Link')))
            self.list.append(getConfigListEntry(_('Server URL'), config.plugins.Manager.hostaddress, _('Server Url i.e. 012.345.678.900')))
            self.list.append(getConfigListEntry(_('Server Port'), config.plugins.Manager.port, _('Port')))
            self.list.append(getConfigListEntry(_('Server Username'), config.plugins.Manager.user, _('Username')))
            self.list.append(getConfigListEntry(_('Server Password'), config.plugins.Manager.passw, _('Password')))

        self['config'].list = self.list
        self['config'].l.setList(self.list)
        self.showhide()

    def KeyText(self):
        sel = self['config'].getCurrent()
        if sel:
            self.session.openWithCallback(self.VirtualKeyBoardCallback, VirtualKeyBoard, title=self['config'].getCurrent()[0], text=self['config'].getCurrent()[1].value)

    def keyLeft(self):
        ConfigListScreen.keyLeft(self)
        print('current selection:', self['config'].l.getCurrentSelection())
        putlblcfg()
        self.createSetup()
        self.getcl()

    def keyRight(self):
        ConfigListScreen.keyRight(self)
        print('current selection:', self['config'].l.getCurrentSelection())
        putlblcfg()
        self.createSetup()
        self.getcl()

    # def keyDown(self):
        # self['config'].instance.moveSelection(self['config'].instance.moveDown)
        # self.createSetup()

    # def keyUp(self):
        # self['config'].instance.moveSelection(self['config'].instance.moveUp)
        # self.createSetup()
    def VirtualKeyBoardCallback(self, callback=None):
        if callback is not None and len(callback):
            self['config'].getCurrent()[1].value = callback
            self['config'].invalidate(self['config'].getCurrent())
        return

    def createSummary(self):
        from Screens.Setup import SetupSummary
        return SetupSummary

    def selectionChanged(self):
        # self["info"].setText(self["config"].getCurrent()[2])
        self.showhide()

    def changedEntry(self):
        for x in self.onChangedEntry:
            x()
        self.selectionChanged()

    def getCurrentEntry(self):
        return self['config'].getCurrent()[0]

    def getCurrentValue(self):
        return str(self['config'].getCurrent()[1].getText())

    def CCcam(self):
        global host, port, user, passw
        if config.plugins.Manager.cfgfile.value != '/etc/CCcam.cfg':
            self.session.open(MessageBox, _('Select CCcam'), type=MessageBox.TYPE_INFO, timeout=5)
            return
        cfgfile = config.plugins.Manager.cfgfile.value
        dest = cfgfile
        host = 'C: ' + str(config.plugins.Manager.hostaddress.value)
        port = str(config.plugins.Manager.port.value)
        user = str(config.plugins.Manager.user.value)
        pasw = str(config.plugins.Manager.passw.value)
        if fileExists('/etc/CCcam.cfg'):
            dest = '/etc/CCcam.cfg'
        else:
            self.session.open(MessageBox, _('Please Reset - No File CFG'), type=MessageBox.TYPE_INFO, timeout=5)
            return
        os.system('chmod -R 755 %s' % dest)
        cfgdok = open(dest, 'a')
        # cfgdok = open(dest, 'a', encoding='utf-8')
        cfgdok.write('\n\n' + host + ' ' + port + ' ' + user + ' ' + pasw)
        cfgdok.close()
        self.session.open(MessageBox, _('Server Copy in ') + dest, type=MessageBox.TYPE_INFO, timeout=8)

    def Oscam(self):
        global host, port, user, passw
        cfgfile = config.plugins.Manager.cfgfile.value
        dest = cfgfile
        host = str(config.plugins.Manager.hostaddress.value)
        port = str(config.plugins.Manager.port.value)
        user = str(config.plugins.Manager.user.value)
        pasw = str(config.plugins.Manager.passw.value)
        if not fileExists(dest):
            self.session.open(MessageBox, _('Please Reset - No File CFG'), type=MessageBox.TYPE_INFO, timeout=5)
            return
        os.system('chmod -R 755 %s' % dest)
        cfgdok = open(dest, 'a')
        # cfgdok = open(dest, 'a', encoding='utf-8')
        cfgdok.write('\n[reader]\nlabel = Server_' + host + '\nenable= 1\nprotocol = cccam\ndevice = ' + host + ',' + port + '\nuser = ' + user + '\npassword = ' + pasw + '\ninactivitytimeout = 30\ngroup = 3\ncccversion = 2.2.1\ncccmaxhops = 0\nccckeepalive = 1\naudisabled = 1\n\n')
        cfgdok.close()
        self.session.open(MessageBox, _('Server Copy in ') + dest, type=MessageBox.TYPE_INFO, timeout=8)

    def Ncam(self):
        global host, port, user, passw
        if config.plugins.Manager.cfgfile.value != '/etc/tuxbox/config/ncam.server':
            self.session.open(MessageBox, _('Select Ncam'), type=MessageBox.TYPE_INFO, timeout=5)
            return
        if not os.path.exists('/etc/tuxbox/config'):
            os.system('mkdir /etc/tuxbox/config')
        cfgfile = config.plugins.Manager.cfgfile.value
        dest = cfgfile
        host = str(config.plugins.Manager.hostaddress.value)
        port = str(config.plugins.Manager.port.value)
        user = str(config.plugins.Manager.user.value)
        pasw = str(config.plugins.Manager.passw.value)
        if fileExists('/etc/tuxbox/config/ncam.server'):
            dest = '/etc/tuxbox/config/ncam.server'
        else:
            self.session.open(MessageBox, _('Please Reset - No File CFG'), type=MessageBox.TYPE_INFO, timeout=5)
            return
        os.system('chmod -R 755 %s' % dest)
        cfgdok = open(dest, 'a')
        # cfgdok = open(dest, 'a', encoding='utf-8')
        cfgdok.write('\n[reader]\nlabel = Server_' + host + '\nenable= 1\nprotocol = cccam\ndevice = ' + host + ',' + port + '\nuser = ' + user + '\npassword = ' + pasw + '\ngroup = 3\ncccversion = 2.0.11\ndisablecrccws_only_for= 0500:032830\ncccmaxhops= 1\nccckeepalive= 1\naudisabled = 1\n\n')
        cfgdok.close()
        self.session.open(MessageBox, _('Server Copy in ') + dest, type=MessageBox.TYPE_INFO, timeout=8)

    def getcl(self):
        try:
            data1 = str(config.plugins.Manager.Server.value)
            data = b64decoder(data1)
            try:
                data = getUrl(data)
                if PY3:
                    import six
                    data = six.ensure_str(data)
                self.timer = eTimer()
                if os.path.exists('/var/lib/dpkg/info'):
                    self.timer_conn = self.timer.timeout.connect(self.load_getcl(data))
                else:
                    self.timer.callback.append(self.load_getcl(data))
                self.timer.start(600, 1)
                # self.load_getcl(data)
            except Exception as e:
                print('getcl error: ', str(e))
        except Exception as e:
            print('error on host', str(e))

    def load_getcl(self, data):
        global host, port, user, passw
        try:

            # data = checkStr(data)
            url1 = re.findall('<h1>C: (.+?) (.+?) (.+?) (.+?)\n', data)
            if 'bosscccam' in data.lower():
                url1 = re.findall('ong>c: (.+?) (.+?) (.+?) (.+?)</', data)

            elif 'testcline' in data.lower():
                url1 = re.findall('C: (.+?) (.+?) (.+?) (.+?)</d', data)

            elif 'free.cccam.net' in data.lower():
                url1 = re.findall('<b>C: (.*?) (.*?) (.*?) (.*?)</b>', data)

            elif 'free.cccam-premium' in data.lower():
                url1 = re.findall('C: (.+?) (.+?) (.+?) (*?).*?</h3>', data)

            elif 'cccamsate' in data.lower():
                url1 = re.findall('<span><b>C: (.+?) (.+?) (.+?) (.+?)</b>', data)

            elif 'cccameagle' in data.lower():
                url1 = re.findall('>C: (.+?) (.+?) (.+?) (.+?)</h2>', data)

            elif 'cccamprime' in data.lower():
                url1 = re.findall('Cline : C: (.+?) (.+?) (.+?) (.+?).*?Host', data)
                url1 = url1.replace('<br><br>', '')

            elif 'cccamprima.com' in data.lower():
                url1 = re.findall('<h1>C: (.+?) (.+?) (.+?) (.+?)\n', data)

            elif 'cccampri.me' in data.lower():
                url1 = re.findall('Cline : C: (.+?) (.+?) (.+?) (.+?)<br>', data)

            elif 'cccamfree.co' in data.lower():
                url1 = re.findall('<h1>C: (.+?) (.+?) (.+?) (.+?)\n', data)

            elif 'iptvcccam' in data.lower():
                url1 = re.findall('C: (.+?) (.+?) (.+?) (*?).*?</h1>', data)

            # elif 'premium' in data.lower():
                # url1 = re.findall('C: (.+?) (.+?) (.+?) (.+?)\n', data)

            elif 'cccamia' in data:
                url1 = re.findall('C: (.+?) (.+?) (.+?) (.+?)\n', data)

            elif 'cccameurop' in data.lower():
                url1 = re.findall('C: (.+?) (.+?)</', data)

            elif 'infosat' in data.lower():
                url1 = re.findall('host: (.+?)<br> port: (.+?) <br>.*?user:(.+?)<br>.*?pass: (.+?)\n', data)

            elif 'cccamx' in data.lower():
                url1 = re.findall('C: (.+?) (.+?) (.+?) (.+?)\n', data)

            elif 'cccamiptv' in data.lower():
                url1 = re.findall('C: (.+?) (.+?) (.+?) (.+?)\n.*?</h3>', data)

            elif 'FREEN12' in data.lower():
                url1 = re.findall('<h1>\nC: (.+?) (.+?) (.+?) (.+?)\n', data)

            elif 'history' in data.lower():
                url1 = re.findall('of the line">C: (.+?) (.+?) (.+?) (.+?)</a>.*?title=', data)

            elif 'store' in data.lower():
                url1 = re.findall('<center><strong>C: (.+?) (.+?) (.+?) (.+?) <br>', data)

            elif 'cccamhub' in data.lower():
                url1 = re.findall('id="cline">.*?C: (.+?) (.+?) (.+?) (.+?).*?</div>', data)

            elif 'rogcam' in data.lower():
                url1 = re.findall('bg-primary"> C: (.+?) (.+?) (.+?) (.+?) </span>', data)

            elif 'cccambird' in data.lower():
                url1 = re.findall('>C: (.+?) (.+?) (.+?) (.+?)</th>', data)

            elif 'bosscccam' in data.lower():
                url1 = re.findall('<strong>c: (.+?) (.+?) (.+?) (.+?)</strong', data)

            elif '15days' in data.lower():
                url1 = re.findall('">C: (.*?) (.*?) (.*?) (.+?)</th></tr>', data)

            elif 'cccamfrei' in data.lower():
                url1 = re.findall('<h1>C: (.+?) (.+?) (.+?) (.+?)\n', data)

            elif 'cccamazon' in data.lower():
                url1 = re.findall('<h1>C: (.+?) (.+?) (.+?) (.+?)\n', data)
            print('===========data=========', url1)

            if url1 != '':
                host = ''
                port = ''
                user = ''
                password = ''
                if 'cccameurop' in data.lower():
                    for u, pw in url1:
                        # url1 = 'cccameurop.com 19000' + url1[0] + url1[1]
                        host = 'cccameurop.com'
                        port = '19000'
                        user = str(u)
                        password = str(pw)
                        print('Host: %s - Port: %s - User: %s - Password: %s' % (host, port, user, password))
                elif 'cccam.net' in data.lower():
                    for h, p, u, pw in url1:
                        print(h, p, u, pw)
                        host = str(h)
                        port = str(p)
                        user = str(u)
                        password = str(pw)
                        password = password.replace('</b>', '').replace('</span>', '')
                        password = password.replace('</div>', '')
                        password = password.replace('</h1>', '')
                        password = password.replace('</div>', '')
                else:
                    for h, p, u, pw in url1:
                        print(h, p, u, pw)
                        host = str(h)
                        port = str(p)
                        user = str(u)
                        password = str(pw)
                        password = password.replace('</h1>', '')
                        password = password.replace('</div>', '')
                # if config.plugins.Manager.active.getValue():
                config.plugins.Manager.hostaddress.setValue(host)
                config.plugins.Manager.port.setValue(port)
                config.plugins.Manager.user.setValue(user)
                config.plugins.Manager.passw.setValue(password)
                self.createSetup()
            else:
                return
        except Exception as e:
            print('error on string cline', str(e))
