from Libs.Misc.SysLib import *
import json

def MergeDict(dict1, dict2):
    for key in dict2.keys():
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
    # return json.loads(DefaultPreferences)
    return {}

def LoadPreferences(Preferences, defaultPreferences = None):
    default = defaultPreferences or {}

    default = OrderedDictEx(default)

    if isinstance(Preferences, dict):
        overwrite = Preferences

    else:
        try:
            overwrite = json.JSONDecoder(object_pairs_hook = OrderedDictEx).decode(open(Preferences, 'rb').read().decode('UTF8'))
        except (FileNotFoundError, PermissionError):
            overwrite = OrderedDictEx()

    MergeDict(default, overwrite)
    return default

def SavePreferences(PreferencesPath, Preferences):
    pref = json.dumps(Preferences, indent = 4, sort_keys = True)
    open(PreferencesPath, 'wb').write(pref.encode('UTF8'))
