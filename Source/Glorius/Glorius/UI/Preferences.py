from ml import *
import json

DefaultPreferences = '''\
{
    "Shortcuts": {
        "Menu": {
            "File": {
                "Open":     "Ctrl+O",
                "Attach":   "Ctrl+F1",
                "Exit":     "Alt+X"
            }
        }
    }
}
'''

def MergeDict(dict1, dict2):
    for key in sorted(dict2.keys()):
        value1 = dict1.get(key)
        value2 = dict2[key]

        if key not in dict1:
            dict1[key] = value2
            continue

        if type(value1) != type(value2):
            dict1[key] = value2
            continue

        if isinstance(value2, dict):
            MergeDict(value1, value2)
            continue

        if value1 != value2:
            dict1[key] = value2
            continue

def CreateDefaultPreferences():
    return json.loads(DefaultPreferences)

def LoadPreferences(Preferences):
    default = CreateDefaultPreferences()
    try:
        overwrite = json.loads(open(Preferences, 'rb').read().decode('UTF8'))
    except FileNotFoundError:
        overwrite = dict()

    MergeDict(default, overwrite)
    return OrderedDictEx(default)

def SavePreferences(Preferences):
    pass
