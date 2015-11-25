from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4122   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4122.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        '亚妮拉丝',                             # 9
        '卡露娜',                               # 10
        '莉莉',                                 # 11
        '丹顿',                                 # 12
        '基蒂',                                 # 13
        '希娜',                                 # 14
        '特雷诺',                               # 15
        '索菲娜',                               # 16
        '卡拉',                                 # 17
        '卢希娅',                               # 18
        '朵洛希',                               # 19
        '艾德尔店长',                           # 20
        '菲尔妲',                               # 21
        '莎夏',                                 # 22
        '鲁特尔',                               # 23
        '雪拉扎德',                             # 24
        '管家菲利普',                           # 25
        '蜜蒂',                                 # 26
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
        'ED6_DT07/CH01630 ._CH',             # 00
        'ED6_DT07/CH01240 ._CH',             # 01
        'ED6_DT07/CH01150 ._CH',             # 02
        'ED6_DT07/CH01020 ._CH',             # 03
        'ED6_DT07/CH01770 ._CH',             # 04
        'ED6_DT07/CH01130 ._CH',             # 05
        'ED6_DT07/CH01120 ._CH',             # 06
        'ED6_DT07/CH01690 ._CH',             # 07
        'ED6_DT07/CH01030 ._CH',             # 08
        'ED6_DT07/CH01070 ._CH',             # 09
        'ED6_DT07/CH02070 ._CH',             # 0A
        'ED6_DT07/CH01210 ._CH',             # 0B
        'ED6_DT07/CH01290 ._CH',             # 0C
        'ED6_DT07/CH01540 ._CH',             # 0D
        'ED6_DT07/CH01020 ._CH',             # 0E
        'ED6_DT07/CH00020 ._CH',             # 0F
        'ED6_DT07/CH02470 ._CH',             # 10
    )

    AddCharChipPat(
        'ED6_DT07/CH01630P._CP',             # 00
        'ED6_DT07/CH01240P._CP',             # 01
        'ED6_DT07/CH01150P._CP',             # 02
        'ED6_DT07/CH01020P._CP',             # 03
        'ED6_DT07/CH01770P._CP',             # 04
        'ED6_DT07/CH01130P._CP',             # 05
        'ED6_DT07/CH01120P._CP',             # 06
        'ED6_DT07/CH01690P._CP',             # 07
        'ED6_DT07/CH01030P._CP',             # 08
        'ED6_DT07/CH01070P._CP',             # 09
        'ED6_DT07/CH02070P._CP',             # 0A
        'ED6_DT07/CH01210P._CP',             # 0B
        'ED6_DT07/CH01290P._CP',             # 0C
        'ED6_DT07/CH01540P._CP',             # 0D
        'ED6_DT07/CH01020P._CP',             # 0E
        'ED6_DT07/CH00020P._CP',             # 0F
        'ED6_DT07/CH02470P._CP',             # 10
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = 8790,
        Z                   = 0,
        Y                   = 10500,
        Direction           = 196,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 12170,
        Z                   = 0,
        Y                   = -4050,
        Direction           = 163,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = -13610,
        Z                   = 250,
        Y                   = 11140,
        Direction           = 182,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = -12600,
        Z                   = 0,
        Y                   = 6400,
        Direction           = 9,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 13600,
        Z                   = 0,
        Y                   = -8480,
        Direction           = 91,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -8770,
        Z                   = 0,
        Y                   = -8610,
        Direction           = 21,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 410,
        Z                   = 0,
        Y                   = 3810,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 2650,
        Z                   = 0,
        Y                   = 3210,
        Direction           = 106,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 9980,
        Z                   = 0,
        Y                   = 6170,
        Direction           = 87,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -50,
        Z                   = 0,
        Y                   = 10,
        Direction           = 204,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -1440,
        Z                   = 0,
        Y                   = 65550,
        Direction           = 179,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 1970,
        Z                   = 0,
        Y                   = 65550,
        Direction           = 175,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -950,
        Z                   = 0,
        Y                   = 60990,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 8850,
        Z                   = 0,
        Y                   = -10950,
        Direction           = 282,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -10430,
        Z                   = 0,
        Y                   = 9410,
        Direction           = 178,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -4540,
        Z                   = 0,
        Y                   = 9850,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )


    DeclActor(
        TriggerX            = 8450,
        TriggerZ            = 0,
        TriggerY            = 8650,
        TriggerRange        = 800,
        ActorX              = 8790,
        ActorZ              = 1500,
        ActorY              = 10500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 24,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 11970,
        TriggerZ            = 0,
        TriggerY            = -5950,
        TriggerRange        = 800,
        ActorX              = 12170,
        ActorZ              = 1500,
        ActorY              = -4050,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 22,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -6400,
        TriggerZ            = 0,
        TriggerY            = 9620,
        TriggerRange        = 800,
        ActorX              = -4540,
        ActorZ              = 1500,
        ActorY              = 9850,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1370,
        TriggerZ            = 0,
        TriggerY            = 63610,
        TriggerRange        = 800,
        ActorX              = -1440,
        ActorZ              = 1500,
        ActorY              = 65550,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1850,
        TriggerZ            = 0,
        TriggerY            = 63640,
        TriggerRange        = 800,
        ActorX              = 1970,
        ActorZ              = 1500,
        ActorY              = 65550,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_426",          # 00, 0
        "Function_1_6CE",          # 01, 1
        "Function_2_727",          # 02, 2
        "Function_3_73D",          # 03, 3
        "Function_4_761",          # 04, 4
        "Function_5_785",          # 05, 5
        "Function_6_9FE",          # 06, 6
        "Function_7_C4E",          # 07, 7
        "Function_8_D76",          # 08, 8
        "Function_9_D7B",          # 09, 9
        "Function_10_1205",        # 0A, 10
        "Function_11_120A",        # 0B, 11
        "Function_12_1A6E",        # 0C, 12
        "Function_13_1EC4",        # 0D, 13
        "Function_14_1F81",        # 0E, 14
        "Function_15_21FC",        # 0F, 15
        "Function_16_268F",        # 10, 16
        "Function_17_28E6",        # 11, 17
        "Function_18_2CA9",        # 12, 18
        "Function_19_3076",        # 13, 19
        "Function_20_307B",        # 14, 20
        "Function_21_354F",        # 15, 21
        "Function_22_416B",        # 16, 22
        "Function_23_4170",        # 17, 23
        "Function_24_499C",        # 18, 24
        "Function_25_49A1",        # 19, 25
        "Function_26_4F1A",        # 1A, 26
        "Function_27_4FEC",        # 1B, 27
    )


    def Function_0_426(): pass

    label("Function_0_426")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_448")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 10500, 0, 5390, 90)

    label("loc_448")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_4AF")
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 8850, 0, -10160, 259)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 4100, 0, -10830, 100)
    OP_43(0x8, 0x0, 0x0, 0x2)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0xE, 2470, 0, -3790, 78)
    Jump("loc_6CD")

    label("loc_4AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_4EA")
    SetChrPos(0xD, -11310, 0, 6390, 355)
    SetChrPos(0xE, 13600, 0, -11620, 107)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_6CD")

    label("loc_4EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_520")
    SetChrPos(0xD, -13220, 0, 9430, 198)
    SetChrPos(0xE, 13600, 0, -7380, 82)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    Jump("loc_6CD")

    label("loc_520")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_578")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 2890, 0, 3290, 87)
    OP_43(0x8, 0x0, 0x0, 0x2)
    SetChrPos(0xD, -8740, 0, 9410, 165)
    SetChrPos(0xE, 5870, 0, -10820, 272)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    Jump("loc_6CD")

    label("loc_578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_5B8")
    SetChrPos(0xD, -10560, 0, 9490, 200)
    SetChrPos(0xE, 4480, 0, -6130, 340)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_6CD")

    label("loc_5B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_60B")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 5000, 0, 1510, 0)
    OP_43(0x8, 0x0, 0x0, 0x2)
    SetChrPos(0xD, -8890, 0, 6200, 349)
    SetChrPos(0xE, 13580, 0, -11020, 70)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_6CD")

    label("loc_60B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_641")
    SetChrPos(0xD, -7480, 0, 4300, 104)
    SetChrPos(0xE, 4480, 0, -6130, 340)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_6CD")

    label("loc_641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_661")
    SetChrPos(0xD, -7480, 0, 4300, 104)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_6CD")

    label("loc_661")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_686")
    SetChrPos(0xD, -12210, 250, 11380, 355)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_6CD")

    label("loc_686")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_6BC")
    SetChrPos(0xD, -11310, 0, 6390, 355)
    SetChrPos(0xE, 13580, 0, -11020, 70)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x16, 0x80)
    Jump("loc_6CD")

    label("loc_6BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_6CD")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x16, 0x80)

    label("loc_6CD")

    Return()

    # Function_0_426 end

    def Function_1_6CE(): pass

    label("Function_1_6CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_701")
    OP_B1("t4122_y")
    Jump("loc_70A")

    label("loc_701")

    OP_B1("t4122_n")

    label("loc_70A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_71A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_71A")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_6CE end

    def Function_2_727(): pass

    label("Function_2_727")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_73C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_727")

    label("loc_73C")

    Return()

    # Function_2_727 end

    def Function_3_73D(): pass

    label("Function_3_73D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_760")
    OP_8D(0xFE, -12460, -5460, -5830, -11220, 3000)
    Jump("Function_3_73D")

    label("loc_760")

    Return()

    # Function_3_73D end

    def Function_4_761(): pass

    label("Function_4_761")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_784")
    OP_8D(0xFE, 2190, 5370, 2900, 2580, 3000)
    Jump("Function_4_761")

    label("loc_784")

    Return()

    # Function_4_761 end

    def Function_5_785(): pass

    label("Function_5_785")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_7F4")

    ChrTalk(
        0x18,
        (
            "#720F殿下虚心地接受了\x01",
            "陛下严厉的训斥和教育。\x01",
            "　\x02\x03",
            "现在正在艾尔贝离宫的房间里面深刻地反省。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9FA")

    label("loc_7F4")

    OP_A2(0x10)

    ChrTalk(
        0x101,
        "#004F哎呀，是菲利普先生。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#720F……这、这不是\x01",
            "艾丝蒂尔小姐和约修亚先生吗。\x02\x03",
            "#722F前些日子由于我的教导无方，\x01",
            "殿下给你们添了不少麻烦，实在是抱歉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F说起来，\x01",
            "杜南公爵现在到哪里去了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#720F哦，殿下虚心地接受了\x01",
            "陛下严厉的训斥和教育。\x01",
            "　\x02\x03",
            "现在正在艾尔贝离宫的房间里面深刻地反省。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哦，是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F那么菲利普先生今天来王都做什么呢？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#722F啊，实、实际上\x01",
            "是殿下叫我来帮他买炸面圈的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F呵，呵～呵……\x02\x03",
            "（真的是在反省吗？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F（可能还是老样子吧。）\x02",
    )

    CloseMessageWindow()

    label("loc_9FA")

    TalkEnd(0xFE)
    Return()

    # Function_5_785 end

    def Function_6_9FE(): pass

    label("Function_6_9FE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_A8F")

    ChrTalk(
        0x17,
        (
            "#020F等回了洛连特之后，\x01",
            "大家一起去逛街购物吧。\x01",
            "已经很久没有去了呢。\x02\x03",
            "作为对你成为正游击士的奖赏，\x01",
            "我会给你买一些好看的衣服哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C4A")

    label("loc_A8F")

    OP_A2(0xF)
    OP_A2(0x6EC)

    ChrTalk(
        0x17,
        "#023F哎呀，是你们两个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F雪拉姐，你在做什么呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#020F呵呵，偶尔也和同伴们\x01",
            "来享受一下购物的乐趣嘛。\x02\x03",
            "好不容易才有这样的机会呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F对了，\x01",
            "小时候雪拉姐就经常\x01",
            "带着我们去买东西呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#021F是啊，老师外出时\x01",
            "我们还时常三个人一起去呢。\x02\x03",
            "#020F怎么样？\x01",
            "等回了洛连特之后，\x01",
            "大家一起去逛街购物吧？\x02\x03",
            "作为对你成为正游击士的奖赏，\x01",
            "我会给你买一些好看的衣服哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F啊，真的吗？\x01",
            "我要去我要去！\x02\x03",
            "雪拉姐，就这么定了哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C4A")

    TalkEnd(0xFE)
    Return()

    # Function_6_9FE end

    def Function_7_C4E(): pass

    label("Function_7_C4E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_C5B")
    Jump("loc_D72")

    label("loc_C5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_C65")
    Jump("loc_D72")

    label("loc_C65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_C6F")
    Jump("loc_D72")

    label("loc_C6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_C79")
    Jump("loc_D72")

    label("loc_C79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_C83")
    Jump("loc_D72")

    label("loc_C83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_C8D")
    Jump("loc_D72")

    label("loc_C8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_C97")
    Jump("loc_D72")

    label("loc_C97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_CA1")
    Jump("loc_D72")

    label("loc_CA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_CAB")
    Jump("loc_D72")

    label("loc_CAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_D15")

    ChrTalk(
        0xFE,
        (
            "一个个的事件相继发生，\x01",
            "让飞艇公社也变得很辛苦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样下去，\x01",
            "现在想要谈买卖都很困难了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D72")

    label("loc_D15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_D72")

    ChrTalk(
        0xFE,
        (
            "呼……\x01",
            "终于到达格兰赛尔了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "由于王国军盘查的缘故，\x01",
            "到达的时间推迟了很久呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D72")

    TalkEnd(0xFE)
    Return()

    # Function_7_C4E end

    def Function_8_D76(): pass

    label("Function_8_D76")

    Call(0, 9)
    Return()

    # Function_8_D76 end

    def Function_9_D7B(): pass

    label("Function_9_D7B")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_DBE")

    ChrTalk(
        0x15,
        (
            "这下乘客们\x01",
            "可以放心地享受\x01",
            "愉快舒适的空中旅行了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1201")

    label("loc_DBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_E0D")

    ChrTalk(
        0x15,
        "真叫人难办啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "处于现在这种休业状态，\x01",
            "什么事情也不能做。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1201")

    label("loc_E0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_E61")

    ChrTalk(
        0x15,
        (
            "乘客们都\x01",
            "纷纷回来退票了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "既然不能搭乘定期船，\x01",
            "退票也是应该的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1201")

    label("loc_E61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_E98")

    ChrTalk(
        0x15,
        (
            "武术大会能顺利结束，\x01",
            "这可比什么都好呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1201")

    label("loc_E98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_F01")

    ChrTalk(
        0x15,
        "今天是武术大会的最后一天吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "虽说之前发生了恐怖事件，\x01",
            "不过今年的武术大会还是很热闹。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1201")

    label("loc_F01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1046")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_F89")

    ChrTalk(
        0x15,
        (
            "修理员佩顿师傅是专门负责\x01",
            "『埃尔赛尤号』的修理工作的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "自从发生政变以来，\x01",
            "飞船就被军方接管，\x01",
            "很是让他郁闷呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1043")

    label("loc_F89")

    OP_A2(0xD)

    ChrTalk(
        0x15,
        (
            "修理员佩顿师傅是专门负责\x01",
            "『埃尔赛尤号』的修理工作的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "自从发生政变以来，\x01",
            "飞船就被军方接管，\x01",
            "很是让他郁闷呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "那艘飞艇\x01",
            "以前是由亲卫队在使用，\x01",
            "本来就是王家的御用飞艇呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1043")

    Jump("loc_1201")

    label("loc_1046")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_10C1")

    ChrTalk(
        0x15,
        (
            "因为『埃尔赛尤号』的缘故，\x01",
            "我和亲卫队的人\x01",
            "经常有谈话的机会……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "他们虽然有些保守，\x01",
            "但都是很认真的人呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1201")

    label("loc_10C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1105")

    ChrTalk(
        0x15,
        (
            "只要不是紧急事态，\x01",
            "军队就不应该占用\x01",
            "定期船的航线……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1201")

    label("loc_1105")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1149")

    ChrTalk(
        0x15,
        (
            "这个时期为了\x01",
            "武术大会和诞辰庆典\x01",
            "而来的旅客果然很多。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1201")

    label("loc_1149")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_11DC")

    ChrTalk(
        0x15,
        (
            "为了配合诞辰庆典，\x01",
            "公社本来准备了\x01",
            "许多的活动议程。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "但是接二连三的发生了这些事件，\x01",
            "可能就不会按原计划执行了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "真可惜……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1201")

    label("loc_11DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1201")

    ChrTalk(
        0x15,
        "欢迎来到利贝尔飞艇公社。\x02",
    )

    CloseMessageWindow()

    label("loc_1201")

    TalkEnd(0x15)
    Return()

    # Function_9_D7B end

    def Function_10_1205(): pass

    label("Function_10_1205")

    Call(0, 11)
    Return()

    # Function_10_1205 end

    def Function_11_120A(): pass

    label("Function_11_120A")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1331")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_128C")

    ChrTalk(
        0x14,
        (
            "这个空港曾一度被封锁，\x01",
            "竟然是为了便于发动政变。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "如果早知道是这样，\x01",
            "才不会那么轻易就让它被封锁住呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_132E")

    label("loc_128C")

    OP_A2(0xC)

    ChrTalk(
        0x14,
        (
            "这个空港曾一度被封锁，\x01",
            "竟然是为了便于发动政变。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "如果早知道是这样，\x01",
            "才不会那么轻易就让它被封锁住呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "不管怎么说，\x01",
            "终归还是平安地迎来了诞辰庆典。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_132E")

    Jump("loc_1A6A")

    label("loc_1331")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_13C3")

    ChrTalk(
        0x14,
        (
            "说起来，\x01",
            "前不久有一位修女\x01",
            "去拜访了修理员佩顿师傅……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "难道说他因为『埃尔赛尤号』\x01",
            "被军队带走而受了打击，\x01",
            "准备出家做修道士了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A6A")

    label("loc_13C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1435")

    ChrTalk(
        0x14,
        "唉……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "空港再一次被\x01",
            "王国军给封锁了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "他们做得也有些太过分了吧。\x01",
            "不知道什么叫适可而止吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A6A")

    label("loc_1435")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_14B0")

    ChrTalk(
        0x14,
        (
            "今天王城里的晚宴，\x01",
            "公爵邀请的都是像\x01",
            "各地市长这样有权有势的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "如果这时出现恐怖袭击，\x01",
            "那该怎么办啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A6A")

    label("loc_14B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_152F")

    ChrTalk(
        0x14,
        (
            "托柏斯的空贼事件和\x01",
            "王国军最近封锁政策的福，\x01",
            "公社这个财政季度又是大赤字了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "最近就没有什么\x01",
            "好一点的消息吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A6A")

    label("loc_152F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1671")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_15C4")

    ChrTalk(
        0x14,
        (
            "因为看守『埃尔赛尤号』\x01",
            "也是要重点加强的工作，\x01",
            "军方还说要我们帮他们的忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "不过即使协助军方，\x01",
            "他们也不会给公社\x01",
            "任何补贴吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_166E")

    label("loc_15C4")

    OP_A2(0xC)

    ChrTalk(
        0x14,
        (
            "军方似乎加强了\x01",
            "大街上的警戒。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "因为看守『埃尔赛尤号』\x01",
            "也是要重点加强的工作，\x01",
            "军方还说要我们帮他们的忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "不过即使协助军方，\x01",
            "他们也不会给公社\x01",
            "任何补贴吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_166E")

    Jump("loc_1A6A")

    label("loc_1671")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1783")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_16EA")

    ChrTalk(
        0x14,
        (
            "其他地区的市民还不是很清楚\x01",
            "女王陛下身体欠佳的事情吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "所以仍然有很多人\x01",
            "为了诞辰庆典来到王都。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1780")

    label("loc_16EA")

    OP_A2(0xC)

    ChrTalk(
        0x14,
        (
            "其他地区的市民还不是很清楚\x01",
            "女王陛下身体欠佳的事情吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "所以仍然有很多人\x01",
            "为了诞辰庆典来到王都。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "不过，\x01",
            "就算在这里抱怨也无济于事啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1780")

    Jump("loc_1A6A")

    label("loc_1783")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1804")

    ChrTalk(
        0x14,
        (
            "因为王国军\x01",
            "强行占用各地的飞艇坪，\x01",
            "定期船运行时刻表都被打乱了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "之前也是因为军队的行动\x01",
            "而导致航班一推再推……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A6A")

    label("loc_1804")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_18AD")

    ChrTalk(
        0x14,
        (
            "在武术大会和诞辰庆典期间，\x01",
            "与乘定期船外出的旅客数量相比，\x01",
            "抵达这里的旅客要更多一些。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "抱怨的人和迷路的人也相应增多，\x01",
            "必须要以饱满的精神来应对才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A6A")

    label("loc_18AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_194B")

    ChrTalk(
        0x14,
        (
            "空港里除了定期船，\x01",
            "还有其他的飞艇停泊在这里，\x01",
            "比如『埃尔赛尤号』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "原本这是亲卫队使用的飞艇，\x01",
            "但自从政变发生之后，\x01",
            "就由王国军代为保管了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A6A")

    label("loc_194B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1A6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_19C6")

    ChrTalk(
        0x14,
        (
            "因为王国军的盘查，\x01",
            "原定的航行时刻表被搅乱得一塌糊涂。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "哎呀，真希望乘客们\x01",
            "能够理解我们的难处啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A6A")

    label("loc_19C6")

    OP_A2(0xC)

    ChrTalk(
        0x14,
        (
            "因为王国军的盘查，\x01",
            "原定的航行时刻表被搅乱得一塌糊涂。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "哎呀，真希望乘客们\x01",
            "能够理解我们的难处啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "我们又没有什么过错，\x01",
            "为何还一定要去赔礼道歉呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A6A")

    TalkEnd(0x14)
    Return()

    # Function_11_120A end

    def Function_12_1A6E(): pass

    label("Function_12_1A6E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1B2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_1ACD")

    ChrTalk(
        0xFE,
        (
            "本店现在正在\x01",
            "举行诞辰庆典的降价酬宾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "一定要好好把握这个机会哦～\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B2B")

    label("loc_1ACD")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        "欢迎光临～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本店现在正在\x01",
            "举行诞辰庆典的降价酬宾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "一定要好好把握这个机会哦～\x02",
    )

    CloseMessageWindow()

    label("loc_1B2B")

    Jump("loc_1EC0")

    label("loc_1B2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1B9C")

    ChrTalk(
        0xFE,
        (
            "诞辰庆典当天的\x01",
            "纪念减价销售正在计划中哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然现在的状况不容乐观，\x01",
            "但还是得提前做好准备。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EC0")

    label("loc_1B9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1BA6")
    Jump("loc_1EC0")

    label("loc_1BA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1BB0")
    Jump("loc_1EC0")

    label("loc_1BB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1CA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_1C08")

    ChrTalk(
        0xFE,
        (
            "本店的特点就是对商品进行比较和甄选，\x01",
            "尽量为客人提供最优质的商品。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C9F")

    label("loc_1C08")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "柏斯超市里\x01",
            "虽说什么类型的商店都有，\x01",
            "不过那里充满活力而又秩序井然。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "保持现状难以取胜，\x01",
            "我们的百货店也要发展\x01",
            "我们自己独特的经营的路线才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C9F")

    Jump("loc_1EC0")

    label("loc_1CA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1CAC")
    Jump("loc_1EC0")

    label("loc_1CAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1E0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_1D3E")

    ChrTalk(
        0xFE,
        (
            "这样下去的话，\x01",
            "就算本店在格兰赛尔一家独大，\x01",
            "也难以在利贝尔王国成为顶尖。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "诞辰庆典结束之后，\x01",
            "就和员工们一起去柏斯研修！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E0C")

    label("loc_1D3E")

    OP_A2(0xB)

    ChrTalk(
        0xFE,
        (
            "这样下去的话，\x01",
            "就算本店在格兰赛尔一家独大，\x01",
            "也难以在利贝尔王国成为顶尖。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……好的，决定了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "诞辰庆典结束之后，\x01",
            "和员工们一起去柏斯研修！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "要知己知彼才行呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "当然也要顺便购购物啦！\x02",
    )

    CloseMessageWindow()

    label("loc_1E0C")

    Jump("loc_1EC0")

    label("loc_1E0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1E19")
    Jump("loc_1EC0")

    label("loc_1E19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1EAF")

    ChrTalk(
        0xFE,
        (
            "好～的，鼓足干劲吧。\x01",
            "目标是打倒柏斯超市哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在和丈夫一起旅行时，\x01",
            "我对各地的商店进行了研究。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我要把我的商店变得更加令人满意。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EC0")

    label("loc_1EAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1EB9")
    Jump("loc_1EC0")

    label("loc_1EB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1EC0")

    label("loc_1EC0")

    TalkEnd(0xFE)
    Return()

    # Function_12_1A6E end

    def Function_13_1EC4(): pass

    label("Function_13_1EC4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_1F11")

    ChrTalk(
        0x110,
        (
            "#151F对了对了，明天我还要去大会取材呢，\x01",
            "到时候请多关照啦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F7D")

    label("loc_1F11")

    OP_A2(0xA)

    ChrTalk(
        0x110,
        (
            "#151F啊，你们俩来了啊。\x01",
            "比赛的照片拍得超棒呢～\x02\x03",
            "已经预定要出版武术大会的特辑了，\x01",
            "你们要好好期待哦～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F7D")

    TalkEnd(0xFE)
    Return()

    # Function_13_1EC4 end

    def Function_14_1F81(): pass

    label("Function_14_1F81")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1F8E")
    Jump("loc_21F8")

    label("loc_1F8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1F98")
    Jump("loc_21F8")

    label("loc_1F98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1FA2")
    Jump("loc_21F8")

    label("loc_1FA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1FAC")
    Jump("loc_21F8")

    label("loc_1FAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1FB6")
    Jump("loc_21F8")

    label("loc_1FB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_20C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_2017")

    ChrTalk(
        0xFE,
        (
            "卢希娅这次要给\x01",
            "那位高个子大叔加油。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过妈妈却支持\x01",
            "戴红头盔的哥哥呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20C1")

    label("loc_2017")

    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "卢希娅这次要给\x01",
            "那位高个子大叔加油。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过妈妈却支持\x01",
            "戴红头盔的哥哥呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F（……大叔，\x01",
            "　是在说金先生吗？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F（他本人听见了一定会很难过的。）\x02",
    )

    CloseMessageWindow()

    label("loc_20C1")

    Jump("loc_21F8")

    label("loc_20C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_20FE")

    ChrTalk(
        0xFE,
        "比赛还没有开始吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "卢希娅相当期待呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_21F8")

    label("loc_20FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_214B")

    ChrTalk(
        0xFE,
        (
            "戴红头巾的哥哥们\x01",
            "最后还是输了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "卢希娅为他们加油了的……\x02",
    )

    CloseMessageWindow()
    Jump("loc_21F8")

    label("loc_214B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_218E")

    ChrTalk(
        0xFE,
        "卢希娅啊～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "拼命支持那些\x01",
            "绑着红头巾的哥哥们哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21F8")

    label("loc_218E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_21CC")

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "我要给我的朋友波利他们\x01",
            "买些礼物带回去哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21F8")

    label("loc_21CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_21F8")

    ChrTalk(
        0xFE,
        (
            "嘿嘿，\x01",
            "我是和妈妈一起来的哦～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21F8")

    TalkEnd(0xFE)
    Return()

    # Function_14_1F81 end

    def Function_15_21FC(): pass

    label("Function_15_21FC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2209")
    Jump("loc_268B")

    label("loc_2209")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2213")
    Jump("loc_268B")

    label("loc_2213")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_221D")
    Jump("loc_268B")

    label("loc_221D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2227")
    Jump("loc_268B")

    label("loc_2227")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2231")
    Jump("loc_268B")

    label("loc_2231")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_22C9")

    ChrTalk(
        0xFE,
        (
            "在比赛中的双方选手\x01",
            "使用各自经过严酷修行练就的本领\x01",
            "过招的那一刻可谓是最棒的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就是那种\x01",
            "厚积薄发的力量和信念\x01",
            "互相碰撞所迸发出的感觉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_268B")

    label("loc_22C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2325")

    ChrTalk(
        0xFE,
        (
            "我和女儿两人\x01",
            "一直在期盼着武术大会呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天也打算从\x01",
            "第一场开始就去观看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_268B")

    label("loc_2325")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_23FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2388")

    ChrTalk(
        0xFE,
        (
            "渡鸦帮那群孩子\x01",
            "果然还是输了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过我看他们离场时\x01",
            "似乎带着满足的神情呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23F7")

    label("loc_2388")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "渡鸦帮那群孩子\x01",
            "果然还是输了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不过，也许是我的错觉……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我看他们离场时\x01",
            "似乎带着满足的神情呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23F7")

    Jump("loc_268B")

    label("loc_23FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_24D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_244C")

    ChrTalk(
        0xFE,
        (
            "渡鸦帮不就是\x01",
            "卢安的流氓团伙嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "最好别成为卢安的耻辱。\x02",
    )

    CloseMessageWindow()
    Jump("loc_24D1")

    label("loc_244C")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "渡鸦帮不就是\x01",
            "被市长利用的\x01",
            "卢安的流氓团伙嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他们还要来参加武术大会，\x01",
            "究竟是怎么想的嘛……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最好别成为\x01",
            "卢安的耻辱。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24D1")

    Jump("loc_268B")

    label("loc_24D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2646")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2561")

    ChrTalk(
        0xFE,
        (
            "卢安的孤儿院\x01",
            "现在得到了捐款和赔偿金，\x01",
            "正在重建之中了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "孩子们在我家开的旅店\x01",
            "里面暂时借宿着，\x01",
            "大家都非常开心呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2643")

    label("loc_2561")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "最近卢安地区还真是不得了。\x01",
            "孤儿院被纵火，\x01",
            "市长又被逮捕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "孤儿院现在得到了捐款和赔偿金，\x01",
            "正在重建之中了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "孩子们在我家开的旅店\x01",
            "里面暂时借宿着，\x01",
            "大家都非常开心呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "希望新的孤儿院\x01",
            "能够早日完工。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2643")

    Jump("loc_268B")

    label("loc_2646")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_268B")

    ChrTalk(
        0xFE,
        (
            "我是从卢安地区的\x01",
            "玛诺利亚村来的，\x01",
            "和女儿一起来王都参观。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_268B")

    TalkEnd(0xFE)
    Return()

    # Function_15_21FC end

    def Function_16_268F(): pass

    label("Function_16_268F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_269C")
    Jump("loc_28E2")

    label("loc_269C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_26A6")
    Jump("loc_28E2")

    label("loc_26A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_26B0")
    Jump("loc_28E2")

    label("loc_26B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_270F")

    ChrTalk(
        0xFE,
        (
            "明天我要坐\x01",
            "定期船回柏斯了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然想带点礼物\x01",
            "回去送给哥哥，\x01",
            "可买什么才好呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28E2")

    label("loc_270F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2758")

    ChrTalk(
        0xFE,
        (
            "我打算下午去参观\x01",
            "西街区的大圣堂。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是很令人期待呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_28E2")

    label("loc_2758")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_2783")

    ChrTalk(
        0xFE,
        (
            "今天该到哪里\x01",
            "去参观一下呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28E2")

    label("loc_2783")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_27D2")

    ChrTalk(
        0xFE,
        (
            "对了，\x01",
            "哥哥还让我去买钓鱼用具呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "一会儿去钓公师团看看吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_28E2")

    label("loc_27D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_282C")

    ChrTalk(
        0xFE,
        (
            "我、我是第一次\x01",
            "观看武术大会呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "非常震撼啊，\x01",
            "甚至让我都有些颤抖了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28E2")

    label("loc_282C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2873")

    ChrTalk(
        0xFE,
        "今天做些什么呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难得有武术大会，\x01",
            "还是去看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28E2")

    label("loc_2873")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_28A4")

    ChrTalk(
        0xFE,
        (
            "好久没来王都了，\x01",
            "要好好快乐一番。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28E2")

    label("loc_28A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_28E2")

    ChrTalk(
        0xFE,
        (
            "为了到这里来买东西，\x01",
            "我特地从柏斯乘坐定期船而来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28E2")

    TalkEnd(0xFE)
    Return()

    # Function_16_268F end

    def Function_17_28E6(): pass

    label("Function_17_28E6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_29BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2952")

    ChrTalk(
        0xFE,
        (
            "我还是不认为\x01",
            "杜南公爵是个坏人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过他给别人带来很多麻烦\x01",
            "倒是无可辩驳的事实。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29B9")

    label("loc_2952")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "大家虽然说了很多\x01",
            "杜南公爵的坏话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我还是不认为\x01",
            "他是个坏人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不会只有我这么想吧……\x02",
    )

    CloseMessageWindow()

    label("loc_29B9")

    Jump("loc_2CA5")

    label("loc_29BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2A14")

    ChrTalk(
        0xFE,
        (
            "街道上到处都是士兵，\x01",
            "这绝对不是什么好事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天最好还是\x01",
            "早些回家吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CA5")

    label("loc_2A14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2A65")

    ChrTalk(
        0xFE,
        (
            "店里的人从刚才起\x01",
            "就在神色慌张地讨论着什么……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "发生什么事了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CA5")

    label("loc_2A65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2AA3")

    ChrTalk(
        0xFE,
        (
            "唔～……\x01",
            "我偶尔想来看看\x01",
            "给妻子买些什么礼物……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CA5")

    label("loc_2AA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2B0F")

    ChrTalk(
        0xFE,
        (
            "一开始我觉得餐具之类的东西\x01",
            "随便买什么样的都无所谓……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过好的东西\x01",
            "始终还是好的东西啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CA5")

    label("loc_2B0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_2B7E")

    ChrTalk(
        0xFE,
        (
            "话说回来，\x01",
            "要等到什么时候\x01",
            "才能抓到恐怖分子啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "竟然会有人袭击中央工房，\x01",
            "真是万万没有想到。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CA5")

    label("loc_2B7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2BD0")

    ChrTalk(
        0xFE,
        (
            "我对武术大会\x01",
            "不太感兴趣呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "所以，\x01",
            "今天就和平常一样度过吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CA5")

    label("loc_2BD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2C3B")

    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "今天好像没有什么新东西呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我原本以为今天\x01",
            "会进些新的商品，\x01",
            "所以一直都在这里等着。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CA5")

    label("loc_2C3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2C5B")

    ChrTalk(
        0xFE,
        "唔～真麻烦啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CA5")

    label("loc_2C5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2C7F")

    ChrTalk(
        0xFE,
        "哦，这个也很不错……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CA5")

    label("loc_2C7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2CA5")

    ChrTalk(
        0xFE,
        (
            "唔，\x01",
            "这个东西非常不错呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CA5")

    TalkEnd(0xFE)
    Return()

    # Function_17_28E6 end

    def Function_18_2CA9(): pass

    label("Function_18_2CA9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2D10")

    ChrTalk(
        0xFE,
        (
            "今天中午\x01",
            "做些什么菜好呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽说是诞辰庆典期间，\x01",
            "但并不是家庭主妇的休息日呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3072")

    label("loc_2D10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2D6D")

    ChrTalk(
        0xFE,
        "今天街上到处都是黑衣士兵。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "给优雅的格兰赛尔大街\x01",
            "带来了很多不和谐的杂色。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3072")

    label("loc_2D6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2DA0")

    ChrTalk(
        0xFE,
        (
            "是我多心了吗，\x01",
            "总觉得东西变少了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3072")

    label("loc_2DA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2DE4")

    ChrTalk(
        0xFE,
        "今天有限时降价销售哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不快点的话就抢不到了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3072")

    label("loc_2DE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2E4C")

    ChrTalk(
        0xFE,
        (
            "今天不去购物了，\x01",
            "找个地方去吃饭吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，现在这个时候\x01",
            "肯定哪个角落都有很多人吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3072")

    label("loc_2E4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_2E7D")

    ChrTalk(
        0xFE,
        (
            "那～么，\x01",
            "今天做些什么菜比较好呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3072")

    label("loc_2E7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2ED5")

    ChrTalk(
        0xFE,
        "这样东西就买全了吧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不写个便条的话，\x01",
            "有些东西\x01",
            "肯定就会忘记买呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3072")

    label("loc_2ED5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2F02")

    ChrTalk(
        0xFE,
        (
            "嗯～\x01",
            "调和油好像已经用完了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3072")

    label("loc_2F02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2FA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2F3E")

    ChrTalk(
        0xFE,
        (
            "顺便也去买一点\x01",
            "和红茶搭配的点心吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F9D")

    label("loc_2F3E")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "咖啡虽然不错，\x01",
            "但我还是坚决拥护红茶。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这里大概就是全利贝尔\x01",
            "红茶品种最全的地方了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F9D")

    Jump("loc_3072")

    label("loc_2FA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_3002")

    ChrTalk(
        0xFE,
        (
            "武术大会开始之后，\x01",
            "大街就会变得拥挤了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要不要事先\x01",
            "尽量多买些东西储备着呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3072")

    label("loc_3002")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3072")

    ChrTalk(
        0xFE,
        (
            "哎呀，\x01",
            "今天拉文努村的特产进货了呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "没有钱的时候却看到了想要的东西，\x01",
            "这可怎么办好呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3072")

    TalkEnd(0xFE)
    Return()

    # Function_18_2CA9 end

    def Function_19_3076(): pass

    label("Function_19_3076")

    Call(0, 20)
    Return()

    # Function_19_3076 end

    def Function_20_307B(): pass

    label("Function_20_307B")

    TalkBegin(0x19)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30DC")
    OP_0D()
    OP_A9(0x5E)
    OP_56(0x0)
    TalkEnd(0x19)
    Return()

    label("loc_30DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30ED")
    TalkEnd(0x19)
    Return()

    label("loc_30ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_31D2")

    ChrTalk(
        0x19,
        (
            "只是背地里说姐姐坏话\x01",
            "果然还是没办法\x01",
            "把红茶销售员的位置给抢过来呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "从现在开始我要更加努力地\x01",
            "学习与红茶相关的事项，\x01",
            "这样迟早会打动店长的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "到那时我就一脚把她踢下去，\x01",
            "然后把红茶销售员的位置优雅地夺回来！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_354B")

    label("loc_31D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_323C")

    ChrTalk(
        0x19,
        (
            "那～个，那～个，\x01",
            "啊～想不出来有什么姐姐的坏话！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "总、总之，\x01",
            "红茶销售员还是我当最合适！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_354B")

    label("loc_323C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_33FB")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_3264"),
        (1, "loc_328C"),
        (2, "loc_32BC"),
        (3, "loc_32E8"),
        (4, "loc_3363"),
        (5, "loc_3397"),
        (SWITCH_DEFAULT, "loc_33CD"),
    )


    label("loc_3264")


    ChrTalk(
        0x19,
        (
            "那～个，那～个，\x01",
            "姐姐她有脚气！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33CD")

    label("loc_328C")


    ChrTalk(
        0x19,
        (
            "那～个，那～个，\x01",
            "姐姐她是个方向白痴呢！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33CD")

    label("loc_32BC")


    ChrTalk(
        0x19,
        (
            "那～个，那～个，\x01",
            "我姐姐很怕蟑螂的！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33CD")

    label("loc_32E8")


    ChrTalk(
        0x19,
        (
            "那～个，那～个，\x01",
            "姐姐她……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "最近都不理我了。\x01",
            "好寂寞哦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "刚、刚才说的不算！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "总、总之她最近很冷漠！\x02",
    )

    CloseMessageWindow()
    Jump("loc_33CD")

    label("loc_3363")


    ChrTalk(
        0x19,
        (
            "这～个，这～个，\x01",
            "姐姐她喜欢吃甜食却长不胖！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33CD")

    label("loc_3397")


    ChrTalk(
        0x19,
        (
            "那～个，那～个，\x01",
            "姐姐有低血压，早晨很衰弱哦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33CD")

    label("loc_33CD")


    ChrTalk(
        0x19,
        (
            "所、所以呢，\x01",
            "她不适合做红茶销售员哦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_354B")

    label("loc_33FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_354B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_347E")

    ChrTalk(
        0x19,
        (
            "她啊，利用姐姐的特权，\x01",
            "把红茶销售员的岗位从我手里抢走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "我一定要赶上她，\x01",
            "并把红茶销售员的岗位夺回来！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_354B")

    label("loc_347E")

    OP_A2(0x11)

    ChrTalk(
        0x19,
        (
            "那边的红茶销售员\x01",
            "基蒂是我的双胞胎姐姐哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "红茶销售员是\x01",
            "这里最受欢迎的岗位呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "她啊，利用姐姐的特权，\x01",
            "把红茶销售员的岗位从我手里抢走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "我一定要赶上她，\x01",
            "并把红茶销售员的岗位夺回来！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_354B")

    TalkEnd(0x19)
    Return()

    # Function_20_307B end

    def Function_21_354F(): pass

    label("Function_21_354F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_35C3")

    ChrTalk(
        0xFE,
        (
            "这次是不是委托\x01",
            "丹顿先生去进一些\x01",
            "共和国制作的茶壶来呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最近这种茶壶\x01",
            "在女性之间非常流行呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4167")

    label("loc_35C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_3678")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_361E")

    ChrTalk(
        0xFE,
        (
            "虽然我也喜欢柠檬茶，\x01",
            "不过最推荐的还是要数\x01",
            "北安布里亚产的诺尔基露茶。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3675")

    label("loc_361E")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        "欢迎光临！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果您喜欢奶茶的话，\x01",
            "尝尝这个共和国产的\x01",
            "卡尔瓦德混合咖啡如何？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3675")

    Jump("loc_4167")

    label("loc_3678")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_37B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_36ED")

    ChrTalk(
        0xFE,
        (
            "那位艾莉茜雅女王陛下\x01",
            "也是一位喜欢红茶的人哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "女王陛下竟然也喜欢红茶，\x01",
            "我觉得相当自豪啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37B4")

    label("loc_36ED")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "这是利贝尔红茶爱好者之间\x01",
            "相当有名的一件事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那位艾莉茜雅女王陛下\x01",
            "也是一位喜欢红茶的人哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "王城里面的人\x01",
            "时常会来我们店购买茶叶的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "女王陛下竟然也喜欢红茶，\x01",
            "我觉得相当自豪啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37B4")

    Jump("loc_4167")

    label("loc_37B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_3926")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_381E")

    ChrTalk(
        0xFE,
        (
            "一定要把\x01",
            "最后一滴茶水注入茶杯！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "想要喝到香浓的红茶，\x01",
            "这件事就绝对不能忘记。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3923")

    label("loc_381E")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "基蒂姐姐的\x01",
            "制作香浓红茶\x01",
            "黄金准则之六！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一定要把\x01",
            "最后一滴茶水注入茶杯！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这一滴是最精华的一滴，\x01",
            "被人们称为黄金水滴。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且倒茶的时候\x01",
            "要一边摇匀，\x01",
            "一边慢慢地倒茶。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以上就是本店\x01",
            "推荐的香浓红茶\x01",
            "黄金六大准则。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "怎么样，很有参考价值吧？\x02",
    )

    CloseMessageWindow()

    label("loc_3923")

    Jump("loc_4167")

    label("loc_3926")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_3A9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3982")

    ChrTalk(
        0xFE,
        "茶叶一定要泡足时间！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "想要喝到香浓的红茶，\x01",
            "这件事就绝对不能忘记。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A97")

    label("loc_3982")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "基蒂姐姐的\x01",
            "制作香浓红茶\x01",
            "黄金准则之五！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "茶叶一定要泡足时间！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "红茶刚泡的时候会有点苦味，\x01",
            "但之后味道会慢慢变香浓的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "所以呢，在品尝之前，\x01",
            "耐心的等待也是很重要的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过泡得太久的话，\x01",
            "红茶味道会变涩的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "长的茶叶就多泡会儿，\x01",
            "短的茶叶就少泡会儿。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A97")

    Jump("loc_4167")

    label("loc_3A9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_3C00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3AF6")

    ChrTalk(
        0xFE,
        "正确掌握茶叶的分量！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "想要喝到香浓的红茶，\x01",
            "这件事就绝对不能忘记。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BFD")

    label("loc_3AF6")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "基蒂姐姐的\x01",
            "制作香浓红茶\x01",
            "黄金准则之四！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "正确掌握茶叶的分量！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "根据茶叶的不同会有些许差异，\x01",
            "但大体上是按照每一茶杯\x01",
            "放一匙茶叶的比例哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "茶叶太多会很苦，\x01",
            "放得太少了\x01",
            "味道就会不足。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "特别是短时间放很多茶叶，\x01",
            "这种做法泡出来的茶\x01",
            "会只剩下苦味。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BFD")

    Jump("loc_4167")

    label("loc_3C00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_3D91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3C61")

    ChrTalk(
        0xFE,
        (
            "请一定要将\x01",
            "茶壶预先加热！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "想要喝到香浓的红茶，\x01",
            "这件事就绝对不能忘记。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D8E")

    label("loc_3C61")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "基蒂姐姐的\x01",
            "制作香浓红茶\x01",
            "黄金准则之三！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "请一定要将\x01",
            "茶壶预先加热！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "倒入热水时，\x01",
            "茶叶上下翻滚的现象\x01",
            "称为『跳跃』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要泡出香浓的好茶，\x01",
            "这是绝对必不可少的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，茶壶冷却的话\x01",
            "热水也会随之冷却，\x01",
            "这样就难以出现跳跃现象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "另外，\x01",
            "据说将茶壶做成圆形\x01",
            "也是为了容易引起跳跃现象。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D8E")

    Jump("loc_4167")

    label("loc_3D91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3EEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3E29")

    ChrTalk(
        0xFE,
        (
            "一定要用纯净的、\x01",
            "沸腾的开水冲泡！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "想要喝到香浓的红茶，\x01",
            "这件事就绝对不能忘记。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "顺便说一句，\x01",
            "沸腾很久的水也不适合泡茶哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EEB")

    label("loc_3E29")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "基蒂姐姐的\x01",
            "制作香浓红茶\x01",
            "黄金准则之二！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一定要用纯净的、\x01",
            "沸腾的开水冲泡！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要让香浓的成分得以释放，\x01",
            "水中必须要溶入\x01",
            "充足的空气才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为此，\x01",
            "要先把水煮沸，\x01",
            "然后再注入茶壶中。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EEB")

    Jump("loc_4167")

    label("loc_3EEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_4018")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3F32")

    ChrTalk(
        0xFE,
        (
            "首先要采用新鲜优良的茶叶，\x01",
            "这是基本中的基本。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4015")

    label("loc_3F32")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "基蒂姐姐的\x01",
            "制作香浓红茶\x01",
            "黄金准则之一！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "首先要采用优良的茶叶，\x01",
            "这是所有一切的先决条件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽说只要红茶没有发霉，\x01",
            "或是气味没有变怪，\x01",
            "也还是可以泡来喝的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过为了保证味道的香浓，\x01",
            "采用新鲜的茶叶才是根本哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4015")

    Jump("loc_4167")

    label("loc_4018")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_409D")

    ChrTalk(
        0xFE,
        (
            "客人，\x01",
            "您知道泡制香浓红茶的黄金准则吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "泡茶的准则\x01",
            "根据地域的不同内容也不尽相同，\x01",
            "本店有六条准则可以推荐给您哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4167")

    label("loc_409D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4167")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4100")

    ChrTalk(
        0xFE,
        (
            "推荐您品尝\x01",
            "我们这里的红茶～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我也可以指导您如何泡茶哦，\x01",
            "客人请试一试吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4167")

    label("loc_4100")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        "欢迎光临～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "推荐您品尝\x01",
            "我们这里的红茶～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我也可以指导您如何泡茶哦，\x01",
            "客人请试一试吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4167")

    TalkEnd(0xFE)
    Return()

    # Function_21_354F end

    def Function_22_416B(): pass

    label("Function_22_416B")

    Call(0, 23)
    Return()

    # Function_22_416B end

    def Function_23_4170(): pass

    label("Function_23_4170")

    TalkBegin(0xB)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41D1")
    OP_0D()
    OP_A9(0x5D)
    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_41D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41E2")
    TalkEnd(0xB)
    Return()

    label("loc_41E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_42B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4244")

    ChrTalk(
        0xB,
        (
            "不管怎么说，女王陛下平安无事，\x01",
            "诞辰庆典也顺利举行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "这不就挺好的吗。\x02",
    )

    CloseMessageWindow()
    Jump("loc_42AE")

    label("loc_4244")

    OP_A2(0x3)

    ChrTalk(
        0xB,
        "哎呀，可喜可贺！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "不管怎么说，女王陛下平安无事，\x01",
            "诞辰庆典也顺利举行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "这不就挺好的吗。\x02",
    )

    CloseMessageWindow()

    label("loc_42AE")

    Jump("loc_4998")

    label("loc_42B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_4385")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_431E")

    ChrTalk(
        0xB,
        (
            "亲卫队如果就这么逃走了，\x01",
            "我的困惑就烟消云散了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "那位尤莉亚中尉\x01",
            "不可能是恐怖分子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4382")

    label("loc_431E")

    OP_A2(0x3)

    ChrTalk(
        0xB,
        (
            "如果亲卫队\x01",
            "就这么逃走了的话，\x01",
            "我的困惑就烟消云散了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "尤莉亚中尉他们\x01",
            "肯定不是恐怖分子。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4382")

    Jump("loc_4998")

    label("loc_4385")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_4458")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_43E6")

    ChrTalk(
        0xB,
        (
            "军队将空港\x01",
            "完全封锁起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "怎么回事啊……\x01",
            "这样的话不是没法进货了吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4455")

    label("loc_43E6")

    OP_A2(0x3)

    ChrTalk(
        0xB,
        (
            "军队将空港\x01",
            "完全封锁起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "怎么回事啊……\x01",
            "这样的话不是没法进货了吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "可恶，看他们干的好事。\x02",
    )

    CloseMessageWindow()

    label("loc_4455")

    Jump("loc_4998")

    label("loc_4458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_44C8")

    ChrTalk(
        0xB,
        "武术大会好像决出优胜者了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "被邀请到王城晚宴的人\x01",
            "为了要迎合公爵的脸面，\x01",
            "也会穿得体面一点吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4998")

    label("loc_44C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_45F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_454C")

    ChrTalk(
        0xB,
        (
            "话说回来，\x01",
            "最近柏斯、卢安还有蔡斯\x01",
            "都相继发生了一些大案件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "什么事情也没有发生的\x01",
            "就只剩下王都和洛连特了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45F5")

    label("loc_454C")

    OP_A2(0x3)

    ChrTalk(
        0xB,
        (
            "话说回来，\x01",
            "最近柏斯、卢安还有蔡斯\x01",
            "都相继发生了一些大案件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "什么事情也没有发生的\x01",
            "就只剩下王都和洛连特了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "希望就这样安然无恙地\x01",
            "什么事情都不发生就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45F5")

    Jump("loc_4998")

    label("loc_45F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_4723")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4679")

    ChrTalk(
        0xB,
        (
            "店长说，\x01",
            "诞辰庆典结束之后\x01",
            "要带我们去柏斯超市研修。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "我们的店长\x01",
            "常常提出一些意见，\x01",
            "就是因为做了对比吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4720")

    label("loc_4679")

    OP_A2(0x3)

    ChrTalk(
        0xB,
        (
            "店长说，\x01",
            "诞辰庆典结束之后\x01",
            "要带我们去柏斯超市研修。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "其实我也想去\x01",
            "那个传说中的柏斯超市\x01",
            "参观取经呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "我们的店长\x01",
            "常常提出一些意见，\x01",
            "就是因为做了对比吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4720")

    Jump("loc_4998")

    label("loc_4723")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4831")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_478C")

    ChrTalk(
        0xB,
        (
            "最近卢安\x01",
            "准备进行市长选举。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "长年以来治理那个地区的\x01",
            "戴尔蒙家族也终于垮台了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_482E")

    label("loc_478C")

    OP_A2(0x3)

    ChrTalk(
        0xB,
        (
            "对了，\x01",
            "我在《利贝尔通讯》上看到……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "最近卢安\x01",
            "准备进行市长选举。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "长年以来治理那个地区的\x01",
            "戴尔蒙家族也终于垮台了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "唉，这也是理所当然的吧。\x02",
    )

    CloseMessageWindow()

    label("loc_482E")

    Jump("loc_4998")

    label("loc_4831")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_48A3")

    ChrTalk(
        0xB,
        (
            "因为卢安市长被捕，\x01",
            "现在那儿的情况变得很混乱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "这段时间水产品完全进不了货，\x01",
            "实在是让人困扰啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4998")

    label("loc_48A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_4905")

    ChrTalk(
        0xB,
        (
            "店长前一阵子外出旅行，\x01",
            "现在已经回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "店长在的时候\x01",
            "店里的气氛果然会很紧张。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4998")

    label("loc_4905")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_4970")

    ChrTalk(
        0xB,
        (
            "欢迎光临，\x01",
            "这里是专卖实用性装饰品\x01",
            "和餐具的柜台。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "如果有看中的东西，\x01",
            "跟我说一声就是了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4998")

    label("loc_4970")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4998")

    ChrTalk(
        0xB,
        (
            "欢迎光临。\x01",
            "是来买礼品的吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4998")

    TalkEnd(0xB)
    Return()

    # Function_23_4170 end

    def Function_24_499C(): pass

    label("Function_24_499C")

    Call(0, 25)
    Return()

    # Function_24_499C end

    def Function_25_49A1(): pass

    label("Function_25_49A1")

    TalkBegin(0xA)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A1A")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_4A03")
    OP_A9(0x69)
    Jump("loc_4A11")

    label("loc_4A03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_4A0F")
    OP_A9(0x68)
    Jump("loc_4A11")

    label("loc_4A0F")

    OP_A9(0x5C)

    label("loc_4A11")

    OP_56(0x0)
    TalkEnd(0xA)
    Return()

    label("loc_4A1A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A2B")
    TalkEnd(0xA)
    Return()

    label("loc_4A2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_4A9C")

    ChrTalk(
        0xA,
        (
            "第一时间报道政变的\x01",
            "《利贝尔通讯》特刊\x01",
            "可以说是疯狂热卖呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "刚刚进货不久，\x01",
            "一下子就又卖光了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F16")

    label("loc_4A9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_4AF9")

    ChrTalk(
        0xA,
        (
            "最近，\x01",
            "那些士兵频繁地来问话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "他们好像在\x01",
            "拼尽全力寻找\x01",
            "亲卫队队长的下落。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F16")

    label("loc_4AF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_4B6B")

    ChrTalk(
        0xA,
        (
            "买一本《利贝尔通讯》的\x01",
            "武术大会特辑临时增刊怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "无论是观众还是选手，\x01",
            "都一定要留个纪念哦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F16")

    label("loc_4B6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_4BB9")

    ChrTalk(
        0xA,
        (
            "啊～\x01",
            "怎么会这么忙呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "武术大会的结果\x01",
            "究竟是什么样的呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F16")

    label("loc_4BB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_4BEE")

    ChrTalk(
        0xA,
        (
            "今天天气很不错，\x01",
            "店里的饮料也很畅销。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F16")

    label("loc_4BEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_4C39")

    ChrTalk(
        0xA,
        (
            "武术大会一开始，\x01",
            "人果然就多起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "店长也喜出望外呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4F16")

    label("loc_4C39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4CB3")

    ChrTalk(
        0xA,
        (
            "因为女王殿下身体欠佳的缘故，\x01",
            "不知道是否还会举行诞辰庆典呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "不过即使如此，\x01",
            "还是来了很多观光的客人哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F16")

    label("loc_4CB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4D0B")

    ChrTalk(
        0xA,
        (
            "这里有卖既可以当旅行纪念\x01",
            "又具有实用性的格兰赛尔观光地图，\x01",
            "来一份怎么样？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F16")

    label("loc_4D0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_4E1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4D8D")

    ChrTalk(
        0xA,
        (
            "最近的《利贝尔通讯》\x01",
            "都是些无关紧要的新闻，\x01",
            "一点都不让人振奋……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "不过上面的照片\x01",
            "还是一如既往地漂亮呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E19")

    label("loc_4D8D")

    OP_A2(0x2)

    ChrTalk(
        0xA,
        (
            "最近的《利贝尔通讯》\x01",
            "都是些无关紧要的新闻，\x01",
            "一点都不让人振奋……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "为何会变成这样呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "不过上面的照片\x01",
            "还是一如既往地漂亮呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E19")

    Jump("loc_4F16")

    label("loc_4E1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_4EEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4E58")

    ChrTalk(
        0xA,
        (
            "我们百货店\x01",
            "从礼品到日用品都一应俱全。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EE7")

    label("loc_4E58")

    OP_A2(0x2)

    ChrTalk(
        0xA,
        (
            "我们百货店\x01",
            "从礼品到日用品都一应俱全。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "虽然在规模方面\x01",
            "的确不及柏斯超市……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "不过这里也有\x01",
            "相当多的优良商品，\x01",
            "不会比他们差的哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EE7")

    Jump("loc_4F16")

    label("loc_4EEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4F16")

    ChrTalk(
        0xA,
        (
            "欢迎光临！\x01",
            "这里是艾德尔百货店。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F16")

    TalkEnd(0xA)
    Return()

    # Function_25_49A1 end

    def Function_26_4F1A(): pass

    label("Function_26_4F1A")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_4F87")

    ChrTalk(
        0xFE,
        (
            "我一般是不会\x01",
            "到这种地方来购物的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是雪拉扎德和亚妮拉丝\x01",
            "不管怎么说都要把我给拉来……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FE8")

    label("loc_4F87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_4F91")
    Jump("loc_4FE8")

    label("loc_4F91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_4F9B")
    Jump("loc_4FE8")

    label("loc_4F9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_4FA5")
    Jump("loc_4FE8")

    label("loc_4FA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_4FAF")
    Jump("loc_4FE8")

    label("loc_4FAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_4FB9")
    Jump("loc_4FE8")

    label("loc_4FB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4FC3")
    Jump("loc_4FE8")

    label("loc_4FC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4FCD")
    Jump("loc_4FE8")

    label("loc_4FCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_4FD7")
    Jump("loc_4FE8")

    label("loc_4FD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_4FE1")
    Jump("loc_4FE8")

    label("loc_4FE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4FE8")

    label("loc_4FE8")

    TalkEnd(0x9)
    Return()

    # Function_26_4F1A end

    def Function_27_4FEC(): pass

    label("Function_27_4FEC")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_51EE")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 9240, 0, 5790, 90)
    SetChrPos(0x102, 9180, 0, 4760, 90)
    SetChrPos(0x108, 8280, 0, 5410, 90)
    TurnDirection(0x8, 0x108, 0)
    SetChrSubChip(0x8, 0)
    OP_A2(0x64C)
    OP_28(0x4B, 0x1, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x1, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x1, 0x20)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x1, 0x40)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x1, 0x80)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5073")
    OP_28(0x4B, 0x1, 0x100)

    label("loc_5073")

    OP_6D(10020, 0, 5390, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "啊呀，这不是\x01",
            "两位游击士新人和金大哥吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "这么快就从城里回来了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F嗯，是啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F亚妮拉丝小姐。\x01",
            "占用你一点时间好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "什么事，什么事？\x01",
            "有什么好玩儿的事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F唔～～～\x02\x03",
            "好玩儿倒是不至于，\x01",
            "不过你听了肯定会吓一跳呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "咦……\x01",
            "好像不太好玩啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "在这儿站着不好说话，\x01",
            "我们到外面的休息处去如何？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FF)
    NewScene("ED6_DT01/T4101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_559D")

    label("loc_51EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_5465")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_5247")

    ChrTalk(
        0xFE,
        (
            "之前第一次\x01",
            "和你们一起执行任务……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们俩配合得\x01",
            "还真是默契呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5462")

    label("loc_5247")

    OP_A2(0x1)

    ChrTalk(
        0x101,
        "#001F亚妮拉丝前辈！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F怎么了啊？\x01",
            "目不转睛地盯着我的脸看……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没什么，\x01",
            "之前第一次和你们一起执行任务……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们俩配合得\x01",
            "还真是默契呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F大概是因为我们一直都在一起，\x01",
            "彼此很熟悉吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5462")

    ChrTalk(
        0xFE,
        "是这样没错啦，不过……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "亚妮拉丝在艾丝蒂尔的耳边\x01",
            "说了几句悄悄话。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(
        0xFE,
        (
            "（嘻嘻，以我个人的看法，\x01",
            "　你们俩会成为恩爱的一对哦㈱）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "（别害羞别害羞！）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "（啊～连我也很向往能有约修亚那样\x01",
            "　俊俏的男孩做自己的男朋友呢。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#503F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F？\x02",
    )

    CloseMessageWindow()

    label("loc_5462")

    Jump("loc_559D")

    label("loc_5465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_546F")
    Jump("loc_559D")

    label("loc_546F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_5479")
    Jump("loc_559D")

    label("loc_5479")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_54EA")

    ChrTalk(
        0xFE,
        "唔～挑哪个好呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "每个都很可爱呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难得来到繁华的王都，\x01",
            "要抓紧时间享受购物的乐趣呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_559D")

    label("loc_54EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_54F4")
    Jump("loc_559D")

    label("loc_54F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_556E")

    ChrTalk(
        0xFE,
        "啊，两位新人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天好可惜呢。\x01",
            "虽然我们已经竭尽全力了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真有点不服气，\x01",
            "下次我们要再比试一下哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_559D")

    label("loc_556E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_5578")
    Jump("loc_559D")

    label("loc_5578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5582")
    Jump("loc_559D")

    label("loc_5582")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_558C")
    Jump("loc_559D")

    label("loc_558C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_5596")
    Jump("loc_559D")

    label("loc_5596")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_559D")

    label("loc_559D")

    TalkEnd(0x8)
    Return()

    # Function_27_4FEC end

    SaveToFile()

Try(main)
