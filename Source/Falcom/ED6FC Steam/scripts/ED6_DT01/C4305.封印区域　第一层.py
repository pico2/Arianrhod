from ED6ScenarioHelper import *

def main():
    # 封印区域　第一层

    CreateScenaFile(
        FileName            = 'C4305   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4305.x',
        MapIndex            = 216,
        MapDefaultBGM       = "ed60035",
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


    AddCharChip(
        'ED6_DT09/CH11090 ._CH',             # 00
        'ED6_DT09/CH11091 ._CH',             # 01
        'ED6_DT09/CH11100 ._CH',             # 02
        'ED6_DT09/CH11101 ._CH',             # 03
        'ED6_DT09/CH10940 ._CH',             # 04
        'ED6_DT09/CH10941 ._CH',             # 05
        'ED6_DT09/CH10940 ._CH',             # 06
        'ED6_DT09/CH10941 ._CH',             # 07
        'ED6_DT09/CH11000 ._CH',             # 08
        'ED6_DT09/CH11001 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT09/CH11090P._CP',             # 00
        'ED6_DT09/CH11091P._CP',             # 01
        'ED6_DT09/CH11100P._CP',             # 02
        'ED6_DT09/CH11101P._CP',             # 03
        'ED6_DT09/CH10940P._CP',             # 04
        'ED6_DT09/CH10941P._CP',             # 05
        'ED6_DT09/CH10940P._CP',             # 06
        'ED6_DT09/CH10941P._CP',             # 07
        'ED6_DT09/CH11000P._CP',             # 08
        'ED6_DT09/CH11001P._CP',             # 09
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -160720,
        Z                   = 0,
        Y                   = 43100,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -239000,
        Y                   = -1000,
        Z                   = 42000,
        Range               = 3000,
        Unknown_10          = 0x5DC,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 3,
    )

    DeclEvent(
        X                   = -376000,
        Y                   = -1000,
        Z                   = 55000,
        Range               = 3000,
        Unknown_10          = 0x5DC,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 5,
    )


    DeclActor(
        TriggerX            = -192730,
        TriggerZ            = 0,
        TriggerY            = -77230,
        TriggerRange        = 1000,
        ActorX              = -192000,
        ActorZ              = 0,
        ActorY              = -77080,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -91700,
        TriggerZ            = 0,
        TriggerY            = 42960,
        TriggerRange        = 1000,
        ActorX              = -91050,
        ActorZ              = 0,
        ActorY              = 43060,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -306370,
        TriggerZ            = 0,
        TriggerY            = 53900,
        TriggerRange        = 1000,
        ActorX              = -305690,
        ActorZ              = 0,
        ActorY              = 54020,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -313240,
        TriggerZ            = 0,
        TriggerY            = -24960,
        TriggerRange        = 1000,
        ActorX              = -314050,
        ActorZ              = 0,
        ActorY              = -25090,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -282740,
        TriggerZ            = 0,
        TriggerY            = -81200,
        TriggerRange        = 1000,
        ActorX              = -283050,
        ActorZ              = 0,
        ActorY              = -81950,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -166860,
        TriggerZ            = 0,
        TriggerY            = -25200,
        TriggerRange        = 1000,
        ActorX              = -166160,
        ActorZ              = 0,
        ActorY              = -25090,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_26E",          # 00, 0
        "Function_1_28B",          # 01, 1
        "Function_2_328",          # 02, 2
        "Function_3_33E",          # 03, 3
        "Function_4_3C9",          # 04, 4
        "Function_5_48F",          # 05, 5
        "Function_6_51A",          # 06, 6
        "Function_7_5E0",          # 07, 7
        "Function_8_7C3",          # 08, 8
        "Function_9_9BE",          # 09, 9
        "Function_10_BB3",         # 0A, 10
        "Function_11_CE4",         # 0B, 11
        "Function_12_E27",         # 0C, 12
    )


    def Function_0_26E(): pass

    label("Function_0_26E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_27C")
    OP_A3(0x3FA)
    Event(0, 4)

    label("loc_27C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_28A")
    OP_A3(0x3FB)
    Event(0, 6)

    label("loc_28A")

    Return()

    # Function_0_26E end

    def Function_1_28B(): pass

    label("Function_1_28B")

    OP_10(0x14, 0x0)
    OP_10(0x13, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A3")
    OP_6F(0x4, 0)
    Jump("loc_2AA")

    label("loc_2A3")

    OP_6F(0x4, 60)

    label("loc_2AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BC")
    OP_6F(0x6, 0)
    Jump("loc_2C3")

    label("loc_2BC")

    OP_6F(0x6, 60)

    label("loc_2C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D5")
    OP_6F(0x7, 0)
    Jump("loc_2DC")

    label("loc_2D5")

    OP_6F(0x7, 60)

    label("loc_2DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EE")
    OP_6F(0x2, 0)
    Jump("loc_2F5")

    label("loc_2EE")

    OP_6F(0x2, 60)

    label("loc_2F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_307")
    OP_6F(0x3, 0)
    Jump("loc_30E")

    label("loc_307")

    OP_6F(0x3, 60)

    label("loc_30E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_320")
    OP_6F(0x5, 0)
    Jump("loc_327")

    label("loc_320")

    OP_6F(0x5, 60)

    label("loc_327")

    Return()

    # Function_1_28B end

    def Function_2_328(): pass

    label("Function_2_328")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_33D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_328")

    label("loc_33D")

    Return()

    # Function_2_328 end

    def Function_3_33E(): pass

    label("Function_3_33E")

    EventBegin(0x0)
    Fade(1000)
    OP_89(0x0, -238200, 20000, 42800, 0)
    OP_89(0x1, -239800, 20000, 42800, 0)
    OP_89(0x2, -239800, 20000, 41200, 0)
    OP_89(0x3, -238200, 20000, 41200, 0)
    OP_6D(-239000, 0, 42000, 1500)
    Sleep(100)
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x12C)
    Sleep(2000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/C4306   ._SN", 134, 0, 0)
    IdleLoop()
    Return()

    # Function_3_33E end

    def Function_4_3C9(): pass

    label("Function_4_3C9")

    EventBegin(0x0)
    SetPlaceName(0xDE) # 封印区域　第一层
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xDE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x0, 150)
    OP_70(0x0, 0x0)
    OP_48()
    OP_89(0x0, -238200, 10000, 42800, 0)
    OP_89(0x1, -239800, 10000, 42800, 0)
    OP_89(0x2, -239800, 10000, 41200, 0)
    OP_89(0x3, -238200, 10000, 41200, 0)
    OP_6D(-239000, 0, 42000, 0)
    OP_73(0x0)
    Sleep(100)
    Fade(1000)
    OP_89(0x0, -238990, 0, 45400, 0)
    OP_89(0x1, -238990, 0, 45400, 0)
    OP_89(0x2, -238990, 0, 45400, 0)
    OP_89(0x3, -238990, 0, 45400, 0)
    EventEnd(0x0)
    Return()

    # Function_4_3C9 end

    def Function_5_48F(): pass

    label("Function_5_48F")

    EventBegin(0x0)
    Fade(1000)
    OP_89(0x0, -375200, 20000, 55800, 0)
    OP_89(0x1, -376800, 20000, 55800, 0)
    OP_89(0x2, -376800, 20000, 54200, 0)
    OP_89(0x3, -375200, 20000, 54200, 0)
    OP_6D(-376000, 0, 55000, 1500)
    Sleep(100)
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x12C)
    Sleep(2000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/C4306   ._SN", 134, 0, 0)
    IdleLoop()
    Return()

    # Function_5_48F end

    def Function_6_51A(): pass

    label("Function_6_51A")

    EventBegin(0x0)
    SetPlaceName(0xDE) # 封印区域　第一层
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xDE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x1, 150)
    OP_70(0x1, 0x0)
    OP_48()
    OP_89(0x0, -375200, 10000, 55800, 0)
    OP_89(0x1, -376800, 10000, 55800, 0)
    OP_89(0x2, -376800, 10000, 54200, 0)
    OP_89(0x3, -375200, 10000, 54200, 0)
    OP_6D(-376000, 0, 55000, 0)
    OP_73(0x1)
    Sleep(100)
    Fade(1000)
    OP_89(0x0, -372640, 0, 55030, 90)
    OP_89(0x1, -372640, 0, 55030, 90)
    OP_89(0x2, -372640, 0, 55030, 90)
    OP_89(0x3, -372640, 0, 55030, 90)
    EventEnd(0x0)
    Return()

    # Function_6_51A end

    def Function_7_5E0(): pass

    label("Function_7_5E0")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_782")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C0")
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, -192000, 1500, -77080, 320)
    TurnDirection(0x9, 0x0, 0)

    def lambda_62F():
        OP_8F(0xFE, 0xFFFD1200, 0x3E8, 0xFFFED2E8, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_62F)

    def lambda_64A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_64A)
    ClearChrFlags(0x9, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "机械人形出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x30F, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x9, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_69B"),
        (2, "loc_6AD"),
        (1, "loc_6BD"),
        (SWITCH_DEFAULT, "loc_6C0"),
    )


    label("loc_69B")

    OP_A2(0x6C0)
    OP_6F(0x4, 60)
    Sleep(500)
    Jump("loc_6C0")

    label("loc_6AD")

    OP_6F(0x4, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_6BD")

    OP_B4(0x0)
    Return()

    label("loc_6C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x41, 1)"), scpexpr(EXPR_END)), "loc_712")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "九尾\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x6BF)
    Jump("loc_77F")

    label("loc_712")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "九尾\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "九尾\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_77F")

    Jump("loc_7B5")

    label("loc_782")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么东西都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7B5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_5E0 end

    def Function_8_7C3(): pass

    label("Function_8_7C3")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_97D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A3")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, -91050, 1500, 43060, 320)
    TurnDirection(0x8, 0x0, 0)

    def lambda_812():
        OP_8F(0xFE, 0xFFFE9C56, 0x3E8, 0xA834, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_812)

    def lambda_82D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_82D)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "机械人形出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x311, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_87E"),
        (2, "loc_890"),
        (1, "loc_8A0"),
        (SWITCH_DEFAULT, "loc_8A3"),
    )


    label("loc_87E")

    OP_A2(0x6C2)
    OP_6F(0x6, 60)
    Sleep(500)
    Jump("loc_8A3")

    label("loc_890")

    OP_6F(0x6, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_8A0")

    OP_B4(0x0)
    Return()

    label("loc_8A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xFD, 1)"), scpexpr(EXPR_END)), "loc_8FD")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "皇家骑士铠甲\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x6C1)
    Jump("loc_97A")

    label("loc_8FD")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "皇家骑士铠甲\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "皇家骑士铠甲\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_97A")

    Jump("loc_9B0")

    label("loc_97D")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么东西都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_9B0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_7C3 end

    def Function_9_9BE(): pass

    label("Function_9_9BE")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B72")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A9E")
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, -305690, 1500, 54020, 320)
    TurnDirection(0x9, 0x0, 0)

    def lambda_A0D():
        OP_8F(0xFE, 0xFFFB55E6, 0x3E8, 0xD304, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A0D)

    def lambda_A28():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_A28)
    ClearChrFlags(0x9, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "机械人形出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x30F, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x9, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_A79"),
        (2, "loc_A8B"),
        (1, "loc_A9B"),
        (SWITCH_DEFAULT, "loc_A9E"),
    )


    label("loc_A79")

    OP_A2(0x6C4)
    OP_6F(0x7, 60)
    Sleep(500)
    Jump("loc_A9E")

    label("loc_A8B")

    OP_6F(0x7, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_A9B")

    OP_B4(0x0)
    Return()

    label("loc_A9E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x9D, 1)"), scpexpr(EXPR_END)), "loc_AF6")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "狂战士巨刃\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x6C3)
    Jump("loc_B6F")

    label("loc_AF6")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "狂战士巨刃\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "狂战士巨刃\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)

    label("loc_B6F")

    Jump("loc_BA5")

    label("loc_B72")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么东西都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_BA5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_9BE end

    def Function_10_BB3(): pass

    label("Function_10_BB3")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CA3")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_C29")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "大回复药\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x6C5)
    Jump("loc_CA0")

    label("loc_C29")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "大回复药\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "大回复药\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_CA0")

    Jump("loc_CD6")

    label("loc_CA3")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么东西都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_CD6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_BB3 end

    def Function_11_CE4(): pass

    label("Function_11_CE4")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_D60")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "ＥＰ改良填充剂\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x6C6)
    Jump("loc_DE3")

    label("loc_D60")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "ＥＰ改良填充剂\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "ＥＰ改良填充剂\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_DE3")

    Jump("loc_E19")

    label("loc_DE6")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么东西都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_E19")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_CE4 end

    def Function_12_E27(): pass

    label("Function_12_E27")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F17")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_E9D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "全回复药\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x6C7)
    Jump("loc_F14")

    label("loc_E9D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "全回复药\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "全回复药\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_F14")

    Jump("loc_F4A")

    label("loc_F17")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么东西都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_F4A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_E27 end

    SaveToFile()

Try(main)
