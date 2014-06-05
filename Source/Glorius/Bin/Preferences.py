from ml import *
import json

DefaultPreferences = '''\
{
    "Shortcuts": {
        "Menu": {
            "File": {
                "Open": "Ctrl+O",
                "Attach": "Ctrl+F1",
                "Exit": "Alt+X"
            }
        }
    }
}
'''

def CreateDefaultPreferences():
    return OrderedDictEx(json.loads(DefaultPreferences))

def MergeDict(dict1, dict2):
    pass

def LoadPreferences(Preferences):
    default = CreateDefaultPreferences()
    loaded = OrderedDictEx(json.loads(open(Preferences, 'rb').read().decode('UTF8')))

    with qtbp():
        pass

    return OrderedDictEx(list(default.items()) + list(loaded.items()))

def SavePreferences(Preferences):
    pass
