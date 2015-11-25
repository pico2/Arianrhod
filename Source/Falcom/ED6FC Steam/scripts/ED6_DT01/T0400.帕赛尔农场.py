from ED6ScenarioHelper import *

def main():
    # 帕赛尔农场

    CreateScenaFile(
        FileName            = 'T0400   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0400.x',
        MapIndex            = 13,
        MapDefaultBGM       = "ed60015",
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
        '缇欧',                                 # 9
        '维鲁',                                 # 10
        '查儿',                                 # 11
        '弗兰兹',                               # 12
        '汉娜',                                 # 13
        '牛',                                   # 14
        '牛',                                   # 15
        '鸡',                                   # 16
        '鸡',                                   # 17
        '鸡',                                   # 18
        '鸡',                                   # 19
        '目标用摄像机',                         # 20
        '米尔西街道方向',                       # 21
    )

    DeclEntryPoint(
        Unknown_00              = 24100,
        Unknown_04              = 0,
        Unknown_08              = 56000,
        Unknown_0C              = 4,
        Unknown_0E              = 180,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 13,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 24100,
        Unknown_04              = 0,
        Unknown_08              = 56000,
        Unknown_0C              = 4,
        Unknown_0E              = 180,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 13,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02480 ._CH',             # 00
        'ED6_DT07/CH01060 ._CH',             # 01
        'ED6_DT07/CH01070 ._CH',             # 02
        'ED6_DT07/CH01020 ._CH',             # 03
        'ED6_DT07/CH01030 ._CH',             # 04
        'ED6_DT07/CH01710 ._CH',             # 05
        'ED6_DT07/CH01720 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH02480P._CP',             # 00
        'ED6_DT07/CH01060P._CP',             # 01
        'ED6_DT07/CH01070P._CP',             # 02
        'ED6_DT07/CH01020P._CP',             # 03
        'ED6_DT07/CH01030P._CP',             # 04
        'ED6_DT07/CH01710P._CP',             # 05
        'ED6_DT07/CH01720P._CP',             # 06
    )

    DeclNpc(
        X                   = 40470,
        Z                   = 0,
        Y                   = 16320,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 21900,
        Z                   = 0,
        Y                   = 25300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 25100,
        Z                   = 0,
        Y                   = 23000,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 28100,
        Z                   = 0,
        Y                   = 24800,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 32800,
        Z                   = 200,
        Y                   = 40000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 39010,
        Z                   = 600,
        Y                   = 22850,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 48160,
        Z                   = 460,
        Y                   = 18800,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 0,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 38780,
        Z                   = 0,
        Y                   = 19310,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 51470,
        Z                   = 0,
        Y                   = 20950,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 51470,
        Z                   = 0,
        Y                   = 20950,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 23910,
        Z                   = 30,
        Y                   = 66820,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_2C6",          # 00, 0
        "Function_1_432",          # 01, 1
        "Function_2_445",          # 02, 2
        "Function_3_45B",          # 03, 3
        "Function_4_47F",          # 04, 4
        "Function_5_4E3",          # 05, 5
        "Function_6_507",          # 06, 6
        "Function_7_54B",          # 07, 7
        "Function_8_698",          # 08, 8
        "Function_9_69E",          # 09, 9
        "Function_10_729",         # 0A, 10
        "Function_11_74F",         # 0B, 11
        "Function_12_F1A",         # 0C, 12
        "Function_13_1401",        # 0D, 13
        "Function_14_188D",        # 0E, 14
        "Function_15_1CE8",        # 0F, 15
        "Function_16_1E5D",        # 10, 16
        "Function_17_2063",        # 11, 17
        "Function_18_2073",        # 12, 18
        "Function_19_235C",        # 13, 19
        "Function_20_2382",        # 14, 20
    )


    def Function_0_2C6(): pass

    label("Function_0_2C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_314")
    SetChrPos(0xB, 38770, -300, 38410, 90)
    SetChrPos(0x8, 29400, 0, 12700, 180)
    SetChrPos(0xC, 29740, -300, 39260, 90)
    SetChrPos(0xA, 36000, 0, 41000, 0)
    Jump("loc_390")

    label("loc_314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_354")
    SetChrPos(0xB, 35500, 100, 36000, 90)
    SetChrPos(0x8, 29400, 0, 12700, 180)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)
    Jump("loc_390")

    label("loc_354")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_37C")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)
    Jump("loc_390")

    label("loc_37C")

    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)

    label("loc_390")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (104, "loc_3A0"),
        (1, "loc_3F2"),
        (SWITCH_DEFAULT, "loc_431"),
    )


    label("loc_3A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EF")
    OP_A2(0x22D)
    SetMapFlags(0x400000)
    OP_6D(24000, 0, 51000, 0)
    OP_6C(36000, 0)
    OP_6B(3000, 0)
    SetChrPos(0x102, 23000, 0, 55000, 0)
    OP_8C(0x102, 180, 0)
    Event(0, 16)

    label("loc_3EF")

    Jump("loc_431")

    label("loc_3F2")

    ClearMapFlags(0x1)
    OP_6D(17500, 0, 22800, 0)
    SetChrPos(0x102, 17000, 600, 23600, 90)
    SetChrPos(0x101, 17500, 600, 22800, 90)
    Event(0, 18)
    Jump("loc_431")

    label("loc_431")

    Return()

    # Function_0_2C6 end

    def Function_1_432(): pass

    label("Function_1_432")

    OP_16(0x2, 0xFA0, 0xFFFE8900, 0xFFFE8900, 0x30004)
    Return()

    # Function_1_432 end

    def Function_2_445(): pass

    label("Function_2_445")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_45A")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_445")

    label("loc_45A")

    Return()

    # Function_2_445 end

    def Function_3_45B(): pass

    label("Function_3_45B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_47E")
    OP_8D(0xFE, 19800, 21600, 24000, 30300, 3000)
    Jump("Function_3_45B")

    label("loc_47E")

    Return()

    # Function_3_45B end

    def Function_4_47F(): pass

    label("Function_4_47F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_4BF")

    label("loc_486")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4BC")
    OP_92(0xFE, 0xC, 0x3E8, 0xBB8, 0x0)
    Sleep(1000)
    OP_8D(0xFE, 36200, 39800, 32400, 43600, 3000)
    Jump("loc_486")

    label("loc_4BC")

    Jump("loc_4E2")

    label("loc_4BF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4E2")
    OP_8D(0xFE, 19800, 21600, 28200, 24800, 3000)
    Jump("loc_4BF")

    label("loc_4E2")

    Return()

    # Function_4_47F end

    def Function_5_4E3(): pass

    label("Function_5_4E3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_506")
    OP_8D(0xFE, 28150, 34670, 34240, 44760, 3000)
    Jump("Function_5_4E3")

    label("loc_506")

    Return()

    # Function_5_4E3 end

    def Function_6_507(): pass

    label("Function_6_507")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_527")

    label("loc_50F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_524")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_50F")

    label("loc_524")

    Jump("loc_54A")

    label("loc_527")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_54A")
    OP_8D(0xFE, 37390, 35010, 40920, 43630, 3000)
    Jump("loc_527")

    label("loc_54A")

    Return()

    # Function_6_507 end

    def Function_7_54B(): pass

    label("Function_7_54B")

    SetChrFlags(0xFE, 0x40)
    OP_8D(0xFE, 28710, 33610, 41830, 44000, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_574")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_697")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_65C")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x7026), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_PUSH_LONG, 0x834A), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0xA366), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0xABE0), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_631")
    SetChrFlags(0xFE, 0x20)
    TurnDirection(0xFE, 0x0, 0)
    ClearChrFlags(0xFE, 0x20)

    def lambda_61E():
        OP_94(0x0, 0xFE, 0xB4, 0x12C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_61E)
    Jump("loc_654")

    label("loc_631")


    def lambda_637():
        OP_8D(0xFE, 28710, 33610, 41830, 44000, 6000)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_637)
    Sleep(200)

    label("loc_654")

    Sleep(30)
    Jump("loc_694")

    label("loc_65C")

    Sleep(50)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_694")
    OP_44(0xFE, 0x2)

    def lambda_67C():
        OP_8D(0xFE, 28710, 33610, 41830, 44000, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_67C)

    label("loc_694")

    Jump("loc_574")

    label("loc_697")

    Return()

    # Function_7_54B end

    def Function_8_698(): pass

    label("Function_8_698")

    OP_22(0x190, 0x0, 0x64)
    Return()

    # Function_8_698 end

    def Function_9_69E(): pass

    label("Function_9_69E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_728")
    OP_43(0xFE, 0x2, 0x0, 0xA)
    OP_22(0x191, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_728")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x38B, 1)"), scpexpr(EXPR_END)), "loc_728")
    TalkBegin(0xFE)
    OP_A2(0x6)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "新鲜鸡蛋\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFE)

    label("loc_728")

    Return()

    # Function_9_69E end

    def Function_10_729(): pass

    label("Function_10_729")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_744")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_10_729")

    label("loc_744")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_10_729 end

    def Function_11_74F(): pass

    label("Function_11_74F")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_923")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C4")
    OP_A2(0x2B7)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "这不是艾丝蒂尔和约修亚嘛。\x01",
            "你们为什么会背着旅行包啊？ \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F嗯～是这样的，\x01",
            "我们要去柏斯那里办些事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "柏斯吗……\x01",
            "我听说定期船已经停航了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难道说你们\x01",
            "打算走路过去吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F就是这样。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F没事没事。\x01",
            "我听说走路去柏斯又不是很远。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔，就算有事非去不可，\x01",
            "这段路对于游击士来说也不轻松呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你们路上要小心哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_920")

    label("loc_8C4")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "唔，就算有事非去不可，\x01",
            "这段路对于游击士来说也不轻松呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你们路上要小心哦。\x02",
    )

    CloseMessageWindow()

    label("loc_920")

    Jump("loc_F14")

    label("loc_923")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_A36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C8")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "哎，是你们俩啊。\x01",
            "最近怎么样啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对了，我想找天搞个聚会，\x01",
            "把以前在主日学校读书的同学都叫到这里来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我也好久没有见过伊莉莎她了呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A33")

    label("loc_9C8")


    ChrTalk(
        0xFE,
        (
            "对了，我想找天搞个聚会，\x01",
            "把以前在主日学校读书的同学都叫到这里来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我也好久没有见过伊莉莎她了呢。\x02",
    )

    CloseMessageWindow()

    label("loc_A33")

    Jump("loc_F14")

    label("loc_A36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_B35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B00")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "艾丝蒂尔、约修亚，\x01",
            "之前真是多谢你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "从那之后我家\x01",
            "可是安静了很多哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可以恢复供应蔬菜，\x01",
            "大家又再度忙碌起来了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "查儿和维鲁\x01",
            "大概还不能这么早\x01",
            "帮家里干活吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B32")

    label("loc_B00")


    ChrTalk(
        0xFE,
        (
            "查儿和维鲁\x01",
            "大概还不能这么早\x01",
            "帮家里干活吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B32")

    Jump("loc_F14")

    label("loc_B35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_C19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC6")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "艾丝蒂尔、约修亚，\x01",
            "真是谢谢你们了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "下次完成工作之后\x01",
            "记得一定来玩啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "查儿和维鲁\x01",
            "一直吵着要你们\x01",
            "下次再来玩。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C16")

    label("loc_BC6")


    ChrTalk(
        0xFE,
        (
            "艾丝蒂尔、约修亚，\x01",
            "真是谢谢你们了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "下次完成工作之后\x01",
            "记得一定来玩啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C16")

    Jump("loc_F14")

    label("loc_C19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EDB")
    EventBegin(0x0)
    OP_A2(0x22E)
    OP_28(0x2, 0x1, 0x4)
    ClearMapFlags(0x1)
    OP_51(0x13, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x13, 0x3E8)

    ChrTalk(
        0x101,
        "#001F呀嗬～缇欧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F嗨，好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "艾丝蒂尔？\x01",
            "还有约修亚……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你们是来找我玩的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F不是啦，我们是来执行任务的。\x02\x03",
            "#000F这里不是有魔兽出现吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "两人向缇欧说明了\x01",
            "代替卡西乌斯执行任务的原因。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0xFE,
        (
            "研修结束了啊……\x01",
            "恭喜你们了，真不错啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯，如果是你们的话，\x01",
            "说不定有办法对付它们……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F真的有魔兽出现吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嗯，这几天一直在捣乱。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "拜它们所赐，\x01",
            "害得我睡眠不足……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F也就是说……\x01",
            "那些魔兽是在夜晚出没的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "说得没错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对了，\x01",
            "你们还是去向我爸妈询问详细的情况吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他们刚才出去送货，\x01",
            "我想这个时候应该已经回来了……\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_F14")

    label("loc_EDB")


    ChrTalk(
        0xFE,
        (
            "我爸妈他们\x01",
            "刚才出去送货。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我想差不多该回来了。\x02",
    )

    CloseMessageWindow()

    label("loc_F14")

    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    # Function_11_74F end

    def Function_12_F1A(): pass

    label("Function_12_F1A")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_FE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F99")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "连查儿姐姐也\x01",
            "开始帮农场干活了，\x01",
            "我自己一个人玩也觉得有点闷了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我也想帮忙呢……\x01",
            "帮农场干活。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FDD")

    label("loc_F99")


    ChrTalk(
        0xFE,
        (
            "连查儿姐姐也\x01",
            "开始帮农场干活了，\x01",
            "我自己一个人玩也觉得有点闷了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FDD")

    Jump("loc_13FD")

    label("loc_FE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_10B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_106D")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "啊，约修亚和艾丝蒂尔！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我说，你们已经成为\x01",
            "守护正义的游击士了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "厉害啊，好酷哦……\x01",
            "我也可以做游击士吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10B0")

    label("loc_106D")


    ChrTalk(
        0xFE,
        (
            "你们已经成为\x01",
            "守护正义的游击士了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我也可以做游击士吗。\x02",
    )

    CloseMessageWindow()

    label("loc_10B0")

    Jump("loc_13FD")

    label("loc_10B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1183")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_114F")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "啊啊，要是我也有\x01",
            "像约修亚那样的哥哥就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "缇欧姐姐因为要帮忙做事，\x01",
            "所以经常不能陪我玩……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "查儿姐姐也\x01",
            "只会玩过家家……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1180")

    label("loc_114F")


    ChrTalk(
        0xFE,
        (
            "啊啊，要是我也有\x01",
            "像约修亚那样的哥哥就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1180")

    Jump("loc_13FD")

    label("loc_1183")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_11BE")
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        "约修亚哥哥，再来玩呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "一定呀。\x02",
    )

    CloseMessageWindow()
    Jump("loc_13FD")

    label("loc_11BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_13FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12B3")
    OP_A2(0x283)
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        "啊，是约修亚哥哥！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "太好了！\x01",
            "一起来玩吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F啊，对不起。\x01",
            "今天我是来工作的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "工作？\x01",
            "我一个人玩很无聊的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#011F呵呵，有时间再一起玩吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F约修亚还是那么\x01",
            "受这里的孩子们欢迎啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12ED")

    label("loc_12B3")

    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "约修亚哥哥，\x01",
            "有空就要陪我玩呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "一定呀。\x02",
    )

    CloseMessageWindow()

    label("loc_12ED")

    Jump("loc_13FD")

    label("loc_12F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 3)), scpexpr(EXPR_END)), "loc_1320")
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "约修亚哥哥～\x01",
            "赶快来玩吧～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13FD")

    label("loc_1320")

    OP_A2(0x283)
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        "啊，是约修亚哥哥！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "太好了！\x01",
            "一起来玩吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F啊，对不起。\x01",
            "今天我是来工作的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "工作？\x01",
            "我一个人玩很无聊的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#011F呵呵，有时间再一起玩吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F约修亚还是那么\x01",
            "受这里的孩子们欢迎啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13FD")

    TalkEnd(0x9)
    Return()

    # Function_12_F1A end

    def Function_13_1401(): pass

    label("Function_13_1401")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_1589")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1541")
    OP_A2(0x2B6)
    TurnDirection(0xA, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "啊，约修亚……\x01",
            "你要到哪儿去啊？ \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯，有点事情要办，\x01",
            "打算去柏斯地区那里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "很快就回来吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F唔……\x01",
            "我想恐怕不太可能……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那个那个……\x01",
            "查儿会等你回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "所以呢，\x01",
            "你回来之后要来这里和我玩哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F嗯，说定了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嘿嘿，太好了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1586")

    label("loc_1541")


    ChrTalk(
        0xFE,
        (
            "那个那个……\x01",
            "查儿会等你回来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "所以呢，你要再来这里玩哦。\x02",
    )

    CloseMessageWindow()

    label("loc_1586")

    Jump("loc_1889")

    label("loc_1589")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1685")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_165F")
    OP_A2(0x3)
    TurnDirection(0xA, 0x102, 400)

    ChrTalk(
        0xFE,
        "那、那个，约修亚。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以后查儿也会\x01",
            "帮农场干活的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F呵呵，这不是很好吗。\x02\x03",
            "加油哦。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "约修亚轻轻地抚摸了一下查儿的头。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0xFE,
        (
            "嗯！\x01",
            "呵呵，加油哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1682")

    label("loc_165F")


    ChrTalk(
        0xFE,
        (
            "以后查儿也会\x01",
            "帮农场干活的哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1682")

    Jump("loc_1889")

    label("loc_1685")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_1889")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_END)), "loc_1790")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 2)), scpexpr(EXPR_END)), "loc_16EE")
    TurnDirection(0xA, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "啊，约修亚……\x01",
            "那个，我爸爸妈妈已经回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "现在就在家里。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_178D")

    label("loc_16EE")

    OP_A2(0x282)

    ChrTalk(
        0xFE,
        (
            "啊……\x01",
            "艾丝蒂尔、约修亚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F呀嗬～查儿，\x01",
            "最近还好吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x102, 400)

    ChrTalk(
        0x102,
        (
            "#010F小查儿，\x01",
            "你爸爸妈妈回来了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊、嗯，回来了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "现在就在家里。\x02",
    )

    CloseMessageWindow()

    label("loc_178D")

    Jump("loc_1889")

    label("loc_1790")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 2)), scpexpr(EXPR_END)), "loc_17D8")

    ChrTalk(
        0xFE,
        (
            "哎呀，\x01",
            "现在爸爸妈妈都不在。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "姐姐的话，\x01",
            "倒是在那边。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1889")

    label("loc_17D8")

    OP_A2(0x282)

    ChrTalk(
        0xFE,
        (
            "啊……\x01",
            "艾丝蒂尔、约修亚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F呀嗬～查儿，\x01",
            "最近还好吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F小查儿，\x01",
            "你爸爸妈妈在哪儿？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "哎呀，\x01",
            "现在爸爸妈妈都不在。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "姐姐的话，\x01",
            "倒是在那边。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1889")

    TalkEnd(0xA)
    Return()

    # Function_13_1401 end

    def Function_14_188D(): pass

    label("Function_14_188D")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_19B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1946")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "自从飞艇发明以来，\x01",
            "我们农场就不断接到\x01",
            "来自各个地方的采购单。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "我们也不能满足所有顾客的定购啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "有时候蔬菜供不应求，\x01",
            "真不知该高兴还是烦恼。 \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19B5")

    label("loc_1946")


    ChrTalk(
        0xFE,
        (
            "自从飞艇发明以来，\x01",
            "我们农场就不断接到\x01",
            "来自各个地方的采购单。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "我们也不能满足所有顾客的定购啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19B5")

    Jump("loc_1CE4")

    label("loc_19B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1AD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A73")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        "哦哦，你们两个啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我到城镇的时候\x01",
            "听到了你们的传闻呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在你们可是\x01",
            "赫赫有名的游击士啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们为我们\x01",
            "保卫农田的这件事\x01",
            "已经成为我引以为豪的话题了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AD2")

    label("loc_1A73")


    ChrTalk(
        0xFE,
        (
            "我到城镇的时候\x01",
            "现在你们可是\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们为我们\x01",
            "保卫农田的这件事\x01",
            "已经成为我引以为豪的话题了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AD2")

    Jump("loc_1CE4")

    label("loc_1AD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1C10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B9E")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        "哦哦，你们两个啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "自从你们来了之后，\x01",
            "那些魔兽再也没有来捣乱了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "蔬菜也像往常那样\x01",
            "可以对外供应了。\x01",
            "一家人总算安心下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "全靠你们的功劳啊。\x01",
            "真的十分感谢你们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C0D")

    label("loc_1B9E")


    ChrTalk(
        0xFE,
        (
            "全靠你们的功劳，\x01",
            "那些魔兽再也没有来捣乱了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "蔬菜也像往常那样\x01",
            "可以对外供应了。\x01",
            "一家人总算安心下来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C0D")

    Jump("loc_1CE4")

    label("loc_1C10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_1CE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C95")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "这次你们真是帮了大忙。\x01",
            "这下就能恢复蔬菜的输出了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "有很多人等着\x01",
            "我们农场的蔬菜呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "必须加把劲了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CE4")

    label("loc_1C95")


    ChrTalk(
        0xFE,
        (
            "这次你们真是帮了大忙，\x01",
            "这下就能恢复蔬菜的输出了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真的十分感谢你们。\x02",
    )

    CloseMessageWindow()

    label("loc_1CE4")

    TalkEnd(0xB)
    Return()

    # Function_14_188D end

    def Function_15_1CE8(): pass

    label("Function_15_1CE8")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_1DE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D8E")
    TurnDirection(0xFE, 0x101, 0)
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "这不是艾丝蒂尔和约修亚嘛。\x01",
            "是来这里办事的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "游击士这份工作\x01",
            "也不是那么轻松的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "千万不要蛮干，\x01",
            "要循序渐进慢慢努力哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DE2")

    label("loc_1D8E")


    ChrTalk(
        0xFE,
        (
            "游击士这份工作\x01",
            "也不是那么轻松的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "千万不要蛮干，\x01",
            "要循序渐进慢慢努力哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DE2")

    Jump("loc_1E59")

    label("loc_1DE5")


    ChrTalk(
        0xFE,
        (
            "哟，艾丝蒂尔、约修亚。\x01",
            "最近你们两个还不错吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果有时间的话，再过来这里玩哦。\x01",
            "那些孩子们都很想见你们呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E59")

    TalkEnd(0xC)
    Return()

    # Function_15_1CE8 end

    def Function_16_1E5D(): pass

    label("Function_16_1E5D")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    SetChrPos(0x101, 23380, 0, 61450, 0)
    SetChrPos(0x102, 24610, 0, 61450, 0)
    OP_6D(44190, 0, 16580, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3830, 0)
    OP_6C(269000, 0)
    OP_6E(261, 0)
    FadeToBright(2000, 0)

    def lambda_1ED2():
        OP_6C(0, 12000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1ED2)
    OP_6D(22290, 0, 23280, 6000)

    def lambda_1EF3():
        OP_6D(24020, 0, 51850, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1EF3)
    Sleep(3000)

    def lambda_1F10():
        OP_8E(0xFE, 0x5CF8, 0x3C, 0xC62A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1F10)
    Sleep(500)

    def lambda_1F30():
        OP_8E(0xFE, 0x60B8, 0xA0, 0xC8D2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1F30)
    Sleep(3600)
    Fade(1000)
    OP_6D(24140, 30, 50930, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#501F哈啊～\x01",
            "每次来这里都感到这么悠闲宁静。\x02\x03",
            "#501F有魔兽来捣乱这种事，\x01",
            "还真是让人不敢相信呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F现在确实感觉不到魔兽的气息……\x01",
            "　\x02\x03",
            "#010F总之先了解一下情况吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F缇欧会在哪里呢？\x02",
    )

    CloseMessageWindow()
    OP_44(0x0, 0xFF)
    EventEnd(0x0)
    ClearMapFlags(0x400000)
    Return()

    # Function_16_1E5D end

    def Function_17_2063(): pass

    label("Function_17_2063")

    OP_A6(0x0)
    OP_6B(4370, 6000)
    OP_A3(0x0)
    Return()

    # Function_17_2063 end

    def Function_18_2073(): pass

    label("Function_18_2073")

    EventBegin(0x0)
    SetMapFlags(0x400000)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8)
    SetChrPos(0xB, 23950, 20, 50260, 0)
    SetChrPos(0xC, 25400, 310, 50280, 0)
    SetChrPos(0x8, 23110, 280, 51210, 45)
    SetChrPos(0x9, 24740, 150, 51220, 0)
    SetChrPos(0xA, 25710, 360, 51250, 0)
    SetChrPos(0x101, 23600, 130, 52840, 180)
    SetChrPos(0x102, 24780, 160, 53490, 180)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_6D(23970, 130, 51650, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToDark(0, 0, -1)
    OP_20(0x0)
    OP_22(0xD, 0x0, 0x64)
    Sleep(5000)
    OP_1E()
    FadeToBright(2000, 0)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "谢谢啊。\x01",
            "这次你们真是帮了大忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "不过最后却害你们没能完成任务。\x01",
            "实在是有点过意不去……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F请不要介意。\x01",
            "我们从这次任务中学到了很多东西。\x02\x03",
            "#010F如果以后再有需要帮助的地方，\x01",
            "尽管联络游击士协会就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "一定会的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "艾丝蒂尔、约修亚。\x01",
            "记得有空多来玩啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "工作不忙的话要经常来这里住哦。\x01",
            "到时候煮些更好吃的菜给你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F谢谢啦，缇欧，还有阿姨。 \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F我们一定会再来拜访的。\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT01/R0201   ._SN", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_18_2073 end

    def Function_19_235C(): pass

    label("Function_19_235C")

    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0x5D52, 0x0, 0xF28A, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x8)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_19_235C end

    def Function_20_2382(): pass

    label("Function_20_2382")

    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0x5D52, 0x0, 0xF28A, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x8)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_20_2382 end

    SaveToFile()

Try(main)
