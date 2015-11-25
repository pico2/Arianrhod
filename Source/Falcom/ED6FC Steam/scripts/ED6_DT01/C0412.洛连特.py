from ED6ScenarioHelper import *

def main():
    # 洛连特

    CreateScenaFile(
        FileName            = 'C0412   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0412.x',
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
        '鲁克',                                 # 9
        '帕特',                                 # 10
        '魔兽',                                 # 11
        '魔兽',                                 # 12
        '魔兽',                                 # 13
        '魔兽',                                 # 14
        '魔兽',                                 # 15
        '魔兽',                                 # 16
        '卡西乌斯',                             # 17
        '卡西乌斯',                             # 18
        '卡西乌斯',                             # 19
        '卡西乌斯',                             # 20
        '卡西乌斯',                             # 21
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
        'ED6_DT07/CH01160 ._CH',             # 00
        'ED6_DT07/CH01060 ._CH',             # 01
        'ED6_DT09/CH10020 ._CH',             # 02
        'ED6_DT09/CH10021 ._CH',             # 03
        'ED6_DT07/CH02000 ._CH',             # 04
        'ED6_DT07/CH00100 ._CH',             # 05
        'ED6_DT07/CH00101 ._CH',             # 06
        'ED6_DT07/CH00110 ._CH',             # 07
        'ED6_DT07/CH00111 ._CH',             # 08
        'ED6_DT07/CH00112 ._CH',             # 09
        'ED6_DT07/CH00102 ._CH',             # 0A
        'ED6_DT09/CH10160 ._CH',             # 0B
        'ED6_DT09/CH10161 ._CH',             # 0C
        'ED6_DT06/CH20031 ._CH',             # 0D
        'ED6_DT09/CH10070 ._CH',             # 0E
        'ED6_DT09/CH10071 ._CH',             # 0F
        'ED6_DT09/CH10040 ._CH',             # 10
        'ED6_DT09/CH10041 ._CH',             # 11
        'ED6_DT09/CH10150 ._CH',             # 12
        'ED6_DT09/CH10151 ._CH',             # 13
    )

    AddCharChipPat(
        'ED6_DT07/CH01160P._CP',             # 00
        'ED6_DT07/CH01060P._CP',             # 01
        'ED6_DT09/CH10020P._CP',             # 02
        'ED6_DT09/CH10021P._CP',             # 03
        'ED6_DT07/CH02000P._CP',             # 04
        'ED6_DT07/CH00100P._CP',             # 05
        'ED6_DT07/CH00101P._CP',             # 06
        'ED6_DT07/CH00110P._CP',             # 07
        'ED6_DT07/CH00111P._CP',             # 08
        'ED6_DT07/CH00112P._CP',             # 09
        'ED6_DT07/CH00102P._CP',             # 0A
        'ED6_DT09/CH10160P._CP',             # 0B
        'ED6_DT09/CH10161P._CP',             # 0C
        'ED6_DT06/CH20031P._CP',             # 0D
        'ED6_DT09/CH10070P._CP',             # 0E
        'ED6_DT09/CH10071P._CP',             # 0F
        'ED6_DT09/CH10040P._CP',             # 10
        'ED6_DT09/CH10041P._CP',             # 11
        'ED6_DT09/CH10150P._CP',             # 12
        'ED6_DT09/CH10151P._CP',             # 13
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 19000,
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
        X                   = 3000,
        Z                   = 0,
        Y                   = 19000,
        Direction           = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -18100,
        Z                   = 0,
        Y                   = 110,
        Unknown_0C          = 180,
        Unknown_0E          = 14,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x31,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 18020,
        Z                   = 0,
        Y                   = 10,
        Unknown_0C          = 180,
        Unknown_0E          = 14,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x32,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    ScpFunction(
        "Function_0_322",          # 00, 0
        "Function_1_341",          # 01, 1
        "Function_2_342",          # 02, 2
        "Function_3_358",          # 03, 3
        "Function_4_28A0",         # 04, 4
        "Function_5_28D6",         # 05, 5
        "Function_6_291E",         # 06, 6
        "Function_7_297D",         # 07, 7
        "Function_8_29DC",         # 08, 8
        "Function_9_2A3B",         # 09, 9
    )


    def Function_0_322(): pass

    label("Function_0_322")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_32E"),
        (SWITCH_DEFAULT, "loc_340"),
    )


    label("loc_32E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33D")
    OP_A2(0x217)
    Event(0, 3)

    label("loc_33D")

    Jump("loc_340")

    label("loc_340")

    Return()

    # Function_0_322 end

    def Function_1_341(): pass

    label("Function_1_341")

    Return()

    # Function_1_341 end

    def Function_2_342(): pass

    label("Function_2_342")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_357")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_342")

    label("loc_357")

    Return()

    # Function_2_342 end

    def Function_3_358(): pass

    label("Function_3_358")

    EventBegin(0x0)
    AddParty(0x3F, 0xFF)
    AddParty(0x40, 0xFF)
    SetChrFlags(0x140, 0x80)
    SetChrFlags(0x141, 0x80)
    FadeToBright(2000, 0)
    OP_6D(20, 500, 21100, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(335000, 0)
    OP_6E(275, 0)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrPos(0x101, -680, 250, 20560, 180)
    SetChrPos(0x102, 630, 250, 20650, 180)
    SetChrPos(0x8, -3860, 0, -3700, 45)
    SetChrPos(0x9, -2850, 0, -4300, 45)
    SetChrPos(0xA, -2830, 0, 1630, 180)
    SetChrPos(0xB, -2120, 0, 2880, 209)
    SetChrPos(0xC, -1510, 0, -250, 192)
    SetChrPos(0xD, 840, 0, 1810, 201)
    SetChrPos(0xE, 1750, 0, -1350, 180)
    TurnDirection(0xA, 0x8, 0)
    TurnDirection(0xB, 0x8, 0)
    TurnDirection(0xC, 0x8, 0)
    TurnDirection(0xD, 0x8, 0)
    TurnDirection(0xE, 0x8, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    OP_6E(262, 2500)
    OP_0D()

    NpcTalk(
        0x8,
        "鲁克的声音",
        "#1S呜哇哇哇～！？\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "帕特的声音",
        "#1S救、救命啊——！\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【自己一口气冲进去】\x01",      # 0
            "【和约修亚一起出击】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_58B"),
        (1, "loc_F6B"),
        (SWITCH_DEFAULT, "loc_187B"),
    )


    label("loc_58B")

    OP_28(0x1, 0x1, 0x10)

    ChrTalk(
        0x101,
        "#005F我要进去救他们！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 5)
    Sleep(500)

    def lambda_5BC():
        OP_8E(0xFE, 0xFFFFFCE0, 0x0, 0xC12, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5BC)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#012F艾丝蒂尔！\x02\x03",
            "#012F老是这么冲动，真拿你没办法……\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x102, 7)
    Sleep(500)

    def lambda_637():
        OP_8E(0xFE, 0x442, 0x0, 0x2706, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_637)
    OP_43(0xA, 0x3, 0x0, 0x2)
    Sleep(100)
    OP_43(0xB, 0x3, 0x0, 0x2)
    Sleep(200)

    def lambda_66A():
        OP_8E(0xFE, 0x442, 0x0, 0x2706, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_66A)
    OP_43(0xC, 0x3, 0x0, 0x2)
    Sleep(100)
    OP_43(0xD, 0x3, 0x0, 0x2)
    Sleep(200)
    OP_43(0xE, 0x3, 0x0, 0x2)
    Sleep(500)

    def lambda_6A9():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_6A9)

    def lambda_6B7():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_6B7)
    SetChrFlags(0x102, 0x80)
    OP_44(0x101, 0xFF)
    Fade(1000)
    OP_6D(-1550, 0, -920, 0)
    OP_67(0, 8670, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(336000, 0)
    OP_6E(306, 0)
    SetChrPos(0x101, 1090, 0, 9990, 66)

    def lambda_721():
        OP_6D(-3060, 0, -2370, 4000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_721)

    def lambda_739():
        OP_94(0x0, 0xFE, 0x0, 0x834, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_739)
    Sleep(100)

    def lambda_754():
        OP_94(0x0, 0xFE, 0x0, 0x7D0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_754)
    Sleep(100)

    def lambda_76F():
        OP_94(0x0, 0xFE, 0x0, 0x7D0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_76F)

    def lambda_785():
        OP_94(0x0, 0xFE, 0x0, 0x834, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_785)
    Sleep(100)

    def lambda_7A0():
        OP_94(0x0, 0xFE, 0x0, 0x578, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_7A0)
    Sleep(1000)
    OP_62(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_7CD():
        OP_8F(0xFE, 0xFFFFEE8A, 0x0, 0xFFFFEE80, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7CD)
    Sleep(500)
    OP_62(0x9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_7FF():
        OP_8F(0xFE, 0xFFFFF29A, 0x0, 0xFFFFEAFC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7FF)
    Sleep(1500)

    ChrTalk(
        0x8,
        "滚、滚开呀，你们这些怪物～！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "呜哇哇哇～\x01",
            "不要过来啊，笨蛋——！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#10A喝啊～～！！\x05\x02",
    )

    Sleep(300)

    def lambda_885():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_885)

    def lambda_893():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_893)

    def lambda_8A1():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_8A1)

    def lambda_8AF():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_8AF)

    def lambda_8BD():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_8BD)

    def lambda_8CB():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_8CB)

    def lambda_8D9():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_8D9)
    Sleep(300)

    def lambda_8EC():
        OP_8E(0xFE, 0xFFFFFB6E, 0x0, 0x8F2, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8EC)

    def lambda_907():
        OP_6D(-2220, 0, -1110, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_907)
    WaitChrThread(0x101, 0x1)

    def lambda_924():

        label("loc_924")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_924")

    QueueWorkItem2(0xA, 2, lambda_924)

    def lambda_935():

        label("loc_935")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_935")

    QueueWorkItem2(0xB, 2, lambda_935)

    def lambda_946():

        label("loc_946")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_946")

    QueueWorkItem2(0xC, 2, lambda_946)

    def lambda_957():

        label("loc_957")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_957")

    QueueWorkItem2(0xD, 2, lambda_957)

    def lambda_968():

        label("loc_968")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_968")

    QueueWorkItem2(0xE, 2, lambda_968)

    def lambda_979():

        label("loc_979")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_979")

    QueueWorkItem2(0x9, 2, lambda_979)

    def lambda_98A():

        label("loc_98A")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_98A")

    QueueWorkItem2(0x8, 2, lambda_98A)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 10)
    SetChrFlags(0x101, 0x1000)
    OP_22(0x1F4, 0x0, 0x64)

    def lambda_9B5():
        OP_99(0xFE, 0x0, 0xC, 0x9C4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9B5)
    OP_8C(0x101, 270, 0)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0x101, 0xFFFFF827, 0x0, 0xFFFFF8A8, 0x7D0, 0x1770)
    OP_22(0xA4, 0x0, 0x64)
    PlayEffect(0x8, 0xFF, 0xFF, -2630, 500, -1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_A22():
        OP_8F(0xFE, 0xFFFFF006, 0x0, 0xFFFFF9DE, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_A22)

    def lambda_A3D():
        OP_94(0x1, 0xFE, 0xB4, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A3D)

    def lambda_A53():
        OP_94(0x1, 0xFE, 0xB4, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_A53)
    Sleep(150)

    def lambda_A6E():
        OP_94(0x1, 0xFE, 0xB4, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_A6E)
    Sleep(100)

    def lambda_A89():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A89)
    Sleep(200)

    def lambda_AA4():
        OP_94(0x1, 0xFE, 0xB4, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_AA4)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 5)

    def lambda_ACA():
        OP_8C(0xFE, 19, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ACA)

    def lambda_AD8():
        OP_8F(0xFE, 0xFFFFF524, 0x0, 0xFFFFF420, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AD8)
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x8,
        "艾丝蒂尔姐姐！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F你们两个！\x01",
            "这里太危险了，快躲到旁边去！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B40():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_B40)

    def lambda_B4E():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_B4E)

    def lambda_B5C():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_B5C)

    def lambda_B6A():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_B6A)

    def lambda_B78():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_B78)

    def lambda_B86():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_B86)

    def lambda_B94():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_B94)
    ClearChrFlags(0x102, 0x80)
    SetChrFlags(0x102, 0x1000)
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 7)
    TurnDirection(0x102, 0x101, 0)
    OP_96(0x102, 0xFFFFFE8E, 0x0, 0x898, 0x3E8, 0x1B58)
    OP_22(0xA4, 0x0, 0x64)
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 9)
    OP_99(0x102, 0x0, 0x5, 0x9C4)
    OP_22(0x1F5, 0x0, 0x64)

    def lambda_BFD():

        label("loc_BFD")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_BFD")

    QueueWorkItem2(0xA, 2, lambda_BFD)

    def lambda_C0E():

        label("loc_C0E")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_C0E")

    QueueWorkItem2(0xB, 2, lambda_C0E)

    def lambda_C1F():

        label("loc_C1F")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_C1F")

    QueueWorkItem2(0xC, 2, lambda_C1F)

    def lambda_C30():

        label("loc_C30")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_C30")

    QueueWorkItem2(0xD, 2, lambda_C30)

    def lambda_C41():

        label("loc_C41")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_C41")

    QueueWorkItem2(0xE, 2, lambda_C41)

    def lambda_C52():

        label("loc_C52")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_C52")

    QueueWorkItem2(0x9, 2, lambda_C52)

    def lambda_C63():

        label("loc_C63")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_C63")

    QueueWorkItem2(0x8, 2, lambda_C63)

    def lambda_C74():
        OP_99(0xFE, 0x5, 0xC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C74)

    def lambda_C84():
        OP_8E(0xFE, 0xFFFFFFD8, 0x0, 0xFFFFFC72, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C84)
    Sleep(100)

    def lambda_CA4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x4B0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_CA4)
    SetChrFlags(0x102, 0x40)
    PlayEffect(0x8, 0xFF, 0xFF, -10, 500, 690, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x102, 0x2)
    OP_44(0x102, 0xFF)
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 7)

    def lambda_D09():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D09)
    OP_96(0x102, 0xFFFFF876, 0x0, 0xFFFFF39E, 0x1F4, 0x1B58)
    OP_22(0xA4, 0x0, 0x64)

    ChrTalk(
        0x9,
        "是约修亚哥哥！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#4P艾丝蒂尔……\x01",
            "知不知道自己一个人冲进来很危险的！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F要训我的话等战斗结束后再说！\x02\x03",
            "来吧，一口气把这些魔兽通通收拾掉！\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    Battle(0x386, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_DF4"),
        (SWITCH_DEFAULT, "loc_DF9"),
    )


    label("loc_DF4")

    OP_B4(0x0)
    Jump("loc_DF9")

    label("loc_DF9")

    SetChrFlags(0x140, 0x80)
    SetChrFlags(0x141, 0x80)
    EventBegin(0x0)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    OP_6D(-3150, 0, -3290, 0)
    OP_67(0, 7450, -10000, 0)
    OP_6B(1710, 0)
    OP_6E(554, 0)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    OP_8C(0x8, 28, 0)
    OP_8C(0x9, 28, 0)
    SetChrPos(0x101, -3210, 0, -460, 291)
    SetChrPos(0x102, -50, 0, -1270, 72)

    def lambda_E92():
        OP_6E(504, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E92)
    OP_6C(225000, 3000)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#502F大获全胜、大获全胜☆\x02",
    )

    CloseMessageWindow()
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 65535)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#017F真的大获全胜吗？\x02\x03",
            "还没看清情况\x01",
            "就那么莽撞地冲进来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F算了～算了。\x01",
            "我们不是打了一场漂亮的战斗嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_187B")

    label("loc_F6B")

    OP_28(0x1, 0x1, 0x8)
    OP_2B(0x1, 0x1)

    ChrTalk(
        0x101,
        "#005F约修亚！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F明白！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 5)
    Sleep(250)
    SetChrChipByIndex(0x102, 7)
    Sleep(250)

    def lambda_FB4():
        OP_8E(0xFE, 0xFFFFFCE0, 0x0, 0xC12, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FB4)
    Sleep(250)

    def lambda_FD4():
        OP_8E(0xFE, 0x442, 0x0, 0x2706, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FD4)
    OP_43(0xA, 0x3, 0x0, 0x2)
    Sleep(100)
    OP_43(0xB, 0x3, 0x0, 0x2)
    Sleep(200)

    def lambda_1007():
        OP_8E(0xFE, 0x442, 0x0, 0x2706, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1007)
    OP_43(0xC, 0x3, 0x0, 0x2)
    Sleep(100)
    OP_43(0xD, 0x3, 0x0, 0x2)
    Sleep(200)
    OP_43(0xE, 0x3, 0x0, 0x2)
    Sleep(500)

    def lambda_1046():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1046)

    def lambda_1054():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1054)
    SetChrFlags(0x102, 0x80)
    OP_44(0x101, 0xFF)
    Fade(1000)
    OP_6D(-1550, 0, -920, 0)
    OP_67(0, 8670, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(336000, 0)
    OP_6E(306, 0)
    SetChrPos(0x101, 1090, 0, 9990, 66)

    def lambda_10BE():
        OP_6D(-3060, 0, -2370, 4000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_10BE)

    def lambda_10D6():
        OP_94(0x0, 0xFE, 0x0, 0x834, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_10D6)
    Sleep(100)

    def lambda_10F1():
        OP_94(0x0, 0xFE, 0x0, 0x7D0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_10F1)
    Sleep(100)

    def lambda_110C():
        OP_94(0x0, 0xFE, 0x0, 0x7D0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_110C)

    def lambda_1122():
        OP_94(0x0, 0xFE, 0x0, 0x834, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1122)
    Sleep(100)

    def lambda_113D():
        OP_94(0x0, 0xFE, 0x0, 0x578, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_113D)
    Sleep(1000)
    OP_62(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_116A():
        OP_8F(0xFE, 0xFFFFEE8A, 0x0, 0xFFFFEE80, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_116A)
    Sleep(500)
    OP_62(0x9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_119C():
        OP_8F(0xFE, 0xFFFFF29A, 0x0, 0xFFFFEAFC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_119C)
    Sleep(1500)

    ChrTalk(
        0x8,
        "滚、滚开呀，你们这些怪物～！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "呜哇哇哇～\x01",
            "不要过来啊，笨蛋——！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#10A喝啊～～！！\x05\x02",
    )

    Sleep(300)

    def lambda_1222():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1222)

    def lambda_1230():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1230)

    def lambda_123E():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_123E)

    def lambda_124C():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_124C)

    def lambda_125A():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_125A)

    def lambda_1268():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1268)

    def lambda_1276():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1276)
    Sleep(300)

    def lambda_1289():
        OP_8E(0xFE, 0xFFFFFB6E, 0x0, 0x8F2, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1289)

    def lambda_12A4():
        OP_6D(-2220, 0, -1110, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_12A4)
    WaitChrThread(0x101, 0x1)

    def lambda_12C1():

        label("loc_12C1")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_12C1")

    QueueWorkItem2(0xA, 2, lambda_12C1)

    def lambda_12D2():

        label("loc_12D2")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_12D2")

    QueueWorkItem2(0xB, 2, lambda_12D2)

    def lambda_12E3():

        label("loc_12E3")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_12E3")

    QueueWorkItem2(0xC, 2, lambda_12E3)

    def lambda_12F4():

        label("loc_12F4")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_12F4")

    QueueWorkItem2(0xD, 2, lambda_12F4)

    def lambda_1305():

        label("loc_1305")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_1305")

    QueueWorkItem2(0xE, 2, lambda_1305)

    def lambda_1316():

        label("loc_1316")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_1316")

    QueueWorkItem2(0x9, 2, lambda_1316)

    def lambda_1327():

        label("loc_1327")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_1327")

    QueueWorkItem2(0x8, 2, lambda_1327)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 10)
    SetChrFlags(0x101, 0x1000)
    OP_22(0x1F4, 0x0, 0x64)

    def lambda_1352():
        OP_99(0xFE, 0x0, 0xC, 0x9C4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1352)
    OP_8C(0x101, 270, 0)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0x101, 0xFFFFF827, 0x0, 0xFFFFF8A8, 0x7D0, 0x1770)
    OP_22(0xA4, 0x0, 0x64)
    PlayEffect(0x8, 0xFF, 0xFF, -2630, 500, -1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_13BF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_13BF)

    def lambda_13D1():
        OP_8F(0xFE, 0xFFFFF006, 0x0, 0xFFFFF9DE, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_13D1)

    def lambda_13EC():
        OP_94(0x1, 0xFE, 0xB4, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_13EC)

    def lambda_1402():
        OP_94(0x1, 0xFE, 0xB4, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1402)
    Sleep(150)

    def lambda_141D():
        OP_94(0x1, 0xFE, 0xB4, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_141D)
    Sleep(100)

    def lambda_1438():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1438)
    Sleep(200)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 5)

    def lambda_1463():
        OP_8C(0xFE, 19, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1463)

    def lambda_1471():
        OP_8F(0xFE, 0xFFFFF524, 0x0, 0xFFFFF420, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1471)

    def lambda_148C():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_148C)

    def lambda_149A():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_149A)

    def lambda_14A8():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_14A8)

    def lambda_14B6():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_14B6)

    def lambda_14C4():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_14C4)

    def lambda_14D2():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_14D2)
    ClearChrFlags(0x102, 0x80)
    SetChrFlags(0x102, 0x1000)
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 7)
    TurnDirection(0x102, 0x101, 0)
    OP_96(0x102, 0xFFFFFE8E, 0x0, 0x898, 0x3E8, 0x1B58)
    OP_22(0xA4, 0x0, 0x64)
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 9)
    OP_99(0x102, 0x0, 0x5, 0x9C4)
    OP_22(0x1F5, 0x0, 0x64)

    def lambda_153B():

        label("loc_153B")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_153B")

    QueueWorkItem2(0xA, 2, lambda_153B)

    def lambda_154C():

        label("loc_154C")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_154C")

    QueueWorkItem2(0xB, 2, lambda_154C)

    def lambda_155D():

        label("loc_155D")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_155D")

    QueueWorkItem2(0xC, 2, lambda_155D)

    def lambda_156E():

        label("loc_156E")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_156E")

    QueueWorkItem2(0xD, 2, lambda_156E)

    def lambda_157F():

        label("loc_157F")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_157F")

    QueueWorkItem2(0xE, 2, lambda_157F)

    def lambda_1590():

        label("loc_1590")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_1590")

    QueueWorkItem2(0x9, 2, lambda_1590)

    def lambda_15A1():

        label("loc_15A1")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_15A1")

    QueueWorkItem2(0x8, 2, lambda_15A1)

    def lambda_15B2():
        OP_99(0xFE, 0x5, 0xC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_15B2)

    def lambda_15C2():
        OP_8E(0xFE, 0xFFFFFFD8, 0x0, 0xFFFFFC72, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_15C2)
    Sleep(100)

    def lambda_15E2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x4B0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_15E2)
    SetChrFlags(0x102, 0x40)
    PlayEffect(0x8, 0xFF, 0xFF, -10, 500, 690, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x102, 0x2)
    OP_44(0x102, 0xFF)
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 7)

    def lambda_1647():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1647)
    OP_96(0x102, 0xFFFFF876, 0x0, 0xFFFFF39E, 0x1F4, 0x1B58)
    OP_22(0xA4, 0x0, 0x64)

    ChrTalk(
        0x8,
        "艾丝蒂尔姐姐！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "是约修亚哥哥！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F你们两个！\x01",
            "这里太危险了，快躲到旁边去！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F#4P我们会马上收拾它们的！\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    Battle(0x3B0, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_1714"),
        (SWITCH_DEFAULT, "loc_1719"),
    )


    label("loc_1714")

    OP_B4(0x0)
    Jump("loc_1719")

    label("loc_1719")

    EventBegin(0x0)
    SetChrFlags(0x140, 0x80)
    SetChrFlags(0x141, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    OP_6D(-3150, 0, -3290, 0)
    OP_67(0, 7450, -10000, 0)
    OP_6B(1710, 0)
    OP_6E(554, 0)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    OP_8C(0x8, 28, 0)
    OP_8C(0x9, 28, 0)
    SetChrPos(0x101, -3210, 0, -460, 291)
    SetChrPos(0x102, -50, 0, -1270, 72)

    def lambda_17B2():
        OP_6E(504, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17B2)
    OP_6C(225000, 3000)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#001F好啦，都收拾掉了。\x02",
    )

    CloseMessageWindow()
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 65535)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#019F嗯，大家都没事，太好了。\x02\x03",
            "#010F而且我们联合出击的时机\x01",
            "也掌握得很不错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F嘿嘿，是吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_187B")

    label("loc_187B")


    ChrTalk(
        0x9,
        "结、结束了吗……？\x02",
    )

    CloseMessageWindow()

    def lambda_1899():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1899)

    def lambda_18A7():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_18A7)

    ChrTalk(
        0x8,
        "厉害～～！\x02",
    )

    CloseMessageWindow()

    def lambda_18C5():

        label("loc_18C5")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_18C5")

    QueueWorkItem2(0x8, 1, lambda_18C5)

    def lambda_18D6():

        label("loc_18D6")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_18D6")

    QueueWorkItem2(0x101, 1, lambda_18D6)

    def lambda_18E7():

        label("loc_18E7")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_18E7")

    QueueWorkItem2(0x102, 1, lambda_18E7)
    OP_62(0x8, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_95(0x8, 0x0, 0x0, 0x0, 0x2BC, 0x1770)
    OP_95(0x8, 0x0, 0x0, 0x0, 0x2BC, 0x1770)
    Sleep(300)

    def lambda_193D():
        OP_8E(0xFE, 0xFFFFF196, 0x0, 0xFFFFF9E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_193D)
    Sleep(300)

    def lambda_195D():
        OP_6D(-3440, 0, -2740, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_195D)
    Sleep(100)

    def lambda_197A():

        label("loc_197A")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_197A")

    QueueWorkItem2(0x9, 1, lambda_197A)

    def lambda_198B():
        OP_8E(0xFE, 0xFFFFFC04, 0x0, 0xFFFFF39E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_198B)
    WaitChrThread(0x8, 0x2)
    OP_96(0x8, 0xFFFFEE6C, 0x0, 0xFFFFFBFA, 0x320, 0x1770)
    OP_96(0x8, 0xFFFFEF66, 0x0, 0xFFFFFF42, 0x4B0, 0x1770)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x8,
        "艾丝蒂尔，你还蛮厉害的嘛！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "虽然只是个小女孩，不过还真有一手啊！\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#005F你这个笨蛋！\x02",
    )

    CloseMessageWindow()

    def lambda_1A5B():
        OP_6D(-4540, 0, -1610, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1A5B)
    SetChrFlags(0x101, 0x40)
    OP_92(0x101, 0x8, 0x190, 0x1770, 0x0)
    OP_22(0x7D, 0x0, 0x64)
    OP_94(0x1, 0x8, 0xB4, 0x1F4, 0x1770, 0x0)
    Sleep(500)
    OP_8F(0x8, 0xFFFFE98A, 0x0, 0x14, 0x7D0, 0x0)

    ChrTalk(
        0x8,
        "好疼，你干什么呀！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F真是的，你呀！\x02\x03",
            "居然把这么乖的帕特\x01",
            "都带到这种地方来……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 1700, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1300)
    OP_62(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_44(0x8, 0xFF)

    def lambda_1B3F():
        OP_8C(0xFE, 270, 800)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1B3F)

    def lambda_1B4D():
        OP_94(0x1, 0xFE, 0xB4, 0x5DC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1B4D)
    ClearChrFlags(0x101, 0x1000)
    OP_8F(0x101, 0xFFFFE5B6, 0x0, 0x10E, 0x1388, 0x0)
    SetChrFlags(0x8, 0x4)
    OP_91(0x8, 0x0, 0x64, 0x0, 0x320, 0x0)

    def lambda_1B95():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B95)
    OP_97(0x8, 0xFFFFE5B6, 0x10E, 0xFFFD40E0, 0xFA0, 0x3)

    ChrTalk(
        0x101,
        "#005F给·我·好·好·反·省！\x02",
    )

    CloseMessageWindow()

    def lambda_1BDB():
        OP_91(0xFE, 0x4B0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1BDB)
    OP_91(0x8, 0x4B0, 0x0, 0x0, 0x7D0, 0x0)
    OP_9E(0x8, 0x3C, 0x0, 0x12C, 0x1F40)
    OP_9E(0x8, 0x3C, 0x0, 0x12C, 0x1F40)

    ChrTalk(
        0x8,
        "疼疼疼，快住手！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "粗暴女！白痴艾丝蒂尔！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F而且还用这种口气\x01",
            "对你的救命恩人说话……\x02\x03",
            "#009F看来不给你点严厉的惩罚是不行的～\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x8, 0x3C, 0x0, 0x1F4, 0x1F40)

    ChrTalk(
        0x8,
        "疼疼疼疼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "艾丝蒂尔姐姐！\x01",
            "饶了我吧，都是我不好！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1D0B():

        label("loc_1D0B")

        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        OP_48()
        Jump("loc_1D0B")

    QueueWorkItem2(0x8, 3, lambda_1D0B)

    ChrTalk(
        0x9,
        "#1P那、那个……姐姐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1P这样就够了吧，饶了他吧。\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xA, 11)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -16000, 0, 0, 282)

    def lambda_1D75():
        OP_8E(0xFE, 0xFFFFD508, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1D75)

    ChrTalk(
        0x101,
        (
            "#006F没关系的，对这样的调皮蛋来说\x01",
            "小小的惩罚反而有好处……\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xA, 0x1)
    TurnDirection(0xA, 0x101, 400)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    ClearChrFlags(0x101, 0x1000)

    ChrTalk(
        0x102,
        "#016F艾丝蒂尔，后面！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊……\x02",
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)
    OP_44(0x101, 0xFF)
    ClearChrFlags(0x8, 0x4)
    TurnDirection(0x101, 0xA, 400)
    TurnDirection(0x8, 0x101, 400)

    def lambda_1E44():
        OP_6D(-6670, 0, -1080, 2000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1E44)

    def lambda_1E5C():
        OP_8E(0xFE, 0xFFFFDAE4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1E5C)
    Sleep(1500)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#002F糟了……\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x0, "battle\\\\mgblood.eff")

    ChrTalk(
        0x102,
        "#510F#4P……该死！\x02",
    )

    CloseMessageWindow()
    OP_43(0x102, 0x0, 0x0, 0x4)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x14, 0x4)
    SetChrFlags(0x10, 0x4)
    SetChrPos(0x11, -21000, 0, 0, 0)
    SetChrPos(0x12, -21040, 0, 0, 0)
    SetChrPos(0x13, -21040, 0, 0, 0)
    SetChrPos(0x14, -21040, 0, 0, 0)
    SetChrPos(0x10, -21040, 0, 0, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x14, 0x40)
    SetChrFlags(0x10, 0x40)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0xC8, 0x0)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x96, 0x0)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x64, 0x0)
    OP_9F(0x14, 0xFF, 0xFF, 0xFF, 0x32, 0x0)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 12)

    def lambda_1FB6():
        OP_8E(0xA, 0xFFFFEA84, 0x0, 0x0, 0xA8C, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1FB6)

    def lambda_1FD1():
        OP_6D(-5130, 0, -1080, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1FD1)

    def lambda_1FE9():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1FE9)

    def lambda_1FFF():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1FFF)
    SetChrFlags(0x10, 0x2)
    SetChrFlags(0x11, 0x2)
    SetChrFlags(0x12, 0x2)
    SetChrFlags(0x13, 0x2)
    SetChrFlags(0x14, 0x2)
    SetChrSubChip(0x10, 0)
    SetChrSubChip(0x11, 0)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x13, 0)
    SetChrSubChip(0x14, 0)
    SetChrFlags(0x10, 0x20)
    SetChrFlags(0x11, 0x20)
    SetChrFlags(0x12, 0x20)
    SetChrFlags(0x13, 0x20)
    SetChrFlags(0x14, 0x20)
    SetChrChipByIndex(0x10, 13)
    SetChrChipByIndex(0x11, 13)
    SetChrChipByIndex(0x12, 13)
    SetChrChipByIndex(0x13, 13)
    SetChrChipByIndex(0x14, 13)

    def lambda_2079():
        OP_8E(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2079)
    Sleep(100)

    def lambda_2099():
        OP_8E(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2099)
    Sleep(100)

    def lambda_20B9():
        OP_8E(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_20B9)
    Sleep(100)

    def lambda_20D9():
        OP_8E(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_20D9)
    Sleep(100)

    def lambda_20F9():
        OP_8E(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_20F9)
    OP_20(0x3E8)
    WaitChrThread(0x10, 0x1)
    OP_43(0x11, 0x1, 0x0, 0x6)
    OP_43(0x12, 0x1, 0x0, 0x7)
    OP_43(0x13, 0x1, 0x0, 0x8)
    OP_43(0x14, 0x1, 0x0, 0x9)
    SetChrSubChip(0x10, 1)
    OP_96(0x10, 0xFFFFE1EC, 0x0, 0x5DC, 0x4B0, 0x2710)
    OP_22(0xA4, 0x0, 0x64)
    OP_43(0x10, 0x1, 0x0, 0x5)
    WaitChrThread(0xA, 0x1)
    OP_22(0x9B, 0x0, 0x64)
    PlayEffect(0x8, 0xFF, 0xFF, -5500, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x9, 0xFF, 0xFF, -5500, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, -5500, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xA, 0x40)

    def lambda_221A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_221A)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F……啊？\x02",
    )

    CloseMessageWindow()
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 65535)
    TurnDirection(0x102, 0x10, 400)
    Sleep(500)

    ChrTalk(
        0x102,
        "#010F太好了，终于来了。\x02",
    )

    CloseMessageWindow()

    def lambda_227D():
        OP_6C(270000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_227D)

    def lambda_228D():
        OP_6D(-5500, 0, 0, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_228D)
    Sleep(1300)
    SetChrSubChip(0x10, 4)
    Sleep(1200)

    def lambda_22B4():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_22B4)

    def lambda_22C2():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_22C2)

    def lambda_22D0():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_22D0)
    OP_1D(0x58)
    Sleep(500)

    ChrTalk(
        0x10,
        (
            "#085F还是太嫩了，艾丝蒂尔。\x02\x03",
            "为了防备难以预见的威胁，\x01",
            "必须时常保持敏锐的感觉才行哦。\x02\x03",
            "#080F这也是游击士的心得。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_235A():

        label("loc_235A")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_235A")

    QueueWorkItem2(0x101, 1, lambda_235A)

    ChrTalk(
        0x101,
        (
            "#004F#4P老、老爸！？\x02\x03",
            "为、什么你会在这儿呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#080F没什么，爱娜把事情都告诉我了。\x02\x03",
            "虽然前往目的地的速度\x01",
            "和处事的判断力都相当不错……\x02\x03",
            "不过最后还是松懈了啊，知道吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F#4P哎呀，真没面子……\x02",
    )

    CloseMessageWindow()

    def lambda_2439():
        OP_6D(-6270, 0, 130, 2000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_2439)

    def lambda_2451():

        label("loc_2451")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_2451")

    QueueWorkItem2(0x8, 1, lambda_2451)

    def lambda_2462():
        OP_8F(0xFE, 0xFFFFEED0, 0x0, 0x5FA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2462)

    def lambda_247D():

        label("loc_247D")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_247D")

    QueueWorkItem2(0x9, 1, lambda_247D)

    def lambda_248E():
        OP_8F(0xFE, 0xFFFFF5E2, 0x0, 0xFFFFF9C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_248E)
    OP_8E(0x102, 0xFFFFED90, 0x0, 0xFFFFFD12, 0xBB8, 0x0)
    OP_44(0x102, 0xFF)
    OP_8C(0x102, 315, 400)
    WaitChrThread(0x8, 0x2)

    ChrTalk(
        0x102,
        (
            "#013F多亏您来了，爸爸。\x02\x03",
            "对不起，有我在还发生这种事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#081F啊，要做到真正保护好别人，\x01",
            "其实你也还差得远呢。\x02\x03",
            "不过再努力一下就会好很多的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#011F……嗯。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#080F那我们回去吧。\x02\x03",
            "孩子们，还走得动吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "嗯、嗯……！\x02",
    )

    CloseMessageWindow()

    def lambda_25B4():
        OP_8E(0xFE, 0xFFFFE9BC, 0x0, 0xFFFFF948, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_25B4)
    Sleep(200)

    def lambda_25D4():
        OP_8E(0xFE, 0xFFFFE476, 0x0, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_25D4)

    def lambda_25EF():

        label("loc_25EF")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_25EF")

    QueueWorkItem2(0x8, 1, lambda_25EF)
    WaitChrThread(0x9, 0x1)

    def lambda_2605():
        OP_8E(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFFBE6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2605)

    def lambda_2620():

        label("loc_2620")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_2620")

    QueueWorkItem2(0x9, 1, lambda_2620)
    WaitChrThread(0x9, 0x2)
    WaitChrThread(0x8, 0x2)

    ChrTalk(
        0x8,
        "太、太有型了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "卡西乌斯叔叔，\x01",
            "你比艾丝蒂尔要酷上一百倍呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#081F哈哈哈，那是当然的啦。\x02\x03",
            "好了，那我们回城镇去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "嗯！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0)
    ClearChrFlags(0x10, 0x2)
    ClearChrFlags(0x10, 0x20)
    SetChrChipByIndex(0x10, 4)
    OP_8C(0x10, 90, 0)
    OP_8C(0x10, 270, 400)

    def lambda_26E9():
        OP_8E(0xFE, 0xFFFF6D2A, 0x0, 0xFFFFFF88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_26E9)
    Sleep(300)

    def lambda_2709():
        OP_8E(0xFE, 0xFFFF6D2A, 0x0, 0xFFFFFF88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2709)
    Sleep(100)

    def lambda_2729():
        OP_8E(0xFE, 0xFFFF6D2A, 0x0, 0xFFFFFF88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2729)

    def lambda_2744():
        OP_6E(471, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2744)

    def lambda_2754():
        OP_6C(224000, 3000)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2754)
    OP_6D(-6000, 0, 290, 2500)
    OP_63(0x101)
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#007F#4P……唔～…………\x02\x03",
            "虽然很感谢老爸救了我们……\x02\x03",
            "可是为什么他会把\x01",
            "我的风头全都抢光了啊！？\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_8C(0x101, 45, 400)
    Sleep(500)

    ChrTalk(
        0x101,
        "#009F#5S#4P我不要啊——！\x02",
    )

    CloseMessageWindow()
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#019F哈哈，这也没办法啊。\x02\x03",
            "#010F不管怎么说……\x01",
            "他可是卡西乌斯·布莱特啊。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_28(0x1, 0x1, 0x20)
    RemoveParty(0x3F, 0xFF)
    RemoveParty(0x40, 0xFF)
    OP_A2(0x217)
    NewScene("ED6_DT01/T0121   ._SN", 1, 0, 0)
    IdleLoop()
    Return()

    # Function_3_358 end

    def Function_4_28A0(): pass

    label("Function_4_28A0")

    ClearChrFlags(0x102, 0x1000)
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 7)
    Sleep(500)

    def lambda_28C0():
        OP_8E(0xFE, 0xFFFFF600, 0x0, 0xFFFFFC54, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_28C0)
    Return()

    # Function_4_28A0 end

    def Function_5_28D6(): pass

    label("Function_5_28D6")

    OP_96(0xFE, 0xFFFFE7C8, 0x0, 0x96, 0x3E8, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    SetChrSubChip(0xFE, 2)
    Sleep(500)
    OP_96(0xFE, 0xFFFFE1EC, 0x0, 0x0, 0x1F4, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    SetChrSubChip(0xFE, 3)
    Return()

    # Function_5_28D6 end

    def Function_6_291E(): pass

    label("Function_6_291E")

    Sleep(100)
    SetChrSubChip(0xFE, 1)
    OP_96(0xFE, 0xFFFFE1EC, 0x0, 0x5DC, 0x4B0, 0x2710)
    OP_96(0xFE, 0xFFFFE7C8, 0x0, 0x96, 0x3E8, 0x1388)
    SetChrSubChip(0xFE, 2)
    Sleep(500)
    OP_96(0xFE, 0xFFFFE1EC, 0x0, 0x0, 0x1F4, 0x1388)
    SetChrFlags(0x11, 0x80)
    Return()

    # Function_6_291E end

    def Function_7_297D(): pass

    label("Function_7_297D")

    Sleep(200)
    SetChrSubChip(0xFE, 1)
    OP_96(0xFE, 0xFFFFE1EC, 0x0, 0x5DC, 0x4B0, 0x2710)
    OP_96(0xFE, 0xFFFFE7C8, 0x0, 0x96, 0x3E8, 0x1388)
    SetChrSubChip(0xFE, 2)
    Sleep(500)
    OP_96(0xFE, 0xFFFFE1EC, 0x0, 0x0, 0x1F4, 0x1388)
    SetChrFlags(0x12, 0x80)
    Return()

    # Function_7_297D end

    def Function_8_29DC(): pass

    label("Function_8_29DC")

    Sleep(300)
    SetChrSubChip(0xFE, 1)
    OP_96(0xFE, 0xFFFFE1EC, 0x0, 0x5DC, 0x4B0, 0x2710)
    OP_96(0xFE, 0xFFFFE7C8, 0x0, 0x96, 0x3E8, 0x1388)
    SetChrSubChip(0xFE, 2)
    Sleep(500)
    OP_96(0xFE, 0xFFFFE1EC, 0x0, 0x0, 0x1F4, 0x1388)
    SetChrFlags(0x13, 0x80)
    Return()

    # Function_8_29DC end

    def Function_9_2A3B(): pass

    label("Function_9_2A3B")

    Sleep(400)
    SetChrSubChip(0xFE, 1)
    OP_96(0xFE, 0xFFFFE1EC, 0x0, 0x5DC, 0x4B0, 0x2710)
    OP_96(0xFE, 0xFFFFE7C8, 0x0, 0x96, 0x3E8, 0x1388)
    SetChrSubChip(0xFE, 2)
    Sleep(500)
    OP_96(0xFE, 0xFFFFE1EC, 0x0, 0x0, 0x1F4, 0x1388)
    SetChrFlags(0x14, 0x80)
    Return()

    # Function_9_2A3B end

    SaveToFile()

Try(main)
