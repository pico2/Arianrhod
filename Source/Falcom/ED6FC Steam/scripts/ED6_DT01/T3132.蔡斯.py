from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3132   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3132.x',
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
        '玛尔奇娜主管',                         # 9
        '艾玛',                                 # 10
        '多杰',                                 # 11
        '亚鲁瓦',                               # 12
        '朵洛希',                               # 13
        '拉德米拉',                             # 14
        '卡雷尔',                               # 15
        '西加罗',                               # 16
        '艾德尔',                               # 17
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


    AddCharChip(
        'ED6_DT07/CH01210 ._CH',             # 00
        'ED6_DT07/CH01350 ._CH',             # 01
        'ED6_DT07/CH01140 ._CH',             # 02
        'ED6_DT07/CH02050 ._CH',             # 03
        'ED6_DT07/CH02070 ._CH',             # 04
        'ED6_DT07/CH01690 ._CH',             # 05
        'ED6_DT07/CH02640 ._CH',             # 06
        'ED6_DT07/CH01040 ._CH',             # 07
        'ED6_DT07/CH01210 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH01210P._CP',             # 00
        'ED6_DT07/CH01350P._CP',             # 01
        'ED6_DT07/CH01140P._CP',             # 02
        'ED6_DT07/CH02050P._CP',             # 03
        'ED6_DT07/CH02070P._CP',             # 04
        'ED6_DT07/CH01690P._CP',             # 05
        'ED6_DT07/CH02640P._CP',             # 06
        'ED6_DT07/CH01040P._CP',             # 07
        'ED6_DT07/CH01210P._CP',             # 08
    )

    DeclNpc(
        X                   = -1700,
        Z                   = 0,
        Y                   = 2400,
        Direction           = 192,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = -44500,
        Z                   = 0,
        Y                   = 7710,
        Direction           = 82,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )


    DeclActor(
        TriggerX            = -1290,
        TriggerZ            = 0,
        TriggerY            = 550,
        TriggerRange        = 400,
        ActorX              = -1700,
        ActorZ              = 1500,
        ActorY              = 2400,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_236",          # 00, 0
        "Function_1_525",          # 01, 1
        "Function_2_547",          # 02, 2
        "Function_3_55D",          # 03, 3
        "Function_4_581",          # 04, 4
        "Function_5_5A5",          # 05, 5
        "Function_6_5C9",          # 06, 6
        "Function_7_5ED",          # 07, 7
        "Function_8_611",          # 08, 8
        "Function_9_635",          # 09, 9
        "Function_10_659",         # 0A, 10
        "Function_11_67D",         # 0B, 11
        "Function_12_6A1",         # 0C, 12
        "Function_13_6C5",         # 0D, 13
        "Function_14_896",         # 0E, 14
        "Function_15_968",         # 0F, 15
        "Function_16_13FF",        # 10, 16
        "Function_17_1712",        # 11, 17
        "Function_18_17D9",        # 12, 18
        "Function_19_19D4",        # 13, 19
        "Function_20_2229",        # 14, 20
        "Function_21_222E",        # 15, 21
        "Function_22_2830",        # 16, 22
    )


    def Function_0_236(): pass

    label("Function_0_236")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_258")
    SetChrPos(0x9, 34920, 0, 91540, 240)
    OP_43(0x9, 0x0, 0x0, 0x6)
    Jump("loc_524")

    label("loc_258")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_28E")
    SetChrPos(0x9, 48750, 0, 137140, 170)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 770, 0, 2490, 280)
    SetChrFlags(0xC, 0x10)
    Jump("loc_524")

    label("loc_28E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2B0")
    SetChrPos(0x9, 53820, 0, 136060, 76)
    OP_43(0x9, 0x0, 0x0, 0x4)
    Jump("loc_524")

    label("loc_2B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_329")
    SetChrPos(0x9, 53820, 0, 136060, 76)
    OP_43(0x9, 0x0, 0x0, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 35060, 0, 51880, 175)
    OP_43(0xB, 0x0, 0x0, 0x8)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 35130, 0, 91450, 214)
    OP_43(0xD, 0x0, 0x0, 0x9)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 32420, 0, 95120, 302)
    OP_43(0xE, 0x0, 0x0, 0xA)
    Jump("loc_524")

    label("loc_329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_368")
    SetChrPos(0x9, 4750, 0, 1370, 265)
    OP_43(0x9, 0x0, 0x0, 0x5)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 68050, 0, 56260, 30)
    OP_43(0xA, 0x0, 0x0, 0x7)
    Jump("loc_524")

    label("loc_368")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_3DA")
    SetChrPos(0x9, 5810, 0, 3490, 194)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 68050, 0, 56260, 30)
    OP_43(0xA, 0x0, 0x0, 0x7)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 35130, 0, 91450, 214)
    OP_43(0xD, 0x0, 0x0, 0x9)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 2990, 0, 1550, 87)
    OP_43(0xE, 0x0, 0x0, 0xB)
    Jump("loc_524")

    label("loc_3DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_42F")
    SetChrPos(0x9, 64750, 0, 95500, 3)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 35130, 0, 91450, 214)
    OP_43(0xD, 0x0, 0x0, 0x9)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 32420, 0, 95120, 302)
    OP_43(0xE, 0x0, 0x0, 0xA)
    Jump("loc_524")

    label("loc_42F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_49A")
    SetChrPos(0x9, 53820, 0, 136060, 76)
    OP_43(0x9, 0x0, 0x0, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 66540, 0, 59500, 354)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 64450, 0, 95110, 275)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 68300, 0, 90910, 151)
    OP_43(0x10, 0x0, 0x0, 0xC)
    Jump("loc_524")

    label("loc_49A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_505")
    SetChrPos(0x9, 53820, 0, 136060, 76)
    OP_43(0x9, 0x0, 0x0, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 66540, 0, 59500, 354)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 64450, 0, 95110, 275)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 68300, 0, 90910, 151)
    OP_43(0x10, 0x0, 0x0, 0xC)
    Jump("loc_524")

    label("loc_505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_524")
    SetChrPos(0x9, 35090, 0, 51720, 32)
    OP_43(0x9, 0x0, 0x0, 0x3)

    label("loc_524")

    Return()

    # Function_0_236 end

    def Function_1_525(): pass

    label("Function_1_525")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_53D")
    OP_B1("t3132_y")
    Jump("loc_546")

    label("loc_53D")

    OP_B1("t3132_n")

    label("loc_546")

    Return()

    # Function_1_525 end

    def Function_2_547(): pass

    label("Function_2_547")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_55C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_547")

    label("loc_55C")

    Return()

    # Function_2_547 end

    def Function_3_55D(): pass

    label("Function_3_55D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_580")
    OP_8D(0xFE, 33590, 49640, 1108473283, 53470, 3000)
    Jump("Function_3_55D")

    label("loc_580")

    Return()

    # Function_3_55D end

    def Function_4_581(): pass

    label("Function_4_581")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5A4")
    OP_8D(0xFE, 44740, 134200, 62330, 137000, 3000)
    Jump("Function_4_581")

    label("loc_5A4")

    Return()

    # Function_4_581 end

    def Function_5_5A5(): pass

    label("Function_5_5A5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5C8")
    OP_8D(0xFE, 1650, -310, 7710, 1910, 3000)
    Jump("Function_5_5A5")

    label("loc_5C8")

    Return()

    # Function_5_5A5 end

    def Function_6_5C9(): pass

    label("Function_6_5C9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5EC")
    OP_8D(0xFE, 4059, 88790, 36250, 93240, 3000)
    Jump("Function_6_5C9")

    label("loc_5EC")

    Return()

    # Function_6_5C9 end

    def Function_7_5ED(): pass

    label("Function_7_5ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_610")
    OP_8D(0xFE, 66680, 54350, 69610, 58920, 2000)
    Jump("Function_7_5ED")

    label("loc_610")

    Return()

    # Function_7_5ED end

    def Function_8_611(): pass

    label("Function_8_611")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_634")
    OP_8D(0xFE, 34200, 49490, 36490, 53440, 2000)
    Jump("Function_8_611")

    label("loc_634")

    Return()

    # Function_8_611 end

    def Function_9_635(): pass

    label("Function_9_635")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_658")
    OP_8D(0xFE, 33860, 89530, 36420, 93590, 1500)
    Jump("Function_9_635")

    label("loc_658")

    Return()

    # Function_9_635 end

    def Function_10_659(): pass

    label("Function_10_659")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_67C")
    OP_8D(0xFE, 31570, 94690, 33720, 95490, 3000)
    Jump("Function_10_659")

    label("loc_67C")

    Return()

    # Function_10_659 end

    def Function_11_67D(): pass

    label("Function_11_67D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6A0")
    OP_8D(0xFE, 1090, -290, 4450, 2920, 3000)
    Jump("Function_11_67D")

    label("loc_6A0")

    Return()

    # Function_11_67D end

    def Function_12_6A1(): pass

    label("Function_12_6A1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6C4")
    OP_8D(0xFE, 67180, 88480, 69500, 93510, 1500)
    Jump("Function_12_6A1")

    label("loc_6C4")

    Return()

    # Function_12_6A1 end

    def Function_13_6C5(): pass

    label("Function_13_6C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_751")

    ChrTalk(
        0xFE,
        (
            "今天我们要去\x01",
            "附近有名的温泉胜地。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在回格兰赛尔之前，\x01",
            "我想留在那里一段时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，这样我老婆\x01",
            "也暂时不会买东西了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_892")

    label("loc_751")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_892")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_7E1")

    ChrTalk(
        0xFE,
        (
            "今天我们要去\x01",
            "附近有名的温泉胜地。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在回格兰赛尔之前，\x01",
            "我想留在那里一段时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，这样我老婆\x01",
            "也暂时不会买东西了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_892")

    label("loc_7E1")

    OP_A2(0x7)

    ChrTalk(
        0xFE,
        "昨天晚上发生什么事了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "当时我很快就睡着了，\x01",
            "完全不知道发生了什么事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……哎呀！\x01",
            "不能再说了，\x01",
            "必须快点准备行李才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天我们要去\x01",
            "附近有名的温泉胜地。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_892")

    TalkEnd(0xFE)
    Return()

    # Function_13_6C5 end

    def Function_14_896(): pass

    label("Function_14_896")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_905")

    ChrTalk(
        0xFE,
        (
            "那个温泉小村\x01",
            "听说相当不错啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好像还有很名贵的特产，\x01",
            "看来我可以好好享受一下购物乐趣了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_964")

    label("loc_905")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_964")

    ChrTalk(
        0xFE,
        (
            "我刚想要睡觉的时候，\x01",
            "灯忽然全都灭掉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可笑的是\x01",
            "我还把丈夫的床错搞成自己的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_964")

    TalkEnd(0xFE)
    Return()

    # Function_14_896 end

    def Function_15_968(): pass

    label("Function_15_968")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_D41")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C80")
    OP_A2(0x583)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        "啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哟，好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F……？\x02\x03",
            "#010F啊，我还以为是谁呢……\x01",
            "真的是好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F嗯？是谁啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F呵呵，就是在洛连特\x01",
            "寻找结晶回路碎片的那个孩子啊。\x02\x03",
            "我们之前不是\x01",
            "接受过他的委托去找那碎片吗。\x02\x03",
            "你要回卡尔瓦德共和国去了？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "嗯，时间差不多了。\x01",
            "不过在那之前要去中央工房。\x01",
            "因为在格兰赛尔卖了些东西……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "老妈说要用那些米拉\x01",
            "买些导力器回去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嘿，老妈也开始知道\x01",
            "什么东西才是有价值的了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F怎么样都好啦。\x01",
            "你还是老样子，那么自大傲慢呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "是吗？我觉得自己 \x01",
            "只不过是说了理所当然的话而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "尽管如此……\x01",
            "那些巨大的飞艇\x01",
            "真的是在这个城市里面建造的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天，我在中央工房里\x01",
            "听到那些技师在商量\x01",
            "关于新型导力引擎的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……了不起啊。\x01",
            "能够建造出可以在天空中翱翔的飞艇。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是了不起啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_D3E")

    label("loc_C80")


    ChrTalk(
        0xFE,
        (
            "那些巨大的飞艇\x01",
            "真的是在这个城市里面建造的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天，我在中央工房里\x01",
            "听到那些技师在商量\x01",
            "关于导力引擎的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……了不起啊。\x01",
            "能够建造出可以在天空中翱翔的飞艇。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是了不起啊。\x02",
    )

    CloseMessageWindow()

    label("loc_D3E")

    Jump("loc_13FB")

    label("loc_D41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_10EF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_109D")
    OP_A2(0x583)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        "啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哟，好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F……？\x02\x03",
            "#010F啊，我还以为是谁呢……\x01",
            "真的是好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F嗯？是谁啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F呵呵，就是在洛连特\x01",
            "寻找结晶回路碎片的那个孩子啊。\x02\x03",
            "我们之前不是\x01",
            "接受过他的委托去找那碎片吗。\x02\x03",
            "你要回卡尔瓦德共和国去了？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "不，在那之前要先去中央工房。\x01",
            "因为在格兰赛尔卖了些东西……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "老妈说要用那些米拉\x01",
            "买些导力器回去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嘿，老妈也开始知道\x01",
            "什么东西才是有价值的了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F怎么样都好啦。\x01",
            "你还是老样子，那么自大傲慢呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "是吗？我觉得自己 \x01",
            "只不过是说了理所当然的话而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "尽管如此……\x01",
            "从刚才开始外面就一直很吵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "出什么事了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们现在就去确认情况。\x01",
            "　\x02\x03",
            "因为可能会有危险，\x01",
            "你千万不可以出去哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "你凭什么不让我出去啊。\x01",
            "我又不是小孩子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F啊，\x01",
            "你还真的挺自大的嘛。\x02\x03",
            "#002F哦，\x01",
            "现在可不是说这种话的场合。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F嗯，我们快点去吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_10EC")

    label("loc_109D")


    ChrTalk(
        0xFE,
        "从刚才开始外面就一直很吵。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果弄清楚是什么事情，\x01",
            "记得回来告诉我哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10EC")

    Jump("loc_13FB")

    label("loc_10EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_13FB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1389")
    OP_A2(0x583)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        "啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哟，好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F……？\x02\x03",
            "#010F啊，我还以为是谁呢……\x01",
            "真的是好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F嗯？是谁啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F呵呵，就是在洛连特\x01",
            "寻找结晶回路碎片的那个孩子啊。\x02\x03",
            "我们之前不是\x01",
            "接受过他的委托去找那碎片吗。\x02\x03",
            "你要回卡尔瓦德共和国去了？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "不，在那之前要先去中央工房。\x01",
            "因为在格兰赛尔卖了些东西……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "老妈说要用那些米拉\x01",
            "买些导力器回去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嘿，老妈也开始知道\x01",
            "什么东西才是有价值的了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F怎么样都好啦。\x01",
            "你还是老样子，那么自大傲慢呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "是吗？我觉得自己 \x01",
            "只不过是说了理所当然的话而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "尽管如此……\x01",
            "这个城市真不得了啊。\x01",
            "到处都装着导力装置。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且飞船也是\x01",
            "在这个城市里建造的啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13FB")

    label("loc_1389")


    ChrTalk(
        0xFE,
        "这个城市，好厉害啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "有可以活动的楼梯，\x01",
            "钟表也是导力驱动的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且飞船也是\x01",
            "在这个城市里建造的啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13FB")

    TalkEnd(0xFE)
    Return()

    # Function_15_968 end

    def Function_16_13FF(): pass

    label("Function_16_13FF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_15DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_14DB")

    ChrTalk(
        0xFE,
        (
            "今天，我去工房四处转了转，\x01",
            "订购了一些导力相机。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "明天把货品领回来，商谈就搞定了。\x01",
            "这样就可以回国了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要是我家的卡雷尔\x01",
            "也能正正经经地\x01",
            "给我帮忙到最后就好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……唉，不能太期待了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_15D9")

    label("loc_14DB")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "今天，我去工房四处转了转，\x01",
            "订购了一些导力相机。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "操作简单的相机，\x01",
            "在共和国也一定很好卖的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "明天把货品领回来，商谈就搞定了。\x01",
            "这样就可以回国了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，要是我家的卡雷尔\x01",
            "能正正经经地\x01",
            "给我帮忙到最后就好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……唉，不能太过期待了。\x02",
    )

    CloseMessageWindow()

    label("loc_15D9")

    Jump("loc_170E")

    label("loc_15DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1681")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1635")

    ChrTalk(
        0xFE,
        (
            "……哎呀，\x01",
            "卡雷尔还是不在。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是的，\x01",
            "那个孩子一点都不安分呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_167E")

    label("loc_1635")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "呼啊啊啊……\x01",
            "啊～好困。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，时间还早呢。\x01",
            "还是下午去工房吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_167E")

    Jump("loc_170E")

    label("loc_1681")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_170E")

    ChrTalk(
        0xFE,
        (
            "这个房间非常宽敞， \x01",
            "让人感到十分舒适呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不愧是高级房间，\x01",
            "花钱多一些也是值得的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那就好好休息吧。\x01",
            "商谈从明天才开始呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_170E")

    TalkEnd(0xFE)
    Return()

    # Function_16_13FF end

    def Function_17_1712(): pass

    label("Function_17_1712")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_17D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1760")

    ChrTalk(
        0xC,
        (
            "#151F那个～不好意思。\x02\x03",
            "可以借用一下\x01",
            "这里的通信器吗～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17D5")

    label("loc_1760")

    OP_A2(0x4)

    ChrTalk(
        0xC,
        (
            "#150F奈尔前辈要我\x01",
            "拍的照片已经拍好了……\x02\x03",
            "现在还是马上到\x01",
            "下一个取材地点去吧～\x02\x03",
            "啊，\x01",
            "还是再联络总编问一下吧～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17D5")

    TalkEnd(0xFE)
    Return()

    # Function_17_1712 end

    def Function_18_17D9(): pass

    label("Function_18_17D9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_19D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1835")

    ChrTalk(
        0x10E,
        (
            "#130F这个时间还在工作，\x01",
            "做游击士也很辛苦啊。\x02\x03",
            "那么，你们要加油哦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19D0")

    label("loc_1835")

    OP_A2(0x3)

    ChrTalk(
        0x10E,
        (
            "#130F哎呀……\x01",
            "艾丝蒂尔、约修亚。\x02\x03",
            "今天白天你们辛苦了吧。\x01",
            "掌握到什么线索了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯……\x01",
            "说到线索的话确实有一些吧……\x02\x03",
            "……对不起，教授。\x01",
            "现在有很急的事情要做呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10E,
        (
            "#130F哦，是吗？\x02\x03",
            "竟然工作到这么晚……\x01",
            "做游击士也很辛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F今天比较特别嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F那么，不好意思，\x01",
            "我们就先告辞了。\x02\x03",
            "能向我们提供情报，\x01",
            "真是多谢您了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10E,
        (
            "#130F我能帮忙的事情\x01",
            "也就只有这些了。\x02\x03",
            "那么，你们要加油哦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19D0")

    TalkEnd(0xFE)
    Return()

    # Function_18_17D9 end

    def Function_19_19D4(): pass

    label("Function_19_19D4")

    TalkBegin(0x8)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",      # 0
            "休息\x01",      # 1
            "离开\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A33")
    OP_0D()
    OP_A9(0x3F)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_1A33")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A44")
    TalkEnd(0x8)
    Return()

    label("loc_1A44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1B54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1AE4")

    ChrTalk(
        0x8,
        (
            "今天也要和\x01",
            "艾玛好好谈谈，\x01",
            "让她努力工作才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "在下一批客人来之前，\x01",
            "必须将全部客房\x01",
            "收拾得一尘不染。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "经营酒店\x01",
            "就是在和时间打仗呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B51")

    label("loc_1AE4")

    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "欢迎光临。\x01",
            "这里是蔡恩拉德酒店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "现在随时可以给您\x01",
            "准备您喜欢的房间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "请务必来我们这里住宿。\x02",
    )

    CloseMessageWindow()

    label("loc_1B51")

    Jump("loc_2225")

    label("loc_1B54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1C30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1BBD")

    ChrTalk(
        0x8,
        (
            "唉，\x01",
            "果然蔡斯这地方的孩子就是麻烦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "……不过其实我自己\x01",
            "也是个纯粹的蔡斯人呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C2D")

    label("loc_1BBD")

    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "唉，\x01",
            "还好我留意了艾玛的行动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "她似乎误解了\x01",
            "我叮嘱她的话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "唉，\x01",
            "果然蔡斯这地方的孩子就是麻烦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C2D")

    Jump("loc_2225")

    label("loc_1C30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_1D62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1CB4")

    ChrTalk(
        0x8,
        (
            "唉，真是的。\x01",
            "提到艾玛……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "她为什么要用那么大的声音\x01",
            "和别人打招呼呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "要是吓走了客人，\x01",
            "那该怎么办啊？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D5F")

    label("loc_1CB4")

    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "唉，真是的，\x01",
            "我都那样提醒她了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "她为什么要用那么大的声音\x01",
            "和别人打招呼呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "虽说我知道\x01",
            "她作为新来的干活很卖力……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "可要是吓走了客人，\x01",
            "那该怎么办啊？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D5F")

    Jump("loc_2225")

    label("loc_1D62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_1DA1")

    ChrTalk(
        0x8,
        "啊，欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "工作到这么晚，\x01",
            "真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2225")

    label("loc_1DA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1E81")

    ChrTalk(
        0x8,
        "没想到工房竟然发生了袭击事件……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "虽然感到很震惊，\x01",
            "不过连我们酒店从业员都表现出动摇的话，\x01",
            "那么就会在客人中间散布不安的情绪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "一定要像平常那样\x01",
            "为各位客人提供服务……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那样客人们应该\x01",
            "也会感到安心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2225")

    label("loc_1E81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1EC2")

    ChrTalk(
        0x8,
        (
            "从刚才开始，\x01",
            "工房那边就很吵闹。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "难道出事了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2225")

    label("loc_1EC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2043")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1F65")

    ChrTalk(
        0x8,
        (
            "对蔡斯人来说\x01",
            "就算被要求若无其事的服务，\x01",
            "也是很难理解的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "总之，\x01",
            "认真努力工作就是蔡斯人的本色。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "……当然如您所知，\x01",
            "也有不少例外。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2040")

    label("loc_1F65")

    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "接待客人的时候，\x01",
            "为了不让客人紧张，\x01",
            "表现得镇定自如也是很重要的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "就算是向蔡斯人要求\x01",
            "那种不加伪装自然的服务，\x01",
            "也是很难理解的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "总之，\x01",
            "认真努力工作就是蔡斯人的本色。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "无论如何\x01",
            "也还是要加把劲呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2040")

    Jump("loc_2225")

    label("loc_2043")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_20E2")

    ChrTalk(
        0x8,
        (
            "呼，\x01",
            "昨晚真是给客人添麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不过总算是万幸，\x01",
            "没用多长时间导力就恢复供应了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "没有导力灯的夜晚，\x01",
            "自从导力革命后好像还是第一次。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2225")

    label("loc_20E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_21BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_213C")

    ChrTalk(
        0x8,
        "顺便提一下……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我们还是第一家实现\x01",
            "全部由导力提供照明的酒店哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21B8")

    label("loc_213C")

    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "欢迎光临。\x01",
            "这里是蔡恩拉德酒店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "本酒店是王国中仅有的\x01",
            "几家历史悠久的酒店之一。\x01",
            "而我已经是本酒店第六代负责人了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21B8")

    Jump("loc_2225")

    label("loc_21BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2225")

    ChrTalk(
        0x8,
        (
            "欢迎光临。\x01",
            "这里是蔡恩拉德酒店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "本酒店会为您\x01",
            "提供尽心周到的服务。\x01",
            "我想一定能令您满意的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2225")

    TalkEnd(0x8)
    Return()

    # Function_19_19D4 end

    def Function_20_2229(): pass

    label("Function_20_2229")

    Call(0, 19)
    Return()

    # Function_20_2229 end

    def Function_21_222E(): pass

    label("Function_21_222E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2301")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_228A")

    ChrTalk(
        0xFE,
        (
            "好的，那就……\x01",
            "首先打扫这房间！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，艾玛。\x01",
            "要拿出气势来哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22FE")

    label("loc_228A")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "今天早上\x01",
            "主管这么对我说……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在没有客人的地方努力\x01",
            "是可以的哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呵呵，今天到现在为止\x01",
            "我都很努力哦～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22FE")

    Jump("loc_282C")

    label("loc_2301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2410")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_236A")

    ChrTalk(
        0xFE,
        (
            "我努力干活的样子被主管看见，\x01",
            "又让她生气了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么接下来\x01",
            "我就不这么努力干活了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_240D")

    label("loc_236A")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "好的，那就……\x01",
            "这个房间已经打扫完了，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "剩下的只有隔壁了。\x01",
            "那么，接下来也要加油……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……哦。\x01",
            "不能太努力了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那，就马虎点。\x01",
            "马虎点……就行了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_240D")

    Jump("loc_282C")

    label("loc_2410")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_24F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2482")

    ChrTalk(
        0xFE,
        (
            "主管训斥我，\x01",
            "说我『努力过度』什么的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我是个新来的，\x01",
            "工作努力应该是\x01",
            "理所当然的啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24F2")

    label("loc_2482")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "主管训斥我，\x01",
            "说我『努力过度』什么的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我是个新来的，\x01",
            "工作努力应该是\x01",
            "理所当然的啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24F2")

    Jump("loc_282C")

    label("loc_24F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_256C")

    ChrTalk(
        0xFE,
        (
            "刚才，\x01",
            "有个学者打扮的客人告诉我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没想到中央工房\x01",
            "竟然被袭击了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "吓了一跳吧？\x01",
            "我也很吃惊呢！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_282C")

    label("loc_256C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2650")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_25DF")

    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "总觉得城里的气氛有点奇怪……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我问过主管，\x01",
            "她也不告诉我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊啊，我有些在意呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_264D")

    label("loc_25DF")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "总觉得城里的气氛有点奇怪……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我问过主管，\x01",
            "她也不告诉我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "总不能向客人打听吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_264D")

    Jump("loc_282C")

    label("loc_2650")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2688")

    ChrTalk(
        0xFE,
        "欢迎光临～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "欢迎来到蔡恩拉德酒店！\x02",
    )

    CloseMessageWindow()
    Jump("loc_282C")

    label("loc_2688")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_26CF")

    ChrTalk(
        0xFE,
        (
            "好，\x01",
            "这间房间也打扫干净了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那我就去打扫下一间吧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_282C")

    label("loc_26CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_27D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_272B")

    ChrTalk(
        0xFE,
        "刚、刚才真的是失礼了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "想要住宿的话，\x01",
            "请一定要来我们酒店哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27D2")

    label("loc_272B")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "你、你们好！\x01",
            "我、我是新人艾玛！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天我也会\x01",
            "更加用心拼命努力的。\x01",
            "希望你们也能在酒店住得舒服哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们看上去好像不是\x01",
            "在这里住宿的客人啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27D2")

    Jump("loc_282C")

    label("loc_27D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_282C")

    ChrTalk(
        0xFE,
        (
            "床单换好后，\x01",
            "接下来要清点家具用品……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "工作量像山一样多，\x01",
            "加油吧艾玛！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_282C")

    TalkEnd(0xFE)
    Return()

    # Function_21_222E end

    def Function_22_2830(): pass

    label("Function_22_2830")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_28A8")

    ChrTalk(
        0xFE,
        (
            "似、似乎\x01",
            "发生什么事情了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本来还打算\x01",
            "一会儿去飞艇坪参观一下……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "或许改个日子\x01",
            "会比较好吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B6E")

    label("loc_28A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2A1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2917")

    ChrTalk(
        0xFE,
        (
            "毕竟是做大买卖的人，\x01",
            "器量就是不一样啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我要以那样的商人为目标，\x01",
            "今后也要好好努力。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A17")

    label("loc_2917")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "昨天，在工房遇到了麻烦，\x01",
            "幸好一位名叫鲁特尔的人帮助了我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "多亏了他，\x01",
            "才能顺利地采购齐制暖用的导力器。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "据说鲁特尔是\x01",
            "从事飞艇中介行业的商人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "毕竟是做大买卖的人，\x01",
            "器量就是不一样啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他利落地指挥着店员，\x01",
            "很快就帮我找到目标商品。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A17")

    Jump("loc_2B6E")

    label("loc_2A1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2B6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2A86")

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "昨天晚上酒店的照明\x01",
            "停了一会儿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个导力灯，\x01",
            "是不是寿命就要到了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B6E")

    label("loc_2A86")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "不愧是利贝尔，真厉害。\x01",
            "连照明都已经全部导力化了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们的村子位于\x01",
            "气候严酷的共和国高原上，\x01",
            "导力器还没有普及呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这次我就是为了购买\x01",
            "采暖用的导力器而来到蔡斯的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，稍微休息一下，\x01",
            "然后就去有名的中央工房看看。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B6E")

    TalkEnd(0xFE)
    Return()

    # Function_22_2830 end

    SaveToFile()

Try(main)
