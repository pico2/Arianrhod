from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4301   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4301.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60089",
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
        'ED6_DT07/CH00440 ._CH',             # 0B
        'ED6_DT07/CH00441 ._CH',             # 0C
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
        'ED6_DT07/CH00440P._CP',             # 0B
        'ED6_DT07/CH00441P._CP',             # 0C
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
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


    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 1000,
        TriggerY            = 42050,
        TriggerRange        = 800,
        ActorX              = 0,
        ActorZ              = 2000,
        ActorY              = 42050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1F6",          # 00, 0
        "Function_1_296",          # 01, 1
        "Function_2_2D9",          # 02, 2
        "Function_3_4EC",          # 03, 3
        "Function_4_9A8",          # 04, 4
        "Function_5_E97",          # 05, 5
        "Function_6_1018",         # 06, 6
        "Function_7_1199",         # 07, 7
        "Function_8_131A",         # 08, 8
        "Function_9_149B",         # 09, 9
        "Function_10_161C",        # 0A, 10
        "Function_11_179D",        # 0B, 11
        "Function_12_191E",        # 0C, 12
        "Function_13_1A9F",        # 0D, 13
    )


    def Function_0_1F6(): pass

    label("Function_0_1F6")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_22A"),
        (100, "loc_240"),
        (102, "loc_256"),
        (103, "loc_25D"),
        (104, "loc_264"),
        (105, "loc_26B"),
        (106, "loc_272"),
        (107, "loc_279"),
        (108, "loc_280"),
        (109, "loc_287"),
        (110, "loc_28E"),
        (SWITCH_DEFAULT, "loc_295"),
    )


    label("loc_22A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_23D")
    OP_A2(0x653)
    Event(0, 3)

    label("loc_23D")

    Jump("loc_295")

    label("loc_240")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_253")
    OP_A2(0x653)
    Event(0, 4)

    label("loc_253")

    Jump("loc_295")

    label("loc_256")

    Event(0, 13)
    Jump("loc_295")

    label("loc_25D")

    Event(0, 12)
    Jump("loc_295")

    label("loc_264")

    Event(0, 11)
    Jump("loc_295")

    label("loc_26B")

    Event(0, 10)
    Jump("loc_295")

    label("loc_272")

    Event(0, 9)
    Jump("loc_295")

    label("loc_279")

    Event(0, 8)
    Jump("loc_295")

    label("loc_280")

    Event(0, 7)
    Jump("loc_295")

    label("loc_287")

    Event(0, 6)
    Jump("loc_295")

    label("loc_28E")

    Event(0, 5)
    Jump("loc_295")

    label("loc_295")

    Return()

    # Function_0_1F6 end

    def Function_1_296(): pass

    label("Function_1_296")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE4A80, 0x30062)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B8")
    OP_72(0x0, 0x10)
    Jump("loc_2BC")

    label("loc_2B8")

    OP_64(0x0, 0x1)

    label("loc_2BC")

    SoundDistance(0x1CB, 0xFFFFFF7E, 0xFA, 0x3E1C, 0x7D0, 0x61A8, 0x64, 0x0)
    Return()

    # Function_1_296 end

    def Function_2_2D9(): pass

    label("Function_2_2D9")

    SetMapFlags(0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_412")
    OP_A2(0x655)
    EventBegin(0x0)
    OP_6D(-70, 1000, 41330, 1000)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上着锁，无法打开。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        "#009F唉～怎么会这样！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F真是相当坚固的锁呢……\x01",
            "得先找到钥匙才行呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DF")

    ChrTalk(
        0x108,
        (
            "#072F唔，\x01",
            "那就只能暂时先到别的地方看看了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40D")

    label("loc_3DF")


    ChrTalk(
        0x108,
        (
            "#070F唔，\x01",
            "去问问那个年轻的管家吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x4C, 0x1, 0x8)

    label("loc_40D")

    EventEnd(0x1)
    Jump("loc_4E6")

    label("loc_412")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 7)), scpexpr(EXPR_END)), "loc_48F")
    EventBegin(0x0)
    OP_6D(-70, 1000, 41330, 1000)
    OP_A2(0x658)
    OP_71(0x0, 0x10)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "使用了\x07\x02",
            "备用钥匙\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3F(0x36F, 1)
    OP_22(0x73, 0x0, 0x64)
    Sleep(800)
    OP_64(0x0, 0x1)
    EventEnd(0x1)
    Jump("loc_4E6")

    label("loc_48F")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上着锁，无法打开。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_4E6")

    ClearMapFlags(0x80)
    Return()

    # Function_2_2D9 end

    def Function_3_4EC(): pass

    label("Function_3_4EC")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    SetChrPos(0x101, 16560, 1000, -8020, 87)
    SetChrPos(0x102, 15530, 1000, -8910, 135)
    SetChrPos(0x108, 15490, 1000, -6910, 45)
    OP_6D(15530, 1000, -7950, 0)
    SetChrChipByIndex(0x8, 6)
    SetChrChipByIndex(0x9, 11)
    SetChrChipByIndex(0xB, 8)
    SetChrChipByIndex(0xC, 8)
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

    def lambda_5CF():
        OP_6D(18540, 1000, -4090, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5CF)

    def lambda_5E7():
        OP_6C(0, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5E7)
    SetChrChipByIndex(0x8, 7)

    def lambda_5FC():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5FC)
    Sleep(50)
    SetChrChipByIndex(0x9, 12)

    def lambda_621():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_621)
    Sleep(50)
    SetChrChipByIndex(0xB, 9)

    def lambda_646():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_646)
    Sleep(50)
    SetChrChipByIndex(0xC, 9)

    def lambda_66B():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_66B)

    def lambda_686():
        TurnDirection(0xFE, 0x8, 800)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_686)

    def lambda_694():
        TurnDirection(0xFE, 0x8, 800)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_694)

    def lambda_6A2():
        TurnDirection(0xFE, 0x8, 800)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_6A2)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0x8, 0x1)
    SetChrChipByIndex(0x8, 6)
    SetChrSubChip(0x8, 0)
    WaitChrThread(0x9, 0x1)
    SetChrChipByIndex(0x9, 11)
    SetChrSubChip(0x9, 0)
    WaitChrThread(0xB, 0x1)
    SetChrChipByIndex(0xB, 8)
    SetChrSubChip(0xB, 0)

    def lambda_722():

        label("loc_722")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_722")

    QueueWorkItem2(0xB, 0, lambda_722)
    WaitChrThread(0xC, 0x1)
    SetChrChipByIndex(0xC, 8)
    SetChrSubChip(0xC, 0)

    def lambda_744():

        label("loc_744")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_744")

    QueueWorkItem2(0xC, 0, lambda_744)
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x9,
        "可疑的人，在那儿不许动！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 7)

    def lambda_77F():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_77F)
    Sleep(50)
    SetChrChipByIndex(0x9, 12)

    def lambda_79E():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_79E)
    Sleep(50)
    SetChrChipByIndex(0xB, 9)

    def lambda_7BD():
        OP_92(0xFE, 0x108, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_7BD)
    Sleep(50)
    SetChrChipByIndex(0xC, 9)

    def lambda_7DC():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_7DC)
    Sleep(400)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    Battle(0x3AB, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_819"),
        (SWITCH_DEFAULT, "loc_81C"),
    )


    label("loc_819")

    OP_B4(0x0)
    Return()

    label("loc_81C")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    SetChrPos(0x101, 17530, 1000, -6110, 45)
    SetChrPos(0x102, 18110, 1000, -4380, 180)
    SetChrPos(0x108, 19360, 1000, -6190, 330)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 10)
    SetChrChipByIndex(0x9, 10)
    ClearChrFlags(0x8, 0x1)
    ClearChrFlags(0x9, 0x1)
    SetChrFlags(0x8, 0x800)
    SetChrFlags(0x9, 0x800)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0x8, 18460, 1000, -2860, 180)
    SetChrPos(0x9, 19820, 1000, -3010, 135)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    OP_6D(17470, 1000, -4720, 0)
    OP_6C(315000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#007F呼～解决了。\x01",
            "冷不妨就跳出几个人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F还有相当数量的特务兵残留在离宫里面。\x01",
            "　\x02\x03",
            "好像定期在中庭的走廊巡逻。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#072F没办法，若是被发现了，\x01",
            "就只有让他们保持沉默了。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_3_4EC end

    def Function_4_9A8(): pass

    label("Function_4_9A8")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    SetChrPos(0x101, -16350, 1000, -7540, 301)
    SetChrPos(0x102, -16410, 1000, -8720, 243)
    SetChrPos(0x108, -15040, 1000, -8100, 302)
    OP_6D(-15730, 1000, -8020, 0)
    SetChrChipByIndex(0x8, 6)
    SetChrChipByIndex(0x9, 11)
    SetChrChipByIndex(0xB, 8)
    SetChrChipByIndex(0xC, 8)
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

    def lambda_A8B():
        OP_6D(-19130, 1000, -4630, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_A8B)

    def lambda_AA3():
        OP_6C(0, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AA3)
    SetChrChipByIndex(0x8, 7)

    def lambda_AB8():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_AB8)
    Sleep(50)
    SetChrChipByIndex(0x9, 12)

    def lambda_ADD():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_ADD)
    Sleep(50)
    SetChrChipByIndex(0xB, 9)

    def lambda_B02():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_B02)
    Sleep(50)
    SetChrChipByIndex(0xC, 9)

    def lambda_B27():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_B27)

    def lambda_B42():
        TurnDirection(0xFE, 0x8, 800)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B42)

    def lambda_B50():
        TurnDirection(0xFE, 0x8, 800)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B50)

    def lambda_B5E():
        TurnDirection(0xFE, 0x8, 800)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_B5E)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0x8, 0x1)
    SetChrChipByIndex(0x8, 6)
    SetChrSubChip(0x8, 0)
    WaitChrThread(0x9, 0x1)
    SetChrChipByIndex(0x9, 11)
    SetChrSubChip(0x9, 0)
    WaitChrThread(0xB, 0x1)
    SetChrChipByIndex(0xB, 8)
    SetChrSubChip(0xB, 0)

    def lambda_BDE():

        label("loc_BDE")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_BDE")

    QueueWorkItem2(0xB, 0, lambda_BDE)
    WaitChrThread(0xC, 0x1)
    SetChrChipByIndex(0xC, 8)
    SetChrSubChip(0xC, 0)

    def lambda_C00():

        label("loc_C00")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_C00")

    QueueWorkItem2(0xC, 0, lambda_C00)
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x8,
        "可疑的人，在那儿不许动！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 7)

    def lambda_C3B():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C3B)
    Sleep(50)
    SetChrChipByIndex(0x9, 12)

    def lambda_C5A():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_C5A)
    Sleep(50)
    SetChrChipByIndex(0xB, 9)

    def lambda_C79():
        OP_92(0xFE, 0x102, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_C79)
    Sleep(50)
    SetChrChipByIndex(0xC, 9)

    def lambda_C98():
        OP_92(0xFE, 0x108, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_C98)
    Sleep(400)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    Battle(0x3AC, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_CD5"),
        (SWITCH_DEFAULT, "loc_CD8"),
    )


    label("loc_CD5")

    OP_B4(0x0)
    Return()

    label("loc_CD8")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    SetChrPos(0x101, -18900, 1000, -6950, 14)
    SetChrPos(0x102, -17970, 1000, -6160, 345)
    SetChrPos(0x108, -20110, 1000, -5730, 45)
    SetChrPos(0x101, -18900, 1000, -6950, 339)
    SetChrPos(0x102, -18280, 1000, -5200, 225)
    SetChrPos(0x108, -20110, 1000, -5730, 105)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 10)
    SetChrChipByIndex(0x9, 10)
    ClearChrFlags(0x8, 0x1)
    ClearChrFlags(0x9, 0x1)
    SetChrFlags(0x8, 0x800)
    SetChrFlags(0x9, 0x800)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0x8, -17200, 1000, -3390, 180)
    SetChrPos(0x9, -18660, 1000, -3640, 225)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    OP_6D(-18490, 1000, -4850, 0)
    OP_6C(45000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#007F呼～解决了。\x01",
            "冷不妨就跳出几个人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F还有相当数量的特务兵残留在离宫里面。\x01",
            "　\x02\x03",
            "好像定期在中庭的走廊巡逻。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#072F没办法，若是被发现了，\x01",
            "就只有让他们保持沉默了。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_4_9A8 end

    def Function_5_E97(): pass

    label("Function_5_E97")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EA9")
    Return()

    label("loc_EA9")

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

    def lambda_F8B():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F8B)

    def lambda_FA0():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_FA0)

    def lambda_FB5():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_FB5)

    def lambda_FCA():
        OP_69(0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_FCA)
    Sleep(800)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x2BD, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    Sleep(500)
    EventEnd(0x0)
    Return()

    # Function_5_E97 end

    def Function_6_1018(): pass

    label("Function_6_1018")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_102A")
    Return()

    label("loc_102A")

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

    def lambda_110C():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_110C)

    def lambda_1121():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1121)

    def lambda_1136():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1136)

    def lambda_114B():
        OP_69(0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_114B)
    Sleep(800)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x2BD, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    Sleep(500)
    EventEnd(0x0)
    Return()

    # Function_6_1018 end

    def Function_7_1199(): pass

    label("Function_7_1199")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11AB")
    Return()

    label("loc_11AB")

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

    def lambda_128D():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_128D)

    def lambda_12A2():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_12A2)

    def lambda_12B7():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_12B7)

    def lambda_12CC():
        OP_69(0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_12CC)
    Sleep(800)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x2BD, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    Sleep(500)
    EventEnd(0x0)
    Return()

    # Function_7_1199 end

    def Function_8_131A(): pass

    label("Function_8_131A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_132C")
    Return()

    label("loc_132C")

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

    def lambda_140E():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_140E)

    def lambda_1423():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1423)

    def lambda_1438():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1438)

    def lambda_144D():
        OP_69(0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_144D)
    Sleep(800)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x2BD, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    Sleep(500)
    EventEnd(0x0)
    Return()

    # Function_8_131A end

    def Function_9_149B(): pass

    label("Function_9_149B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14AD")
    Return()

    label("loc_14AD")

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

    def lambda_158F():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_158F)

    def lambda_15A4():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_15A4)

    def lambda_15B9():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_15B9)

    def lambda_15CE():
        OP_69(0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_15CE)
    Sleep(800)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x2BD, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    Sleep(500)
    EventEnd(0x0)
    Return()

    # Function_9_149B end

    def Function_10_161C(): pass

    label("Function_10_161C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_162E")
    Return()

    label("loc_162E")

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

    def lambda_1710():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1710)

    def lambda_1725():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1725)

    def lambda_173A():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_173A)

    def lambda_174F():
        OP_69(0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_174F)
    Sleep(800)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x2BD, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    Sleep(500)
    EventEnd(0x0)
    Return()

    # Function_10_161C end

    def Function_11_179D(): pass

    label("Function_11_179D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17AF")
    Return()

    label("loc_17AF")

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

    def lambda_1891():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1891)

    def lambda_18A6():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_18A6)

    def lambda_18BB():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_18BB)

    def lambda_18D0():
        OP_69(0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_18D0)
    Sleep(800)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x2BD, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    Sleep(500)
    EventEnd(0x0)
    Return()

    # Function_11_179D end

    def Function_12_191E(): pass

    label("Function_12_191E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1930")
    Return()

    label("loc_1930")

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

    def lambda_1A12():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1A12)

    def lambda_1A27():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1A27)

    def lambda_1A3C():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1A3C)

    def lambda_1A51():
        OP_69(0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1A51)
    Sleep(800)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x2BD, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    Sleep(500)
    EventEnd(0x0)
    Return()

    # Function_12_191E end

    def Function_13_1A9F(): pass

    label("Function_13_1A9F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AB1")
    Return()

    label("loc_1AB1")

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

    def lambda_1B93():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1B93)

    def lambda_1BA8():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1BA8)

    def lambda_1BBD():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1BBD)

    def lambda_1BD2():
        OP_69(0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1BD2)
    Sleep(800)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x2BD, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    Sleep(500)
    EventEnd(0x0)
    Return()

    # Function_13_1A9F end

    SaveToFile()

Try(main)
