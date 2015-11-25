from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3113   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3113.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
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
        '乔丝特',                               # 9
        '吉尔',                                 # 10
        '多伦',                                 # 11
        '士兵的声音',                           # 12
        '男性的声音',                           # 13
        '空贼',                                 # 14
        '空贼',                                 # 15
        '空贼',                                 # 16
        '空贼',                                 # 17
        '空贼',                                 # 18
        '空贼',                                 # 19
        '亲卫队',                               # 20
        '亲卫队',                               # 21
        '亲卫队',                               # 22
        '戴尔蒙市长',                           # 23
        '基尔巴特',                             # 24
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
        'ED6_DT07/CH02130 ._CH',             # 00
        'ED6_DT07/CH02120 ._CH',             # 01
        'ED6_DT07/CH02110 ._CH',             # 02
        'ED6_DT07/CH01380 ._CH',             # 03
        'ED6_DT07/CH01320 ._CH',             # 04
        'ED6_DT07/CH02410 ._CH',             # 05
        'ED6_DT07/CH02420 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH02130P._CP',             # 00
        'ED6_DT07/CH02120P._CP',             # 01
        'ED6_DT07/CH02110P._CP',             # 02
        'ED6_DT07/CH01380P._CP',             # 03
        'ED6_DT07/CH01320P._CP',             # 04
        'ED6_DT07/CH02410P._CP',             # 05
        'ED6_DT07/CH02420P._CP',             # 06
    )

    DeclNpc(
        X                   = -142470,
        Z                   = 0,
        Y                   = -550,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -142390,
        Z                   = 0,
        Y                   = 4030,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -140430,
        Z                   = 0,
        Y                   = 4030,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -8770,
        Z                   = 0,
        Y                   = -4840,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 18140,
        Z                   = 0,
        Y                   = -490,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -132720,
        Z                   = 0,
        Y                   = 1930,
        Direction           = 171,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -131510,
        Z                   = 0,
        Y                   = 2890,
        Direction           = 167,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -130850,
        Z                   = 0,
        Y                   = 1430,
        Direction           = 215,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -124600,
        Z                   = 0,
        Y                   = 2120,
        Direction           = 154,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -123080,
        Z                   = 0,
        Y                   = 2980,
        Direction           = 177,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -123420,
        Z                   = 0,
        Y                   = 950,
        Direction           = 189,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -110610,
        Z                   = 0,
        Y                   = 3930,
        Direction           = 174,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -108510,
        Z                   = 0,
        Y                   = 3910,
        Direction           = 179,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -106630,
        Z                   = 0,
        Y                   = 3280,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -119400,
        Z                   = 0,
        Y                   = 4390,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -115010,
        Z                   = 0,
        Y                   = -550,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 20980,
        TriggerZ            = 0,
        TriggerY            = 158210,
        TriggerRange        = 800,
        ActorX              = 20980,
        ActorZ              = 1000,
        ActorY              = 158210,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -14930,
        TriggerZ            = 0,
        TriggerY            = 1930,
        TriggerRange        = 800,
        ActorX              = -14930,
        ActorZ              = 1000,
        ActorY              = 1930,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -2910,
        TriggerZ            = 0,
        TriggerY            = 1930,
        TriggerRange        = 800,
        ActorX              = -2910,
        ActorZ              = 1000,
        ActorY              = 1930,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7070,
        TriggerZ            = 0,
        TriggerY            = 1930,
        TriggerRange        = 800,
        ActorX              = 7070,
        ActorZ              = 1000,
        ActorY              = 1930,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 23900,
        TriggerZ            = 0,
        TriggerY            = 114940,
        TriggerRange        = 800,
        ActorX              = 23900,
        ActorZ              = 1000,
        ActorY              = 114940,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 23900,
        TriggerZ            = 0,
        TriggerY            = 126940,
        TriggerRange        = 800,
        ActorX              = 23900,
        ActorZ              = 1000,
        ActorY              = 126940,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 23900,
        TriggerZ            = 0,
        TriggerY            = 138940,
        TriggerRange        = 800,
        ActorX              = 23900,
        ActorZ              = 1000,
        ActorY              = 138940,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3DE",          # 00, 0
        "Function_1_41B",          # 01, 1
        "Function_2_454",          # 02, 2
        "Function_3_46A",          # 03, 3
        "Function_4_1044",         # 04, 4
        "Function_5_1088",         # 05, 5
        "Function_6_10B8",         # 06, 6
        "Function_7_10E8",         # 07, 7
        "Function_8_1118",         # 08, 8
        "Function_9_1148",         # 09, 9
        "Function_10_118F",        # 0A, 10
        "Function_11_11E5",        # 0B, 11
        "Function_12_1227",        # 0C, 12
        "Function_13_1273",        # 0D, 13
        "Function_14_12B0",        # 0E, 14
        "Function_15_1414",        # 0F, 15
        "Function_16_1889",        # 10, 16
        "Function_17_1962",        # 11, 17
        "Function_18_1A01",        # 12, 18
        "Function_19_1AF5",        # 13, 19
    )


    def Function_0_3DE(): pass

    label("Function_0_3DE")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (102, "loc_3EE"),
        (104, "loc_404"),
        (SWITCH_DEFAULT, "loc_41A"),
    )


    label("loc_3EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_401")
    OP_A2(0x56C)
    Event(0, 3)

    label("loc_401")

    Jump("loc_41A")

    label("loc_404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_417")
    OP_A2(0x56E)
    Event(0, 16)

    label("loc_417")

    Jump("loc_41A")

    label("loc_41A")

    Return()

    # Function_0_3DE end

    def Function_1_41B(): pass

    label("Function_1_41B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 4)), scpexpr(EXPR_END)), "loc_427")
    OP_1B(0x1, 0x0, 0xE)

    label("loc_427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 4)), scpexpr(EXPR_END)), "loc_433")
    OP_1B(0x0, 0x0, 0xF)

    label("loc_433")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_443")
    OP_72(0x12, 0x10)
    Jump("loc_447")

    label("loc_443")

    OP_64(0x0, 0x1)

    label("loc_447")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 3)), scpexpr(EXPR_END)), "loc_453")
    OP_22(0xAC, 0x1, 0x50)

    label("loc_453")

    Return()

    # Function_1_41B end

    def Function_2_454(): pass

    label("Function_2_454")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_469")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_454")

    label("loc_469")

    Return()

    # Function_2_454 end

    def Function_3_46A(): pass

    label("Function_3_46A")

    EventBegin(0x0)
    OP_24(0xAC, 0x3C)
    OP_6D(-98070, 0, 2550, 0)
    OP_67(0, 8870, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(0, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -150200, 3000, 3950, 90)
    SetChrPos(0x102, -150200, 3000, 3950, 90)
    SetChrPos(0x106, -150200, 3000, 3950, 90)
    SetChrPos(0x107, -150200, 3000, 3950, 90)
    SetChrPos(0x10B, -150200, 3000, 3950, 90)
    FadeToBright(2000, 0)

    def lambda_511():
        OP_6D(-142510, 0, 2940, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_511)
    WaitChrThread(0x101, 0x1)
    Fade(1000)
    OP_6D(-142510, 0, 2940, 0)
    OP_67(0, 6470, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#215F#1P我、我说……\x01",
            "总觉得外面好像很吵啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#200F啊……\x01",
            "好像有入侵者。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#192F啥，有入侵者……\x02\x03",
            "#196F呆不下去了！\x01",
            "趁此机会逃狱吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#203F大哥，饶了我吧。\x01",
            "哪有这么简单就能逃狱的……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_639():
        OP_6D(-146150, 0, -10, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_639)
    OP_43(0x101, 0x1, 0x0, 0x4)
    Sleep(600)
    OP_43(0x102, 0x1, 0x0, 0x5)
    Sleep(600)
    OP_43(0x107, 0x1, 0x0, 0x6)
    Sleep(600)
    OP_43(0x10B, 0x1, 0x0, 0x8)
    Sleep(600)
    OP_43(0x106, 0x1, 0x0, 0x7)
    WaitChrThread(0x102, 0x1)

    ChrTalk(
        0x102,
        (
            "#012F这里……\x01",
            "看来是地牢啊。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#501F嗯，和哈肯大门相比，\x01",
            "要塞地牢的规模要大多了……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6EE():
        OP_6D(-142480, 0, -140, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6EE)

    def lambda_706():
        OP_6C(13000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_706)

    def lambda_716():
        OP_6B(3170, 2000)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_716)

    def lambda_726():

        label("loc_726")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_726")

    QueueWorkItem2(0x107, 1, lambda_726)

    def lambda_737():

        label("loc_737")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_737")

    QueueWorkItem2(0x102, 1, lambda_737)

    def lambda_748():

        label("loc_748")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_748")

    QueueWorkItem2(0x10B, 1, lambda_748)

    def lambda_759():

        label("loc_759")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_759")

    QueueWorkItem2(0x106, 1, lambda_759)

    def lambda_76A():
        OP_8E(0xFE, 0xFFFDD2B2, 0x0, 0xFFFFF5D8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_76A)
    Sleep(100)

    def lambda_78A():
        OP_8E(0xFE, 0xFFFDD636, 0x0, 0xFFFFF240, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_78A)
    Sleep(300)

    def lambda_7AA():
        OP_8E(0xFE, 0xFFFDD3FC, 0x0, 0xFFFFEFD4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7AA)

    def lambda_7C5():
        OP_8E(0xFE, 0xFFFDCE52, 0x0, 0xFFFFEE80, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 2, lambda_7C5)
    Sleep(200)

    def lambda_7E5():
        OP_8E(0xFE, 0xFFFDCE2A, 0x0, 0xFFFFF25E, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_7E5)
    WaitChrThread(0x101, 0x2)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x101,
        "#004F咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#213F#5P啊。\x02",
    )

    CloseMessageWindow()

    def lambda_846():

        label("loc_846")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_846")

    QueueWorkItem2(0x101, 1, lambda_846)

    def lambda_857():

        label("loc_857")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_857")

    QueueWorkItem2(0x107, 1, lambda_857)

    def lambda_868():

        label("loc_868")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_868")

    QueueWorkItem2(0x102, 1, lambda_868)

    def lambda_879():

        label("loc_879")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_879")

    QueueWorkItem2(0x10B, 1, lambda_879)

    def lambda_88A():

        label("loc_88A")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_88A")

    QueueWorkItem2(0x106, 1, lambda_88A)

    ChrTalk(
        0x101,
        "#501F哎……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x101)
    OP_63(0x8)

    ChrTalk(
        0x101,
        "#005F#1K#3S啊啊啊啊啊！？\x02",
    )


    ChrTalk(
        0x8,
        "#214F#1K#3S#5P啊啊啊啊啊！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(500)
    OP_56(0x1)
    OP_59()
    SetChrFlags(0x9, 0x4)
    OP_8E(0x9, 0xFFFDD802, 0x0, 0x3F2, 0x1770, 0x0)
    OP_8C(0x9, 180, 400)

    ChrTalk(
        0x9,
        "#201F是、是你们！？\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xA, 0x4)
    OP_8E(0xA, 0xFFFDDC80, 0x0, 0xFFFFFDEE, 0x1388, 0x0)
    TurnDirection(0xA, 0x102, 400)

    ChrTalk(
        0xA,
        "#192F那时候的小鬼！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F该说什么好呢……\x01",
            "真是好久不见了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F是吗……\x01",
            "原来你们被关在这里啊。\x02\x03",
            "#003F…………………………\x02\x03",
            "#506F嗯，那个，还好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#214F#5P哼、哼……\x01",
            "少来假惺惺地可怜我们！\x02\x03",
            "你这个只会耍棍棒的蠢女人！\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F不好意思……\x01",
            "你说什么我都不会生气了。\x02\x03",
            "如果能让你觉得好过点的话，\x01",
            "随便怎么骂好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#216F#5P气、气死人啦～！\x01",
            "你在说什么不痛不痒的话啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#052F喂喂。\x01",
            "你们认识这帮家伙吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F他们是卡普亚空贼团……\x01",
            "劫持定期船『林德号』的犯人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#103F哦，是传说中的空贼啊。\x02\x03",
            "听说你们拥有性能相当高的飞艇。\x01",
            "　\x02\x03",
            "#101F听说是帝国制造的，\x01",
            "能不能告诉我一下规格啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#202F啊、啊啊……\x01",
            "最高时速可是能达到２３００塞尔矩呢……\x02\x03",
            "#201F喂，老头。\x01",
            "为什么我要回答这些啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        "#102F什么嘛，真小气～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#067F哎呀、爷爷啊。\x02\x03",
            "现在好像不是问这个的场合吧……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#190F等、等一下。\x02\x03",
            "说起来……\x01",
            "你们这些游击士怎会在这里的？\x02\x03",
            "难道说刚才的警报声……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        "#100F…………唔…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#562F…………啊…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#053F……那么，我们告辞了。\x02",
    )

    CloseMessageWindow()

    def lambda_DA2():
        OP_6D(-143280, 0, 2210, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_DA2)

    def lambda_DBA():
        OP_6C(0, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_DBA)
    OP_43(0x106, 0x1, 0x0, 0xD)
    OP_43(0x10B, 0x1, 0x0, 0xB)
    OP_43(0x102, 0x1, 0x0, 0xA)
    OP_43(0x107, 0x1, 0x0, 0xC)
    OP_43(0x101, 0x1, 0x0, 0x9)
    Sleep(2000)

    ChrTalk(
        0x8,
        "#214F啊，想蒙混过去！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#201F入侵者就是你们吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#196F拜、拜托～！\x01",
            "把我们也放出去啦～\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_24(0xAC, 0x46)
    OP_6D(-24930, 0, 38220, 0)
    OP_6B(3000, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x10B, 0xFF)
    OP_44(0x107, 0xFF)
    OP_44(0x106, 0xFF)
    SetChrPos(0x101, -25930, 0, 36130, 0)
    SetChrPos(0x102, -24890, 0, 36720, 315)
    SetChrPos(0x10B, -26310, 0, 37690, 135)
    SetChrPos(0x107, -25050, 0, 38100, 225)
    SetChrPos(0x106, -25740, 0, 38770, 180)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x107, 0)
    SetChrSubChip(0x106, 0)
    SetChrSubChip(0x10B, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#007F呼……\x01",
            "真是吓了一跳。\x02\x03",
            "#003F对了……\x01",
            "他们也是和那些黑衣人一伙的啊。\x02\x03",
            "为什么会被理查德上校关起来……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#2P他们可能只是被上校利用了。\x01",
            "　\x02\x03",
            "或许卢安的戴尔蒙市长也是……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#551F嘁，就算如此，\x01",
            "我们也没必要同情他们。\x02\x03",
            "#057F浪费了这么多时间，\x01",
            "快找其他可以逃脱的路线吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x44, 0x1, 0x200)
    EventEnd(0x0)
    Return()

    # Function_3_46A end

    def Function_4_1044(): pass

    label("Function_4_1044")

    OP_8E(0xFE, 0xFFFDC3B2, 0x3E8, 0xF6E, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFDC498, 0x0, 0xFFFFF542, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFDC948, 0x0, 0xFFFFF542, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_4_1044 end

    def Function_5_1088(): pass

    label("Function_5_1088")

    OP_8E(0xFE, 0xFFFDC3B2, 0x3E8, 0xF6E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDC524, 0x0, 0xFFFFF196, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_5_1088 end

    def Function_6_10B8(): pass

    label("Function_6_10B8")

    OP_8E(0xFE, 0xFFFDC3B2, 0x3E8, 0xF6E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDC560, 0x0, 0xFFFFF560, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_6_10B8 end

    def Function_7_10E8(): pass

    label("Function_7_10E8")

    OP_8E(0xFE, 0xFFFDC3B2, 0x3E8, 0xF6E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDC0D8, 0x0, 0xFFFFF736, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_7_10E8 end

    def Function_8_1118(): pass

    label("Function_8_1118")

    OP_8E(0xFE, 0xFFFDC3B2, 0x3E8, 0xF6E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDC088, 0x0, 0xFFFFF2F4, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_8_1118 end

    def Function_9_1148(): pass

    label("Function_9_1148")

    Sleep(500)
    Sleep(500)
    OP_8E(0xFE, 0xFFFDC3EE, 0x0, 0xFFFFF3F8, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDC1BE, 0x3E8, 0xEB0, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDB548, 0xBB8, 0xF6E, 0xBB8, 0x0)
    Return()

    # Function_9_1148 end

    def Function_10_118F(): pass

    label("Function_10_118F")

    Sleep(500)
    Sleep(500)
    Sleep(500)
    Sleep(500)
    Sleep(300)
    OP_8E(0xFE, 0xFFFDC3EE, 0x0, 0xFFFFF3F8, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDC1BE, 0x3E8, 0xEB0, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDB548, 0xBB8, 0xF6E, 0xBB8, 0x0)
    Return()

    # Function_10_118F end

    def Function_11_11E5(): pass

    label("Function_11_11E5")

    Sleep(500)
    OP_8E(0xFE, 0xFFFDC3EE, 0x0, 0xFFFFF3F8, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDC1BE, 0x3E8, 0xEB0, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDB548, 0xBB8, 0xF6E, 0xBB8, 0x0)
    Return()

    # Function_11_11E5 end

    def Function_12_1227(): pass

    label("Function_12_1227")

    Sleep(500)
    Sleep(500)
    Sleep(500)
    OP_8E(0xFE, 0xFFFDC3EE, 0x0, 0xFFFFF3F8, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDC1BE, 0x3E8, 0xEB0, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDB548, 0xBB8, 0xF6E, 0xBB8, 0x0)
    Return()

    # Function_12_1227 end

    def Function_13_1273(): pass

    label("Function_13_1273")

    OP_8E(0xFE, 0xFFFDC3EE, 0x0, 0xFFFFF3F8, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDC1BE, 0x3E8, 0xEB0, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDB548, 0xBB8, 0xF6E, 0xBB8, 0x0)
    Return()

    # Function_13_1273 end

    def Function_14_12B0(): pass

    label("Function_14_12B0")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 5)), scpexpr(EXPR_END)), "loc_133A")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12FC")

    ChrTalk(
        0x106,
        (
            "#054F不能走这边！\x01",
            "赶快顺着刚才的叫声去看看吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1337")

    label("loc_12FC")

    TurnDirection(0x106, 0x0, 400)

    ChrTalk(
        0x106,
        (
            "#054F不能走这边！\x01",
            "赶快顺着刚才的叫声去看看吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1337")

    Jump("loc_13F8")

    label("loc_133A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_139F")

    ChrTalk(
        0x106,
        (
            "#050F总之不要再去地牢了……\x02\x03",
            "让那些家伙闹起来就糟了。\x01",
            "还是找找其它的逃跑路线吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13F8")

    label("loc_139F")

    TurnDirection(0x106, 0x0, 400)

    ChrTalk(
        0x106,
        (
            "#050F喂，别再去地牢了。\x02\x03",
            "让那些家伙闹起来就糟了。\x01",
            "赶快找找其它的逃跑路线吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13F8")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_14_12B0 end

    def Function_15_1414(): pass

    label("Function_15_1414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1888")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1762")
    EventBegin(0x0)
    OP_A2(0x56D)
    OP_28(0x44, 0x1, 0x400)

    ChrTalk(
        0xB,
        "喂，找到了吗！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x0, 0xB, 0)
    TurnDirection(0x1, 0xB, 0)
    TurnDirection(0x2, 0xB, 0)
    TurnDirection(0x3, 0xB, 0)
    TurnDirection(0x4, 0xB, 0)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "还没有，\x01",
            "兵营那边都找过了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "监视塔也无异常！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "……那么只剩下\x01",
            "这个司令部里面了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "向少校报告一下，\x01",
            "然后进行地毯式搜索吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F不妙！\x01",
            "好像朝这边来了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#057F可恶……\x01",
            "这里就是死路了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "过来！这边！\x02",
    )

    CloseMessageWindow()
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x0, 0xC, 0)
    TurnDirection(0x1, 0xC, 0)
    TurnDirection(0x2, 0xC, 0)
    TurnDirection(0x3, 0xC, 0)
    TurnDirection(0x4, 0xC, 0)

    ChrTalk(
        0x101,
        "#004F刚才的声音，听到了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#065F嗯、嗯……\x01",
            "好像是说来这边。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "……没时间了，\x01",
            "你们不想被抓吧！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        "#102F好像不是错觉啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#054F没办法了！\x01",
            "死马当活马医吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_1888")

    label("loc_1762")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17A7")

    ChrTalk(
        0x101,
        (
            "#005F士兵们要来了！\x01",
            "要快去传来声音的方向才行！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_186D")

    label("loc_17A7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17E8")

    ChrTalk(
        0x102,
        (
            "#012F脚步声近了……\x01",
            "去传来声音的方向看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_186D")

    label("loc_17E8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1827")

    ChrTalk(
        0x106,
        (
            "#057F这边不妙……\x01",
            "去传来声音的方向一探吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_186D")

    label("loc_1827")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_186D")

    ChrTalk(
        0x107,
        (
            "#065F士兵们快过来了……\x01",
            "要赶快去传来声音的方向才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_186D")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_1888")

    Return()

    # Function_15_1414 end

    def Function_16_1889(): pass

    label("Function_16_1889")

    EventBegin(0x0)
    OP_6D(21440, 0, 108290, 0)
    SetChrPos(0xC, 20330, 0, 120850, 0)
    SetChrPos(0x101, 21240, 0, 106790, 0)
    SetChrPos(0x102, 20030, 0, 106050, 0)
    SetChrPos(0x107, 21530, 0, 105630, 0)
    SetChrPos(0x106, 21050, 0, 104420, 0)
    SetChrPos(0x10B, 20280, 0, 104880, 0)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "快！\x01",
            "就这样一直走进来！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F约修亚，这个声音……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F啊……\x01",
            "我记得这声音。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_16_1889 end

    def Function_17_1962(): pass

    label("Function_17_1962")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A00")
    OP_A2(0x56F)
    SetChrPos(0xC, 21160, 0, 159230, 0)
    OP_1C(0x12, 0x0, 0xFFFF)
    EventBegin(0x0)
    OP_6D(21080, 0, 158340, 1000)

    ChrTalk(
        0xC,
        "来，快进来！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#050F喂喂，这个房间……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#100F唔，不知他打算怎样，\x01",
            "现在唯有进去一看了。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    OP_71(0x12, 0x10)

    label("loc_1A00")

    Return()

    # Function_17_1962 end

    def Function_18_1A01(): pass

    label("Function_18_1A01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 6)), scpexpr(EXPR_END)), "loc_1AA5")
    OP_A2(0x56F)
    SetChrPos(0xC, 21160, 0, 159230, 0)
    OP_1C(0x12, 0x0, 0xFFFF)
    EventBegin(0x0)
    OP_6D(21080, 0, 158340, 1000)

    ChrTalk(
        0xC,
        "来，快进来！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#052F喂喂，这个房间……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#102F唔，不知他打算怎样，\x01",
            "现在唯有进去一看了。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    OP_71(0x12, 0x10)
    OP_64(0x0, 0x1)
    Jump("loc_1AF4")

    label("loc_1AA5")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上着锁，无法打开。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)

    label("loc_1AF4")

    Return()

    # Function_18_1A01 end

    def Function_19_1AF5(): pass

    label("Function_19_1AF5")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上着锁，无法打开。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_19_1AF5 end

    SaveToFile()

Try(main)
