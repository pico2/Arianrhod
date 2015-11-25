from ED6ScenarioHelper import *

def main():
    # 古罗尼山道

    CreateScenaFile(
        FileName            = 'C1500_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 61,
        MapDefaultBGM       = "ed60022",
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
        "Function_1_636",          # 01, 1
        "Function_2_B34",          # 02, 2
        "Function_3_FF0",          # 03, 3
        "Function_4_13E8",         # 04, 4
        "Function_5_1416",         # 05, 5
        "Function_6_1444",         # 06, 6
        "Function_7_1502",         # 07, 7
        "Function_8_159E",         # 08, 8
        "Function_9_1635",         # 09, 9
        "Function_10_16CC",        # 0A, 10
        "Function_11_1767",        # 0B, 11
        "Function_12_17E5",        # 0C, 12
        "Function_13_1863",        # 0D, 13
    )


    def Function_0_66(): pass

    label("Function_0_66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_635")
    ClearMapFlags(0x1)
    EventBegin(0x0)
    TurnDirection(0x0, 0x8, 400)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F1")

    ChrTalk(
        0x101,
        (
            "#004F…………咦？\x02\x03",
            "好像有什么东西在动……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15A")

    label("loc_F1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_125")

    ChrTalk(
        0x102,
        (
            "#014F…………嗯。\x02\x03",
            "那是…………\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15A")

    label("loc_125")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15A")

    ChrTalk(
        0x103,
        (
            "#023F…………嗯？\x02\x03",
            "……大家等一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15A")


    def lambda_160():
        OP_6D(-149500, 2000, 60700, 2000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_160)
    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x8, 0x1, 0x1, 0x6)
    OP_43(0x9, 0x1, 0x1, 0x7)
    OP_43(0xA, 0x1, 0x1, 0x8)
    OP_43(0xB, 0x1, 0x1, 0x9)
    OP_A2(0x0)
    Sleep(600)
    OP_A2(0x1)
    Sleep(600)
    OP_A2(0x2)
    Sleep(800)
    OP_A2(0x3)
    SetChrPos(0x101, -143800, 3500, 73400, 165)
    SetChrPos(0x103, -143590, 2970, 74590, 165)
    SetChrPos(0x102, -144440, 2820, 73810, 165)
    SetChrPos(0x135, -144850, 3310, 75450, 165)

    def lambda_24B():
        OP_6C(300000, 3000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_24B)
    OP_A5(0x0)
    OP_A5(0x1)
    OP_A5(0x2)
    OP_A5(0x3)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#012F我们中埋伏了……\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)
    TurnDirection(0x102, 0xC, 400)
    Sleep(400)

    def lambda_2AF():
        OP_6D(-146900, 4000, 81700, 2000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2AF)

    def lambda_2C7():
        TurnDirection(0x101, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2C7)

    def lambda_2D5():
        TurnDirection(0x103, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2D5)
    Sleep(400)

    def lambda_2E8():
        TurnDirection(0x135, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x135, 1, lambda_2E8)
    OP_43(0xC, 0x1, 0x1, 0xA)
    OP_43(0xD, 0x1, 0x1, 0xB)
    OP_43(0xE, 0x1, 0x1, 0xC)
    OP_43(0xF, 0x1, 0x1, 0xD)
    OP_A2(0x4)
    Sleep(600)
    OP_A2(0x5)
    Sleep(800)
    OP_62(0x135, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0x135, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    OP_A2(0x6)
    Sleep(400)
    OP_62(0x135, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_A2(0x7)
    Sleep(600)
    OP_8E(0x135, 0xFFFDCB00, 0xC1C, 0x123EA, 0x7D0, 0x0)
    TurnDirection(0x135, 0xC, 400)
    OP_A5(0x4)
    OP_A5(0x5)
    OP_A5(0x6)
    OP_A5(0x7)
    Sleep(400)
    TurnDirection(0x135, 0x103, 0)

    ChrTalk(
        0x135,
        "怎、怎、怎么办！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x135, 0)

    ChrTalk(
        0x103,
        (
            "#024F冷静一点！\x02\x03",
            "没关系的，\x01",
            "我们一定会好好保护你。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    OP_51(0x11, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#002F前面和后面都有魔兽……\x02\x03",
            "好～那么我们就……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_476")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_62B")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【正面突破！】\x01",      # 0
            "【保护后方！】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4E6"),
        (1, "loc_55F"),
        (SWITCH_DEFAULT, "loc_628"),
    )


    label("loc_4E6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x101, 0x80)
    OP_43(0x11, 0x3, 0x0, 0x2)

    ChrTalk(
        0x101,
        "#005F正面突破！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x8, 400)

    ChrTalk(
        0x103,
        (
            "#022F嗯，对。\x01",
            "队伍分散是很危险的。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x10, 0x1, 0x8)
    OP_2C(0x10, 0xC8)
    OP_2B(0x10, 0x1)
    Call(1, 1)
    Jump("loc_628")

    label("loc_55F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x101, 0x80)
    OP_43(0x11, 0x3, 0x0, 0x2)

    ChrTalk(
        0x101,
        "#005F赶快保护后方！\x02",
    )

    CloseMessageWindow()
    OP_44(0x11, 0xFF)
    SetChrFlags(0x11, 0x40)

    def lambda_5A5():

        label("loc_5A5")

        TurnDirection(0x135, 0x11, 0)
        OP_48()
        Jump("loc_5A5")

    QueueWorkItem2(0x135, 1, lambda_5A5)

    def lambda_5B6():

        label("loc_5B6")

        TurnDirection(0x103, 0x11, 0)
        OP_48()
        Jump("loc_5B6")

    QueueWorkItem2(0x103, 1, lambda_5B6)

    def lambda_5C7():

        label("loc_5C7")

        TurnDirection(0x102, 0x11, 0)
        OP_48()
        Jump("loc_5C7")

    QueueWorkItem2(0x102, 1, lambda_5C7)
    SetChrChipByIndex(0x11, 5)

    def lambda_5DD():
        OP_6D(-144030, 3060, 74750, 1000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5DD)
    OP_8E(0x11, 0xFFFDCC0E, 0xE10, 0x12912, 0x1388, 0x0)
    SetChrChipByIndex(0x11, 2)
    OP_43(0x11, 0x3, 0x0, 0x2)
    OP_44(0x135, 0x1)
    OP_44(0x103, 0x1)
    OP_44(0x102, 0x1)
    OP_28(0x10, 0x1, 0x10)
    Call(1, 3)
    Jump("loc_628")

    label("loc_628")

    Jump("loc_476")

    label("loc_62B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_635")

    Return()

    # Function_0_66 end

    def Function_1_636(): pass

    label("Function_1_636")


    def lambda_63C():
        TurnDirection(0x102, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_63C)

    def lambda_64A():
        TurnDirection(0x135, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x135, 1, lambda_64A)
    Sleep(400)

    ChrTalk(
        0x102,
        "#012F明白！\x02",
    )

    CloseMessageWindow()
    OP_51(0x12, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x102, 0x80)
    OP_43(0x12, 0x3, 0x0, 0x2)

    ChrTalk(
        0x103,
        "#022F速战速决！把前方的敌人杀个片甲不留！\x02",
    )

    CloseMessageWindow()
    OP_51(0x13, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x103, 0x80)
    OP_43(0x13, 0x3, 0x0, 0x2)

    ChrTalk(
        0x101,
        "#002F嗯！\x02",
    )

    CloseMessageWindow()
    OP_44(0x11, 0x3)
    OP_44(0x12, 0x3)
    OP_44(0x13, 0x3)
    SetChrChipByIndex(0x11, 5)
    SetChrChipByIndex(0x12, 6)
    SetChrChipByIndex(0x13, 7)

    def lambda_739():
        OP_6D(-142800, 2000, 69900, 1000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_739)

    def lambda_751():
        OP_92(0x11, 0x10, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_751)

    def lambda_766():
        OP_92(0x13, 0x10, 0xFA0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_766)

    def lambda_77B():
        OP_92(0x12, 0x10, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_77B)
    OP_62(0x135, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_7A2():
        OP_92(0x135, 0x10, 0x1770, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x135, 2, lambda_7A2)

    def lambda_7B7():
        OP_92(0x8, 0x101, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7B7)

    def lambda_7CC():
        OP_92(0x9, 0x101, 0xFA0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7CC)

    def lambda_7E1():
        OP_92(0xA, 0x101, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7E1)

    def lambda_7F6():
        OP_92(0xB, 0x101, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_7F6)
    Sleep(800)
    OP_44(0x101, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x135, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x12, 0xFF)
    Battle(0x3F0, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_83F"),
        (SWITCH_DEFAULT, "loc_842"),
    )


    label("loc_83F")

    OP_B4(0x0)
    Return()

    label("loc_842")

    EventBegin(0x0)
    OP_6D(-142800, 2000, 69900, 0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0x11, -142200, 2500, 67300, 165)
    SetChrPos(0x13, -143500, 2500, 67900, 165)
    SetChrPos(0x12, -141300, 2500, 68600, 165)
    SetChrPos(0x135, -143500, 2000, 70600, 165)
    SetChrChipByIndex(0x11, 2)
    SetChrChipByIndex(0x12, 3)
    SetChrChipByIndex(0x13, 4)
    OP_43(0x11, 0x3, 0x0, 0x2)
    OP_43(0x12, 0x3, 0x0, 0x2)
    OP_43(0x13, 0x3, 0x0, 0x2)
    SetChrPos(0xC, -146200, 4000, 79800, 165)
    SetChrPos(0xD, -146200, 4000, 79800, 165)
    SetChrPos(0xE, -146200, 4000, 79800, 165)
    SetChrPos(0xF, -146200, 4000, 79800, 165)
    SetChrChipByIndex(0xC, 1)
    SetChrChipByIndex(0xD, 1)
    SetChrChipByIndex(0xE, 1)
    SetChrChipByIndex(0xF, 1)
    OP_62(0x135, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_941():
        OP_8E(0x135, 0xFFFDD2F8, 0x834, 0x100A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x135, 2, lambda_941)
    OP_0D()
    OP_8C(0x11, 345, 400)
    OP_8C(0x12, 345, 400)
    OP_8C(0x13, 345, 400)
    Sleep(800)
    OP_8C(0x135, 345, 400)

    ChrTalk(
        0x13,
        (
            "#022F好了，还剩后面的。\x01",
            "集中精神！一鼓作气消灭它们！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9B8():

        label("loc_9B8")

        TurnDirection(0x11, 0xC, 0)
        OP_48()
        Jump("loc_9B8")

    QueueWorkItem2(0x11, 1, lambda_9B8)

    def lambda_9C9():

        label("loc_9C9")

        TurnDirection(0x13, 0xC, 0)
        OP_48()
        Jump("loc_9C9")

    QueueWorkItem2(0x13, 1, lambda_9C9)

    def lambda_9DA():

        label("loc_9DA")

        TurnDirection(0x12, 0xC, 0)
        OP_48()
        Jump("loc_9DA")

    QueueWorkItem2(0x12, 1, lambda_9DA)

    def lambda_9EB():
        OP_92(0xC, 0x10, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_9EB)
    Sleep(400)

    def lambda_A05():
        OP_92(0xD, 0x10, 0x7D0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_A05)
    Sleep(400)

    def lambda_A1F():
        OP_92(0xE, 0x10, 0xBB8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_A1F)
    Sleep(400)

    def lambda_A39():
        OP_92(0xF, 0x10, 0xFA0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_A39)
    Sleep(600)
    OP_44(0x101, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x135, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x12, 0xFF)
    Battle(0x3F0, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_A82"),
        (SWITCH_DEFAULT, "loc_A85"),
    )


    label("loc_A82")

    OP_B4(0x0)
    Return()

    label("loc_A85")

    EventBegin(0x0)
    OP_6D(-142180, 2040, 67240, 0)
    SetChrPos(0x101, -142200, 2000, 67300, 0)
    SetChrPos(0x103, -143500, 2000, 67900, 0)
    SetChrPos(0x102, -141300, 2000, 68600, 0)
    SetChrPos(0x135, -143500, 2000, 70600, 0)
    SetChrPos(0x135, -142600, 2100, 65700, 345)
    SetChrChipByIndex(0x101, 2)
    SetChrChipByIndex(0x102, 3)
    SetChrChipByIndex(0x103, 4)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x103, 0x80)
    OP_0D()
    Call(1, 2)
    Return()

    # Function_1_636 end

    def Function_2_B34(): pass

    label("Function_2_B34")

    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(
        0x101,
        "#007F呼……\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x102, 65535)
    TurnDirection(0x102, 0x103, 400)

    ChrTalk(
        0x102,
        "#014F总算是……\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x103, 65535)
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(
        0x103,
        "#020F……已经结束了呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        "呼呼～～～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        "得、得救了～～～\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x135, 400)

    def lambda_BCE():
        TurnDirection(0x102, 0x135, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BCE)
    OP_8C(0x101, 165, 400)

    ChrTalk(
        0x103,
        "#021F如何？我说没问题的吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        (
            "呼…………\x01",
            "不敢相信我竟然平安无事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        "呀，你们游击士真是太厉害了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        (
            "那样的魔兽\x01",
            "简单几下就收拾掉了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x135, 400)
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#001F嘿嘿㈱\x02\x03",
            "当然了，我的棒术用来对付魔兽，\x01",
            "可以说是一击必杀的哦。\x02\x03",
            "啊，对了。\x01",
            "我就给您专门来一场棒术表演吧⊙\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x1F4, 0x0, 0x64)
    OP_8C(0x101, 300, 2000)
    OP_8C(0x101, 75, 2000)
    OP_8C(0x101, 165, 2000)
    SetChrChipByIndex(0x101, 2)
    OP_43(0x101, 0x0, 0x0, 0x2)
    TurnDirection(0x103, 0x101, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_E47")

    ChrTalk(
        0x103,
        (
            "#022F好了，不要再得意忘形了。\x02\x03",
            "如果不是因为判断失误的话，\x01",
            "那些魔兽应该很好解决的。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0x0)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)
    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(
        0x101,
        "#007F呜呜……我知道错了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F嗯，就当作经验教训吧。\x02\x03",
            "那么，\x01",
            "我们就继续向目的地出发吧。\x02\x03",
            "还不知道魔兽\x01",
            "会不会再来袭击呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB2")

    label("loc_E47")


    ChrTalk(
        0x103,
        (
            "#026F好啦好啦，不用继续了，\x01",
            "以后有的是机会。\x02\x03",
            "我们就继续向目的地出发吧。\x01",
            "说不定还会有魔兽再来袭击呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EB2")

    TurnDirection(0x135, 0x103, 0)
    OP_62(0x135, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_95(0x135, 0x0, 0x0, 0x0, 0x320, 0x2EE0)

    ChrTalk(
        0x135,
        "那、那可就麻烦了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x135,
        "快、快点出发吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_F91")

    ChrTalk(
        0x102,
        (
            "#010F好啦，艾丝蒂尔，\x01",
            "我们继续赶路吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0x0)
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)
    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#007F嘁，知道啦～\x02",
    )

    CloseMessageWindow()

    label("loc_F91")


    ChrTalk(
        0x103,
        (
            "#020F关所就在前面不远了，\x01",
            "在到达之前可不要掉以轻心哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(
        0x101,
        "#006F好～的。\x02",
    )

    CloseMessageWindow()
    OP_28(0x10, 0x1, 0x4000)
    EventEnd(0x0)
    Return()

    # Function_2_B34 end

    def Function_3_FF0(): pass

    label("Function_3_FF0")

    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x102,
        "#014F艾丝蒂尔！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#023F不要分散了啊！\x02\x03",
            "#025F……唉，来不及了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x11,
        "#004F咦……？！\x02",
    )

    CloseMessageWindow()

    def lambda_10A1():
        OP_92(0x8, 0x101, 0x12C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_10A1)

    def lambda_10B6():
        OP_92(0x9, 0x101, 0xED8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_10B6)

    def lambda_10CB():
        OP_92(0xA, 0x101, 0x12C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_10CB)

    def lambda_10E0():
        OP_92(0xB, 0x101, 0x16A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_10E0)

    def lambda_10F5():
        OP_92(0xC, 0x11, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_10F5)

    def lambda_110A():
        OP_92(0xD, 0x11, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_110A)

    def lambda_111F():
        OP_92(0xE, 0x11, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_111F)

    def lambda_1134():
        OP_92(0xF, 0x11, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1134)
    WaitChrThread(0xB, 0x1)
    WaitChrThread(0xF, 0x1)
    OP_51(0x12, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x102, 0x80)
    TurnDirection(0x12, 0x9, 400)

    ChrTalk(
        0x12,
        "#013F完全被包围了……\x02",
    )

    CloseMessageWindow()
    OP_43(0x12, 0x3, 0x0, 0x2)
    OP_62(0x11, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x11,
        (
            "#509F难、难道是判断失误……！？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x13, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x103, 0x80)
    TurnDirection(0x13, 0x9, 400)

    ChrTalk(
        0x13,
        (
            "#022F待会儿再后悔吧。\x02\x03",
            "既然这样，\x01",
            "就只有下决心战斗到底了。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x13, 0x3, 0x0, 0x2)
    OP_44(0x8, 0x1)
    OP_44(0x9, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xC, 0x1)
    OP_44(0xD, 0x1)
    OP_44(0xE, 0x1)
    OP_44(0xF, 0x1)
    OP_43(0x9, 0x1, 0x1, 0x4)
    Sleep(200)
    OP_43(0xC, 0x1, 0x1, 0x5)
    OP_43(0x8, 0x1, 0x1, 0x4)
    Sleep(200)
    OP_43(0xF, 0x1, 0x1, 0x5)
    OP_43(0xA, 0x1, 0x1, 0x4)
    Sleep(200)
    OP_43(0xD, 0x1, 0x1, 0x5)
    OP_43(0xB, 0x1, 0x1, 0x4)
    Sleep(200)
    OP_43(0xE, 0x1, 0x1, 0x5)
    WaitChrThread(0xC, 0x1)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    OP_44(0x13, 0xFF)
    Battle(0x3F1, 0x0, 0x1, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_1322"),
        (SWITCH_DEFAULT, "loc_1325"),
    )


    label("loc_1322")

    OP_B4(0x0)
    Return()

    label("loc_1325")

    EventBegin(0x0)
    OP_6D(-142180, 2040, 67240, 0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x103, 0x80)
    SetChrPos(0x101, -142200, 2000, 67300, 0)
    SetChrPos(0x103, -143500, 2000, 67900, 0)
    SetChrPos(0x102, -141300, 2000, 68600, 0)
    SetChrPos(0x135, -143500, 2000, 70600, 0)
    SetChrPos(0x135, -142600, 2100, 65700, 345)
    SetChrChipByIndex(0x101, 2)
    SetChrChipByIndex(0x102, 3)
    SetChrChipByIndex(0x103, 4)
    OP_0D()
    Call(1, 2)
    Return()

    # Function_3_FF0 end

    def Function_4_13E8(): pass

    label("Function_4_13E8")

    SetChrChipByIndex(0xFE, 1)
    OP_8E(0xFE, 0xFFFDD302, 0x802, 0x10F72, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFDD046, 0x870, 0x1180A, 0x1388, 0x0)
    Return()

    # Function_4_13E8 end

    def Function_5_1416(): pass

    label("Function_5_1416")

    SetChrChipByIndex(0xFE, 1)
    OP_8E(0xFE, 0xFFFDC998, 0x102C, 0x13074, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFDCB8C, 0xF78, 0x12C6E, 0x1388, 0x0)
    Return()

    # Function_5_1416 end

    def Function_6_1444(): pass

    label("Function_6_1444")

    OP_A6(0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 1)
    OP_8E(0x8, 0xFFFDC420, 0x1E78, 0xF35C, 0x1388, 0x0)
    OP_8C(0x8, 165, 0)
    SetChrChipByIndex(0x8, 0)
    OP_22(0x81, 0x0, 0x50)
    OP_96(0x8, 0xFFFDC86C, 0x1A90, 0xE2F4, 0x9C4, 0x1388)
    OP_8C(0x8, 75, 0)
    ClearChrFlags(0x8, 0x4)
    OP_22(0x81, 0x0, 0x5A)
    OP_96(0x8, 0xFFFDCD80, 0x7D0, 0xF168, 0x9C4, 0x1388)
    SetChrChipByIndex(0x8, 1)

    def lambda_14C0():
        OP_6D(-143500, 2500, 73000, 2000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_14C0)
    OP_22(0x81, 0x0, 0x64)
    OP_8E(0x8, 0xFFFDDC58, 0x7D0, 0x10680, 0x1388, 0x0)
    SetChrChipByIndex(0x8, 0)
    OP_43(0x8, 0x3, 0x0, 0x2)
    TurnDirection(0x8, 0x0, 400)
    OP_A3(0x0)
    Return()

    # Function_6_1444 end

    def Function_7_1502(): pass

    label("Function_7_1502")

    OP_A6(0x1)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 1)
    OP_8E(0x9, 0xFFFDC420, 0x1E78, 0xF35C, 0x1388, 0x0)
    OP_8C(0x9, 165, 0)
    SetChrChipByIndex(0x8, 0)
    OP_96(0x9, 0xFFFDC86C, 0x1A90, 0xE2F4, 0x9C4, 0x1388)
    OP_8C(0x8, 75, 0)
    ClearChrFlags(0x9, 0x4)
    OP_96(0x9, 0xFFFDCD80, 0x7D0, 0xF168, 0x9C4, 0x1388)
    SetChrChipByIndex(0x9, 1)
    OP_22(0x81, 0x0, 0x64)
    OP_8E(0x9, 0xFFFDD550, 0x7D0, 0x109A0, 0x1388, 0x0)
    SetChrChipByIndex(0x9, 0)
    OP_43(0x9, 0x3, 0x0, 0x2)
    TurnDirection(0x9, 0x0, 400)
    OP_A3(0x1)
    Return()

    # Function_7_1502 end

    def Function_8_159E(): pass

    label("Function_8_159E")

    OP_A6(0x2)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 1)
    OP_8E(0xA, 0xFFFDC420, 0x1E78, 0xF35C, 0x1388, 0x0)
    OP_8C(0xA, 165, 0)
    SetChrChipByIndex(0xA, 0)
    OP_96(0xA, 0xFFFDC86C, 0x1A90, 0xE2F4, 0x9C4, 0x1388)
    OP_8C(0xA, 75, 0)
    ClearChrFlags(0xA, 0x4)
    OP_96(0xA, 0xFFFDCD80, 0x7D0, 0xF168, 0x9C4, 0x1388)
    SetChrChipByIndex(0xA, 1)
    OP_8E(0xA, 0xFFFDCF10, 0x7D0, 0x1048C, 0x1388, 0x0)
    SetChrChipByIndex(0xA, 0)
    OP_43(0xA, 0x3, 0x0, 0x2)
    TurnDirection(0xA, 0x0, 400)
    OP_A3(0x2)
    Return()

    # Function_8_159E end

    def Function_9_1635(): pass

    label("Function_9_1635")

    OP_A6(0x3)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 1)
    OP_8E(0xB, 0xFFFDC420, 0x1E78, 0xF35C, 0x1388, 0x0)
    OP_8C(0xB, 165, 0)
    SetChrChipByIndex(0xB, 0)
    OP_96(0xB, 0xFFFDC86C, 0x1A90, 0xE2F4, 0x9C4, 0x1388)
    OP_8C(0xB, 75, 0)
    ClearChrFlags(0xB, 0x4)
    OP_96(0xB, 0xFFFDCD80, 0x7D0, 0xF168, 0x9C4, 0x1388)
    SetChrChipByIndex(0xB, 1)
    OP_8E(0xB, 0xFFFDD6E0, 0x7D0, 0xFFDC, 0x1388, 0x0)
    SetChrChipByIndex(0xB, 0)
    OP_43(0xB, 0x3, 0x0, 0x2)
    TurnDirection(0xB, 0x0, 400)
    OP_A3(0x3)
    Return()

    # Function_9_1635 end

    def Function_10_16CC(): pass

    label("Function_10_16CC")

    OP_A6(0x4)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 1)
    OP_8E(0xC, 0xFFFDB7A0, 0x1AF4, 0x142A8, 0x1388, 0x0)
    OP_8C(0xC, 120, 0)
    SetChrChipByIndex(0xC, 0)
    ClearChrFlags(0xC, 0x4)
    OP_22(0x81, 0x0, 0x50)
    OP_96(0xC, 0xFFFDBB88, 0xFA0, 0x13880, 0x9C4, 0x1388)
    SetChrChipByIndex(0xC, 1)

    def lambda_1725():
        OP_6D(-143900, 2800, 74200, 3000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1725)
    OP_22(0x81, 0x0, 0x5A)
    OP_8E(0xC, 0xFFFDCF74, 0xFA0, 0x1381C, 0x1388, 0x0)
    SetChrChipByIndex(0xC, 0)
    OP_43(0xC, 0x3, 0x0, 0x2)
    TurnDirection(0xC, 0x0, 400)
    OP_A3(0x4)
    Return()

    # Function_10_16CC end

    def Function_11_1767(): pass

    label("Function_11_1767")

    OP_A6(0x5)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 1)
    OP_8E(0xD, 0xFFFDB7A0, 0x1AF4, 0x142A8, 0x1388, 0x0)
    OP_8C(0xD, 120, 0)
    SetChrChipByIndex(0xD, 0)
    ClearChrFlags(0xD, 0x4)
    OP_96(0xD, 0xFFFDBB88, 0xFA0, 0x13880, 0x9C4, 0x1388)
    SetChrChipByIndex(0xD, 1)
    OP_22(0x81, 0x0, 0x5A)
    OP_8E(0xD, 0xFFFDC740, 0xFA0, 0x139AC, 0x1388, 0x0)
    SetChrChipByIndex(0xD, 0)
    OP_43(0xD, 0x3, 0x0, 0x2)
    TurnDirection(0xD, 0x0, 400)
    OP_A3(0x5)
    Return()

    # Function_11_1767 end

    def Function_12_17E5(): pass

    label("Function_12_17E5")

    OP_A6(0x6)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 1)
    OP_8E(0xE, 0xFFFDB7A0, 0x1AF4, 0x142A8, 0x1388, 0x0)
    OP_8C(0xE, 120, 0)
    SetChrChipByIndex(0xE, 0)
    ClearChrFlags(0xE, 0x4)
    OP_96(0xE, 0xFFFDBB88, 0xFA0, 0x13880, 0x9C4, 0x1388)
    SetChrChipByIndex(0xE, 1)
    OP_22(0x81, 0x0, 0x5A)
    OP_8E(0xE, 0xFFFDC22C, 0xFA0, 0x1381C, 0x1388, 0x0)
    SetChrChipByIndex(0xE, 0)
    OP_43(0xE, 0x3, 0x0, 0x2)
    TurnDirection(0xE, 0x0, 400)
    OP_A3(0x6)
    Return()

    # Function_12_17E5 end

    def Function_13_1863(): pass

    label("Function_13_1863")

    OP_A6(0x7)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 1)
    OP_8E(0xF, 0xFFFDB7A0, 0x1AF4, 0x142A8, 0x1388, 0x0)
    OP_8C(0xF, 120, 0)
    SetChrChipByIndex(0xF, 0)
    ClearChrFlags(0xF, 0x4)
    OP_96(0xF, 0xFFFDBB88, 0xFA0, 0x13880, 0x9C4, 0x1388)
    SetChrChipByIndex(0xF, 1)
    OP_8E(0xF, 0xFFFDC164, 0xFA0, 0x13114, 0x1388, 0x0)
    SetChrChipByIndex(0xF, 0)
    OP_43(0xF, 0x3, 0x0, 0x2)
    TurnDirection(0xF, 0x0, 400)
    OP_A3(0x7)
    Return()

    # Function_13_1863 end

    SaveToFile()

Try(main)
