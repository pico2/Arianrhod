from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4137   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4137.x',
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
        '奥利维尔',                             # 9
        '奈尔',                                 # 10
        '朵洛希',                               # 11
        '总编',                                 # 12
        '库拉茨',                               # 13
        '克鲁茨',                               # 14
        '科蕾蒂',                               # 15
        '彭萨',                                 # 16
        '金',                                   # 17
        '奥利维尔',                             # 18
        '米亚尔',                               # 19
        '戈万',                                 # 20
        '帕菲',                                 # 21
        '娜娜',                                 # 22
        '巴拉尔',                               # 23
        '科尼嘉',                               # 24
        '诺蒂亚',                               # 25
        '法尔茨',                               # 26
        '莎莉亚',                               # 27
        '士兵丹',                               # 28
        '士兵阿尔兹',                           # 29
        '阿加特',                               # 30
        '提妲',                                 # 31
        '拉赛尔',                               # 32
        '\u3000',                               # 33
        '\u3000',                               # 34
        '\u3000',                               # 35
        '\u3000',                               # 36
        '\u3000',                               # 37
        '\u3000',                               # 38
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
        'ED6_DT07/CH00030 ._CH',             # 00
        'ED6_DT07/CH02060 ._CH',             # 01
        'ED6_DT07/CH02070 ._CH',             # 02
        'ED6_DT07/CH01120 ._CH',             # 03
        'ED6_DT07/CH01260 ._CH',             # 04
        'ED6_DT07/CH01620 ._CH',             # 05
        'ED6_DT07/CH01150 ._CH',             # 06
        'ED6_DT07/CH01140 ._CH',             # 07
        'ED6_DT07/CH00070 ._CH',             # 08
        'ED6_DT06/CH20050 ._CH',             # 09
        'ED6_DT07/CH01040 ._CH',             # 0A
        'ED6_DT07/CH01120 ._CH',             # 0B
        'ED6_DT07/CH02480 ._CH',             # 0C
        'ED6_DT07/CH02490 ._CH',             # 0D
        'ED6_DT07/CH01100 ._CH',             # 0E
        'ED6_DT07/CH01140 ._CH',             # 0F
        'ED6_DT07/CH01050 ._CH',             # 10
        'ED6_DT07/CH01140 ._CH',             # 11
        'ED6_DT07/CH01540 ._CH',             # 12
        'ED6_DT07/CH01300 ._CH',             # 13
        'ED6_DT07/CH00050 ._CH',             # 14
        'ED6_DT07/CH00060 ._CH',             # 15
        'ED6_DT07/CH02020 ._CH',             # 16
        'ED6_DT07/CH00003 ._CH',             # 17
        'ED6_DT07/CH00013 ._CH',             # 18
        'ED6_DT06/CH20086 ._CH',             # 19
        'ED6_DT06/CH20020 ._CH',             # 1A
    )

    AddCharChipPat(
        'ED6_DT07/CH00030P._CP',             # 00
        'ED6_DT07/CH02060P._CP',             # 01
        'ED6_DT07/CH02070P._CP',             # 02
        'ED6_DT07/CH01120P._CP',             # 03
        'ED6_DT07/CH01260P._CP',             # 04
        'ED6_DT07/CH01620P._CP',             # 05
        'ED6_DT07/CH01150P._CP',             # 06
        'ED6_DT07/CH01140P._CP',             # 07
        'ED6_DT07/CH00070P._CP',             # 08
        'ED6_DT06/CH20050P._CP',             # 09
        'ED6_DT07/CH01040P._CP',             # 0A
        'ED6_DT07/CH01120P._CP',             # 0B
        'ED6_DT07/CH02480P._CP',             # 0C
        'ED6_DT07/CH02490P._CP',             # 0D
        'ED6_DT07/CH01100P._CP',             # 0E
        'ED6_DT07/CH01140P._CP',             # 0F
        'ED6_DT07/CH01050P._CP',             # 10
        'ED6_DT07/CH01140P._CP',             # 11
        'ED6_DT07/CH01540P._CP',             # 12
        'ED6_DT07/CH01300P._CP',             # 13
        'ED6_DT07/CH00050P._CP',             # 14
        'ED6_DT07/CH00060P._CP',             # 15
        'ED6_DT07/CH02020P._CP',             # 16
        'ED6_DT07/CH00003P._CP',             # 17
        'ED6_DT07/CH00013P._CP',             # 18
        'ED6_DT06/CH20086P._CP',             # 19
        'ED6_DT06/CH20020P._CP',             # 1A
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -54180,
        Z                   = 0,
        Y                   = 61080,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x111,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 5200,
        Z                   = 4000,
        Y                   = 2130,
        Direction           = 182,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = 4560,
        Z                   = 0,
        Y                   = 2500,
        Direction           = 186,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = 4460,
        Z                   = 0,
        Y                   = -3910,
        Direction           = 94,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x111,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1D6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = -3600,
        Z                   = 0,
        Y                   = -2029,
        Direction           = 174,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = -3520,
        Z                   = 0,
        Y                   = -4540,
        Direction           = 6,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 58680,
        Z                   = 0,
        Y                   = -3720,
        Direction           = 188,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 59970,
        Z                   = 0,
        Y                   = -4990,
        Direction           = 263,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 61020,
        Z                   = 0,
        Y                   = 2490,
        Direction           = 197,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 61340,
        Z                   = 0,
        Y                   = 550,
        Direction           = 347,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -57020,
        Z                   = 0,
        Y                   = 61110,
        Direction           = 327,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -59180,
        Z                   = 0,
        Y                   = 59600,
        Direction           = 5,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x111,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -56630,
        Z                   = 0,
        Y                   = 5500,
        Direction           = 174,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -3620,
        Z                   = 0,
        Y                   = -2020,
        Direction           = 171,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -3550,
        Z                   = 0,
        Y                   = -4570,
        Direction           = 9,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65562,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65562,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65562,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1572890,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1572890,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1572890,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_542",          # 00, 0
        "Function_1_8AD",          # 01, 1
        "Function_2_8BE",          # 02, 2
        "Function_3_8D4",          # 03, 3
        "Function_4_8F8",          # 04, 4
        "Function_5_91C",          # 05, 5
        "Function_6_940",          # 06, 6
        "Function_7_9B1",          # 07, 7
        "Function_8_B7E",          # 08, 8
        "Function_9_CA6",          # 09, 9
        "Function_10_D16",         # 0A, 10
        "Function_11_DF1",         # 0B, 11
        "Function_12_12F0",        # 0C, 12
        "Function_13_1A81",        # 0D, 13
        "Function_14_217B",        # 0E, 14
        "Function_15_24B7",        # 0F, 15
        "Function_16_2690",        # 10, 16
        "Function_17_4147",        # 11, 17
        "Function_18_4637",        # 12, 18
        "Function_19_4D5E",        # 13, 19
        "Function_20_4E8C",        # 14, 20
        "Function_21_4F8E",        # 15, 21
        "Function_22_5048",        # 16, 22
        "Function_23_51A6",        # 17, 23
        "Function_24_5403",        # 18, 24
        "Function_25_57E2",        # 19, 25
        "Function_26_5FFF",        # 1A, 26
        "Function_27_660E",        # 1B, 27
        "Function_28_67C6",        # 1C, 28
        "Function_29_6FA9",        # 1D, 29
        "Function_30_7ADE",        # 1E, 30
        "Function_31_89AA",        # 1F, 31
        "Function_32_9C30",        # 20, 32
        "Function_33_B3AF",        # 21, 33
        "Function_34_C7E9",        # 22, 34
    )


    def Function_0_542(): pass

    label("Function_0_542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_550")
    OP_A3(0x3FA)
    Event(0, 29)

    label("loc_550")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_55E")
    OP_A3(0x3FB)
    Event(0, 30)

    label("loc_55E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_56C")
    OP_A3(0x3FC)
    Event(0, 31)

    label("loc_56C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 5)), scpexpr(EXPR_END)), "loc_57A")
    OP_A3(0x3FD)
    Event(0, 34)

    label("loc_57A")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (105, "loc_586"),
        (SWITCH_DEFAULT, "loc_5AF"),
    )


    label("loc_586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_599")
    OP_A2(0x627)
    Event(0, 32)

    label("loc_599")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5AC")
    OP_A2(0x64E)
    Event(0, 33)

    label("loc_5AC")

    Jump("loc_5AF")

    label("loc_5AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D1")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 4650, 0, 600, 0)

    label("loc_5D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_675")
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, 57670, 0, -5070, 111)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1F, 59920, 0, -5060, 275)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 5860, 4000, -4760, 350)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -3620, 0, -2160, 186)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, -3600, 0, -4420, 359)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 62780, 0, -3550, 162)
    OP_43(0xA, 0x0, 0x0, 0x3)
    Jump("loc_8AC")

    label("loc_675")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_6C8")
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -54200, 0, 63010, 194)
    OP_43(0xA, 0x0, 0x0, 0x2)
    SetChrPos(0x18, -53520, 0, 123230, 98)
    OP_43(0x18, 0x0, 0x0, 0x2)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    Jump("loc_8AC")

    label("loc_6C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_6F9")
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -54200, 0, 63010, 194)
    OP_43(0xA, 0x0, 0x0, 0x2)
    Jump("loc_8AC")

    label("loc_6F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_74F")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 5860, 4000, -4760, 350)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 62780, 0, -3550, 162)
    OP_43(0xA, 0x0, 0x0, 0x3)
    Jump("loc_8AC")

    label("loc_74F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_759")
    Jump("loc_8AC")

    label("loc_759")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_7C9")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -3620, 0, -2160, 186)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -3690, 0, -4720, 344)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0x18, -60680, 0, 122710, 160)
    OP_43(0x18, 0x0, 0x0, 0x5)
    SetChrPos(0x19, -54350, 0, 1120, 265)
    OP_43(0x19, 0x0, 0x0, 0x2)
    Jump("loc_8AC")

    label("loc_7C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_7D3")
    Jump("loc_8AC")

    label("loc_7D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_830")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -3620, 0, -2160, 186)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -3690, 0, -4720, 344)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0x18, -63230, 0, 59560, 338)
    OP_43(0x18, 0x0, 0x0, 0x2)
    SetChrFlags(0x19, 0x80)
    Jump("loc_8AC")

    label("loc_830")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_83A")
    Jump("loc_8AC")

    label("loc_83A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_872")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_END)), "loc_86F")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 910, 0, -3650, 189)
    SetChrPos(0xE, 610, 0, -3020, 146)

    label("loc_86F")

    Jump("loc_8AC")

    label("loc_872")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_8AC")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 5860, 4000, -4760, 350)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0x18, -63230, 0, 59560, 338)
    OP_43(0x18, 0x0, 0x0, 0x2)

    label("loc_8AC")

    Return()

    # Function_0_542 end

    def Function_1_8AD(): pass

    label("Function_1_8AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_8BD")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8BD")

    Return()

    # Function_1_8AD end

    def Function_2_8BE(): pass

    label("Function_2_8BE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8D3")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_8BE")

    label("loc_8D3")

    Return()

    # Function_2_8BE end

    def Function_3_8D4(): pass

    label("Function_3_8D4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8F7")
    OP_8D(0xFE, 61240, -1420, 64280, -5700, 3000)
    Jump("Function_3_8D4")

    label("loc_8F7")

    Return()

    # Function_3_8D4 end

    def Function_4_8F8(): pass

    label("Function_4_8F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_91B")
    OP_8D(0xFE, -57970, 64269, -56460, 57520, 3000)
    Jump("Function_4_8F8")

    label("loc_91B")

    Return()

    # Function_4_8F8 end

    def Function_5_91C(): pass

    label("Function_5_91C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_93F")
    OP_8D(0xFE, -62670, 124500, -59560, 120770, 3000)
    Jump("Function_5_91C")

    label("loc_93F")

    Return()

    # Function_5_91C end

    def Function_6_940(): pass

    label("Function_6_940")

    TalkBegin(0xFE)

    ChrTalk(
        0x10B,
        (
            "#100F呼～逃亡的生活\x01",
            "对于我这一把老骨头而言真是艰苦。\x02\x03",
            "多亏了你们，\x01",
            "又回到了从前那样\x01",
            "安安稳稳的生活。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_940 end

    def Function_7_9B1(): pass

    label("Function_7_9B1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_END)), "loc_A29")

    ChrTalk(
        0x1E,
        (
            "#060F终于实现\x01",
            "和爷爷一起\x01",
            "吃冰淇淋的愿望了。\x02\x03",
            "本来还想和阿加特大哥哥\x01",
            "一起来这里吃的，\x01",
            "结果他生气了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B7A")

    label("loc_A29")

    OP_A2(0x16)

    ChrTalk(
        0x1E,
        (
            "#060F啊……艾丝蒂尔姐姐和\x01",
            "约修亚哥哥！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F提妲，\x01",
            "你好像很开心嘛。 \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#060F嘿嘿，因为终于实现\x01",
            "和爷爷一起\x01",
            "吃冰淇淋的愿望了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊～真不错呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#060F嗯！\x02\x03",
            "本来还想和阿加特大哥哥\x01",
            "一起来这里吃的，\x01",
            "结果他生气了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F要阿加特吃冰淇淋……\x01",
            "哈哈，他会生气也是没办法的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#060F啊……\x01",
            "冰淇淋很好吃的嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B7A")

    TalkEnd(0xFE)
    Return()

    # Function_7_9B1 end

    def Function_8_B7E(): pass

    label("Function_8_B7E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_BC1")

    ChrTalk(
        0x106,
        (
            "#050F武术大会啊……\x02\x03",
            "的确是个\x01",
            "一试身手的好机会。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA2")

    label("loc_BC1")

    OP_A2(0x15)

    ChrTalk(
        0x106,
        (
            "#050F武术大会啊……\x02\x03",
            "的确是个\x01",
            "一试身手的好机会。\x02\x03",
            "而且那个『不动金』\x01",
            "这次也参加了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F明年阿加特\x01",
            "你也来参加如何呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#050F……哼，虽然是有兴趣，\x01",
            "但我可不想被别人看热闹。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F真是一点都不老实的说法～\x02",
    )

    CloseMessageWindow()

    label("loc_CA2")

    TalkEnd(0xFE)
    Return()

    # Function_8_B7E end

    def Function_9_CA6(): pass

    label("Function_9_CA6")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "由特务兵来镇守王都，\x01",
            "王都守卫队却撤离了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是难以理解，\x01",
            "而且根本不知道\x01",
            "是谁下达的这个命令啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_CA6 end

    def Function_10_D16(): pass

    label("Function_10_D16")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_D77")

    ChrTalk(
        0xFE,
        (
            "对于最近发生的事情，\x01",
            "我们也是一头雾水。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总之王都的正规军\x01",
            "基本上都撤离了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DED")

    label("loc_D77")

    OP_A2(0x14)

    ChrTalk(
        0xFE,
        (
            "对于发生的事情，\x01",
            "我们也是一头雾水。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总之王都的正规军\x01",
            "基本上都撤离了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "这么一来可如何是好啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DED")

    TalkEnd(0xFE)
    Return()

    # Function_10_D16 end

    def Function_11_DF1(): pass

    label("Function_11_DF1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_E5D")

    ChrTalk(
        0xFE,
        (
            "政变的发动人\x01",
            "竟然是那位理查德上校……\x01",
            "让我好震惊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "能防范于未然实在是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12EC")

    label("loc_E5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_EAE")

    ChrTalk(
        0xFE,
        "要发生什么事了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那些王都的守卫队士兵\x01",
            "都已经慌忙地撤离了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12EC")

    label("loc_EAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_F10")

    ChrTalk(
        0xFE,
        (
            "为了筹备庆典的取材，\x01",
            "大家都在忙着做准备……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但说实话，\x01",
            "庆典到底会怎么样啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12EC")

    label("loc_F10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_F7A")

    ChrTalk(
        0xFE,
        (
            "武术大会的优胜者\x01",
            "好像是朵洛希认识的人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "她呀，高兴过头了，\x01",
            "一边跳着舞一边跑回来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12EC")

    label("loc_F7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_105A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_FD9")

    ChrTalk(
        0xFE,
        (
            "一大早，\x01",
            "朵洛希就拿着照相机\x01",
            "跑到竞技场去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我看她好像充满干劲呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1057")

    label("loc_FD9")

    OP_A2(0x12)

    ChrTalk(
        0xFE,
        (
            "早上好。\x01",
            "今天是武术大会总决赛的日子呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一大早，\x01",
            "朵洛希就拿着照相机\x01",
            "跑到竞技场去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我看她好像充满干劲呢。\x02",
    )

    CloseMessageWindow()

    label("loc_1057")

    Jump("loc_12EC")

    label("loc_105A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_10B4")

    ChrTalk(
        0xFE,
        (
            "最近，\x01",
            "王国军的人每天都会过来检查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们通讯社\x01",
            "并没有做什么坏事对吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12EC")

    label("loc_10B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1190")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_110F")

    ChrTalk(
        0xFE,
        (
            "理查德上校\x01",
            "真是个很棒的男人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我也好像去\x01",
            "对他进行采访取材呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_118D")

    label("loc_110F")

    OP_A2(0x12)

    ChrTalk(
        0xFE,
        (
            "理查德上校\x01",
            "真是个很棒的男人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "举止文雅，知识渊博，\x01",
            "风度翩翩，一表人才……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我也好像去\x01",
            "对他进行采访取材呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_118D")

    Jump("loc_12EC")

    label("loc_1190")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1201")

    ChrTalk(
        0xFE,
        (
            "刚才奈尔记者\x01",
            "从外面回来了。\x01",
            "感觉有好一阵子没见到他了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他这个人啊，\x01",
            "经常会突然失踪好几天呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12EC")

    label("loc_1201")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_123F")

    ChrTalk(
        0xFE,
        (
            "本社的记者们\x01",
            "白天外出取材，\x01",
            "很少呆在通讯社里。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12EC")

    label("loc_123F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_12A6")

    ChrTalk(
        0xFE,
        (
            "下班之后约朵洛希\x01",
            "一起去外面玩的计划\x01",
            "又泡汤了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "别看她那个样子，\x01",
            "其实工作很忙的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12EC")

    label("loc_12A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_12EC")

    ChrTalk(
        0xFE,
        "欢迎来到利贝尔通讯社。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一楼是接待处，\x01",
            "二楼是编辑室。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12EC")

    TalkEnd(0xFE)
    Return()

    # Function_11_DF1 end

    def Function_12_12F0(): pass

    label("Function_12_12F0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1335")

    ChrTalk(
        0xFE,
        (
            "接下来就去\x01",
            "最近引起热门话题的\x01",
            "冰淇淋店进行取材吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A7D")

    label("loc_1335")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_13F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_1386")

    ChrTalk(
        0xFE,
        (
            "奈尔前辈他\x01",
            "被军队逮捕了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "幸亏我是\x01",
            "文化专栏的负责人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13EE")

    label("loc_1386")

    OP_A2(0x11)

    ChrTalk(
        0xFE,
        (
            "奈尔前辈他\x01",
            "被军队逮捕了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我就知道\x01",
            "他迟早会落到如此下场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "幸亏我是\x01",
            "文化专栏的负责人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13EE")

    Jump("loc_1A7D")

    label("loc_13F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_14E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_1462")

    ChrTalk(
        0xFE,
        (
            "本打算去到柏斯的\x01",
            "『安特洛丝餐厅』取材的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "怎么办啊……\x01",
            "只能写一篇别的报道来代替了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14E4")

    label("loc_1462")

    OP_A2(0x11)

    ChrTalk(
        0xFE,
        (
            "哇呀呀，\x01",
            "定期船停飞了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本打算去到柏斯的\x01",
            "『安特洛丝餐厅』取材的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "怎么办啊……\x01",
            "只能写一篇别的报道来代替了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14E4")

    Jump("loc_1A7D")

    label("loc_14E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_160C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_1563")

    ChrTalk(
        0xFE,
        (
            "取材的方式是\x01",
            "去美味的店品尝料理，\x01",
            "然后展示在文化专栏里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一定要做出可以向\x01",
            "奈尔前辈炫耀的东西来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1609")

    label("loc_1563")

    OP_A2(0x11)

    ChrTalk(
        0xFE,
        (
            "嘿嘿，\x01",
            "这次就以现在热门的餐厅\x01",
            "为主题作一期特辑吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "取材的方式是\x01",
            "去美味的店品尝料理，\x01",
            "然后展示在文化专栏里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一定要做出可以向\x01",
            "奈尔前辈炫耀的东西来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1609")

    Jump("loc_1A7D")

    label("loc_160C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_173F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_1685")

    ChrTalk(
        0xFE,
        (
            "朵洛希虽说是个新人，\x01",
            "不过实力确实非常强。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，让她进入我们通讯社的\x01",
            "总编的眼光更加令人佩服。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_173C")

    label("loc_1685")

    OP_A2(0x11)

    ChrTalk(
        0xFE,
        (
            "朵洛希虽说是个新人，\x01",
            "不过实力确实非常强。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不管是拍武术大会的照片，\x01",
            "还是料理的照片，\x01",
            "她总能选择最佳的角度去拍摄。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，让她进入我们通讯社的\x01",
            "总编的眼光更加令人佩服。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_173C")

    Jump("loc_1A7D")

    label("loc_173F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_182E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_179E")

    ChrTalk(
        0xFE,
        (
            "很多作家或者撰稿人\x01",
            "每逢截稿的时间临近\x01",
            "就会犯感冒。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是让人头疼……\x02",
    )

    CloseMessageWindow()
    Jump("loc_182B")

    label("loc_179E")

    OP_A2(0x11)

    ChrTalk(
        0xFE,
        (
            "很多作家或者撰稿人\x01",
            "每逢截稿的时间临近\x01",
            "就会犯感冒。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可能是太过拼命，\x01",
            "结果把身体弄坏了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "再或者就是装病，\x01",
            "总之很让人头疼。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_182B")

    Jump("loc_1A7D")

    label("loc_182E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1928")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_1893")

    ChrTalk(
        0xFE,
        (
            "唉唉，\x01",
            "我乘坐定期船去外地取原稿……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "结果到了之后\x01",
            "才被作者告知还没有写好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1925")

    label("loc_1893")

    OP_A2(0x11)

    ChrTalk(
        0xFE,
        (
            "唉唉，\x01",
            "我乘坐定期船去外地取原稿……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "结果到了之后\x01",
            "才被作者告知还没有写好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果导力通信能够更加普及的话，\x01",
            "联络起来就会方便了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1925")

    Jump("loc_1A7D")

    label("loc_1928")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1932")
    Jump("loc_1A7D")

    label("loc_1932")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_198C")

    ChrTalk(
        0xFE,
        (
            "今天我要乘坐定期船\x01",
            "去外地取原稿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要早点做好准备\x01",
            "才不至于延误乘船……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A7D")

    label("loc_198C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1A17")

    ChrTalk(
        0xFE,
        (
            "《利贝尔通讯》的文化专栏\x01",
            "是由我来担当编辑的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本专栏通常会刊登\x01",
            "连载小说和读者的意见，\x01",
            "也会对一些热门话题进行取材报道。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A7D")

    label("loc_1A17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1A7D")

    ChrTalk(
        0xFE,
        (
            "呼～\x01",
            "如果不能快点取回作者的原稿，\x01",
            "我会被责骂的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "奈尔和诺蒂亚\x01",
            "都要比总编严厉许多呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A7D")

    TalkEnd(0xFE)
    Return()

    # Function_12_12F0 end

    def Function_13_1A81(): pass

    label("Function_13_1A81")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1AB5")

    ChrTalk(
        0xFE,
        (
            "呵呵，\x01",
            "这次又麻烦奈尔帮我的忙了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2177")

    label("loc_1AB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1ADB")

    ChrTalk(
        0xFE,
        "街上的情况很奇怪呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2177")

    label("loc_1ADB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1B5E")

    ChrTalk(
        0xFE,
        (
            "奈尔从刚来杂志社的时候\x01",
            "就会做些让人目瞪口呆的事呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过大概正因为如此，\x01",
            "才能抢在别人之前\x01",
            "报道一些独家新闻吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2177")

    label("loc_1B5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1C5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_1BBB")

    ChrTalk(
        0xFE,
        (
            "那个狐狸眼睛的女上尉，\x01",
            "实在让人生气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不管走到哪里\x01",
            "都要挖苦别人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C57")

    label("loc_1BBB")

    OP_A2(0x10)

    ChrTalk(
        0xFE,
        (
            "理查德上校是很不错，\x01",
            "但情报部和特务兵\x01",
            "那些家伙就不敢恭维了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "特别是那个\x01",
            "长着狐狸眼睛的女上尉，\x01",
            "实在让人生气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不管走到哪里\x01",
            "都要挖苦别人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C57")

    Jump("loc_2177")

    label("loc_1C5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1CCE")

    ChrTalk(
        0xFE,
        (
            "呼呼，情报部的监视非常严，\x01",
            "取材也寸步难行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他们这样做，\x01",
            "和当年埃雷波尼亚帝国的宪兵有什么区别。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2177")

    label("loc_1CCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1DFB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_1D5B")

    ChrTalk(
        0xFE,
        (
            "我和奈尔常常都会\x01",
            "围绕着杂志报道方针的问题\x01",
            "与总编极力争辩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总编总能以\x01",
            "一副笑脸哄着我们，\x01",
            "我们很吃他的怀柔政策呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DF8")

    label("loc_1D5B")

    OP_A2(0x10)

    ChrTalk(
        0xFE,
        "总编是一个不可思议的人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我和奈尔常常都会\x01",
            "围绕着杂志报道方针的问题\x01",
            "与总编极力争辩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总编总能以\x01",
            "一副笑脸哄着我们，\x01",
            "我们很吃他的怀柔政策呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DF8")

    Jump("loc_2177")

    label("loc_1DFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1EDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_1E5C")

    ChrTalk(
        0xFE,
        (
            "直到今天早上\x01",
            "奈尔还在调查什么东西……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难道是发现了什么\x01",
            "好的新闻线索？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EDA")

    label("loc_1E5C")

    OP_A2(0x10)

    ChrTalk(
        0xFE,
        (
            "直到今天早上\x01",
            "奈尔还在调查什么东西……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难道是发现了什么\x01",
            "好的新闻线索？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔～作为前辈，\x01",
            "我也不能就这样输给他。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EDA")

    Jump("loc_2177")

    label("loc_1EDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1F57")

    ChrTalk(
        0xFE,
        (
            "呼～\x01",
            "大会今年改成了团体赛，\x01",
            "想拍摄好的确很困难啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可能的话，\x01",
            "真想找个好一点的摄影师\x01",
            "来替我拍摄啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2177")

    label("loc_1F57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2016")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_1FAB")

    ChrTalk(
        0xFE,
        (
            "利贝尔通讯正在准备\x01",
            "出版武术大会的特刊哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "要努力取材啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2013")

    label("loc_1FAB")

    OP_A2(0x10)

    ChrTalk(
        0xFE,
        "今天终于到大会的正式赛了呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "利贝尔通讯正在准备\x01",
            "出版武术大会的特刊哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "要努力取材啊。\x02",
    )

    CloseMessageWindow()

    label("loc_2013")

    Jump("loc_2177")

    label("loc_2016")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_210C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_2077")

    ChrTalk(
        0xFE,
        (
            "还是老样子，\x01",
            "奈尔又是一去不复返。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "刚回来没多久，\x01",
            "就立刻又飞奔出去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2109")

    label("loc_2077")

    OP_A2(0x10)

    ChrTalk(
        0xFE,
        (
            "还是老样子，\x01",
            "奈尔又是一去不复返。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "刚回来没多久，\x01",
            "就立刻又飞奔出去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他脸色不太健康是因为吸烟的缘故，\x01",
            "但体力至少是常人的一倍。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2109")

    Jump("loc_2177")

    label("loc_210C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2177")

    ChrTalk(
        0xFE,
        (
            "啊，真是的，\x01",
            "再不快点，预选赛就要开始了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯，器材带上了，\x01",
            "取材用的通行许可证也带上了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2177")

    TalkEnd(0xFE)
    Return()

    # Function_13_1A81 end

    def Function_14_217B(): pass

    label("Function_14_217B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2329")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_21EB")

    ChrTalk(
        0x110,
        (
            "#150F对了，奈尔前辈\x01",
            "告诉我了～\x02\x03",
            "因为这次的报道，\x01",
            "前辈和我很有可能会获得\x01",
            "菲利特尔奖哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2326")

    label("loc_21EB")

    OP_A2(0xF)

    ChrTalk(
        0x110,
        (
            "#150F啊，是小艾你们啊～！\x02\x03",
            "对了，奈尔前辈\x01",
            "告诉我了～\x02\x03",
            "因为这次的报道，\x01",
            "前辈和我很有可能会获得\x01",
            "菲利特尔奖哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F菲利特尔？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F在新闻、文学和音乐等领域\x01",
            "取得年度最佳成绩的人\x01",
            "被授予的奖项。\x02\x03",
            "对于记者而言\x01",
            "毫无疑问是最高荣誉呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊～真不错呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x110,
        (
            "#150F嘿嘿嘿，这也是\x01",
            "托小艾你们的福啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2326")

    Jump("loc_24B3")

    label("loc_2329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2364")

    ChrTalk(
        0x110,
        (
            "#150F呜～哇！\x01",
            "奈尔前辈还活着，\x01",
            "真是太好了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24B3")

    label("loc_2364")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_23A8")

    ChrTalk(
        0x110,
        (
            "#150F啊，拜托了～！\x01",
            "小艾～！\x02\x03",
            "一定要救救奈尔前辈～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24B3")

    label("loc_23A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2470")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_23F8")

    ChrTalk(
        0x110,
        (
            "#150F虽然总编让我\x01",
            "去找奈尔前辈～……\x01",
            "　\x02\x03",
            "但上哪去找呢～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_246D")

    label("loc_23F8")

    OP_A2(0xF)

    ChrTalk(
        0x110,
        (
            "#150F呀，是小艾你们啊～\x02\x03",
            "恭喜你们获得优胜～\x01",
            "比赛真是很精彩啊～\x02\x03",
            "我太兴奋了，\x01",
            "我拍了好多照片，\x01",
            "请你们期待哦～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_246D")

    Jump("loc_24B3")

    label("loc_2470")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_247A")
    Jump("loc_24B3")

    label("loc_247A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_2484")
    Jump("loc_24B3")

    label("loc_2484")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_248E")
    Jump("loc_24B3")

    label("loc_248E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2498")
    Jump("loc_24B3")

    label("loc_2498")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_24A2")
    Jump("loc_24B3")

    label("loc_24A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_24AC")
    Jump("loc_24B3")

    label("loc_24AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_24B3")

    label("loc_24B3")

    TalkEnd(0xFE)
    Return()

    # Function_14_217B end

    def Function_15_24B7(): pass

    label("Function_15_24B7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_262B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_2528")

    ChrTalk(
        0x10F,
        (
            "#140F对你们的采访\x01",
            "读者的反响尤为强烈呢。\x02\x03",
            "如果以后有什么有趣的消息，\x01",
            "还要靠你们提供了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2628")

    label("loc_2528")

    OP_A2(0xE)

    ChrTalk(
        0x10F,
        (
            "#140F哟，艾丝蒂尔、约修亚！\x01",
            "这次你们真是出尽风头了。\x02\x03",
            "多亏了你们，\x01",
            "这次与政变相关的特刊简直卖疯了。\x02\x03",
            "对了对了，你们的\x01",
            "读者的反响尤为强烈呢。\x02\x03",
            "不管怎么说你们也是\x01",
            "阻止了理查德上校\x01",
            "政变阴谋的小小英雄呢。\x02\x03",
            "如果以后有什么有趣的消息，\x01",
            "还要靠你们提供了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2628")

    Jump("loc_268C")

    label("loc_262B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2635")
    Jump("loc_268C")

    label("loc_2635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_263F")
    Jump("loc_268C")

    label("loc_263F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2649")
    Jump("loc_268C")

    label("loc_2649")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2653")
    Jump("loc_268C")

    label("loc_2653")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_265D")
    Jump("loc_268C")

    label("loc_265D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2667")
    Jump("loc_268C")

    label("loc_2667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2671")
    Jump("loc_268C")

    label("loc_2671")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_267B")
    Jump("loc_268C")

    label("loc_267B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2685")
    Jump("loc_268C")

    label("loc_2685")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_268C")

    label("loc_268C")

    TalkEnd(0xFE)
    Return()

    # Function_15_24B7 end

    def Function_16_2690(): pass

    label("Function_16_2690")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_27D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_2717")

    ChrTalk(
        0xFE,
        (
            "理查德上校的\x01",
            "政变报道特辑反响强烈。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "转瞬之间销量就已经赶上了\x01",
            "理查德上校介绍特辑\x01",
            "和戴尔蒙市长被捕特辑了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27D5")

    label("loc_2717")

    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "理查德上校的\x01",
            "政变报道特辑反响强烈。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "转瞬之间销量就已经赶上了\x01",
            "理查德上校介绍特辑\x01",
            "和戴尔蒙市长被捕特辑了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如此有冲击力的事件，\x01",
            "与报道有关的质问非常多，\x01",
            "回答起来也很麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27D5")

    Jump("loc_4143")

    label("loc_27D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_289C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_2838")

    ChrTalk(
        0xFE,
        (
            "刚才协会发联络过来，\x01",
            "说在艾贝尔离宫找到奈尔了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哎呀～太好了太好了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2899")

    label("loc_2838")

    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "刚才游击士协会\x01",
            "发了联络过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说在艾贝尔离宫\x01",
            "找到奈尔了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哎呀～太好了太好了。\x02",
    )

    CloseMessageWindow()

    label("loc_2899")

    Jump("loc_4143")

    label("loc_289C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_28C3")

    ChrTalk(
        0xFE,
        (
            "奈尔的事\x01",
            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4143")

    label("loc_28C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2BEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_2929")

    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "我正有事要找奈尔呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他跑到哪里去了。\x01",
            "说起来，\x01",
            "这几天都没有看到他。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BEC")

    label("loc_2929")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_2987")

    ChrTalk(
        0xFE,
        (
            "我正有事要找奈尔呢，\x01",
            "可这几天都没有看到他。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "算了，\x01",
            "这种事情早已经习惯了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BEC")

    label("loc_2987")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_END)), "loc_2A0C")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "我正有事要找奈尔呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他跑到哪里去了。\x01",
            "说起来，\x01",
            "这几天都没有看到他。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "算了，\x01",
            "这种事情早已经习惯了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BEC")

    label("loc_2A0C")

    OP_A2(0x67F)
    OP_A2(0xD)

    NpcTalk(
        0xFE,
        "中年男子",
        "哦，你们胸前的徽章是……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "中年男子",
        (
            "莫非是游击士协会的\x01",
            "艾丝蒂尔和约修亚吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎？您是怎么知道的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本人就是\x01",
            "《利贝尔通讯》的总编。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我从奈尔和朵洛希那里\x01",
            "听说过很多你们的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，原来是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F初次见面，请多关照。\x02\x03",
            "《利贝尔通讯》的每一期\x01",
            "都给我们带来了不少乐趣呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈哈哈。\x01",
            "听你这么说我很高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "对了，你们是来找奈尔的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我也正有事要找他呢，\x01",
            "可这几天都没有看到他。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "算了，\x01",
            "这种事情早已经习惯了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BEC")

    Jump("loc_4143")

    label("loc_2BEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2F00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_2C89")

    ChrTalk(
        0xFE,
        (
            "今天你们要进行\x01",
            "武术大会的决赛了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我的工作太忙，不能去竞技场了，\x01",
            "就在这里给你们加油吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "朵洛希她今天\x01",
            "也要去竞技场取材。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EFD")

    label("loc_2C89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_END)), "loc_2CEB")

    ChrTalk(
        0xFE,
        (
            "哟，今天是总决赛哦。\x01",
            "我会支持你们的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "朵洛希她今天也要去竞技场取材。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EFD")

    label("loc_2CEB")

    OP_A2(0x67F)
    OP_A2(0xD)

    NpcTalk(
        0xFE,
        "中年男子",
        "哦，你们胸前的徽章是……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "中年男子",
        (
            "莫非是游击士协会的\x01",
            "艾丝蒂尔和约修亚吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎？您是怎么知道的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本人就是\x01",
            "《利贝尔通讯》的总编。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我从奈尔和朵洛希那里\x01",
            "听说过很多你们的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，原来是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F初次见面，请多关照。\x02\x03",
            "《利贝尔通讯》的每一期\x01",
            "都给我们带来了不少乐趣呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈哈哈。\x01",
            "听你这么说我很高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说起来，今天你们\x01",
            "要进行武术大会的决赛了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我的工作太忙，不能去竞技场了，\x01",
            "就在这里给你们加油吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "朵洛希她今天\x01",
            "也要去竞技场取材。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，谢谢！\x02",
    )

    CloseMessageWindow()

    label("loc_2EFD")

    Jump("loc_4143")

    label("loc_2F00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_3241")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_2F3E")

    ChrTalk(
        0xFE,
        (
            "哈哈哈，\x01",
            "我们社的记者人人都很有个性呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_323E")

    label("loc_2F3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_2F9C")

    ChrTalk(
        0xFE,
        (
            "找奈尔吗？\x01",
            "他现在就在编辑室里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "编辑室在出版社的二层。\x01",
            "你们赶快去找他吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_323E")

    label("loc_2F9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_END)), "loc_302F")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "我们社的记者\x01",
            "人人都很有个性。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因此，\x01",
            "每到讨论问题的时候\x01",
            "场面简直就像在吵架一样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过许多优秀的文章\x01",
            "也是那样诞生的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_323E")

    label("loc_302F")

    OP_A2(0x67F)
    OP_A2(0xD)

    NpcTalk(
        0xFE,
        "中年男子",
        "哦，你们胸前的徽章是……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "中年男子",
        (
            "莫非是游击士协会的\x01",
            "艾丝蒂尔和约修亚吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎？您是怎么知道的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本人就是\x01",
            "《利贝尔通讯》的总编。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我从奈尔和朵洛希那里\x01",
            "听说过很多你们的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，原来是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F初次见面，请多关照。\x02\x03",
            "《利贝尔通讯》的每一期\x01",
            "都给我们带来了不少乐趣呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈哈哈。\x01",
            "听你这么说我很高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对了，\x01",
            "你们是来找奈尔的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，是啊。\x01",
            "今天我们和他约好了的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是这样啊，\x01",
            "他现在就在编辑室里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "编辑室在出版社的二层。\x01",
            "你们赶快去找他吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_323E")

    Jump("loc_4143")

    label("loc_3241")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_35A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_32AC")

    ChrTalk(
        0xFE,
        (
            "最近，军队的情报部\x01",
            "要求对我们的报道进行审查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "军队本来应该\x01",
            "没有这样的权利才对。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35A5")

    label("loc_32AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_32FC")

    ChrTalk(
        0xFE,
        (
            "奈尔他啊，\x01",
            "好像又外出取材了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我想短时间内\x01",
            "他应该回不来呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35A5")

    label("loc_32FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_END)), "loc_33B5")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "自从女王陛下生病以来，\x01",
            "情报部的家伙们就经常来制造麻烦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "竟然还蛮横无理地\x01",
            "要求对我们的报道进行审查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "利贝尔王国\x01",
            "保障国民的言论自由，\x01",
            "他们根本没有这样的权利。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35A5")

    label("loc_33B5")

    OP_A2(0x67F)
    OP_A2(0xD)

    NpcTalk(
        0xFE,
        "中年男子",
        "哦，你们胸前的徽章是……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "中年男子",
        (
            "莫非是游击士协会的\x01",
            "艾丝蒂尔和约修亚吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎？您是怎么知道的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本人就是\x01",
            "《利贝尔通讯》的总编。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我从奈尔和朵洛希那里\x01",
            "听说过很多你们的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，原来是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F初次见面，请多关照。\x02\x03",
            "《利贝尔通讯》的每一期\x01",
            "都给我们带来了不少乐趣呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈哈哈。\x01",
            "听你这么说我很高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对了，\x01",
            "你们是来找奈尔的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，其实不是的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看起来，\x01",
            "他好像又外出取材了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我想短时间内\x01",
            "他应该回不来呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35A5")

    Jump("loc_4143")

    label("loc_35A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3907")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_3622")

    ChrTalk(
        0xFE,
        (
            "我听记者们说了。\x01",
            "你们是参加武术大会的选手吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "奈尔知道以后，\x01",
            "说要去采访你们，\x01",
            "然后就跑出去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3904")

    label("loc_3622")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_3687")

    ChrTalk(
        0xFE,
        (
            "听说你们\x01",
            "是参加武术大会的选手。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "奈尔知道以后，\x01",
            "说要去采访你们，\x01",
            "然后就跑出去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3904")

    label("loc_3687")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_END)), "loc_3727")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        "哦，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我听记者们说了，\x01",
            "你们是参加武术大会的选手吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "奈尔知道以后\x01",
            "说要去采访你们，\x01",
            "然后就跑出去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你们没有遇见他吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3904")

    label("loc_3727")

    OP_A2(0x67F)
    OP_A2(0xD)

    NpcTalk(
        0xFE,
        "中年男子",
        "哦，你们胸前的徽章是……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "中年男子",
        (
            "莫非是游击士协会的\x01",
            "艾丝蒂尔和约修亚吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎？您是怎么知道的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本人就是\x01",
            "《利贝尔通讯》的总编。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我从奈尔和朵洛希那里\x01",
            "听说过很多你们的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，原来是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F初次见面，请多关照。\x02\x03",
            "《利贝尔通讯》的每一期\x01",
            "都给我们带来了不少乐趣呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈哈哈。\x01",
            "听你这么说我很高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "听说你们\x01",
            "是参加武术大会的选手。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "奈尔知道以后\x01",
            "说要去采访你们，\x01",
            "然后就跑出去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你们没有遇见他吗？\x02",
    )

    CloseMessageWindow()

    label("loc_3904")

    Jump("loc_4143")

    label("loc_3907")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_3C63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_397B")

    ChrTalk(
        0xFE,
        (
            "从今天开始\x01",
            "武术大会终于进入正式赛了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为要出特刊，\x01",
            "所以本社的记者们\x01",
            "一早就外出取材了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C60")

    label("loc_397B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_39CB")

    ChrTalk(
        0xFE,
        (
            "奈尔他啊，\x01",
            "好像又外出取材了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我想短时间内\x01",
            "他应该回不来呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C60")

    label("loc_39CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_END)), "loc_3A70")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "从今天开始\x01",
            "武术大会终于进入正式赛了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然不知道诞辰庆典会如何，\x01",
            "但肯定也会很热闹吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为要出特刊，\x01",
            "所以本社的记者们\x01",
            "一早就外出取材了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C60")

    label("loc_3A70")

    OP_A2(0x67F)
    OP_A2(0xD)

    NpcTalk(
        0xFE,
        "中年男子",
        "哦，你们胸前的徽章是……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "中年男子",
        (
            "莫非是游击士协会的\x01",
            "艾丝蒂尔和约修亚吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎？您是怎么知道的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本人就是\x01",
            "《利贝尔通讯》的总编。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我从奈尔和朵洛希那里\x01",
            "听说过很多你们的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，原来是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F初次见面，请多关照。\x02\x03",
            "《利贝尔通讯》的每一期\x01",
            "都给我们带来了不少乐趣呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈哈哈。\x01",
            "听你这么说我很高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对了，\x01",
            "你们是来找奈尔的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，其实不是的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看起来，\x01",
            "他好像又外出取材了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我想短时间内\x01",
            "他应该回不来呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C60")

    Jump("loc_4143")

    label("loc_3C63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_3EFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_3CBA")

    ChrTalk(
        0xFE,
        (
            "奈尔他啊，\x01",
            "好像又外出取材了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我想短时间内\x01",
            "他应该回不来呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EFC")

    label("loc_3CBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_END)), "loc_3D0C")

    ChrTalk(
        0xFE,
        (
            "虽然本刊刊登了\x01",
            "女王陛下身体欠佳的报道，\x01",
            "但这个消息确实缺乏可信度。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EFC")

    label("loc_3D0C")

    OP_A2(0x67F)
    OP_A2(0xD)

    NpcTalk(
        0xFE,
        "中年男子",
        "哦，你们胸前的徽章是……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "中年男子",
        (
            "莫非是游击士协会的\x01",
            "艾丝蒂尔和约修亚吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎？您是怎么知道的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本人就是\x01",
            "《利贝尔通讯》的总编。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我从奈尔和朵洛希那里\x01",
            "听说过很多你们的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，原来是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F初次见面，请多关照。\x02\x03",
            "《利贝尔通讯》的每一期\x01",
            "都给我们带来了不少乐趣呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈哈哈。\x01",
            "听你这么说我很高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对了，\x01",
            "你们是来找奈尔的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，其实不是的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看起来，\x01",
            "他好像又外出取材了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我想短时间内\x01",
            "他应该回不来呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EFC")

    Jump("loc_4143")

    label("loc_3EFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4143")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_3F56")

    ChrTalk(
        0xFE,
        (
            "奈尔他啊，\x01",
            "好像又外出取材了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我想短时间内\x01",
            "他应该回不来呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4143")

    label("loc_3F56")

    OP_A2(0xD)

    NpcTalk(
        0xFE,
        "中年男子",
        "哦，你们胸前的徽章是……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "中年男子",
        (
            "莫非是游击士协会的\x01",
            "艾丝蒂尔和约修亚吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎？您是怎么知道的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本人就是\x01",
            "《利贝尔通讯》的总编。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我从奈尔和朵洛希那里\x01",
            "听说过很多你们的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，原来是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F初次见面，请多关照。\x02\x03",
            "《利贝尔通讯》的每一期\x01",
            "都给我们带来了不少乐趣呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈哈哈。\x01",
            "听你这么说我很高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对了，\x01",
            "你们是来找奈尔的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，其实不是的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看起来，\x01",
            "他好像又外出取材了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我想短时间内\x01",
            "他应该回不来呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4143")

    TalkEnd(0xFE)
    Return()

    # Function_16_2690 end

    def Function_17_4147(): pass

    label("Function_17_4147")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_427A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_41D4")

    ChrTalk(
        0xFE,
        (
            "连游击士和亲卫队\x01",
            "攻入城内的场面都有，\x01",
            "这部分报道相当有魄力啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样一来《利贝尔通讯》的发行量\x01",
            "又要大幅上涨了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4277")

    label("loc_41D4")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "很久没有看到过\x01",
            "如此精彩的报道了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "连游击士和亲卫队\x01",
            "攻入城内的场面都有，\x01",
            "这部分报道相当有魄力啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样一来《利贝尔通讯》的发行量\x01",
            "又要大幅上涨了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4277")

    Jump("loc_4633")

    label("loc_427A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_42E9")

    ChrTalk(
        0xFE,
        (
            "这几天阅读了\x01",
            "很多书籍和新闻，\x01",
            "从中得到了不少启示。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在我们看不见的地方，\x01",
            "似乎正有暗流涌动。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4633")

    label("loc_42E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_4357")

    ChrTalk(
        0xFE,
        (
            "我觉得亲卫队的人们\x01",
            "虽然有些作风古板……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过那种高雅的气质和举止\x01",
            "看上去就让人心情很愉快。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4633")

    label("loc_4357")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_43C5")

    ChrTalk(
        0xFE,
        (
            "关于女王病情的详情，\x01",
            "现在也没有对外发表。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "陛下本人也没有作出声明，\x01",
            "我怀疑真的是生病了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4633")

    label("loc_43C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_4402")

    ChrTalk(
        0xFE,
        (
            "呼～对于我来说，\x01",
            "喝杯咖啡就能驱散早晨的困倦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4633")

    label("loc_4402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_4438")

    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "士兵为什么都那样\x01",
            "粗暴不知礼节呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4633")

    label("loc_4438")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4460")

    ChrTalk(
        0xFE,
        "呼，书籍是心灵的养料啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4633")

    label("loc_4460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_44CF")

    ChrTalk(
        0xFE,
        (
            "这里的老板以前\x01",
            "是外交使节的一员呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为工作关系，\x01",
            "他好像去过帝国、共和国\x01",
            "等等很多的国家。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4633")

    label("loc_44CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_450C")

    ChrTalk(
        0xFE,
        (
            "我是属于那种只要知道\x01",
            "比赛结果就满足了的类型。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4633")

    label("loc_450C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_45D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_4566")

    ChrTalk(
        0xFE,
        (
            "最近的《利贝尔通讯》\x01",
            "给人的感觉有些平淡。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "一点都不让人吃惊啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_45D3")

    label("loc_4566")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "最近《利贝尔通讯》\x01",
            "给人的感觉有些平淡。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "基本上都是\x01",
            "普普通通的新闻……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "一点都不让人吃惊啊。\x02",
    )

    CloseMessageWindow()

    label("loc_45D3")

    Jump("loc_4633")

    label("loc_45D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4633")

    ChrTalk(
        0xFE,
        "哎呀，这个地方很舒适嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在这里一边喝咖啡\x01",
            "一边看书的话，\x01",
            "时间很快就过去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4633")

    TalkEnd(0xFE)
    Return()

    # Function_17_4147 end

    def Function_18_4637(): pass

    label("Function_18_4637")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_46C2")

    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "没想到表面上是在召开武术大会，\x01",
            "暗地里却是在策划政变。 \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "话说回来，\x01",
            "像理查德上校这样的人\x01",
            "怎么还会感到不满足呢。 \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D5A")

    label("loc_46C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_47BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_472B")

    ChrTalk(
        0xFE,
        (
            "我感到军队的警戒\x01",
            "好像又提高了一个层次。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这件事事先也没有\x01",
            "向我们市民通知一声。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47B7")

    label("loc_472B")

    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "我感到军队的警戒\x01",
            "好像又提高了一个层次。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这件事事先也没有\x01",
            "向我们市民通知一声。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然没有发生什么事情，\x01",
            "但总是觉得有些不安。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47B7")

    Jump("loc_4D5A")

    label("loc_47BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_48B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_4823")

    ChrTalk(
        0xFE,
        (
            "刚才来的特务兵\x01",
            "嘴里嘟囔个不停……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对于搜捕亲卫队的事，\x01",
            "市民好像不是很配合呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48B1")

    label("loc_4823")

    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "刚才来的特务兵\x01",
            "嘴里嘟囔个不停……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对于搜捕亲卫队的事，\x01",
            "市民好像不是很配合呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呵呵，主要还是因为\x01",
            "亲卫队平时很受大家欢迎吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48B1")

    Jump("loc_4D5A")

    label("loc_48B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_491E")

    ChrTalk(
        0xFE,
        (
            "武术大会的优胜者\x01",
            "好像已经产生了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "王城里的利贝尔宫廷料理\x01",
            "可都是十分丰盛的，好羡慕呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D5A")

    label("loc_491E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_49B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_4964")

    ChrTalk(
        0xFE,
        (
            "各位客人要不要尝尝\x01",
            "本店引以为荣的『浓缩咖啡』？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49B4")

    label("loc_4964")

    OP_A2(0xA)

    ChrTalk(
        0xFE,
        "你们好，欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "各位客人要不要尝尝\x01",
            "本店引以为荣的『浓缩咖啡』？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49B4")

    Jump("loc_4D5A")

    label("loc_49B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_4AB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_4A2B")

    ChrTalk(
        0xFE,
        (
            "刚才来的士兵说什么\x01",
            "晚上９点以后严禁外出。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没办法，\x01",
            "还是早些关店门，\x01",
            "听听音乐休息一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AB0")

    label("loc_4A2B")

    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "刚才，\x01",
            "王国军的士兵们到店里来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他们说什么\x01",
            "晚上９点以后严禁外出。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没办法，\x01",
            "还是早些关店门，\x01",
            "听听音乐休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AB0")

    Jump("loc_4D5A")

    label("loc_4AB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4B45")

    ChrTalk(
        0xFE,
        (
            "这个西街区，\x01",
            "在王都格兰赛尔的街区当中\x01",
            "也算是相当安静的区域了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了要开这家店，\x01",
            "我曾经到处寻找地方，\x01",
            "最后发现还是这里最好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D5A")

    label("loc_4B45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4C4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_4BAA")

    ChrTalk(
        0xFE,
        (
            "哎呀，\x01",
            "我过去因为工作的关系\x01",
            "到过好多的国家呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "呵呵，饮食文化真是深奥啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C49")

    label("loc_4BAA")

    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "哎呀，\x01",
            "我过去因为工作的关系\x01",
            "到过好多的国家呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "当时可以说\x01",
            "吃遍了各国的美味。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这里卖的咖喱饭\x01",
            "就是其中一种哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "呵呵，饮食文化真是深奥啊。\x02",
    )

    CloseMessageWindow()

    label("loc_4C49")

    Jump("loc_4D5A")

    label("loc_4C4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_4CA6")

    ChrTalk(
        0xFE,
        "啊，你们请随便坐吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本店会让顾客\x01",
            "享受到宾至如归\x01",
            "而又舒适悠闲的感觉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D5A")

    label("loc_4CA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_4D20")

    ChrTalk(
        0xFE,
        (
            "旁边的建筑就是现在大受欢迎的\x01",
            "《利贝尔通讯》的出版社办公楼了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那里的记者和编辑\x01",
            "也常到这里来吃饭休息。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D5A")

    label("loc_4D20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4D5A")

    ChrTalk(
        0xFE,
        "你们，欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "欢迎来到\x01",
            "巴拉尔咖啡厅。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D5A")

    TalkEnd(0xFE)
    Return()

    # Function_18_4637 end

    def Function_19_4D5E(): pass

    label("Function_19_4D5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_4D68")
    Jump("loc_4E8B")

    label("loc_4D68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_4DBE")

    ChrTalk(
        0xFE,
        (
            "啊～\x01",
            "那么一会儿去吃冰淇淋如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我知道有一家店的\x01",
            "冰淇淋很好吃哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E8B")

    label("loc_4DBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_4DEA")

    ChrTalk(
        0xFE,
        "诞辰庆典之前都没什么事做呢～\x02",
    )

    CloseMessageWindow()
    Jump("loc_4E8B")

    label("loc_4DEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_4E48")

    ChrTalk(
        0xFE,
        (
            "嗯～\x01",
            "我觉得明年肯定会变回个人战。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样的话～\x01",
            "我只给约修亚君一个人加油哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E8B")

    label("loc_4E48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_4E52")
    Jump("loc_4E8B")

    label("loc_4E52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_4E5C")
    Jump("loc_4E8B")

    label("loc_4E5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4E66")
    Jump("loc_4E8B")

    label("loc_4E66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4E70")
    Jump("loc_4E8B")

    label("loc_4E70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_4E7A")
    Jump("loc_4E8B")

    label("loc_4E7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_4E84")
    Jump("loc_4E8B")

    label("loc_4E84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4E8B")

    label("loc_4E8B")

    Return()

    # Function_19_4D5E end

    def Function_20_4E8C(): pass

    label("Function_20_4E8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_4E96")
    Jump("loc_4F8D")

    label("loc_4E96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_4ECE")

    ChrTalk(
        0xFE,
        "超级不爽啊～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "现在要做些什么好呢～？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4F8D")

    label("loc_4ECE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_4F1D")

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "诞辰庆典真的会如期举办吗～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "女王陛下似乎病了啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4F8D")

    label("loc_4F1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_4F4A")

    ChrTalk(
        0xFE,
        (
            "啊啊～\x01",
            "洛伦斯大人竟然输掉了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F8D")

    label("loc_4F4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_4F54")
    Jump("loc_4F8D")

    label("loc_4F54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_4F5E")
    Jump("loc_4F8D")

    label("loc_4F5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4F68")
    Jump("loc_4F8D")

    label("loc_4F68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4F72")
    Jump("loc_4F8D")

    label("loc_4F72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_4F7C")
    Jump("loc_4F8D")

    label("loc_4F7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_4F86")
    Jump("loc_4F8D")

    label("loc_4F86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4F8D")

    label("loc_4F8D")

    Return()

    # Function_20_4E8C end

    def Function_21_4F8E(): pass

    label("Function_21_4F8E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_4F9B")
    Jump("loc_5044")

    label("loc_4F9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_4FA5")
    Jump("loc_5044")

    label("loc_4FA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_4FAF")
    Jump("loc_5044")

    label("loc_4FAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_5001")

    ChrTalk(
        0xFE,
        (
            "金小组，\x01",
            "优胜万岁！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最后的最后，\x01",
            "还是我支持的队伍取得了胜利！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5044")

    label("loc_5001")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_500B")
    Jump("loc_5044")

    label("loc_500B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_5015")
    Jump("loc_5044")

    label("loc_5015")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_501F")
    Jump("loc_5044")

    label("loc_501F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5029")
    Jump("loc_5044")

    label("loc_5029")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_5033")
    Jump("loc_5044")

    label("loc_5033")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_503D")
    Jump("loc_5044")

    label("loc_503D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_5044")

    label("loc_5044")

    TalkEnd(0xFE)
    Return()

    # Function_21_4F8E end

    def Function_22_5048(): pass

    label("Function_22_5048")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_5055")
    Jump("loc_51A2")

    label("loc_5055")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_505F")
    Jump("loc_51A2")

    label("loc_505F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_5069")
    Jump("loc_51A2")

    label("loc_5069")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_515F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_50D6")

    ChrTalk(
        0xFE,
        (
            "因为我和他都支持同一个小组，\x01",
            "所以很合得来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "比赛结束之后\x01",
            "我们就来这里一起喝酒了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_515C")

    label("loc_50D6")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "因为我和他都支持同一个小组，\x01",
            "所以很合得来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "比赛结束之后\x01",
            "我们就来这里一起喝酒了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天肯定也会彻夜狂欢吧。\x01",
            "哈哈哈～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_515C")

    Jump("loc_51A2")

    label("loc_515F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_5169")
    Jump("loc_51A2")

    label("loc_5169")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_5173")
    Jump("loc_51A2")

    label("loc_5173")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_517D")
    Jump("loc_51A2")

    label("loc_517D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5187")
    Jump("loc_51A2")

    label("loc_5187")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_5191")
    Jump("loc_51A2")

    label("loc_5191")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_519B")
    Jump("loc_51A2")

    label("loc_519B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_51A2")

    label("loc_51A2")

    TalkEnd(0xFE)
    Return()

    # Function_22_5048 end

    def Function_23_51A6(): pass

    label("Function_23_51A6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_51B3")
    Jump("loc_53FF")

    label("loc_51B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_51BD")
    Jump("loc_53FF")

    label("loc_51BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_51C7")
    Jump("loc_53FF")

    label("loc_51C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_51D1")
    Jump("loc_53FF")

    label("loc_51D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_51DB")
    Jump("loc_53FF")

    label("loc_51DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_52D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_5254")

    ChrTalk(
        0x104,
        (
            "#030F哎呀，和雪拉君\x01",
            "可不是在这样的\x01",
            "节奏和气氛下喝酒呢。\x02\x03",
            "和她喝酒的时候，\x01",
            "总有一种欲生欲死的感觉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52CD")

    label("loc_5254")

    OP_A2(0x5)

    ChrTalk(
        0x104,
        (
            "#030F哈·哈·哈！\x02\x03",
            "哎呀，和雪拉君\x01",
            "可不是在这样的\x01",
            "节奏和气氛下喝酒呢。\x02\x03",
            "和她喝酒的时候，\x01",
            "总有一种欲生欲死的感觉。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52CD")

    Jump("loc_53FF")

    label("loc_52D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_52DA")
    Jump("loc_53FF")

    label("loc_52DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_53AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_5338")

    ChrTalk(
        0x104,
        (
            "#030F呵，食物可以滋润心灵，\x01",
            "创造生命。\x02\x03",
            "哎呀呀，厨师真是\x01",
            "伟大的存在啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53A9")

    label("loc_5338")

    OP_A2(0x5)

    ChrTalk(
        0x104,
        (
            "#030F哈·哈·哈，\x01",
            "夜幕降临了。\x02\x03",
            "来吧，继续畅饮吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F奥利维尔明明这么瘦，\x01",
            "为什么能装下那么多……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53A9")

    Jump("loc_53FF")

    label("loc_53AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_53B6")
    Jump("loc_53FF")

    label("loc_53B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_53F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_END)), "loc_53F5")

    ChrTalk(
        0x104,
        (
            "#030F唔、嗯……\x02\x03",
            "青春诚短暂，恋爱吧少女……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53F5")

    Jump("loc_53FF")

    label("loc_53F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_53FF")

    label("loc_53FF")

    TalkEnd(0xFE)
    Return()

    # Function_23_51A6 end

    def Function_24_5403(): pass

    label("Function_24_5403")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_566E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_546E")

    ChrTalk(
        0x10,
        (
            "#070F我打算暂时留在这里。\x02\x03",
            "难得来到这里，\x01",
            "等和各位高手较量过之后\x01",
            "再回国也不迟嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_566B")

    label("loc_546E")

    OP_A2(0x4)

    ChrTalk(
        0x10,
        "#070F哟，是你们俩啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F金大哥……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F对了，金大哥你\x01",
            "接下来准备做什么呢？\x02\x03",
            "真的要回去共和国吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#070F不，在共和国\x01",
            "没有发生什么大事，\x01",
            "我准备在这儿呆一段时间。\x02\x03",
            "这个国家有几位\x01",
            "很著名的年轻游击士。\x02\x03",
            "难得来到这里，\x01",
            "等和他们切磋了技艺之后\x01",
            "再回国也不迟嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F著名的游击士？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#070F是啊……\x01",
            "首先是对面的『重剑阿加特』，\x01",
            "然后是『银闪雪拉扎德』。\x02\x03",
            "而且……\x02\x03",
            "一定得和你们俩\x01",
            "也较量一下才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F哇，这真有些难为情啊……\x02\x03",
            "不过，我很期待！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F到时候\x01",
            "还要请您手下留情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_566B")

    Jump("loc_57DE")

    label("loc_566E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_5678")
    Jump("loc_57DE")

    label("loc_5678")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_5682")
    Jump("loc_57DE")

    label("loc_5682")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_568C")
    Jump("loc_57DE")

    label("loc_568C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_5696")
    Jump("loc_57DE")

    label("loc_5696")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_56D6")

    ChrTalk(
        0x10,
        (
            "#070F明天就是决赛了。\x02\x03",
            "记得多吃点，\x01",
            "睡个好觉哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57DE")

    label("loc_56D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_56E0")
    Jump("loc_57DE")

    label("loc_56E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_57C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5719")

    ChrTalk(
        0x10,
        (
            "#070F嗝，怎么样？\x01",
            "你们也来喝吧～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57C0")

    label("loc_5719")

    OP_A2(0x4)

    ChrTalk(
        0x10,
        (
            "#070F哦哦～！\x01",
            "艾丝蒂尔、约修亚！\x02\x03",
            "怎么样？\x01",
            "你们也来喝吧～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F我们可是未成年人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#070F什么，不喝\x01",
            "我的酒吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F哈哈，好像已经\x01",
            "完全喝醉了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57C0")

    Jump("loc_57DE")

    label("loc_57C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_57CD")
    Jump("loc_57DE")

    label("loc_57CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_57D7")
    Jump("loc_57DE")

    label("loc_57D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_57DE")

    label("loc_57DE")

    TalkEnd(0xFE)
    Return()

    # Function_24_5403 end

    def Function_25_57E2(): pass

    label("Function_25_57E2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_58EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5863")

    ChrTalk(
        0xFE,
        (
            "竟然是理查德上校\x01",
            "策动的这起政变。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以前接受杂志的访谈\x01",
            "说的那些了不起的话，\x01",
            "也只是表面文章而已吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58EB")

    label("loc_5863")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "竟然是理查德上校\x01",
            "策动的这起政变。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以前接受杂志的访谈\x01",
            "说的那些了不起的话，\x01",
            "也只是表面文章而已吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "一想到就觉得震惊。\x02",
    )

    CloseMessageWindow()

    label("loc_58EB")

    Jump("loc_5FFB")

    label("loc_58EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_5948")

    ChrTalk(
        0xFE,
        (
            "不知道为什么，\x01",
            "总觉得街上的气氛很怪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "感觉像是\x01",
            "暴风雨来临之前的宁静。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FFB")

    label("loc_5948")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_59AA")

    ChrTalk(
        0xFE,
        (
            "诞辰庆典马上就到了，\x01",
            "王城里面如果能快点\x01",
            "发布公告就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不要这样就中止啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5FFB")

    label("loc_59AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_5A12")

    ChrTalk(
        0xFE,
        (
            "大会明明都结束了，\x01",
            "士兵的数量却一点也没有减少。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "女王陛下又身体欠佳，\x01",
            "真是不吉利啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FFB")

    label("loc_5A12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_5B03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5A85")

    ChrTalk(
        0xFE,
        (
            "昨天晚上满街都是士兵，\x01",
            "回家的时候被他们叫住了四次。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难道我的样子\x01",
            "真的像是一个坏人吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B00")

    label("loc_5A85")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "昨天晚上满街都是士兵，\x01",
            "回家的时候被他们叫住了四次。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难道我的样子\x01",
            "真的像是一个坏人吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是让人泄气啊。\x02",
    )

    CloseMessageWindow()

    label("loc_5B00")

    Jump("loc_5FFB")

    label("loc_5B03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_5B84")

    ChrTalk(
        0xFE,
        (
            "自从《利贝尔通讯》刊登采访以来，\x01",
            "理查德上校的人气\x01",
            "最近一段时间急剧上升啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "无论男女老少，\x01",
            "支持他的人都很多。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FFB")

    label("loc_5B84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_5BF0")

    ChrTalk(
        0xFE,
        (
            "虽然『巴拉尔』咖啡厅的\x01",
            "帝国风味早点也很不错……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但我更喜欢这个店里的\x01",
            "利贝尔风味的早餐。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FFB")

    label("loc_5BF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5CF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5C63")

    ChrTalk(
        0xFE,
        (
            "哎呀呀，\x01",
            "难道说造成柏斯混乱的空贼\x01",
            "也参加了比武大会吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "他们不在监狱服役，这样好吗……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5CEF")

    label("loc_5C63")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "哎呀呀，\x01",
            "难道说造成柏斯混乱的空贼\x01",
            "也参加了比武大会吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然他们的确很有实力，\x01",
            "比赛也很有意思……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "但是不在监狱服役好吗……\x02",
    )

    CloseMessageWindow()

    label("loc_5CEF")

    Jump("loc_5FFB")

    label("loc_5CF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_5E51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5D8C")

    ChrTalk(
        0xFE,
        (
            "武术大会原本是军人用来\x01",
            "展示武技和进行演习的活动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "自从现在的女王陛下继位以来，\x01",
            "就逐渐转变成普通民众\x01",
            "也可以参与的开放式比赛了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E4E")

    label("loc_5D8C")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "武术大会原本是军人用来\x01",
            "展示武技和进行演习的活动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "自从现在的女王陛下继位以来，\x01",
            "就逐渐转变成普通民众\x01",
            "也可以参与的开放式比赛了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "从那个时候开始，\x01",
            "普通民众也可以\x01",
            "报名参加大会了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E4E")

    Jump("loc_5FFB")

    label("loc_5E51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_5EBA")

    ChrTalk(
        0xFE,
        (
            "武术大会变更为团体赛，\x01",
            "这还是头一次。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然是那个\x01",
            "差劲公爵出的主意，\x01",
            "不过也算挺有趣。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FFB")

    label("loc_5EBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_5FFB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_END)), "loc_5EF0")

    ChrTalk(
        0xFE,
        (
            "哎哟，\x01",
            "吓得我被通心粉给哽住了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FFB")

    label("loc_5EF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5F55")

    ChrTalk(
        0xFE,
        (
            "亲卫队因为有制造恐怖活动的嫌疑，\x01",
            "正在被王国军追捕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "最近这类事情还真是接连不断。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5FFB")

    label("loc_5F55")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "亲卫队因为有制造恐怖活动的嫌疑，\x01",
            "正在被王国军追捕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "柏斯的空贼带来的混乱，\x01",
            "卢安的市长被捕事件，\x01",
            "蔡斯的导力停止现象……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "最近这类事情还真是接连不断。\x02",
    )

    CloseMessageWindow()

    label("loc_5FFB")

    TalkEnd(0xFE)
    Return()

    # Function_25_57E2 end

    def Function_26_5FFF(): pass

    label("Function_26_5FFF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_60DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_604A")

    ChrTalk(
        0xFE,
        (
            "虽然发生了许多事情，\x01",
            "但现在终于可以平静地生活了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60D8")

    label("loc_604A")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "看到女王陛下健康的样子，\x01",
            "我就放心了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "亲卫队的嫌疑\x01",
            "也只是被人嫁祸了而已……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然发生了许多事情，\x01",
            "但现在可以平静地生活了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60D8")

    Jump("loc_660A")

    label("loc_60DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_6128")

    ChrTalk(
        0xFE,
        (
            "刚才有几个士兵\x01",
            "慌慌张张跑过去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "到底会发生什么事呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_660A")

    label("loc_6128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_6191")

    ChrTalk(
        0xFE,
        (
            "最近，\x01",
            "在街上能看到很多士兵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "亲卫队的人策划了\x01",
            "这次的恐怖事件的说法\x01",
            "果然是真的吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_660A")

    label("loc_6191")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_61EC")

    ChrTalk(
        0xFE,
        "今天奥利维尔先生没有来呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "听说他们取得了优胜，\x01",
            "本来想特地庆贺一下的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_660A")

    label("loc_61EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_625B")

    ChrTalk(
        0xFE,
        (
            "啊～\x01",
            "我也想去竞技场看比赛呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "干我们这种工作，\x01",
            "在别人在玩乐的时候，\x01",
            "自己却非要工作不可啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_660A")

    label("loc_625B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_62C0")

    ChrTalk(
        0xFE,
        (
            "刚才，\x01",
            "王国军的人来了，\x01",
            "告诉我说只能营业到晚上９点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉～\x01",
            "难得最近的生意那么好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_660A")

    label("loc_62C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_6337")

    ChrTalk(
        0xFE,
        (
            "奥利维尔先生，\x01",
            "你们今天要参加武术大会吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我往年支持的亲卫队\x01",
            "今年不能来参加，\x01",
            "所以就给你们加油吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_660A")

    label("loc_6337")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_637C")

    ChrTalk(
        0xFE,
        (
            "第一天的比赛\x01",
            "好像已经结束了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "结果究竟如何呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_660A")

    label("loc_637C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_646B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_63C5")

    ChrTalk(
        0xFE,
        "你们都是奥利维尔先生的朋友吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "比赛要加油哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6468")

    label("loc_63C5")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "哎呀，奥利维尔先生，\x01",
            "昨天撞到的头没事了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F哈·哈·哈，你看呢。\x02\x03",
            "我那充满世间博爱的\x01",
            "热烈心跳将会\x01",
            "持续到永恒的那一刻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嗯，看来是没问题了。\x02",
    )

    CloseMessageWindow()

    label("loc_6468")

    Jump("loc_660A")

    label("loc_646B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_6525")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_END)), "loc_64E9")

    ChrTalk(
        0xFE,
        (
            "哎呀……仔细看看，\x01",
            "这不是经常在这里演奏的\x01",
            "奥利维尔先生吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "又是因为对女性纠缠不休\x01",
            "而被打飞的吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6522")

    label("loc_64E9")


    ChrTalk(
        0xFE,
        (
            "大会的预选赛好像已经结束了。\x01",
            "这里客人立刻多了起来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6522")

    Jump("loc_660A")

    label("loc_6525")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_660A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_6582")

    ChrTalk(
        0xFE,
        (
            "说亲卫队的人是\x01",
            "恐怖分子什么的，\x01",
            "我难以相信。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "肯定是哪里搞错了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_660A")

    label("loc_6582")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "说亲卫队的人是\x01",
            "恐怖分子什么的，\x01",
            "我难以相信。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽说他们很少到这里来，\x01",
            "但我知道他们都是很正直的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "肯定是哪里搞错了……\x02",
    )

    CloseMessageWindow()

    label("loc_660A")

    TalkEnd(0xFE)
    Return()

    # Function_26_5FFF end

    def Function_27_660E(): pass

    label("Function_27_660E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_67C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_668B")

    ChrTalk(
        0xFE,
        (
            "立下了那么多功绩，\x01",
            "你们俩现在已经是\x01",
            "优秀的正游击士了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不要就此满足，\x01",
            "要向更高的目标发起冲击。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67C2")

    label("loc_668B")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "哟，\x01",
            "这回的事件解决得不错啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "立下了那么多功绩，\x01",
            "你们俩现在已经是\x01",
            "优秀的正游击士了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不要就此满足，\x01",
            "要向更高的目标发起冲击。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嘿嘿，谢谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F克鲁茨大哥，\x01",
            "你的身体已经没什么大碍了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊，\x01",
            "你看看，棒得很啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "遗憾的是……\x01",
            "到底是谁消除了我的记忆，\x01",
            "我怎么也想不起来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67C2")

    TalkEnd(0xFE)
    Return()

    # Function_27_660E end

    def Function_28_67C6(): pass

    label("Function_28_67C6")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B48")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 3930, 0, -620, 0)
    SetChrPos(0x102, 5070, 0, -540, 0)
    SetChrPos(0x108, 4540, 0, -1430, 0)
    TurnDirection(0xC, 0x108, 0)
    OP_A2(0x64A)
    OP_6D(4720, 0, 250, 1000)

    ChrTalk(
        0x101,
        "#000F库拉茨大哥，终于找到你了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "哦，\x01",
            "优胜组出现了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "晚宴后应该在城里住住吧，\x01",
            "怎么这么快就回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "想必一定是吃了\x01",
            "不少美味佳肴吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F的确是很美味……\x01",
            "不过远非如此简单呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "远非如此？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "把至今为止发生的事情\x01",
            "和女王的委托\x01",
            "依次予以说明。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0xC,
        (
            "…………………………\x01",
            "……喂喂，没搞错吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F很可惜，\x01",
            "确实是真的。\x02\x03",
            "我可以用我的称号作为赌注。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "『不动的金』……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "你所担保的事情\x01",
            "肯定是勿庸置疑了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "好，我明白了，\x01",
            "让我也来帮忙吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F谢谢你，库拉茨大哥！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F首先要召开作战会议，\x01",
            "请回游击士协会去吧。\x02\x03",
            "大家都会集中在那里的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "明白了，待会儿见！\x02",
    )

    CloseMessageWindow()

    def lambda_6AA3():

        label("loc_6AA3")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_6AA3")

    QueueWorkItem2(0x101, 1, lambda_6AA3)

    def lambda_6AB4():

        label("loc_6AB4")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_6AB4")

    QueueWorkItem2(0x102, 1, lambda_6AB4)

    def lambda_6AC5():

        label("loc_6AC5")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_6AC5")

    QueueWorkItem2(0x108, 1, lambda_6AC5)
    OP_8E(0xC, 0xBEA, 0x0, 0x1E, 0xBB8, 0x0)
    OP_8E(0xC, 0x406, 0x0, 0xFFFFF402, 0xBB8, 0x0)
    OP_8E(0xC, 0x2C6, 0xFFFFFF06, 0xFFFFEA8E, 0xBB8, 0x0)

    def lambda_6B12():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6B12)
    OP_8E(0xC, 0x2C6, 0xFFFFFF06, 0xFFFFE2D2, 0xBB8, 0x0)
    SetChrFlags(0xC, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    EventEnd(0x0)
    Jump("loc_6FA5")

    label("loc_6B48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_6CF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_6B9E")

    ChrTalk(
        0xFE,
        (
            "我们以后可能就要\x01",
            "一起执行任务了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "到时候还要多多关照哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6CF0")

    label("loc_6B9E")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "哟，英雄们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F库拉茨大哥……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们两个\x01",
            "干得真漂亮。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "竟然还只是准游击士，\x01",
            "简直不可思议啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嘿嘿……\x02\x03",
            "其实这是大家共同努力\x01",
            "所换回来的美好结果呢。\x02\x03",
            "到了最后还是老爸\x01",
            "出手相助的，\x01",
            "我们的本领还没到家啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……你们真的\x01",
            "已经做得很好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们以后可能就要\x01",
            "一起执行任务了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "到时候还要多多关照哦。\x02",
    )

    CloseMessageWindow()

    label("loc_6CF0")

    Jump("loc_6FA5")

    label("loc_6CF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_6CFD")
    Jump("loc_6FA5")

    label("loc_6CFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_6D07")
    Jump("loc_6FA5")

    label("loc_6D07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_6DF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_6D5C")

    ChrTalk(
        0xFE,
        (
            "咦？\x01",
            "那个金发的兄弟到哪里去了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他的枪法\x01",
            "有相当的水准呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DF5")

    label("loc_6D5C")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "哦哦，\x01",
            "这不是优胜组的成员吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天的比赛，\x01",
            "我们都认真地观摩了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然说我们也想取得优胜，\x01",
            "不过这个冠军让你们拿了\x01",
            "我们一点也没觉得遗憾。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DF5")

    Jump("loc_6FA5")

    label("loc_6DF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_6E02")
    Jump("loc_6FA5")

    label("loc_6E02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_6E0C")
    Jump("loc_6FA5")

    label("loc_6E0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_6E16")
    Jump("loc_6FA5")

    label("loc_6E16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6E20")
    Jump("loc_6FA5")

    label("loc_6E20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_6F94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_6E6D")

    ChrTalk(
        0xFE,
        (
            "就算是游击士，\x01",
            "也要保证良好的睡眠，\x01",
            "早饭也要吃好才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F91")

    label("loc_6E6D")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "哟，\x01",
            "你们也是来吃早饭的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，是库拉茨大哥。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就算是游击士，\x01",
            "也要保证良好的睡眠，\x01",
            "早饭也要吃好才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们在协会的研修中也学了吧。\x01",
            "如果没有休息好，判断力和身体都会迟钝。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F哈哈，\x01",
            "艾丝蒂尔只有对这一点是完全理解的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F喂……\x01",
            "那个『只有』是什么意思。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F91")

    Jump("loc_6FA5")

    label("loc_6F94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_6F9E")
    Jump("loc_6FA5")

    label("loc_6F9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_6FA5")

    label("loc_6FA5")

    TalkEnd(0xC)
    Return()

    # Function_28_67C6 end

    def Function_29_6FA9(): pass

    label("Function_29_6FA9")

    EventBegin(0x0)
    OP_6D(90, 0, 3350, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -2570, -30, 1820, 90)
    SetChrPos(0x101, 220, -250, -4920, 0)
    SetChrPos(0x102, 1840, -250, -4860, 0)
    OP_6D(590, 0, -1250, 2500)

    ChrTalk(
        0x101,
        (
            "#000F……果然是大赖皮蛋奥利维尔啊。\x02\x03",
            "不过，本来以为演奏家什么的\x01",
            "只是他自称的而已……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F听起来水平相当的高啊。\x02\x03",
            "只有自称职业的演奏家这点\x01",
            "应该是没错的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯……\x01",
            "我听得有点入迷了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#030F刚才的曲子是\x01",
            "『身陷琥珀之城』。\x02\x03",
            "本来这首曲子是\x01",
            "虽然只是一首伴奏曲……\x02\x03",
            "在此借用这首曲子，献上爱与真心的演奏。\x02\x03",
            "以把我无尽的爱，\x01",
            "毫无保留地赠送予你们。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7179():
        OP_8E(0xFE, 0xFFFFFC2C, 0x0, 0xFFFFF9DE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7179)
    Sleep(500)

    def lambda_7199():
        OP_8E(0xFE, 0xFFFFF827, 0x0, 0xAA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7199)

    def lambda_71B4():
        OP_6D(-1740, 0, 1730, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_71B4)
    WaitChrThread(0x101, 0x1)

    def lambda_71D1():
        OP_8E(0xFE, 0xFFFFF402, 0x0, 0xC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_71D1)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x8, 400)
    WaitChrThread(0x102, 0x1)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0x101,
        (
            "#000F还是老样子，\x01",
            "自我感觉良好的人啊……\x02\x03",
            "哈啊……\x01",
            "本来想感动一番的，气氛都被破坏了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F很久不见了，奥利维尔。\x01",
            "你也来王都了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#030F当然，像落入河中的人鱼眼泪\x01",
            "终究会到达大海一样……\x02\x03",
            "本人是为了与黑发的王子\x01",
            "令人感动地再会而来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F……真是一点也没变啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F玩笑就开到这里，\x01",
            "赶快招待我们坐下吧。\x02\x03",
            "就会装模作样，\x01",
            "一点也不会看人脸色。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#030F艾丝蒂尔君……\x01",
            "不觉得太过分了吗？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    SetChrPos(0x8, -3770, 0, -2300, 180)
    SetChrPos(0x101, -3460, 0, -4600, 0)
    SetChrPos(0x102, -4940, 0, -4560, 0)
    OP_6D(-3770, 0, -3540, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#000F我记得，奥利维尔\x01",
            "你不是和雪拉姐一起到洛连特去了吗？\x02\x03",
            "什么时候来王都的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#030F嗯……大概是一个月之前吧？\x02\x03",
            "和你们分别之后，\x01",
            "我与雪拉小姐在洛连特\x01",
            "度过了一段美好的时光。\x02\x03",
            "可是，我到底是个\x01",
            "漂泊的诗人和演奏家……\x02\x03",
            "最终还是狠心拒绝了\x01",
            "雪拉小姐含泪的挽留，\x01",
            "漂流到了这美丽的王都。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F该怎么说呢……\x01",
            "真是让人无法相信的说法啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F肯定是每天晚上\x01",
            "被雪拉姐强迫灌酒，\x01",
            "结果实在忍受不了而逃出来吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#030F呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F难不成，\x01",
            "是和爱娜小姐一起喝酒吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#030F………………………………\x01",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F对了，奥利维尔\x01",
            "还不认识爱娜小姐吧？\x02\x03",
            "她是雪拉姐的朋友，\x01",
            "洛连特支部的接待员。\x02\x03",
            "据说她的酒量\x01",
            "比雪拉姐还要高……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#030F……哈哈哈，\x01",
            "真讨厌啊，艾丝蒂尔君。\x02\x03",
            "叫这个名字的人，\x01",
            "我没有见过，也没有听说过哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F你的声音\x01",
            "完全把你给出卖了呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔……\x01",
            "就放过他吧。 \x02\x03",
            "我想一定发生了悲惨……\x01",
            "非常悲惨的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#030F呜呜，没想到还有比雪拉小姐酒量更高的，\x01",
            "简直是无底洞……\x02\x03",
            "啊啊啊……\x02\x03",
            "不～要～再带着那迷人的微笑\x01",
            "给我灌酒啦～！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)

    ChrTalk(
        0x101,
        "#000F回、回忆重现！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F着实沉醉于\x01",
            "爱娜小姐的最强传说中呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#030F呼呼呼……\x01",
            "唉，这个就先别提了。\x02\x03",
            "你们不是走遍其他地方，\x01",
            "然后来到王都了吗？\x02\x03",
            "都遇到过什么有趣的事情？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，这可是短时间内\x01",
            "没办法说清楚的……\x02\x03",
            "而且现在我们正在找人，\x01",
            "下次见面的时候再说好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#030F哎……\x01",
            "你们是在找谁啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F一位名叫『金』的\x01",
            "认识了一个从卡尔瓦德\x01",
            "武术家游击士。\x02\x03",
            "据说他经常来酒馆，\x01",
            "奥利维尔，你见过吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#030F啊啊！\x01",
            "那个像山一样高大的老兄啊。\x02\x03",
            "以前见过很多次，\x01",
            "不过今天还没有看见他。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F是吗……\x01",
            "今天没有来酒馆吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A7C")

    ChrTalk(
        0x102,
        (
            "#010F在卡尔瓦德共和国大使馆\x01",
            "那边的可能性就很高了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#030F呼……\x01",
            "那我们赶快去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7ACE")

    label("loc_7A7C")


    ChrTalk(
        0x102,
        (
            "#010F在艾尔贝周游道\x01",
            "那边的可能性就很高了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#030F呼……\x01",
            "那我们赶快去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7ACE")

    OP_A2(0x613)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_29_6FA9 end

    def Function_30_7ADE(): pass

    label("Function_30_7ADE")

    EventBegin(0x0)
    SetChrFlags(0x108, 0x4)
    SetChrPos(0x108, -3800, 0, -2180, 180)
    SetChrPos(0x101, -3460, 0, -4600, 0)
    SetChrPos(0x102, -4940, 0, -4600, 0)
    OP_6D(-3770, 0, -3540, 0)

    ChrTalk(
        0x108,
        (
            "#070F……原来如此，是这样啊。\x02\x03",
            "我问你们一件事，\x01",
            "为什么要参加武术大会呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯……看过预选赛之后，\x01",
            "身体就按耐不住了。\x02\x03",
            "情不自禁地想要\x01",
            "和强大的对手大战一场呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们现在以正游击士为目标\x01",
            "在王国各地旅行。\x02\x03",
            "所以想借此机会\x01",
            "测试一下至今的修行成果。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F嗯……\x02\x03",
            "可以啊。\x01",
            "一起组队吧。\x02\x03",
            "在明天大会开始之前\x01",
            "去报一下名就没问题了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F太好了～㈱\x02\x03",
            "……嗯，\x01",
            " \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F你们的实力\x01",
            "我之前就见识过了。\x02\x03",
            "作为协助我的人已经足够了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嘿嘿……\x01",
            "谢谢，金先生！\x02\x03",
            "我会尽全力加油的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F请多指教。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F彼此彼此。\x02\x03",
            "不过，本来是打算挑战一下，\x01",
            "只靠１个人能够到达什么程度的……\x02\x03",
            "现在有了协助的人，\x01",
            "就不能不想到要拿冠军了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F那当然了！\x01",
            "既然参加就要拿冠军！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F不过，如果这样打算的话，\x01",
            "缺少一个人，还是很难办到的。\x02\x03",
            "团体赛的人数是４个啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，是啊……\x01",
            "还缺少一个人呢。\x02\x03",
            "不过，\x01",
            "只要鼓足干劲的话！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F不，如果目标提高的话，\x01",
            "就要做好万全的准备。\x02\x03",
            "作战在拳脚相加之前\x01",
            "就应该要开始。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯……确实是这样啊。\x02\x03",
            "这个时候，\x01",
            "如果雪拉姐在就好了……\x02\x03",
            "喂，我们去拜托艾南先生\x01",
            "联络一下洛连特支部吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯……\x01",
            "但是雪拉姐姐一定会很忙的。\x02\x03",
            "父亲和我们都不在，\x01",
            "洛连特支部正缺少人手呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F是……是这样没错。\x02\x03",
            "啊～真是的，不管是谁都好，\x01",
            "有没有能帮我们的人啊！\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x8, -1920, 4000, 4680, 180)
    ClearChrFlags(0x8, 0x80)

    ChrTalk(
        0x8,
        (
            "唔……\x01",
            "我就是在等这句话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F这、这个声音是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F难道……\x02",
    )

    CloseMessageWindow()
    OP_6D(-1290, 4000, 5210, 3000)

    def lambda_8069():
        OP_6D(-2350, 0, -630, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8069)
    OP_8E(0x8, 0xFFFFEDAE, 0x7D0, 0x11C6, 0xBB8, 0x0)
    OP_8E(0x8, 0xFFFFED36, 0x0, 0xFFFFFE7A, 0xBB8, 0x0)

    ChrTalk(
        0x101,
        (
            "#000F果然出现了～\x01",
            "这个乱侃的演奏家。\x02\x03",
            "不会一直在２楼潜伏着吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F难道……\x01",
            "刚才的话你都听见了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#030F呵呵……\x01",
            "一字不漏地全都听见了。\x02\x03",
            "于是就想：这次轮到我出场了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x4)
    OP_96(0x8, 0xFFFFEC64, 0x0, 0xFFFFF722, 0x3E8, 0x1388)

    ChrTalk(
        0x101,
        (
            "#000F啊，等一下！\x01",
            "怎么随便就坐下来了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F这个不是弹钢琴的\x01",
            "那个演奏家小哥嘛。\x02\x03",
            "是你们的熟人吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F该说是熟人呢，\x01",
            "还是缘分的捉弄呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F……还没有达到\x01",
            "熟人这种程度吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#030F本人是奥利维尔·朗海姆。\x01",
            "来自埃雷波尼亚的旅行演奏家。\x02\x03",
            "和艾丝蒂尔君、约修亚君\x01",
            "是在之前的事件中认识的。\x02\x03",
            "从那以后，关系变得很不一般呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F请不要用容易引起误会的方式说话！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F嗯，虽然不知道是怎么回事，\x01",
            "我也来报个名字吧。\x02\x03",
            "金·瓦赛克，\x01",
            "来自卡尔瓦德的游击士，\x01",
            "以武术之道为志向。\x02\x03",
            "你的钢琴\x01",
            "我一直很欣赏呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#030F嘻嘻……\x01",
            "能得到夸奖真是光荣至极。\x02\x03",
            "本人也听说了\x01",
            "你在武术大会预选赛中的武勇事迹。\x02\x03",
            "面对４个人的对手，\x01",
            "只凭借１个人就获得压倒性胜利对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F遇到新手的对手，只是运气好罢了。\x02\x03",
            "那么，演奏家先生\x01",
            "找我们到底有什么事情呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F给我等一下～～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F奥利维尔先生……\x01",
            "我想确认一件事……\x02\x03",
            "难道最近\x01",
            "你没有事情可做吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#030F不愧是约修亚君，\x01",
            "这个问题真是尖锐啊。\x02\x03",
            "来到王都的这１个月间……\x02\x03",
            "到处观光一遍之后，\x01",
            "剩下的格兰赛尔城\x01",
            "却因为有士兵把守而无法进入……\x02\x03",
            "想去别的地方看看，\x01",
            "诞辰庆典又快要到了，\x01",
            "现在还舍不得离开王都……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F总之，就是很闲。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#030F然后突然听到了\x01",
            "『缺少一个队员』的谈话……\x02\x03",
            "而且最重要的是，\x01",
            "优胜者会得到豪华晚餐会的招待……\x02\x03",
            "简直是女神的启示！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我就知道。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#030F就是这样，\x01",
            "能不能让我也成为参加武术大会的伙伴呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#070F为什么不呢？\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#000F等、等一下金先生。\x01",
            "这么简单就……\x02\x03",
            "你还不知道\x01",
            "奥利维尔的战斗方法吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F他擅长的是导力枪对吗？\x02\x03",
            "这样可以采取广泛的战术，\x01",
            "我觉得能组成很好的队伍呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#000F哎～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#030F这真是……让人吃惊啊。\x02\x03",
            "是不是从腰间的鼓起\x01",
            "和走路的方式判断出来的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F还有视线移动的方式。\x02\x03",
            "武术家和剑士捕捉移动的目标时\x01",
            "视线是沿着线移动的……\x02\x03",
            "而你对别人的行动的把握\x01",
            "集中在一个一个点上。\x02\x03",
            "这是使枪的人移动视线的特殊之处。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嘿哎，真是专业啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F原来如此……\x01",
            "确实很有道理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#030F嗯……\x01",
            "今后我要注意一点了。\x02\x03",
            "那么，在你这位高手的眼光看来，\x01",
            "我就算合格了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#070F啊，请多关照啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯。\x01",
            "虽然感觉有点不安……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F奥利维尔先生，\x01",
            "请多多关照。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_30_7ADE end

    def Function_31_89AA(): pass

    label("Function_31_89AA")

    EventBegin(0x0)
    OP_6D(63970, 200, 7220, 0)
    OP_67(0, 7860, -10000, 0)
    OP_6B(2540, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x17, 0x80)
    SetChrChipByIndex(0x101, 23)
    SetChrChipByIndex(0x102, 24)
    SetChrChipByIndex(0x9, 25)
    SetChrPos(0x20, 58830, 640, -4430, 0)
    SetChrPos(0x25, 58360, 640, -4450, 0)
    SetChrPos(0x22, 59290, 640, -4980, 0)
    SetChrPos(0x23, 59290, 640, -4720, 0)
    SetChrPos(0x21, 58740, 640, -5400, 0)
    SetChrPos(0x24, 58930, 640, -5550, 0)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    SetChrPos(0x101, 60050, 200, -4970, 270)
    SetChrPos(0x9, 58770, 200, -3750, 180)
    SetChrPos(0x102, 58770, 200, -6150, 0)
    SetChrPos(0x16, 62360, 0, 2910, 0)
    ClearChrFlags(0x9, 0x80)
    FadeToBright(1000, 0)
    OP_6D(59510, 200, -4760, 5000)

    ChrTalk(
        0x101,
        (
            "#001F哈～虽然有点辣，\x01",
            "不过很好吃呢㈱\x02\x03",
            "#008F香脆的里脊肉和松软的蒸土豆，\x01",
            "真的是极佳的配搭呢……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F饭后的咖啡也是非常香浓。\x02\x03",
            "虽然听说过用玻璃器具泡咖啡\x01",
            "有相当的难度……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#142F真是的，花别人的钱，\x01",
            "就可以这么狼吞虎咽的吃……\x02\x03",
            "我那点可怜的工资都给你们吃完了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#502F好啦好啦。\x01",
            "总之谢谢你招待我们啦。\x02\x03",
            "#006F那么……\x01",
            "你果然在为新闻素材伤脑筋吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#142F哼……\x01",
            "新闻素材要多少有多少。\x02\x03",
            "#145F不过，都是些关于亲卫队的恐怖活动、\x01",
            "女王身体欠佳之类的小道消息，\x01",
            "这些东西的可信度很难保证啊。\x02\x03",
            "明确地说，\x01",
            "我想要的是没有经过军队过滤的、\x01",
            "新鲜可靠的、最新最快的情报。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F我从朵洛希那里听说了一些\x01",
            "关于蔡斯发生的绑架事件的消息……\x02\x03",
            "就开门见山地说吧。\x02\x03",
            "你们对那个理查德上校\x01",
            "到底调查到什么程度了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F该怎么说呢，真是一针见血啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F能提出这样深入的问题，\x01",
            "您应该已经有所推测了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#145F果然上校就是幕后主谋啊……\x02\x03",
            "我们杂志还因采访过他而人气大增，\x01",
            "真是不想接受这个现实啊……\x01",
            "　\x02\x03",
            "#142F反叛者马上就要有所行动了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F他是否对女王陛下有反叛企图，\x01",
            "现在我们还不得而知。\x02\x03",
            "但是，他们把杜南公爵作为傀儡，\x01",
            "在暗地企图什么是可以肯定的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#142F杜南公爵吗……\x02\x03",
            "趁着陛下身体欠佳，\x01",
            "把自己当成格兰赛尔城的主人，\x01",
            "一个肆意妄为的王室败家子……\x02\x03",
            "不可思议的是，\x01",
            "军队的高官为什么听之任之呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F唉，那个是因为……\x02\x03",
            "#505F……喂，约修亚。\x01",
            "这个可以说出来吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F是啊……\x01",
            "我们也要尽可能地收集相关的情报。\x01",
            "　\x02\x03",
            "#010F如果是奈尔先生的话，\x01",
            "我想一定能帮助我们的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#143F喂喂，怎么了。\x01",
            "你们果然知道些什么吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F我事先声明……\x02\x03",
            "接下来要说的事情，\x01",
            "是不能作为报道写出去的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#507F也就是说，先要做好心理准备。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#142F可恶……\x01",
            "这不是很糟糕的事情吗。\x02\x03",
            "算了，赶快说吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrSubChip(0x9, 3)
    FadeToBright(1500, 0)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#145F………………………………\x01",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F啊～\x01",
            "所以我说要做好心理准备嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#145F这怎么可能……\x02\x03",
            "#142F喂……这是千真万确的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F虽然很遗憾，不过事实就是这样。\x02\x03",
            "先是空贼事件，然后是孤儿院纵火事件，\x01",
            "之后是中央工房的袭击事件……\x02\x03",
            "所有这些事情，\x01",
            "都和情报部的特务兵有关系。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F而且，军队的上层都被抓住了痛脚，\x01",
            "连摩尔根将军也被强制软禁了……\x02\x03",
            "亲卫队被强加上莫须有的罪名，\x01",
            "被当作恐怖分子受到追捕……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrSubChip(0x9, 0)

    ChrTalk(
        0x9,
        (
            "#144F啊啊～真是的！\x01",
            "怎么又是这样！\x02\x03",
            "#145F可恶……\x01",
            "这怎么能写成报道呢。\x02\x03",
            "最近我们杂志也要接受军队的检查……\x01",
            "　\x02\x03",
            "印刷的时候肯定会被拦下来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F是、是这样吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#142F没办法……\x01",
            "只好勉强报道一下与这些事情\x01",
            "没什么关系的武术大会了……\x02\x03",
            "#143F……啊，对了。\x02\x03",
            "你们参加武术大会，\x01",
            "也是有什么特别的理由吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯，没错。\x02\x03",
            "虽然和委托的内容有关，\x01",
            "所以不能告诉你详细的情况……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F您只要知道这是为了打开目前局面\x01",
            "所采取的行动就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#142F是吗……\x02\x03",
            "#145F………………………………\x01",
            "………………………………\x02\x03",
            "……好，我决定了。\x02\x03",
            "#142F虽然作为记者不能够做些什么……\x01",
            "不过，我也来帮你们忙吧。\x02\x03",
            "游击士协会调查不到的事情，\x01",
            "就由我通过私人的途径来调查吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F谢谢，真是帮大忙了呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F对方可是军队啊，\x01",
            "这样做的话恐怕太危险了。\x02\x03",
            "即使这样，你也愿意帮忙吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#144F真啰嗦，这是我的战斗。\x02\x03",
            "作为一名记者，\x01",
            "我怎么能眼睁睁地看着笔杆输给刀剑呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F奈尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F我明白了……\x01",
            "那么这件事就拜托您了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#141F嗯，就交给我吧。\x02\x03",
            "那么，还有一点，\x01",
            "具体来说你们想调查些什么事情呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F这个嘛……\x01",
            "应该是军队的动向吧。\x02\x03",
            "亲卫队的人是不是都被逮捕了……\x01",
            "　\x02\x03",
            "摩尔根将军被囚禁在哪里……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#142F知道了，\x01",
            "我会多加注意的。\x02\x03",
            "除了调查这些事情，\x01",
            "……还有没有其他的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F……那个……\x02\x03",
            "有关情报部成员的经历，\x01",
            "请问能帮我们调查一下吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#143F情报部成员的经历吗……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F说具体一点，\x01",
            "就是作为核心的理查德上校、凯诺娜上尉，\x01",
            "以及洛伦斯少尉这三个人。\x02\x03",
            "因为以后要和他们对决，\x01",
            "所以想知道他们的一些详细经历……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#141F我明白了……\x01",
            "你的意思是『知己知彼，百战不殆』吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F没错，除了上校，\x01",
            "那个少尉的事情也想知道得更多一些。\x02\x03",
            "约修亚刚才也说了，\x01",
            "明天或者后天的比赛中说不定\x01",
            "会和这个人领衔的特务部队对战……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F奈尔先生，这件事拜托您可以吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#145F……我在军队里认识不少人。\x02\x03",
            "军队的机密情报先不说，\x01",
            "如果是单纯的简历的话说不定能弄到手。\x01",
            "　\x02\x03",
            "#141F好吧，我就试试看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F那真是太感谢了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那就拜托您了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#141F哎呀，没什么大不了的啦。\x02\x03",
            "总之大家就要有来有往嘛。\x01",
            "如果你们取得优胜后被招待进王城的话，\x01",
            "一定要把详细情形都告诉我哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F果然是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我知道了，\x01",
            "只要是能说出来的都会告诉你。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，艾丝蒂尔他们和奈尔在咖啡厅分手，\x01",
            "接着就回到酒店早早地休息了。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "然后，第二天早上——\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_56(0x0)
    Sleep(500)
    OP_22(0xD, 0x0, 0x64)
    Sleep(3000)
    SetMapFlags(0x100000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4132   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_31_89AA end

    def Function_32_9C30(): pass

    label("Function_32_9C30")

    EventBegin(0x0)
    OP_6D(-61470, 0, 67180, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x9, -56660, 0, 64750, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x101, -61900, 0, 67420, 135)
    SetChrPos(0x102, -63460, 0, 66810, 135)

    ChrTalk(
        0x101,
        "#000F喂～奈尔。\x02",
    )

    CloseMessageWindow()

    def lambda_9CC2():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9CC2)

    ChrTalk(
        0x102,
        "#010F打扰了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F……哦哦，终于来了。\x02\x03",
            "朵洛希那家伙，\x01",
            "传话难得能成功一次呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9D29():
        OP_6D(-57890, 0, 65099, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_9D29)

    def lambda_9D41():
        OP_6B(2600, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_9D41)

    def lambda_9D51():

        label("loc_9D51")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_9D51")

    QueueWorkItem2(0x101, 1, lambda_9D51)

    def lambda_9D62():

        label("loc_9D62")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_9D62")

    QueueWorkItem2(0x9, 1, lambda_9D62)

    def lambda_9D73():
        OP_8E(0xFE, 0xFFFF18F2, 0x0, 0xFC94, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9D73)
    OP_8E(0x102, 0xFFFF1370, 0x0, 0x1046E, 0xBB8, 0x0)

    def lambda_9DA2():
        OP_8E(0xFE, 0xFFFF1F6E, 0x0, 0xFB9A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_9DA2)
    OP_8E(0x102, 0xFFFF13B6, 0x0, 0xFC30, 0xBB8, 0x0)
    OP_8E(0x102, 0xFFFF1A28, 0x0, 0xF988, 0xBB8, 0x0)
    TurnDirection(0x102, 0x9, 400)

    ChrTalk(
        0x9,
        (
            "#140F对了，\x01",
            "今天你们也赢了吧。\x02\x03",
            "朵洛希那家伙，\x01",
            "回来的时候兴高采烈的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嘿嘿，是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F那么奈尔先生，\x01",
            "关于那件事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F哦，真是开门见山啊。\x02\x03",
            "给你……\x01",
            "主要成员的经历都收集到了呢。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "奈尔拿出\x01",
            "一本黑色封皮的文件。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        "#000F这是……王国军的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F啊，虽然机密度不是很高，\x01",
            "不过也是不能随便拿出来的文件呢。\x02\x03",
            "好不容易说服军队中的熟人\x01",
            "才借来的，不要往外说啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F那么，\x01",
            "我们就在这里看吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔和约修亚\x01",
            "翻看着那本黑色封皮的文件。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_A008")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A775")
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A083")

    Menu(
        0,
        10,
        10,
        0,
        (
            "关于理查德上校\x01",      # 0
            "关于凯诺娜上尉\x01",      # 1
            "关于洛伦斯少尉\x01",      # 2
            "关闭文件\x01",            # 3
        )
    )

    Jump("loc_A0B9")

    label("loc_A083")


    Menu(
        0,
        10,
        10,
        0,
        (
            "关于理查德上校\x01",      # 0
            "关于凯诺娜上尉\x01",      # 1
            "关于洛伦斯少尉\x01",      # 2
        )
    )


    label("loc_A0B9")

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A0EC"),
        (1, "loc_A398"),
        (2, "loc_A569"),
        (3, "loc_A762"),
        (SWITCH_DEFAULT, "loc_A772"),
    )


    label("loc_A0EC")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "亚兰·理查德上校。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "七耀历１１６８年，\x01",
            "生于利贝尔王国卢安地区。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "作为士官学校的主席毕业之后，\x01",
            "编入了卡西乌斯·布莱特上校\x01",
            "加入了独立机动部队。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在１０年前的百日战役中\x01",
            "作为卡西乌斯上校的部下\x01",
            "在反攻作战中屡立战功。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "卡西乌斯上校退役之后，\x01",
            "被提拔为军队作战中心的成员，\x01",
            "在组织改革中建立了很多功绩。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "１年前，作出了设立情报部的提案。\x01",
            "之后获得了艾莉茜雅女王的承认，\x01",
            "就任情报部首任指挥官。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A395")
    OP_A2(0x673)

    ChrTalk(
        0x101,
        (
            "#000F该怎么说呢……\x01",
            "这就是所谓的精英吧。\x02\x03",
            "他可是主席呢，主席。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F确实是个很厉害的人物呢。\x02\x03",
            "希德少校说得没错，\x01",
            "１０年前战争的时候，\x01",
            "他确实是父亲的部下呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，老爸\x01",
            "真的当过上校呢……\x02\x03",
            "明明这么了不起，\x01",
            "为什么要辞掉呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A395")

    Jump("loc_A772")

    label("loc_A398")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "凯诺娜·亚马尔迪亚上尉。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "七耀历１１７５年，\x01",
            "生于利贝尔王国王都格兰赛尔。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "以优秀的成绩从士官学校毕业之后，\x01",
            "被提拔为军队作战中心的成员。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "１年前，在情报部设立的同时，\x01",
            "得到理查德上校的提拔，\x01",
            "调到了情报部。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，作为理查德上校的副官，\x01",
            "担当辅佐其进行作战指挥的工作。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A566")
    OP_A2(0x674)

    ChrTalk(
        0x101,
        (
            "#000F『以优秀的成绩毕业』，\x01",
            "看起来又是一个精英呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F自从她担任军官以来，\x01",
            "她好像一直在\x01",
            "理查德上校手下做事。\x02\x03",
            "真是相当地忠诚呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A566")

    Jump("loc_A772")

    label("loc_A569")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "洛伦斯·博格少尉。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "年龄、国籍不明。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "原属佣兵部队『杰斯塔猎兵团』，\x01",
            "应理查德上校的征召，\x01",
            "成为了情报部的一员。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在这之前的经历不明。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A75F")
    OP_A2(0x675)

    ChrTalk(
        0x101,
        (
            "#000F那个戴面具的家伙……\x01",
            "不是利贝尔人啊。\x02\x03",
            "而且作为原佣兵的经历不明\x01",
            "是怎么一回事啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F……不知道呢。\x02\x03",
            "所谓『猎兵团』，\x01",
            "是只有最高级别的佣兵部队\x01",
            "才能获得的称号……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F哎～是这样啊。\x02\x03",
            "是不是因为战斗能力很强，\x01",
            "才得到上校提拔的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯……说不定。\x02\x03",
            "『杰斯塔猎兵团』……\x01",
            "这名字我好像在哪听到过。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A75F")

    Jump("loc_A772")

    label("loc_A762")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_A772")

    label("loc_A772")

    Jump("loc_A008")

    label("loc_A775")


    ChrTalk(
        0x101,
        (
            "#000F谢谢你，奈尔。\x01",
            "不管怎么说，能看清敌人的样子了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F能帮上忙就再好不过了。\x02\x03",
            "我在调查资料的时候，\x01",
            "也发现了很多有趣的事情呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 400)

    ChrTalk(
        0x102,
        "#010F有趣的事情……是？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F比如，现在被通缉的\x01",
            "亲卫队的尤莉亚中尉……\x02\x03",
            "在士官学校和凯诺娜上尉\x01",
            "是同一年级的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎～是吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F不过看起来，\x01",
            "那两个人的关系\x01",
            "好像不是很好呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F不管怎么说，她们是\x01",
            "互相竞争主席职位的对手呢。\x02\x03",
            "学问有凯诺娜上尉，\x01",
            "武术有尤莉亚中尉。\x01",
            "两个人真是很好的对照呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F原来如此……\x01",
            "我大概能想象出来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F尤莉亚中尉威风凛凛的\x01",
            "好像过去的骑士呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F还有……\x01",
            "虽然这个和军队没有关系。\x02\x03",
            "你们听说过\x01",
            "『科洛蒂娅公主』这个名字吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F科洛蒂娅公主……\x01",
            "好像在哪里听说过？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我记得，是在海难事故中去世的\x01",
            "王太子夫妻的遗孤吧。\x02\x03",
            "是女王陛下的孙女……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F嗯，虽然不太有名，\x01",
            "不过可是直系中的直系呢。\x02\x03",
            "她好像一直生活在\x01",
            "格兰赛尔城的女王宫里……\x02\x03",
            "而且，好像某个人物正在寻找\x01",
            "那位公主殿下的相亲对象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F相亲对象啊……\x02\x03",
            "虽然对大户人家来说，\x01",
            "不是什么新鲜事……\x02\x03",
            "不过觉得有点可怜呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔，重点不在那里吧。\x02\x03",
            "现在应该注意的问题是\x01",
            "『某个人物』吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#140F呵呵，真是敏锐啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎，那个人难道是……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "艾莉茜雅女王？\x01",      # 0
            "杜南公爵？\x01",          # 1
            "理查德上校？\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_AC6B"),
        (1, "loc_ACFC"),
        (2, "loc_AD83"),
        (SWITCH_DEFAULT, "loc_AE12"),
    )


    label("loc_AC6B")


    ChrTalk(
        0x9,
        (
            "#140F啊，名义上是的。\x02\x03",
            "不过实际上，派人去外国\x01",
            "寻找合适的候选人的，\x01",
            "是那个理查德上校呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F什么～！？\x02\x03",
            "可、可是，这不是很奇怪吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE12")

    label("loc_ACFC")


    ChrTalk(
        0x9,
        (
            "#140F没错。\x02\x03",
            "不过实际上，派人去外国\x01",
            "寻找合适的候选人的，\x01",
            "是那个理查德上校呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F什么～！？\x02\x03",
            "可、可是，这不是很奇怪吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE12")

    label("loc_AD83")


    ChrTalk(
        0x9,
        (
            "#140Fほ哦，还真是敏锐啊。\x02\x03",
            "实际上，派人去外国\x01",
            "寻找合适的候选人的，\x01",
            "是那个理查德上校呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F果然是……\x02\x03",
            "但是……这不是很奇怪吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE12")

    label("loc_AE12")


    ChrTalk(
        0x101,
        (
            "#000F为什么会是理查德上校\x01",
            "来寻找公主的结婚对象呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F所以我说，\x01",
            "到处充满了可疑的气味呢。\x02\x03",
            "所以说……\x01",
            "有件事情想拜托你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F——如果明天的比赛能获胜，\x01",
            "被招待进城参加晚餐会的话，\x01",
            "打听一下这方面的情报。\x02\x03",
            "是这样没错吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，是这样啊……\x02\x03",
            "真是的，\x01",
            "不过确实告诉我们很多事情呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F我调查到的只有这些了。\x01",
            "Give&take是理所当然的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F确实帮了我们很多忙呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F没办法呢～\x01",
            "如果知道了什么，就告诉你吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F嘿，早这样说不就好了。\x02\x03",
            "不过，就算不拜托你们，\x01",
            "运气好的话今天也能……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    OP_44(0x9, 0xFF)
    OP_8E(0x9, 0xFFFF2630, 0x0, 0xFBCB, 0xBB8, 0x0)

    ChrTalk(
        0x9,
        (
            "#140F喂。\x01",
            "这里是利贝尔通讯社……\x02\x03",
            "哦，是你啊！\x01",
            "我一直在等你的联络呢。\x02\x03",
            "什么……现在就？\x02\x03",
            "啊，知道了。\x01",
            "我立刻过去找你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F怎么，发生什么事情了？\x02",
    )

    CloseMessageWindow()
    OP_8E(0x9, 0xFFFF1F6E, 0x0, 0xFB9A, 0xBB8, 0x0)
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(
        0x9,
        (
            "#140F稍微有点私事。\x01",
            "现在要去和别人会面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F很重要的事吗。\x01",
            "太阳已经下山了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F本来我就是夜猫子啊。\x02\x03",
            "因为要带那个我行我素的丫头\x01",
            "进行新人研修，\x01",
            "才改变成白天型的了……\x02\x03",
            "唉，不说这件事情了。\x02\x03",
            "我要出去了，\x01",
            "你们接着干你们的事情吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，明白了。\x02\x03",
            "要加油工作哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F你们也是，明天的比赛，\x01",
            "一定不能输啊！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B274():

        label("loc_B274")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_B274")

    QueueWorkItem2(0x101, 1, lambda_B274)

    def lambda_B285():

        label("loc_B285")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_B285")

    QueueWorkItem2(0x102, 1, lambda_B285)
    OP_8E(0x9, 0xFFFF1B9A, 0x0, 0xFF14, 0xBB8, 0x0)
    OP_8E(0x9, 0xFFFF1564, 0x0, 0xFF14, 0xBB8, 0x0)
    OP_8E(0x9, 0xFFFF1258, 0x0, 0x1039C, 0xBB8, 0x0)
    OP_8E(0x9, 0xFFFF0736, 0x0, 0x1039C, 0xBB8, 0x0)
    OP_8E(0x9, 0xFFFF0736, 0xFFFFF74A, 0xF406, 0xBB8, 0x0)
    SetChrFlags(0x9, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F嗯……\x01",
            "我们该怎么办呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F是呀……\x01",
            "总之，先顺路去协会，\x01",
            "然后就回旅馆吧。\x02\x03",
            "最好把奈尔先生调查到的情报\x01",
            "向协会报告一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，明白。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_32_9C30 end

    def Function_33_B3AF(): pass

    label("Function_33_B3AF")

    EventBegin(0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -56250, 0, 60940, 90)
    SetChrPos(0x101, -60190, 0, 65280, 135)
    SetChrPos(0x102, -61190, 0, 64849, 135)
    SetChrPos(0x108, -60700, 0, 66190, 135)
    OP_6D(-54490, 0, 61730, 0)

    ChrTalk(
        0xA,
        (
            "#150F主编，真的好奇怪～\x02\x03",
            "已经两天没有取得联络了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "嗯，我想他是沉浸\x01",
            "在寻找独家新闻\x01",
            "的美梦中了吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "不过在这个戒严时期\x01",
            "不能取得联系的确有些奇怪……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    ChrTalk(
        0xB,
        "咦……\x02",
    )

    CloseMessageWindow()

    def lambda_B4DB():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B4DB)
    OP_6D(-56640, 0, 63970, 2000)

    ChrTalk(
        0xA,
        "#150F啊，小艾你们来了！\x02",
    )

    CloseMessageWindow()

    def lambda_B517():

        label("loc_B517")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_B517")

    QueueWorkItem2(0xA, 1, lambda_B517)

    def lambda_B528():

        label("loc_B528")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_B528")

    QueueWorkItem2(0x101, 1, lambda_B528)

    def lambda_B539():

        label("loc_B539")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_B539")

    QueueWorkItem2(0x102, 1, lambda_B539)

    def lambda_B54A():

        label("loc_B54A")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_B54A")

    QueueWorkItem2(0x108, 1, lambda_B54A)

    def lambda_B55B():
        OP_8E(0xFE, 0xFFFF2AF4, 0x0, 0xF532, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B55B)
    Sleep(100)

    def lambda_B57B():
        OP_8E(0xFE, 0xFFFF26EE, 0x0, 0xF51E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B57B)
    Sleep(300)

    def lambda_B59B():
        OP_8E(0xFE, 0xFFFF22D4, 0x0, 0xF4EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_B59B)
    OP_6D(-54340, 0, 62290, 3000)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)

    ChrTalk(
        0xB,
        "哦，武术大会的优胜者……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "本人就是\x01",
            "《利贝尔通讯》的总编。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "我从奈尔和朵洛希那里\x01",
            "听说过你们的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "你们二位是游击士协会的\x01",
            "艾丝蒂尔和约修亚吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，您好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F初次见面，请多关照。\x02\x03",
            "《利贝尔通讯》的每一期\x01",
            "都给我们带来了不少乐趣呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "哈哈哈。\x01",
            "听你这么说我很高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "对了，你们\x01",
            "是来找奈尔的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，是的，可以这么说……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "是你们啊……\x01",
            "你总算来啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F你好，打扰了～\x02\x03",
            "我们是来找奈尔的，\x01",
            "难道他出去了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "我们刚才正在\x01",
            "谈起这件事请呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "事实上奈尔他昨天和今天\x01",
            "都没有到编辑部来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "完全不能和他取得联络。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F昨天和今天都……\x02\x03",
            "我们前天傍晚\x01",
            "还在这里和奈尔先生\x01",
            "商讨事情……\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xA, 0xFF)
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(
        0xA,
        "#150F真、真的吗～！？\x02",
    )

    CloseMessageWindow()

    def lambda_B88F():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B88F)
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(
        0x101,
        (
            "#000F什么真的假的呀，给奈尔捎口信\x01",
            "的不就是朵洛希你吗。\x02\x03",
            "半决赛之后，\x01",
            "让我们到这里来向他打听情报。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#150F啊－我想起来了，\x01",
            "是那件事情－啊。\x02\x03",
            "请问，奈尔前辈\x01",
            "那时是怎么说的呢～？\x02\x03",
            "他到哪里去了呢～\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "去收集新闻了\x01",        # 0
            "有人叫他出去\x01",        # 1
            "一起去吃晚餐了\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B9E6"),
        (1, "loc_BA63"),
        (2, "loc_BAB4"),
        (SWITCH_DEFAULT, "loc_BB26"),
    )


    label("loc_B9E6")


    ChrTalk(
        0x102,
        (
            "#010F嗯，很有可能是去\x01",
            "外面收集新闻了……\x02\x03",
            "事实上当时有人叫他出去，\x01",
            "于是他可能到某个地方去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，是这样。\x02",
    )

    CloseMessageWindow()
    Jump("loc_BB26")

    label("loc_BA63")


    ChrTalk(
        0x102,
        (
            "#010F啊，的确是那样的呢。\x02\x03",
            "当时有人叫他出去，\x01",
            "于是他可能到某个地方去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BB26")

    label("loc_BAB4")


    ChrTalk(
        0x102,
        (
            "#010F不，那是３天前的事情了。\x02\x03",
            "２天前的傍晚奈尔先生\x01",
            "是被某个人用通信器叫出去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，是这样吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_BB26")

    label("loc_BB26")


    ChrTalk(
        0xB,
        "你们说的是真的吗？\x02",
    )

    CloseMessageWindow()

    def lambda_BB44():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BB44)
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(
        0x102,
        (
            "#010F嗯。\x02\x03",
            "大概这就是为何从那时开始\x01",
            "到现在为止他都没有消息的原因吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#150F怎、怎么会！\x01",
            "前辈你不能死啊～！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(
        0x101,
        (
            "#000F哎，不要说那些\x01",
            "莫名其妙的话！\x02\x03",
            "从今天开始定期船\x01",
            "也停止航行了……\x02\x03",
            "到昨天为止还是在航行的，\x01",
            "他会不会到别的地方去了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "已经到飞艇坪看过了，\x01",
            "在登艇名单上没有记载。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BC85():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BC85)

    def lambda_BC93():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_BC93)

    ChrTalk(
        0xB,
        (
            "也就是说他应该\x01",
            "还在王都这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F嗯……\x02\x03",
            "你们俩在和那个记者\x01",
            "最后一次见面的时候……\x02\x03",
            "那个名叫奈尔的记者\x01",
            "不是提起过，说他得到\x01",
            "了什么新闻材料吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BD3C():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_BD3C)

    def lambda_BD4A():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BD4A)
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(
        0x101,
        "#000F哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F现在这种局势。\x02\x03",
            "大众传媒也被\x01",
            "军队所管制吧。\x02\x03",
            "对吗，主编先生？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "是啊，的确如此呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "特别是围绕情报部的话题，\x01",
            "正处于被拼命的审批的状态。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "一时的气话而已，你们别放在心上。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F……在这种状况下，\x01",
            "可以报道的新闻自然就少了。\x02\x03",
            "可是，作为一个记者，\x01",
            "哪怕是有一点新的消息，\x01",
            "都想尽快传达给读者。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F原来如此……\x02\x03",
            "情报部的管制不成问题，\x01",
            "以新的具有话题性的消息为重……\x02\x03",
            "关于这个，奈尔先生\x01",
            "曾经是提起过什么的对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，对了……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "武术大会优胜者的相关事宜\x01",          # 0
            "科洛蒂亚公主婚姻的相关事宜\x01",        # 1
            "尤莉亚和凯诺娜过去的相关事宜\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_BFDD"),
        (1, "loc_C111"),
        (2, "loc_C13E"),
        (SWITCH_DEFAULT, "loc_C272"),
    )


    label("loc_BFDD")


    ChrTalk(
        0x108,
        (
            "#070F要把这个作为新闻的话，\x01",
            "也应该是在我们取得优胜之前的事情。\x02\x03",
            "作为现在的新的消息就不太行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F是吗……\x02\x03",
            "的确，因为特务兵他们\x01",
            "还是有可能取胜的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F……还有一个线索。\x02\x03",
            "奈尔先生对科洛蒂亚公主\x01",
            "的婚姻问题似乎很有兴趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊……没错！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F哦，晚宴的时候\x01",
            "公爵所说的话……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C272")

    label("loc_C111")


    ChrTalk(
        0x108,
        (
            "#070F哦，晚宴的时候\x01",
            "公爵所说的话……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C272")

    label("loc_C13E")


    ChrTalk(
        0x108,
        (
            "#070F情报部的才女和\x01",
            "和逃亡中的女亲卫队员\x01",
            "在士官学校里是对手……\x02\x03",
            "虽然很有趣，不过对于情报部来说\x01",
            "这种事情允许取材吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，确实……\x01",
            "不能作为报道呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F……还有一个线索。\x02\x03",
            "奈尔先生对科洛蒂亚公主\x01",
            "的婚姻问题似乎很有兴趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊……没错！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F哦，晚宴的时候\x01",
            "公爵所说的话……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C272")

    label("loc_C272")


    ChrTalk(
        0xB,
        (
            "什么，奈尔和你们\x01",
            "谈到了这件事。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C29D():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C29D)

    def lambda_C2AB():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C2AB)

    ChrTalk(
        0xB,
        (
            "如果是真的，\x01",
            "那就是个爆炸性的新闻啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "总算是可以获取\x01",
            "一些内幕了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F那个叫奈尔的记者\x01",
            "怎么会知道这些事情？\x02\x03",
            "不是说与王室无关\x01",
            "的人员都不知道这个情报的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#150F他可能是从那个在艾尔贝离宫\x01",
            "工作的朋友那里听说的吧。\x02\x03",
            "还有一个不能报道的消息，公主殿下\x01",
            "也被恐怖分子作为目标了～\x02\x03",
            "因此公主殿下在艾尔贝离宫\x01",
            "里面被秘密保护了起来～\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_C457():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C457)

    def lambda_C465():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C465)

    def lambda_C473():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_C473)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#000F……果然！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F呵呵呵，\x01",
            "得来全不费工夫啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F难道那天叫奈尔出去的\x01",
            "就是他在离宫里面工作的朋友吗……\x02\x03",
            "这样一来奈尔先生在离宫\x01",
            "的可能性就很高了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "是、是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "也许奈尔为了\x01",
            "去采访公主殿下，\x01",
            "强行潜入了离宫……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "然后被士兵发现了，\x01",
            "抓了起来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#150F呜～哇！\x01",
            "奈尔前辈死定了～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F这样才不会死呢……\x02\x03",
            "但是，如果这是事实，\x01",
            "他是不会被轻易释放的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯……\x02\x03",
            "他和科洛蒂娅公主站在\x01",
            "同样立场的可能性比较高。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "你们是……\x01",
            "你们究竟知道了什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "在这个王都……不，\x01",
            "在利贝尔究竟发生了什么事，\x01",
            "你们不会是知道什么吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C6B8():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C6B8)
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(
        0x101,
        (
            "#000F唔－嗯，对不起。\x01",
            "请恕我们无可奉告。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F奈尔先生的事情，\x01",
            "请交给我们游击士协会去办。\x02\x03",
            "如果的确是被拘捕了，\x01",
            "那我们一定会把他解救出来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "太好了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "我明白了，拜托你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#150F啊，拜托了～！\x01",
            "小艾～！\x02\x03",
            "一定要救救奈尔前辈～！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(
        0x101,
        "#000F嗯，交给我们吧！\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_33_B3AF end

    def Function_34_C7E9(): pass

    label("Function_34_C7E9")

    EventBegin(0x0)
    OP_6D(-53660, 0, 62750, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(33000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xA, -59130, 0, 59600, 0)
    SetChrPos(0x9, -53500, 0, 62630, 90)
    OP_6D(-54490, 0, 61730, 0)

    ChrTalk(
        0x9,
        (
            "#140F嘁……\x01",
            "终于开始了吗！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C890():
        OP_6D(-56110, 0, 62480, 1000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_C890)
    OP_8E(0x9, 0xFFFF2400, 0x0, 0xF44C, 0xBB8, 0x0)
    TurnDirection(0x9, 0xA, 400)

    ChrTalk(
        0x9,
        (
            "#140F出发，朵洛希！\x02\x03",
            "必须要确保找到\x01",
            "可以从远处眺望这场战斗的最佳位置！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#150F等、等一下好吗～！\x02\x03",
            "感光回路马上就可以\x01",
            "设置好了的呀～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "喂喂，到底是怎么回事啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "这三天来你去哪里旅游了啊……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xB, 400)

    ChrTalk(
        0x9,
        (
            "#140F这可是独家新闻！\x02\x03",
            "『利贝尔通讯社』建社以来\x01",
            " 前所未有过的独家新闻啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4240   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_34_C7E9 end

    SaveToFile()

Try(main)
