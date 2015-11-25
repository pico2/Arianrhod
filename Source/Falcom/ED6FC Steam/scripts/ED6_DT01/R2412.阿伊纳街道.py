from ED6ScenarioHelper import *

def main():
    # 阿伊纳街道

    CreateScenaFile(
        FileName            = 'R2412   ._SN',
        MapName             = 'Ruan',
        Location            = 'R2412.x',
        MapIndex            = 103,
        MapDefaultBGM       = "ed60086",
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
        '黑衣男子',                             # 9
        '黑衣男子',                             # 10
        '阿加特',                               # 11
        '蒙面队长',                             # 12
        '目标用摄像机',                         # 13
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
        Unknown_3A              = 103,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH00341 ._CH',             # 00
        'ED6_DT07/CH00151 ._CH',             # 01
        'ED6_DT07/CH00152 ._CH',             # 02
        'ED6_DT07/CH00260 ._CH',             # 03
        'ED6_DT07/CH00340 ._CH',             # 04
        'ED6_DT07/CH00341 ._CH',             # 05
        'ED6_DT07/CH00342 ._CH',             # 06
        'ED6_DT07/CH00344 ._CH',             # 07
        'ED6_DT07/CH00260 ._CH',             # 08
        'ED6_DT07/CH00261 ._CH',             # 09
        'ED6_DT07/CH00262 ._CH',             # 0A
        'ED6_DT07/CH00264 ._CH',             # 0B
        'ED6_DT07/CH00265 ._CH',             # 0C
        'ED6_DT07/CH02200 ._CH',             # 0D
        'ED6_DT06/CH20137 ._CH',             # 0E
        'ED6_DT06/CH20138 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT07/CH00341P._CP',             # 00
        'ED6_DT07/CH00151P._CP',             # 01
        'ED6_DT07/CH00152P._CP',             # 02
        'ED6_DT07/CH00260P._CP',             # 03
        'ED6_DT07/CH00340P._CP',             # 04
        'ED6_DT07/CH00341P._CP',             # 05
        'ED6_DT07/CH00342P._CP',             # 06
        'ED6_DT07/CH00344P._CP',             # 07
        'ED6_DT07/CH00260P._CP',             # 08
        'ED6_DT07/CH00261P._CP',             # 09
        'ED6_DT07/CH00262P._CP',             # 0A
        'ED6_DT07/CH00264P._CP',             # 0B
        'ED6_DT07/CH00265P._CP',             # 0C
        'ED6_DT07/CH02200P._CP',             # 0D
        'ED6_DT06/CH20137P._CP',             # 0E
        'ED6_DT06/CH20138P._CP',             # 0F
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 180,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -2060,
        TriggerZ            = 0,
        TriggerY            = 120820,
        TriggerRange        = 1500,
        ActorX              = -2060,
        ActorZ              = 1500,
        ActorY              = 120820,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1EE",          # 00, 0
        "Function_1_1F3",          # 01, 1
        "Function_2_206",          # 02, 2
        "Function_3_20A9",         # 03, 3
        "Function_4_218F",         # 04, 4
        "Function_5_2230",         # 05, 5
        "Function_6_2408",         # 06, 6
        "Function_7_2455",         # 07, 7
        "Function_8_2482",         # 08, 8
        "Function_9_24AF",         # 09, 9
    )


    def Function_0_1EE(): pass

    label("Function_0_1EE")

    Event(0, 2)
    Return()

    # Function_0_1EE end

    def Function_1_1F3(): pass

    label("Function_1_1F3")

    OP_16(0x2, 0xFA0, 0xFFFDECC0, 0xFFFF34E0, 0x30025)
    Return()

    # Function_1_1F3 end

    def Function_2_206(): pass

    label("Function_2_206")

    FadeToBright(2000, 0)
    LoadEffect(0x0, "craft\\\\cr201_00.eff")
    LoadEffect(0x1, "craft\\\\cr201_01.eff")
    LoadEffect(0x2, "craft\\\\cr201_02.eff")
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-4600, 3000, 117500, 0)
    OP_6B(3400, 0)
    OP_67(0, 3300, -10000, 0)
    OP_6C(52000, 0)
    SetChrPos(0x8, -4900, 0, 125700, 0)
    SetChrPos(0x9, -3900, 0, 125000, 0)
    SetChrPos(0xA, 5300, 0, 139100, 0)

    def lambda_2C5():
        OP_6C(45000, 5000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2C5)
    OP_6D(-4600, 0, 117500, 5000)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)

    def lambda_2F5():
        OP_8E(0xFE, 0xFFFFE9BC, 0x0, 0x1C4BC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2F5)

    def lambda_310():
        OP_8E(0xFE, 0xFFFFEE08, 0x0, 0x1CAFC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_310)
    WaitChrThread(0x9, 0x1)

    def lambda_330():
        OP_8C(0x9, 0, 800)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_330)
    WaitChrThread(0x8, 0x1)

    def lambda_343():
        OP_8C(0x8, 0, 800)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_343)

    ChrTalk(
        0x8,
        "哈啊哈啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2P好、好缠人的家伙！\x02",
    )

    CloseMessageWindow()

    def lambda_37E():
        OP_6C(21000, 3000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_37E)
    OP_43(0xA, 0x1, 0x0, 0x5)

    ChrTalk(
        0xA,
        "#15A#4P哦喔喔喔喔！\x05\x02",
    )

    Sleep(200)
    OP_43(0x8, 0x1, 0x0, 0x3)
    Sleep(200)
    OP_43(0x9, 0x1, 0x0, 0x4)
    OP_6A(0x9)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#15A#6P背着这么一把巨剑，\x01",
            "竟然还能追得上来！\x05\x02",
        )
    )

    Sleep(2000)

    ChrTalk(
        0xA,
        "#10A#1P哼，别把我和你们这些三脚猫混为一谈。\x05\x02",
    )

    Sleep(1400)

    ChrTalk(
        0xA,
        "#12A#5S#5P喝啊啊啊啊啊！\x05\x02",
    )

    WaitChrThread(0xA, 0x1)

    def lambda_45E():
        OP_6C(348000, 4000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_45E)
    Sleep(500)
    OP_96(0xA, 0xFFFFE0C0, 0x0, 0xE358, 0x1F4, 0x1770)
    OP_22(0xA4, 0x0, 0x64)
    OP_99(0xA, 0x7, 0x0, 0x7D0)
    ClearChrFlags(0xA, 0x800)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#6P呜……\x01",
            "还是甩不掉吗……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4C2():

        label("loc_4C2")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_4C2")

    QueueWorkItem2(0x8, 0, lambda_4C2)

    def lambda_4D3():

        label("loc_4D3")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_4D3")

    QueueWorkItem2(0x9, 0, lambda_4D3)

    def lambda_4E4():
        OP_96(0x8, 0xFFFFECE6, 0x1E, 0xCB3E, 0x320, 0x1388)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4E4)
    WaitChrThread(0x8, 0x1)
    SetChrChipByIndex(0x8, 4)
    SetChrSubChip(0x8, 0)
    Sleep(100)

    def lambda_516():
        OP_96(0x9, 0xFFFFE3CC, 0x14, 0xC648, 0x320, 0x1388)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_516)
    WaitChrThread(0x9, 0x1)
    SetChrChipByIndex(0x9, 4)
    SetChrSubChip(0x9, 0)
    WaitChrThread(0xA, 0x1)

    ChrTalk(
        0x9,
        "没办法了，迎击吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#051F好极了。\x01",
            "终于打算动手了啊。\x02\x03",
            "和你们这些杂碎捉迷藏，\x01",
            "我可早就玩腻了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "你要是识趣不追上来的话，\x01",
            "或许还能保住自己的小命……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "愚蠢的家伙……\x01",
            "一对二你还想赢吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#051F哈哈，\x01",
            "我当然会赢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "什么……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#054F打架也要打得有气势。\x01",
            "连气势也输掉的话那就别想赢了。\x02\x03",
            "你们从夹着尾巴开溜那一刻起，\x01",
            "就已注定成为丧家之犬了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "一、一派胡言！\x01",
            "你这只协会的走狗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "看我们两个\x01",
            "怎么好好收拾你！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6FE():
        OP_6E(243, 1500)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_6FE)

    def lambda_70E():
        OP_6D(-7660, 0, 57680, 1500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_70E)
    PlayEffect(0x1, 0x1, 0xA, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_75B():
        OP_99(0xFE, 0x0, 0x4, 0xA28)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_75B)
    SetChrChipByIndex(0x8, 5)
    SetChrChipByIndex(0x9, 5)
    TurnDirection(0x8, 0xA, 0)
    TurnDirection(0x9, 0xA, 0)

    def lambda_783():
        OP_94(0x1, 0xFE, 0xB4, 0x5DC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_783)

    def lambda_799():
        OP_94(0x1, 0xFE, 0xB4, 0x5DC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_799)
    Sleep(500)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    Sleep(100)

    def lambda_7C1():
        OP_94(0x1, 0xFE, 0x0, 0x2328, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_7C1)
    Sleep(50)

    def lambda_7DC():
        OP_94(0x1, 0xFE, 0x0, 0x2328, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_7DC)
    Sleep(400)
    OP_82(0x1, 0x2)
    PlayEffect(0x0, 0xFF, 0xA, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_82F():
        OP_99(0xFE, 0x4, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_82F)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 7)
    SetChrFlags(0x8, 0x20)

    def lambda_88E():
        OP_94(0x1, 0xFE, 0xB4, 0xFA0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_88E)
    Sleep(50)
    PlayEffect(0x2, 0xFF, 0x9, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 7)
    SetChrFlags(0x9, 0x20)

    def lambda_8F3():
        OP_94(0x1, 0xFE, 0xB4, 0xFA0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_8F3)

    def lambda_909():
        OP_94(0x1, 0xFE, 0xB4, 0xFA0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_909)
    Sleep(50)

    def lambda_924():
        OP_94(0x1, 0xFE, 0xB4, 0xFA0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_924)

    def lambda_93A():
        OP_94(0x1, 0xFE, 0xB4, 0xFA0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_93A)
    Sleep(50)

    def lambda_955():
        OP_94(0x1, 0xFE, 0xB4, 0xFA0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_955)

    def lambda_96B():
        OP_94(0x1, 0xFE, 0xB4, 0xFA0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_96B)
    Sleep(50)

    def lambda_986():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_986)

    def lambda_99C():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_99C)
    Sleep(50)

    def lambda_9B7():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_9B7)
    Sleep(450)
    Fade(1000)
    OP_44(0x0, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_6D(-7670, 0, 56050, 0)
    OP_6B(3000, 0)
    OP_67(0, 8200, -10000, 0)
    OP_6C(45000, 0)
    SetChrPos(0x8, -8400, 0, 54200, 0)
    SetChrPos(0x9, -9800, 0, 54800, 0)
    SetChrPos(0xB, -6700, 0, 58700, 180)
    TurnDirection(0xA, 0x8, 0)
    TurnDirection(0x8, 0xA, 0)
    TurnDirection(0x9, 0xA, 0)
    PlayEffect(0x2, 0xFF, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0x9, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "#4P呜啊啊啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "呜……\x01",
            "怎么能在这种地方被抓住………\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B0E():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B0E)

    def lambda_B1C():
        OP_99(0xFE, 0x5, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_B1C)
    OP_96(0xA, 0xFFFFE37C, 0x0, 0xDC50, 0x2BC, 0xFA0)
    OP_44(0xA, 0x2)
    SetChrChipByIndex(0xA, 14)
    SetChrSubChip(0xA, 0)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#050F#5P哼，还不赶快投降。\x01",
            "给我老老实实地坦白一切！\x02\x03",
            "你们是什么人？\x01",
            "干那么多坏事有什么企图……\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    SetChrPos(0xB, -4010, 0, 61460, 270)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    NpcTalk(
        0xB,
        "青年的声音",
        "#4P——这可真让人为难啊。\x02",
    )

    CloseMessageWindow()
    OP_21()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)
    SetChrChipByIndex(0xA, 14)
    SetChrSubChip(0xA, 0)
    OP_8C(0xA, 43, 600)

    ChrTalk(
        0xA,
        "#052F#4P什么！？\x02",
    )

    CloseMessageWindow()
    OP_1D(0x51)
    SetChrChipByIndex(0xB, 13)
    ClearChrFlags(0xB, 0x80)

    def lambda_C55():
        OP_6D(-6790, 0, 56980, 1500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_C55)

    def lambda_C6D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_C6D)

    def lambda_C7F():
        OP_8E(0xFE, 0xFFFFE5D4, 0x0, 0xE54C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_C7F)
    SetChrChipByIndex(0xA, 2)
    SetChrSubChip(0xA, 7)

    def lambda_CA4():
        OP_8C(0xFE, 0, 800)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_CA4)
    OP_96(0xA, 0xFFFFE890, 0x0, 0xD6D8, 0x2BC, 0xFA0)
    Sleep(500)

    ChrTalk(
        0xA,
        "#055F#4P什、什么时候……\x02",
    )

    CloseMessageWindow()

    def lambda_CEC():
        OP_99(0x8, 0x3, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_CEC)

    ChrTalk(
        0x8,
        "队、队长！\x02",
    )

    CloseMessageWindow()

    def lambda_D0C():
        OP_99(0x9, 0x3, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_D0C)

    ChrTalk(
        0x9,
        "您来救我们了吗！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#281F真拿你们没办法。\x02\x03",
            "不仅没按时进行联络，\x01",
            "还在这种地方玩起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "实、实在抱歉！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "一路上遇到重重阻挠……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#050F#4P原来如此啊……\x01",
            "这么说你就是他们的老大吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 400)
    Sleep(400)

    ChrTalk(
        0xB,
        (
            "#280F呵呵……\x01",
            "我只不过是现场负责人而已。\x02\x03",
            "我为部下的失礼表示歉意，\x01",
            "能不能在此放他们一马呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#055F#4P啊？\x02\x03",
            "你刚才……说什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#280F我说能不能放他们一马。\x02\x03",
            "说到底，\x01",
            "我们也没打算和游击士协会为敌。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#054F#4P白、白痴啊你！\x01",
            "世上哪有这么便宜的好事！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#281F哎呀哎呀……\x01",
            "我可是觉得这提议不错啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x9, 400)
    Sleep(400)

    ChrTalk(
        0xB,
        (
            "#281F……你们两个。\x01",
            "这里由我来挡着。\x02\x03",
            "你们快去会合地点吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)

    ChrTalk(
        0x8,
        "是、是！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 5)
    ClearChrFlags(0x8, 0x20)

    def lambda_F8F():
        OP_8E(0xFE, 0xFFFFDD3C, 0x0, 0xAB7C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F8F)

    ChrTalk(
        0x9,
        "多谢队长！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x9, 5)
    ClearChrFlags(0x8, 0x20)

    def lambda_FC4():
        OP_8E(0xFE, 0xFFFFDD3C, 0x0, 0xAB7C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_FC4)
    SetChrChipByIndex(0xA, 14)
    SetChrSubChip(0xA, 0)

    def lambda_FE9():

        label("loc_FE9")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_FE9")

    QueueWorkItem2(0xA, 1, lambda_FE9)
    Sleep(300)
    OP_44(0xA, 0xFF)

    ChrTalk(
        0xA,
        "#054F又想逃吗？喂！！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xB, 9)
    OP_8E(0xB, 0xFFFFE318, 0x0, 0xDEA8, 0x1B58, 0x0)

    def lambda_1037():
        OP_6C(0, 2000)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_1037)

    def lambda_1047():
        OP_6D(-9340, 0, 52260, 1000)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1047)

    def lambda_105F():
        OP_97(0xFE, 0xFFFFEC14, 0xD034, 0xFFFEDB08, 0x36B0, 0x1)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_105F)
    SetChrChipByIndex(0xA, 1)
    OP_8E(0xA, 0xFFFFDF94, 0x0, 0xCF08, 0x1B58, 0x0)
    TurnDirection(0xA, 0xB, 0)

    def lambda_109B():

        label("loc_109B")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_109B")

    QueueWorkItem2(0xB, 0, lambda_109B)
    SetChrChipByIndex(0xA, 14)
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xB, 8)

    def lambda_10CC():
        OP_96(0xFE, 0xFFFFE124, 0xFFFFFFCE, 0xD0AC, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_10CC)
    OP_22(0x1F5, 0x0, 0x64)
    TurnDirection(0xA, 0xB, 0)
    TurnDirection(0xB, 0xA, 800)
    OP_8F(0xB, 0xFFFFD760, 0x0, 0xC738, 0xFA0, 0x0)
    Sleep(500)
    WaitChrThread(0xB, 0x3)

    ChrTalk(
        0xB,
        "#280F………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#057F#2P混帐……\x02\x03",
            "#053F哼，算了。\x01",
            "不过是换了个猎物罢了。\x02\x03",
            "看来你知道的东西\x01",
            "比那两个杂碎的更有价值……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#280F呵呵……\x01",
            "你以为这么简单就能抓住我吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11D3():

        label("loc_11D3")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_11D3")

    QueueWorkItem2(0xA, 0, lambda_11D3)

    ChrTalk(
        0xA,
        "#054F#2P正是！\x02",
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    OP_21()
    OP_1D(0x2B)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)

    def lambda_120F():
        OP_6C(315000, 1000)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_120F)
    ClearChrFlags(0xA, 0x20)
    SetChrChipByIndex(0xA, 1)
    OP_94(0x1, 0xA, 0xB4, 0x1F4, 0x3E8, 0x0)
    OP_51(0xC, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xC, 0x3E8)
    OP_6A(0xC)
    OP_43(0x8, 0x1, 0x0, 0x6)
    OP_93(0xA, 0xB, 0x640, 0x2EE0, 0x0)
    SetChrFlags(0xA, 0x20)
    SetChrChipByIndex(0xB, 12)
    SetChrSubChip(0xB, 0)
    SetChrChipByIndex(0xA, 15)
    SetChrSubChip(0xA, 0)
    OP_22(0x1F9, 0x0, 0x64)

    def lambda_12B4():
        OP_94(0x1, 0xFE, 0x0, 0xC8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_12B4)

    def lambda_12CA():
        OP_94(0x1, 0xFE, 0xB4, 0xC8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_12CA)
    OP_9E(0xB, 0x1E, 0x0, 0x12C, 0x1388)
    WaitChrThread(0xB, 0x1)

    def lambda_12F8():
        OP_94(0x1, 0xFE, 0x0, 0x5DC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_12F8)
    SetChrChipByIndex(0xB, 8)
    SetChrSubChip(0xB, 0)
    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0xA, 2)
    SetChrSubChip(0xA, 7)
    OP_96(0xB, 0xFFFFCFF4, 0x514, 0xC47C, 0x578, 0x3A98)
    Sleep(100)
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xB, 10)
    OP_44(0xB, 0xFF)

    def lambda_1357():
        OP_96(0xFE, 0xFFFFD828, 0x514, 0xC670, 0x3E8, 0x2710)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1357)

    def lambda_1375():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1375)
    Sleep(200)
    OP_22(0x1F5, 0x0, 0x64)

    def lambda_138F():
        OP_96(0xFE, 0xFFFFDC10, 0x0, 0xCF08, 0x3E8, 0x2710)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_138F)

    def lambda_13AD():

        label("loc_13AD")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_13AD")

    QueueWorkItem2(0xB, 0, lambda_13AD)
    SetChrChipByIndex(0xA, 1)
    WaitChrThread(0xB, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_96(0xB, 0xFFFFDAE4, 0x0, 0xBAB8, 0x3E8, 0x2710)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_13E9():
        OP_99(0xFE, 0x7, 0xB, 0x5DC)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_13E9)
    OP_6B(2900, 1000)
    SetChrChipByIndex(0xB, 9)
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_96(0xB, 0xFFFFDF94, 0x0, 0xC030, 0x1F4, 0xBB8)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_142E():
        OP_6B(2500, 1000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_142E)
    OP_96(0xB, 0xFFFFD954, 0x0, 0xC3B4, 0x1F4, 0x1B58)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_145A():
        OP_8C(0xA, 30, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_145A)
    OP_96(0xB, 0xFFFFE188, 0x0, 0xCA58, 0x1F4, 0x2710)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_1484():
        OP_96(0xB, 0xFFFFDCD8, 0x0, 0xCB20, 0x1F4, 0x2710)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1484)
    OP_44(0xA, 0xFF)
    OP_22(0x1F9, 0x0, 0x64)
    OP_8C(0xA, 315, 1300)
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xB, 8)

    def lambda_14C2():
        OP_96(0xFE, 0xFFFFDAE4, 0x1F4, 0xCABC, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_14C2)
    OP_8C(0xA, 135, 1600)
    Sleep(350)
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xB, 10)

    def lambda_14FC():
        OP_99(0xFE, 0x0, 0x2, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_14FC)
    OP_8C(0xA, 225, 0)
    SetChrChipByIndex(0xA, 2)
    OP_99(0xA, 0x6, 0x7, 0x5DC)

    def lambda_1521():
        OP_99(0xA, 0x5, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_1521)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_1536():
        OP_99(0xFE, 0x2, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1536)

    def lambda_1546():
        OP_96(0xB, 0xFFFFDD3C, 0x0, 0xDDE0, 0xFA0, 0x1B58)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1546)
    Sleep(200)

    def lambda_1569():
        OP_8C(0xA, 0, 500)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_1569)
    Sleep(300)

    def lambda_157C():
        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_157C)
    OP_22(0xA4, 0x0, 0x64)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_1596():
        OP_96(0xA, 0xFFFFDD3C, 0x0, 0xDA5C, 0x7D0, 0x2710)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1596)

    def lambda_15B4():
        OP_99(0xA, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_15B4)
    Sleep(200)
    OP_22(0x1F9, 0x0, 0x64)
    Sleep(200)

    def lambda_15D3():
        OP_99(0xFE, 0x7, 0xB, 0x5DC)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_15D3)
    OP_8F(0xB, 0xFFFFE34A, 0x0, 0xDDE0, 0x3A98, 0x0)
    WaitChrThread(0xA, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_22(0x55, 0x0, 0x5A)
    PlayEffect(0x12, 0xFF, 0xFF, -8610, -1000, 56740, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    OP_96(0xB, 0xFFFFEC78, 0x0, 0xDD7C, 0x514, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(1000)

    def lambda_166D():
        OP_99(0xA, 0x7, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_166D)

    def lambda_167D():
        TurnDirection(0xA, 0xB, 400)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_167D)
    Sleep(500)

    ChrTalk(
        0xA,
        "#051F哼，有一手嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#281F怀着无法抑制的激情\x01",
            "来挥舞着沉重的铁块……\x02\x03",
            "你……\x01",
            "和我倒是有点像嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#052F………………………\x02\x03",
            "……什么……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#280F曾因自己的软弱无力\x01",
            "而被绝望束缚……\x02\x03",
            "你的眼神是这么说的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#052F………………………\x02\x03",
            "#053F哼哼哼，不错嘛。\x02\x03",
            "虽然不知道你是什么人，\x01",
            "不过说话倒是相当讨人喜欢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#280F我也一样，\x01",
            "并不讨厌你这种直性子的人。\x02\x03",
            "继续打斗下去也没意义，\x01",
            "我们干脆就此握手言和吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#057F#5S#5P玩笑开够了吧！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    LoadEffect(0x0, "battle\\\\mgaria0.eff")

    def lambda_1879():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1879)
    PlayEffect(0x0, 0x0, 0xA, 0, 200, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(500)

    ChrTalk(
        0xA,
        (
            "#057F#5P我不出声，\x01",
            "你就乱弹琴地鬼扯个没完！\x02\x03",
            "看我怎么打烂你那张胡言乱语的臭嘴！\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)

    ChrTalk(
        0xB,
        "#280F呵呵……\x02",
    )

    CloseMessageWindow()
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xB, 12)

    def lambda_1949():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1949)
    PlayEffect(0x0, 0x1, 0xB, 0, 200, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)

    def lambda_1998():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1998)
    Sleep(1000)

    def lambda_19B7():
        OP_6C(0, 6000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_19B7)

    def lambda_19C7():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_19C7)

    ChrTalk(
        0xA,
        "#15A#054F哦哦哦哦哦哦哦！\x05\x02",
    )

    Sleep(3000)

    def lambda_1A05():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1A05)

    ChrTalk(
        0xB,
        "#15A#282F喝啊啊啊啊啊啊！\x05\x02",
    )

    Sleep(3000)
    Sleep(500)
    OP_44(0xB, 0xFF)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xA, 0x40)
    OP_99(0xA, 0x0, 0x3, 0x7D0)

    def lambda_1A5F():
        OP_99(0xA, 0x3, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1A5F)

    def lambda_1A6F():
        TurnDirection(0xA, 0xB, 400)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_1A6F)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xB, 10)

    def lambda_1A96():
        OP_99(0xFE, 0x0, 0x3, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_1A96)

    def lambda_1AA6():
        OP_8E(0xFE, 0xFFFFDD3C, 0x0, 0xDA5C, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1AA6)

    def lambda_1AC1():
        OP_8E(0xFE, 0xFFFFEC78, 0x0, 0xDD7C, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1AC1)
    Sleep(100)
    OP_20(0x0)
    OP_22(0x9B, 0x0, 0x64)
    FadeToDark(1, 16777215, -1)
    OP_0D()
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    FadeToBright(200, 16777215)
    LoadEffect(0x0, "map\\\\mp009_00.eff")
    PlayEffect(0x0, 0x0, 0xC, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    PlayEffect(0x0, 0x1, 0xC, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)

    def lambda_1B89():
        OP_99(0xFE, 0x3, 0x7, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_1B89)

    ChrTalk(
        0xB,
        "#281F哼……\x02",
    )

    OP_9E(0xB, 0x32, 0x0, 0x1F4, 0x1388)
    CloseMessageWindow()
    WaitChrThread(0xB, 0x3)
    SetChrChipByIndex(0xB, 11)
    OP_99(0xB, 0x1, 0x3, 0x4B0)
    Sleep(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1BDE():
        OP_99(0xA, 0x7, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1BDE)
    OP_8C(0xA, 225, 400)
    Sleep(500)

    ChrTalk(
        0xA,
        (
            "#051F嘿……\x01",
            "看来你就只有嘴上工夫还算厉害。\x02\x03",
            "现在就把你带回协会\x01",
            "彻彻底底地审问一番吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x99, 0x0, 0x64)
    OP_43(0xB, 0x1, 0x0, 0x7)
    Sleep(1000)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    SetChrChipByIndex(0xA, 14)
    SetChrSubChip(0xA, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#052F什、什么……\x02",
    )

    CloseMessageWindow()
    OP_43(0xB, 0x1, 0x0, 0x8)
    Sleep(1000)
    OP_44(0xB, 0x1)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0xC8, 0x0)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
    Sleep(500)

    ChrTalk(
        0xA,
        (
            "#055F这、这是……\x01",
            "分身的战技！？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在昏暗树丛的空隙中隐隐约约地漂浮着人影。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_1D(0x53)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("青年的声音")
    SetMessageWindowPos(75, 250, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#50W呵呵呵……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrName("青年的声音")

    AnonymousTalk(
        (
            "#50W不错的一击，\x01",
            "只是似乎还带有些迷惘啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("青年的声音")

    AnonymousTalk(
        "#50W这份迷惘会令刀法产生破绽。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(
        0xA,
        "#057F什、什么！？\x02",
    )

    CloseMessageWindow()
    SetChrName("青年的声音")

    AnonymousTalk(
        (
            "#50W想要化身修罗，\x01",
            "就必须有舍弃一切的觉悟。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            "#50W想在这个世上生存下去……\x01",
            "就必须忘却一切愤怒和悲伤。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        "#100W那么，后会有期……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "树丛空隙间隐隐约约漂浮着的人影\x01",
            "一瞬间隐入黑暗中消失了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x1)

    def lambda_1F1E():
        OP_6D(-5100, 1400, 56900, 1600)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1F1E)
    WaitChrThread(0xA, 0x2)
    SetChrChipByIndex(0xA, 15)
    SetChrSubChip(0xA, 0)
    OP_9E(0xA, 0x14, 0x0, 0x3E8, 0x1388)

    ChrTalk(
        0xA,
        (
            "#056F#50W#5P…………………………\x02\x03",
            "#50W……说什么忘却……\x02\x03",
            "#50W这种事……\x01",
            "……我怎么可能做得出……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1FBF():
        OP_6B(2400, 2000)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_1FBF)

    def lambda_1FCF():
        OP_67(0, 6000, -10000, 2300)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1FCF)

    def lambda_1FE7():
        OP_6C(54000, 2000)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_1FE7)
    Sleep(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2005():
        OP_6B(5000, 3000)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_2005)

    def lambda_2015():

        label("loc_2015")

        OP_9E(0xFE, 0x1E, 0x0, 0x7D0, 0x1388)
        OP_48()
        Jump("loc_2015")

    QueueWorkItem2(0xA, 0, lambda_2015)
    SetChrSubChip(0xA, 1)

    ChrTalk(
        0xA,
        "#550F#5P#22A#5S呜哦哦哦哦哦哦哦哦！\x05\x02",
    )

    FadeToDark(3000, 0, -1)
    OP_0D()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_20(0x7D0)
    OP_21()
    Sleep(1000)
    OP_AD(0x4003F, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    OP_A2(0x3FF)
    NewScene("ED6_DT01/T2100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_206 end

    def Function_3_20A9(): pass

    label("Function_3_20A9")

    SetChrFlags(0xFE, 0x40)
    OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFDF30, 0x0, 0x186A0, 0x2710, 0x0)
    OP_8E(0xFE, 0xFFFFD634, 0x0, 0x15180, 0x2710, 0x0)

    def lambda_20EB():
        OP_6C(324000, 3000)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_20EB)

    def lambda_20FB():
        OP_67(0, 5200, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_20FB)

    def lambda_2113():
        OP_6D(-8000, 1300, 66400, 2700)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2113)
    ClearMapFlags(0x1)
    OP_8E(0xFE, 0xFFFFE0C0, 0x0, 0x11A08, 0x2EE0, 0x0)
    OP_8E(0xFE, 0xFFFFE7C8, 0x0, 0x10CC0, 0x2EE0, 0x0)
    OP_8E(0xFE, 0xFFFFEC14, 0x0, 0xFBF4, 0x32C8, 0x0)
    OP_8E(0xFE, 0xFFFFE7C8, 0x0, 0xE54C, 0x32C8, 0x0)
    OP_8E(0xFE, 0xFFFFDA80, 0x0, 0xBD74, 0x32C8, 0x0)
    Return()

    # Function_3_20A9 end

    def Function_4_218F(): pass

    label("Function_4_218F")

    SetChrFlags(0xFE, 0x40)
    OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFDF30, 0x0, 0x186A0, 0x2710, 0x0)
    OP_8E(0xFE, 0xFFFFD634, 0x0, 0x15180, 0x2AF8, 0x0)
    OP_8E(0xFE, 0xFFFFE0C0, 0x0, 0x11A08, 0x2EE0, 0x0)
    OP_8E(0xFE, 0xFFFFE7C8, 0x0, 0x10CC0, 0x2EE0, 0x0)
    OP_8E(0xFE, 0xFFFFEC14, 0x0, 0xFBF4, 0x2EE0, 0x0)
    OP_8E(0xFE, 0xFFFFE7C8, 0x0, 0xE54C, 0x2EE0, 0x0)
    OP_8E(0xFE, 0xFFFFDF30, 0x0, 0xC670, 0x2EE0, 0x0)
    Return()

    # Function_4_218F end

    def Function_5_2230(): pass

    label("Function_5_2230")

    OP_8E(0xFE, 0x0, 0x0, 0x20850, 0x2EE0, 0x0)
    OP_8E(0xFE, 0xFFFFDF30, 0x0, 0x186A0, 0x32C8, 0x0)
    OP_8E(0xFE, 0xFFFFD634, 0x0, 0x15180, 0x36B0, 0x0)
    OP_8E(0xFE, 0xFFFFE0C0, 0x0, 0x11A08, 0x3A98, 0x0)
    OP_44(0x8, 0x2)
    OP_44(0x8, 0x3)
    SetChrFlags(0xFE, 0x4)
    OP_22(0xA4, 0x0, 0x64)
    OP_96(0xFE, 0xFFFFE0C0, 0x5DC, 0x10360, 0x7D0, 0x1F40)

    def lambda_22AF():
        OP_6D(-7300, 0, 56400, 600)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_22AF)
    SetChrFlags(0xA, 0x20)
    SetChrChipByIndex(0xA, 2)

    def lambda_22D1():
        OP_99(0xA, 0x0, 0x3, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_22D1)

    def lambda_22E1():
        OP_6C(24000, 800)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_22E1)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_22F6():
        OP_96(0xFE, 0xFFFFE37C, 0x0, 0xDC50, 0x7D0, 0x1F40)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_22F6)
    WaitChrThread(0xA, 0x0)

    def lambda_2319():
        OP_99(0xA, 0x3, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_2319)
    OP_22(0x1F9, 0x0, 0x64)
    WaitChrThread(0xA, 0x3)
    OP_22(0x55, 0x0, 0x5A)
    PlayEffect(0x12, 0xFF, 0xFF, -6800, -2500, 55400, 0, 0, 0, 5000, 5000, 5000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    TurnDirection(0x8, 0xA, 0)
    TurnDirection(0x9, 0xA, 0)

    def lambda_2394():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2394)

    def lambda_23AA():
        OP_96(0xFE, 0xFFFFEA84, 0x0, 0xD5AC, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_23AA)
    WaitChrThread(0x9, 0x1)
    TurnDirection(0x9, 0xA, 400)

    def lambda_23D4():
        OP_94(0x1, 0xFE, 0xB4, 0x12C, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_23D4)
    WaitChrThread(0x8, 0x1)

    def lambda_23EF():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_23EF)
    OP_6A(0x0)
    ClearMapFlags(0x1)
    Return()

    # Function_5_2230 end

    def Function_6_2408(): pass

    label("Function_6_2408")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2454")
    OP_51(0xC, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_6_2408")

    label("loc_2454")

    Return()

    # Function_6_2408 end

    def Function_7_2455(): pass

    label("Function_7_2455")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2481")
    Sleep(100)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x64, 0x0)
    Sleep(100)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0xC8, 0x0)
    Jump("Function_7_2455")

    label("loc_2481")

    Return()

    # Function_7_2455 end

    def Function_8_2482(): pass

    label("Function_8_2482")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_24AE")
    Sleep(50)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x64, 0x0)
    Sleep(50)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0xC8, 0x0)
    Jump("Function_8_2482")

    label("loc_24AE")

    Return()

    # Function_8_2482 end

    def Function_9_24AF(): pass

    label("Function_9_24AF")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "北　卢安市\x01",
            "南　艾尔·雷登　１７５塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_9_24AF end

    SaveToFile()

Try(main)
