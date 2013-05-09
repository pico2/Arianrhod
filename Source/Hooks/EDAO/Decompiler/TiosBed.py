from EDAOScenaFile import *
from ScenarioHelper import *

StaticCharList = \
(
    '罗伊德',
    '艾莉',
    '缇欧',
    '兰迪',
    '瓦吉',
    '银',
    '诺艾尔上士',
)

def SelectTargetCharMenu():
    pass

def ShowChangeMemberMenu():

    CharList = StaticCharList.copy()

    for i in range(len(CharList)):
        CharList[i] = CharList[i] + '\x01'
    CharList.append('放弃\x01')


    menu_end_label = GenerateUniqueLable()
    show_menu_label = GenerateUniqueLable()

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)))

    label(show_menu_label)

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), menu_end_label)

    MenuTitle(0xFFFF, 0x19, 0x0, "要替换谁")
    Menu(1, 0xFFFF, 0xFFFF, 1, CharList)

    MenuEnd(0x0)
    OP_60(1)

    CaseList = []
    for i in range(len(CharList) - 1):
        CaseList.append( (i, GenerateUniqueLable()) )

    CaseList.append((SWITCH_DEFAULT, GenerateUniqueLable()))

    expr = (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END))

    args = CaseList.copy()
    args.insert(0, expr)
    Switch(*args)

    for i in range(len(CaseList)):
        caseid, caselabel = CaseList[i]
        label(caselabel)

        if caseid == SWITCH_DEFAULT:
            RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_END)))
        else:
            RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0), scpexpr(EXPR_END)))

        Jump(show_menu_label)

    label(menu_end_label)

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

def ShowMenu():
    OP_F4(0x3)
    OP_53(0xFF)

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)))

    label('show_menu')

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "menu_return")

    MenuTitle(0xFFFF, 0x19, 0x0, "缇欧的床")

    Menu(
        0,
        0xFFFF,
        0xFFFF,
        0x1,
        (
            "满血满魔满CP\x01",              # 0
            "换人\x01",                      # 1
            "进入Debug地图\x01",             # 2
            "放弃\x01",                      # 3
        )
    )

    MenuCmd(0x4, 0x0, 0x0)
    MenuEnd(0x0)
    MenuCmd(0x4, 0x0, 0x0)

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "rest_here"),
        (1, "change_member"),
        (2, "enter_debug_map"),
        (-1, "close_menu"),
    )

    label("rest_here")

    OP_32(0xFF, 0xFF, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump('show_menu')


    label('change_member')


    ShowChangeMemberMenu()
    Jump('show_menu')


    label('enter_debug_map')
    NewScene('a0000', 0, 0, 0)
    OP_07()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump('show_menu')


    label('close_menu')
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump('show_menu')

    label('menu_return')

    OP_60(0x0)
    OP_57(0x0)
    OP_DD()
    #ClearXXXFlags(0x80)
    OP_54(0xFF)
    Return()
