from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS, SCOPE_LANGUAGE
import gettext
import os
from os import environ as os_environ
plugin_path = '/usr/lib/enigma2/python/Plugins/Extensions/Levi45MulticamManager/'
PluginLanguageDomain = 'Levi45MulticamManager'
PluginLanguagePath = plugin_path + 'locale'
DreamOS = False
def DreamOS():
    DreamOS = False
    if os.path.exists('/var/lib/dpkg/status'):
        DreamOS = True
        return DreamOS
DreamOS()
def localeInit():
    if DreamOS:
        lang = language.getLanguage()[:2]
        os_environ['LANGUAGE'] = lang
    gettext.bindtextdomain(PluginLanguageDomain, resolveFilename(SCOPE_PLUGINS, PluginLanguagePath))


if DreamOS():
    _ = lambda txt: (gettext.dgettext(PluginLanguageDomain, txt) if txt else '')
    localeInit()
    language.addCallback(localeInit)
else:

    def _(txt):
        if gettext.dgettext(PluginLanguageDomain, txt):
            return gettext.dgettext(PluginLanguageDomain, txt)
        else:
            print('[' + PluginLanguageDomain + '] fallback to default translation for ' + txt)
            return gettext.gettext(txt)
    language.addCallback(localeInit())
