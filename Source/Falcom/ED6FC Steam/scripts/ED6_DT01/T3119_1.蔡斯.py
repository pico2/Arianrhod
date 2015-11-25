from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3119_1 ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3119.x',
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
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
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

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_207")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x100)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17E")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F刚才已经问过话了，\x01",
            "可是安东尼一点反应也没有。\x02\x03",
            "我们在工房里面再调查一下吧。\x01",
            "　\x02\x03",
            "照米妮亚姆医生说的，\x01",
            "在某个地方也许会有线索的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F唔……也只有这样了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FB")

    label("loc_17E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_194")
    TurnDirection(0x102, 0x1, 400)
    Jump("loc_19B")

    label("loc_194")

    TurnDirection(0x102, 0x0, 400)

    label("loc_19B")


    ChrTalk(
        0x102,
        (
            "#010F刚才已经问过话了，\x01",
            "安东尼一点反应也没有。\x02\x03",
            "我们还是去二楼\x01",
            "工房长的房间调查看看吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FB")

    TalkEnd(0xFE)
    ClearChrFlags(0xFE, 0x10)
    Return()

    label("loc_207")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_257")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "哦，怎么样了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我的嫌疑洗清了吧？\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_257")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(400, 0, 9640, 0)
    SetChrPos(0x101, 450, 0, 9220, 358)
    SetChrPos(0x102, 1650, 0, 9460, 322)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B0")
    SetChrPos(0x107, 1160, 0, 8750, 357)

    label("loc_2B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CF")
    SetChrPos(0x106, -720, 0, 8630, 37)

    label("loc_2CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EE")
    SetChrPos(0x13C, -590, 0, 9610, 42)

    label("loc_2EE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_308")

    def lambda_300():
        TurnDirection(0x0, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_300)

    label("loc_308")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_322")

    def lambda_31A():
        TurnDirection(0x1, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_31A)

    label("loc_322")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_33C")

    def lambda_334():
        TurnDirection(0x2, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_334)

    label("loc_33C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_356")

    def lambda_34E():
        TurnDirection(0x3, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_34E)

    label("loc_356")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_370")

    def lambda_368():
        TurnDirection(0x4, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_368)

    label("loc_370")

    TurnDirection(0x8, 0x101, 0)
    OP_4A(0xFE, 255)
    OP_0D()

    ChrTalk(
        0xFE,
        "哟，各位。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你们要找的东西找到了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，嗯。\x01",
            "虽说已经找到了……\x02\x03",
            "但是还需要找另外一件东西。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "另外一件东西？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯，\x01",
            "我们还要寻找被人从医务室里\x01",
            "拿出来的烟草。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "哦哦……\x01",
            "是这件事情啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀～\x01",
            "你们也真是很辛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F特莱斯主任您今天去过医务室吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没有，没有去过。\x01",
            "我今天一直都在这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果不相信的话，\x01",
            "可以对这间屋子进行搜查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F唔唔～\x01",
            "好像没什么可怀疑的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F是啊，白忙一场。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "怎么样？我的嫌疑洗清了吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F非常抱歉，\x01",
            "在您百忙之中前来打扰。\x02\x03",
            "可以的话，\x01",
            "今后还要请您协助调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊，当然没问题。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 400)
    OP_4B(0xFE, 255)
    OP_28(0x2C, 0x1, 0x20)
    Jump("loc_E81")

    label("loc_5EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_890")
    EventBegin(0x0)
    OP_4A(0xFE, 255)
    Fade(1000)
    OP_6D(400, 0, 9640, 0)
    SetChrPos(0x101, 450, 0, 9220, 358)
    SetChrPos(0x102, 1650, 0, 9460, 322)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_654")
    SetChrPos(0x107, 1160, 0, 8750, 357)

    label("loc_654")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_673")
    SetChrPos(0x106, -720, 0, 8630, 37)

    label("loc_673")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_692")
    SetChrPos(0x13C, -590, 0, 9610, 42)

    label("loc_692")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6AC")

    def lambda_6A4():
        TurnDirection(0x0, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_6A4)

    label("loc_6AC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C6")

    def lambda_6BE():
        TurnDirection(0x1, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_6BE)

    label("loc_6C6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E0")

    def lambda_6D8():
        TurnDirection(0x2, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_6D8)

    label("loc_6E0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6FA")

    def lambda_6F2():
        TurnDirection(0x3, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_6F2)

    label("loc_6FA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_714")

    def lambda_70C():
        TurnDirection(0x4, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_70C)

    label("loc_714")

    TurnDirection(0x8, 0x101, 400)
    OP_0D()

    ChrTalk(
        0xFE,
        "哦，怎么样了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我的嫌疑洗清了吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F不好意思。\x01",
            "很快就会结束的。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_774():
        TurnDirection(0x102, 0x13C, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_774)

    def lambda_782():
        TurnDirection(0x107, 0x13C, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_782)
    TurnDirection(0x101, 0x13C, 400)

    ChrTalk(
        0x13C,
        "…………………………\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    TurnDirection(0x13C, 0x101, 400)

    ChrTalk(
        0x13C,
        "………………喵噢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#063F没有反应呢～\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xFE, 400)

    ChrTalk(
        0x102,
        (
            "#010F抱歉打扰了。\x02\x03",
            "谢谢您配合我们工作。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_820():
        TurnDirection(0x107, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_820)
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(
        0x101,
        "#000F那么再见了～\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0xFE,
        "到、到底怎么回事啊？\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 400)
    OP_4B(0xFE, 255)
    OP_28(0x2C, 0x1, 0x40)
    Jump("loc_D0C")

    label("loc_890")

    EventBegin(0x0)
    OP_4A(0xFE, 255)
    Fade(1000)
    OP_6D(400, 0, 9640, 0)
    SetChrPos(0x101, 450, 0, 9220, 358)
    SetChrPos(0x102, 1650, 0, 9460, 322)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8ED")
    SetChrPos(0x107, 1160, 0, 8750, 357)

    label("loc_8ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_90C")
    SetChrPos(0x106, -720, 0, 8630, 37)

    label("loc_90C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_92B")
    SetChrPos(0x13C, -590, 0, 9610, 42)

    label("loc_92B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_945")

    def lambda_93D():
        TurnDirection(0x0, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_93D)

    label("loc_945")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_95F")

    def lambda_957():
        TurnDirection(0x1, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_957)

    label("loc_95F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_979")

    def lambda_971():
        TurnDirection(0x2, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_971)

    label("loc_979")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_993")

    def lambda_98B():
        TurnDirection(0x3, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_98B)

    label("loc_993")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9AD")

    def lambda_9A5():
        TurnDirection(0x4, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_9A5)

    label("loc_9AD")

    TurnDirection(0x8, 0x101, 400)
    OP_0D()

    ChrTalk(
        0xFE,
        "哟，各位。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你们要找的东西找到了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，嗯。\x01",
            "虽说已经找到了……\x02\x03",
            "但是还需要找另外一件东西。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "另外一件东西？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯，\x01",
            "我们还要寻找被人从医务室里\x01",
            "拿出来的烟草。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "哦哦……\x01",
            "是这件事情啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀～\x01",
            "你们也真是很辛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F特莱斯主任您今天去过医务室吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没有，没有去过。\x01",
            "我今天一直都在这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果不相信的话，\x01",
            "可以对这间屋子进行搜查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F唔唔～\x01",
            "好像没什么可怀疑的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F是啊，白忙一场。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "怎么样？我的嫌疑洗清了吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F啊，对了。\x01",
            "安东尼，如何？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BD6():
        TurnDirection(0x102, 0x13C, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BD6)

    def lambda_BE4():
        TurnDirection(0x107, 0x13C, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_BE4)
    TurnDirection(0x101, 0x13C, 400)

    ChrTalk(
        0x13C,
        "…………………………\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    TurnDirection(0x13C, 0x101, 400)

    ChrTalk(
        0x13C,
        "………………喵噢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#063F没有反应呢～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F哎呀，\x01",
            "这么说来果真是预料落空了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xFE, 400)

    ChrTalk(
        0x102,
        (
            "#010F非常抱歉，\x01",
            "在您百忙之中前来打扰。\x02\x03",
            "可以的话，\x01",
            "今后还要请您协助调查。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CD0():
        TurnDirection(0x107, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_CD0)
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(
        0xFE,
        "啊，当然没问题。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 400)
    OP_4B(0xFE, 255)
    OP_28(0x2C, 0x1, 0x20)
    OP_28(0x2C, 0x1, 0x40)

    label("loc_D0C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_E81")

    def lambda_D1D():
        TurnDirection(0x102, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D1D)
    TurnDirection(0x101, 0x102, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x100)"), scpexpr(EXPR_END)), "loc_DC0")

    ChrTalk(
        0x101,
        (
            "#505F唔～对两个人都没有反应呢。\x02\x03",
            "还是去刚才安东尼\x01",
            "有反应的地方调查一下吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是二楼工房长的房间对吧。\x02\x03",
            "我们赶快去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E7B")

    label("loc_DC0")


    ChrTalk(
        0x101,
        (
            "#505F唔～\x01",
            "对两个人都没有反应呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F也就是说没有线索了。\x02\x03",
            "#010F我们到工房里面再调查一下吧。\x01",
            "　\x02\x03",
            "照米妮亚姆医生说的，\x01",
            "在某个地方也许会有线索的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F唔……也只有这样了。\x02",
    )

    CloseMessageWindow()

    label("loc_E7B")

    OP_28(0x2C, 0x1, 0x80)

    label("loc_E81")

    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_2_AC end

    SaveToFile()

Try(main)
