from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'R3102_1 ._SN',
        MapName             = 'Zeiss',
        Location            = 'R3102.x',
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
        Unknown_3A              = 144,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
        "Function_3_19BB",         # 03, 3
        "Function_4_2148",         # 04, 4
        "Function_5_215D",         # 05, 5
        "Function_6_2172",         # 06, 6
        "Function_7_21BA",         # 07, 7
        "Function_8_21CF",         # 08, 8
        "Function_9_21E4",         # 09, 9
        "Function_10_21F9",        # 0A, 10
        "Function_11_2241",        # 0B, 11
        "Function_12_2289",        # 0C, 12
        "Function_13_22D1",        # 0D, 13
        "Function_14_2315",        # 0E, 14
        "Function_15_2353",        # 0F, 15
        "Function_16_2398",        # 10, 16
        "Function_17_2427",        # 11, 17
        "Function_18_2443",        # 12, 18
        "Function_19_2469",        # 13, 19
        "Function_20_248F",        # 14, 20
        "Function_21_24AB",        # 15, 21
        "Function_22_24E8",        # 16, 22
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    Return()

    # Function_1_AB end

    def Function_2_AC(): pass

    label("Function_2_AC")

    EventBegin(0x0)
    OP_44(0x9, 0xFF)
    OP_44(0x8, 0xFF)
    Fade(1000)
    OP_6D(-19410, 40, -38900, 0)
    SetChrPos(0x101, -18990, 50, -38440, 180)
    SetChrPos(0x102, -20320, 20, -39060, 135)
    SetChrPos(0x107, -19090, 50, -36910, 180)
    OP_6C(300000, 0)
    OP_6B(3000, 0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "呜～……\x01",
            "难道出故障了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "啊……\x01",
            "看来的确是啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "偏偏坏在平原正中间，\x01",
            "真是麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F请问这里是怎么了？\x02\x03",
            "你们是不是遇到什么麻烦了？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x101, 400)
    TurnDirection(0x9, 0x101, 400)
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 4)), scpexpr(EXPR_END)), "loc_2BF")

    ChrTalk(
        0x8,
        (
            "啊啊，我以为是谁呢……\x01",
            "原来是艾丝蒂尔和约修亚啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F您好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F很久不见了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(
        0x9,
        "是认识的人吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "嗯，\x01",
            "他们和我一样也是游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F不过我们还只是准游击士。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)
    Jump("loc_40F")

    label("loc_2BF")


    ChrTalk(
        0x9,
        (
            "怎么了？\x01",
            "你们几个……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "咦？那个徽章……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "难道说你们是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯，对啊，\x01",
            "我们是准游击士。\x02\x03",
            "我叫艾丝蒂尔，\x01",
            "旁边的那位是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我叫约修亚，请多指教。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "哟，\x01",
            "这么年轻就当上游击士了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "对了，你们就是传说中的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "请多指教，我叫王，\x01",
            "是蔡斯支部所属的游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "你们的事情，\x01",
            "我在雾香小姐那里听说过。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40F")


    ChrTalk(
        0x8,
        (
            "可是你们\x01",
            "为什么会到这里来呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，是这样的。\x01",
            "我们正在护送这个女孩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F啊，是的。\x01",
            "我要去一趟亚尔摩村……\x02\x03",
            "所以就让艾丝蒂尔姐姐她们送我过去。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x107, 400)

    ChrTalk(
        0x9,
        (
            "哦，我就说在哪儿见过你，\x01",
            "你不是提妲小妹妹吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "又是博士叫你去的吧？\x01",
            "每次要你去做的事情都很辛苦呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#067F呵呵…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F……王先生，\x01",
            "你们在这里做什么呢？\x02\x03",
            "刚才看你们的样子，\x01",
            "好像遇到了什么麻烦吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(
        0x8,
        "啊，是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我们打算把运输车\x01",
            "护送到沃尔费堡垒去……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "刚走到这里\x01",
            "车子就突然出毛病了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我想应该是\x01",
            "导力引擎出了故障。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "刚开始发出咔嗒咔嗒的声音时，\x01",
            "我还以为是路况不平引起的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(
        0x101,
        "#003F哎呀，这可就麻烦了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x28, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_7BA")
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#002F啊，说起来……\x02\x03",
            "公告板上有一个寻找运输车的委托。\x01",
            "　\x02\x03",
            "难道说就是王先生你们这辆吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F嗯，应该就是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "这样啊……\x01",
            "原来协会也开始找我们了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#063F唔～可是……\x01",
            "是导力引擎出了故障。\x02\x03",
            "如果是这个原因，\x01",
            "那么不把内部用的\x01",
            "驱动导力器全部更换掉是不行的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80A")

    label("loc_7BA")


    ChrTalk(
        0x107,
        (
            "#063F是导力引擎的故障吗？\x02\x03",
            "那么不把内部用的\x01",
            "驱动导力器全部更换掉是不行的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80A")


    def lambda_810():
        TurnDirection(0x102, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_810)
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(
        0x101,
        (
            "#004F啊…………？\x01",
            "现在不能进行修理吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(
        0x107,
        (
            "#063F因为导力引擎的核心\x01",
            "是极为精密的机械……\x02\x03",
            "如果要拆开修理，\x01",
            "就必须有相应的设备。\x02\x03",
            "只用简单的工具是无从下手的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F原来如此。\x02\x03",
            "要在室外修理的确是比较困难。\x01",
            "　\x02\x03",
            "#012F………………嗯！？\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_8C(0x102, 215, 400)
    Sleep(800)
    OP_21()
    OP_1D(0x56)

    def lambda_94C():
        TurnDirection(0x8, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_94C)

    def lambda_95A():
        TurnDirection(0x107, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_95A)

    def lambda_968():
        TurnDirection(0x9, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_968)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#002F怎、怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F嗯，这个感觉是……\x02",
    )

    CloseMessageWindow()

    def lambda_9B1():
        OP_6D(-27480, -30, -42850, 3000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_9B1)

    def lambda_9C9():
        OP_6C(270000, 3000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_9C9)
    Sleep(700)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 8)
    SetChrPos(0xA, -26150, -50, -46240, 45)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 8)
    SetChrPos(0xB, -27650, 30, -47100, 45)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 8)
    SetChrPos(0xC, -28470, -90, -45180, 45)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 8)
    SetChrPos(0xD, -30510, -30, -44920, 45)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 8)
    SetChrPos(0xE, -29310, -90, -43270, 45)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 8)
    SetChrPos(0xF, -30380, 0, -46760, 45)
    OP_43(0xA, 0x1, 0x1, 0x4)
    OP_43(0xC, 0x1, 0x1, 0x6)
    OP_43(0xE, 0x1, 0x1, 0x8)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_AC3():
        OP_8C(0x8, 270, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_AC3)

    def lambda_AD1():
        OP_8C(0x101, 215, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AD1)
    Sleep(150)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_B12():
        OP_8C(0x9, 270, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B12)

    def lambda_B20():
        OP_8C(0x107, 215, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_B20)
    OP_43(0xB, 0x1, 0x1, 0x5)
    OP_43(0xD, 0x1, 0x1, 0x7)
    Sleep(100)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 9)
    SetChrChipByIndex(0x8, 5)
    SetChrChipByIndex(0x107, 13)
    OP_43(0xF, 0x1, 0x1, 0x9)
    WaitChrThread(0xF, 0x1)

    def lambda_B61():
        OP_6D(-21250, -20, -39110, 1500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_B61)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(120)
    OP_62(0x107, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    WaitChrThread(0x11, 0x1)
    OP_94(0x1, 0x9, 0xB4, 0xC8, 0x3E8, 0x0)

    ChrTalk(
        0x9,
        "魔、魔兽！？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x14, 0x80)
    SetChrChipByIndex(0x14, 8)
    SetChrPos(0x14, -22130, -40, -48120, 26)
    SetChrFlags(0x14, 0x4)
    OP_51(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4A(0x14, 0)
    SetChrSubChip(0x14, 4)
    OP_96(0x14, 0xFFFFAC90, 0x7D0, 0xFFFF4F2A, 0x898, 0x1388)
    SetChrChipByIndex(0x14, 7)
    OP_4B(0x14, 0)

    def lambda_C1C():
        OP_6D(-19870, -30, -41930, 1000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_C1C)

    def lambda_C34():
        OP_6C(180000, 1500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_C34)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x101, 0x14, 400)
    WaitChrThread(0x11, 0x2)

    ChrTalk(
        0x101,
        "#005F王先生！上面！\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x8, 0x14, 400)
    SetChrChipByIndex(0x14, 8)
    OP_8E(0x14, 0xFFFFB17C, 0x7D0, 0xFFFF572C, 0x1B58, 0x0)
    OP_51(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4A(0x14, 0)
    SetChrSubChip(0x14, 4)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_CE2():

        label("loc_CE2")

        TurnDirection(0x9, 0x14, 400)
        OP_48()
        Jump("loc_CE2")

    QueueWorkItem2(0x9, 1, lambda_CE2)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_CF8():
        OP_96(0x14, 0xFFFFB302, 0xFFFFFFD8, 0xFFFF5E52, 0x64, 0x1388)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_CF8)
    OP_51(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_43(0x8, 0x1, 0x1, 0xD)
    Sleep(120)
    OP_44(0x14, 0xFF)
    SetChrFlags(0x14, 0x20)
    SetChrFlags(0x14, 0x4)
    SetChrFlags(0x14, 0x40)
    PlayEffect(0x8, 0xFF, 0x14, 0, 2000, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x14, 2)
    SetChrSubChip(0x14, 0)
    OP_8F(0x14, 0xFFFFB0F0, 0x320, 0xFFFF5BDC, 0x1F40, 0x0)
    PlayEffect(0x12, 0xFF, 0xFF, -20370, 800, -42730, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x14, -20240, 1000, -42020, 0)
    OP_51(0x14, 0x2A, (scpexpr(EXPR_PUSH_LONG, 0x7530), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x2B, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x2C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF15A0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x14, 0x3, 0x1, 0xF)
    OP_43(0x14, 0x2, 0x1, 0x10)
    Sleep(400)
    OP_96(0xB, 0xFFFF98FE, 0xFFFFFFBA, 0xFFFF50D8, 0x1F4, 0xBB8)
    WaitChrThread(0x14, 0x2)
    WaitChrThread(0x8, 0x1)
    OP_44(0x9, 0x1)
    OP_44(0x14, 0x3)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x9,
        "#1P哇、哇哦！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 400)
    SetChrChipByIndex(0x8, 5)
    TurnDirection(0x8, 0xB, 400)
    OP_4B(0x8, 0)

    ChrTalk(
        0x8,
        "#1P布鲁诺先生，请退后！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1P哦、哦！\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_ED8():
        OP_8E(0x9, 0xFFFFC09A, 0xFFFFFFE2, 0xFFFF6640, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_ED8)

    def lambda_EF3():
        OP_6D(-15540, -50, -40250, 2000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_EF3)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 8)
    SetChrPos(0x11, -19100, -30, -50010, 43)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 8)
    SetChrPos(0x12, -19100, -30, -50010, 43)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 8)
    SetChrPos(0x13, -19100, -30, -50010, 43)
    OP_43(0x11, 0x1, 0x1, 0xA)
    Sleep(400)
    OP_43(0x12, 0x1, 0x1, 0xB)
    Sleep(400)
    OP_43(0x13, 0x1, 0x1, 0xC)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x9, 0x12, 400)
    OP_95(0x9, 0x0, 0x0, 0x0, 0x320, 0x2EE0)

    def lambda_FB0():
        OP_6D(-19630, 60, -38120, 2000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_FB0)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0x9, 0xFFFFBBD6, 0x0, 0xFFFF6D66, 0xBB8, 0x0)
    TurnDirection(0x9, 0x12, 400)
    WaitChrThread(0x14, 0x1)

    ChrTalk(
        0x9,
        (
            "哇、哇～！\x01",
            "后面也来了！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(120)
    OP_62(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_1061():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1061)

    def lambda_106F():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_106F)
    TurnDirection(0x8, 0x12, 400)

    ChrTalk(
        0x8,
        "………………嗯？！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F王先生，\x01",
            "后面的就拜托你了！\x02\x03",
            "这边的就由我们来对付。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1P好、好的……放心吧！\x02",
    )

    CloseMessageWindow()

    def lambda_10FA():
        OP_8C(0xFE, 215, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10FA)
    OP_8C(0x107, 215, 400)

    ChrTalk(
        0x101,
        (
            "#005F好！\x01",
            "交给我们吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0xA, 8)
    SetChrChipByIndex(0xB, 8)
    SetChrChipByIndex(0xC, 8)
    SetChrChipByIndex(0xD, 8)
    SetChrChipByIndex(0xE, 8)
    SetChrChipByIndex(0xF, 8)

    def lambda_115B():
        OP_94(0x1, 0xFE, 0x0, 0xFA0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_115B)

    def lambda_1171():
        OP_94(0x1, 0xFE, 0x0, 0xFA0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1171)

    def lambda_1187():
        OP_94(0x1, 0xFE, 0x0, 0xFA0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1187)

    def lambda_119D():
        OP_94(0x1, 0xFE, 0x0, 0xFA0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_119D)

    def lambda_11B3():
        OP_94(0x1, 0xFE, 0x0, 0xFA0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_11B3)

    def lambda_11C9():
        OP_94(0x1, 0xFE, 0x0, 0xFA0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_11C9)
    SetChrChipByIndex(0x8, 6)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x8, 0x1000)
    OP_43(0x8, 0x1, 0x1, 0xE)
    WaitChrThread(0x8, 0x1)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x14, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x107, 0xFF)
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0x9, 0x40)
    ClearChrFlags(0x8, 0x1000)
    Battle(0x3F6, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_1258"),
        (SWITCH_DEFAULT, "loc_125B"),
    )


    label("loc_1258")

    OP_B4(0x0)
    Return()

    label("loc_125B")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    OP_6D(-18050, 20, -37820, 0)
    OP_6B(3000, 0)
    OP_6C(180000, 0)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrPos(0x8, -17230, 10, -39580, 104)
    SetChrPos(0x9, -17250, 20, -36060, 199)
    SetChrPos(0x101, -18990, 50, -38440, 225)
    SetChrPos(0x102, -20320, 20, -39060, 225)
    SetChrPos(0x107, -19090, 50, -36910, 225)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 9)
    SetChrChipByIndex(0x107, 13)
    SetChrChipByIndex(0x8, 5)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#002F大家总算都平安无事了……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F嗯，已经把它们击退了。\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x107, 65535)
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(
        0x107,
        "#561F呼……太好了～\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 0)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "还好大家都\x01",
            "没受到任何伤害。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)

    def lambda_13D3():
        TurnDirection(0x102, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_13D3)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x9,
        "呼～捡回一条命啊。\x02",
    )

    CloseMessageWindow()

    def lambda_1400():
        OP_8C(0x101, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1400)

    def lambda_140E():
        OP_8C(0x107, 135, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_140E)

    def lambda_141C():
        OP_6C(270000, 3500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_141C)

    def lambda_142C():
        OP_6D(-18530, 50, -38340, 3500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_142C)
    SetChrFlags(0x9, 0x40)
    OP_43(0x102, 0x1, 0x1, 0x11)
    OP_8E(0x9, 0xFFFFBB18, 0xA, 0xFFFF718A, 0x3E8, 0x0)
    OP_8E(0x9, 0xFFFFBE10, 0xFFFFFFF6, 0xFFFF6A32, 0x3E8, 0x0)
    TurnDirection(0x9, 0x102, 400)
    ClearChrFlags(0x9, 0x40)
    WaitChrThread(0xA, 0x1)
    WaitChrThread(0xA, 0x2)
    OP_44(0x101, 0xFF)
    OP_44(0x107, 0xFF)

    ChrTalk(
        0x9,
        (
            "嗯…………\x01",
            "虽然得救了，\x01",
            "但是还要考虑接下来怎么做。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(
        0x8,
        "嗯，是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "首先，无论如何\x01",
            "也要让这个运输车动起来才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F可是，\x01",
            "刚刚不是已经说过不能修理了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#063F唔～\x01",
            "我觉得的确很困难。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F这么说来……\x01",
            "除了更换零件以外，\x01",
            "的确已经没有其他办法了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "运输车的管理员是\x01",
            "中央工房的普罗梅笛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "只要问问他，\x01",
            "应该可以知道更换用的零件的保管场所……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "可是，要做到这一点，\x01",
            "就必须要回蔡斯一趟。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(
        0x8,
        (
            "嗯～真头疼啊。\x01",
            "布鲁诺先生，怎么办？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "要回蔡斯去吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(
        0x9,
        (
            "我认为现在还没这必要，\x01",
            "还是再稍微摆弄一下这车子吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "能动的话当然是最好了。\x01",
            "如果实在是动不了，\x01",
            "也就只有回蔡斯去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "这样啊…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那就暂时\x01",
            "先呆在这里吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "嗯，只有这样了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "就是这么回事，\x01",
            "我们要留在这里\x01",
            "继续努力试试。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F嗯，我知道了……\x01",
            "王先生你们要注意安全哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "没问题，我不会蛮干的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "一旦有什么危险，\x01",
            "我们会立刻返回城里的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x107, 400)

    ChrTalk(
        0x8,
        (
            "那么，提妲小妹妹，\x01",
            "你们去亚尔摩的路上也要小心。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x8, 400)

    ChrTalk(
        0x107,
        "#060F啊，好的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "如果你们有空的话，\x01",
            "请帮忙联络一下普罗梅笛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "他应该一直都在中央工房\x01",
            "三楼的设计室里面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，那再见吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F王先生你们务必要注意安全。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【寻找运输车】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_43(0x8, 0x1, 0x1, 0x12)
    OP_43(0x9, 0x1, 0x1, 0x13)
    Sleep(100)
    OP_28(0x28, 0x4, 0x4)
    OP_28(0x28, 0x4, 0x2)
    OP_28(0x28, 0x4, 0x10)
    OP_28(0x28, 0x1, 0x1)
    OP_28(0x28, 0x1, 0x2)
    OP_28(0x28, 0x1, 0x4)
    OP_28(0x28, 0x1, 0x8)
    OP_28(0x28, 0x1, 0x10)
    OP_28(0x28, 0x1, 0x20)
    OP_28(0x29, 0x4, 0x4)
    OP_28(0x29, 0x4, 0x2)
    EventEnd(0x0)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    OP_43(0x9, 0x0, 0x0, 0x2)
    OP_43(0x8, 0x0, 0x0, 0x2)
    Return()

    # Function_2_AC end

    def Function_3_19BB(): pass

    label("Function_3_19BB")

    EventBegin(0x0)
    OP_44(0x9, 0xFF)
    OP_44(0x8, 0xFF)
    Fade(1000)
    OP_6D(-19410, 40, -38900, 0)
    SetChrPos(0x101, -18990, 50, -38440, 180)
    SetChrPos(0x102, -20320, 20, -39060, 135)
    SetChrPos(0x107, -19090, 50, -36910, 180)
    OP_6C(300000, 0)
    OP_6B(3000, 0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_0D()

    ChrTalk(
        0x101,
        "#000F呼～久等了～\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x8, 0x101, 400)
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(
        0x8,
        "哦，艾丝蒂尔、约修亚。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "怎么样？\x01",
            "导力引擎\x01",
            "已经找到了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F嗯，已经找到了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F让你们久等了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "哦哦，就是这东西，\x01",
            "哎呀，真是帮了大忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "你们走了之后\x01",
            "我又想尽了各种办法……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "但是不管怎样\x01",
            "还是没法让车子动起来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我们本来打算离开的。\x01",
            "刚刚正准备商量\x01",
            "回蔡斯的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F是这样啊，\x01",
            "我们能够赶上真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F那么就立刻修理运输车吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F啊，好的。\x02\x03",
            "#061F交给我来办吧，\x01",
            "啪啪几下就可以更换好导力引擎了呢～\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x107, 400)

    ChrTalk(
        0x8,
        "啊，拜托了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x107, 400)

    ChrTalk(
        0x9,
        "多谢你帮忙了，小姑娘。\x02",
    )

    CloseMessageWindow()

    def lambda_1C6A():
        OP_8E(0x9, 0xFFFFB4A6, 0xFFFFFFE2, 0xFFFF5E98, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1C6A)
    OP_43(0x8, 0x1, 0x1, 0x14)
    SetChrFlags(0x107, 0x40)
    OP_8E(0x107, 0xFFFFBAD2, 0x14, 0xFFFF6AC8, 0x5DC, 0x0)
    FadeToDark(1000, 0, -1)
    OP_8E(0x107, 0xFFFFB596, 0x1E, 0xFFFF606E, 0x5DC, 0x0)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x9, 0x1)
    OP_0D()
    OP_6D(-18190, 10, -40240, 0)
    SetChrPos(0x107, -17490, 10, -39610, 182)
    SetChrPos(0x8, -19060, -10, -40450, 145)
    SetChrChipByIndex(0x9, 14)
    OP_6B(3000, 0)
    OP_6C(276000, 0)
    SetChrPos(0x10, -17420, -20, -41550, 51)
    SetChrFlags(0x10, 0x40)
    OP_A1(0x10, 0x0)
    OP_72(0x0, 0x4)
    OP_72(0x0, 0x2)
    OP_71(0x0, 0x400)
    OP_71(0x0, 0x40)
    Sleep(1)
    ClearChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x40)
    SetChrBattleFlags(0x9, 0x20)
    OP_89(0x9, -17120, 440, -41360, 51)
    SetChrFlags(0x9, 0x20)
    LoadEffect(0x0, "map\\\\mp024_00.eff")
    TurnDirection(0x101, 0x9, 0)
    Sleep(400)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x107,
        "#060F#4P……这样就可以了。\x02",
    )

    CloseMessageWindow()
    OP_94(0x1, 0x107, 0xB4, 0x5DC, 0x7D0, 0x0)

    ChrTalk(
        0x9,
        (
            "……那么，\x01",
            "动起来了哦。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x9D, 0x0, 0x64)
    Sleep(400)
    OP_22(0xCF, 0x1, 0x55)

    ChrTalk(
        0x107,
        (
            "#062F#4P……………………\x02\x03",
            "#060F#4P……嗯，没问题了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "呼～\x01",
            "这下总算可以把货物运送过去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "真不愧是\x01",
            "拉赛尔博士的孙女啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "虽然还在上主日学校的年纪，\x01",
            "维修的能力却是顶呱呱哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#067F#4P嘿嘿……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "好了，我们该出发了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "你们也要注意安全。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F#2P嗯，我们会的。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "那么就再见了，\x01",
            "今天多亏了你们的帮忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#2P路上小心。\x02",
    )

    CloseMessageWindow()

    def lambda_1F6D():

        label("loc_1F6D")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_1F6D")

    QueueWorkItem2(0x0, 1, lambda_1F6D)

    def lambda_1F7E():

        label("loc_1F7E")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_1F7E")

    QueueWorkItem2(0x1, 1, lambda_1F7E)

    def lambda_1F8F():

        label("loc_1F8F")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_1F8F")

    QueueWorkItem2(0x2, 1, lambda_1F8F)
    OP_8C(0x8, 51, 400)
    SetChrFlags(0x8, 0x40)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 40)
    OP_70(0x0, 0xC8)

    def lambda_1FBF():
        OP_6D(-14070, -40, -37570, 3000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_1FBF)
    OP_24(0xCF, 0x64)

    def lambda_1FDB():
        OP_94(0x1, 0x10, 0x0, 0x4650, 0x6A4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1FDB)
    PlayEffect(0x0, 0x0, 0x10, 0, 200, -7000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x10, 0, 200, -4000, 0, 0, 0, 1000, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_8E(0x8, 0xFFFFBBAE, 0xA, 0xFFFF6546, 0x6A4, 0x0)
    OP_8C(0x8, 51, 0)

    def lambda_2076():
        OP_94(0x1, 0x8, 0x0, 0x4E20, 0x6A4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2076)
    WaitChrThread(0x10, 0x3)
    Sleep(1000)

    def lambda_2096():
        OP_69(0x101, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_2096)
    OP_43(0x0, 0x3, 0x1, 0x16)
    WaitChrThread(0x10, 0x1)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_72(0x0, 0x20)
    OP_3F(0x346, 1)
    OP_28(0x29, 0x1, 0x40)
    OP_28(0x29, 0x4, 0x10)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x10, 0x80)
    OP_71(0x0, 0x4)
    WaitChrThread(0x10, 0x3)
    WaitChrThread(0x0, 0x3)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【修理运输车】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_3_19BB end

    def Function_4_2148(): pass

    label("Function_4_2148")

    OP_94(0x1, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 7)
    Return()

    # Function_4_2148 end

    def Function_5_215D(): pass

    label("Function_5_215D")

    OP_94(0x1, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 7)
    Return()

    # Function_5_215D end

    def Function_6_2172(): pass

    label("Function_6_2172")

    OP_94(0x1, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
    OP_4A(0xFE, 0)
    SetChrSubChip(0xFE, 4)
    OP_96(0xFE, 0xFFFF9F3E, 0x3C, 0xFFFF5D80, 0x320, 0x3E8)
    OP_4B(0xFE, 0)
    OP_94(0x1, 0xFE, 0x0, 0xC8, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 7)
    Return()

    # Function_6_2172 end

    def Function_7_21BA(): pass

    label("Function_7_21BA")

    OP_94(0x1, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 7)
    Return()

    # Function_7_21BA end

    def Function_8_21CF(): pass

    label("Function_8_21CF")

    OP_94(0x1, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 7)
    Return()

    # Function_8_21CF end

    def Function_9_21E4(): pass

    label("Function_9_21E4")

    OP_94(0x1, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 7)
    Return()

    # Function_9_21E4 end

    def Function_10_21F9(): pass

    label("Function_10_21F9")

    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFFC16C, 0xA, 0xFFFF531C, 0x1388, 0x0)

    def lambda_2218():

        label("loc_2218")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_2218")

    QueueWorkItem2(0xFE, 2, lambda_2218)
    OP_8F(0xFE, 0xFFFFCA04, 0xFFFFFFD8, 0xFFFF6816, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 7)
    OP_44(0xFE, 0x2)
    Return()

    # Function_10_21F9 end

    def Function_11_2241(): pass

    label("Function_11_2241")

    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFFC16C, 0xA, 0xFFFF531C, 0x1388, 0x0)

    def lambda_2260():

        label("loc_2260")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_2260")

    QueueWorkItem2(0xFE, 2, lambda_2260)
    OP_8F(0xFE, 0xFFFFC932, 0xFFFFFFA6, 0xFFFF5F2E, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 7)
    OP_44(0xFE, 0x2)
    Return()

    # Function_11_2241 end

    def Function_12_2289(): pass

    label("Function_12_2289")

    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFFC16C, 0xA, 0xFFFF531C, 0x1388, 0x0)

    def lambda_22A8():

        label("loc_22A8")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_22A8")

    QueueWorkItem2(0xFE, 2, lambda_22A8)
    OP_8F(0xFE, 0xFFFFC360, 0xFFFFFFC4, 0xFFFF5A2E, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 7)
    OP_44(0xFE, 0x2)
    Return()

    # Function_12_2289 end

    def Function_13_22D1(): pass

    label("Function_13_22D1")

    OP_8C(0x8, 225, 0)
    OP_44(0x8, 0x0)
    SetChrChipByIndex(0x8, 11)
    OP_22(0x1F5, 0x0, 0x64)
    OP_99(0x8, 0x0, 0x3, 0xBB8)
    Sleep(200)
    OP_99(0x8, 0x4, 0x7, 0xBB8)
    OP_95(0x9, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    Return()

    # Function_13_22D1 end

    def Function_14_2315(): pass

    label("Function_14_2315")

    OP_8E(0xFE, 0xFFFFBAD2, 0x1E, 0xFFFF65D2, 0x1388, 0x0)

    def lambda_232F():

        label("loc_232F")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_232F")

    QueueWorkItem2(0xFE, 2, lambda_232F)
    OP_8F(0xFE, 0xFFFFC02C, 0xFFFFFFEC, 0xFFFF67DA, 0x1388, 0x0)
    OP_44(0xFE, 0x2)
    Return()

    # Function_14_2315 end

    def Function_15_2353(): pass

    label("Function_15_2353")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2397")
    OP_8C(0xFE, 45, 1000)
    OP_8C(0xFE, 90, 1000)
    OP_8C(0xFE, 135, 1000)
    OP_8C(0xFE, 180, 1000)
    OP_8C(0xFE, 225, 1000)
    OP_8C(0xFE, 270, 1000)
    OP_8C(0xFE, 315, 1000)
    OP_8C(0xFE, 360, 1000)
    Jump("Function_15_2353")

    label("loc_2397")

    Return()

    # Function_15_2353 end

    def Function_16_2398(): pass

    label("Function_16_2398")

    OP_8F(0x14, 0xFFFFA358, 0xC8, 0xFFFF5088, 0x1F40, 0x0)
    PlayEffect(0x12, 0xFF, 0xFF, -23720, 30, -44920, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_22(0x20B, 0x0, 0x5F)

    def lambda_23EC():
        OP_9F(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_23EC)
    OP_96(0x14, 0xFFFF9EA8, 0xC8, 0xFFFF5092, 0x1F4, 0xFA0)
    OP_96(0x14, 0xFFFF9AAC, 0xC8, 0xFFFF4D0E, 0x1F4, 0x7D0)
    Return()

    # Function_16_2398 end

    def Function_17_2427(): pass

    label("Function_17_2427")

    OP_8E(0x102, 0xFFFFB2B2, 0x14, 0xFFFF65FA, 0x3E8, 0x0)
    TurnDirection(0xFE, 0x8, 400)
    Return()

    # Function_17_2427 end

    def Function_18_2443(): pass

    label("Function_18_2443")

    SetChrFlags(0xFE, 0x40)
    OP_8E(0x8, 0xFFFFB58C, 0xFFFFFFF6, 0xFFFF61FE, 0x7D0, 0x0)
    OP_8C(0x8, 145, 400)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_18_2443 end

    def Function_19_2469(): pass

    label("Function_19_2469")

    SetChrFlags(0xFE, 0x40)
    OP_8E(0x9, 0xFFFFBBAE, 0xA, 0xFFFF6546, 0x7D0, 0x0)
    OP_8C(0x9, 182, 400)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_19_2469 end

    def Function_20_248F(): pass

    label("Function_20_248F")

    OP_8E(0x8, 0xFFFFAE34, 0xFFFFFFCE, 0xFFFF6334, 0xBB8, 0x0)
    OP_8C(0x8, 135, 400)
    Return()

    # Function_20_248F end

    def Function_21_24AB(): pass

    label("Function_21_24AB")

    OP_94(0x1, 0xFE, 0x5A, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xFE, 0x10E, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xFE, 0x5A, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xFE, 0x10E, 0x64, 0xBB8, 0x0)
    Return()

    # Function_21_24AB end

    def Function_22_24E8(): pass

    label("Function_22_24E8")

    Sleep(4000)
    OP_24(0xCF, 0x5F)
    Sleep(100)
    OP_24(0xCF, 0x5A)
    Sleep(100)
    OP_24(0xCF, 0x55)
    Sleep(100)
    OP_24(0xCF, 0x50)
    Sleep(100)
    OP_24(0xCF, 0x4B)
    Sleep(100)
    OP_24(0xCF, 0x46)
    Sleep(100)
    OP_24(0xCF, 0x41)
    Sleep(100)
    OP_24(0xCF, 0x3C)
    Sleep(100)
    OP_24(0xCF, 0x37)
    Sleep(100)
    OP_23(0xCF)
    Return()

    # Function_22_24E8 end

    SaveToFile()

Try(main)
