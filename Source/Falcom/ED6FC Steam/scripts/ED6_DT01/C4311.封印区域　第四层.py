from ED6ScenarioHelper import *

def main():
    # 封印区域　第四层

    CreateScenaFile(
        FileName            = 'C4311   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4311.x',
        MapIndex            = 1,
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
        'ED6_DT09/CH10920 ._CH',             # 04
        'ED6_DT09/CH10921 ._CH',             # 05
        'ED6_DT09/CH10940 ._CH',             # 06
        'ED6_DT09/CH10941 ._CH',             # 07
        'ED6_DT09/CH10950 ._CH',             # 08
        'ED6_DT09/CH10951 ._CH',             # 09
        'ED6_DT09/CH10990 ._CH',             # 0A
        'ED6_DT09/CH10991 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT09/CH11090P._CP',             # 00
        'ED6_DT09/CH11091P._CP',             # 01
        'ED6_DT09/CH11100P._CP',             # 02
        'ED6_DT09/CH11101P._CP',             # 03
        'ED6_DT09/CH10920P._CP',             # 04
        'ED6_DT09/CH10921P._CP',             # 05
        'ED6_DT09/CH10940P._CP',             # 06
        'ED6_DT09/CH10941P._CP',             # 07
        'ED6_DT09/CH10950P._CP',             # 08
        'ED6_DT09/CH10951P._CP',             # 09
        'ED6_DT09/CH10990P._CP',             # 0A
        'ED6_DT09/CH10991P._CP',             # 0B
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        X                   = -205700,
        Z                   = 0,
        Y                   = -291370,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x291,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -110910,
        Z                   = -4000,
        Y                   = -303160,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x30D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 6950,
        Z                   = -4000,
        Y                   = -349460,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x291,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -32200,
        Z                   = -8000,
        Y                   = -171090,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x30D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -58060,
        Z                   = 0,
        Y                   = -104990,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x30D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -60000,
        Y                   = -1000,
        Z                   = -32000,
        Range               = 3000,
        Unknown_10          = 0x5DC,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 3,
    )


    DeclActor(
        TriggerX            = -261269,
        TriggerZ            = -4000,
        TriggerY            = -297640,
        TriggerRange        = 1000,
        ActorX              = -261100,
        ActorZ              = -4000,
        ActorY              = -296970,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 17060,
        TriggerZ            = -4000,
        TriggerY            = -165400,
        TriggerRange        = 1000,
        ActorX              = 17040,
        ActorZ              = -4000,
        ActorY              = -164810,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -204610,
        TriggerZ            = -4000,
        TriggerY            = -359520,
        TriggerRange        = 1000,
        ActorX              = -204860,
        ActorZ              = -4000,
        ActorY              = -360270,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 16350,
        TriggerZ            = -8000,
        TriggerY            = -118970,
        TriggerRange        = 1000,
        ActorX              = 16920,
        ActorZ              = -8000,
        ActorY              = -119010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_286",          # 00, 0
        "Function_1_295",          # 01, 1
        "Function_2_2FD",          # 02, 2
        "Function_3_313",          # 03, 3
        "Function_4_39E",          # 04, 4
        "Function_5_464",          # 05, 5
        "Function_6_653",          # 06, 6
        "Function_7_848",          # 07, 7
        "Function_8_98B",          # 08, 8
    )


    def Function_0_286(): pass

    label("Function_0_286")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_294")
    OP_A3(0x3FA)
    Event(0, 4)

    label("loc_294")

    Return()

    # Function_0_286 end

    def Function_1_295(): pass

    label("Function_1_295")

    OP_10(0x17, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AA")
    OP_6F(0x1, 0)
    Jump("loc_2B1")

    label("loc_2AA")

    OP_6F(0x1, 60)

    label("loc_2B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C3")
    OP_6F(0x3, 0)
    Jump("loc_2CA")

    label("loc_2C3")

    OP_6F(0x3, 60)

    label("loc_2CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DC")
    OP_6F(0x2, 0)
    Jump("loc_2E3")

    label("loc_2DC")

    OP_6F(0x2, 60)

    label("loc_2E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F5")
    OP_6F(0x4, 0)
    Jump("loc_2FC")

    label("loc_2F5")

    OP_6F(0x4, 60)

    label("loc_2FC")

    Return()

    # Function_1_295 end

    def Function_2_2FD(): pass

    label("Function_2_2FD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_312")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2FD")

    label("loc_312")

    Return()

    # Function_2_2FD end

    def Function_3_313(): pass

    label("Function_3_313")

    EventBegin(0x0)
    Fade(1000)
    OP_89(0x0, -59200, 20000, -32800, 0)
    OP_89(0x1, -60800, 20000, -32800, 0)
    OP_89(0x2, -60800, 20000, -31200, 0)
    OP_89(0x3, -59200, 20000, -31200, 0)
    OP_6D(-60000, 0, -32000, 1500)
    Sleep(100)
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x12C)
    Sleep(2000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/C4302   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_313 end

    def Function_4_39E(): pass

    label("Function_4_39E")

    EventBegin(0x0)
    SetPlaceName(0xE1) # 封印区域　第四层
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x0, 150)
    OP_70(0x0, 0x0)
    OP_48()
    OP_89(0x0, -59200, 20000, -32800, 0)
    OP_89(0x1, -60800, 20000, -32800, 0)
    OP_89(0x2, -60800, 20000, -31200, 0)
    OP_89(0x3, -59200, 20000, -31200, 0)
    OP_6D(-60000, 0, -32000, 0)
    OP_73(0x0)
    Sleep(100)
    Fade(1000)
    OP_89(0x0, -60000, 0, -35200, 180)
    OP_89(0x1, -60000, 0, -35200, 180)
    OP_89(0x2, -60000, 0, -35200, 180)
    OP_89(0x3, -60000, 0, -35200, 180)
    EventEnd(0x0)
    Return()

    # Function_4_39E end

    def Function_5_464(): pass

    label("Function_5_464")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_612")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_544")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, -261100, -1500, -296970, 320)
    TurnDirection(0x8, 0x0, 0)

    def lambda_4B3():
        OP_8F(0xFE, 0xFFFC0414, 0xFFFFF448, 0xFFFB77F6, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4B3)

    def lambda_4CE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_4CE)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "机械人形出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x312, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_51F"),
        (2, "loc_531"),
        (1, "loc_541"),
        (SWITCH_DEFAULT, "loc_544"),
    )


    label("loc_51F")

    OP_A2(0x698)
    OP_6F(0x1, 60)
    Sleep(500)
    Jump("loc_544")

    label("loc_531")

    OP_6F(0x1, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_541")

    OP_B4(0x0)
    Return()

    label("loc_544")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x29, 1)"), scpexpr(EXPR_END)), "loc_59A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "合金乌剑\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x697)
    Jump("loc_60F")

    label("loc_59A")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "合金乌剑\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "合金乌剑\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_60F")

    Jump("loc_645")

    label("loc_612")

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

    label("loc_645")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_464 end

    def Function_6_653(): pass

    label("Function_6_653")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_807")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_733")
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, 17040, -1500, -164810, 320)
    TurnDirection(0x9, 0x0, 0)

    def lambda_6A2():
        OP_8F(0xFE, 0x4290, 0xFFFFF448, 0xFFFD7C36, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6A2)

    def lambda_6BD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_6BD)
    ClearChrFlags(0x9, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "机械人形出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x313, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x9, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_70E"),
        (2, "loc_720"),
        (1, "loc_730"),
        (SWITCH_DEFAULT, "loc_733"),
    )


    label("loc_70E")

    OP_A2(0x69A)
    OP_6F(0x3, 60)
    Sleep(500)
    Jump("loc_733")

    label("loc_720")

    OP_6F(0x3, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_730")

    OP_B4(0x0)
    Return()

    label("loc_733")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xFE, 1)"), scpexpr(EXPR_END)), "loc_78B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "女武神战甲\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x699)
    Jump("loc_804")

    label("loc_78B")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "女武神战甲\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "女武神战甲\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_804")

    Jump("loc_83A")

    label("loc_807")

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

    label("loc_83A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_653 end

    def Function_7_848(): pass

    label("Function_7_848")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_8C4")
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
    OP_A2(0x69B)
    Jump("loc_947")

    label("loc_8C4")

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
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_947")

    Jump("loc_97D")

    label("loc_94A")

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

    label("loc_97D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_848 end

    def Function_8_98B(): pass

    label("Function_8_98B")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_A01")
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
    OP_A2(0x69C)
    Jump("loc_A78")

    label("loc_A01")

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
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_A78")

    Jump("loc_AAE")

    label("loc_A7B")

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

    label("loc_AAE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_98B end

    SaveToFile()

Try(main)
