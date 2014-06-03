from .BaseCommon import *
from . import I18n

GlobalData = None

class __GlobalData(object):
    def __init__(self, argv):
        path = os.path.abspath(os.path.join(os.path.dirname(argv[0]), 'Lang\\'))
        CurrentUICulture = 'en-US'

        xml = os.path.join(path, CurrentUICulture + '.xml')
        if not os.path.exists(xml):
            xml = os.path.join(path, 'DefaultLanguage.xml')

        self.Lang = I18n.LoadLanguageFile(xml)

def Initialize(argv):
    global GlobalData
    GlobalData = __GlobalData(argv)
