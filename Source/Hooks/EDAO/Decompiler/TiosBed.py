from EDAOScenaFile import *

def ShowMenu():
    OP_F4(0x3)
    OP_53(0xFF)
    #FadeToDark(300, 0x0, 0x64)

    Menu(
        0x0,
        0xFFFF,
        0xFFFF,
        0x1,
        (
            "在这里休息\x01",                # 0
            "进入Debug地图\x01",                # 1
            "放弃\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "rest_here"),
        (1, "enter_debug_map"),
        (-1, "menu_return"),
    )

    label("rest_here")

    SoundLoad(13)
    OP_21(0xBB8)
    FadeToDark(1000, 0x0, 0xFF)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0x0)
    OP_57(0x0)
    Jump('menu_return')

    label('enter_debug_map')

    NewScene('b0101', 0, 0, 0)
    OP_07()

    label('menu_return')

    OP_54(0xFF)
    Return()
