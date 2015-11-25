from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4303   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4303.x',
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
        '特务兵',                               # 9
        '特务兵',                               # 10
        '特务兵',                               # 11
        '军用犬',                               # 12
        '军用犬',                               # 13
        '军用犬',                               # 14
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
        'ED6_DT07/CH00100 ._CH',             # 00
        'ED6_DT07/CH00101 ._CH',             # 01
        'ED6_DT07/CH00110 ._CH',             # 02
        'ED6_DT07/CH00111 ._CH',             # 03
        'ED6_DT07/CH00170 ._CH',             # 04
        'ED6_DT07/CH00171 ._CH',             # 05
        'ED6_DT07/CH00340 ._CH',             # 06
        'ED6_DT07/CH00341 ._CH',             # 07
        'ED6_DT09/CH10060 ._CH',             # 08
        'ED6_DT09/CH10061 ._CH',             # 09
        'ED6_DT06/CH20042 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH00100P._CP',             # 00
        'ED6_DT07/CH00101P._CP',             # 01
        'ED6_DT07/CH00110P._CP',             # 02
        'ED6_DT07/CH00111P._CP',             # 03
        'ED6_DT07/CH00170P._CP',             # 04
        'ED6_DT07/CH00171P._CP',             # 05
        'ED6_DT07/CH00340P._CP',             # 06
        'ED6_DT07/CH00341P._CP',             # 07
        'ED6_DT09/CH10060P._CP',             # 08
        'ED6_DT09/CH10061P._CP',             # 09
        'ED6_DT06/CH20042P._CP',             # 0A
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_1C2",          # 00, 0
        "Function_1_262",          # 01, 1
        "Function_2_275",          # 02, 2
        "Function_3_646",          # 03, 3
        "Function_4_A28",          # 04, 4
        "Function_5_BCA",          # 05, 5
        "Function_6_D6C",          # 06, 6
        "Function_7_F0E",          # 07, 7
        "Function_8_10B0",         # 08, 8
        "Function_9_1252",         # 09, 9
        "Function_10_13F4",        # 0A, 10
        "Function_11_1596",        # 0B, 11
        "Function_12_1738",        # 0C, 12
    )


    def Function_0_1C2(): pass

    label("Function_0_1C2")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_1F6"),
        (100, "loc_20C"),
        (102, "loc_222"),
        (103, "loc_229"),
        (104, "loc_230"),
        (105, "loc_237"),
        (106, "loc_23E"),
        (107, "loc_245"),
        (108, "loc_24C"),
        (109, "loc_253"),
        (110, "loc_25A"),
        (SWITCH_DEFAULT, "loc_261"),
    )


    label("loc_1F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_209")
    OP_A2(0x653)
    Event(0, 2)

    label("loc_209")

    Jump("loc_261")

    label("loc_20C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21F")
    OP_A2(0x653)
    Event(0, 3)

    label("loc_21F")

    Jump("loc_261")

    label("loc_222")

    Event(0, 12)
    Jump("loc_261")

    label("loc_229")

    Event(0, 11)
    Jump("loc_261")

    label("loc_230")

    Event(0, 10)
    Jump("loc_261")

    label("loc_237")

    Event(0, 9)
    Jump("loc_261")

    label("loc_23E")

    Event(0, 8)
    Jump("loc_261")

    label("loc_245")

    Event(0, 7)
    Jump("loc_261")

    label("loc_24C")

    Event(0, 6)
    Jump("loc_261")

    label("loc_253")

    Event(0, 5)
    Jump("loc_261")

    label("loc_25A")

    Event(0, 4)
    Jump("loc_261")

    label("loc_261")

    Return()

    # Function_0_1C2 end

    def Function_1_262(): pass

    label("Function_1_262")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE4A80, 0x30062)
    Return()

    # Function_1_262 end

    def Function_2_275(): pass

    label("Function_2_275")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    SetChrPos(0x101, 16560, 1000, -8020, 87)
    SetChrPos(0x102, 15530, 1000, -8910, 135)
    SetChrPos(0x108, 15490, 1000, -6910, 45)
    OP_6D(15530, 1000, -7950, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x8, 18910, 1000, 720, 180)
    SetChrPos(0x9, 18910, 1000, 3690, 180)
    SetChrPos(0xB, 18130, 1000, 2540, 180)
    SetChrPos(0xC, 19750, 1000, 2310, 180)

    ChrTalk(
        0x8,
        "你……你们是什么人！？\x02",
    )

    CloseMessageWindow()

    def lambda_344():
        OP_6D(18540, 1000, -4090, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_344)

    def lambda_35C():
        OP_6C(0, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_35C)

    def lambda_36C():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_36C)

    def lambda_387():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_387)

    def lambda_3A2():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3A2)

    def lambda_3BD():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3BD)

    def lambda_3D8():
        TurnDirection(0xFE, 0x8, 800)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3D8)

    def lambda_3E6():
        TurnDirection(0xFE, 0x8, 800)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3E6)

    def lambda_3F4():
        TurnDirection(0xFE, 0x8, 800)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_3F4)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0x9, 0x1)

    ChrTalk(
        0x9,
        "可疑的人，在那儿不许动！\x02",
    )

    CloseMessageWindow()

    def lambda_46A():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_46A)

    def lambda_47F():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_47F)

    def lambda_494():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_494)

    def lambda_4A9():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_4A9)
    Sleep(500)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    Battle(0x3AB, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_4E6"),
        (SWITCH_DEFAULT, "loc_4E9"),
    )


    label("loc_4E6")

    OP_B4(0x0)
    Return()

    label("loc_4E9")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    SetChrPos(0x101, 17040, 1000, -5470, 19)
    SetChrPos(0x102, 16580, 1000, -3860, 45)
    SetChrPos(0x108, 18690, 1000, -6040, 11)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 10)
    SetChrChipByIndex(0x9, 10)
    SetChrChipByIndex(0xA, 10)
    SetChrPos(0x8, 19930, 1000, -3920, 190)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    OP_6D(17470, 1000, -4720, 0)
    OP_6C(315000, 1000)

    ChrTalk(
        0x101,
        (
            "#000F呼～解决了。\x01",
            "冷不妨就跳出几个人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F还有相当数量的特务兵\x01",
            "残留在离宫里面。\x02\x03",
            "好像定期在中庭\x01",
            "的走廊巡逻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F没办法，若是被发现了\x01",
            "就只有让他们保持沉默了。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_2_275 end

    def Function_3_646(): pass

    label("Function_3_646")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    SetChrPos(0x101, -16350, 1000, -7540, 301)
    SetChrPos(0x102, -16410, 1000, -8720, 243)
    SetChrPos(0x108, -15040, 1000, -8100, 302)
    OP_6D(-15730, 1000, -8020, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x8, -19240, 1000, -50, 188)
    SetChrPos(0x9, -19280, 1000, 2470, 180)
    SetChrPos(0xB, -20160, 1000, 960, 180)
    SetChrPos(0xC, -18110, 1000, 970, 180)

    ChrTalk(
        0x8,
        "你……你们是什么人！？\x02",
    )

    CloseMessageWindow()

    def lambda_715():
        OP_6D(-19130, 1000, -4630, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_715)

    def lambda_72D():
        OP_6C(0, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_72D)

    def lambda_73D():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_73D)

    def lambda_758():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_758)

    def lambda_773():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_773)

    def lambda_78E():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_78E)

    def lambda_7A9():
        TurnDirection(0xFE, 0x8, 800)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7A9)

    def lambda_7B7():
        TurnDirection(0xFE, 0x8, 800)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7B7)

    def lambda_7C5():
        TurnDirection(0xFE, 0x8, 800)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_7C5)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0x9, 0x1)

    ChrTalk(
        0x9,
        "可疑的人，在那儿不许动！\x02",
    )

    CloseMessageWindow()

    def lambda_83B():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_83B)

    def lambda_850():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_850)

    def lambda_865():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_865)

    def lambda_87A():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_87A)
    Sleep(500)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    Battle(0x3AC, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_8B7"),
        (SWITCH_DEFAULT, "loc_8BA"),
    )


    label("loc_8B7")

    OP_B4(0x0)
    Return()

    label("loc_8BA")

    EventBegin(0x0)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 10)
    SetChrChipByIndex(0x9, 10)
    SetChrChipByIndex(0xA, 10)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    SetChrPos(0x101, -18900, 1000, -6950, 14)
    SetChrPos(0x102, -17970, 1000, -6160, 345)
    SetChrPos(0x108, -20110, 1000, -5730, 45)
    SetChrPos(0x8, -17200, 1000, -3390, 270)
    SetChrPos(0x9, -18660, 1000, -3640, 270)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    OP_6D(-18490, 1000, -4850, 0)
    OP_6C(45000, 0)

    ChrTalk(
        0x101,
        (
            "#000F呼～解决了。\x01",
            "冷不妨就跳出几个人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F还有相当数量的特务兵\x01",
            "残留在离宫里面。\x02\x03",
            "好像定期在中庭\x01",
            "的走廊巡逻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F没办法，若是被发现了\x01",
            "就只有让他们保持沉默了。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_3_646 end

    def Function_4_A28(): pass

    label("Function_4_A28")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3A")
    Return()

    label("loc_A3A")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    SetChrPos(0x101, 19940, 1000, 6790, 294)
    SetChrPos(0x102, 21170, 1000, 6410, 326)
    SetChrPos(0x108, 21290, 1000, 7450, 303)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, 19310, 1000, 13490, 173)
    SetChrPos(0x9, 20360, 1000, 15020, 170)
    SetChrPos(0xA, 18980, 1000, 14690, 186)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_6D(19290, 1000, 10760, 1000)

    def lambda_B1C():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B1C)

    def lambda_B31():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B31)

    def lambda_B46():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B46)

    def lambda_B5B():
        OP_69(0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_B5B)
    Sleep(800)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x2BD, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 10)
    SetChrChipByIndex(0x9, 10)
    SetChrChipByIndex(0xA, 10)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    Sleep(500)
    EventEnd(0x0)
    Return()

    # Function_4_A28 end

    def Function_5_BCA(): pass

    label("Function_5_BCA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BDC")
    Return()

    label("loc_BDC")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    SetChrPos(0x101, 20250, 1000, 21120, 295)
    SetChrPos(0x102, 20800, 1000, 20430, 2)
    SetChrPos(0x108, 20970, 1000, 21870, 149)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, 19240, 1000, 31840, 174)
    SetChrPos(0x9, 20580, 1000, 32970, 194)
    SetChrPos(0xA, 18940, 1000, 32770, 160)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_6D(19670, 1000, 32770, 1000)

    def lambda_CBE():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_CBE)

    def lambda_CD3():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_CD3)

    def lambda_CE8():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_CE8)

    def lambda_CFD():
        OP_69(0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_CFD)
    Sleep(800)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x2BD, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 10)
    SetChrChipByIndex(0x9, 10)
    SetChrChipByIndex(0xA, 10)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    Sleep(500)
    EventEnd(0x0)
    Return()

    # Function_5_BCA end

    def Function_6_D6C(): pass

    label("Function_6_D6C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D7E")
    Return()

    label("loc_D7E")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    SetChrPos(0x101, 20270, 1000, 32830, 270)
    SetChrPos(0x102, 21030, 1000, 32090, 267)
    SetChrPos(0x108, 21160, 1000, 33550, 274)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, 12630, 1000, 35570, 101)
    SetChrPos(0x9, 11450, 1000, 36350, 97)
    SetChrPos(0xA, 11530, 1000, 34890, 88)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_6D(12350, 1000, 35970, 1000)

    def lambda_E60():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E60)

    def lambda_E75():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_E75)

    def lambda_E8A():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_E8A)

    def lambda_E9F():
        OP_69(0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_E9F)
    Sleep(800)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x2BD, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 10)
    SetChrChipByIndex(0x9, 10)
    SetChrChipByIndex(0xA, 10)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    Sleep(500)
    EventEnd(0x0)
    Return()

    # Function_6_D6C end

    def Function_7_F0E(): pass

    label("Function_7_F0E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F20")
    Return()

    label("loc_F20")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    SetChrPos(0x101, 9090, 1000, 36810, 270)
    SetChrPos(0x102, 9630, 1000, 37440, 270)
    SetChrPos(0x108, 8380, 1000, 36730, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, 400, 1000, 35050, 88)
    SetChrPos(0x9, -330, 1000, 36110, 103)
    SetChrPos(0xA, -640, 1000, 34500, 78)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_6D(490, 1000, 35070, 1000)

    def lambda_1002():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1002)

    def lambda_1017():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1017)

    def lambda_102C():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_102C)

    def lambda_1041():
        OP_69(0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1041)
    Sleep(800)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x2BD, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 10)
    SetChrChipByIndex(0x9, 10)
    SetChrChipByIndex(0xA, 10)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    Sleep(500)
    EventEnd(0x0)
    Return()

    # Function_7_F0E end

    def Function_8_10B0(): pass

    label("Function_8_10B0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10C2")
    Return()

    label("loc_10C2")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    SetChrPos(0x101, -180, 1000, 40300, 186)
    SetChrPos(0x102, 840, 1000, 40700, 166)
    SetChrPos(0x108, -890, 1000, 40810, 198)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, 150, 250, 29590, 351)
    SetChrPos(0x9, -440, 500, 30500, 356)
    SetChrPos(0xA, 940, 500, 30620, 341)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_6D(150, 250, 29590, 1000)

    def lambda_11A4():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_11A4)

    def lambda_11B9():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_11B9)

    def lambda_11CE():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_11CE)

    def lambda_11E3():
        OP_69(0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_11E3)
    Sleep(800)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x2BD, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 10)
    SetChrChipByIndex(0x9, 10)
    SetChrChipByIndex(0xA, 10)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    Sleep(500)
    EventEnd(0x0)
    Return()

    # Function_8_10B0 end

    def Function_9_1252(): pass

    label("Function_9_1252")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1264")
    Return()

    label("loc_1264")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    SetChrPos(0x101, -8960, 1000, 36360, 83)
    SetChrPos(0x102, -9650, 1000, 36960, 83)
    SetChrPos(0x108, -7870, 1000, 36840, 87)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, 1650, 1000, 34820, 248)
    SetChrPos(0x9, 2640, 1000, 35540, 277)
    SetChrPos(0xA, 2540, 1000, 34230, 260)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_6D(1650, 1000, 34820, 1000)

    def lambda_1346():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1346)

    def lambda_135B():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_135B)

    def lambda_1370():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1370)

    def lambda_1385():
        OP_69(0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1385)
    Sleep(800)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x2BD, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 10)
    SetChrChipByIndex(0x9, 10)
    SetChrChipByIndex(0xA, 10)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    Sleep(500)
    EventEnd(0x0)
    Return()

    # Function_9_1252 end

    def Function_10_13F4(): pass

    label("Function_10_13F4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1406")
    Return()

    label("loc_1406")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    SetChrPos(0x101, -20560, 1000, 29250, 23)
    SetChrPos(0x102, -21000, 1000, 28080, 60)
    SetChrPos(0x108, -21470, 1000, 29440, 52)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, -16129, 1000, 34890, 224)
    SetChrPos(0x9, -16560, 1000, 36340, 211)
    SetChrPos(0xA, -17730, 1000, 36360, 209)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_6D(-16560, 1000, 36340, 1000)

    def lambda_14E8():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_14E8)

    def lambda_14FD():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_14FD)

    def lambda_1512():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1512)

    def lambda_1527():
        OP_69(0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1527)
    Sleep(800)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x2BD, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 10)
    SetChrChipByIndex(0x9, 10)
    SetChrChipByIndex(0xA, 10)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    Sleep(500)
    EventEnd(0x0)
    Return()

    # Function_10_13F4 end

    def Function_11_1596(): pass

    label("Function_11_1596")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15A8")
    Return()

    label("loc_15A8")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    SetChrPos(0x101, -20250, 1000, 20460, 144)
    SetChrPos(0x102, -21290, 1000, 20210, 133)
    SetChrPos(0x108, -20770, 1000, 21590, 119)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, -16300, 1000, 16040, 316)
    SetChrPos(0x9, -15870, 750, 15030, 297)
    SetChrPos(0xA, -15260, 750, 16170, 306)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_6D(-16300, 1000, 16040, 1000)

    def lambda_168A():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_168A)

    def lambda_169F():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_169F)

    def lambda_16B4():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_16B4)

    def lambda_16C9():
        OP_69(0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_16C9)
    Sleep(800)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x2BD, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 10)
    SetChrChipByIndex(0x9, 10)
    SetChrChipByIndex(0xA, 10)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    Sleep(500)
    EventEnd(0x0)
    Return()

    # Function_11_1596 end

    def Function_12_1738(): pass

    label("Function_12_1738")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_174A")
    Return()

    label("loc_174A")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    SetChrPos(0x101, -20590, 1000, 3380, 29)
    SetChrPos(0x102, -21500, 1000, 3480, 55)
    SetChrPos(0x108, -21000, 1000, 2080, 29)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, -19300, 1000, 10370, 167)
    SetChrPos(0x9, -20480, 1000, 11180, 175)
    SetChrPos(0xA, -18330, 1000, 10260, 167)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_6D(-19300, 1000, 10370, 1000)

    def lambda_182C():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_182C)

    def lambda_1841():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1841)

    def lambda_1856():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1856)

    def lambda_186B():
        OP_69(0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_186B)
    Sleep(800)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x2BD, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 10)
    SetChrChipByIndex(0x9, 10)
    SetChrChipByIndex(0xA, 10)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    Sleep(500)
    EventEnd(0x0)
    Return()

    # Function_12_1738 end

    SaveToFile()

Try(main)
