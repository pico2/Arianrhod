from ml import *
import json

def LoadPreferences(Preferences):
    return dict2(json.loads(open(Preferences, 'rb').read().decode('UTF8')))

def SavePreferences(Preferences):
    pass
