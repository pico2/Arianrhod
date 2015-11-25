from ED6ScenarioHelper import *

def main():
    # 卢安

    CreateScenaFile(
        FileName            = 'T2331   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2331.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        '雷克斯',                               # 9
        '卡拉',                                 # 10
        '特蕾莎院长',                           # 11
        '达尼艾尔',                             # 12
        '玛丽',                                 # 13
        '波利',                                 # 14
        '克拉姆',                               # 15
        '戴尔蒙市长',                           # 16
        '秘书基尔巴特',                         # 17
        '卡露娜',                               # 18
        '阿尔宾',                               # 19
        '蔡尔德',                               # 20
        '卢希娅',                               # 21
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
        'ED6_DT07/CH01270 ._CH',             # 00
        'ED6_DT07/CH02590 ._CH',             # 01
        'ED6_DT07/CH02640 ._CH',             # 02
        'ED6_DT07/CH02630 ._CH',             # 03
        'ED6_DT07/CH02570 ._CH',             # 04
        'ED6_DT07/CH02410 ._CH',             # 05
        'ED6_DT07/CH02420 ._CH',             # 06
        'ED6_DT07/CH01030 ._CH',             # 07
        'ED6_DT07/CH01240 ._CH',             # 08
        'ED6_DT07/CH02500 ._CH',             # 09
        'ED6_DT07/CH01040 ._CH',             # 0A
        'ED6_DT07/CH01140 ._CH',             # 0B
        'ED6_DT07/CH01070 ._CH',             # 0C
        'ED6_DT06/CH20093 ._CH',             # 0D
        'ED6_DT06/CH20101 ._CH',             # 0E
        'ED6_DT06/CH20053 ._CH',             # 0F
        'ED6_DT07/CH01023 ._CH',             # 10
        'ED6_DT07/CH01143 ._CH',             # 11
    )

    AddCharChipPat(
        'ED6_DT07/CH01270P._CP',             # 00
        'ED6_DT07/CH02590P._CP',             # 01
        'ED6_DT07/CH02640P._CP',             # 02
        'ED6_DT07/CH02630P._CP',             # 03
        'ED6_DT07/CH02570P._CP',             # 04
        'ED6_DT07/CH02410P._CP',             # 05
        'ED6_DT07/CH02420P._CP',             # 06
        'ED6_DT07/CH01030P._CP',             # 07
        'ED6_DT07/CH01240P._CP',             # 08
        'ED6_DT07/CH02500P._CP',             # 09
        'ED6_DT07/CH01040P._CP',             # 0A
        'ED6_DT07/CH01140P._CP',             # 0B
        'ED6_DT07/CH01070P._CP',             # 0C
        'ED6_DT06/CH20093P._CP',             # 0D
        'ED6_DT06/CH20101P._CP',             # 0E
        'ED6_DT06/CH20053P._CP',             # 0F
        'ED6_DT07/CH01023P._CP',             # 10
        'ED6_DT07/CH01143P._CP',             # 11
    )

    DeclNpc(
        X                   = -25500,
        Z                   = 0,
        Y                   = 43210,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -37500,
        Z                   = 0,
        Y                   = 44500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -50190,
        Z                   = 0,
        Y                   = -1000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -50850,
        Z                   = 0,
        Y                   = 180,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -50850,
        Z                   = 0,
        Y                   = 1400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -50570,
        Z                   = 0,
        Y                   = -2840,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -49420,
        Z                   = 0,
        Y                   = -2280,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 1200,
        Z                   = 4000,
        Y                   = 16700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1200,
        Z                   = 4000,
        Y                   = 16700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -400,
        Z                   = 0,
        Y                   = 45400,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -33200,
        Z                   = 150,
        Y                   = 41740,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -32060,
        Z                   = 150,
        Y                   = 42960,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -23900,
        Z                   = 0,
        Y                   = -1170,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )


    DeclActor(
        TriggerX            = -37020,
        TriggerZ            = 0,
        TriggerY            = 42970,
        TriggerRange        = 400,
        ActorX              = -37500,
        ActorZ              = 1500,
        ActorY              = 44500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -26870,
        TriggerZ            = 0,
        TriggerY            = 42820,
        TriggerRange        = 400,
        ActorX              = -25500,
        ActorZ              = 1500,
        ActorY              = 43210,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_322",          # 00, 0
        "Function_1_5D0",          # 01, 1
        "Function_2_5D1",          # 02, 2
        "Function_3_5E7",          # 03, 3
        "Function_4_5EC",          # 04, 4
        "Function_5_11B6",         # 05, 5
        "Function_6_11BB",         # 06, 6
        "Function_7_175F",         # 07, 7
        "Function_8_17B0",         # 08, 8
        "Function_9_1803",         # 09, 9
        "Function_10_1B6E",        # 0A, 10
        "Function_11_1C13",        # 0B, 11
        "Function_12_1CE1",        # 0C, 12
        "Function_13_1D5B",        # 0D, 13
        "Function_14_1DEE",        # 0E, 14
        "Function_15_1E99",        # 0F, 15
        "Function_16_1EC3",        # 10, 16
        "Function_17_44DA",        # 11, 17
        "Function_18_44EB",        # 12, 18
        "Function_19_44FC",        # 13, 19
        "Function_20_450D",        # 14, 20
        "Function_21_451E",        # 15, 21
        "Function_22_452F",        # 16, 22
        "Function_23_5751",        # 17, 23
        "Function_24_5772",        # 18, 24
        "Function_25_5793",        # 19, 25
        "Function_26_57B4",        # 1A, 26
        "Function_27_57E2",        # 1B, 27
        "Function_28_5815",        # 1C, 28
        "Function_29_5848",        # 1D, 29
        "Function_30_587B",        # 1E, 30
    )


    def Function_0_322(): pass

    label("Function_0_322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_389")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -48350, 0, 150, 215)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -50850, 0, 180, 135)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -50570, 0, -2840, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -49420, 0, -2280, 315)
    Jump("loc_59A")

    label("loc_389")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_421")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x11, -53290, 0, 2040, 180)
    SetChrPos(0xA, -53080, 0, -870, 180)
    SetChrPos(0xB, -50850, 0, -230, 270)
    SetChrPos(0xD, -50850, 0, -1430, 270)
    SetChrPos(0xC, -52530, 0, -2420, 0)
    SetChrPos(0xE, -50800, 0, 1470, 270)
    Jump("loc_59A")

    label("loc_421")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_506")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    OP_72(0x2, 0x20)
    OP_6F(0x2, 15)
    OP_72(0x4, 0x20)
    OP_6F(0x4, 15)
    SetChrPos(0x11, -53000, 0, 2040, 90)
    SetChrPos(0xA, -53000, 0, -870, 90)
    SetChrChipByIndex(0xA, 13)
    SetChrChipByIndex(0x11, 14)
    OP_44(0x11, 0xFF)
    OP_44(0xA, 0xFF)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0x11, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x11, 0x2)
    SetChrFlags(0xA, 0x2)
    SetChrPos(0xB, -50850, 0, -230, 270)
    SetChrPos(0xD, -50850, 0, -1430, 270)
    SetChrPos(0xC, -52530, 0, -2420, 0)
    SetChrPos(0xE, -50800, 0, 1470, 270)
    ClearChrFlags(0x14, 0x80)
    Jump("loc_59A")

    label("loc_506")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_51A")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0x12, 0x10)
    Jump("loc_59A")

    label("loc_51A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_56B")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -48450, 0, -990, 270)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -49690, 0, -120, 90)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -47720, 0, 2100, 0)
    Jump("loc_59A")

    label("loc_56B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_575")
    Jump("loc_59A")

    label("loc_575")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_57F")
    Jump("loc_59A")

    label("loc_57F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_589")
    Jump("loc_59A")

    label("loc_589")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_593")
    Jump("loc_59A")

    label("loc_593")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_59A")

    label("loc_59A")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (107, "loc_5A6"),
        (SWITCH_DEFAULT, "loc_5CF"),
    )


    label("loc_5A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B9")
    OP_A2(0x428)
    Event(0, 16)

    label("loc_5B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CC")
    OP_A2(0x436)
    Event(0, 22)

    label("loc_5CC")

    Jump("loc_5CF")

    label("loc_5CF")

    Return()

    # Function_0_322 end

    def Function_1_5D0(): pass

    label("Function_1_5D0")

    Return()

    # Function_1_5D0 end

    def Function_2_5D1(): pass

    label("Function_2_5D1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5E6")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_5D1")

    label("loc_5E6")

    Return()

    # Function_2_5D1 end

    def Function_3_5E7(): pass

    label("Function_3_5E7")

    Call(0, 4)
    Return()

    # Function_3_5E7 end

    def Function_4_5EC(): pass

    label("Function_4_5EC")

    TalkBegin(0x8)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_64D")
    OP_0D()
    OP_A9(0x2A)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_64D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_65E")
    TalkEnd(0x8)
    Return()

    label("loc_65E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB1")
    EventBegin(0x0)
    OP_69(0x8, 0x320)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A08")

    ChrTalk(
        0x8,
        "欢迎来到『白之木莲亭』。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "啊，以前没见过你们。\x01",
            "是来玛诺利亚村观光的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F不是呢。\x01",
            "其实我们正在去卢安市的途中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们是从柏斯那边\x01",
            "越过古罗尼山峰来到这里的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "越过古罗尼山峰！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "哈～没想到现在这个年代\x01",
            "还会有人爬那座山峰。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "你们平时有爬山的爱好吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F啊……\x01",
            "也不算是啦。\x02\x03",
            "#501F总之，我们走了好久的山路，\x01",
            "现在肚子饿得咕咕直叫呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F这里有什么特别推荐的料理吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "料理的话……\x01",
            "中午特别推荐的就肯定是便当了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F便当？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我们村里的风车屋前\x01",
            "有个可以看到漂亮海景的了望台。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "每到中午的时候，\x01",
            "就有很多客人来这里买便当拿去那里吃。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F啊～好像蛮有趣的嘛⊙\x02\x03",
            "光是听你这么介绍，\x01",
            "我就已经觉得很好吃呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F那么我们就买便当吧。\x02\x03",
            "#010F请问这里的便当有几种呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "今天有海鲜焗饭\x01",
            "和熏火腿三明治两种。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "不管哪一个都非常值得品尝的哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F嗯～\x01",
            "我要熏火腿三明治。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那我要海鲜焗饭吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "多谢惠顾。\x01",
            "两款便当合计１２０米拉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A60")

    label("loc_A08")


    ChrTalk(
        0x8,
        (
            "我们这里今天出售\x01",
            "海鲜焗饭和熏火腿三明治\x01",
            "两种便当。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "一共是１２０米拉，可以吗？\x02",
    )

    CloseMessageWindow()

    label("loc_A60")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【购买】\x01",          # 0
            "【还是算了】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_AC7"),
        (1, "loc_C1C"),
        (SWITCH_DEFAULT, "loc_CAC"),
    )


    label("loc_AC7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BDD")
    OP_4F(0x12, (scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "特制午餐盒饭\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x33C, 1)

    ChrTalk(
        0x8,
        (
            "另外，作为今天的特别服务，\x01",
            "随便当附送香草茶哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "这种茶也是本店的推荐饮品。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F啊～谢谢㈱\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#010F那我们现在就去了望台吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x101,
        "#006F嗯！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x413)
    Jump("loc_C19")

    label("loc_BDD")


    ChrTalk(
        0x8,
        (
            "咦……\x01",
            "好像没有足够的米拉呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "攒够了钱再来吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x401)

    label("loc_C19")

    Jump("loc_CAC")

    label("loc_C1C")


    ChrTalk(
        0x8,
        (
            "那么，\x01",
            "就在这里用餐怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "我们还供应很多别的料理。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F嗯～\x01",
            "我还是想在室外吃便当呢。\x02\x03",
            "#008F不好意思，我们再考虑一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x401)
    Jump("loc_CAC")

    label("loc_CAC")

    EventEnd(0x1)
    Jump("loc_11B2")

    label("loc_CB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_D4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D1E")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "袭击老师他们的犯人\x01",
            "终于被抓住了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "希望他们能够深刻反省，\x01",
            "以偿还自己犯下的罪。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D4B")

    label("loc_D1E")


    ChrTalk(
        0x8,
        (
            "希望被捕的犯人能够深刻反省，\x01",
            "好好赎罪。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D4B")

    Jump("loc_11B2")

    label("loc_D4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_D81")

    ChrTalk(
        0x8,
        (
            "外面已经很暗了。\x01",
            "出去的时候要小心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11B2")

    label("loc_D81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_E67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E0A")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        "马上就要到学园祭了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "孤儿院的孩子们\x01",
            "好像也要到学院里去玩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "能忘记以前的不快，\x01",
            "玩得开心就最好不过了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E64")

    label("loc_E0A")


    ChrTalk(
        0x8,
        (
            "孤儿院的孩子们\x01",
            "好像也要到学院里去玩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "能忘记以前的不快，\x01",
            "玩得开心就最好不过了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E64")

    Jump("loc_11B2")

    label("loc_E67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_EBA")

    ChrTalk(
        0x8,
        (
            "就在刚才，\x01",
            "有个孤儿院的男孩子飞奔出去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "发生什么事情了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_11B2")

    label("loc_EBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_F82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F48")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "听说孤儿院\x01",
            "被烧得精光？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我马上就去\x01",
            "腾出房间给孩子们住。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "小姑娘，如果可以的话，\x01",
            "请你们鼓励一下那些孩子哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F7F")

    label("loc_F48")


    ChrTalk(
        0x8,
        (
            "小姑娘，如果可以的话，\x01",
            "请你们鼓励一下那些孩子哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F7F")

    Jump("loc_11B2")

    label("loc_F82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_FC5")

    ChrTalk(
        0x8,
        "今天的风很宜人啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "沿着海岸散步\x01",
            "感觉很舒服哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11B2")

    label("loc_FC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_10ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_108A")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "来这里的游客大多都是\x01",
            "这里大部分的游客\x01",
            "都是来赏花和观景的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "还有就是\x01",
            "会零零散散过来的登山客。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "以前的人都是通过这里往来于柏斯和卢安的，\x01",
            "所以说村里曾经非常热闹呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10EA")

    label("loc_108A")


    ChrTalk(
        0x8,
        (
            "从这里望向风车小屋，\x01",
            "景色很美丽吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那个风车小屋和湛蓝的大海\x01",
            "搭配起来很是诗情画意呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10EA")

    Jump("loc_11B2")

    label("loc_10ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_1178")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1158")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "哦，\x01",
            "这不是刚才来过的小姑娘吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "有什么事情吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "男孩子？\x01",
            "没有看到啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1175")

    label("loc_1158")


    ChrTalk(
        0x8,
        (
            "男孩子？\x01",
            "没有看到啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1175")

    Jump("loc_11B2")

    label("loc_1178")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_11B2")

    ChrTalk(
        0x8,
        (
            "我们村里的风车屋前\x01",
            "有一个了望台哦。（※假定）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11B2")

    TalkEnd(0x8)
    Return()

    # Function_4_5EC end

    def Function_5_11B6(): pass

    label("Function_5_11B6")

    Call(0, 6)
    Return()

    # Function_5_11B6 end

    def Function_6_11BB(): pass

    label("Function_6_11BB")

    TalkBegin(0x9)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_121A")
    OP_0D()
    OP_A9(0x29)
    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_121A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_122B")
    TalkEnd(0x9)
    Return()

    label("loc_122B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1280")

    ChrTalk(
        0x9,
        "听说犯人被抓住了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "与其交给游击士协会，\x01",
            "我们更想亲自来惩罚他们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_175B")

    label("loc_1280")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_12C9")

    ChrTalk(
        0x9,
        "怎么会变成这样……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "不可原谅……\x01",
            "不可原谅这些犯人……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_175B")

    label("loc_12C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1379")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1336")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "孤儿院的老师和孩子们\x01",
            "就由我们『白之木莲亭』\x01",
            "来好好照顾吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "一人有难大家帮嘛。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1376")

    label("loc_1336")


    ChrTalk(
        0x9,
        (
            "孤儿院的老师和孩子们\x01",
            "就由我们『白之木莲亭』\x01",
            "来好好照顾吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1376")

    Jump("loc_175B")

    label("loc_1379")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_13B6")

    ChrTalk(
        0x9,
        (
            "刚才克拉姆\x01",
            "好像跑出去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "到底怎么了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_175B")

    label("loc_13B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_14EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14AC")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        "啊呀，那件制服是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "难道，\x01",
            "你就是科洛丝吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F啊，是的。\x01",
            "我就是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "孤儿院的孩子们\x01",
            "急着想见你呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "他们应该都\x01",
            "还在二楼的大房间里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "你快点去见见他们吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F嗯，好、好的。\x01",
            "真是麻烦您了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14E9")

    label("loc_14AC")


    ChrTalk(
        0x9,
        (
            "孤儿院的孩子们\x01",
            "急着想见你呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "你快点去见见他们吧。\x02",
    )

    CloseMessageWindow()

    label("loc_14E9")

    Jump("loc_175B")

    label("loc_14EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_158A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1552")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        "好，接下来该洗衣服了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "今天的天气很不错，\x01",
            "晒床单的话应该很快就能干吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1587")

    label("loc_1552")


    ChrTalk(
        0x9,
        (
            "今天的天气很不错，\x01",
            "晒床单的话应该很快就能干吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1587")

    Jump("loc_175B")

    label("loc_158A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_164F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_160C")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "今年的木莲之花\x01",
            "也开始陆陆续续地盛开了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "这里虽然不是什么起眼的村子，\x01",
            "但是来赏木莲花的人\x01",
            "却不少呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_164C")

    label("loc_160C")


    ChrTalk(
        0x9,
        (
            "这里虽然不是什么起眼的村子，\x01",
            "但是来赏木莲花的人\x01",
            "却不少呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_164C")

    Jump("loc_175B")

    label("loc_164F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_16A7")

    ChrTalk(
        0x9,
        (
            "男孩子？\x01",
            "我没见过呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "如果是王立学院的女生，\x01",
            "那刚才还见到过一个……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_175B")

    label("loc_16A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_175B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_172E")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        "哟，两位客人你好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "如果可以的话，\x01",
            "请在我们这里享用午餐吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "和丈夫一起经营旅馆，\x01",
            "我也渐渐有了信心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_175B")

    label("loc_172E")


    ChrTalk(
        0x9,
        (
            "如果可以的话，\x01",
            "请在我们这里享用午餐吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_175B")

    TalkEnd(0x9)
    Return()

    # Function_6_11BB end

    def Function_7_175F(): pass

    label("Function_7_175F")

    TalkBegin(0x12)

    ChrTalk(
        0xFE,
        (
            "老师和孩子们\x01",
            "由我们日夜轮流来守护。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们就安心地\x01",
            "去搜查犯人吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x12)
    Return()

    # Function_7_175F end

    def Function_8_17B0(): pass

    label("Function_8_17B0")

    TalkBegin(0x13)

    ChrTalk(
        0xFE,
        (
            "唔，\x01",
            "虽然不知道能不能派上用场……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是我们打算\x01",
            "尽自己所能来帮忙。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x13)
    Return()

    # Function_8_17B0 end

    def Function_9_1803(): pass

    label("Function_9_1803")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_19DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1998")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "#750F啊，是你们几个……\x02\x03",
            "我从旅馆的人那里听说了。\x01",
            "你们已经把那些犯人抓住了吧。\x02\x03",
            "总是给你们添麻烦，\x01",
            "我该怎么感谢你们才好呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F您、您这么说，\x01",
            "我们会不好意思的。\x02\x03",
            "而且……\x02\x03",
            "（嗯……现在还是不要\x01",
            "　把实情说出来比较好啊……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F……我们还要报告工作情况，\x01",
            "所以现在要先回卢安。\x02\x03",
            "犯人们如今在\x01",
            "卡露娜小姐的严密监视之下，\x01",
            "请你们放心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#750F嗯，真的非常感谢你们……\x02",
    )

    CloseMessageWindow()
    Jump("loc_19D7")

    label("loc_1998")


    ChrTalk(
        0xFE,
        (
            "#750F最近我总是给你们添麻烦，\x01",
            "我该怎么感谢你们才好呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19D7")

    Jump("loc_1B6A")

    label("loc_19DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_1A02")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "特蕾莎院长安静地睡着。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_1B6A")

    label("loc_1A02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1A88")

    ChrTalk(
        0xFE,
        (
            "#750F啊，艾丝蒂尔、约修亚。\x02\x03",
            "这段时间真的帮了我们大忙啊。\x01",
            "　\x02\x03",
            "我们也受到了玛诺利亚村村民的照顾，\x01",
            "真是太感谢大家了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B6A")

    label("loc_1A88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1B6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B24")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "#750F我已经听玛丽说了。\x02\x03",
            "怎么会这样呢……\x01",
            "那孩子竟然听到了那件事……\x02\x03",
            "求求你们了。\x01",
            "请一定要把克拉姆带回来。\x02\x03",
            "我一会儿也会赶过去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B6A")

    label("loc_1B24")


    ChrTalk(
        0xFE,
        (
            "#750F求求你们了。\x01",
            "请一定要把克拉姆带回来。\x02\x03",
            "我一会儿也会赶过去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B6A")

    TalkEnd(0xFE)
    Return()

    # Function_9_1803 end

    def Function_10_1B6E(): pass

    label("Function_10_1B6E")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1BC3")

    ChrTalk(
        0xFE,
        (
            "#770F啊，是姐姐你们啊！\x02\x03",
            "你们已经把那些家伙抓住了吧？\x01",
            "　\x02\x03",
            "真厉害！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C0F")

    label("loc_1BC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_1C0F")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(
        0xFE,
        (
            "#773F约修亚哥哥……\x02\x03",
            "我，一定要成为\x01",
            "像哥哥一样强的人……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C0F")

    TalkEnd(0xE)
    Return()

    # Function_10_1B6E end

    def Function_11_1C13(): pass

    label("Function_11_1C13")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1C5F")

    ChrTalk(
        0xFE,
        (
            "清早的时候\x01",
            "老师终于醒过来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嘿嘿嘿，真是太好了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CDD")

    label("loc_1C5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_1CB3")

    ChrTalk(
        0xFE,
        (
            "大家终于都\x01",
            "稍微镇静下来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "接下来只要等\x01",
            "老师醒过来就行了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CDD")

    label("loc_1CB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1CDD")

    ChrTalk(
        0xFE,
        (
            "大姐姐，\x01",
            "克拉姆就拜托你们了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CDD")

    TalkEnd(0xC)
    Return()

    # Function_11_1C13 end

    def Function_12_1CE1(): pass

    label("Function_12_1CE1")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1D17")

    ChrTalk(
        0xFE,
        (
            "哈～一旦放心下来，\x01",
            "肚子就觉得饿了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D57")

    label("loc_1D17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_1D33")

    ChrTalk(
        0xFE,
        "呜……呜……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D57")

    label("loc_1D33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1D57")

    ChrTalk(
        0xFE,
        (
            "克拉姆他\x01",
            "突然怎么了啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D57")

    TalkEnd(0xB)
    Return()

    # Function_12_1CE1 end

    def Function_13_1D5B(): pass

    label("Function_13_1D5B")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1D83")

    ChrTalk(
        0xFE,
        (
            "哇～\x01",
            "老师醒过来了～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DEA")

    label("loc_1D83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_1DA9")

    ChrTalk(
        0xFE,
        "老师……不会有事吧……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DEA")

    label("loc_1DA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1DEA")

    ChrTalk(
        0xFE,
        (
            "克拉姆他啊，\x01",
            "在吃布丁的时候\x01",
            "不知道又在想些什么事情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DEA")

    TalkEnd(0xD)
    Return()

    # Function_13_1D5B end

    def Function_14_1DEE(): pass

    label("Function_14_1DEE")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1E74")

    ChrTalk(
        0xFE,
        (
            "在事情了结之前，\x01",
            "这些属于特蕾莎院长的捐款\x01",
            "就先由我来暂代保管吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这次我一定会保护好的，\x01",
            "所以你们就安心出发吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E95")

    label("loc_1E74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_1E95")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "卡露娜安静地睡着。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1E95")

    TalkEnd(0x11)
    Return()

    # Function_14_1DEE end

    def Function_15_1E99(): pass

    label("Function_15_1E99")

    TalkBegin(0x14)

    ChrTalk(
        0xFE,
        (
            "卢希娅一定要\x01",
            "鼓励大家才行……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x14)
    Return()

    # Function_15_1E99 end

    def Function_16_1EC3(): pass

    label("Function_16_1EC3")

    EventBegin(0x0)
    OP_6D(-50180, 0, -790, 0)
    OP_6B(2800, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xA, -52390, 0, 510, 90)
    SetChrPos(0xB, -50850, 0, 180, 315)
    SetChrPos(0xD, -50850, 0, 1400, 225)
    SetChrPos(0xC, -50570, 0, -2840, 45)
    SetChrPos(0xE, -49420, 0, -2280, 225)
    SetChrPos(0x101, -46270, 0, -1540, 270)
    SetChrPos(0x102, -46100, 0, -760, 270)
    SetChrPos(0x136, -47050, 0, -1030, 270)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x136,
        "#043F老师、孩子们……！\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xD, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_4A(0xD, 255)
    OP_4A(0xC, 255)
    OP_4A(0xE, 255)

    def lambda_204D():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_204D)

    def lambda_205B():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_205B)

    def lambda_2069():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2069)

    def lambda_2077():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2077)

    def lambda_2085():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2085)
    Sleep(400)

    ChrTalk(
        0xE,
        "#774F啊，科洛丝姐姐！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "姐姐来了啊……！\x02",
    )

    CloseMessageWindow()

    def lambda_20C9():
        OP_6D(-50670, 0, -380, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_20C9)

    def lambda_20E1():
        OP_8F(0xFE, 0xFFFF41A6, 0x0, 0xFFFFFE8E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_20E1)
    Sleep(100)

    def lambda_2101():
        OP_8E(0xFE, 0xFFFF3DD2, 0x0, 0x21C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2101)
    Sleep(100)

    def lambda_2121():
        OP_8E(0xFE, 0xFFFF3D5A, 0x0, 0xFFFFFF38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2121)

    def lambda_213C():
        OP_8E(0xFE, 0xFFFF3FD0, 0x0, 0xFFFFFB50, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_213C)
    Sleep(100)

    def lambda_215C():
        OP_8E(0xFE, 0xFFFF4322, 0x0, 0xFFFFFBD2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_215C)
    WaitChrThread(0xE, 0x2)
    TurnDirection(0xE, 0x136, 400)

    ChrTalk(
        0x136,
        (
            "#042F#2P大家……\x01",
            "都没受伤吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#1P嗯，没事！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "嘿嘿。\x01",
            "波利也没事～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#048F#2P太好了……\x01",
            "真是太好了……\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xA, 0x4)
    OP_8E(0xA, 0xFFFF394A, 0x0, 0xB4, 0x7D0, 0x0)

    ChrTalk(
        0xA,
        (
            "#750F呵呵……\x01",
            "你能来真是太好了。\x02\x03",
            "#751F艾丝蒂尔和约修亚\x01",
            "也一起来了啊？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_225E():

        label("loc_225E")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_225E")

    QueueWorkItem2(0xA, 1, lambda_225E)

    def lambda_226F():

        label("loc_226F")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_226F")

    QueueWorkItem2(0xB, 1, lambda_226F)

    def lambda_2280():

        label("loc_2280")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_2280")

    QueueWorkItem2(0xD, 1, lambda_2280)

    def lambda_2291():

        label("loc_2291")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_2291")

    QueueWorkItem2(0xC, 1, lambda_2291)

    def lambda_22A2():

        label("loc_22A2")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_22A2")

    QueueWorkItem2(0xE, 1, lambda_22A2)

    def lambda_22B3():

        label("loc_22B3")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_22B3")

    QueueWorkItem2(0x136, 1, lambda_22B3)

    def lambda_22C4():
        OP_8E(0xFE, 0xFFFF4124, 0x0, 0xFFFFF498, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_22C4)
    Sleep(500)

    def lambda_22E4():
        OP_8E(0xFE, 0xFFFF441C, 0x0, 0xFFFFF5F6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_22E4)
    WaitChrThread(0x101, 0x2)

    def lambda_2304():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2304)
    WaitChrThread(0x102, 0x2)

    def lambda_2317():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2317)
    Sleep(500)
    OP_44(0xA, 0xFF)

    ChrTalk(
        0x101,
        (
            "#000F嗯……\x01",
            "有人通知了游击士协会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们是来调查的，\x01",
            "顺便和科洛丝一起来看望你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#750F是吗……\x01",
            "谢谢你们的关心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#772F#2P你说来调查……\x01",
            "是来调查昨天的火灾吗？\x02\x03",
            "发现什么了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F这个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F该怎么说好呢……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔和约修亚\x01",
            "为难地互相交换了一下眼神。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TurnDirection(0x136, 0x101, 400)
    OP_62(0x136, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x136)
    OP_44(0x136, 0xFF)
    TurnDirection(0x136, 0xB, 400)
    Sleep(200)
    TurnDirection(0x136, 0x102, 400)

    ChrTalk(
        0x136,
        (
            "#040F好了，孩子们。\x01",
            "大家的肚子都饿了吧？\x02\x03",
            "我还没有吃早饭呢，\x01",
            "正准备到下面食堂吃点东西。\x02\x03",
            "#041F所以呢，\x01",
            "今天就请大家吃点好东西好吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2535():

        label("loc_2535")

        TurnDirection(0xFE, 0x136, 400)
        OP_48()
        Jump("loc_2535")

    QueueWorkItem2(0x101, 1, lambda_2535)

    def lambda_2546():

        label("loc_2546")

        TurnDirection(0xFE, 0x136, 400)
        OP_48()
        Jump("loc_2546")

    QueueWorkItem2(0x102, 1, lambda_2546)
    Sleep(50)

    def lambda_255C():

        label("loc_255C")

        TurnDirection(0xFE, 0x136, 400)
        OP_48()
        Jump("loc_255C")

    QueueWorkItem2(0xA, 1, lambda_255C)
    OP_44(0xB, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xE, 0xFF)
    Sleep(50)

    def lambda_2582():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2582)

    def lambda_2590():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2590)
    Sleep(50)

    def lambda_25A3():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_25A3)

    def lambda_25B1():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_25B1)

    ChrTalk(
        0xB,
        "#1P哎？真的！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "波利要吃布丁！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#773F#3P可、可是姐姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#1P…………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xE, 400)

    ChrTalk(
        0xC,
        "#1P走吧，克拉姆。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xC, 400)

    ChrTalk(
        0xE,
        "#774F#4P哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#1P别啰嗦了，\x01",
            "快点过来啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#1P科洛丝姐姐，\x01",
            "我们快点下去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#048F呵呵，好呢。\x02",
    )

    CloseMessageWindow()
    OP_43(0x136, 0x2, 0x0, 0x11)
    OP_43(0xE, 0x2, 0x0, 0x12)
    OP_43(0xC, 0x2, 0x0, 0x13)
    OP_43(0xB, 0x2, 0x0, 0x14)
    OP_43(0xD, 0x2, 0x0, 0x15)

    def lambda_26D4():
        OP_8E(0xFE, 0xFFFF51F0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_26D4)
    Sleep(600)

    def lambda_26F4():
        OP_8E(0xFE, 0xFFFF51F0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_26F4)
    Sleep(50)

    def lambda_2714():
        OP_8E(0xFE, 0xFFFF51F0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2714)
    Sleep(200)

    def lambda_2734():
        OP_8E(0xFE, 0xFFFF51F0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2734)
    Sleep(300)

    def lambda_2754():
        OP_8E(0xFE, 0xFFFF51F0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2754)
    WaitChrThread(0x136, 0x1)
    SetChrFlags(0x136, 0x80)
    WaitChrThread(0xE, 0x1)
    SetChrFlags(0xE, 0x80)
    WaitChrThread(0xC, 0x1)
    SetChrFlags(0xC, 0x80)
    WaitChrThread(0xB, 0x1)
    SetChrFlags(0xB, 0x80)
    WaitChrThread(0xD, 0x1)
    SetChrFlags(0xD, 0x80)
    Sleep(500)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0xA, 0xFF)

    ChrTalk(
        0x101,
        (
            "#007F呼……还好没事。\x02\x03",
            "调查的事还是不要\x01",
            "让孩子们知道好一些……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#4P是啊。\x02\x03",
            "#010F不过，那个叫玛丽的孩子\x01",
            "似乎已经察觉到我们的意思……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#751F呵呵，有这样懂事的孩子，\x01",
            "我自己也觉得很欣慰啊……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 0)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#750F对了，\x01",
            "你们刚才说是来调查。\x02\x03",
            "想知道些什么，请随便问吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 0)
    Sleep(100)
    TurnDirection(0x102, 0xA, 0)

    ChrTalk(
        0x102,
        "#012F#4P多谢您的配合。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F嗯，那么……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, -49200, 0, -1200, 0)
    SetChrPos(0x102, -50100, 0, -990, 45)
    SetChrPos(0xA, -49670, 0, 200, 180)
    OP_6D(-50810, 0, 340, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "首先，根据我们在火灾现场\x01",
            "调查得到的结果来看……\x02\x03",
            "这次火灾并不是意外， \x01",
            "人为纵火的可能性极高。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#754F#2P是吗……果然啊……\x02\x03",
            "我也觉得着火的时候\x01",
            "屋外的情况确实有点古怪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F我们想问问您……\x01",
            "您觉得有什么可疑的人物吗？\x02\x03",
            "也就是说， \x01",
            "谁会有做这种事的动机。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#757F#2P……我不清楚……\x02\x03",
            "我们几乎没有什么钱财，\x01",
            "印象中也完全没和别人结怨……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F也就是说，\x01",
            "犯人的动机既不是抢劫也不是报复吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F这样的话，虽然很不愿相信，\x01",
            "但有可能是纯粹的恶作剧犯罪。\x02\x03",
            "事件发生前后，\x01",
            "有什么不寻常的事情吗？\x02\x03",
            "比如说有没有\x01",
            "陌生人在孤儿院附近晃荡……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#756F#2P这个嘛……\x02\x03",
            "除了白天见到了你们之外，\x01",
            "就没有什么特别的了……\x02\x03",
            "#757F……也应该跟那个人无关的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F那个人？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#754F#2P在我们将要逃出\x01",
            "被大火包围的屋子的时候……\x02\x03",
            "天花板上的梁柱突然掉了下来，\x01",
            "挡住了通往门口的路。\x02\x03",
            "#750F但就在那个时候，\x01",
            "有人打破了门，冲了进来……\x02\x03",
            "那个人挪开了梁柱，\x01",
            "把我和孩子们救了出去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F还、还有这么一回事啊。\x02\x03",
            "那人是玛诺利亚的村民吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#756F#2P那个人把我们救出来之后，\x01",
            "说去村子里叫人过来，\x01",
            "连名字都没有留下就离开了……\x02\x03",
            "我问了玛诺利亚的村民，\x01",
            "不过似乎没人知道那个人是谁。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F……这有点可疑。\x02\x03",
            "半夜三更出现在孤儿院附近，\x01",
            "怎么想也有点太过蹊跷了吧。\x02\x03",
            "那是个什么样的人？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#750F#2P是个穿着象牙色外套、\x01",
            "不到３０岁的青年男子。\x02\x03",
            "而且，还有一头耀眼的银发。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F银发……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#750F#2P嗯，虽然看样子还很年轻，\x01",
            "但那深邃的眼神让人感到他饱经沧桑。\x02\x03",
            "看起来不像是坏人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F虽然感觉不是普通人，\x01",
            "但他救了人这点的确是事实……\x02\x03",
            "听起来不像是犯人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F…………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 300)

    ChrTalk(
        0x101,
        (
            "#002F#4P约修亚？\x02\x03",
            "怎么了，为什么发起呆来了？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 200)

    ChrTalk(
        0x102,
        (
            "#013F#1P没什么……\x02\x03",
            "你们说得也对， \x01",
            "也许是哪里过来的游击士也说不定……\x02\x03",
            "#015F总之这个人的事\x01",
            "还是先别下定论的好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F#4P啊，嗯……\x02",
    )

    CloseMessageWindow()
    OP_22(0x10, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x136,
        "#1P……打扰了。\x02",
    )

    CloseMessageWindow()
    OP_22(0xF, 0x0, 0x64)
    Sleep(500)
    TurnDirection(0x136, 0xA, 0)
    ClearChrFlags(0x136, 0x80)

    def lambda_3062():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3062)

    def lambda_3070():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3070)

    def lambda_307E():
        OP_6D(-49000, 0, -520, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_307E)

    def lambda_3096():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x136, 3, lambda_3096)
    OP_8E(0x136, 0xFFFF4818, 0x0, 0xFFFFFCAE, 0x7D0, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        "#000F啊，科洛丝？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那些孩子怎么样了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#041F呵呵……\x01",
            "大家都在下面吃蛋糕呢。\x02\x03",
            "#040F对了，老师。\x01",
            "有两位客人来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#753F客人？\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xF, -44560, 0, -1000, 0)
    SetChrPos(0x10, -44420, 0, -1440, 0)
    OP_9F(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xF, 0xA, 0)

    NpcTalk(
        0xF,
        "男性的声音",
        "#1P打扰了。\x02",
    )

    CloseMessageWindow()
    OP_8E(0x136, 0xFFFF44B2, 0x0, 0xFFFFF8D0, 0x7D0, 0x0)

    def lambda_31C3():

        label("loc_31C3")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_31C3")

    QueueWorkItem2(0x136, 1, lambda_31C3)

    def lambda_31D4():

        label("loc_31D4")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_31D4")

    QueueWorkItem2(0x101, 1, lambda_31D4)

    def lambda_31E5():

        label("loc_31E5")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_31E5")

    QueueWorkItem2(0x102, 1, lambda_31E5)

    def lambda_31F6():

        label("loc_31F6")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_31F6")

    QueueWorkItem2(0xA, 1, lambda_31F6)
    ClearChrFlags(0xF, 0x80)

    def lambda_320C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_320C)

    def lambda_321E():
        OP_8E(0xFE, 0xFFFF4926, 0x0, 0xFFFFFD76, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_321E)
    Sleep(500)
    ClearChrFlags(0x10, 0x80)

    def lambda_3243():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_3243)

    def lambda_3255():
        OP_8E(0xFE, 0xFFFF4DD6, 0x0, 0xFFFFFA60, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3255)
    WaitChrThread(0x10, 0x1)

    ChrTalk(
        0x101,
        "#004F啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F戴尔蒙市长……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#660F#2P啊，昨天碰到的\x01",
            "两位游击士也在啊。\x02\x03",
            "不愧是嘉恩，\x01",
            "这么快就安排人手过来了。\x02\x03",
            "#664F对了……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3306():
        OP_8E(0xFE, 0xFFFF443A, 0x0, 0xFA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3306)
    Sleep(500)

    def lambda_3326():
        OP_8E(0xFE, 0xFFFF4796, 0x0, 0xFFFFFC68, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3326)
    WaitChrThread(0xF, 0x1)
    TurnDirection(0xF, 0xA, 400)
    WaitChrThread(0x10, 0x1)

    ChrTalk(
        0xF,
        (
            "#660F#4P好久不见了，特蕾莎院长。\x02\x03",
            "我刚刚接到报告，\x01",
            "所以就急急忙忙赶了过来。\x02\x03",
            "不过，幸好你们都没事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#750F谢谢您，市长。\x02\x03",
            "要您在百忙之中抽出时间过来，\x01",
            "我真是感到过意不去啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#660F#4P没什么，这也是身为\x01",
            "卢安市长所应尽的职责啊。\x02\x03",
            "#664F而且，虽然不知道是何人所为，\x01",
            "总之这种行径绝不能饶恕。\x02\x03",
            "竟然灭绝人性地把\x01",
            "约瑟夫心爱的屋子给……\x02\x03",
            "#662F简直令人惋惜和气愤啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#754F不……\x02\x03",
            "只要孩子们得救了，\x01",
            "我想他也会觉得欣慰吧。\x02\x03",
            "#757F唯一遗憾的是，\x01",
            "他的遗物全都被烧毁了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#043F特蕾莎老师……\x02",
    )

    CloseMessageWindow()
    OP_8C(0xF, 225, 300)

    ChrTalk(
        0xF,
        (
            "#662F两位游击士，\x01",
            "案件有眉目了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F调查才刚开始，\x01",
            "所以还不能下明确的结论……\x02\x03",
            "不过，经过初步的判断，\x01",
            "也存在着恶作剧性质的犯罪可能。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#664F是吗……\x01",
            "真是令人遗憾啊。\x02\x03",
            "在这美丽的卢安，\x01",
            "竟然也有如此丑恶的人存在。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 315, 400)

    ChrTalk(
        0x10,
        "#673F市长，请恕我失礼……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x10, 400)

    ChrTalk(
        0xF,
        "#660F嗯，什么事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#671F这次的火灾……\x01",
            "该不会是他们几个做的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#662F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F等、等等！\x01",
            "『他们几个』是指谁？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 270, 300)

    ChrTalk(
        0x10,
        (
            "#671F你们几位昨天不是也被他们缠上了吗。\x02\x03",
            "就是聚集在卢安仓库那一带的\x01",
            "那些地痞流氓啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F是他们……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#043F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F恕我多言……\x01",
            "为什么您会怀疑他们？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#671F昨天的事也是这样……\x01",
            "那帮家伙总是跟市长作对，\x01",
            "整天惹是生非，唯恐天下不乱。\x02\x03",
            "甚至以给市长惹麻烦为乐。\x01",
            "　\x02\x03",
            "#673F所以就对和市长\x01",
            "交情很深的特蕾莎院长……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#665F基尔巴特！\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x10, 315, 400)

    ChrTalk(
        0x10,
        "#676F是、是！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#663F不要光凭猜测就\x01",
            "如此口无遮拦地妄下判断。\x02\x03",
            "这是重大的犯罪。\x01",
            "绝不能冤枉任何人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#676F十、十分抱歉。\x01",
            "请恕我考虑不周……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#664F用不着你多嘴，\x01",
            "这两位游击士也\x01",
            "一定会把犯人缉捕归案的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF, 225, 400)

    ChrTalk(
        0xF,
        "#660F我这样说没问题吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，包在我们身上！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我们一定尽力而为。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#661F嗯，这回答真让人放心。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xA, 400)
    Sleep(500)
    OP_8C(0x10, 270, 0)

    ChrTalk(
        0xF,
        (
            "#660F#4P对了，特蕾莎院长……\x01",
            "我有件事想和你谈谈。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#753F什么事呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#660F#4P孤儿院现在毁了，\x01",
            "从今以后你有什么打算？\x02\x03",
            "房子重建需要一段时间，\x01",
            "而且需要花费的金钱也不少吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#757F…………………………\x02\x03",
            "老实说，我也不知该如何是好啊。\x02\x03",
            "我这里虽然有一点积蓄，\x01",
            "但要重建孤儿院的话根本……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F院长老师……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#043F……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#664F#4P果然如此吗……\x02\x03",
            "#660F要不这样吧。\x01",
            "你听听我个人的提议如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#750F……是什么呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#660F#4P其实是这样的，\x01",
            "格兰赛尔有我们戴尔蒙家的别墅。\x02\x03",
            "我平时只是偶尔去住一下，\x01",
            "所以那里一直都是闲置着的……\x02\x03",
            "可以的话，你就和孩子们\x01",
            "搬到我那别墅住一段时间如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#753F哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#660F#4P当然，院长你也不必\x01",
            "为房租这类无关痛痒的事情和我客气。\x02\x03",
            "直到重建的事有眉目为止，\x01",
            "随便你们在那里住多久都没问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#757F但、但这也太麻烦您了……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#661F#4P反正那屋子也没人住。\x02\x03",
            "你要是觉得过意不去……\x01",
            "嗯，那不妨就帮我看管房子吧。\x02\x03",
            "当然，我会付报酬的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#756F市长……\x02\x03",
            "…………………………\x02\x03",
            "#757F能让我考虑一下吗？\x02\x03",
            "真的很感谢您的提议，\x01",
            "不过实在发生了太多事情，\x01",
            "所以我现在很难一下子给您答复……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#664F#4P这也难怪……\x01",
            "你就先好好休息一下吧。\x02\x03",
            "#660F我们这就告辞了。\x02\x03",
            "如果你考虑好了，\x01",
            "可以随时和我联系。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#750F好的……\x01",
            "真的非常感谢您。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x10, 400)

    ChrTalk(
        0xF,
        "#660F基尔巴特，走吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xF, 400)

    ChrTalk(
        0x10,
        "#670F是！\x02",
    )

    CloseMessageWindow()
    OP_8E(0x10, 0xFFFF4818, 0x0, 0xFFFFF9B6, 0x7D0, 0x0)
    OP_8C(0x10, 0, 400)

    def lambda_3EE5():
        OP_8E(0xFE, 0xFFFF4F20, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3EE5)
    WaitChrThread(0xF, 0x1)

    def lambda_3F05():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_3F05)

    def lambda_3F17():
        OP_8E(0xFE, 0xFFFF51F0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3F17)
    Sleep(300)

    def lambda_3F37():
        OP_8E(0xFE, 0xFFFF4F20, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3F37)
    WaitChrThread(0x10, 0x1)

    def lambda_3F57():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_3F57)

    def lambda_3F69():
        OP_8E(0xFE, 0xFFFF51F0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3F69)
    WaitChrThread(0xF, 0x1)
    SetChrFlags(0xF, 0x80)
    WaitChrThread(0x10, 0x1)
    SetChrFlags(0x10, 0x80)
    Sleep(500)

    def lambda_3F9D():
        OP_6D(-49600, 0, -480, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3F9D)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#008F哈～真是吃了一惊。\x02\x03",
            "原来除了梅贝尔市长之外，\x01",
            "这个戴尔蒙市长也是这么大度的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是啊……\x01",
            "真不愧是昔日的豪门贵族。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x136, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x136)

    def lambda_4056():
        OP_6D(-49200, 0, 70, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4056)
    OP_44(0x136, 0xFF)
    OP_8E(0x136, 0xFFFF4354, 0x0, 0xFFFFFF9C, 0x7D0, 0x0)
    TurnDirection(0x136, 0xA, 400)
    OP_44(0xA, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    def lambda_4099():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4099)

    def lambda_40A7():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_40A7)
    TurnDirection(0xA, 0x136, 400)

    ChrTalk(
        0x136,
        (
            "#049F老师，市长的提议，\x01",
            "您打算怎么回应呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#754F是啊……\x01",
            "你又是怎么想的呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#049F…………………………\x02\x03",
            "#049F从常理来说，\x01",
            "我觉得自然是应该接受的。\x02\x03",
            "可是……\x01",
            "你们要是去了王都的话……\x02\x03",
            "#043F不……没什么。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#750F呵呵，我知道你向来\x01",
            "都是个很明白事理的孩子。\x02\x03",
            "没事的，科洛丝。\x01",
            "有什么心里话尽管说出来好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#043F…………………………\x02\x03",
            "#049F要是你们去了王都，\x01",
            "那块香草田就会没人打理……\x02\x03",
            "而且……而且……\x02\x03",
            "#047F我总觉得老师和约瑟夫叔叔\x01",
            "疼爱我照顾我的那段回忆\x01",
            "也会随之消失掉似的……\x02\x03",
            "对不起……\x01",
            "我说了一些任性的话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#750F呵呵，其实我也有同样的感受。\x02\x03",
            "在那里，充满了许多\x01",
            "孩子们和我丈夫的珍贵回忆。\x02\x03",
            "但是我觉得，\x01",
            "和这些回忆相比起来，\x01",
            "如何生存下去才是更加重要的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#049F是的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#750F嗯……\x01",
            "这段时间我就会做出决定的。\x02\x03",
            "你还是继续\x01",
            "专心准备学园祭的事情吧。\x02\x03",
            "那些孩子也都\x01",
            "很期待那天的到来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#048F……是。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 300)

    ChrTalk(
        0xA,
        (
            "#750F艾丝蒂尔、约修亚。\x02\x03",
            "这么说虽然很不好意思……\x01",
            "不过调查的事情，还是要拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 0)
    Sleep(100)
    TurnDirection(0x102, 0xA, 0)

    ChrTalk(
        0x102,
        "#010F请放心交给我们吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F我们一定会捉到犯人，\x01",
            "绝对不会让他们逍遥法外的！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2300   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_1EC3 end

    def Function_17_44DA(): pass

    label("Function_17_44DA")

    Sleep(1500)
    OP_9F(0x136, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_17_44DA end

    def Function_18_44EB(): pass

    label("Function_18_44EB")

    Sleep(2000)
    OP_9F(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_18_44EB end

    def Function_19_44FC(): pass

    label("Function_19_44FC")

    Sleep(2500)
    OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_19_44FC end

    def Function_20_450D(): pass

    label("Function_20_450D")

    Sleep(3000)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_20_450D end

    def Function_21_451E(): pass

    label("Function_21_451E")

    Sleep(3500)
    OP_9F(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_21_451E end

    def Function_22_452F(): pass

    label("Function_22_452F")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-50180, 0, -790, 0)
    AddParty(0x5, 0xFF)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0xA, 0x4)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x9, -52430, 0, 480, 0)
    SetChrPos(0xB, -50850, 0, -1230, 270)
    SetChrPos(0xD, -51540, 0, -2430, 0)
    SetChrPos(0xC, -52530, 0, -2420, 0)
    SetChrPos(0xE, -50800, 0, 1470, 270)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x106, 0x80)
    SetChrPos(0x101, -44330, 0, -1080, 270)
    SetChrPos(0x102, -44330, 0, -1080, 270)
    SetChrPos(0x105, -44330, 0, -1080, 270)
    SetChrPos(0x106, -44330, 0, -1080, 270)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4A(0x9, 255)
    OP_4A(0xB, 255)
    OP_4A(0xD, 255)
    OP_4A(0xC, 255)
    OP_4A(0xE, 255)
    SetChrFlags(0x106, 0x80)
    FadeToBright(1000, 0)
    OP_43(0x105, 0x1, 0x0, 0x19)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_43(0x101, 0x1, 0x0, 0x17)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_43(0x102, 0x1, 0x0, 0x18)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0x11, 0x1)
    OP_62(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xD, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_471E():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_471E)

    def lambda_472C():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_472C)

    def lambda_473A():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_473A)

    def lambda_4748():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4748)

    def lambda_4756():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4756)

    ChrTalk(
        0xE,
        "#775F#2P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "哥哥姐姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#043F孩子们……\x02",
    )

    CloseMessageWindow()
    OP_43(0xB, 0x1, 0x0, 0x1A)
    OP_43(0xC, 0x1, 0x0, 0x1B)
    OP_43(0xE, 0x1, 0x0, 0x1C)
    OP_43(0xD, 0x1, 0x0, 0x1D)
    WaitChrThread(0xB, 0x1)
    OP_43(0x9, 0x1, 0x0, 0x1E)

    ChrTalk(
        0xB,
        "呜哇啊啊啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#1P好可怕啊～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F太好了……\x01",
            "大家都平安无事。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x9, 0x1)

    def lambda_481B():

        label("loc_481B")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_481B")

    QueueWorkItem2(0x102, 1, lambda_481B)

    ChrTalk(
        0x102,
        (
            "#012F对不起。\x01",
            "老师她们的状况如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "放心吧。\x01",
            "两人都没受什么伤。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "只是一直昏迷不醒，\x01",
            "着实让人有些担心……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015F……容我失礼一下。\x02",
    )

    CloseMessageWindow()
    OP_44(0x102, 0xFF)
    SetChrFlags(0x102, 0x40)
    SetChrFlags(0x102, 0x4)

    def lambda_48CD():

        label("loc_48CD")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_48CD")

    QueueWorkItem2(0x101, 1, lambda_48CD)

    def lambda_48DE():

        label("loc_48DE")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_48DE")

    QueueWorkItem2(0x105, 1, lambda_48DE)

    def lambda_48EF():

        label("loc_48EF")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_48EF")

    QueueWorkItem2(0xE, 1, lambda_48EF)

    def lambda_4900():

        label("loc_4900")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_4900")

    QueueWorkItem2(0xC, 1, lambda_4900)

    def lambda_4911():

        label("loc_4911")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_4911")

    QueueWorkItem2(0x9, 1, lambda_4911)
    OP_8E(0x102, 0xFFFF42DC, 0x0, 0x5A, 0x7D0, 0x0)
    OP_8E(0x102, 0xFFFF3F6C, 0x0, 0x3CA, 0x7D0, 0x0)

    def lambda_494A():
        OP_6D(-52260, 0, -520, 2000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_494A)
    OP_8E(0x102, 0xFFFF3896, 0x0, 0x226, 0x7D0, 0x0)
    OP_8E(0x102, 0xFFFF30EE, 0x0, 0x1F4, 0x7D0, 0x0)
    OP_8C(0x102, 0, 400)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_8C(0x102, 180, 400)
    Sleep(1000)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#013F果然没错……\x01",
            "看来是对她们施了催眠药。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F催、催眠药？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F嗯，还能闻到一点刺激性气味。\x02\x03",
            "这是没有副作用的品种，\x01",
            "所以我想应该可以放心……\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xC, 0xFF)

    ChrTalk(
        0x101,
        "#505F嗯……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 90, 400)

    def lambda_4AA6():
        OP_6D(-50370, 0, -640, 1500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4AA6)
    OP_8E(0x102, 0xFFFF3A80, 0x0, 0xF0, 0x7D0, 0x0)
    TurnDirection(0x101, 0xE, 400)

    ChrTalk(
        0x101,
        (
            "#002F对了，克拉姆。\x01",
            "可以告诉我们发生了什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#773F…………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(
        0xC,
        "我来说吧……\x02",
    )

    CloseMessageWindow()
    OP_44(0x9, 0xFF)

    def lambda_4B4B():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4B4B)

    def lambda_4B59():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4B59)
    Sleep(50)

    def lambda_4B6C():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4B6C)

    def lambda_4B7A():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4B7A)
    Sleep(50)

    def lambda_4B8D():
        TurnDirection(0xFE, 0xC, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4B8D)

    def lambda_4B9B():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_4B9B)
    Sleep(50)
    OP_44(0xE, 0xFF)
    TurnDirection(0xE, 0x101, 400)
    Sleep(500)

    ChrTalk(
        0xC,
        (
            "#1P我们……\x01",
            "和游击士姐姐一起\x01",
            "在海道上走着走着……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#1P就在那时，\x01",
            "突然出现了几个蒙面的怪人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#1P游击士姐姐\x01",
            "虽然想把他们赶走……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#1P但是我们很快就被\x01",
            "那几个蒙面的怪人包围了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#1P老师也为了保护我们，\x01",
            "跟那帮怪人纠缠了起来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#1P……然后就……呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F好了好了，大家都吓坏了吧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#773F……那帮家伙……\x01",
            "还把老师身上的信封给抢走了……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4D35():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4D35)
    Sleep(50)

    def lambda_4D48():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_4D48)
    Sleep(50)

    def lambda_4D5B():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4D5B)
    Sleep(50)

    def lambda_4D6E():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4D6E)
    Sleep(50)
    TurnDirection(0x102, 0xE, 400)
    Sleep(500)

    ChrTalk(
        0xE,
        (
            "#775F我……\x01",
            "我想把信封抢回来的，\x01",
            "但一下子就被他们踢倒了……\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xE, 0xFF)
    TurnDirection(0xE, 0x102, 300)

    ChrTalk(
        0xE,
        (
            "#777F约修亚哥哥……\x01",
            "我……没能保护好老师……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#1P……没这回事。\x02\x03",
            "只要你们没事，\x01",
            "老师就一定已经很高兴了。\x02\x03",
            "#012F所以……不要责备自己了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#777F但是……\x01",
            "我……我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "呜……呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F不可原谅……！\x01",
            "到底是什么人干的好事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#047F#2P………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        (
            "#042F#2P现在可以确定的是……\x01",
            "那些蒙面人的犯案手段相当老练。\x02\x03",
            "连游击士都不是他们对手，\x01",
            "甚至还被他们用催眠药弄晕了……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4F74():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4F74)

    def lambda_4F82():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_4F82)

    def lambda_4F90():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4F90)
    TurnDirection(0xE, 0x105, 400)

    ChrTalk(
        0x101,
        "#004F科洛丝……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#042F#2P另外还有一点……\x01",
            "我认为这是有计划的犯罪。\x02\x03",
            "目标当然是\x01",
            "老师身上的那大批捐款……\x02\x03",
            "纵火烧孤儿院\x01",
            "恐怕同样是这些人的所为吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F#1P嗯，这种可能性很高。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F科洛丝……\x01",
            "看来你终于镇定下来了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#043F#2P是的……\x01",
            "因为再沮丧也于事无补。\x02\x03",
            "总之现在要尽快\x01",
            "找到犯人的行踪才行……\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x106, -44560, 0, -1160, 0)
    TurnDirection(0x106, 0x105, 0)
    ClearChrFlags(0x106, 0x80)

    NpcTalk(
        0x106,
        "青年的声音",
        "#1P……我也有同感。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrChipByIndex(0x106, 15)

    def lambda_5173():
        OP_6D(-49600, 0, -620, 1500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5173)
    ClearChrFlags(0x106, 0x80)

    def lambda_5190():
        OP_8E(0xFE, 0xFFFF4598, 0x0, 0xFFFFFD08, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_5190)

    def lambda_51AB():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_51AB)

    def lambda_51B9():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_51B9)

    def lambda_51C7():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_51C7)

    def lambda_51D5():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_51D5)

    def lambda_51E3():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_51E3)

    def lambda_51F1():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_51F1)

    def lambda_51FF():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_51FF)

    def lambda_520D():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_520D)
    OP_9F(0x106, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0x106, 0x1)

    ChrTalk(
        0x101,
        "#004F啊～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F阿加特兄……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#051F事情我在协会听说了。\x02\x03",
            "看来这次的情况\x01",
            "还满棘手的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005F别、别说得好像事不关己一样！\x02\x03",
            "连卡露娜姐姐都\x01",
            "中了他们的暗算啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#053F我知道……\x01",
            "别大呼小叫的。\x02\x03",
            "#050F卡露娜是一流的游击士。\x01",
            "看来是帮相当危险的家伙啊。\x02\x03",
            "把事情经过给我说一遍吧，\x01",
            "说个大概就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F好的……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "约修亚向阿加特说明了\x01",
            "包括捐款被抢在内一系列事情的经过。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x106,
        (
            "#053F嗯，这样啊……\x01",
            "不过事情有点古怪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F古怪？什么古怪？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#050F啊啊，其实是……\x02\x03",
            "『渡鸦帮』的那帮蠢货\x01",
            "已经离开了港口的仓库。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F这、这就是说……\x02\x03",
            "#005F果然是这帮家伙\x01",
            "袭击特蕾莎院长他们吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F不，这还不好说。\x02\x03",
            "我觉得以他们的力量\x01",
            "根本不足以做卡露娜小姐的对手。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F这倒也是……\x02\x03",
            "那帮家伙只会耍嘴皮子，\x01",
            "根本就没什么真功夫。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#057F我盯了他们一阵子，\x01",
            "本来还以为他们变老实了……\x02\x03",
            "谁知道那些蠢货\x01",
            "今天突然不见了……\x02\x03",
            "刚好又在这时候发生了这事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F先不说他们是不是犯人，\x01",
            "但肯定跟这件事脱不了关系。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#050F是啊……\x01",
            "不过现在还不是研究这个的时候。\x02\x03",
            "你们两个，跟我一起走。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F什么呀，忽然冒出这一句……\x02\x03",
            "#002F到底要去哪里啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#053F你还真是迟钝。\x01",
            "当然是去犯罪现场的海道了。\x02\x03",
            "先不管这件事\x01",
            "是不是那帮蠢货干的……\x02\x03",
            "#054F总之要尽量多搜集些线索，\x01",
            "找到犯人的行踪！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊……是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F明白了，我们跟你一起去。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T2301   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_22_452F end

    def Function_23_5751(): pass

    label("Function_23_5751")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF4070, 0x0, 0xFFFFFA6A, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_23_5751 end

    def Function_24_5772(): pass

    label("Function_24_5772")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF430E, 0x0, 0xFFFFFD44, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_24_5772 end

    def Function_25_5793(): pass

    label("Function_25_5793")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF3EA4, 0x0, 0xFFFFFE52, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_25_5793 end

    def Function_26_57B4(): pass

    label("Function_26_57B4")

    OP_62(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0xFFFF3C42, 0x0, 0xFFFFFD12, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_26_57B4 end

    def Function_27_57E2(): pass

    label("Function_27_57E2")

    Sleep(150)
    OP_62(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0xFFFF3F8A, 0x0, 0xFFFFF7B8, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_27_57E2 end

    def Function_28_5815(): pass

    label("Function_28_5815")

    Sleep(100)
    OP_62(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0xFFFF3F12, 0x0, 0x10E, 0xBB8, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_28_5815 end

    def Function_29_5848(): pass

    label("Function_29_5848")

    Sleep(50)
    OP_62(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0xFFFF3D28, 0x0, 0xFFFFFAB0, 0xBB8, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_29_5848 end

    def Function_30_587B(): pass

    label("Function_30_587B")

    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x9, 0x4)
    OP_8E(0x9, 0xFFFF3922, 0x0, 0x15E, 0x7D0, 0x0)
    OP_8E(0x9, 0xFFFF3E4A, 0x0, 0x3F2, 0x7D0, 0x0)
    OP_8E(0x9, 0xFFFF4336, 0x0, 0x35C, 0x7D0, 0x0)
    TurnDirection(0x9, 0x102, 400)
    Return()

    # Function_30_587B end

    SaveToFile()

Try(main)
