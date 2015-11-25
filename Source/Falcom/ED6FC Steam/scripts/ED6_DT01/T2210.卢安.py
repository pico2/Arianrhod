from ED6ScenarioHelper import *

def main():
    # 卢安

    CreateScenaFile(
        FileName            = 'T2210   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2210.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T2210   ._SN',
            'ED6_DT01/T2210_1 ._SN',
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
        '戴尔蒙市长',                           # 9
        '奈尔',                                 # 10
        '杜南公爵',                             # 11
        '管家菲利普',                           # 12
        '芙罗拉',                               # 13
        '多米尼克',                             # 14
        '飞球',                                 # 15
        '野马',                                 # 16
        '秘书基尔巴特',                         # 17
        '照相机',                               # 18
        '达里奥',                               # 19
        '比古',                                 # 20
        '玻璃杯',                               # 21
        '玻璃杯',                               # 22
        '瓶子',                                 # 23
        '玻璃杯',                               # 24
        '玻璃杯',                               # 25
        '瓶子',                                 # 26
        '玻璃杯',                               # 27
    )

    DeclEntryPoint(
        Unknown_00              = 88000,
        Unknown_04              = 0,
        Unknown_08              = 22000,
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
        'ED6_DT07/CH02410 ._CH',             # 00
        'ED6_DT07/CH02470 ._CH',             # 01
        'ED6_DT06/CH20088 ._CH',             # 02
        'ED6_DT07/CH02060 ._CH',             # 03
        'ED6_DT07/CH01350 ._CH',             # 04
        'ED6_DT09/CH11020 ._CH',             # 05
        'ED6_DT09/CH11021 ._CH',             # 06
        'ED6_DT09/CH11022 ._CH',             # 07
        'ED6_DT07/CH00100 ._CH',             # 08
        'ED6_DT07/CH00110 ._CH',             # 09
        'ED6_DT07/CH00140 ._CH',             # 0A
        'ED6_DT07/CH00101 ._CH',             # 0B
        'ED6_DT07/CH00111 ._CH',             # 0C
        'ED6_DT07/CH00141 ._CH',             # 0D
        'ED6_DT07/CH02420 ._CH',             # 0E
        'ED6_DT07/CH02540 ._CH',             # 0F
        'ED6_DT07/CH01560 ._CH',             # 10
        'ED6_DT07/CH01280 ._CH',             # 11
        'ED6_DT06/CH20081 ._CH',             # 12
        'ED6_DT06/CH20082 ._CH',             # 13
        'ED6_DT09/CH11030 ._CH',             # 14
        'ED6_DT09/CH11031 ._CH',             # 15
        'ED6_DT09/CH11032 ._CH',             # 16
        'ED6_DT06/CH20020 ._CH',             # 17
        'ED6_DT06/CH20021 ._CH',             # 18
        'ED6_DT06/CH20034 ._CH',             # 19
    )

    AddCharChipPat(
        'ED6_DT07/CH02410P._CP',             # 00
        'ED6_DT07/CH02470P._CP',             # 01
        'ED6_DT06/CH20088P._CP',             # 02
        'ED6_DT07/CH02060P._CP',             # 03
        'ED6_DT07/CH01350P._CP',             # 04
        'ED6_DT09/CH11020P._CP',             # 05
        'ED6_DT09/CH11021P._CP',             # 06
        'ED6_DT09/CH11022P._CP',             # 07
        'ED6_DT07/CH00100P._CP',             # 08
        'ED6_DT07/CH00110P._CP',             # 09
        'ED6_DT07/CH00140P._CP',             # 0A
        'ED6_DT07/CH00101P._CP',             # 0B
        'ED6_DT07/CH00111P._CP',             # 0C
        'ED6_DT07/CH00141P._CP',             # 0D
        'ED6_DT07/CH02420P._CP',             # 0E
        'ED6_DT07/CH02540P._CP',             # 0F
        'ED6_DT07/CH01560P._CP',             # 10
        'ED6_DT07/CH01280P._CP',             # 11
        'ED6_DT06/CH20081P._CP',             # 12
        'ED6_DT06/CH20082P._CP',             # 13
        'ED6_DT09/CH11030P._CP',             # 14
        'ED6_DT09/CH11031P._CP',             # 15
        'ED6_DT09/CH11032P._CP',             # 16
        'ED6_DT06/CH20020P._CP',             # 17
        'ED6_DT06/CH20021P._CP',             # 18
        'ED6_DT06/CH20034P._CP',             # 19
    )

    DeclNpc(
        X                   = -63850,
        Z                   = 0,
        Y                   = 34900,
        Direction           = 0,
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
        X                   = 24500,
        Z                   = 0,
        Y                   = 6100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 24500,
        Z                   = 0,
        Y                   = 6100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 24500,
        Z                   = 0,
        Y                   = 6100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 470,
        Z                   = 0,
        Y                   = -670,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -59600,
        Z                   = 0,
        Y                   = -18600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 24500,
        Z                   = 0,
        Y                   = 6100,
        Direction           = 270,
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
        X                   = 24500,
        Z                   = 0,
        Y                   = 6100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4530,
        Z                   = 0,
        Y                   = 36330,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 68100,
        Z                   = 0,
        Y                   = -9000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 37390,
        Z                   = 0,
        Y                   = 34110,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 20,
        Z                   = 700,
        Y                   = 39430,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -780,
        Z                   = 700,
        Y                   = 38600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -150,
        Z                   = 750,
        Y                   = 38740,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1966103,
        ChipIndex           = 0x17,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 20,
        Z                   = 700,
        Y                   = 39430,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65560,
        ChipIndex           = 0x18,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -780,
        Z                   = 700,
        Y                   = 38600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65560,
        ChipIndex           = 0x18,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -150,
        Z                   = 750,
        Y                   = 38740,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1966103,
        ChipIndex           = 0x17,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 20,
        Z                   = 700,
        Y                   = 39430,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 917528,
        ChipIndex           = 0x18,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -475,
        TriggerZ            = 0,
        TriggerY            = 3173,
        TriggerRange        = 800,
        ActorX              = -475,
        ActorZ              = 800,
        ActorY              = 3173,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -63800,
        TriggerZ            = 0,
        TriggerY            = 50790,
        TriggerRange        = 900,
        ActorX              = -63800,
        ActorZ              = -300,
        ActorY              = 50790,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 22,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -62370,
        TriggerZ            = 0,
        TriggerY            = -43110,
        TriggerRange        = 500,
        ActorX              = -62370,
        ActorZ              = 2000,
        ActorY              = -43110,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 23,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -59500,
        TriggerZ            = 250,
        TriggerY            = -36760,
        TriggerRange        = 800,
        ActorX              = -59500,
        ActorZ              = 1250,
        ActorY              = -36760,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 24,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_46A",          # 00, 0
        "Function_1_697",          # 01, 1
        "Function_2_6E8",          # 02, 2
        "Function_3_6FE",          # 03, 3
        "Function_4_744",          # 04, 4
        "Function_5_C58",          # 05, 5
        "Function_6_1273",         # 06, 6
        "Function_7_1E80",         # 07, 7
        "Function_8_231C",         # 08, 8
        "Function_9_2600",         # 09, 9
        "Function_10_283B",        # 0A, 10
        "Function_11_28EE",        # 0B, 11
        "Function_12_3014",        # 0C, 12
        "Function_13_5525",        # 0D, 13
        "Function_14_680F",        # 0E, 14
        "Function_15_6844",        # 0F, 15
        "Function_16_687E",        # 10, 16
        "Function_17_68B8",        # 11, 17
        "Function_18_68F0",        # 12, 18
        "Function_19_698B",        # 13, 19
        "Function_20_69FF",        # 14, 20
        "Function_21_6A7B",        # 15, 21
        "Function_22_6AAD",        # 16, 22
        "Function_23_6AB7",        # 17, 23
        "Function_24_6AC1",        # 18, 24
    )


    def Function_0_46A(): pass

    label("Function_0_46A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4B1")
    SetChrPos(0xC, -700, 0, -710, 90)
    SetChrPos(0xD, 790, 0, -710, 270)
    SetChrPos(0x13, 36970, 0, 27900, 270)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x10, 0x80)
    Jump("loc_612")

    label("loc_4B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_4FD")
    SetChrPos(0xC, 36850, 0, 31730, 0)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xD, 35800, 0, 34250, 180)
    SetChrPos(0x13, 36970, 0, 27900, 270)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x10, 0x80)
    Jump("loc_612")

    label("loc_4FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_573")
    SetChrPos(0xC, 67550, 0, 28050, 90)
    SetChrPos(0xD, -61450, 0, 2440, 180)
    SetChrPos(0x13, 36970, 0, 27900, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_55A")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 4530, 0, 36330, 90)
    Jump("loc_570")

    label("loc_55A")

    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 0, 1800, 0)

    label("loc_570")

    Jump("loc_612")

    label("loc_573")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_5C1")
    SetChrPos(0xC, 36850, 0, 31730, 0)
    SetChrPos(0xD, 35800, 0, 34250, 180)
    SetChrPos(0x13, 36970, 0, 27900, 270)
    SetChrPos(0x12, -2090, 0, 2630, 180)
    Jump("loc_612")

    label("loc_5C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_5DC")
    SetChrPos(0x13, 36970, 0, 27900, 270)
    Jump("loc_612")

    label("loc_5DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_END)), "loc_5F7")
    SetChrPos(0xC, 33500, 0, 24550, 270)
    Jump("loc_612")

    label("loc_5F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_612")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8)

    label("loc_612")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_622"),
        (114, "loc_669"),
        (SWITCH_DEFAULT, "loc_67F"),
    )


    label("loc_622")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_638")
    OP_A2(0x440)
    Event(0, 11)
    Jump("loc_666")

    label("loc_638")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x200)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_666")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x8, 0x80)
    OP_28(0x20, 0x4, 0x10)
    Event(1, 4)

    label("loc_666")

    Jump("loc_67F")

    label("loc_669")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_67C")
    OP_A2(0x441)
    Event(0, 12)

    label("loc_67C")

    Jump("loc_67F")

    label("loc_67F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_696")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FB)
    Event(0, 13)

    label("loc_696")

    Return()

    # Function_0_46A end

    def Function_1_697(): pass

    label("Function_1_697")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x200)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D4")
    OP_71(0x7, 0x4)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_71(0x6, 0x4)

    label("loc_6D4")

    OP_72(0x10, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6E7")
    OP_6F(0x10, 300)

    label("loc_6E7")

    Return()

    # Function_1_697 end

    def Function_2_6E8(): pass

    label("Function_2_6E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6FD")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_6E8")

    label("loc_6FD")

    Return()

    # Function_2_6E8 end

    def Function_3_6FE(): pass

    label("Function_3_6FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_72E")

    label("loc_708")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_72B")
    OP_8D(0xFE, 3420, 32950, 6190, 40410, 1500)
    Jump("loc_708")

    label("loc_72B")

    Jump("loc_743")

    label("loc_72E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_743")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_72E")

    label("loc_743")

    Return()

    # Function_3_6FE end

    def Function_4_744(): pass

    label("Function_4_744")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_9C1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_83B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E9")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "#660F各位，\x01",
            "这一次真是辛苦你们了。\x02\x03",
            "本来我应该\x01",
            "专程去向你们道谢的。\x01",
            "无奈事情堆积如山。\x02\x03",
            "非常抱歉，\x01",
            "我现在有事在身，没有时间。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_838")

    label("loc_7E9")


    ChrTalk(
        0xFE,
        (
            "#660F各位，\x01",
            "这一次真是辛苦你们了。\x02\x03",
            "希望以后能够看到\x01",
            "你们更加杰出的表现。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_838")

    Jump("loc_9BE")

    label("loc_83B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_933")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "#662F想必你们都已经听说了吧……\x01",
            "　\x02\x03",
            "其实，我家被盗贼闯进过，\x01",
            "传家宝也被盗走了。\x02\x03",
            "#664F但是，这件事只是件家务事。\x01",
            "我必须以完成公务为先。\x02\x03",
            "#660F所以，\x01",
            "这件事就交给了秘书基尔巴特全权处理。\x02\x03",
            "如果想了解有关情况的话，\x01",
            "你们可以去问他。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9BE")

    label("loc_933")


    ChrTalk(
        0xFE,
        (
            "#662F其实我家被盗贼闯进过。\x01",
            "传家宝也被盗走了。\x02\x03",
            "#660F这件事我交给了\x01",
            "秘书基尔巴特全权处理。\x02\x03",
            "如果想了解有关情况的话，\x01",
            "你们可以去问他。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9BE")

    Jump("loc_C54")

    label("loc_9C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_A8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A58")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "#660F对特蕾莎院长来说，\x01",
            "这真是一场浩劫啊。\x02\x03",
            "只要有我能帮上忙的，\x01",
            "你们尽量来找我就行了。\x02\x03",
            "这是作为一市之长\x01",
            "有义务去做的事情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A88")

    label("loc_A58")


    ChrTalk(
        0xFE,
        (
            "#660F对特蕾莎院长来说，\x01",
            "这真是一场浩劫啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A88")

    Jump("loc_C54")

    label("loc_A8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_B85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B2F")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "#660F我想你们已经听说了，\x01",
            "最近一段时间有一位\x01",
            "王族的客人要来卢安。\x02\x03",
            "就是今明两天，\x01",
            "希望不要出什么事情……\x02\x03",
            "请转告嘉恩\x01",
            "让他做好万全的准备。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B82")

    label("loc_B2F")


    ChrTalk(
        0xFE,
        (
            "#660F最近一段时间有一位\x01",
            "王族的客人要来卢安。\x02\x03",
            "请转告嘉恩\x01",
            "让他做好万全的准备。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B82")

    Jump("loc_C54")

    label("loc_B85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_C54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C01")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "#660F噢，原来是你们啊。\x02\x03",
            "关于刚才那些家伙，\x01",
            "市民都相继过来向我诉苦。\x02\x03",
            "看来我要采取一些行动了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C54")

    label("loc_C01")


    ChrTalk(
        0xFE,
        (
            "#660F关于刚才那些家伙，\x01",
            "市民都相继过来向我诉苦。\x02\x03",
            "看来我要采取一些行动了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C54")

    TalkEnd(0x8)
    Return()

    # Function_4_744 end

    def Function_5_C58(): pass

    label("Function_5_C58")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_DB6")
    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D24")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "#670F哟，各位游击士。\x01",
            "这次干得很漂亮嘛。\x02\x03",
            "这下我就可以放心地\x01",
            "去参加学院祭了。\x02\x03",
            "这样的机会是可遇不可求啊。\x01",
            "能见到许多学长和学弟学妹。\x02\x03",
            "我们每年也都\x01",
            "期待着这个时候的到来呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DB0")

    label("loc_D24")


    ChrTalk(
        0xFE,
        (
            "#670F这下我就可以安心地\x01",
            "去参加学院祭了。\x02\x03",
            "这样的机会是可遇不可求啊。\x01",
            "能见到许多学长和学弟学妹。\x02\x03",
            "我们每年也都\x01",
            "期待着这个时候的到来呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DB0")

    TalkEnd(0x10)
    Jump("loc_1272")

    label("loc_DB6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_106F")
    TalkBegin(0x10)

    ChrTalk(
        0xFE,
        "#670F呀，有什么疑问吗？\x02",
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
            "【确认卡片上的内容】\x01",      # 0
            "【没什么事】\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E5B"),
        (1, "loc_1038"),
        (SWITCH_DEFAULT, "loc_1038"),
    )


    label("loc_E5B")


    ChrTalk(
        0xFE,
        (
            "#670F卡片的内容啊。\x02\x03",
            "那你们再好好地确认一下吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "『方才蚕食巢穴的乃是比野兽更狂野的兽中之兽。\x01",
            "　\x01",
            "　苍之光将黑暗中迷失的灵魂赞颂并传承。\x01",
            "　让残存之耀得以救赎，而我即为解放者。\x01",
            "　\x01",
            "　啊，探寻者们。\x01",
            "　如女神一般直视真实，抛弃虚伪吧。\x01",
            "　\x01",
            "　前往耸立于此村落中的\x01",
            "　三眼巨人所在之处吧。\x01",
            "　如是，探寻者们，\x01",
            "　汝等将至苍之光所在。\x01",
            "　　　　　　　　　　　　　　　　　　　　怪盗Ｂ』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)

    ChrTalk(
        0xFE,
        (
            "#670F那调查的事情\x01",
            "就拜托你们继续进行了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1069")

    label("loc_1038")


    ChrTalk(
        0xFE,
        (
            "#670F那调查的事情\x01",
            "就拜托你们继续进行了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1069")

    label("loc_1069")

    TalkEnd(0x10)
    Jump("loc_1272")

    label("loc_106F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_108D")
    Call(1, 0)
    Jump("loc_1272")

    label("loc_108D")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1156")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1104")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "#671F找到犯人了吗？\x02\x03",
            "无论如何，\x01",
            "也不能让那些小流氓\x01",
            "在街头横行霸道。\x02\x03",
            "问题真是堆成山啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1153")

    label("loc_1104")


    ChrTalk(
        0xFE,
        (
            "#670F无论如何，\x01",
            "也不能让那些小流氓\x01",
            "在街头横行霸道。\x02\x03",
            "问题真是堆成山啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1153")

    Jump("loc_126F")

    label("loc_1156")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_11C3")

    ChrTalk(
        0xFE,
        (
            "#670F非常抱歉，卢安市里面\x01",
            "的确有一些不像样的家伙。\x02\x03",
            "说不定以后还要\x01",
            "麻烦你们帮忙解决他们的事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_126F")

    label("loc_11C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_126F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_123B")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "#671F真是的，\x01",
            "渡鸦帮那些小混混老是在惹麻烦……\x02\x03",
            "放任他们不管的话，\x01",
            "恐怕会给城市带来不良影响。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_126F")

    label("loc_123B")


    ChrTalk(
        0xFE,
        (
            "#671F真是的，\x01",
            "渡鸦帮那些小混混老是在惹麻烦……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_126F")

    TalkEnd(0x10)

    label("loc_1272")

    Return()

    # Function_5_C58 end

    def Function_6_1273(): pass

    label("Function_6_1273")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1A61")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x200)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_198A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x400)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1925")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -760, 0, -1810, 0)
    SetChrPos(0x102, -1660, -250, -2470, 0)
    SetChrPos(0x105, -660, -500, -2740, 0)
    TurnDirection(0xC, 0x101, 0)
    TurnDirection(0xD, 0x101, 0)
    OP_4A(0xD, 255)
    OP_28(0x20, 0x1, 0x400)
    OP_28(0x20, 0x1, 0x800)
    OP_6D(-1090, -250, -2370, 0)
    OP_0D()
    Sleep(100)
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0xC,
        "啊，各位。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "请你们看看。\x01",
            "烛台已经回来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8B(0x101, 0xA, 0xF46, 0x190)
    Sleep(100)
    OP_8B(0x105, 0xA, 0xF46, 0x190)
    OP_8B(0x102, 0xA, 0xF46, 0x190)

    ChrTalk(
        0x101,
        (
            "#501F啊，真的呢。\x02\x03",
            "是谁找它回来的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "不，不是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "不久之前\x01",
            "它自己回来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "真是奇怪得很……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F……这么说，\x01",
            "是犯人主动归还的了？\x02\x03",
            "犯人并不是为了钱，\x01",
            "这点我明白是明白……\x01",
            "可犯人的动机究竟是什么呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_146F():
        TurnDirection(0x102, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_146F)

    def lambda_147D():
        TurnDirection(0x105, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_147D)
    TurnDirection(0x101, 0xC, 400)

    ChrTalk(
        0x102,
        "#012F是什么时候回来的？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x102, 400)

    ChrTalk(
        0xC,
        "啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "这个……嗯……\x01",
            "是市长大人被逮捕的后一天。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F……是这样啊。\x02",
    )

    CloseMessageWindow()

    def lambda_1508():
        TurnDirection(0x105, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1508)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#501F是怎么回事呢？\x02",
    )

    CloseMessageWindow()

    def lambda_1536():
        TurnDirection(0xC, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1536)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F嗯…………\x01",
            "我是这么推测的……\x02\x03",
            "犯人的目的并非是烛台，\x01",
            "而是针对市长本人。\x02\x03",
            "如果不是这样，\x01",
            "那就没有理由要归还烛台了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F也就是说，\x01",
            "是为了揭穿市长的恶行吗？\x02\x03",
            "那么犯人直接去告发\x01",
            "不就行了吗……\x02\x03",
            "为什么还要盗取烛台后\x01",
            "留下一张张卡片，\x01",
            "绕了那么大一个圈子呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F也许不是为了揭露恶行……\x02\x03",
            "可能是……\x01",
            "为了好玩吧，我是这么想的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F犯人肯定是一开始就知道\x01",
            "市长的真面目的。\x01",
            "　\x02\x03",
            "一旦盗取了烛台，\x01",
            "我们游击士就会在\x01",
            "市长官邸里仔细调查。\x02\x03",
            "对戴尔蒙市长来说，\x01",
            "他可能一早明白犯人的用意。\x02\x03",
            "他知道喂养魔兽的房间\x01",
            "有被发现的危险。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F……唉，\x01",
            "可是我们当时立场不够坚定，\x01",
            "并没有那么做。\x02\x03",
            "#003F是啊…………\x01",
            "不过，市长他们当时\x01",
            "可能吓得冒了一身冷汗哦。\x02\x03",
            "不愿让我们调查屋子，\x01",
            "反而更加可疑……\x02\x03",
            "#002F……犯人大概在某处\x01",
            "看着市长的反应偷偷地冷笑吧？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F大概吧。\x01",
            "不出预料的话，应该就是这样的。\x02\x03",
            "因为如果不这么想的话，\x01",
            "这件事就没法解释了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_18BB():
        TurnDirection(0x105, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_18BB)
    OP_8C(0x101, 0, 400)

    ChrTalk(
        0x101,
        (
            "#505F…………怪盗Ｂ。\x02\x03",
            "真是一个来历不明的家伙呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Sleep(50)
    EventEnd(0x4)
    OP_8C(0xC, 90, 0)
    OP_8C(0xD, 270, 0)
    OP_4B(0xD, 255)
    Jump("loc_1987")

    label("loc_1925")


    ChrTalk(
        0xFE,
        (
            "盗走的烛台，\x01",
            "不久之前自己回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "主人也已经被逮捕了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "不知道到底怎么回事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1987")

    Jump("loc_1A5E")

    label("loc_198A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A23")

    ChrTalk(
        0xFE,
        (
            "这个烛台，\x01",
            "不久之前还是被盗走的东西……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不知道什么时候\x01",
            "就自己回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "主人也已经被逮捕了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "不知道到底怎么回事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A5E")

    label("loc_1A23")


    ChrTalk(
        0xFE,
        "主人已经被逮捕了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这座房子究竟会\x01",
            "何去何从呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A5E")

    Jump("loc_1E7C")

    label("loc_1A61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1B16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ADA")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "噜嗯噜嗯噜噜噜～⊙\x01",
            "啦嗯啦～啊哈哈嗯⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊啊，那炯炯的琥珀色眼睛……\x01",
            "好像要把人吸进去似的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B13")

    label("loc_1ADA")


    ChrTalk(
        0xFE,
        (
            "啊啊，那炯炯的琥珀色眼睛……\x01",
            "好像要把人吸进去似的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B13")

    Jump("loc_1E7C")

    label("loc_1B16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1BCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B92")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "就在不久之前，\x01",
            "从王都来了一位\x01",
            "埃雷波尼亚帝国的大使。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最近，地位显赫的大人物\x01",
            "经常到这里来呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BCC")

    label("loc_1B92")


    ChrTalk(
        0xFE,
        (
            "就在不久之前，\x01",
            "从王都来了一位\x01",
            "埃雷波尼亚帝国的大使。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BCC")

    Jump("loc_1E7C")

    label("loc_1BCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1C8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C6B")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "不久前，我在路上走的时候，\x01",
            "有一位一头红发眼神锐利的\x01",
            "游击士向我打招呼。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "哈……\x01",
            "有野性的男人真棒。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C8A")

    label("loc_1C6B")


    ChrTalk(
        0xFE,
        (
            "哈……\x01",
            "有野性的男人真棒。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C8A")

    Jump("loc_1E7C")

    label("loc_1C8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_1DE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D5E")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "卢安的市长一职\x01",
            "是通过选举产生的，\x01",
            "但每次戴尔蒙家族的主人都会当选。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "光是作为前贵族，\x01",
            "戴尔蒙家族的影响力\x01",
            "就已经非常大了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这座市长官邸\x01",
            "也是由戴尔蒙家族的主人\x01",
            "代代掌管的别墅。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DE0")

    label("loc_1D5E")


    ChrTalk(
        0xFE,
        (
            "卢安的市长一职\x01",
            "是通过选举产生的，\x01",
            "但每次戴尔蒙家族的主人都会当选。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "光是作为前贵族，\x01",
            "戴尔蒙家族的影响力\x01",
            "就已经非常大了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DE0")

    Jump("loc_1E7C")

    label("loc_1DE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_END)), "loc_1E14")

    ChrTalk(
        0xFE,
        (
            "因为市长回来了，\x01",
            "我正在准备茶水。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E7C")

    label("loc_1E14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_1E7C")

    ChrTalk(
        0xFE,
        (
            "真是非常抱歉，\x01",
            "市长现在外出了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果有什么事的话，\x01",
            "告诉我就可以了。\x01",
            "我会转达给市长的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E7C")

    TalkEnd(0xC)
    Return()

    # Function_6_1273 end

    def Function_7_1E80(): pass

    label("Function_7_1E80")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2004")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1F8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F27")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "竟然被卷进这样的事，\x01",
            "真是的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "接下来的事就交给\x01",
            "管家达里奥先生好了，\x01",
            "我还是赶快去找其他的工作吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "去试试做导游吧……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F87")

    label("loc_1F27")


    ChrTalk(
        0xFE,
        (
            "接下来的事就交给\x01",
            "管家达里奥先生好了，\x01",
            "我还是赶快去找其他的工作吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "去试试做导游吧……\x02",
    )

    CloseMessageWindow()

    label("loc_1F87")

    Jump("loc_2001")

    label("loc_1F8A")


    ChrTalk(
        0xFE,
        (
            "戴尔蒙家的传家宝什么的\x01",
            "跟我们又没什么关系。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "与之相比，\x01",
            "我对找工作的事情\x01",
            "更在意一些。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "去试试做导游吧……\x02",
    )

    CloseMessageWindow()

    label("loc_2001")

    Jump("loc_2318")

    label("loc_2004")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_2049")

    ChrTalk(
        0xFE,
        "哎呀哎呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "芙罗拉这孩子\x01",
            "真的很容易胡思乱想呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2318")

    label("loc_2049")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_20C0")

    ChrTalk(
        0xFE,
        (
            "为什么那些有权有势的人\x01",
            "没什么事情就从大老远的地方\x01",
            "特地赶到这里来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "用导力通信\x01",
            "明明就已经足够了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2318")

    label("loc_20C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2149")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_211F")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "唉～\x01",
            "芙罗拉这孩子又开始发病了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我真希望她能够\x01",
            "多动手少说话。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2146")

    label("loc_211F")


    ChrTalk(
        0xFE,
        (
            "唉～\x01",
            "芙罗拉这孩子又开始发病了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2146")

    Jump("loc_2318")

    label("loc_2149")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_2283")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2220")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "有很多人说市长的坏话，\x01",
            "但这也是没办法的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为血统的原因而当上市长，\x01",
            "这也是事实……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "市民会有不满，\x01",
            "也是理所当然的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……但是，\x01",
            "选出市长的也是市民们啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这又该怎么说。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2280")

    label("loc_2220")


    ChrTalk(
        0xFE,
        (
            "有很多人说市长的坏话，\x01",
            "但这也是没办法的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为血统的原因而当上市长，\x01",
            "这也是事实……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2280")

    Jump("loc_2318")

    label("loc_2283")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_END)), "loc_22E7")

    ChrTalk(
        0xFE,
        (
            "虽然他本人好像\x01",
            "完全没有发觉……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "基尔巴特是那种很容易\x01",
            "被那些小流氓钻空子的性格。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2318")

    label("loc_22E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_2318")

    ChrTalk(
        0xFE,
        "我现在很忙。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "能不能不要来烦我？\x02",
    )

    CloseMessageWindow()

    label("loc_2318")

    TalkEnd(0xD)
    Return()

    # Function_7_1E80 end

    def Function_8_231C(): pass

    label("Function_8_231C")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_238E")

    ChrTalk(
        0xFE,
        "我在戴尔蒙家工作了三十多年……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "长年来为卢安作贡献的这个家族，\x01",
            "却以这种形式拉下了大幕………\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25FC")

    label("loc_238E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_23E2")

    ChrTalk(
        0xFE,
        (
            "请问，\x01",
            "你们有什么事情？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在我家主人\x01",
            "与杜南公爵大人谈得正欢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25FC")

    label("loc_23E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_24C0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_245C")

    ChrTalk(
        0xFE,
        "哦，各位游击士。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们顺利地\x01",
            "把烛台找了回来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我代表这里的员工\x01",
            "向你们表示深深的感谢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24BD")

    label("loc_245C")


    ChrTalk(
        0xFE,
        (
            "没想到传家宝烛台\x01",
            "竟然被盗了…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "门窗都应该关严了。\x01",
            "那个小偷到底是\x01",
            "从哪里进来的呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24BD")

    Jump("loc_25FC")

    label("loc_24C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2524")

    ChrTalk(
        0xFE,
        (
            "这个烛台是\x01",
            "戴尔蒙家族的传家之宝。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为它的价值非常高，\x01",
            "我打理它的时候非常紧张。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25FC")

    label("loc_2524")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_2591")

    ChrTalk(
        0xFE,
        (
            "主人对于家庭名望\x01",
            "非常地重视。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然已经不再是领主了，\x01",
            "但这也是戴尔蒙家族\x01",
            "流传下来的义务。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25FC")

    label("loc_2591")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_END)), "loc_25C0")

    ChrTalk(
        0xFE,
        (
            "主人他最近\x01",
            "总是为很多事情操劳。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25FC")

    label("loc_25C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_25FC")

    ChrTalk(
        0xFE,
        "是客人吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是非常抱歉，\x01",
            "主人现在外出了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25FC")

    TalkEnd(0x12)
    Return()

    # Function_8_231C end

    def Function_9_2600(): pass

    label("Function_9_2600")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_266B")

    ChrTalk(
        0xFE,
        (
            "我一直以为市长是个伟大的人，\x01",
            "所以才为他做饭到现在。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "结果却变成这样，\x01",
            "真是太遗憾了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2837")

    label("loc_266B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_26C7")

    ChrTalk(
        0xFE,
        (
            "基尔巴特那小子\x01",
            "到底跑到哪里去了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "听说今天会有一个\x01",
            "很重要的客人来访……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2837")

    label("loc_26C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_272C")

    ChrTalk(
        0xFE,
        (
            "说起东方的刀具，\x01",
            "做得还真精致啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最近在厨师之间，\x01",
            "东方产的菜刀\x01",
            "引起了不少关注。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2837")

    label("loc_272C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2788")

    ChrTalk(
        0xFE,
        "午餐马上就做好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天的菜是浸泡烤鱼面\x01",
            "和蒜香吐司，\x01",
            "还有香草烤土鸡腿。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2837")

    label("loc_2788")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_27F3")

    ChrTalk(
        0xFE,
        (
            "市长小的时候\x01",
            "非常喜欢挑食，\x01",
            "不过最近他什么都吃了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "大概，\x01",
            "这也是作为市长的干劲之一吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2837")

    label("loc_27F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_2837")

    ChrTalk(
        0xFE,
        "厨具就是厨师的生命。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "保养它们的时候\x01",
            "必须非常细心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2837")

    TalkEnd(0x13)
    Return()

    # Function_9_2600 end

    def Function_10_283B(): pass

    label("Function_10_283B")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『苍耀之灯火』\x01",
            "　被誉为早期导力艺术\x01",
            "　的颠峰作品。\x01",
            "　导力革命之后，卢安\x01",
            "　市民将其赠与了为城\x01",
            "　市的发展鞠躬尽瘁的\x01",
            "　戴尔蒙家族。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_10_283B end

    def Function_11_28EE(): pass

    label("Function_11_28EE")

    EventBegin(0x0)
    OP_6D(-6240, 0, 6040, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0xC, -5830, 0, 5580, 315)
    SetChrPos(0x101, -600, -500, -3890, 0)
    SetChrPos(0x102, 950, -500, -3720, 315)
    SetChrPos(0x105, 570, -500, -5040, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_4A(0xC, 255)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xC, 0x101, 400)

    def lambda_29A8():
        OP_6D(-760, -500, -2510, 3000)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_29A8)
    OP_8E(0xC, 0xFFFFFDBC, 0x0, 0xFFFFF95C, 0xBB8, 0x0)
    TurnDirection(0xC, 0x101, 400)
    WaitChrThread(0xC, 0x1)

    ChrTalk(
        0xC,
        "欢迎光临卢安市长官邸。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "非常抱歉，\x01",
            "市长他现在正在会客……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "能请几位改日再来吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F哎～～！\x01",
            "等一下嘛……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F市长正在会见的那位客人，\x01",
            "其实我们也认识。\x02\x03",
            "是杜南公爵吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F哎……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x102, 400)

    ChrTalk(
        0xC,
        "是的，正是公爵大人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "……难道各位\x01",
            "也是受市长邀请前来的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是的，是市长亲自请我们来的。\x02\x03",
            "请问我们可以进去吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "仔细一看，各位原来是游击士啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "既然是这样，\x01",
            "那就请各位进来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "市长和公爵大人\x01",
            "正在二楼的大厅里谈话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F好的。\x01",
            "谢谢你的热情接待。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "………………（脸红）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "对、对了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "既然多了几位客人，\x01",
            "那我得去准备一下茶点才行……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "那我先失陪了。\x02",
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xC, 90, 400)

    def lambda_2C92():
        OP_6D(1390, 0, -20, 3000)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2C92)

    def lambda_2CAA():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2CAA)

    def lambda_2CB8():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2CB8)

    def lambda_2CC6():

        label("loc_2CC6")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_2CC6")

    QueueWorkItem2(0x102, 1, lambda_2CC6)
    OP_8E(0xC, 0x1432, 0x0, 0x49C, 0xBB8, 0x0)
    OP_44(0x102, 0xFF)
    SetChrFlags(0xC, 0x4)
    OP_8E(0xC, 0x2DF0, 0x0, 0x29E, 0xBB8, 0x0)
    ClearChrFlags(0xC, 0x4)
    SetChrPos(0xC, 33500, 0, 24550, 270)
    WaitChrThread(0xC, 0x1)
    OP_6D(-630, -500, -2970, 2000)

    ChrTalk(
        0x101,
        "#004F#1P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#044F……………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 225, 400)

    ChrTalk(
        0x102,
        "#014F#2P咦？怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F#1P没什么～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#045F这、这个嘛……\x02\x03",
            "#040F对了，你怎么知道\x01",
            "来的客人就是公爵大人？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2P啊，我也只是碰碰运气。\x02\x03",
            "昨晚基尔巴特不是说过\x01",
            "别墅是准备卖给国内外的富豪吗？\x02\x03",
            "我想像杜南公爵这样的人，\x01",
            "正是市长最理想的主顾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#044F的确是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F#1P真是的，一肚子鬼点子。\x02\x03",
            "居然信口开河说\x01",
            "是市长邀请我们来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#011F#2P这可不是信口开河哦。\x02\x03",
            "我们第一次见到戴尔蒙市长的时候，\x01",
            "他不是这样说过吗？\x02\x03",
            "要是渡鸦帮的人再给我们惹麻烦的话，\x01",
            "可以不必客气，尽管来这里找他。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#1P啊……这样吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#048F呵呵……\x01",
            "那的确就是应邀前来的了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F#2P没错，就是这样。\x02\x03",
            "#010F那么，就不必客气了，\x01",
            "我们直接去二楼的大厅吧。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    OP_4B(0xC, 255)
    Return()

    # Function_11_28EE end

    def Function_12_3014(): pass

    label("Function_12_3014")

    EventBegin(0x0)
    OP_6D(-2510, 0, 40990, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x14, 20, 700, 39500, 0)
    SetChrPos(0x15, -900, 700, 38600, 0)
    SetChrPos(0x16, -150, 850, 38740, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrPos(0x101, 11020, 0, 36640, 270)
    SetChrPos(0x102, 11020, 0, 36640, 270)
    SetChrPos(0x105, 11020, 0, 36640, 270)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0x8, 0x4)
    OP_4A(0x8, 255)
    SetChrPos(0xA, -50, 200, 40550, 180)
    SetChrPos(0x8, -2000, 0, 38810, 90)
    SetChrPos(0xB, 950, 0, 41760, 180)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "#227F#2P嗝……\x01",
            "嗯，听起来很不错嘛。\x02\x03",
            "这卢安的确是\x01",
            "购置别墅的绝佳地方啊。\x02\x03",
            "在这里住了一阵后深有体会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#661F#1P呵呵，的确如此。\x02\x03",
            "在这些高级别墅区中，\x01",
            "我们计划为公爵大人您\x01",
            "定制了一套位置极佳的豪华大屋。\x02\x03",
            "相信您一定会喜欢的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#227F#2P呵～呵～呵……\x01",
            "市长还真是善解人意啊。\x02\x03",
            "#483F很好，价格方面无所谓。\x02\x03",
            "你尽管去准备一套\x01",
            "配得起下任国王的豪宅就可以了。\x02\x03",
            "嗯，我想想……\x01",
            "最起码要达到这座官邸的水准。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#722F殿下，请稍等一下。\x02\x03",
            "不跟女王陛下商量\x01",
            "就擅自动用如此大额的巨款……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 1)

    ChrTalk(
        0xA,
        (
            "#482F#2P闭嘴，菲利普！\x01",
            "我可是下任国王！\x02\x03",
            "为自己买房子也是理所当然的吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#661F#1P哎呀哎呀，\x01",
            "我就知道公爵大人一定有这眼光的。\x02\x03",
            "稍后我会准备合同。\x02\x03",
            "在那之前，我们再干一杯吧……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0)

    ChrTalk(
        0xA,
        "#481F#2P哦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1P您好～\x01",
            "我们是游击士协会的人。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_3461():
        OP_6D(-380, 0, 39240, 2000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3461)
    OP_43(0x101, 0x1, 0x0, 0xE)
    OP_43(0x102, 0x1, 0x0, 0xF)
    OP_43(0x105, 0x1, 0x0, 0x10)
    SetChrSubChip(0xA, 1)
    OP_8C(0xB, 135, 400)
    WaitChrThread(0x105, 0x1)

    ChrTalk(
        0x8,
        "#663F你们是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#480F嗝……\x01",
            "你们是什么人？\x02\x03",
            "我好像在哪见过你们……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#721F哦哦，是上次的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F您好，管家先生。\x02\x03",
            "我们今天来\x01",
            "是想向市长先生请教一件事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#662F这种行为实在令人困扰……\x02\x03",
            "身为协会的游击士，\x01",
            "我想你们应该很清楚什么叫礼数吧。\x02\x03",
            "我和公爵大人在谈很重要的事情，\x01",
            "所以麻烦你们改天再来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F因为事出紧急，\x01",
            "如有失礼之处还请市长多多见谅。\x02\x03",
            "这件事其实是，\x01",
            "我们终于找到纵火事件的犯人了……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#664F是这件事吗……那就没办法了。\x02\x03",
            "#661F公爵大人，\x01",
            "我可以离开片刻吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#227F嗝……\x01",
            "不，在这里说就好了。\x02\x03",
            "我也很想听听是什么事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#663F可、可是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F这样不是更好嘛⊙\x01",
            "连公爵大人都这么说了。\x02\x03",
            "反正又不是什么见不得人的事情。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 1)

    ChrTalk(
        0x8,
        (
            "#662F算了，反正又不是……\x02\x03",
            "说起来，\x01",
            "特蕾莎院长他们昨晚又受到了袭击。\x02\x03",
            "是和纵火事件的同一批犯人所做的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F这种可能性很高。\x02\x03",
            "不过非常遗憾，\x01",
            "一部分的犯案人员逃掉了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#662F是吗……\x02\x03",
            "虽然没全部捉拿归案，\x01",
            "不过能找到犯人就已经很不错了。\x02\x03",
            "那么犯人究竟是谁？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯，这个嘛。\x02\x03",
            "这些犯人究竟是谁，\x01",
            "我想市长先生也应该心里有底了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#664F是吗……那真是遗憾。\x02\x03",
            "我本想他们总有一天\x01",
            "会浪子回头痛改前非的……\x02\x03",
            "看来……\x01",
            "这也只是我的一厢情愿罢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F咦？市长先生。\x01",
            "您这是在说谁啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#661F谁？这还用问吗……\x02\x03",
            "当然是在说\x01",
            "『渡鸦帮』的那些流氓了。\x02\x03",
            "我听说他们从昨晚起就一直行踪不明，\x01",
            "当然真正的犯人就是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F很遗憾……\x01",
            "他们并不是犯人。\x02\x03",
            "在这次的事件中，\x01",
            "他们甚至应该说是受害者才对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#663F什、什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#502F这次事件的犯人，就是……\x02",
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
            "【戴尔蒙市长】\x01",        # 0
            "【杜南公爵】\x01",          # 1
            "【秘书基尔巴特】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3AE1"),
        (1, "loc_3B23"),
        (2, "loc_3CAA"),
        (SWITCH_DEFAULT, "loc_3D1F"),
    )


    label("loc_3AE1")

    OP_20(0x3E8)
    Sleep(1000)
    OP_1D(0x51)

    ChrTalk(
        0x101,
        "#005F#3S就是你，戴尔蒙市长！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Jump("loc_3D1F")

    label("loc_3B23")

    Sleep(400)

    ChrTalk(
        0x101,
        "#005F#3S就是你，杜南公爵！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_9E(0xA, 0xF, 0x0, 0x12C, 0xFA0)
    OP_62(0xA, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0xA,
        "#484F什、什么！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#721F是、是不是\x01",
            "什么地方弄错了！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#018F艾丝蒂尔……\x01",
            "你在说什么啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        "#045F艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F嘿嘿，不好意思说错了。\x02\x03",
            "#502F……这次事件的犯人，那就是……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3C52():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3C52)

    def lambda_3C60():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3C60)
    OP_20(0x3E8)
    Sleep(1000)
    OP_1D(0x51)

    ChrTalk(
        0x101,
        "#005F#3S就是你，戴尔蒙市长！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Jump("loc_3D1F")

    label("loc_3CAA")


    ChrTalk(
        0x101,
        (
            "#002F市长秘书基尔巴特！\x02\x03",
            "而其幕后主使就是……\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    Sleep(1000)
    OP_1D(0x51)

    ChrTalk(
        0x101,
        "#005F#3S就是你，戴尔蒙市长！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Jump("loc_3D1F")

    label("loc_3D1F")


    ChrTalk(
        0x8,
        "#663F！！！\x02",
    )

    OP_9E(0x8, 0xF, 0x0, 0x12C, 0xFA0)
    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F你的秘书基尔巴特\x01",
            "已经在昨晚当场被捕了。\x02\x03",
            "而且还做出了\x01",
            "受戴尔蒙市长指使、\x01",
            "雇凶烧毁孤儿院并抢夺捐款的证言。\x02\x03",
            "这证言应该没有错吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#665F胡、胡说八道！\x02\x03",
            "我才不认识那帮黑衣家伙！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F哎～？奇怪了。\x02\x03",
            "我们刚刚可完全\x01",
            "没提到什么黑衣家伙啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#666F呜……\x02\x03",
            "我不知道！我什么都不知道！\x01",
            "一切都是那个秘书擅自做的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F大叔你还真是厚颜无耻啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F因为孤儿院会妨碍到\x01",
            "市长你建造高级别墅区的计划。\x02\x03",
            "到了现在，你还想为自己开脱罪行吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#665F太纠缠不休了，你们！\x02\x03",
            "的确，我从很早之前\x01",
            "就开始计划别墅区的开发！\x02\x03",
            "但是，那只不过是\x01",
            "卢安地区今后发展的其中一环！\x02\x03",
            "难道我为了完成区区一个建筑计划，\x01",
            "就会不惜犯罪来急着完成它！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F这、这个……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 11020, 0, 36640, 270)

    NpcTalk(
        0x9,
        "男人的声音",
        (
            "#1P……那是因为\x01",
            "你欠下了庞大的债务吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_409E():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_409E)

    def lambda_40AC():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_40AC)

    def lambda_40BA():

        label("loc_40BA")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_40BA")

    QueueWorkItem2(0x102, 1, lambda_40BA)

    def lambda_40CB():

        label("loc_40CB")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_40CB")

    QueueWorkItem2(0x105, 1, lambda_40CB)
    Sleep(200)

    def lambda_40E1():

        label("loc_40E1")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_40E1")

    QueueWorkItem2(0x101, 1, lambda_40E1)
    SetChrFlags(0x9, 0x4)
    OP_8E(0x9, 0xC26, 0x0, 0x8FB6, 0xBB8, 0x0)
    ClearChrFlags(0x9, 0x4)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x105, 0xFF)

    ChrTalk(
        0x101,
        "#004F奈、奈尔！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F为什么会在这里……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#141F哟，我来这里\x01",
            "是想采访戴尔蒙市长的。\x01",
            "刚好在外面看见你们走了进来。\x02\x03",
            "我估计大概是有什么事，\x01",
            "才刚进来就见到了这种情况。\x02\x03",
            "#147F哎呀～\x01",
            "我从头到尾都听见了哦㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#663F你、你是什么人！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F啊，我是《利贝尔通讯》的记者，\x01",
            "奈尔·班兹。\x02\x03",
            "其实是这样的。\x01",
            "我这段时间一直在\x01",
            "调查卢安市最近的财政情况……\x02\x03",
            "戴尔蒙市长，您……\x01",
            "透支了卢安市的预算吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_42CA():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_42CA)

    def lambda_42D8():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_42D8)

    def lambda_42E6():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_42E6)

    def lambda_42F4():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_42F4)
    SetChrSubChip(0xA, 0)

    ChrTalk(
        0x8,
        (
            "#663F……这、这个……\x02\x03",
            "这是用作建造别墅区的资金……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#142F这可说不通。\x01",
            "施工还完全没有开始呢。\x02\x03",
            "我觉得有点不寻常，\x01",
            "就去王都的飞艇公社\x01",
            "调查了一下你乘坐的飞艇的记录。\x02\x03",
            "结果，大～吃一惊啊。\x02\x03",
            "就在一年之前，\x01",
            "你去了共和国好几次是吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#663F……只、只是旅游性质……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#145F这是表面理由吧。\x02\x03",
            "真正的理由是……\x01",
            "你在那里进行了投机买卖，\x01",
            "并且落得损失惨重的结果对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#666F！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F那个……投机买卖是什么啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#043F就是利用市场的价格差\x01",
            "来赚钱的交易行当。\x02\x03",
            "比如趁低价时购入某一商品，\x01",
            "然后再趁高价时将商品抛出……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F哦，原来是这样啊。\x02\x03",
            "那么，这个市长\x01",
            "到底损失了多少钱呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#140F就我在共和国的\x01",
            "记者朋友调查所知……\x02\x03",
            "大约也有一亿米拉。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#005F#3S一、一、一亿米拉～！！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F是捐款数额的一百倍啊……\x02\x03",
            "的确，为了偿还这巨额借款，\x01",
            "甘心染指犯罪也不足为奇了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#481F嗝，一亿啊……\x02\x03",
            "#483F虽然我也是挥金如土，\x01",
            "但没想到你比我还厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#666F呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F这种事也要拿来比啊～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#145F总之，因为这个原因……\x02\x03",
            "你为了偿还巨额借款\x01",
            "而动用了卢安市的预算，\x01",
            "但这也只是拆东墙补西墙罢了。\x02\x03",
            "我还在猜你下一步会怎么做的时候，\x01",
            "没想到你居然不惜放火抢劫\x01",
            "来建造什么高级别墅区。\x02\x03",
            "#141F怎么说呢……\x01",
            "还真是走投无路了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#664F…………………………\x02\x03",
            "哼，你有证据吗？\x02\x03",
            "#665F你敢把这种臆测当作新闻写出去试试。\x01",
            "我一定会告你侵害现任市长的名誉！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#143F哎呀，翻脸了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#665F你们几个也一样！\x02\x03",
            "游击士协会根本就没权\x01",
            "逮捕身为市长的我！\x02\x03",
            "你们，马上给我出去！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F哼，果然使出了这一招。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F看来你对自己身为市长的权力\x01",
            "倒是知道得很清楚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#049F……………………………\x02\x03",
            "市长，有一点……\x01",
            "可以请你回答一下吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#665F你又怎么会在这里！？\x02\x03",
            "身为王立学院的学生，\x01",
            "怎么能跟这些人混在一起……\x02\x03",
            "快点回学院去！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#042F………………………………\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "科洛丝以凛然的眼神\x01",
            "直视着恼火中的戴尔蒙市长。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        "#663F呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#043F为什么你不以自己的财产\x01",
            "来偿还投机欠下借款呢？\x02\x03",
            "一亿米拉的确是很大的数目……\x02\x03",
            "但是以戴尔蒙家族的财力，\x01",
            "我想应该还是可以偿还的。\x02\x03",
            "比如说，\x01",
            "这幢大宅就已经值一亿米拉了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#665F说、说什么蠢话……！\x02\x03",
            "这幢房子，可是我先祖代代相传的，\x01",
            "也是我戴尔蒙家族的骄傲！\x02\x03",
            "怎么能够拿去卖掉！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#049F其实孤儿院也是一样。\x02\x03",
            "对我和老师他们来说，\x01",
            "那是个充满珍贵回忆的地方……\x02\x03",
            "谁都没有权利\x01",
            "去破坏这一份回忆……\x02\x03",
            "#042F而为什么你却……\x01",
            "能够做出那种事情来？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#668F别、别把那间破烂的小屋\x01",
            "和我这幢大宅混为一谈！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#047F你终究还是只在乎你自己……\x01",
            "　\x02\x03",
            "你仅仅只在乎\x01",
            "作为卢安市长的自己，\x01",
            "和作为戴尔蒙家族主人的自己而已。\x02\x03",
            "#049F真是可怜的人……\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x8, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x8,
        "#668F……………………………\x02",
    )

    CloseMessageWindow()
    OP_9E(0x8, 0xF, 0x0, 0x190, 0x1388)

    ChrTalk(
        0x8,
        (
            "#667F……哼哼……哼哼哼哼哼………\x02\x03",
            "说得真好啊，小丫头……\x02\x03",
            "……既然事已至此，\x01",
            "那我也不用顾虑什么后果了！\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrPos(0x8, -2230, 0, 39700, 90)
    SetChrSubChip(0xA, 2)
    OP_0D()
    OP_8C(0x8, 270, 400)

    def lambda_4DA5():
        OP_6D(-2940, 0, 40120, 2000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4DA5)
    OP_8E(0x8, 0xFFFFE2F0, 0x0, 0x9EB6, 0xBB8, 0x0)
    Sleep(500)
    OP_20(0x5DC)
    OP_72(0x10, 0x800)
    OP_22(0x70, 0x0, 0x64)
    OP_72(0x10, 0x10)
    OP_70(0x10, 0x12C)
    Sleep(1500)

    ChrTalk(
        0x8,
        (
            "#667F#3S飞球，野马！#2S\x02\x03",
            "#3S进餐的时间到了，出来吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0xFFFFE2D2, 0x0, 0x98DA, 0xBB8, 0x0)
    TurnDirection(0x8, 0x101, 400)
    OP_73(0x10)

    ChrTalk(
        0x101,
        "#580F#1P什、什么呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#016F#1P是魔兽的气息……！\x02",
    )

    CloseMessageWindow()

    def lambda_4E8A():
        OP_6D(-500, 0, 39570, 3000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4E8A)

    def lambda_4EA2():
        OP_6C(291000, 4000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_4EA2)

    def lambda_4EB2():
        OP_6B(3100, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4EB2)
    OP_1D(0x56)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 6)
    SetChrPos(0xE, -9610, 0, 41180, 0)
    OP_8E(0xE, 0xFFFFE4B2, 0x0, 0x9F4C, 0xFA0, 0x0)
    OP_8E(0xE, 0xFFFFEFB6, 0x0, 0xA276, 0xFA0, 0x0)
    TurnDirection(0xE, 0x101, 400)
    SetChrChipByIndex(0xE, 5)
    OP_43(0xE, 0x1, 0x0, 0x2)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 21)
    SetChrPos(0xF, -9610, 0, 41180, 0)
    OP_8E(0xF, 0xFFFFE4B2, 0x0, 0x9F4C, 0x1388, 0x0)
    OP_8E(0xF, 0xFFFFEE26, 0x0, 0x9844, 0x1388, 0x0)
    TurnDirection(0xF, 0x101, 400)
    SetChrChipByIndex(0xF, 20)
    OP_43(0xF, 0x1, 0x0, 0x2)

    ChrTalk(
        0x9,
        "#144F#3P这、这两只是什么东西啊！？\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0xA,
        (
            "#484F#4P魔、魔兽～！？\x02\x03",
            "#228F呜……呜呜呜……\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x20C, 0x0, 0x64)
    SetChrSubChip(0xA, 3)
    Sleep(500)
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(
        0xB,
        "#721F公、公爵大人！？\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xB, 0x30C, 0x0, 0x9F06, 0xBB8, 0x0)
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(
        0x105,
        (
            "#042F真是难以置信……\x01",
            "你竟然私自饲养魔兽……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#667F#6P哼哼哼……\x02\x03",
            "只要把你们全部杀光，\x01",
            "就没人知道这件事的真相了……\x02\x03",
            "放心吧。它们吃剩的部分，\x01",
            "我会帮你们扔进河里去的。\x02\x03",
            "呀————哈、哈、哈！\x02",
        )
    )

    CloseMessageWindow()
    OP_94(0x1, 0x9, 0xB4, 0x3E8, 0xBB8, 0x0)

    ChrTalk(
        0x9,
        "#142F#3P这、这家伙疯了……\x02",
    )

    CloseMessageWindow()

    def lambda_5132():
        OP_6D(1064, 0, 38330, 1000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_5132)

    def lambda_514A():
        OP_6C(315000, 1000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_514A)

    def lambda_515A():
        OP_6B(2800, 800)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_515A)
    SetChrChipByIndex(0xE, 6)
    OP_96(0xE, 0x226, 0x5DC, 0x9646, 0x7D0, 0x1770)
    OP_22(0xEC, 0x0, 0x64)
    Fade(500)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x19, 0x100)
    ClearChrFlags(0x17, 0x100)
    ClearChrFlags(0x18, 0x100)
    SetChrPos(0x17, 320, 1000, 39500, 0)
    SetChrPos(0x18, -100, 1500, 38100, 0)
    SetChrPos(0x19, 700, 1450, 38140, 0)
    OP_51(0x19, 0x2A, (scpexpr(EXPR_PUSH_LONG, 0x7530), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x2B, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x2C, (scpexpr(EXPR_PUSH_LONG, 0xFFFDF0A8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x2A, (scpexpr(EXPR_PUSH_LONG, 0x7530), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x2B, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x2C, (scpexpr(EXPR_PUSH_LONG, 0xFFFEA070), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x2A, (scpexpr(EXPR_PUSH_LONG, 0x7530), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x2B, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x2C, (scpexpr(EXPR_PUSH_LONG, 0xFFFD40E0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    SetChrChipByIndex(0xE, 5)
    OP_43(0xE, 0x1, 0x0, 0x2)
    OP_0D()
    OP_22(0x195, 0x0, 0x64)

    ChrTalk(
        0xE,
        "#4P嗷呜呜呜呜……\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xF, 21)
    OP_96(0xF, 0x1B8, 0x5DC, 0x8C82, 0x7D0, 0x1770)
    OP_22(0xEC, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    SetChrChipByIndex(0xF, 20)
    OP_43(0xF, 0x1, 0x0, 0x2)
    Sleep(500)
    OP_22(0x195, 0x0, 0x64)

    ChrTalk(
        0xF,
        "#4P……嗷呜呜……………\x02",
    )

    CloseMessageWindow()

    def lambda_5355():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5355)
    Sleep(100)

    def lambda_5370():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5370)
    Sleep(100)

    def lambda_538B():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_538B)
    WaitChrThread(0x101, 0x1)
    SetChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0x101, 8)
    WaitChrThread(0x102, 0x1)
    SetChrFlags(0x102, 0x1000)
    SetChrChipByIndex(0x102, 9)
    WaitChrThread(0x105, 0x1)
    SetChrFlags(0x105, 0x1000)
    SetChrChipByIndex(0x105, 10)

    ChrTalk(
        0x101,
        (
            "#002F没、没想到竟然要\x01",
            "在这种房子里和魔兽战斗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F但这样一来，\x01",
            "就可以将市长作为现行犯逮捕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#047F虽然我和你们并无仇恨，\x01",
            "但是……\x02\x03",
            "#046F如果你们想伤害大家的话，\x01",
            "我决不会允许！\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xE, 7)
    SetChrFlags(0xE, 0x20)
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_54A7():
        OP_96(0xFE, 0x132E, 0x0, 0x9632, 0xBB8, 0x1770)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_54A7)
    Sleep(150)
    SetChrChipByIndex(0xF, 22)
    SetChrFlags(0xF, 0x20)
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_54DF():
        OP_96(0xFE, 0x132E, 0x0, 0x8A7A, 0x9C4, 0x1770)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_54DF)
    Sleep(400)
    Battle(0x394, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_5515"),
        (SWITCH_DEFAULT, "loc_5518"),
    )


    label("loc_5515")

    OP_B4(0x0)
    Return()

    label("loc_5518")

    OP_A2(0x3FB)
    NewScene("ED6_DT01/T2210   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_3014 end

    def Function_13_5525(): pass

    label("Function_13_5525")

    EventBegin(0x0)
    OP_1D(0x51)
    OP_4A(0x8, 255)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xA, -50, 200, 40550, 180)
    SetChrSubChip(0xA, 3)
    SetChrPos(0xB, 780, 0, 40710, 225)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x19, 0x100)
    ClearChrFlags(0x17, 0x100)
    ClearChrFlags(0x18, 0x100)
    SetChrPos(0x17, 320, 1000, 39500, 0)
    SetChrPos(0x18, -100, 1500, 38100, 0)
    SetChrPos(0x19, 700, 1450, 38140, 0)
    OP_51(0x19, 0x2A, (scpexpr(EXPR_PUSH_LONG, 0x7530), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x2B, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x2C, (scpexpr(EXPR_PUSH_LONG, 0xFFFDF0A8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x2A, (scpexpr(EXPR_PUSH_LONG, 0x7530), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x2B, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x2C, (scpexpr(EXPR_PUSH_LONG, 0xFFFEA070), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x2A, (scpexpr(EXPR_PUSH_LONG, 0x7530), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x2B, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x2C, (scpexpr(EXPR_PUSH_LONG, 0xFFFD40E0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x10, 300)
    OP_72(0x10, 0x10)
    OP_44(0xF, 0xFF)
    OP_44(0xE, 0xFF)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xE, 0x80)
    OP_6D(-5830, 0, 39000, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(346000, 0)
    OP_6E(280, 0)
    SetChrPos(0x8, -5850, 0, 40270, 180)
    SetChrPos(0x101, -5500, 0, 35010, 0)
    SetChrPos(0x102, -6750, 0, 35300, 0)
    SetChrPos(0x105, -4320, 0, 35440, 0)
    SetChrPos(0x9, -2140, 0, 42020, 270)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#668F不、不可能……\x01",
            "我忠实的爱犬竟然……\x02\x03",
            "这群混蛋，看你们做的好事！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F呼～呼～……\x01",
            "这句话应该是我们说才对！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F现根据游击士协会的规定，\x01",
            "我们要将你作为现行犯逮捕归案。\x02\x03",
            "请你不要再做多余的抵抗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#667F嘿嘿嘿嘿嘿……\x02\x03",
            "这样的话没办法了……\x01",
            "只有亮出我的最后底牌了！\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x8, 18)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        "#580F哎！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F手杖……？\x02",
    )

    CloseMessageWindow()

    def lambda_5898():
        OP_91(0xFE, 0x0, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5898)
    Sleep(100)

    def lambda_58B8():
        OP_6C(315000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_58B8)

    def lambda_58C8():
        OP_6D(-6640, 0, 41150, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_58C8)

    def lambda_58E0():
        OP_90(0xFE, 0x0, 0x0, 0x170C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_58E0)

    def lambda_58FB():
        OP_90(0xFE, 0x0, 0x0, 0x170C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_58FB)

    def lambda_5916():
        OP_90(0xFE, 0x0, 0x0, 0x170C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5916)
    Sleep(600)
    OP_22(0xC5, 0x0, 0x64)
    OP_44(0x8, 0xFF)
    LoadEffect(0x0, "map\\\\mp006_00.eff")
    PlayEffect(0x0, 0x0, 0x8, -350, 1100, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(
        0x8,
        "#665F时间啊，停止吧！\x05\x02",
    )

    FadeToDark(1, 16777215, -1)
    OP_44(0x9, 0xFF)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0x105, 0x1)
    OP_0D()
    OP_43(0x101, 0x1, 0x0, 0x15)
    FadeToBright(400, 16777215)
    Sleep(500)
    OP_9E(0x101, 0xF, 0x0, 0x12C, 0xFA0)
    Sleep(700)
    OP_9E(0x101, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x101,
        "#581F身、身体动不了了……！\x02",
    )

    CloseMessageWindow()
    OP_9E(0x102, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x102,
        (
            "#513F这、这是……\x01",
            "导力魔法吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x105, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x105,
        (
            "#541F不、不是……\x02\x03",
            "这恐怕是古代遗物的力量！\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x9, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x9,
        "#144F那是什么东西！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#667F#2P呵呵，科洛丝还真是博学。\x02\x03",
            "这就是我戴尔蒙家族的传家之宝，\x01",
            "古代遗物『封印宝杖』……\x02\x03",
            "它拥有让一定范围内的人\x01",
            "完全无法动弹的力量。\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x101, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x101,
        "#581F怎、怎么有这种荒唐的力量……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#513F竟然还有这样强大的古代遗物\x01",
            "未被教会回收而流传在外……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#667F#2P呵呵……\x01",
            "不愧是古代文明的智慧结晶。\x02\x03",
            "拥有着战术导力器\x01",
            "所无法比拟的力量啊。\x02\x03",
            "不过……\x01",
            "缺点就是只有这一项功能。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x8, 19)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#667F#2P没办法。\x01",
            "只好由我来亲手了结你们了。\x02\x03",
            "呵呵呵……你们感到很荣幸吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5CA8():
        OP_6D(-6640, 0, 40150, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5CA8)
    OP_92(0x8, 0x101, 0x76C, 0x3E8, 0x0)

    ChrTalk(
        0x8,
        (
            "#667F#2P那么首先第一个……\x01",
            "就从狂妄的小丫头开始吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x101, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x101,
        "#009F哼，谁是狂妄的小丫头啊！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 200)

    ChrTalk(
        0x8,
        (
            "#667F#2P而自以为是的小丫头\x01",
            "就留到最后解决好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x105, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x105,
        "#042F…………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 200)

    ChrTalk(
        0x8,
        (
            "#667F#2P呵呵呵……\x01",
            "刚才的气势跑到哪里去了？\x02\x03",
            "要是现在乖乖求饶，\x01",
            "或许我会大发慈悲放过你们哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x101, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x101,
        "#005F谁、谁要向你这种家伙……\x02",
    )

    CloseMessageWindow()
    OP_9E(0x102, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x102,
        "#013F别用你那……脏手……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#663F#2P什么？\x02",
    )

    CloseMessageWindow()

    def lambda_5E94():
        OP_9E(0x102, 0xF, 0x0, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5E94)

    ChrTalk(
        0x102,
        (
            "#510F别用你那脏手碰艾丝蒂尔……\x02\x03",
            "要是……\x01",
            "你敢动她一根头发的话……\x02\x03",
            "我一定不惜一切代价，\x01",
            "让你尸骨无存……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x8,
        "#668F#2P什……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F约、约修亚……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#044F约修亚……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#666F#2P你、你根本连一根指头都动不了，\x01",
            "还敢在我面前说狠话……\x02\x03",
            "#666F好吧！\x01",
            "我就先解决你再说！\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x8, 0x102, 0x4B0, 0x3E8, 0x0)
    TurnDirection(0x8, 0x102, 400)
    Sleep(400)
    OP_9E(0x101, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x101,
        (
            "#005F住、住手！\x02\x03",
            "你要是敢伤害约修亚，\x01",
            "我艾丝蒂尔绝对不会放过你！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#510F……………………………\x02",
    )

    CloseMessageWindow()
    OP_9E(0x105, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x105,
        "#043F约修亚！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#667F#2P去死吧。\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_44(0x101, 0xFF)

    def lambda_60AD():
        OP_9E(0x101, 0xF, 0x0, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_60AD)

    ChrTalk(
        0x101,
        "#504F不要啊啊啊啊啊啊啊啊！！！！\x02",
    )

    CloseMessageWindow()
    OP_22(0x90, 0x0, 0x64)
    LoadEffect(0x1, "map\\\\mp007_01.eff")
    PlayEffect(0x1, 0x2, 0x101, 350, 800, 200, 0, 0, 0, 100, 100, 100, 0xFF, 0, 0, 0, 0)
    OP_77(0xBE, 0xBE, 0xBE, 0x7D000, 0x0)
    OP_0D()
    Sleep(1600)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x8,
        "#668F#2P什……！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)
    OP_8F(0x8, 0xFFFFE87C, 0x0, 0xA1B8, 0xBB8, 0x0)
    OP_77(0xA0, 0xA0, 0xA0, 0x3E800, 0x0)

    ChrTalk(
        0x105,
        "#044F这光是……\x02",
    )

    CloseMessageWindow()
    OP_77(0x82, 0x82, 0x82, 0x3E800, 0x0)

    ChrTalk(
        0x9,
        (
            "#142F#3P可恶……\x01",
            "要是手能动的话就能拍照了……\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x91, 0x0, 0x64)
    LoadEffect(0x1, "map\\\\mp015_00.eff")
    PlayEffect(0x1, 0x3, 0x101, 350, 800, 200, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_77(0x64, 0x64, 0x64, 0x1F400, 0x0)
    Sleep(500)
    OP_23(0x90)
    OP_82(0x2, 0x2)
    OP_82(0x0, 0x2)
    OP_77(0xFF, 0xFF, 0xFF, 0x3E800, 0x0)
    Sleep(1500)

    ChrTalk(
        0x8,
        "#668F什、什什什什么——！？\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_51(0x101, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    Sleep(50)
    OP_44(0x102, 0xFF)
    OP_51(0x102, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    Sleep(50)
    OP_44(0x105, 0xFF)
    OP_51(0x105, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x105, 65535)
    SetChrSubChip(0x105, 0)
    Sleep(500)

    ChrTalk(
        0x105,
        "#044F身体……能动了？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#014F艾丝蒂尔……刚才那黑色的光是？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F啊、嗯……\x02\x03",
            "是寄给老爸的\x01",
            "那个黑色导力器……\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 25)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -5500, 500, 38500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        "#505F好像是那东西发出来的光……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#668F这、这怎么可能……\x02\x03",
            "#668F我戴尔蒙家族祖传的古代遗物\x01",
            "怎么可能被这种东西破坏！\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x1A, 0x80)
    SetChrChipByIndex(0x101, 65535)

    def lambda_6403():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6403)

    def lambda_6411():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6411)

    def lambda_641F():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_641F)

    ChrTalk(
        0x102,
        (
            "#015F不管怎样……\x01",
            "现在你的手上已经没有底牌了。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x1F5, 0x0, 0x64)
    SetChrChipByIndex(0x102, 9)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#012F还是面对现实吧。\x01",
            "戴尔蒙，你已经无处可逃了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F没、没错！\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x1F4, 0x0, 0x64)
    SetChrChipByIndex(0x101, 8)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#005F刚才你竟敢\x01",
            "用那种无耻的手法整我们～！\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x1F8, 0x0, 0x64)
    SetChrChipByIndex(0x105, 10)
    OP_0D()

    ChrTalk(
        0x105,
        "#042F真卑劣……\x02",
    )

    CloseMessageWindow()
    OP_9E(0x8, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x8,
        (
            "#666F呜呜呜呜呜呜呜……\x02\x03",
            "……你们休想抓住我！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6567():

        label("loc_6567")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_6567")

    QueueWorkItem2(0x101, 1, lambda_6567)

    def lambda_6578():

        label("loc_6578")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_6578")

    QueueWorkItem2(0x102, 1, lambda_6578)

    def lambda_6589():

        label("loc_6589")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_6589")

    QueueWorkItem2(0x105, 1, lambda_6589)
    SetChrChipByIndex(0x8, 0)
    OP_8C(0x8, 270, 800)
    OP_8E(0x8, 0xFFFFDDB4, 0x0, 0x9FBA, 0x1770, 0x0)
    SetChrFlags(0x8, 0x80)

    ChrTalk(
        0x101,
        "#005F啊！\x02",
    )

    CloseMessageWindow()
    OP_1D(0x52)

    ChrTalk(
        0x102,
        "#016F我们快追！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#046F是！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    OP_43(0x101, 0x1, 0x0, 0x11)
    Sleep(400)
    SetChrChipByIndex(0x102, 65535)
    OP_43(0x102, 0x1, 0x0, 0x11)
    Sleep(300)
    SetChrChipByIndex(0x105, 65535)
    OP_43(0x105, 0x1, 0x0, 0x11)
    WaitChrThread(0x105, 0x1)

    ChrTalk(
        0x9,
        (
            "#144F#3P啊啊，等等我！\x02\x03",
            "这、这种爆炸性的新闻，\x01",
            "岂能让我白白错过！！\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x9, 0x1, 0x0, 0x11)
    Sleep(2000)
    OP_6D(-1160, 0, 41000, 2000)

    ChrTalk(
        0xB,
        (
            "#722F哎呀哎呀……\x01",
            "这下非减寿不可……\x02\x03",
            "公爵大人，没事吧，大人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#228F#1P嗯……\x01",
            "有魔兽，魔兽……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x9, 0x80)
    Fade(1000)
    OP_6D(-61080, 0, 54230, 0)
    SetChrPos(0x8, -59900, 0, 51220, 0)

    def lambda_6738():
        OP_8E(0xFE, 0xFFFF0B8C, 0x0, 0xC634, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6738)
    OP_43(0x101, 0x1, 0x0, 0x12)
    Sleep(700)

    def lambda_675F():
        OP_96(0xFE, 0xFFFF0696, 0xFFFFEC78, 0xC724, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_675F)
    OP_43(0x102, 0x1, 0x0, 0x12)
    Sleep(700)
    OP_43(0x105, 0x1, 0x0, 0x12)
    WaitChrThread(0x101, 0x1)
    OP_72(0xF, 0x10)
    OP_6F(0xF, 29)
    Fade(1000)
    OP_6D(-61320, 0, -38840, 0)
    OP_43(0x101, 0x1, 0x0, 0x13)
    Sleep(700)
    OP_43(0x102, 0x1, 0x0, 0x13)
    Sleep(700)
    OP_43(0x105, 0x1, 0x0, 0x13)
    Sleep(2200)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_43(0x9, 0x1, 0x0, 0x14)
    Sleep(500)
    WaitChrThread(0x101, 0x1)
    Sleep(1000)
    SetMapFlags(0x2000000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2200   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_13_5525 end

    def Function_14_680F(): pass

    label("Function_14_680F")

    ClearChrFlags(0xFE, 0x80)
    OP_8F(0xFE, 0x1D4C, 0x0, 0x92C2, 0xFA0, 0x0)
    OP_8F(0xFE, 0xA6E, 0x0, 0x9A1A, 0xFA0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_14_680F end

    def Function_15_6844(): pass

    label("Function_15_6844")

    Sleep(500)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x1D38, 0x0, 0x909C, 0xFA0, 0x0)
    OP_8E(0xFE, 0xD02, 0x0, 0x9416, 0xFA0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_15_6844 end

    def Function_16_687E(): pass

    label("Function_16_687E")

    Sleep(1000)
    ClearChrFlags(0xFE, 0x80)
    OP_8F(0xFE, 0x1D38, 0x0, 0x909C, 0xFA0, 0x0)
    OP_8F(0xFE, 0xFFA, 0x0, 0x968C, 0xFA0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_16_687E end

    def Function_17_68B8(): pass

    label("Function_17_68B8")

    OP_8E(0xFE, 0xFFFFE264, 0x0, 0x9F92, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFCED2, 0x0, 0xA032, 0x1770, 0x0)
    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_17_68B8 end

    def Function_18_68F0(): pass

    label("Function_18_68F0")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -55480, 0, 54970, 0)
    OP_8E(0xFE, 0xFFFF1DB6, 0x0, 0xD692, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF18D4, 0x0, 0xCB66, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF05F6, 0x0, 0xCBFC, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x4)

    def lambda_694D():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_694D)
    OP_96(0xFE, 0xFFFF04CA, 0xFFFFFE0C, 0xC6D4, 0x3E8, 0x1770)
    Sleep(100)
    OP_8F(0xFE, 0xFFFF04CA, 0xFFFFE0C0, 0xC6D4, 0xFA0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_18_68F0 end

    def Function_19_698B(): pass

    label("Function_19_698B")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -62450, 2310, -43030, 270)
    OP_8F(0xFE, 0xFFFF0C0E, 0x3E8, 0xFFFF57EA, 0xFA0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_96(0xFE, 0xFFFF0F9C, 0x0, 0xFFFF57B8, 0xC8, 0xFA0)
    OP_8E(0xFE, 0xFFFF0D8A, 0x0, 0xFFFF6B54, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF04E8, 0x0, 0xFFFF6CD0, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_19_698B end

    def Function_20_69FF(): pass

    label("Function_20_69FF")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -62450, 2310, -43030, 270)
    OP_96(0xFE, 0xFFFF0E02, 0x0, 0xFFFF57EA, 0xC8, 0x1770)
    OP_96(0xFE, 0xFFFF0F9C, 0x0, 0xFFFF57B8, 0x12C, 0x1770)
    Sleep(500)
    OP_8E(0xFE, 0xFFFF0D8A, 0x0, 0xFFFF6B54, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF04E8, 0x0, 0xFFFF6CD0, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_20_69FF end

    def Function_21_6A7B(): pass

    label("Function_21_6A7B")

    OP_77(0xCD, 0xED, 0xF0, 0x0, 0x0)

    label("loc_6A84")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6AAC")
    OP_77(0xCD, 0xED, 0xF0, 0x1F400, 0x0)
    Sleep(1000)
    OP_77(0x8C, 0xCE, 0xFF, 0x1F400, 0x0)
    Sleep(1000)
    Jump("loc_6A84")

    label("loc_6AAC")

    Return()

    # Function_21_6A7B end

    def Function_22_6AAD(): pass

    label("Function_22_6AAD")

    NewScene("ED6_DT01/T2210   ._SN", 123, 1, 0)
    IdleLoop()
    Return()

    # Function_22_6AAD end

    def Function_23_6AB7(): pass

    label("Function_23_6AB7")

    NewScene("ED6_DT01/T2210   ._SN", 121, 1, 0)
    IdleLoop()
    Return()

    # Function_23_6AB7 end

    def Function_24_6AC1(): pass

    label("Function_24_6AC1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "是开合桥的控制装置。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_24_6AC1 end

    SaveToFile()

Try(main)
