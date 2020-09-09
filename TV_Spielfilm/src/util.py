from re import sub, findall, S as RES
from Components.config import config
from Components.ConditionalWidget import BlinkingWidget
from Components.ScrollLabel import ScrollLabel
from Components.Label import Label
from Components.MenuList import MenuList
from enigma import eListboxPythonMultiContent, gFont

MEDIAROOT = "/usr/lib/enigma2/python/Plugins/Extensions/TVSpielfilm/"
PICPATH = MEDIAROOT + "pic/"
ICONPATH = PICPATH + "icons/"
TVSPNG = PICPATH + "tvspielfilm.png"
TVSHDPNG = PICPATH + "tvspielfilmHD.png"


class serviceDB():

    def __init__(self, servicefile):
        self.servicefile = servicefile
        self.d = dict()
        try:
            for x in open(self.servicefile):
                key, val = x.split()
                self.d[key] = val

        except:
            pass

    def lookup(self, key):
        if key in self.d:
            return self.d[key]
        return 'nope'

    def close(self):
        pass

class channelDB():

    def __init__(self, servicefile):
        self.servicefile = servicefile
        self.d = dict()
        try:
            for x in open(self.servicefile):
                val, key = x.split()
                self.d[key] = val

        except:
            pass

    def lookup(self, key):
        if key in self.d:
            return self.d[key]
        return 'nope'

    def close(self):
        pass


class BlinkingLabel(Label, BlinkingWidget):

    def __init__(self, text = ''):
        Label.__init__(self, text=text)
        BlinkingWidget.__init__(self)

class CScrollLabel(ScrollLabel):

    def __init__(self, text = ''):
        ScrollLabel.__init__(self, text=text)

        if config.plugins.tvspielfilm.font_size.value == 'verylarge':
            _fontsize = 28
        elif config.plugins.tvspielfilm.font_size.value == 'large':
            _fontsize = 20
        else:
            _fontsize = 18
            self.setFont(-1, gFont('Regular', _fontsize))

class CLabel2(Label):

    def __init__(self, text = ''):
        Label.__init__(self, text=text)

        if config.plugins.tvspielfilm.font_size.value == 'verylarge':
            _fontsize = 26
        elif config.plugins.tvspielfilm.font_size.value == 'large':
            _fontsize = 18
        else:
            _fontsize = 16
            self.setFont(-1, gFont('Regular', _fontsize))

class CLabel(Label):

    def __init__(self, text = ''):
        Label.__init__(self, text=text)

        if config.plugins.tvspielfilm.font_size.value == 'verylarge':
            _fontsize = 28
        elif config.plugins.tvspielfilm.font_size.value == 'large':
            _fontsize = 20
        else:
            _fontsize = 18
            self.setFont(-1, gFont('Regular', _fontsize))

class ItemList(MenuList):

    def __init__(self, items, enableWrapAround = True):
        MenuList.__init__(self, items, enableWrapAround, eListboxPythonMultiContent)
#        if config.plugins.tvspielfilm.font.value == 'yes':
#            self.l.setFont(-2, gFont('Sans', 24))
#            if config.plugins.tvspielfilm.font_size.value == 'verylarge':
#                self.l.setFont(-1, gFont('Sans', 26))
#                self.l.setFont(0, gFont('Sans', 24))
#                self.l.setFont(1, gFont('Sans', 22))
#                self.l.setFont(2, gFont('Sans', 20))
#            elif config.plugins.tvspielfilm.font_size.value == 'large':
#                self.l.setFont(-1, gFont('Sans', 24))
#                self.l.setFont(0, gFont('Sans', 22))
#                self.l.setFont(1, gFont('Sans', 20))
#                self.l.setFont(2, gFont('Sans', 18))
#            else:
#                self.l.setFont(-1, gFont('Sans', 22))
#                self.l.setFont(0, gFont('Sans', 20))
#                self.l.setFont(1, gFont('Sans', 18))
#                self.l.setFont(2, gFont('Sans', 16))
#        else:
        self.l.setFont(-2, gFont('Regular', 24))
        if config.plugins.tvspielfilm.font_size.value == 'verylarge':
            self.l.setFont(-1, gFont('Regular', 28))
            self.l.setFont(0, gFont('Regular', 24))
            self.l.setFont(1, gFont('Regular', 22))
            self.l.setFont(2, gFont('Regular', 20))
        elif config.plugins.tvspielfilm.font_size.value == 'large':
            self.l.setFont(-1, gFont('Regular', 24))
            self.l.setFont(0, gFont('Regular', 22))
            self.l.setFont(1, gFont('Regular', 20))
            self.l.setFont(2, gFont('Regular', 18))
        else:
            self.l.setFont(-1, gFont('Regular', 22))
            self.l.setFont(0, gFont('Regular', 20))
            self.l.setFont(1, gFont('Regular', 18))
            self.l.setFont(2, gFont('Regular', 16))


def applySkinVars(skin, dict):
    for key in dict.keys():
        try:
            skin = skin.replace('{' + key + '}', dict[key])
        except Exception as e:
            print(e, '@key=', key)
    return skin

def makeWeekDay(weekday):
    if weekday == 0:
        _weekday = 'Montag'
    elif weekday == 1:
        _weekday = 'Dienstag'
    elif weekday == 2:
        _weekday = 'Mittwoch'
    elif weekday == 3:
        _weekday = 'Donnerstag'
    elif weekday == 4:
        _weekday = 'Freitag'
    elif weekday == 5:
        _weekday = 'Samstag'
    elif weekday == 6:
        _weekday = 'Sonntag'
    return _weekday
