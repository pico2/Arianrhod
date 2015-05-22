from Libs.Misc.SysLib import *

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

    for attr, value in node.attrib.items():
        # lang[node.tag]['@%s' % attr] = value
        lang['%s:%s' % (node.tag, attr)] = value

    return lang
