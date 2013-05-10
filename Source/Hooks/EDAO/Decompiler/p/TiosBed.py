from ScenarioHelper import *

class CharInfo:
    def __init__(self, id, name):
        self.Name = name
        self.Id = id

StaticCharList = \
(
    CharInfo(0x00, '罗伊德'),
    CharInfo(0x01, '艾莉'),
    CharInfo(0x02, '缇欧'),
    CharInfo(0x03, '兰迪'),
    CharInfo(0x04, '瓦吉'),
    CharInfo(0x05, '银'),
    CharInfo(0x09, '诺艾尔上士'),
)

StaticGodList = \
(
    CharInfo(0xB0, '阿瑞安赫德'),
    CharInfo(0xB1, '战鬼西格蒙德'),
    CharInfo(0xB2, '玛丽亚贝尔'),
    CharInfo(0xB3, '亚里欧斯长官'),
    CharInfo(0xB4, '风之剑圣亚里欧斯'),
)

StaticCharMap = {}
StaticGodMap = {}

for char in StaticCharList: StaticCharMap[char.Id] = char.Name
for char in StaticGodList: StaticGodMap[char.Id] = char.Name

def ShowGodListMenu(SourceCharId):

    CharList = []
    for char in StaticGodList:
        CharList.append(char.Name + '\x01')
    CharList.append('放弃\x01')

    menu_end_label = GenerateUniqueLable()
    menu_return_label = GenerateUniqueLable()


    MenuTitle(0xFFFF, 0x19, 0x0, "要把 %s 替换成" % StaticCharMap[SourceCharId])
    Menu(1, 0xFFFF, 0xFFFF, 1, CharList)

    MenuCmd(0x4, 0x0, 0x0)
    MenuEnd(0x0)
    MenuCmd(0x4, 0x0, 0x0)

    CaseList = []
    for i in range(len(CharList) - 1):
        CaseList.append( (i, GenerateUniqueLable()) )

    CaseList.append((SWITCH_DEFAULT, GenerateUniqueLable()))

    Switch((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)), *CaseList)

    for i in range(len(CaseList)):
        caseid, caselabel = CaseList[i]
        label(caselabel)

        if caseid == SWITCH_DEFAULT:
            Jump(menu_return_label)
            continue

        SetChrChipPat(SourceCharId, 1, StaticGodList[i].Id)
        Jump(menu_end_label)

    label(menu_end_label)
    LoadChrChipPat()


    label(menu_return_label)

    OP_60(1)

def ShowChangeMemberMenu():

    CharList = []
    for char in StaticCharList:
        CharList.append(char.Name + '\x01')
    CharList.append('放弃\x01')


    menu_end_label = GenerateUniqueLable()
    show_menu_label = GenerateUniqueLable()

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)))

    label(show_menu_label)

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), menu_end_label)

    MenuTitle(0xFFFF, 0x19, 0x0, "要替换谁")
    Menu(1, 0xFFFF, 0xFFFF, 1, CharList)

    MenuCmd(0x4, 0x0, 0x0)
    MenuEnd(0x0)
    MenuCmd(0x4, 0x0, 0x0)

    CaseList = []
    for i in range(len(CharList) - 1):
        CaseList.append( (i, GenerateUniqueLable()) )

    CaseList.append((SWITCH_DEFAULT, GenerateUniqueLable()))

    Switch((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)), *CaseList)

    for i in range(len(CaseList)):
        caseid, caselabel = CaseList[i]
        label(caselabel)

        if caseid == SWITCH_DEFAULT:
            RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_END)))
            Jump(show_menu_label)
            continue

        RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0), scpexpr(EXPR_END)))
        ShowGodListMenu(StaticCharList[i].Id)

        Jump(show_menu_label)

    label(menu_end_label)

    OP_60(1)

def ReleaseAllGod():
    for i in range(len(StaticCharList)):
        SetChrChipPat(StaticCharList[i].Id, 1, StaticCharList[i].Id)

def ShowMenu():
    OP_F4(0x3)
    OP_53(0xFF)

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)))

    label('show_menu')

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "menu_return")

    MenuTitle(0xFFFF, 0x19, 0x0, "星辰之间")

    Menu(
        0,
        0xFFFF,
        0xFFFF,
        0x1,
        (
            "满血满魔满CP\x01",              # 0
            "换人\x01",                      # 1
            "全部还原\x01",                  # 2
            "进入Debug地图\x01",             # 3
            "放弃\x01",                      # 4
        )
    )

    MenuCmd(0x4, 0x0, 0x0)
    MenuEnd(0x0)
    MenuCmd(0x4, 0x0, 0x0)

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "rest_here"),
        (1, "change_member"),
        (2, "restore_all"),
        (3, "enter_debug_map"),
        (-1, "close_menu"),
    )

    label("rest_here")

    OP_32(0xFF, 0xFF, 0)
    Jump('continue_show_menu')


    label('change_member')

    ShowChangeMemberMenu()
    Jump('continue_show_menu')


    label('restore_all')
    ReleaseAllGod()
    Jump('continue_show_menu')


    label('enter_debug_map')
    NewScene('a0000', 0, 0, 0)
    OP_07()
    Jump('close_menu')


    label('close_menu')
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump('show_menu')


    label('continue_show_menu')
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump('show_menu')


    label('menu_return')

    OP_60(0x0)
    OP_57(0x0)
    OP_DD()
    #ClearXXXFlags(0x80)
    OP_54(0xFF)
    Return()
