from ml import *

def LoadLanguageFile(file):
    root = ET.parse(file).getroot()
    lang = OrderedDictEx()

    for child in root:
        LoadNode(lang, child)

    return lang

def LoadNode(lang, node):
    if len(node) != 0:
        sub = OrderedDictEx()
        lang[node.tag] = sub
        for child in node:
            LoadNode(sub, child)
    else:
        lang[node.tag] = node.text
        lang['%s:Tip' % node.tag] = node.attrib.get('Tip', None)

    return lang

def main():
    lang = LoadLanguageFile(r"..\Lang\DefaultLanguage.xml")
    print(lang)
    PauseConsole()

if __name__ == '__main__':
    TryInvoke(main)
