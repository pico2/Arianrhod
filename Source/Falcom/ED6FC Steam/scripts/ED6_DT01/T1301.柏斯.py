from ED6ScenarioHelper import *

def main():
    # 柏斯

    CreateScenaFile(
        FileName            = 'T1301   ._SN',
        MapName             = 'Bose',
        Location            = 'T1301.x',
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
        '士兵卡多尔斯',                         # 9
        '士兵阿萨',                             # 10
        '魔兽',                                 # 11
        '魔兽',                                 # 12
        '魔兽',                                 # 13
        '魔兽',                                 # 14
        '魔兽',                                 # 15
        '魔兽',                                 # 16
        '魔兽',                                 # 17
        '赛尔斯特队长',                         # 18
        '赛罗斯副长',                           # 19
        '士兵迈奇',                             # 20
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
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT09/CH10060 ._CH',             # 01
        'ED6_DT09/CH10061 ._CH',             # 02
        'ED6_DT09/CH10062 ._CH',             # 03
        'ED6_DT09/CH10064 ._CH',             # 04
        'ED6_DT09/CH10063 ._CH',             # 05
        'ED6_DT07/CH01310 ._CH',             # 06
        'ED6_DT07/CH00150 ._CH',             # 07
        'ED6_DT07/CH00151 ._CH',             # 08
        'ED6_DT07/CH00152 ._CH',             # 09
        'ED6_DT07/CH00100 ._CH',             # 0A
        'ED6_DT07/CH00101 ._CH',             # 0B
        'ED6_DT07/CH00110 ._CH',             # 0C
        'ED6_DT07/CH00111 ._CH',             # 0D
        'ED6_DT07/CH01650 ._CH',             # 0E
        'ED6_DT06/CH20053 ._CH',             # 0F
        'ED6_DT06/CH20053 ._CH',             # 10
        'ED6_DT07/CH00330 ._CH',             # 11
        'ED6_DT07/CH00331 ._CH',             # 12
        'ED6_DT07/CH00332 ._CH',             # 13
        'ED6_DT07/CH00320 ._CH',             # 14
        'ED6_DT07/CH00321 ._CH',             # 15
        'ED6_DT07/CH00322 ._CH',             # 16
        'ED6_DT07/CH00324 ._CH',             # 17
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT09/CH10060P._CP',             # 01
        'ED6_DT09/CH10061P._CP',             # 02
        'ED6_DT09/CH10062P._CP',             # 03
        'ED6_DT09/CH10064P._CP',             # 04
        'ED6_DT09/CH10063P._CP',             # 05
        'ED6_DT07/CH01310P._CP',             # 06
        'ED6_DT07/CH00150P._CP',             # 07
        'ED6_DT07/CH00151P._CP',             # 08
        'ED6_DT07/CH00152P._CP',             # 09
        'ED6_DT07/CH00100P._CP',             # 0A
        'ED6_DT07/CH00101P._CP',             # 0B
        'ED6_DT07/CH00110P._CP',             # 0C
        'ED6_DT07/CH00111P._CP',             # 0D
        'ED6_DT07/CH01650P._CP',             # 0E
        'ED6_DT06/CH20053P._CP',             # 0F
        'ED6_DT06/CH20053P._CP',             # 10
        'ED6_DT07/CH00330P._CP',             # 11
        'ED6_DT07/CH00331P._CP',             # 12
        'ED6_DT07/CH00332P._CP',             # 13
        'ED6_DT07/CH00320P._CP',             # 14
        'ED6_DT07/CH00321P._CP',             # 15
        'ED6_DT07/CH00322P._CP',             # 16
        'ED6_DT07/CH00324P._CP',             # 17
    )

    DeclNpc(
        X                   = -52000,
        Z                   = -50,
        Y                   = 12200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -52000,
        Z                   = -50,
        Y                   = 12200,
        Direction           = 0,
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
        X                   = -52000,
        Z                   = -50,
        Y                   = 12200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -52000,
        Z                   = -50,
        Y                   = 12200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -52000,
        Z                   = -50,
        Y                   = 12200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -52000,
        Z                   = -50,
        Y                   = 12200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -52000,
        Z                   = -50,
        Y                   = 12200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -52000,
        Z                   = -50,
        Y                   = 12200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -52000,
        Z                   = -50,
        Y                   = 12200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -52000,
        Z                   = -50,
        Y                   = 12200,
        Direction           = 0,
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
        X                   = -52000,
        Z                   = -50,
        Y                   = 12200,
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
        X                   = -46890,
        Z                   = -50,
        Y                   = -15230,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 196631,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_2EA",          # 00, 0
        "Function_1_31F",          # 01, 1
        "Function_2_332",          # 02, 2
        "Function_3_348",          # 03, 3
        "Function_4_B0A",          # 04, 4
        "Function_5_2505",         # 05, 5
        "Function_6_274F",         # 06, 6
        "Function_7_2A64",         # 07, 7
    )


    def Function_0_2EA(): pass

    label("Function_0_2EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_2FD")
    OP_A3(0x3FA)
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_2FD")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (102, "loc_309"),
        (SWITCH_DEFAULT, "loc_31E"),
    )


    label("loc_309")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 4)
    Jump("loc_31E")

    label("loc_31E")

    Return()

    # Function_0_2EA end

    def Function_1_31F(): pass

    label("Function_1_31F")

    OP_16(0x2, 0xFA0, 0xFFFD48B0, 0xFFFE17B8, 0x30044)
    Return()

    # Function_1_31F end

    def Function_2_332(): pass

    label("Function_2_332")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_347")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_332")

    label("loc_347")

    Return()

    # Function_2_332 end

    def Function_3_348(): pass

    label("Function_3_348")

    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_4A(0xE, 255)
    OP_4A(0xF, 255)
    SetChrPos(0x8, -50060, 0, 12640, 0)
    SetChrPos(0x9, -50070, 450, 8800, 0)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-50200, 0, 9940, 0)
    OP_6B(3000, 0)
    OP_6C(225000, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_70(0x6, 0x64)
    OP_73(0x6)
    SetChrFlags(0x9, 0x4)
    OP_8E(0x9, 0xFFFF3CB9, 0x1C2, 0x2BE3, 0x7D0, 0x0)
    ClearChrFlags(0x9, 0x4)
    OP_4A(0x8, 255)

    ChrTalk(
        0x9,
        (
            "#1P久等了。\x01",
            "已经到交班时间了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(
        0x8,
        "啊，已经这么晚了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不过我说，既然没有人通行，\x01",
            "那就没必要一直在这里站岗吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "其实我们可以整夜关着门，\x01",
            "这样不就更省事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1P这是上头的决定，我们只能照办。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1P之前的空贼事件就不说了，\x01",
            "最近还经常感觉到附近有骚动……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x9, 270, 400)
    Sleep(200)
    OP_8C(0x9, 0, 400)
    OP_8C(0x9, 90, 400)
    Sleep(500)
    OP_62(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        "怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1P你没听到有声音吗？\x01",
            "听！沙沙沙的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "是风吹的声音吧？\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xA, -46050, -600, 23150, 225)
    SetChrPos(0xB, -43720, -300, 22970, 225)
    SetChrPos(0xC, -45010, -400, 25300, 225)
    SetChrPos(0xD, -44180, -500, 24380, 225)
    SetChrPos(0xE, -43420, -500, 25190, 225)
    SetChrPos(0xF, -42140, -600, 25680, 225)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    OP_20(0x5DC)
    OP_21()
    OP_22(0x193, 0x0, 0x64)

    NpcTalk(
        0xF,
        "低吟声",
        "#1P咕噜噜噜……\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x9, 45, 400)
    OP_8C(0x8, 45, 400)
    OP_1D(0x52)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xE, 0x40)
    SetChrFlags(0xF, 0x40)

    def lambda_6B5():
        OP_6B(3000, 2500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6B5)

    def lambda_6C5():
        OP_6D(-47350, 0, 17130, 1700)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6C5)
    Sleep(500)

    def lambda_6E2():
        OP_8E(0xFE, 0xFFFF275C, 0x0, 0x3EEE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6E2)

    def lambda_6FD():
        OP_8E(0xFE, 0xFFFF1708, 0x0, 0x401A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6FD)

    def lambda_718():
        OP_8E(0xFE, 0xFFFF236A, 0x0, 0x41F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_718)

    def lambda_733():
        OP_8E(0xFE, 0xFFFF1D2A, 0x0, 0x4344, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_733)
    Sleep(100)

    def lambda_753():
        OP_8E(0xFE, 0xFFFF1884, 0x0, 0x4754, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_753)
    Sleep(100)

    def lambda_773():
        OP_8E(0xFE, 0xFFFF2374, 0x0, 0x4830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_773)
    Sleep(1000)

    def lambda_793():
        OP_6D(-49494, 0, 13760, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_793)

    def lambda_7AB():
        OP_8E(0xFE, 0xFFFF4A84, 0x0, 0x3EEE, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_7AB)
    Sleep(150)

    def lambda_7CB():
        OP_8E(0xFE, 0xFFFF3A30, 0x0, 0x401A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7CB)
    Sleep(150)

    def lambda_7EB():
        OP_8E(0xFE, 0xFFFF444E, 0x0, 0x4330, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_7EB)
    Sleep(150)

    def lambda_80B():
        OP_8E(0xFE, 0xFFFF4052, 0x0, 0x4344, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_80B)
    Sleep(150)

    def lambda_82B():
        OP_8E(0xFE, 0xFFFF3C24, 0x0, 0x4650, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_82B)
    Sleep(150)

    def lambda_84B():
        OP_8E(0xFE, 0xFFFF4890, 0x0, 0x4650, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_84B)
    WaitChrThread(0xB, 0x1)
    SetChrChipByIndex(0xB, 1)
    OP_43(0xB, 0x1, 0x0, 0x2)
    PlayEffect(0x12, 0xFF, 0xB, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)

    def lambda_8AC():
        OP_94(0x1, 0xFE, 0x0, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_8AC)
    WaitChrThread(0xA, 0x1)
    SetChrChipByIndex(0xA, 1)
    OP_43(0xA, 0x1, 0x0, 0x2)
    PlayEffect(0x12, 0xFF, 0xA, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)

    def lambda_908():
        OP_94(0x1, 0xFE, 0x0, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_908)
    WaitChrThread(0xD, 0x1)
    SetChrChipByIndex(0xD, 1)
    OP_43(0xD, 0x1, 0x0, 0x2)
    PlayEffect(0x12, 0xFF, 0xD, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)

    def lambda_964():
        OP_94(0x1, 0xFE, 0x0, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_964)
    WaitChrThread(0xC, 0x1)
    SetChrChipByIndex(0xC, 1)
    OP_43(0xC, 0x1, 0x0, 0x2)
    PlayEffect(0x12, 0xFF, 0xC, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)

    def lambda_9C0():
        OP_94(0x1, 0xFE, 0x0, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_9C0)
    WaitChrThread(0xE, 0x1)
    SetChrChipByIndex(0xE, 1)
    OP_43(0xE, 0x1, 0x0, 0x2)
    PlayEffect(0x12, 0xFF, 0xE, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)

    def lambda_A1C():
        OP_94(0x1, 0xFE, 0x0, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_A1C)
    WaitChrThread(0xF, 0x1)
    SetChrChipByIndex(0xF, 1)
    OP_43(0xF, 0x1, 0x0, 0x2)
    PlayEffect(0x12, 0xFF, 0xF, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)

    def lambda_A78():
        OP_94(0x1, 0xFE, 0x0, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_A78)
    WaitChrThread(0xE, 0x2)
    TurnDirection(0xE, 0x8, 0)
    WaitChrThread(0x101, 0x1)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_94(0x1, 0x8, 0xB4, 0x1F4, 0x3E8, 0x0)

    ChrTalk(
        0x8,
        "狼、狼群！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "喂喂，不是做梦吧！？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3FA)
    SetMapFlags(0x2000000)
    NewScene("ED6_DT01/T1311   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_348 end

    def Function_4_B0A(): pass

    label("Function_4_B0A")

    AddParty(0x5, 0xFF)
    ClearMapFlags(0x10)
    OP_31(0x5, 0x0, 0x16)
    OP_B5(0x5, 0x0)
    OP_B5(0x5, 0x1)
    OP_B5(0x5, 0x2)
    OP_41(0x5, 0x97)
    OP_41(0x5, 0xF2)
    OP_41(0x5, 0x110)
    OP_41(0x5, 0x25E, 0x0)
    OP_41(0x5, 0x258, 0x1)
    OP_41(0x5, 0x261, 0x2)
    OP_35(0x5, 0xC8)
    OP_35(0x5, 0xC9)
    OP_36(0x5, 0xFF)
    OP_31(0x5, 0x5, 0x64)
    EventBegin(0x0)
    OP_6F(0x6, 120)
    OP_72(0x6, 0x10)
    OP_6F(0x7, 120)
    OP_72(0x7, 0x10)
    OP_6D(-49790, 450, 10030, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(4080, 0)
    OP_6C(201000, 0)
    OP_6E(262, 0)
    SetChrPos(0x106, -49160, 450, 11070, 20)
    SetChrPos(0x101, -50770, 450, 11200, 20)
    SetChrPos(0x102, -50340, 450, 10410, 20)
    SetChrPos(0x8, -52080, 0, 15480, 315)
    SetChrPos(0x9, -47500, 0, 13630, 90)
    SetChrPos(0x12, -49730, 0, 15340, 0)
    SetChrPos(0x11, -48130, 0, 14880, 45)
    SetChrChipByIndex(0x8, 20)
    SetChrChipByIndex(0x9, 20)
    SetChrChipByIndex(0x12, 20)
    SetChrChipByIndex(0x11, 17)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_4A(0xE, 255)
    OP_4A(0xF, 255)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xA, -45600, 0, 14320, 270)
    SetChrPos(0xB, -47500, 0, 15620, 225)
    SetChrPos(0xF, -44730, 0, 19520, 225)
    SetChrPos(0xD, -47980, 0, 18190, 180)
    SetChrPos(0xC, -50380, 0, 18680, 135)
    SetChrPos(0xE, -51820, 0, 17000, 135)
    TurnDirection(0xA, 0x9, 0)
    TurnDirection(0xB, 0x11, 0)
    TurnDirection(0xF, 0x11, 0)
    TurnDirection(0xD, 0x12, 0)
    TurnDirection(0xC, 0x12, 0)
    TurnDirection(0xE, 0x8, 0)
    TurnDirection(0x12, 0xD, 0)
    SetChrChipByIndex(0xA, 1)
    SetChrChipByIndex(0xB, 1)
    SetChrChipByIndex(0xC, 1)
    SetChrChipByIndex(0xD, 1)
    SetChrChipByIndex(0xE, 1)
    SetChrChipByIndex(0xF, 1)
    OP_43(0xA, 0x1, 0x0, 0x2)
    OP_43(0xC, 0x1, 0x0, 0x2)
    OP_43(0xD, 0x1, 0x0, 0x2)
    OP_43(0xE, 0x1, 0x0, 0x2)
    OP_43(0xF, 0x1, 0x0, 0x2)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)
    SetChrChipByIndex(0x106, 15)
    OP_43(0x11, 0x1, 0x0, 0x6)
    OP_43(0x9, 0x1, 0x0, 0x5)
    OP_43(0x12, 0x1, 0x0, 0x7)
    OP_6D(-49360, 450, 13230, 2000)

    ChrTalk(
        0x102,
        "#012F#2P狼群……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#2P不、不好了！\x01",
            "我们快点去帮忙吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#053F#1P……给我回去，这里不用你们管。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(
        0x101,
        (
            "#005F#2P什、什么不用我们管！？\x02\x03",
            "你说这种话还算是个游击士吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#050F#1P你们别理解错了。\x01",
            "守护关所是军队的使命。\x02\x03",
            "而且这些士兵都受过严格训练，\x01",
            "他们很快就会把这群狼消灭掉的。\x02\x03",
            "你们过去帮忙也只是多余罢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F#2P虽、虽然这样说……\x02",
    )

    CloseMessageWindow()
    OP_A6(0x0)
    OP_44(0xF, 0x2)
    OP_44(0xB, 0x2)
    OP_4A(0x11, 1)
    OP_44(0x11, 0xFF)
    SetChrFlags(0x11, 0x20)
    OP_51(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x11, 19)
    OP_22(0x84, 0x0, 0x64)

    def lambda_F27():
        OP_99(0x11, 0x0, 0x3, 0x7D0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_F27)
    OP_93(0x11, 0xB, 0x258, 0x1B58, 0x0)

    def lambda_F45():
        OP_99(0x11, 0x3, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_F45)
    SetChrChipByIndex(0xB, 5)
    OP_44(0xB, 0xFF)
    TurnDirection(0xB, 0x11, 0)
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x20)
    PlayEffect(0x9, 0xFF, 0xFF, -47540, 1000, 15460, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_FAA():
        OP_94(0x1, 0xB, 0xB4, 0x7D0, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_FAA)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
    OP_51(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x11, 17)
    OP_96(0x11, 0xFFFF43FE, 0x0, 0x3A20, 0x3E8, 0x1388)
    SetChrFlags(0xB, 0x40)

    ChrTalk(
        0x11,
        (
            "他说得没错！\x01",
            "守护关所是我们军人的本分！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "小姑娘，这里不用你们操心！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x11, 400)

    ChrTalk(
        0x101,
        "#003F#2P但、但是……\x02",
    )

    CloseMessageWindow()

    def lambda_1065():
        OP_8E(0xFE, 0xFFFF458E, 0x0, 0x3C96, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_1065)
    OP_51(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x11, 19)
    OP_22(0xC2, 0x0, 0x64)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(70)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(70)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_10E9():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_10E9)
    Sleep(300)

    def lambda_10FC():
        OP_8C(0xFE, 160, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10FC)

    def lambda_110A():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_110A)
    OP_6D(-49790, 450, 10030, 1000)

    ChrTalk(
        0x106,
        "#057F#1P……嘁！\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x106, 0x4)
    OP_8E(0x106, 0xFFFF3C6A, 0x122, 0x2328, 0x1B58, 0x0)
    OP_8E(0x106, 0xFFFF3B7A, 0x1C2, 0x1A9A, 0x1B58, 0x0)
    ClearChrFlags(0x106, 0x4)
    SetChrFlags(0x106, 0x80)

    ChrTalk(
        0x101,
        "#004F#1P又怎么了！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#016F#1P艾丝蒂尔，是对面！\x02\x03",
            "通往卢安那面的出口\x01",
            "好像也受到了魔兽袭击。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F#1P你说什么～！？\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(-49110, -500, -18460, 0)
    OP_6C(315000, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_44(0x11, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0x12, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    ClearChrFlags(0x10, 0x80)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0xA, 0x20)
    ClearChrFlags(0xB, 0x20)
    ClearChrFlags(0xC, 0x20)
    ClearChrFlags(0xD, 0x20)
    ClearChrFlags(0xE, 0x20)
    ClearChrFlags(0xF, 0x20)
    ClearChrFlags(0x10, 0x20)
    SetChrChipByIndex(0xA, 1)
    SetChrChipByIndex(0xB, 1)
    SetChrChipByIndex(0xC, 1)
    SetChrChipByIndex(0xD, 1)
    SetChrChipByIndex(0xE, 1)
    SetChrChipByIndex(0xF, 2)
    SetChrChipByIndex(0x10, 1)
    SetChrPos(0xA, -45460, -500, -20310, 315)
    SetChrPos(0xB, -51540, -300, -17880, 90)
    SetChrPos(0xD, -51890, -500, -20520, 45)
    SetChrPos(0xC, -50260, -500, -20200, 45)
    SetChrPos(0xE, -48980, -500, -20950, 0)
    SetChrPos(0xF, -44270, -300, -18680, 270)
    SetChrPos(0x10, -44460, 0, -17870, 225)
    OP_43(0xA, 0x1, 0x0, 0x2)
    OP_43(0xB, 0x1, 0x0, 0x2)
    OP_43(0xC, 0x1, 0x0, 0x2)
    OP_43(0xD, 0x1, 0x0, 0x2)
    OP_43(0xE, 0x1, 0x0, 0x2)
    OP_43(0xF, 0x1, 0x0, 0x2)
    OP_43(0x10, 0x1, 0x0, 0x2)
    SetChrPos(0x13, -49160, -600, -17710, 180)
    SetChrFlags(0xF, 0x40)
    ClearChrFlags(0x106, 0x80)
    SetChrPos(0x106, -50596, 300, -9470, 0)
    SetChrPos(0x101, -50644, 0, -9440, 180)
    SetChrPos(0x102, -49430, 0, -9440, 180)
    SetChrFlags(0x106, 0x1000)
    SetChrChipByIndex(0x106, 8)

    def lambda_13BA():
        OP_92(0xF, 0x13, 0x8FC, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_13BA)
    OP_0D()
    OP_8E(0x106, 0xFFFF3F84, 0xFFFFFE0C, 0xFFFFBF6E, 0x1770, 0x0)
    SetChrChipByIndex(0x106, 9)
    OP_22(0xA3, 0x0, 0x64)
    SetChrFlags(0x106, 0x20)

    def lambda_13F3():
        OP_99(0x106, 0x0, 0x4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_13F3)

    def lambda_1403():
        OP_96(0x106, 0xFFFF459E, 0xFFFFFE0C, 0xFFFFB442, 0x708, 0xFA0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1403)

    def lambda_1421():
        OP_96(0xF, 0xFFFF402A, 0xFFFFFE0C, 0xFFFFB7E4, 0x7D0, 0x1B58)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1421)

    def lambda_143F():
        OP_6B(2600, 1500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_143F)
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x20)
    Sleep(350)
    SetChrFlags(0xF, 0x4)
    OP_44(0xF, 0xFF)
    OP_4A(0x106, 1)
    Sleep(100)
    OP_4B(0x106, 1)
    PlayEffect(0x9, 0xFF, 0xFF, -47725, 3000, -19196, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F9, 0x0, 0x64)

    def lambda_14B4():
        OP_99(0x106, 0x4, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_14B4)
    SetChrChipByIndex(0xF, 5)
    OP_44(0xF, 0xFF)
    TurnDirection(0xF, 0x106, 0)
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x20)
    OP_8F(0xF, 0xFFFF49DA, 0xFFFFFE0C, 0xFFFFADB2, 0x4E20, 0x0)
    SetChrChipByIndex(0xE, 2)
    SetChrChipByIndex(0x10, 2)
    SetChrChipByIndex(0xA, 2)

    def lambda_1507():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1507)

    def lambda_151D():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_151D)

    def lambda_1533():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1533)
    PlayEffect(0x12, 0xFF, 0xFF, -46630, -500, -21070, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0xF, 0x4)

    def lambda_1583():
        OP_96(0xF, 0xFFFF4C28, 0xFFFFFE0C, 0xFFFFA966, 0x7D0, 0x2710)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1583)
    OP_9F(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x258)
    Sleep(50)
    SetChrChipByIndex(0xB, 2)

    def lambda_15B6():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_15B6)
    Sleep(100)
    SetChrChipByIndex(0xD, 2)

    def lambda_15D6():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_15D6)
    Sleep(100)
    SetChrChipByIndex(0xC, 2)

    def lambda_15F6():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_15F6)
    OP_99(0x106, 0x0, 0x3, 0x7D0)
    OP_96(0x106, 0xFFFF3F58, 0xFFFFFE0C, 0xFFFFB5FA, 0x3E8, 0xFA0)
    SetChrChipByIndex(0x106, 7)
    ClearChrFlags(0x106, 0x20)

    def lambda_1636():
        OP_6C(340000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1636)
    OP_6D(-50734, 0, -10950, 2000)

    ChrTalk(
        0x101,
        "#004F#1P好、好厉害……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F看来他比传说中还要厉害呢。\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6D(-49960, -600, -18520, 0)

    def lambda_16B0():
        OP_6D(-49070, -600, -19300, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_16B0)
    SetChrPos(0x13, -46890, -50, -15230, 180)
    OP_0D()

    def lambda_16DA():

        label("loc_16DA")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_16DA")

    QueueWorkItem2(0xA, 2, lambda_16DA)

    def lambda_16EB():

        label("loc_16EB")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_16EB")

    QueueWorkItem2(0xB, 2, lambda_16EB)

    def lambda_16FC():

        label("loc_16FC")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_16FC")

    QueueWorkItem2(0xC, 2, lambda_16FC)

    def lambda_170D():

        label("loc_170D")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_170D")

    QueueWorkItem2(0xD, 2, lambda_170D)

    def lambda_171E():

        label("loc_171E")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_171E")

    QueueWorkItem2(0xE, 2, lambda_171E)

    def lambda_172F():

        label("loc_172F")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_172F")

    QueueWorkItem2(0x10, 2, lambda_172F)
    SetChrFlags(0x106, 0x40)
    SetChrChipByIndex(0x106, 8)

    def lambda_174A():
        OP_8E(0xFE, 0xFFFF3B84, 0xFFFFFE0C, 0xFFFFB0E6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_174A)

    def lambda_1765():
        OP_96(0xFE, 0xFFFF31E8, 0xFFFFFE0C, 0xFFFFB262, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1765)
    Sleep(100)

    def lambda_1788():
        OP_8F(0xFE, 0xFFFF3576, 0xFFFFFE0C, 0xFFFFAA2E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1788)

    def lambda_17A3():
        OP_96(0xFE, 0xFFFF36D4, 0x0, 0xFFFFC248, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_17A3)
    Sleep(100)

    def lambda_17C6():
        OP_96(0xFE, 0xFFFF4124, 0xFFFFFE0C, 0xFFFFA81C, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_17C6)

    def lambda_17E4():
        OP_96(0xFE, 0xFFFF46B0, 0xFFFFFE0C, 0xFFFFB3AC, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_17E4)

    def lambda_1802():
        OP_8F(0xFE, 0xFFFF4606, 0xFFFFFE0C, 0xFFFFAEE8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1802)
    WaitChrThread(0x106, 0x1)
    SetChrChipByIndex(0x106, 7)
    OP_43(0x106, 0x1, 0x0, 0x2)
    WaitChrThread(0xC, 0x1)
    WaitChrThread(0xD, 0x1)
    WaitChrThread(0xE, 0x1)
    WaitChrThread(0x10, 0x1)
    TurnDirection(0x106, 0x10, 600)
    SetChrFlags(0x106, 0x40)
    SetChrChipByIndex(0x106, 8)

    def lambda_1853():
        OP_96(0xFE, 0xFFFF4304, 0xFFFFFDA8, 0xFFFFB1AE, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1853)

    def lambda_1871():
        OP_96(0xFE, 0xFFFF4B4C, 0xFFFFFE0C, 0xFFFFB442, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1871)
    Sleep(100)

    def lambda_1894():
        OP_8F(0xFE, 0xFFFF4E6C, 0xFFFFFE0C, 0xFFFFAD30, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1894)

    def lambda_18AF():
        OP_96(0xFE, 0xFFFF367A, 0xFFFFFED4, 0xFFFFB85C, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_18AF)

    def lambda_18CD():
        OP_8F(0xFE, 0xFFFF3A58, 0xFFFFFE0C, 0xFFFFAECA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_18CD)
    WaitChrThread(0x106, 0x1)
    SetChrChipByIndex(0x106, 7)
    WaitChrThread(0xC, 0x1)
    WaitChrThread(0xD, 0x1)
    WaitChrThread(0xE, 0x1)
    WaitChrThread(0x10, 0x1)

    def lambda_1906():
        OP_92(0xFE, 0x106, 0xBB8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1906)

    def lambda_191B():
        OP_92(0xFE, 0x106, 0xBB8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_191B)

    def lambda_1930():
        OP_96(0xFE, 0xFFFF4084, 0xFFFFFED4, 0xFFFFC112, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1930)
    Sleep(150)

    def lambda_1953():
        OP_92(0xFE, 0x106, 0xDAC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1953)
    Sleep(150)

    def lambda_196D():
        OP_92(0xFE, 0x106, 0xDAC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_196D)
    Sleep(150)

    def lambda_1987():
        OP_92(0xFE, 0x106, 0xBB8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1987)
    WaitChrThread(0xA, 0x1)
    WaitChrThread(0xB, 0x1)
    WaitChrThread(0xC, 0x1)
    WaitChrThread(0xD, 0x1)
    WaitChrThread(0xE, 0x1)
    WaitChrThread(0x10, 0x1)

    def lambda_19BA():
        OP_94(0x1, 0xFE, 0x64, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_19BA)
    Sleep(200)

    def lambda_19D5():
        OP_94(0x1, 0xFE, 0x64, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_19D5)
    Sleep(100)

    def lambda_19F0():
        OP_94(0x1, 0xFE, 0x64, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_19F0)

    def lambda_1A06():
        OP_94(0x1, 0xFE, 0x64, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1A06)
    Sleep(100)

    def lambda_1A21():
        OP_94(0x1, 0xFE, 0x64, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1A21)
    Sleep(200)

    def lambda_1A3C():
        OP_94(0x1, 0xFE, 0x64, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1A3C)
    Sleep(100)

    def lambda_1A57():
        OP_94(0x1, 0xFE, 0x5A, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1A57)

    def lambda_1A6D():
        OP_94(0x1, 0xFE, 0x5A, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1A6D)
    Sleep(100)

    def lambda_1A88():
        OP_94(0x1, 0xFE, 0x5A, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1A88)
    Sleep(200)

    def lambda_1AA3():
        OP_94(0x1, 0xFE, 0x5A, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1AA3)
    Sleep(100)

    def lambda_1ABE():
        OP_94(0x1, 0xFE, 0x5A, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1ABE)
    Sleep(200)

    def lambda_1AD9():
        OP_94(0x1, 0xFE, 0x5A, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1AD9)
    OP_8C(0x106, 135, 400)

    ChrTalk(
        0x106,
        (
            "#051F哈～想夹击我吗？\x02\x03",
            "一群光使蛮劲的野狗，\x01",
            "偶尔也会动动脑筋嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "……我们来帮忙了！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x102, 12)
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x102, 0x1000)

    def lambda_1B68():
        OP_8E(0x101, 0xFFFF4426, 0xFFFFFED4, 0xFFFFBF32, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B68)
    Sleep(300)

    def lambda_1B88():
        OP_8E(0x102, 0xFFFF4426, 0xFFFFFED4, 0xFFFFBF32, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1B88)
    WaitChrThread(0x101, 0x1)

    def lambda_1BA8():
        OP_96(0x101, 0xFFFF3F9E, 0xFFFFFD80, 0xFFFFB3D4, 0x3E8, 0x2710)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1BA8)
    WaitChrThread(0x102, 0x1)

    def lambda_1BCB():
        OP_96(0x102, 0xFFFF4372, 0xFFFFFE0C, 0xFFFFB5FA, 0x3E8, 0x2710)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1BCB)

    def lambda_1BE9():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1BE9)
    Sleep(100)

    def lambda_1C04():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1C04)

    def lambda_1C1A():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1C1A)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_1C3A():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C3A)
    Sleep(50)

    def lambda_1C4D():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1C4D)

    def lambda_1C63():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1C63)
    Sleep(100)

    def lambda_1C7E():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1C7E)
    WaitChrThread(0x102, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_1C9E():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1C9E)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x106,
        "#054F喂！谁叫你们过来的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嘿嘿～～\x01",
            "我们想过来就过来的啦☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F我们不会给你添麻烦的，\x01",
            "让我们和你一起并肩作战吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#053F哼，随你们吧……\x02\x03",
            "#054F不过你们要注意了，\x01",
            "我的『重剑』可是不长眼的！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1D9C():
        OP_94(0x1, 0xFE, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1D9C)

    def lambda_1DB2():
        OP_94(0x1, 0xFE, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1DB2)
    Sleep(100)

    def lambda_1DCD():
        OP_94(0x1, 0xFE, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1DCD)
    Sleep(50)

    def lambda_1DE8():
        OP_94(0x1, 0xFE, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1DE8)

    def lambda_1DFE():
        OP_94(0x1, 0xFE, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1DFE)
    Sleep(100)

    def lambda_1E19():
        OP_94(0x1, 0xFE, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1E19)
    Sleep(200)
    Battle(0x396, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_1E47"),
        (SWITCH_DEFAULT, "loc_1E4A"),
    )


    label("loc_1E47")

    OP_B4(0x0)
    Return()

    label("loc_1E4A")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    OP_31(0x5, 0x0, 0x18)
    OP_41(0x5, 0xF3)
    OP_41(0x5, 0x111)
    OP_6B(3000, 0)
    SetChrPos(0x101, -49970, -650, -18800, 315)
    SetChrPos(0x102, -47880, -430, -19000, 45)
    SetChrPos(0x106, -48850, -540, -20000, 180)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x106, 0xFF)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x106, 15)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)

    ChrTalk(
        0x101,
        (
            "#501F呼……\x01",
            "终于击败它们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F嗯，它们数目众多，\x01",
            "而且都是很难缠的魔兽。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#050F……………………………\x02\x03",
            "#053F哼……\x01",
            "看来你们也没有想象中那么没用。\x02\x03",
            "毕竟是继承了大叔的真传，\x01",
            "这点水平还是应该有的。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1FBB():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1FBB)
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(
        0x101,
        "#004F啊。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x106, 0, 400)

    ChrTalk(
        0x106,
        (
            "#050F别搞错了。\x01",
            "你们始终还是新人。\x02\x03",
            "离正游击士还差得远啦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x11, 6)
    SetChrChipByIndex(0x12, 14)
    SetChrPos(0x11, -50620, 450, -7940, 0)
    SetChrPos(0x12, -49390, 450, -8010, 0)
    ClearChrFlags(0x11, 0x20)
    ClearChrFlags(0x12, 0x20)

    ChrTalk(
        0x11,
        (
            "喂——！\x01",
            "你们那边没事吧！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_207D():
        OP_6D(-49756, -300, -16490, 2000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_207D)

    def lambda_2095():
        OP_8E(0xFE, 0xFFFF3B7A, 0x0, 0xFFFFC630, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2095)
    Sleep(500)

    def lambda_20B5():
        OP_8E(0xFE, 0xFFFF3F9E, 0x0, 0xFFFFC824, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_20B5)

    def lambda_20D0():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_20D0)

    def lambda_20DE():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_20DE)

    def lambda_20EC():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_20EC)
    WaitChrThread(0x11, 0x1)

    ChrTalk(
        0x106,
        (
            "#050F#3P啊，没问题。\x01",
            "把它们杀个片甲不留了。\x02\x03",
            "刚才那个晕倒的士兵怎样了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "还好没什么大碍。\x01",
            "这次幸好有你在这里帮了大忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "真不愧是『重剑阿加特』啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#053F#3P也没什么大不了的。\x02\x03",
            "#053F而且……\x01",
            "这两个小鬼也帮了我不少忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "是这样啊……\x01",
            "小姑娘，太谢谢你们啦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊，嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "为了安全起见，\x01",
            "我们还要继续在这周围巡逻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "你们大概都有点累了，\x01",
            "回到休息室好好睡一觉吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#051F啊啊，你们也小心点。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 45, 400)

    def lambda_22AF():
        OP_8E(0xFE, 0xFFFF3C60, 0x1C2, 0xFFFFE2B4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_22AF)
    Sleep(500)
    OP_8C(0x12, 45, 400)

    def lambda_22D6():
        OP_8E(0xFE, 0xFFFF3C60, 0x1C2, 0xFFFFE2B4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_22D6)
    WaitChrThread(0x11, 0x1)
    SetChrFlags(0x11, 0x80)
    WaitChrThread(0x12, 0x1)
    SetChrFlags(0x12, 0x80)

    def lambda_2305():

        label("loc_2305")

        TurnDirection(0xFE, 0x106, 400)
        OP_48()
        Jump("loc_2305")

    QueueWorkItem2(0x101, 1, lambda_2305)

    def lambda_2316():

        label("loc_2316")

        TurnDirection(0xFE, 0x106, 400)
        OP_48()
        Jump("loc_2316")

    QueueWorkItem2(0x102, 1, lambda_2316)
    OP_6D(-49340, -600, -17500, 1000)

    ChrTalk(
        0x106,
        (
            "#050F我要回去接着睡了。\x02\x03",
            "危险已经排除了，\x01",
            "你们也快点回去睡觉吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_8E(0x106, 0xFFFF3C60, 0x1C2, 0xFFFFE2B4, 0xBB8, 0x0)
    SetChrFlags(0x106, 0x80)
    OP_63(0x101)
    OP_63(0x102)
    OP_44(0x101, 0x1)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#004F怎、怎么回事？\x02\x03",
            "那个刀子嘴\x01",
            "这次竟然表扬我们呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x102, 0x1)
    TurnDirection(0x102, 0x101, 300)

    ChrTalk(
        0x102,
        (
            "#010F也许，他或多或少\x01",
            "开始承认我们两个的能力了吧。\x02\x03",
            "其实他也不是那种不近人情的人，\x01",
            "只不过是性格比较直率而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F呼……\x01",
            "其实是率直过头了吧。\x02\x03",
            "#006F……不过话说回来，\x01",
            "那家伙也有相当可爱的一面。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_21()
    OP_22(0xD, 0x0, 0x64)
    SetMapFlags(0x100000)
    Sleep(3000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T1310   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_B0A end

    def Function_5_2505(): pass

    label("Function_5_2505")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_274E")
    OP_93(0x9, 0xA, 0x258, 0x1388, 0x0)
    OP_94(0x1, 0xA, 0xB4, 0x3E8, 0x1388, 0x0)

    def lambda_2531():
        OP_8F(0xFE, 0xFFFF4DE0, 0x0, 0x37F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2531)

    def lambda_254C():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_254C)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0xA, 0xFFFF4674, 0x0, 0x353E, 0x7D0, 0x1770)
    TurnDirection(0xA, 0x9, 0)
    TurnDirection(0x9, 0xA, 800)
    Sleep(1000)

    def lambda_2589():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2589)

    def lambda_259F():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_259F)
    WaitChrThread(0x9, 0x2)
    WaitChrThread(0xA, 0x2)
    Sleep(700)
    SetChrChipByIndex(0xA, 2)

    def lambda_25C9():
        OP_94(0x1, 0xFE, 0x0, 0x640, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_25C9)

    def lambda_25DF():
        OP_94(0x1, 0xFE, 0x0, 0x640, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_25DF)
    WaitChrThread(0x9, 0x2)
    WaitChrThread(0xA, 0x2)
    OP_22(0x22B, 0x0, 0x64)
    SetChrChipByIndex(0xA, 1)

    def lambda_2609():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2609)

    def lambda_261F():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_261F)
    Sleep(600)

    def lambda_263A():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_263A)

    def lambda_2650():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2650)
    Sleep(200)

    def lambda_266B():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_266B)

    def lambda_2681():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2681)
    Sleep(200)

    def lambda_269C():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_269C)

    def lambda_26B2():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_26B2)
    Sleep(200)

    def lambda_26CD():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_26CD)

    def lambda_26E3():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_26E3)
    Sleep(200)

    def lambda_26FE():
        OP_8F(0xFE, 0xFFFF4674, 0x0, 0x353E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_26FE)

    def lambda_2719():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2719)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0xA, 0xFFFF4DE0, 0x0, 0x37F0, 0x7D0, 0x1770)
    TurnDirection(0xA, 0x9, 0)
    TurnDirection(0x9, 0xA, 800)
    Jump("Function_5_2505")

    label("loc_274E")

    Return()

    # Function_5_2505 end

    def Function_6_274F(): pass

    label("Function_6_274F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A63")
    SetChrFlags(0x11, 0x20)
    OP_51(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x11, 19)

    def lambda_2773():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2773)

    def lambda_2789():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2789)
    Sleep(200)

    def lambda_27A4():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_27A4)

    def lambda_27BA():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_27BA)
    Sleep(200)

    def lambda_27D5():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_27D5)

    def lambda_27EB():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_27EB)
    Sleep(200)

    def lambda_2806():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2806)

    def lambda_281C():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_281C)
    Sleep(200)

    def lambda_2837():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2837)

    def lambda_284D():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_284D)
    Sleep(200)

    def lambda_2868():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2868)

    def lambda_287E():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_287E)
    Sleep(200)

    def lambda_2899():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2899)

    def lambda_28AF():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_28AF)
    Sleep(500)
    OP_A3(0x0)
    SetChrChipByIndex(0xF, 2)

    def lambda_28D2():
        OP_94(0x1, 0xFE, 0x0, 0x5DC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_28D2)
    Sleep(500)
    WaitChrThread(0xF, 0x2)

    def lambda_28F2():
        OP_96(0xFE, 0xFFFF4F84, 0x0, 0x4326, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_28F2)
    OP_44(0xF, 0x1)
    OP_44(0xB, 0x1)
    OP_99(0x11, 0x1, 0x3, 0xBB8)
    SetChrChipByIndex(0xB, 5)
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x20)
    OP_22(0x1F5, 0x0, 0x64)

    def lambda_293B():
        OP_99(0x11, 0x3, 0x7, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_293B)

    def lambda_294B():
        OP_8F(0xFE, 0xFFFF43FE, 0x0, 0x3A20, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_294B)

    def lambda_2966():
        OP_8F(0xFE, 0xFFFF5146, 0x0, 0x4C40, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2966)
    WaitChrThread(0xF, 0x2)

    def lambda_2986():
        OP_96(0xFE, 0xFFFF4674, 0x0, 0x3D04, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_2986)
    WaitChrThread(0xB, 0x2)
    SetChrChipByIndex(0xB, 1)
    WaitChrThread(0xF, 0x2)
    SetChrChipByIndex(0xF, 1)
    SetChrPos(0xB, -47500, 0, 15620, 225)
    SetChrPos(0xF, -44730, 0, 19520, 225)

    def lambda_29DA():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_29DA)
    OP_51(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x11, 19)
    OP_94(0x1, 0x11, 0xB4, 0x1F4, 0x1770, 0x0)
    OP_51(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x11, 17)
    OP_43(0xB, 0x1, 0x0, 0x2)
    OP_43(0xF, 0x1, 0x0, 0x2)
    OP_A2(0x0)
    OP_43(0x11, 0x2, 0x0, 0x2)
    Sleep(500)
    Sleep(1000)

    def lambda_2A41():
        OP_94(0x1, 0xFE, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2A41)
    OP_94(0x1, 0x11, 0x0, 0x1F4, 0xFA0, 0x0)
    Jump("Function_6_274F")

    label("loc_2A63")

    Return()

    # Function_6_274F end

    def Function_7_2A64(): pass

    label("Function_7_2A64")

    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xE, 0x40)
    SetChrFlags(0x12, 0x40)

    def lambda_2A7E():

        label("loc_2A7E")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_2A7E")

    QueueWorkItem2(0x8, 0, lambda_2A7E)

    def lambda_2A8F():

        label("loc_2A8F")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2A8F")

    QueueWorkItem2(0xE, 0, lambda_2A8F)

    label("loc_2A9A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E11")
    OP_22(0x227, 0x0, 0x64)

    def lambda_2AAE():
        OP_93(0xFE, 0x8, 0x258, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_2AAE)

    def lambda_2AC3():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2AC3)
    SetChrChipByIndex(0xD, 2)
    OP_93(0xD, 0x12, 0x258, 0x1770, 0x0)
    SetChrChipByIndex(0xD, 1)
    OP_94(0x1, 0x12, 0xB4, 0x1F4, 0x1388, 0x0)
    Sleep(200)
    OP_94(0x1, 0x12, 0x0, 0x1F4, 0x1388, 0x0)

    def lambda_2B14():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2B14)

    def lambda_2B2A():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_2B2A)

    def lambda_2B40():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2B40)

    def lambda_2B56():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2B56)
    Sleep(500)

    def lambda_2B71():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2B71)

    def lambda_2B87():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2B87)
    Sleep(500)

    def lambda_2BA2():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2BA2)

    def lambda_2BB8():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2BB8)
    Sleep(500)
    OP_44(0x8, 0x2)

    def lambda_2BD7():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_2BD7)
    OP_22(0xCB, 0x0, 0x64)
    OP_96(0x8, 0xFFFF3B20, 0x0, 0x40D8, 0x258, 0x1770)
    WaitChrThread(0xC, 0x2)

    def lambda_2C0E():
        OP_94(0x1, 0xFE, 0xB4, 0x7D0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2C0E)

    def lambda_2C24():
        OP_92(0xFE, 0x8, 0x12C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_2C24)
    Sleep(150)
    OP_96(0x8, 0xFFFF347C, 0x0, 0x4236, 0x3E8, 0x1770)
    OP_22(0xCB, 0x0, 0x64)

    def lambda_2C5A():
        TurnDirection(0xFE, 0xE, 800)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2C5A)
    TurnDirection(0xE, 0x8, 800)
    OP_92(0x8, 0xE, 0x258, 0x1388, 0x0)
    OP_22(0x227, 0x0, 0x64)
    OP_94(0x1, 0xE, 0xB4, 0x3E8, 0x1388, 0x0)
    WaitChrThread(0x8, 0x2)
    WaitChrThread(0xE, 0x2)

    def lambda_2C9B():
        OP_8F(0xFE, 0xFFFF3490, 0x0, 0x3C78, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2C9B)

    def lambda_2CB6():
        OP_8E(0xFE, 0xFFFF3706, 0x0, 0x4268, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_2CB6)

    def lambda_2CD1():
        OP_93(0xFE, 0x12, 0x9C4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2CD1)
    SetChrChipByIndex(0xC, 2)
    Sleep(1700)

    def lambda_2CF0():
        OP_93(0xFE, 0x12, 0x258, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2CF0)
    OP_22(0x22A, 0x0, 0x64)
    OP_44(0xD, 0x1)
    SetChrChipByIndex(0xD, 5)
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xD, 0x20)

    def lambda_2D23():
        OP_8F(0xFE, 0xFFFF4494, 0x0, 0x470E, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2D23)

    def lambda_2D3E():
        OP_94(0x1, 0xFE, 0x0, 0x1F4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2D3E)

    def lambda_2D54():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2D54)

    def lambda_2D6A():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_2D6A)
    WaitChrThread(0xD, 0x2)
    SetChrChipByIndex(0xD, 1)
    ClearChrFlags(0xD, 0x20)
    OP_43(0xD, 0x1, 0x0, 0x2)
    WaitChrThread(0xC, 0x2)
    OP_22(0x22B, 0x0, 0x64)
    OP_44(0xC, 0x1)
    SetChrChipByIndex(0xC, 5)
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x20)

    def lambda_2DB9():
        OP_8F(0xFE, 0xFFFF3B34, 0x0, 0x48F8, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2DB9)

    def lambda_2DD4():
        OP_8F(0xFE, 0xFFFF3DBE, 0x0, 0x3BEC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2DD4)
    WaitChrThread(0xC, 0x2)
    SetChrChipByIndex(0xC, 1)
    ClearChrFlags(0xC, 0x20)
    OP_43(0xC, 0x1, 0x0, 0x2)
    WaitChrThread(0x12, 0x2)
    WaitChrThread(0xC, 0x2)
    WaitChrThread(0xD, 0x2)
    Jump("loc_2A9A")

    label("loc_2E11")

    Return()

    # Function_7_2A64 end

    SaveToFile()

Try(main)
