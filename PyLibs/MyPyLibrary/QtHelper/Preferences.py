from ml import *

DefaultPreferences = '''\
{
    "Properties": {
        "noTicker": false,
        "noRescale": false,
        "noAnimations": true,
        "noBlending": false,
        "noScreenSync": false,
        "fullscreen": false,
        "usePixmaps": false,
        "useLoop": false,
        "showBoundingRect": false,
        "showFps": false,
        "noAdapt": false,
        "noWindowMask": true,
        "useButtonBalls": false,
        "useEightBitPalette": false,
        "noTimerUpdate": false,
        "noTickerMorph": false,
        "adapted": false,
        "verbose": false,
        "pause": true
    },

    "Shortcuts": {
        "Menu": {
            "File": {
                "OpenPE":   "F3",
                "Attach":   "Ctrl+F1",
                "Exit":     "Alt+X"
            },
            "Debug": {
                "StopDebugging":    "ALT+F2"
            }
        },
        "Docks": {
            "Cpu":          "ALT+C",
            "Memory":       "ALT+D",
            "Registers":    "ALT+R",
            "Stack":        "ALT+S"
        }
    },

    "Layout": {
        "Cpu": {
            "Splitter": [85, 285, 905]
        },
        "Memory": {
            "Splitter": [85, 660]
        },
        "Stack": {
            "Splitter": [85, 171]
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
    except:
        overwrite = dict()

    MergeDict(default, overwrite)
    return OrderedDictEx(default)

def SavePreferences(PreferencesPath, Preferences):
    pref = json.dumps(Preferences, indent = 4, sort_keys = True)
    open(PreferencesPath, 'wb').write(pref.encode('UTF8'))
