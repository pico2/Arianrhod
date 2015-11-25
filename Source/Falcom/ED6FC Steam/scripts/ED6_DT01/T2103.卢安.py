from ED6ScenarioHelper import *

def main():
    # 卢安

    CreateScenaFile(
        FileName            = 'T2103   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2103.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
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
        '戴尔蒙市长',                           # 9
        ' ',                                    # 10
        ' ',                                    # 11
        ' ',                                    # 12
        ' ',                                    # 13
        ' ',                                    # 14
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
        'ED6_DT07/CH02410 ._CH',             # 00
        'ED6_DT06/CH20083 ._CH',             # 01
        'ED6_DT07/CH00005 ._CH',             # 02
        'ED6_DT07/CH00015 ._CH',             # 03
        'ED6_DT07/CH00045 ._CH',             # 04
        'ED6_DT07/CH00107 ._CH',             # 05
        'ED6_DT07/CH00100 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH02410P._CP',             # 00
        'ED6_DT06/CH20083P._CP',             # 01
        'ED6_DT07/CH00005P._CP',             # 02
        'ED6_DT07/CH00015P._CP',             # 03
        'ED6_DT07/CH00045P._CP',             # 04
        'ED6_DT07/CH00107P._CP',             # 05
        'ED6_DT07/CH00100P._CP',             # 06
    )

    DeclNpc(
        X                   = 1200,
        Z                   = 4000,
        Y                   = 16700,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
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
        NpcIndex            = 0x180,
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
        NpcIndex            = 0x180,
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
        NpcIndex            = 0x180,
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
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_1A2",          # 00, 0
        "Function_1_1B3",          # 01, 1
        "Function_2_1B9",          # 02, 2
    )


    def Function_0_1A2(): pass

    label("Function_0_1A2")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FA)
    Event(0, 2)
    Return()

    # Function_0_1A2 end

    def Function_1_1B3(): pass

    label("Function_1_1B3")

    OP_22(0x1C4, 0x1, 0x64)
    Return()

    # Function_1_1B3 end

    def Function_2_1B9(): pass

    label("Function_2_1B9")

    EventBegin(0x0)
    OP_22(0xDA, 0x1, 0x64)
    LoadEffect(0x4, "map\\\\mp013_00.eff")
    LoadEffect(0x5, "map\\\\mp013_01.eff")
    PlayEffect(0x4, 0x4, 0xA, 0, 50, 2700, 180, 0, 0, 2500, 500, 10000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x9, 0, 50, 2400, 180, 0, 0, 1600, 500, 10000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xA, 0, -300, -3000, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0x9, 0, -300, -1800, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6D(27900, -2990, 4040, 0)
    OP_67(0, 5630, -10000, 0)
    OP_6B(1410, 0)
    OP_6C(270000, 0)
    OP_6E(713, 0)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x102, 0x20)
    SetChrFlags(0x105, 0x20)
    SetChrChipByIndex(0x101, 2)
    SetChrChipByIndex(0x102, 3)
    SetChrChipByIndex(0x105, 4)
    OP_89(0x101, 6290, -2000, -10, 270)
    OP_89(0x102, 8650, -2000, -420, 270)
    OP_89(0x105, 7180, -2000, 320, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x4)
    SetChrBattleFlags(0x8, 0x20)
    OP_89(0x8, -180, -2000, 370, 270)
    OP_72(0x0, 0x2)
    OP_71(0x0, 0x20)
    OP_71(0x0, 0x40)
    OP_6F(0x0, 301)
    OP_70(0x0, 0x168)
    OP_72(0x1, 0x2)
    OP_71(0x1, 0x20)
    OP_71(0x1, 0x40)
    OP_6F(0x1, 301)
    OP_70(0x1, 0x168)
    OP_A1(0xA, 0x0)
    OP_A1(0x9, 0x1)
    SetChrPos(0xA, 0, -2950, 0, 90)
    SetChrPos(0x9, 27900, -2990, 4040, 90)

    def lambda_3D6():
        OP_8F(0xFE, 0x2EFE, 0xFFFFF452, 0x3C0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3D6)

    def lambda_3F1():
        OP_6D(6770, -2990, 360, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F1)

    def lambda_409():
        OP_6C(225000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_409)
    Sleep(4600)

    def lambda_41E():
        OP_8F(0xFE, 0x2EFE, 0xFFFFF452, 0x3C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_41E)
    Sleep(200)

    def lambda_43E():
        OP_8F(0xFE, 0x2EFE, 0xFFFFF452, 0x3C0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_43E)
    Sleep(180)

    def lambda_45E():
        OP_8F(0xFE, 0x2EFE, 0xFFFFF452, 0x3C0, 0x640, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_45E)
    Sleep(160)

    def lambda_47E():
        OP_8F(0xFE, 0x2EFE, 0xFFFFF452, 0x3C0, 0x578, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_47E)
    Sleep(140)

    def lambda_49E():
        OP_8F(0xFE, 0x2EFE, 0xFFFFF452, 0x3C0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_49E)
    Sleep(120)

    def lambda_4BE():
        OP_8F(0xFE, 0x2EFE, 0xFFFFF452, 0x3C0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4BE)
    Sleep(100)

    def lambda_4DE():
        OP_8F(0xFE, 0x2EFE, 0xFFFFF452, 0x3C0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4DE)
    WaitChrThread(0x9, 0x1)

    ChrTalk(
        0x101,
        "#508F好～了，终于追上了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F因为我们坐的是小型艇，\x01",
            "船体比较轻。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_54B():
        OP_8C(0x8, 90, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_54B)

    def lambda_559():
        OP_6D(6770, -2990, 290, 3500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_559)

    def lambda_571():
        OP_6C(122000, 3500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_571)
    Sleep(1000)
    SetChrChipByIndex(0x8, 1)

    def lambda_58B():
        OP_8E(0x8, 0x64A, 0xFFFFF4F2, 0xB4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_58B)
    WaitChrThread(0x8, 0x1)

    ChrTalk(
        0x8,
        (
            "#666F呜……\x01",
            "真是缠人的家伙……\x02\x03",
            "#665F尝尝这个！\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x2, "map\\\\mp008_00.eff")
    SetChrChipByIndex(0x101, 65535)
    Sleep(100)
    SetChrChipByIndex(0x101, 6)
    Sleep(100)
    SetChrChipByIndex(0x101, 5)
    OP_22(0x7E, 0x1, 0x64)

    def lambda_612():

        label("loc_612")

        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        OP_48()
        Jump("loc_612")

    QueueWorkItem2(0x101, 0, lambda_612)
    SetChrPos(0xD, 9550, -1900, 1300, 0)
    PlayEffect(0x2, 0xFF, 0x8, 250, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xD, 0, 0, 0, 0)

    def lambda_66B():
        OP_6D(10040, -2600, 1040, 1300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_66B)

    def lambda_683():
        OP_6C(102000, 1300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_683)
    Sleep(250)
    SetChrPos(0xD, 9550, -1300, 1000, 0)
    PlayEffect(0x2, 0xFF, 0x8, 250, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xD, 0, 0, 0, 0)
    Sleep(250)
    Sleep(300)
    SetChrPos(0xD, 9550, -1500, 1600, 0)
    PlayEffect(0x2, 0xFF, 0x8, 250, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xD, 0, 0, 0, 0)
    Sleep(200)
    SetChrPos(0xD, 9550, -1900, 1300, 0)
    PlayEffect(0x2, 0xFF, 0x8, 250, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xD, 0, 0, 0, 0)
    Sleep(300)

    def lambda_77E():
        OP_6C(225000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_77E)
    SetChrPos(0xD, 9550, -1300, 1000, 0)
    PlayEffect(0x2, 0xFF, 0x8, 250, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xD, 0, 0, 0, 0)

    ChrTalk(
        0x101,
        "#005F#20A#3S喝啊！\x05\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(300)
    SetChrPos(0xD, 9550, -1500, 1600, 0)
    PlayEffect(0x2, 0xFF, 0x8, 250, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xD, 0, 0, 0, 0)
    Sleep(700)

    def lambda_84D():
        OP_6D(6660, -2990, 520, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_84D)
    OP_44(0x101, 0x0)
    OP_23(0x7E)
    OP_99(0x101, 0x0, 0x13, 0xBB8)
    Sleep(500)
    OP_99(0x101, 0x13, 0x8, 0xBB8)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 6)

    ChrTalk(
        0x8,
        "#668F什、什么！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#502F嘿嘿～\x01",
            "市长你太小看游击士了！\x02\x03",
            "#005F约修亚，\x01",
            "就这样从右边靠上去！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8F6():
        OP_94(0x1, 0xA, 0xB4, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_8F6)

    ChrTalk(
        0x102,
        (
            "#012F明白。\x02\x03",
            "#014F……咦？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_92C():
        OP_6D(4890, -2990, 200, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_92C)
    OP_22(0x96, 0x0, 0x64)

    def lambda_949():
        OP_94(0x1, 0x9, 0xB4, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_949)
    Sleep(250)

    def lambda_964():
        OP_94(0x1, 0x9, 0xB4, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_964)
    Sleep(250)
    OP_B0(0x0, 0x64)

    def lambda_983():
        OP_94(0x1, 0xA, 0xB4, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_983)

    def lambda_999():
        OP_94(0x1, 0x9, 0xB4, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_999)
    Sleep(200)

    def lambda_9B4():
        OP_94(0x1, 0x9, 0xB4, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9B4)

    def lambda_9CA():
        OP_94(0x1, 0xA, 0xB4, 0xBB8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_9CA)
    Sleep(300)

    def lambda_9E5():
        OP_94(0x1, 0xA, 0xB4, 0xBB8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_9E5)
    Sleep(200)

    def lambda_A00():
        OP_94(0x1, 0xA, 0xB4, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A00)
    Sleep(200)

    def lambda_A1B():
        OP_94(0x1, 0xA, 0xB4, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A1B)

    ChrTalk(
        0x101,
        "#580F怎、怎么忽然变快了！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#042F这是……\x01",
            "从海岸吹来的海风！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F糟了，\x01",
            "这下帆船就大占优势了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F你、你说什么～！？\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 0)

    ChrTalk(
        0x8,
        (
            "#667F哇哈哈！！\x01",
            "看来女神也向我这边微笑了啊！\x02\x03",
            "那么再见了，小丫头们！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B0E():
        OP_8C(0x8, 270, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B0E)
    OP_B0(0x0, 0x1E)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 240)
    OP_70(0x0, 0x12C)

    def lambda_B33():
        OP_94(0x1, 0xA, 0xB4, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B33)
    Sleep(200)

    def lambda_B4E():
        OP_94(0x1, 0xA, 0xB4, 0x7530, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B4E)
    Sleep(300)

    def lambda_B69():
        OP_94(0x1, 0xA, 0xB4, 0x7530, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B69)
    Sleep(300)

    def lambda_B84():
        OP_94(0x1, 0xA, 0xB4, 0x7530, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B84)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 301)
    OP_70(0x0, 0x168)

    def lambda_BB0():
        OP_94(0x1, 0xA, 0xB4, 0x4E20, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_BB0)
    Sleep(300)

    def lambda_BCB():
        OP_94(0x1, 0xA, 0xB4, 0x9C40, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_BCB)
    Sleep(300)

    def lambda_BE6():
        OP_94(0x1, 0xA, 0xB4, 0x9C40, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_BE6)
    Sleep(300)

    def lambda_C01():
        OP_94(0x1, 0xA, 0xB4, 0x9C40, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C01)
    Sleep(300)

    def lambda_C1C():
        OP_94(0x1, 0xA, 0xB4, 0x9C40, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C1C)
    Sleep(300)

    def lambda_C37():
        OP_94(0x1, 0xA, 0xB4, 0x9C40, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C37)

    ChrTalk(
        0x101,
        (
            "#005F开什么玩笑！\x01",
            "就只差那么一步了～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F这样下去恐怕只能\x01",
            "眼睁睁地看他远走高飞了……\x02\x03",
            "要是还有什么办法的话……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_CE5():
        OP_6D(11720, -2900, 1060, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CE5)
    SetChrPos(0xB, 60000, 2950, 2000, 270)
    SetChrChipByIndex(0x102, 65535)
    TurnDirection(0x102, 0xB, 800)
    Sleep(500)
    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0xB, 800)
    SetChrChipByIndex(0x105, 65535)
    TurnDirection(0x105, 0xB, 800)

    ChrTalk(
        0x101,
        "#580F什、什么……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#047F#1S……来了。\x02",
    )

    CloseMessageWindow()

    def lambda_D68():

        label("loc_D68")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_D68")

    QueueWorkItem2(0x101, 1, lambda_D68)

    def lambda_D79():

        label("loc_D79")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_D79")

    QueueWorkItem2(0x102, 1, lambda_D79)

    def lambda_D8A():

        label("loc_D8A")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_D8A")

    QueueWorkItem2(0x105, 1, lambda_D8A)
    OP_72(0x2, 0x4)
    OP_A1(0xB, 0x2)
    SetChrPos(0xB, 60000, 2950, 2000, 270)
    OP_22(0xDB, 0x0, 0x64)

    def lambda_DBB():
        OP_94(0x1, 0xB, 0x0, 0x186A0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_DBB)

    def lambda_DD1():
        OP_6B(2300, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_DD1)
    Sleep(3000)
    OP_20(0x7D0)
    FadeToDark(2000, 0, -1)
    OP_24(0xDA, 0x5F)
    Sleep(200)
    OP_24(0xDA, 0x5A)
    Sleep(200)
    OP_24(0xDA, 0x55)
    Sleep(200)
    OP_24(0xDA, 0x50)
    Sleep(200)
    OP_24(0xDA, 0x4B)
    Sleep(200)
    OP_24(0xDA, 0x46)
    Sleep(200)
    OP_24(0xDA, 0x41)
    Sleep(200)
    OP_23(0xDA)
    OP_0D()
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    FadeToBright(1000, 0)
    OP_6D(-33030, -2950, 110, 0)
    OP_67(0, 7310, -10000, 0)
    OP_6B(2280, 0)
    OP_6C(315000, 0)
    OP_6E(710, 0)
    OP_82(0x3, 0x0)
    OP_44(0xA, 0xFF)
    SetChrPos(0xA, -33030, -2950, 110, 90)
    OP_44(0xB, 0xFF)
    SetChrPos(0xB, 34720, 0, 18480, 270)
    SetChrPos(0xC, 34720, 30000, 18480, 270)
    OP_22(0xDA, 0x1, 0x64)
    OP_24(0xDA, 0x41)
    Sleep(100)
    OP_24(0xDA, 0x46)
    Sleep(100)
    OP_24(0xDA, 0x4B)
    Sleep(100)
    OP_24(0xDA, 0x50)
    Sleep(100)
    OP_24(0xDA, 0x55)
    Sleep(100)
    OP_24(0xDA, 0x5A)
    Sleep(100)
    OP_24(0xDA, 0x5F)
    Sleep(100)
    OP_24(0xDA, 0x64)
    OP_0D()
    OP_B0(0x3, 0x1E)
    OP_72(0x3, 0x4)
    OP_A1(0xC, 0x3)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 900)
    OP_70(0x3, 0x514)
    OP_B0(0x3, 0x3C)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x40)

    ChrTalk(
        0x8,
        (
            "#664F呀，总算逃出来了。\x01",
            "不过从今往后该怎么办呢……\x02\x03",
            "果然，唯有在军队插手之前，\x01",
            "尽早逃到帝国去吧。\x02\x03",
            "#667F算了，只要稍微忍耐一阵，\x01",
            "『他』肯定会帮我想办法的……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xB, 400)
    OP_22(0x79, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0x65)

    def lambda_1017():

        label("loc_1017")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_1017")

    QueueWorkItem2(0x8, 1, lambda_1017)
    SetChrPos(0xB, 28720, 0, 18000, 270)
    SetChrPos(0xC, 34720, 15000, 18000, 270)
    SetChrPos(0x9, 300000, 300000, 300000, 0)

    def lambda_105B():
        OP_8F(0xB, 0xFFFFB5C8, 0xFFFFF4AC, 0x4650, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_105B)

    def lambda_1076():
        OP_8F(0xC, 0xFFFFCD38, 0x3A98, 0x4650, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1076)

    def lambda_1091():
        OP_6D(-31420, -2990, 9180, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1091)

    def lambda_10A9():
        OP_67(0, 11900, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10A9)

    def lambda_10C1():
        OP_6C(270000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10C1)

    def lambda_10D1():
        OP_6B(3210, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_10D1)
    Sleep(2200)

    def lambda_10E6():
        OP_8F(0xB, 0xFFFFB5C8, 0xFFFFF4AC, 0x4650, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_10E6)

    def lambda_1101():
        OP_8F(0xC, 0xFFFFCD38, 0x3A98, 0x4650, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1101)
    Sleep(300)

    def lambda_1121():
        OP_8F(0xB, 0xFFFFB5C8, 0xFFFFF4AC, 0x4650, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1121)

    def lambda_113C():
        OP_8F(0xC, 0xFFFFCD38, 0x3A98, 0x4650, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_113C)
    Sleep(300)

    def lambda_115C():
        OP_8F(0xB, 0xFFFFB5C8, 0xFFFFF4AC, 0x4650, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_115C)

    def lambda_1177():
        OP_8F(0xC, 0xFFFFCD38, 0x3A98, 0x4650, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1177)
    Sleep(300)

    def lambda_1197():
        OP_8F(0xB, 0xFFFFB5C8, 0xFFFFF4AC, 0x4650, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1197)

    def lambda_11B2():
        OP_8F(0xC, 0xFFFFCD38, 0x3A98, 0x4650, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_11B2)
    Sleep(300)

    def lambda_11D2():
        OP_8F(0xB, 0xFFFFB5C8, 0xFFFFF4AC, 0x4650, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_11D2)

    def lambda_11ED():
        OP_8F(0xC, 0xFFFFCD38, 0x3A98, 0x4650, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_11ED)
    Sleep(300)

    def lambda_120D():
        OP_8F(0xB, 0xFFFFB5C8, 0xFFFFF4AC, 0x4650, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_120D)

    def lambda_1228():
        OP_8F(0xC, 0xFFFFCD38, 0x3A98, 0x4650, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1228)
    Sleep(300)

    def lambda_1248():
        OP_8F(0xB, 0xFFFFB5C8, 0xFFFFF4AC, 0x4650, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1248)

    def lambda_1263():
        OP_8F(0xC, 0xFFFFCD38, 0x3A98, 0x4650, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1263)
    Sleep(300)

    def lambda_1283():
        OP_8F(0xB, 0xFFFFB5C8, 0xFFFFF4AC, 0x4650, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1283)

    def lambda_129E():
        OP_8F(0xC, 0xFFFFCD38, 0x3A98, 0x4650, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_129E)
    Sleep(300)

    def lambda_12BE():
        OP_8F(0xB, 0xFFFFB5C8, 0xFFFFF4AC, 0x4650, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_12BE)

    def lambda_12D9():
        OP_8F(0xC, 0xFFFFCD38, 0x3A98, 0x4650, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_12D9)
    Sleep(300)

    def lambda_12F9():
        OP_8F(0xB, 0xFFFFB5C8, 0xFFFFF4AC, 0x4650, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_12F9)

    def lambda_1314():
        OP_8F(0xC, 0xFFFFCD38, 0x3A98, 0x4650, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1314)
    Sleep(300)

    def lambda_1334():
        OP_8F(0xB, 0xFFFFB5C8, 0xFFFFF4AC, 0x4650, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1334)

    def lambda_134F():
        OP_8F(0xC, 0xFFFFCD38, 0x3A98, 0x4650, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_134F)
    Sleep(300)

    def lambda_136F():
        OP_8F(0xB, 0xFFFFB5C8, 0xFFFFF4AC, 0x4650, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_136F)

    def lambda_138A():
        OP_8F(0xC, 0xFFFFCD38, 0x3A98, 0x4650, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_138A)

    ChrTalk(
        0x8,
        "#668F#3S什、什、什么————！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_13DC():
        OP_6D(-39220, -2900, 9180, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13DC)

    def lambda_13F4():
        OP_8F(0xB, 0xFFFF7540, 0xFFFFF4AC, 0x4650, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_13F4)

    def lambda_140F():
        OP_8F(0xC, 0xFFFF7D10, 0x2710, 0x4650, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_140F)
    Sleep(300)

    def lambda_142F():
        OP_8F(0xB, 0xFFFF7540, 0xFFFFF4AC, 0x4650, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_142F)

    def lambda_144A():
        OP_8F(0xC, 0xFFFF7D10, 0x2710, 0x4650, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_144A)
    OP_72(0x3, 0x20)
    OP_B0(0x3, 0x1E)
    OP_6F(0x3, 1300)
    OP_70(0x3, 0x604)
    Sleep(300)

    def lambda_1481():
        OP_8F(0xB, 0xFFFF7540, 0xFFFFF4AC, 0x4650, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1481)

    def lambda_149C():
        OP_8F(0xC, 0xFFFF7D10, 0x2710, 0x4650, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_149C)
    Sleep(300)

    def lambda_14BC():
        OP_8F(0xB, 0xFFFF7540, 0xFFFFF4AC, 0x4650, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_14BC)

    def lambda_14D7():
        OP_8F(0xC, 0xFFFF7D10, 0x2710, 0x4650, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_14D7)
    Sleep(300)

    def lambda_14F7():
        OP_8F(0xB, 0xFFFF7540, 0xFFFFF4AC, 0x4650, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_14F7)

    def lambda_1512():
        OP_8F(0xC, 0xFFFF7D10, 0x2710, 0x4650, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1512)
    WaitChrThread(0xC, 0x1)

    def lambda_1532():
        OP_67(0, 7250, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1532)

    def lambda_154A():
        OP_6D(-35670, 4660, 3490, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_154A)

    def lambda_1562():
        OP_6C(179000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1562)

    def lambda_1572():
        OP_8C(0xFE, 180, 2)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1572)

    def lambda_1580():
        OP_8C(0xFE, 180, 2)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1580)

    def lambda_158E():
        OP_97(0xB, 0xFFFF7540, 0x0, 0xFFFEA070, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_158E)

    def lambda_15AA():
        OP_97(0xC, 0xFFFF7D10, 0x0, 0xFFFEA070, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_15AA)

    def lambda_15C6():
        OP_94(0x1, 0xA, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_15C6)
    Sleep(150)

    def lambda_15E1():
        OP_8C(0xFE, 180, 7)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_15E1)

    def lambda_15EF():
        OP_8C(0xFE, 180, 7)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_15EF)
    OP_B0(0x3, 0x1E)
    OP_6F(0x3, 1540)
    OP_70(0x3, 0x640)
    Sleep(150)

    def lambda_1614():
        OP_8C(0xFE, 180, 11)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1614)

    def lambda_1622():
        OP_8C(0xFE, 180, 11)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1622)

    def lambda_1630():
        OP_97(0xB, 0xFFFF7540, 0x0, 0xFFFEA070, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1630)

    def lambda_164C():
        OP_97(0xC, 0xFFFF7D10, 0x0, 0xFFFEA070, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_164C)

    def lambda_1668():
        OP_94(0x1, 0xA, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1668)
    Sleep(200)

    def lambda_1683():
        OP_8C(0xFE, 180, 16)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1683)

    def lambda_1691():
        OP_8C(0xFE, 180, 16)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1691)
    Sleep(200)

    def lambda_16A4():
        OP_8C(0xFE, 180, 22)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_16A4)

    def lambda_16B2():
        OP_8C(0xFE, 180, 22)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_16B2)

    def lambda_16C0():
        OP_97(0xB, 0xFFFF7540, 0x0, 0xFFFEA070, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_16C0)

    def lambda_16DC():
        OP_97(0xC, 0xFFFF7D10, 0x0, 0xFFFEA070, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_16DC)

    def lambda_16F8():
        OP_94(0x1, 0xA, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_16F8)
    Sleep(400)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 1595)
    OP_70(0x3, 0x640)

    def lambda_1726():
        OP_8C(0xFE, 180, 22)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1726)

    def lambda_1734():
        OP_8C(0xFE, 180, 22)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1734)

    def lambda_1742():
        OP_97(0xB, 0xFFFF7540, 0x0, 0xFFFEA070, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1742)

    def lambda_175E():
        OP_97(0xC, 0xFFFF7D10, 0x0, 0xFFFEA070, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_175E)

    def lambda_177A():
        OP_94(0x1, 0xA, 0x0, 0x1388, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_177A)
    Sleep(400)

    def lambda_1795():
        OP_8C(0xFE, 180, 22)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1795)

    def lambda_17A3():
        OP_8C(0xFE, 180, 22)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_17A3)

    def lambda_17B1():
        OP_97(0xB, 0xFFFF7540, 0x0, 0xFFFEA070, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_17B1)

    def lambda_17CD():
        OP_97(0xC, 0xFFFF7D10, 0x0, 0xFFFEA070, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_17CD)

    def lambda_17E9():
        OP_94(0x1, 0xA, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_17E9)
    Sleep(400)

    def lambda_1804():
        OP_8C(0xFE, 180, 22)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1804)

    def lambda_1812():
        OP_8C(0xFE, 180, 22)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1812)

    def lambda_1820():
        OP_97(0xB, 0xFFFF7540, 0x0, 0xFFFEA070, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1820)

    def lambda_183C():
        OP_97(0xC, 0xFFFF7D10, 0x0, 0xFFFEA070, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_183C)

    def lambda_1858():
        OP_94(0x1, 0xA, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1858)
    Sleep(400)

    def lambda_1873():
        OP_8C(0xFE, 180, 22)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1873)

    def lambda_1881():
        OP_8C(0xFE, 180, 22)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1881)

    def lambda_188F():
        OP_97(0xB, 0xFFFF7540, 0x0, 0xFFFEA070, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_188F)

    def lambda_18AB():
        OP_97(0xC, 0xFFFF7D10, 0x0, 0xFFFEA070, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_18AB)

    def lambda_18C7():
        OP_94(0x1, 0xA, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_18C7)
    Sleep(400)

    def lambda_18E2():
        OP_8C(0xFE, 180, 22)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_18E2)

    def lambda_18F0():
        OP_8C(0xFE, 180, 22)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_18F0)

    def lambda_18FE():
        OP_97(0xB, 0xFFFF7540, 0x0, 0xFFFEA070, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_18FE)

    def lambda_191A():
        OP_97(0xC, 0xFFFF7D10, 0x0, 0xFFFEA070, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_191A)

    def lambda_1936():
        OP_94(0x1, 0xA, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1936)
    Sleep(300)

    def lambda_1951():
        OP_8C(0xFE, 180, 22)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1951)

    def lambda_195F():
        OP_8C(0xFE, 180, 22)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_195F)

    def lambda_196D():
        OP_97(0xB, 0xFFFF7540, 0x0, 0xFFFEA070, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_196D)

    def lambda_1989():
        OP_97(0xC, 0xFFFF7D10, 0x0, 0xFFFEA070, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1989)

    def lambda_19A5():
        OP_94(0x1, 0xA, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_19A5)
    Sleep(200)

    def lambda_19C0():
        OP_8C(0xFE, 180, 22)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_19C0)

    def lambda_19CE():
        OP_8C(0xFE, 180, 22)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_19CE)

    def lambda_19DC():
        OP_97(0xB, 0xFFFF7540, 0x0, 0xFFFEA070, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_19DC)

    def lambda_19F8():
        OP_97(0xC, 0xFFFF7D10, 0x0, 0xFFFEA070, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_19F8)

    def lambda_1A14():
        OP_94(0x1, 0xA, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1A14)
    Sleep(100)

    def lambda_1A2F():
        OP_8C(0xFE, 180, 22)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1A2F)

    def lambda_1A3D():
        OP_8C(0xFE, 180, 22)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1A3D)

    def lambda_1A4B():
        OP_97(0xB, 0xFFFF7540, 0x0, 0xFFFEA070, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1A4B)

    def lambda_1A67():
        OP_97(0xC, 0xFFFF7D10, 0x0, 0xFFFEA070, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1A67)

    def lambda_1A83():
        OP_94(0x1, 0xA, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1A83)
    Sleep(100)

    def lambda_1A9E():
        OP_97(0xB, 0xFFFF7540, 0x0, 0xFFFEA070, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1A9E)

    def lambda_1ABA():
        OP_97(0xC, 0xFFFF7D10, 0x0, 0xFFFEA070, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1ABA)

    def lambda_1AD6():
        OP_94(0x1, 0xA, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1AD6)
    Sleep(100)

    def lambda_1AF1():
        OP_97(0xB, 0xFFFF7540, 0x0, 0xFFFEA070, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1AF1)

    def lambda_1B0D():
        OP_97(0xC, 0xFFFF7D10, 0x0, 0xFFFEA070, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1B0D)
    Sleep(200)
    OP_44(0xC, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xA, 0x1)
    OP_72(0x3, 0x20)
    OP_6F(0x3, 1600)
    OP_70(0x3, 0x686)

    ChrTalk(
        0x8,
        "#668F#10A#5P什、什、什……\x05\x02",
    )


    def lambda_1B6D():
        OP_6D(46000, -2990, -4059, 8100)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B6D)

    def lambda_1B85():
        OP_91(0xFE, 0x7530, 0x0, 0x0, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_1B85)

    def lambda_1BA0():
        OP_91(0xFE, 0x7530, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_1BA0)

    def lambda_1BBB():
        OP_91(0xFE, 0x7530, 0xFFFFD8F0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_1BBB)
    Sleep(200)

    def lambda_1BDB():
        OP_91(0xFE, 0x7530, 0x0, 0x0, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_1BDB)

    def lambda_1BF6():
        OP_91(0xFE, 0x7530, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_1BF6)

    def lambda_1C11():
        OP_91(0xFE, 0x7530, 0xFFFFD8F0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_1C11)
    Sleep(200)

    def lambda_1C31():
        OP_91(0xFE, 0x7530, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_1C31)

    def lambda_1C4C():
        OP_91(0xFE, 0x7530, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_1C4C)

    def lambda_1C67():
        OP_91(0xFE, 0x7530, 0xFFFFD8F0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_1C67)
    Sleep(200)

    def lambda_1C87():
        OP_91(0xFE, 0x7530, 0x0, 0x0, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_1C87)

    def lambda_1CA2():
        OP_91(0xFE, 0x7530, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_1CA2)

    def lambda_1CBD():
        OP_91(0xFE, 0x7530, 0xFFFFD8F0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_1CBD)
    Sleep(200)

    def lambda_1CDD():
        OP_91(0xFE, 0x7530, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_1CDD)

    def lambda_1CF8():
        OP_91(0xFE, 0x7530, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_1CF8)

    def lambda_1D13():
        OP_91(0xFE, 0x7530, 0xFFFFD8F0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_1D13)
    Sleep(200)

    def lambda_1D33():
        OP_91(0xFE, 0x7530, 0x0, 0x0, 0xAF0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_1D33)

    def lambda_1D4E():
        OP_91(0xFE, 0x7530, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_1D4E)

    def lambda_1D69():
        OP_91(0xFE, 0x7530, 0xFFFFD8F0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_1D69)
    Sleep(200)

    def lambda_1D89():
        OP_91(0xFE, 0x7530, 0x0, 0x0, 0xE95, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_1D89)

    def lambda_1DA4():
        OP_91(0xFE, 0x7530, 0x0, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_1DA4)

    def lambda_1DBF():
        OP_91(0xFE, 0x7530, 0xFFFFD8F0, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_1DBF)
    Sleep(200)

    def lambda_1DDF():
        OP_91(0xFE, 0x7530, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_1DDF)

    def lambda_1DFA():
        OP_91(0xFE, 0x7530, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_1DFA)

    def lambda_1E15():
        OP_91(0xFE, 0x7530, 0xFFFFD8F0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_1E15)
    Sleep(200)

    def lambda_1E35():
        OP_91(0xFE, 0x7530, 0x0, 0x0, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_1E35)

    def lambda_1E50():
        OP_91(0xFE, 0x7530, 0xFFFFD8F0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_1E50)
    Sleep(200)

    def lambda_1E70():
        OP_91(0xFE, 0x7530, 0x0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_1E70)

    def lambda_1E8B():
        OP_91(0xFE, 0x7530, 0xFFFFD8F0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_1E8B)
    OP_B0(0x3, 0x1E)
    OP_6F(0x3, 1670)
    OP_70(0x3, 0x708)

    def lambda_1EB8():
        OP_8C(0xFE, 180, 33)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1EB8)
    OP_82(0x4, 0x2)
    PlayEffect(0x4, 0x5, 0xA, 0, 0, 2300, 180, 0, 0, 2000, 100, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(500)

    ChrTalk(
        0x8,
        "#668F#10A#5P呜哇啊啊啊啊！！\x05\x02",
    )

    OP_B0(0x0, 0xC8)
    OP_23(0xDA)
    OP_23(0xDC)
    OP_22(0xDC, 0x0, 0x64)
    LoadEffect(0x0, "map\\\\mpsibuk.eff")
    PlayEffect(0x0, 0xFF, 0xC, 3600, 0, 22870, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, 5550, 0, 18820, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, 9480, 0, 16660, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, 8470, 0, 11180, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, 5930, 0, 13690, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, 5590, 0, 8880, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, 9170, 0, 6400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, 11620, 0, 3140, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, 11760, 0, -2390, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, 11440, 0, -6800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, 9040, 0, -10280, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, 4730, 0, -11890, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, 5560, 0, -17380, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, -3600, 0, 22870, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, -5550, 0, 18820, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, -9480, 0, 16660, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, -8470, 0, 11180, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, -5930, 0, 13690, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, -5590, 0, 8880, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, -9170, 0, 6400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, -11620, 0, 3140, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, -11760, 0, -2390, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, -11440, 0, -6800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, -9040, 0, -10280, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, -4730, 0, -11890, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xC, -5560, 0, -17380, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x12C, 0x1388, 0x7D0)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xC, 0x4)
    Sleep(500)

    def lambda_24C9():
        OP_91(0xFE, 0x493E0, 0xFFFF8AD0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_24C9)

    def lambda_24E4():
        OP_91(0xFE, 0x493E0, 0xFFFF8AD0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_24E4)

    def lambda_24FF():
        OP_91(0xFE, 0x493E0, 0x0, 0x0, 0x4C2C, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_24FF)
    Sleep(150)

    def lambda_251F():
        OP_91(0xFE, 0x493E0, 0x0, 0x0, 0x4A38, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_251F)
    Sleep(150)

    def lambda_253F():
        OP_91(0xFE, 0x493E0, 0x0, 0x0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_253F)
    Sleep(150)

    def lambda_255F():
        OP_91(0xFE, 0x493E0, 0x0, 0x0, 0x4268, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_255F)
    Sleep(150)

    def lambda_257F():
        OP_91(0xFE, 0x493E0, 0x0, 0x0, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_257F)
    Sleep(150)

    def lambda_259F():
        OP_91(0xFE, 0x493E0, 0x0, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_259F)
    Sleep(150)

    def lambda_25BF():
        OP_91(0xFE, 0x493E0, 0x0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_25BF)
    Sleep(900)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2104   ._SN", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1B9 end

    SaveToFile()

Try(main)
