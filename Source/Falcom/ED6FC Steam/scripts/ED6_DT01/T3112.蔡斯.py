from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3112   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3112.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_D0",           # 01, 1
        "Function_2_116",          # 02, 2
        "Function_3_518",          # 03, 3
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_B6"),
        (SWITCH_DEFAULT, "loc_CF"),
    )


    label("loc_B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C8")
    OP_A2(0x50A)
    Event(0, 2)
    Jump("loc_CC")

    label("loc_C8")

    Event(0, 3)

    label("loc_CC")

    Jump("loc_CF")

    label("loc_CF")

    Return()

    # Function_0_AA end

    def Function_1_D0(): pass

    label("Function_1_D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E8")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_115")

    label("loc_E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_100")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_115")

    label("loc_100")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_115")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_115")

    Return()

    # Function_1_D0 end

    def Function_2_116(): pass

    label("Function_2_116")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(1400, 0, 4500, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 1000, 0, 3390, 0)
    SetChrPos(0x102, -390, 0, 2980, 0)
    SetChrPos(0x107, 680, 0, 2210, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(800)
    OP_8C(0x101, 270, 400)
    Sleep(200)
    OP_8C(0x101, 0, 400)
    OP_8C(0x101, 90, 400)
    Sleep(500)

    ChrTalk(
        0x101,
        "#501F#5P咦，这个房间是……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F这个是导力梯哦。\x02\x03",
            "从地下到房顶，\x01",
            "这么一跳～就上去了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 135, 400)
    OP_8C(0x101, 225, 400)

    ChrTalk(
        0x101,
        (
            "#505F#5P嗯……？\x02\x03",
            "导力梯不就是\x01",
            "矿山里用的那种升降装置吗？\x02\x03",
            "我哪也没看到导力梯啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F不是的，艾丝蒂尔。\x02\x03",
            "其实这整个房间就是导力梯了，\x01",
            "只不过我们现在看到的这个不同而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#5P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#061F嘿嘿，这可是最新式的哦。\x02\x03",
            "最大载重量５０托里姆……\x02\x03",
            "就算要搬运大型器材，\x01",
            "也是轻轻松松的呢⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F#5P虽、虽然不大明白……\x01",
            "但感觉好像很厉害呢。\x02\x03",
            "#000F对了，怎么做才能让它动起来呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F啊，只要在那边的控制板上\x01",
            "选择要去的楼层就ＯＫ了。\x02\x03",
            "嗯……\x01",
            "是要去城里吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯，\x01",
            "能带我们去一楼吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#061F好的。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x107, 135, 400)

    def lambda_462():

        label("loc_462")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_462")

    QueueWorkItem2(0x101, 1, lambda_462)

    def lambda_473():

        label("loc_473")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_473")

    QueueWorkItem2(0x102, 1, lambda_473)
    OP_8E(0x107, 0x6D6, 0x0, 0x5B4, 0x7D0, 0x0)
    OP_8C(0x107, 90, 400)
    Sleep(500)
    OP_22(0x67, 0x0, 0x64)
    OP_6D(1400, -500, 4500, 500)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x101,
        "#004F#10A#1P哇哇……\x05\x02",
    )

    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_6D(1400, -12000, 4500, 1500)
    OP_0D()
    Sleep(1000)
    OP_A2(0x3FA)
    SetMapFlags(0x10000000)
    NewScene("ED6_DT01/T3111   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_116 end

    def Function_3_518(): pass

    label("Function_3_518")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    SetChrPos(0x0, 1750, 0, 1370, 90)
    SetChrPos(0x1, 1280, 0, 2600, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_55E")
    SetChrPos(0x2, 70, 0, 1470, 180)

    label("loc_55E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_57B")
    SetChrPos(0x3, -50, 0, 2600, 180)

    label("loc_57B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_598")
    SetChrPos(0x4, -1380, 0, 1470, 180)

    label("loc_598")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B5")
    SetChrPos(0x5, -1380, 0, 2600, 180)

    label("loc_5B5")

    OP_6D(1400, 0, 4500, 0)
    OP_6B(3000, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 0)), scpexpr(EXPR_END)), "loc_66D")

    Menu(
        0,
        10,
        10,
        1,
        (
            "　【 顶楼 】\x01",      # 0
            "　【 ５层 】\x01",      # 1
            "　【 ４层 】\x01",      # 2
            "　【 ３层 】\x01",      # 3
            "　【 ２层 】\x01",      # 4
            "　【 １层 】\x01",      # 5
            "★【 Ｂ１ 】\x01",      # 6
            "　【 离开 】\x01",      # 7
        )
    )

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9AC")

    label("loc_66D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 1)), scpexpr(EXPR_END)), "loc_6F8")

    Menu(
        0,
        10,
        10,
        1,
        (
            "　【 顶楼 】\x01",      # 0
            "　【 ５层 】\x01",      # 1
            "　【 ４层 】\x01",      # 2
            "　【 ３层 】\x01",      # 3
            "　【 ２层 】\x01",      # 4
            "★【 １层 】\x01",      # 5
            "　【 Ｂ１ 】\x01",      # 6
            "　【 离开 】\x01",      # 7
        )
    )

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9AC")

    label("loc_6F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_783")

    Menu(
        0,
        10,
        10,
        1,
        (
            "　【 顶楼 】\x01",      # 0
            "　【 ５层 】\x01",      # 1
            "　【 ４层 】\x01",      # 2
            "　【 ３层 】\x01",      # 3
            "★【 ２层 】\x01",      # 4
            "　【 １层 】\x01",      # 5
            "　【 Ｂ１ 】\x01",      # 6
            "　【 离开 】\x01",      # 7
        )
    )

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9AC")

    label("loc_783")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 3)), scpexpr(EXPR_END)), "loc_80E")

    Menu(
        0,
        10,
        10,
        1,
        (
            "　【 顶楼 】\x01",      # 0
            "　【 ５层 】\x01",      # 1
            "　【 ４层 】\x01",      # 2
            "★【 ３层 】\x01",      # 3
            "　【 ２层 】\x01",      # 4
            "　【 １层 】\x01",      # 5
            "　【 Ｂ１ 】\x01",      # 6
            "　【 离开 】\x01",      # 7
        )
    )

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9AC")

    label("loc_80E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 4)), scpexpr(EXPR_END)), "loc_899")

    Menu(
        0,
        10,
        10,
        1,
        (
            "　【 顶楼 】\x01",      # 0
            "　【 ５层 】\x01",      # 1
            "★【 ４层 】\x01",      # 2
            "　【 ３层 】\x01",      # 3
            "　【 ２层 】\x01",      # 4
            "　【 １层 】\x01",      # 5
            "　【 Ｂ１ 】\x01",      # 6
            "　【 离开 】\x01",      # 7
        )
    )

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9AC")

    label("loc_899")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 5)), scpexpr(EXPR_END)), "loc_924")

    Menu(
        0,
        10,
        10,
        1,
        (
            "　【 顶楼 】\x01",      # 0
            "★【 ５层 】\x01",      # 1
            "　【 ４层 】\x01",      # 2
            "　【 ３层 】\x01",      # 3
            "　【 ２层 】\x01",      # 4
            "　【 １层 】\x01",      # 5
            "　【 Ｂ１ 】\x01",      # 6
            "　【 离开 】\x01",      # 7
        )
    )

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9AC")

    label("loc_924")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 6)), scpexpr(EXPR_END)), "loc_9AC")

    Menu(
        0,
        10,
        10,
        1,
        (
            "★【 顶楼 】\x01",      # 0
            "　【 ５层 】\x01",      # 1
            "　【 ４层 】\x01",      # 2
            "　【 ３层 】\x01",      # 3
            "　【 ２层 】\x01",      # 4
            "　【 １层 】\x01",      # 5
            "　【 Ｂ１ 】\x01",      # 6
            "　【 离开 】\x01",      # 7
        )
    )

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9AC")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9DC")
    RunExpression(0x0, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A0A")
    FadeToDark(2000, 0, -1)
    OP_22(0x67, 0x0, 0x64)
    OP_6D(1400, -11900, 4500, 2000)
    Jump("loc_A35")

    label("loc_A0A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A35")
    FadeToDark(2000, 0, -1)
    OP_22(0x67, 0x0, 0x64)
    OP_6D(1400, 11900, 4500, 2000)

    label("loc_A35")

    OP_A3(0x540)
    OP_A3(0x541)
    OP_A3(0x542)
    OP_A3(0x543)
    OP_A3(0x544)
    OP_A3(0x545)
    OP_A3(0x546)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (6, "loc_A6F"),
        (5, "loc_A7E"),
        (4, "loc_A8D"),
        (3, "loc_A9C"),
        (2, "loc_AAB"),
        (1, "loc_ABA"),
        (0, "loc_AC9"),
        (SWITCH_DEFAULT, "loc_AF0"),
    )


    label("loc_A6F")

    OP_A2(0x540)
    NewScene("ED6_DT01/T3111   ._SN", 106, 0, 0)
    IdleLoop()
    Jump("loc_AF0")

    label("loc_A7E")

    OP_A2(0x541)
    NewScene("ED6_DT01/T3111   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_AF0")

    label("loc_A8D")

    OP_A2(0x542)
    NewScene("ED6_DT01/T3114   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_AF0")

    label("loc_A9C")

    OP_A2(0x543)
    NewScene("ED6_DT01/T3114   ._SN", 106, 0, 0)
    IdleLoop()
    Jump("loc_AF0")

    label("loc_AAB")

    OP_A2(0x544)
    NewScene("ED6_DT01/T3114   ._SN", 112, 0, 0)
    IdleLoop()
    Jump("loc_AF0")

    label("loc_ABA")

    OP_A2(0x545)
    NewScene("ED6_DT01/T3119   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_AF0")

    label("loc_AC9")

    OP_A2(0x546)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AE4")
    NewScene("ED6_DT01/T3104   ._SN", 104, 0, 0)
    IdleLoop()
    Jump("loc_AED")

    label("loc_AE4")

    NewScene("ED6_DT01/T3101   ._SN", 104, 0, 0)
    IdleLoop()

    label("loc_AED")

    Jump("loc_AF0")

    label("loc_AF0")

    Return()

    # Function_3_518 end

    SaveToFile()

Try(main)
