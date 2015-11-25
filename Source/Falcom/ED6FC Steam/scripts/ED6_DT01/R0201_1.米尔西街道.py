from ED6ScenarioHelper import *

def main():
    # 米尔西街道

    CreateScenaFile(
        FileName            = 'R0201_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T0131.x',
        MapIndex            = 22,
        MapDefaultBGM       = "ed60020",
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

    ScpFunction(
        "Function_0_66",           # 00, 0
        "Function_1_5B1",          # 01, 1
        "Function_2_BA1",          # 02, 2
        "Function_3_F4F",          # 03, 3
        "Function_4_1833",         # 04, 4
        "Function_5_1BA5",         # 05, 5
        "Function_6_1BAF",         # 06, 6
        "Function_7_1C03",         # 07, 7
        "Function_8_1C57",         # 08, 8
        "Function_9_1CAB",         # 09, 9
        "Function_10_1CFF",        # 0A, 10
        "Function_11_1D26",        # 0B, 11
        "Function_12_1D4D",        # 0C, 12
        "Function_13_1D75",        # 0D, 13
        "Function_14_1D99",        # 0E, 14
        "Function_15_1DBD",        # 0F, 15
        "Function_16_1DE5",        # 10, 16
        "Function_17_1E06",        # 11, 17
    )


    def Function_0_66(): pass

    label("Function_0_66")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    SetMapFlags(0x8000000)
    Fade(1000)
    OP_6C(260000, 0)

    def lambda_86():
        OP_6B(2500, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_86)
    SetChrPos(0x101, -205210, 0, -19200, 135)
    SetChrPos(0x102, -206190, 20, -20420, 135)
    OP_6D(-205750, 20, -20780, 3000)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#000F根据佛莱迪叔叔所说的，\x01",
            "我想大概就是这个路灯吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我也是这么想的。\x02\x03",
            "#010F外面的面板上\x01",
            "也写着『６号路灯』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F啊，果然。\x02\x03",
            "好～的，\x01",
            "我们赶快把它弄好收工吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    OP_8C(0x102, 180, 400)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#012F……很可惜，\x01",
            "好像不会那么顺利。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#004F……哎？\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x8, -202100, 0, -35820, 0)
    SetChrPos(0x9, -199870, 1000, -36700, 0)
    SetChrPos(0xA, -197980, 0, -35450, 0)
    SetChrPos(0xB, -196350, 0, -33810, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)

    def lambda_245():
        OP_90(0x8, 0xFFFFFC18, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_245)
    Sleep(150)

    def lambda_265():
        OP_90(0x9, 0xFFFFFC18, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_265)
    Sleep(100)

    def lambda_285():
        OP_90(0xA, 0xFFFFFC18, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_285)
    Sleep(120)

    def lambda_2A5():
        OP_90(0xB, 0xFFFFFC18, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2A5)

    def lambda_2C0():
        OP_6C(225000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2C0)

    def lambda_2D0():
        OP_6D(-202310, 0, -28900, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_2D0)
    WaitChrThread(0x8, 0x1)
    SetChrChipByIndex(0x8, 8)
    OP_43(0x8, 0x0, 0x0, 0x2)

    def lambda_2F9():

        label("loc_2F9")

        TurnDirection(0x8, 0x101, 0)
        OP_48()
        Jump("loc_2F9")

    QueueWorkItem2(0x8, 1, lambda_2F9)
    WaitChrThread(0x9, 0x1)
    SetChrChipByIndex(0x9, 8)
    OP_43(0x9, 0x0, 0x0, 0x2)

    def lambda_31B():

        label("loc_31B")

        TurnDirection(0x9, 0x101, 0)
        OP_48()
        Jump("loc_31B")

    QueueWorkItem2(0x9, 1, lambda_31B)
    WaitChrThread(0xA, 0x1)
    SetChrChipByIndex(0xA, 8)
    OP_43(0xA, 0x0, 0x0, 0x2)

    def lambda_33D():

        label("loc_33D")

        TurnDirection(0xA, 0x101, 0)
        OP_48()
        Jump("loc_33D")

    QueueWorkItem2(0xA, 1, lambda_33D)
    WaitChrThread(0xB, 0x1)
    SetChrChipByIndex(0xB, 8)
    OP_43(0xB, 0x0, 0x0, 0x2)

    def lambda_35F():

        label("loc_35F")

        TurnDirection(0xB, 0x101, 0)
        OP_48()
        Jump("loc_35F")

    QueueWorkItem2(0xB, 1, lambda_35F)
    WaitChrThread(0x0, 0x1)
    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xD, 0x8)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrPos(0xC, -206450, 50, -21160, 141)
    SetChrPos(0xD, -206450, 50, -21160, 141)
    SetChrFlags(0xD, 0x1000)
    SetChrFlags(0xC, 0x1000)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrChipByIndex(0xD, 5)
    SetChrChipByIndex(0xC, 4)

    def lambda_3D3():
        OP_8E(0xD, 0xFFFCE06E, 0xFFFFFFBA, 0xFFFF9EC6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3D3)
    OP_8E(0xC, 0xFFFCE4A6, 0xFFFFFFE2, 0xFFFFA060, 0x1388, 0x0)
    WaitChrThread(0xD, 0x1)
    OP_8C(0xD, 180, 0)
    OP_8C(0xC, 180, 0)
    SetChrChipByIndex(0xD, 7)
    SetChrChipByIndex(0xC, 6)
    OP_6D(-202010, 10, -26160, 1000)

    ChrTalk(
        0xC,
        "#002F怎、怎么会有这么多魔兽！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#012F应该是由于\x01",
            "导力灯的故障而被引来的。\x02\x03",
            "#012F总而言之，如果不击退它们，\x01",
            "是没法安心更换导力灯的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#002F嗯，对，没错。\x02\x03",
            "那么……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58B")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【魔兽就交给我来解决！】\x01",        # 0
            "【魔兽就交给约修亚你了！】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_560"),
        (1, "loc_574"),
        (SWITCH_DEFAULT, "loc_588"),
    )


    label("loc_560")

    Call(1, 1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_588")

    label("loc_574")

    Call(1, 2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_588")

    label("loc_588")

    Jump("loc_4DA")

    label("loc_58B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_64(0x0, 0x1)
    OP_28(0x6, 0x1, 0x8)
    ClearChrFlags(0x102, 0x40)
    ClearChrFlags(0x101, 0x40)
    EventEnd(0x0)
    ClearMapFlags(0x8000000)
    Return()

    # Function_0_66 end

    def Function_1_5B1(): pass

    label("Function_1_5B1")

    RemoveParty(0x1, 0x0)

    ChrTalk(
        0xC,
        "#002F魔兽就交给我来解决！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#012F明白。\x02\x03",
            "我去打开控电盘的时候，\x01",
            "其他的就拜托你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#005F嗯！交给我吧！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xD, 18)
    SetChrChipByIndex(0xC, 4)
    SetChrChipByIndex(0x8, 9)
    SetChrChipByIndex(0x9, 9)
    SetChrChipByIndex(0xA, 9)
    SetChrChipByIndex(0xB, 9)

    def lambda_64C():
        OP_92(0x8, 0x101, 0x11F8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_64C)

    def lambda_661():
        OP_92(0x9, 0x101, 0x11F8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_661)

    def lambda_676():
        OP_92(0xA, 0x101, 0x11F8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_676)

    def lambda_68B():
        OP_92(0xB, 0x101, 0x11F8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_68B)

    def lambda_6A0():
        OP_8E(0xD, 0xFFFCDB64, 0x3C, 0xFFFFABA0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6A0)
    OP_8E(0xC, 0xFFFCE82A, 0x0, 0xFFFF9868, 0x1770, 0x0)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x3EB, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_703"),
        (SWITCH_DEFAULT, "loc_708"),
    )


    label("loc_703")

    OP_B4(0x0)
    Jump("loc_708")

    label("loc_708")

    EventBegin(0x0)
    OP_1D(0x14)
    AddParty(0x1, 0x1)
    OP_6D(-203550, -30, -24610, 0)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x101, 0x8)
    SetChrChipByIndex(0x101, 6)
    SetChrPos(0x101, -202010, 10, -26160, 180)
    SetChrPos(0x102, -204100, 0, -20750, 180)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        "#002F哼，知道我的厉害了吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F（……很厉害啊。）\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#002F约修亚！\x01",
            "你那边的情况如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F现在正在输入解锁密码。\x02\x03",
            "嗯……\x01",
            "５·４·４·８·１·８……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F我这边没问题了，\x01",
            "放心去弄吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    OP_22(0x83, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x102,
        (
            "#012F……好的，打开了。\x02\x03",
            "接下来是更换导力器……\x02",
        )
    )

    CloseMessageWindow()
    OP_3F(0x327, 1)

    ChrTalk(
        0x101,
        (
            "#502F嘿嘿嘿嘿，\x01",
            "我的斗志正在燃烧～～～\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 6)
    OP_8C(0x101, 0, 400)
    OP_8C(0x101, 45, 400)
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    OP_22(0x7E, 0x1, 0x64)
    SetChrChipByIndex(0x101, 16)

    def lambda_905():

        label("loc_905")

        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        OP_48()
        Jump("loc_905")

    QueueWorkItem2(0x101, 0, lambda_905)

    def lambda_918():
        OP_6D(-202010, 10, -26160, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_918)
    SetChrFlags(0x102, 0x40)

    def lambda_935():
        OP_8E(0x102, 0xFFFCE64A, 0xFFFFFFF6, 0xFFFFAF2E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_935)
    WaitChrThread(0x102, 0x1)

    def lambda_955():
        OP_8E(0x102, 0xFFFCEC44, 0xFFFFFFE2, 0xFFFFA7F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_955)
    WaitChrThread(0x102, 0x1)

    def lambda_975():
        OP_92(0x102, 0x101, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_975)
    OP_23(0x7E)
    OP_44(0x101, 0x0)
    SetChrChipByIndex(0x101, 6)
    OP_8C(0x101, 180, 400)
    WaitChrThread(0x102, 0x1)

    ChrTalk(
        0x101,
        "#005F出来吧！你们这些魔兽！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)

    ChrTalk(
        0x102,
        (
            "#010F久等了，艾丝蒂尔。\x01",
            "已经完成了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(800)
    Sleep(400)
    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0x102, 400)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#000F……啊？\x02\x03",
            "#004F咦？已经完成了……\x02\x03",
            "难道连导力器\x01",
            "也已经更换好了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F嗯，这样就不会再有魔兽来袭了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 45, 400)
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        "#007F唉，这样就结束了啊。\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x102)

    ChrTalk(
        0x102,
        (
            "#018F……………………\x02\x03",
            "怎么觉得你好像\x01",
            "有点意犹未尽的样子。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#506F哈、哈哈哈☆\x02\x03",
            "错、错觉啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F真是的，艾丝蒂尔你啊……\x02",
    )

    CloseMessageWindow()
    OP_2B(0x6, 0x1)
    Sleep(400)
    Return()

    # Function_1_5B1 end

    def Function_2_BA1(): pass

    label("Function_2_BA1")

    RemoveParty(0x0, 0x0)

    ChrTalk(
        0xC,
        "#002F魔兽就交给约修亚你了！\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0xD,
        "#014F艾丝蒂尔，这样没问题吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#009F真是的～别担心那么多啦。\x02\x03",
            "更换导力器这种小事，\x01",
            "对我来说简直是轻而易举啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#012F明白。\x02\x03",
            "那么，路灯就拜托你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#005F嗯！交给我吧！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xD, 5)
    SetChrChipByIndex(0xC, 17)
    SetChrChipByIndex(0x8, 9)
    SetChrChipByIndex(0x9, 9)
    SetChrChipByIndex(0xA, 9)
    SetChrChipByIndex(0xB, 9)

    def lambda_CBE():
        OP_92(0x8, 0x101, 0x11F8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_CBE)

    def lambda_CD3():
        OP_92(0x9, 0x101, 0x11F8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_CD3)

    def lambda_CE8():
        OP_92(0xA, 0x101, 0x11F8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_CE8)

    def lambda_CFD():
        OP_92(0xB, 0x101, 0x11F8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_CFD)

    def lambda_D12():
        OP_8E(0xC, 0xFFFCDB64, 0x3C, 0xFFFFABA0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_D12)
    OP_8E(0xD, 0xFFFCE82A, 0x0, 0xFFFF9868, 0x1770, 0x0)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x3EB, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_D75"),
        (SWITCH_DEFAULT, "loc_D7A"),
    )


    label("loc_D75")

    OP_B4(0x0)
    Jump("loc_D7A")

    label("loc_D7A")

    EventBegin(0x0)
    OP_1D(0x14)
    AddParty(0x0, 0x0)
    OP_6D(-203550, -30, -24610, 0)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x101, 0x8)
    SetChrChipByIndex(0x102, 7)
    SetChrPos(0x102, -202010, 10, -26160, 180)
    SetChrPos(0x101, -204100, 0, -20750, 180)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xC, 0x80)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x102,
        "#012F……这样就算解决了吧。\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    SetChrChipByIndex(0x102, 65535)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F艾丝蒂尔，\x01",
            "你那边的情况如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F正在开始输入控电盘的解锁密码。\x01",
            "　\x02\x03",
            "#505F嗯～～\x01",
            "正确的密码是……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E8B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F3F")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【５４５８１８】\x01",      # 0
            "【５５４８１８】\x01",      # 1
            "【５４４８１８】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_F14"),
        (1, "loc_F1E"),
        (2, "loc_F28"),
        (SWITCH_DEFAULT, "loc_F3C"),
    )


    label("loc_F14")

    Call(1, 3)
    OP_5F(0x0)
    Jump("loc_F3C")

    label("loc_F1E")

    Call(1, 3)
    OP_5F(0x0)
    Jump("loc_F3C")

    label("loc_F28")

    Call(1, 4)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_F3C")

    label("loc_F3C")

    Jump("loc_E8B")

    label("loc_F3F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(400)
    Return()

    # Function_2_BA1 end

    def Function_3_F4F(): pass

    label("Function_3_F4F")

    OP_28(0x6, 0x1, 0x4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FDE")

    ChrTalk(
        0x101,
        (
            "#002F５·４·５·８·１·８……\x02\x03",
            "……………………………………\x02\x03",
            "#509F……………………咦？\x02\x03",
            "怎么回事～\x01",
            "怎么没打开呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1057")

    label("loc_FDE")


    ChrTalk(
        0x101,
        (
            "#002F５·５·４·８·１·８……\x02\x03",
            "……………………………………\x02\x03",
            "#509F……………………咦？\x02\x03",
            "怎么回事～\x01",
            "怎么没打开呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1057")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x102,
        "#017F（果然。）\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    SetChrChipByIndex(0x102, 7)
    OP_8C(0x102, 180, 400)
    Sleep(400)
    SetChrPos(0x8, -202100, 0, -35820, 0)
    SetChrPos(0xA, -197980, 0, -35450, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)

    def lambda_10EC():
        OP_6D(-202310, 0, -28900, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_10EC)

    def lambda_1104():
        OP_90(0x8, 0xFFFFFC18, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1104)
    Sleep(150)

    def lambda_1124():
        OP_90(0xA, 0xFFFFFC18, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1124)
    WaitChrThread(0x8, 0x1)
    SetChrChipByIndex(0x8, 8)
    OP_43(0x8, 0x0, 0x0, 0x2)

    def lambda_1150():

        label("loc_1150")

        TurnDirection(0x8, 0x102, 0)
        OP_48()
        Jump("loc_1150")

    QueueWorkItem2(0x8, 1, lambda_1150)
    WaitChrThread(0xA, 0x1)
    SetChrChipByIndex(0xA, 8)
    OP_43(0xA, 0x0, 0x0, 0x2)

    def lambda_1172():

        label("loc_1172")

        TurnDirection(0xA, 0x102, 0)
        OP_48()
        Jump("loc_1172")

    QueueWorkItem2(0xA, 1, lambda_1172)
    WaitChrThread(0x0, 0x2)

    ChrTalk(
        0x102,
        "#013F唉，又来了吗……\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xD, -202010, 10, -26160, 180)
    SetChrChipByIndex(0xD, 7)
    ClearChrFlags(0xD, 0x8)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0x102, 0x8)
    SetChrChipByIndex(0x8, 9)
    SetChrChipByIndex(0xA, 9)

    def lambda_11D2():
        OP_92(0x8, 0xD, 0xE10, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_11D2)

    def lambda_11E7():
        OP_92(0xA, 0xD, 0xE10, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_11E7)
    WaitChrThread(0xA, 0x1)
    OP_44(0x8, 0xFF)
    OP_44(0xA, 0xFF)
    RemoveParty(0x0, 0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x3EC, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_1228"),
        (SWITCH_DEFAULT, "loc_122D"),
    )


    label("loc_1228")

    OP_B4(0x0)
    Jump("loc_122D")

    label("loc_122D")

    EventBegin(0x0)
    OP_1D(0x14)
    AddParty(0x0, 0x0)
    OP_6D(-203550, -30, -24610, 0)
    SetChrChipByIndex(0x102, 7)
    SetChrPos(0x102, -202010, 10, -26160, 180)
    SetChrPos(0x101, -204100, 0, -20750, 180)
    OP_6D(-203320, -20, -24970, 0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x102, 0x80)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#009F啊～\x01",
            "为什么还是没打开！？\x02\x03",
            "气死我了，我要采取一些行动了！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 225, 2000)
    OP_8C(0x101, 45, 2000)
    OP_8C(0x101, 180, 2000)
    SetChrChipByIndex(0x101, 6)

    ChrTalk(
        0x101,
        "#005F就让我用实力把它……\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x102, 65535)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F艾丝蒂尔，等一下！\x02\x03",
            "解锁密码是『５４４８１８』！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        "#501F…………嗯？\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0x101, 65535)
    OP_8C(0x101, 135, 400)

    ChrTalk(
        0x101,
        (
            "#004F等、等一下，\x01",
            "再说一次！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F５·４·４…………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    ChrTalk(
        0x101,
        "#002F嗯～５·４·４……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F…………８·１·８。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F……８·１·８。\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_22(0x83, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#004F……啊，打开了。\x02\x03",
            "#502F呵呵㈱\x01",
            "这样就等于完全成功了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F（她还真是自得其乐啊。）\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#006F接下来，\x02\x03",
            "把导力器更换……好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F好了，完成～～⊙\x02\x03",
            "呼～～～\x01",
            "这回可真是累人啊～\x02",
        )
    )

    CloseMessageWindow()

    def lambda_155E():
        OP_6D(-203230, -10, -20760, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_155E)
    OP_8E(0x102, 0xFFFCE924, 0xFFFFFFF6, 0xFFFFAEF2, 0x7D0, 0x0)
    TurnDirection(0x102, 0x101, 400)
    OP_3F(0x327, 1)

    ChrTalk(
        0x102,
        (
            "#010F辛苦了，艾丝蒂尔。\x02\x03",
            "好像也不会有魔兽再过来了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 800)

    ChrTalk(
        0x101,
        (
            "#007F约修亚，对不起啊。\x02\x03",
            "是我把事情变得麻烦了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我倒是没关系。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 225, 400)

    ChrTalk(
        0x102,
        (
            "#017F反正最后街道的路灯也完好无损。\x01",
            "　\x02\x03",
            "刚刚艾丝蒂尔摆出挥棍姿势的时候\x01",
            "真是吓死我了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#008F那、那只是\x01",
            "为了让精神集中而摆出的架势啦。\x02\x03",
            "我做什么事都是以华丽为宗旨的……\x01",
            "怎么会做出那种野蛮的事呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#018F真的吗？\x01",
            "我怎么觉得你现在还想打它呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#009F哼。\x02\x03",
            "不、不管怎样已经完成了委托，\x01",
            "这样也就可以了。\x02\x03",
            "#508F完成就好了，\x01",
            "至于其他的小事就不用管了☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯，说得也是。\x02\x03",
            "那现在我们就回城里去吧。\x02\x03",
            "要向佛莱迪叔叔\x01",
            "报告一下情况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F嗯⊙　走吧。\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_3_F4F end

    def Function_4_1833(): pass

    label("Function_4_1833")

    OP_2B(0x6, 0x1)

    ChrTalk(
        0x101,
        "#002F５·４·４·８·１·８……\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_22(0x83, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#000F……好了，打开了。\x02\x03",
            "#502F嘿嘿嘿㈱\x01",
            "我果然是聪明伶俐！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔，\x01",
            "我这边已经没问题了。\x02\x03",
            "#010F慢慢来，要沉着冷静。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，明～白。\x02\x03",
            "接下来是更换导力器……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        "#001F好了，完成～～⊙\x02",
    )

    CloseMessageWindow()

    def lambda_1966():
        OP_6D(-203230, -10, -20760, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1966)
    OP_8E(0x102, 0xFFFCE924, 0xFFFFFFF6, 0xFFFFAEF2, 0x7D0, 0x0)
    TurnDirection(0x102, 0x101, 400)
    OP_3F(0x327, 1)

    ChrTalk(
        0x102,
        (
            "#010F辛苦了，艾丝蒂尔。\x02\x03",
            "好像也不会有魔兽再过来了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#007F呼～～～\x02\x03",
            "这次还真有一点紧张呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F因为面临的是这样的状况嘛。\x02\x03",
            "不过出乎我意料的是，\x01",
            "艾丝蒂尔居然记得密码。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#001F呵呵呵⊙\x02\x03",
            "其实我只是凭印象随便输入的，\x01",
            "没想到居然对了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x102,
        (
            "#017F果然。\x02\x03",
            "真是的，艾丝蒂尔你啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F总之已经完成了委托，\x01",
            "这样也就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F呵呵，说的也是。\x02\x03",
            "#010F那现在我们就回城里去吧。\x02\x03",
            "#010F要向佛莱迪先生报告一下情况。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F嗯⊙　走吧。\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_4_1833 end

    def Function_5_1BA5(): pass

    label("Function_5_1BA5")

    OP_6C(270000, 2000)
    Return()

    # Function_5_1BA5 end

    def Function_6_1BAF(): pass

    label("Function_6_1BAF")

    OP_A6(0x0)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFCE708, 0x0, 0xFFFF793C, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 0)
    OP_43(0x8, 0x2, 0x0, 0x2)
    OP_A3(0x0)
    OP_A6(0x0)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFCE578, 0x0, 0xFFFF874C, 0x1B58, 0x0)
    OP_8C(0xFE, 0, 0)
    OP_A3(0x0)
    Return()

    # Function_6_1BAF end

    def Function_7_1C03(): pass

    label("Function_7_1C03")

    OP_A6(0x1)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFCF194, 0x0, 0xFFFF7C5C, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 0)
    OP_43(0x9, 0x2, 0x0, 0x2)
    OP_A3(0x1)
    OP_A6(0x1)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFCEE74, 0x0, 0xFFFF88DC, 0x1B58, 0x0)
    OP_8C(0xFE, 315, 0)
    OP_A3(0x1)
    Return()

    # Function_7_1C03 end

    def Function_8_1C57(): pass

    label("Function_8_1C57")

    OP_A6(0x2)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFCF2C0, 0x0, 0xFFFF7554, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 0)
    OP_43(0xA, 0x2, 0x0, 0x2)
    OP_A3(0x2)
    OP_A6(0x2)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFCEAF0, 0x0, 0xFFFF84F4, 0x1B58, 0x0)
    OP_8C(0xFE, 0, 0)
    OP_A3(0x2)
    Return()

    # Function_8_1C57 end

    def Function_9_1CAB(): pass

    label("Function_9_1CAB")

    OP_A6(0x3)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFCFD4C, 0x0, 0xFFFF7874, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 0)
    OP_43(0xB, 0x2, 0x0, 0x2)
    OP_A3(0x3)
    OP_A6(0x3)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFCF194, 0x0, 0xFFFF842C, 0x1B58, 0x0)
    OP_8C(0xFE, 315, 0)
    OP_A3(0x3)
    Return()

    # Function_9_1CAB end

    def Function_10_1CFF(): pass

    label("Function_10_1CFF")

    OP_A6(0x4)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFCE384, 0x0, 0xFFFF99A8, 0xBB8, 0x0)
    OP_8C(0xFE, 180, 0)
    OP_A3(0x4)
    Return()

    # Function_10_1CFF end

    def Function_11_1D26(): pass

    label("Function_11_1D26")

    OP_A6(0x5)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFCEA8C, 0x0, 0xFFFF9AD4, 0xBB8, 0x0)
    OP_8C(0xFE, 180, 0)
    OP_A3(0x5)
    Return()

    # Function_11_1D26 end

    def Function_12_1D4D(): pass

    label("Function_12_1D4D")

    OP_A6(0x4)
    SetChrChipByIndex(0xC, 4)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFCE7D0, 0x0, 0xFFFF8BFC, 0x1770, 0x0)
    OP_A3(0x4)
    OP_A3(0x5)
    Return()

    # Function_12_1D4D end

    def Function_13_1D75(): pass

    label("Function_13_1D75")

    OP_A6(0x5)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFCE60E, 0x0, 0xFFFFA902, 0x1770, 0x0)
    OP_8C(0xFE, 315, 0)
    Return()

    # Function_13_1D75 end

    def Function_14_1D99(): pass

    label("Function_14_1D99")

    OP_A6(0x4)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFCE60E, 0x0, 0xFFFFA902, 0x1770, 0x0)
    OP_8C(0xFE, 315, 0)
    Return()

    # Function_14_1D99 end

    def Function_15_1DBD(): pass

    label("Function_15_1DBD")

    OP_A6(0x5)
    SetChrChipByIndex(0xD, 5)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFCE7D0, 0x0, 0xFFFF8BFC, 0x1770, 0x0)
    OP_A3(0x5)
    OP_A3(0x4)
    Return()

    # Function_15_1DBD end

    def Function_16_1DE5(): pass

    label("Function_16_1DE5")

    OP_A6(0x5)
    SetChrFlags(0xFE, 0x40)
    OP_92(0x102, 0xE, 0x3E8, 0xBB8, 0x0)
    TurnDirection(0x102, 0xE, 0)
    OP_A3(0x5)
    Return()

    # Function_16_1DE5 end

    def Function_17_1E06(): pass

    label("Function_17_1E06")

    OP_A6(0x5)
    SetChrFlags(0xFE, 0x40)
    OP_92(0x102, 0x101, 0x3E8, 0xBB8, 0x0)
    TurnDirection(0x102, 0x101, 0)
    OP_A3(0x5)
    Return()

    # Function_17_1E06 end

    SaveToFile()

Try(main)
