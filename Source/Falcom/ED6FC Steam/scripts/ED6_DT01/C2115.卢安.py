from ED6ScenarioHelper import *

def main():
    # 卢安

    CreateScenaFile(
        FileName            = 'C2115   ._SN',
        MapName             = 'Ruan',
        Location            = 'C2115.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60033",
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
        'ED6_DT09/CH10560 ._CH',             # 00
        'ED6_DT09/CH10561 ._CH',             # 01
        'ED6_DT09/CH10570 ._CH',             # 02
        'ED6_DT09/CH10571 ._CH',             # 03
        'ED6_DT09/CH10580 ._CH',             # 04
        'ED6_DT09/CH10581 ._CH',             # 05
        'ED6_DT09/CH10590 ._CH',             # 06
        'ED6_DT09/CH10591 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT09/CH10560P._CP',             # 00
        'ED6_DT09/CH10561P._CP',             # 01
        'ED6_DT09/CH10570P._CP',             # 02
        'ED6_DT09/CH10571P._CP',             # 03
        'ED6_DT09/CH10580P._CP',             # 04
        'ED6_DT09/CH10581P._CP',             # 05
        'ED6_DT09/CH10590P._CP',             # 06
        'ED6_DT09/CH10591P._CP',             # 07
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 3970,
        Z                   = 0,
        Y                   = 3770,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1BC,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -8230,
        TriggerZ            = 0,
        TriggerY            = 8330,
        TriggerRange        = 1000,
        ActorX              = -8730,
        ActorZ              = 0,
        ActorY              = 8830,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 9350,
        TriggerZ            = 0,
        TriggerY            = 9330,
        TriggerRange        = 1000,
        ActorX              = 8850,
        ActorZ              = 0,
        ActorY              = 8830,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 12530,
        TriggerZ            = 0,
        TriggerY            = -660,
        TriggerRange        = 1000,
        ActorX              = 12530,
        ActorZ              = 0,
        ActorY              = 0,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -12430,
        TriggerZ            = 0,
        TriggerY            = -640,
        TriggerRange        = 1000,
        ActorX              = -12430,
        ActorZ              = 0,
        ActorY              = 110,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4470,
        TriggerZ            = 0,
        TriggerY            = 22500,
        TriggerRange        = 1000,
        ActorX              = 4690,
        ActorZ              = 0,
        ActorY              = 23200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_23A",          # 00, 0
        "Function_1_23B",          # 01, 1
        "Function_2_2D5",          # 02, 2
        "Function_3_2EB",          # 03, 3
        "Function_4_4D0",          # 04, 4
        "Function_5_6AF",          # 05, 5
        "Function_6_894",          # 06, 6
        "Function_7_A79",          # 07, 7
    )


    def Function_0_23A(): pass

    label("Function_0_23A")

    Return()

    # Function_0_23A end

    def Function_1_23B(): pass

    label("Function_1_23B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24D")
    OP_6F(0x0, 0)
    Jump("loc_254")

    label("loc_24D")

    OP_6F(0x0, 60)

    label("loc_254")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x96, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_266")
    OP_6F(0x1, 0)
    Jump("loc_26D")

    label("loc_266")

    OP_6F(0x1, 60)

    label("loc_26D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x96, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27F")
    OP_6F(0x2, 0)
    Jump("loc_286")

    label("loc_27F")

    OP_6F(0x2, 60)

    label("loc_286")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x96, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_298")
    OP_6F(0x3, 0)
    Jump("loc_29F")

    label("loc_298")

    OP_6F(0x3, 60)

    label("loc_29F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x96, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B1")
    OP_6F(0x4, 0)
    Jump("loc_2B8")

    label("loc_2B1")

    OP_6F(0x4, 60)

    label("loc_2B8")

    SoundDistance(0x1CB, 0xFFFFFFA6, 0x0, 0x96, 0x7D0, 0x61A8, 0x64, 0x0)
    Return()

    # Function_1_23B end

    def Function_2_2D5(): pass

    label("Function_2_2D5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2EA")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2D5")

    label("loc_2EA")

    Return()

    # Function_2_2D5 end

    def Function_3_2EB(): pass

    label("Function_3_2EB")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C7")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, -8730, 3000, 8830, 320)
    TurnDirection(0x8, 0x0, 0)

    def lambda_33A():
        OP_8F(0xFE, 0xFFFFDDE6, 0x5DC, 0x227E, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_33A)

    def lambda_355():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_355)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔兽出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x1BD, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_3A2"),
        (2, "loc_3B4"),
        (1, "loc_3C4"),
        (SWITCH_DEFAULT, "loc_3C7"),
    )


    label("loc_3A2")

    OP_A2(0x4AF)
    OP_6F(0x0, 60)
    Sleep(500)
    Jump("loc_3C7")

    label("loc_3B4")

    OP_6F(0x0, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_3C4")

    OP_B4(0x0)
    Return()

    label("loc_3C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x7B, 1)"), scpexpr(EXPR_END)), "loc_41B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "水纹剑\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x4AE)
    Jump("loc_48C")

    label("loc_41B")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "水纹剑\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "水纹剑\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_48C")

    Jump("loc_4C2")

    label("loc_48F")

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

    label("loc_4C2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_2EB end

    def Function_4_4D0(): pass

    label("Function_4_4D0")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x96, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x96, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AC")
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, 8850, 3000, 8830, 320)
    TurnDirection(0x9, 0x0, 0)

    def lambda_51F():
        OP_8F(0xFE, 0x2292, 0x5DC, 0x227E, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_51F)

    def lambda_53A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_53A)
    ClearChrFlags(0x9, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔兽出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x1BD, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x9, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_587"),
        (2, "loc_599"),
        (1, "loc_5A9"),
        (SWITCH_DEFAULT, "loc_5AC"),
    )


    label("loc_587")

    OP_A2(0x4B1)
    OP_6F(0x1, 60)
    Sleep(500)
    Jump("loc_5AC")

    label("loc_599")

    OP_6F(0x1, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_5A9")

    OP_B4(0x0)
    Return()

    label("loc_5AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2D0, 1)"), scpexpr(EXPR_END)), "loc_5FE")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "美臭\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x4B0)
    Jump("loc_66B")

    label("loc_5FE")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "美臭\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "美臭\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_66B")

    Jump("loc_6A1")

    label("loc_66E")

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

    label("loc_6A1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_4D0 end

    def Function_5_6AF(): pass

    label("Function_5_6AF")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x96, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_853")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x96, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78B")
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xA, 12530, 3000, 0, 320)
    TurnDirection(0xA, 0x0, 0)

    def lambda_6FE():
        OP_8F(0xFE, 0x30F2, 0x5DC, 0x0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6FE)

    def lambda_719():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_719)
    ClearChrFlags(0xA, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔兽出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x1BD, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xA, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_766"),
        (2, "loc_778"),
        (1, "loc_788"),
        (SWITCH_DEFAULT, "loc_78B"),
    )


    label("loc_766")

    OP_A2(0x4B3)
    OP_6F(0x2, 60)
    Sleep(500)
    Jump("loc_78B")

    label("loc_778")

    OP_6F(0x2, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_788")

    OP_B4(0x0)
    Return()

    label("loc_78B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xF9, 1)"), scpexpr(EXPR_END)), "loc_7DF")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "战斗服\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x4B2)
    Jump("loc_850")

    label("loc_7DF")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "战斗服\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "战斗服\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_850")

    Jump("loc_886")

    label("loc_853")

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

    label("loc_886")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_6AF end

    def Function_6_894(): pass

    label("Function_6_894")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x96, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A38")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x96, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_970")
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xB, -12430, 3000, 110, 320)
    TurnDirection(0xB, 0x0, 0)

    def lambda_8E3():
        OP_8F(0xFE, 0xFFFFCF72, 0x5DC, 0x6E, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_8E3)

    def lambda_8FE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_8FE)
    ClearChrFlags(0xB, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔兽出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x1BD, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xB, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_94B"),
        (2, "loc_95D"),
        (1, "loc_96D"),
        (SWITCH_DEFAULT, "loc_970"),
    )


    label("loc_94B")

    OP_A2(0x4B5)
    OP_6F(0x3, 60)
    Sleep(500)
    Jump("loc_970")

    label("loc_95D")

    OP_6F(0x3, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_96D")

    OP_B4(0x0)
    Return()

    label("loc_970")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x117, 1)"), scpexpr(EXPR_END)), "loc_9C4")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "军用靴\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x4B4)
    Jump("loc_A35")

    label("loc_9C4")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "军用靴\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "军用靴\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_A35")

    Jump("loc_A6B")

    label("loc_A38")

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

    label("loc_A6B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_894 end

    def Function_7_A79(): pass

    label("Function_7_A79")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x96, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B6F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_AF1")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "ＥＰ填充剂\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x4B6)
    Jump("loc_B6C")

    label("loc_AF1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "ＥＰ填充剂\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "ＥＰ填充剂\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_B6C")

    Jump("loc_BA2")

    label("loc_B6F")

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

    label("loc_BA2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_A79 end

    SaveToFile()

Try(main)
