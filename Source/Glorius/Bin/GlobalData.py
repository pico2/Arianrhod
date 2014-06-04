from ml import *
from . import I18n
from . import Preferences

GlobalData = None

class __GlobalData(object):
    def __init__(self, argv):
        program = os.path.abspath(os.path.dirname(argv[0]))
        path = os.path.abspath(os.path.join(program, 'Lang\\'))
        CurrentUICulture = 'en-US'

        xml = os.path.join(path, CurrentUICulture + '.xml')
        if not os.path.exists(xml):
            xml = os.path.join(path, 'DefaultLanguage.xml')

        self.Lang = I18n.LoadLanguageFile(xml)
        self.Preferences = Preferences.LoadPreferences(os.path.abspath(os.path.join(program, self.Lang.Preferences)))

def Initialize(argv):
    global GlobalData
    print('init')
    GlobalData = __GlobalData(argv)
