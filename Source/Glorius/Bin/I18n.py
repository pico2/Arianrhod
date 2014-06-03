from ml import *

def LoadLanguageFile(file):
    root = ET.parse(file).getroot()
    lang = dict2()

    for child in root:
        LoadNode(lang, child)

    return lang

def LoadNode(lang, node):
    if len(node) != 0:
        sub = dict2()
        lang[node.tag] = sub
        for child in node:
            LoadNode(sub, child)
    else:
        lang[node.tag] = node.text

    return lang

def main():
    lang = LoadLanguageFile(r"..\Lang\DefaultLanguage.xml")
    print(lang.Menu.File)
    PauseConsole()

if __name__ == '__main__':
    TryInvoke(main)
