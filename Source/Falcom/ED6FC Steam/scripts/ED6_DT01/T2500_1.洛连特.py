from ED6ScenarioHelper import *

def main():
    # 洛连特

    CreateScenaFile(
        FileName            = 'T2500_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T2500.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
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
        "Function_1_30E",          # 01, 1
        "Function_2_BF8",          # 02, 2
        "Function_3_15B9",         # 03, 3
    )


    def Function_0_66(): pass

    label("Function_0_66")

    EventBegin(0x0)
    Fade(1000)
    OP_6C(135000, 0)
    OP_0D()

    ChrTalk(
        0xFE,
        "呼，难办啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样下去校园的装饰\x01",
            "就完成不了了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "想要找人帮忙，\x01",
            "但是学生们现在都很忙啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 135, 400)

    ChrTalk(
        0xFE,
        (
            "你们看吧，\x01",
            "还有一些没能装饰到的地方。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_119():
        OP_6D(49960, 1500, 53870, 2000)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_119)
    Sleep(100)
    OP_8B(0x101, 0xC328, 0xD26E, 0x190)
    Sleep(150)
    OP_8B(0x105, 0xC328, 0xD26E, 0x190)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16A")
    OP_8B(0x13B, 0xC328, 0xD26E, 0x190)

    label("loc_16A")

    WaitChrThread(0xFE, 0x1)

    ChrTalk(
        0x101,
        (
            "#004F哎呀……\x01",
            "正中间没有垂幕啊。\x02\x03",
            "#003F唔～\x01",
            "的确有些不好看。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "对吧？\x02",
    )

    CloseMessageWindow()

    def lambda_1CA():
        OP_69(0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1CA)
    Sleep(100)
    TurnDirection(0x101, 0xFE, 400)
    Sleep(100)
    TurnDirection(0x105, 0xFE, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FF")
    TurnDirection(0x13B, 0xFE, 400)

    label("loc_1FF")

    WaitChrThread(0xFE, 0x1)

    ChrTalk(
        0xFE,
        (
            "如果看到没有装饰的地方，\x01",
            "还请告诉我一声。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我会很快过去，\x01",
            "把它给弄好的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只要稍微注意一下\x01",
            "应该就可以发现的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F这么说，\x01",
            "只要找到像这样\x01",
            "还没装饰的地方就可以了吧。\x02\x03",
            "嗯，明白了。\x01",
            "如果看到了就回来告诉您。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊，那就拜托了。\x02",
    )

    CloseMessageWindow()
    OP_28(0x27, 0x1, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    OP_65(0x5, 0x1)
    EventEnd(0x1)
    Return()

    # Function_0_66 end

    def Function_1_30E(): pass

    label("Function_1_30E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF4")
    EventBegin(0x0)
    Fade(1000)
    OP_6C(225000, 0)
    SetChrPos(0x101, 21320, 250, 26540, 180)
    SetChrPos(0x105, 21880, 0, 27550, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36B")
    SetChrPos(0x13B, 20790, 0, 27100, 180)

    label("loc_36B")

    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#004F哎……？\x02\x03",
            "这里没有彩旗吗……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C5")
    TurnDirection(0x101, 0x13B, 400)
    Jump("loc_3CC")

    label("loc_3C5")

    TurnDirection(0x101, 0x105, 400)

    label("loc_3CC")


    ChrTalk(
        0x101,
        (
            "#002F你看，其他建筑物的门口\x01",
            "不都有挂上彩旗的吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_48F")

    ChrTalk(
        0x13B,
        (
            "#643F啊，\x01",
            "这样说的话好像真的是这样。\x02\x03",
            "这个地方应该是还没有装饰好。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F我们去告诉\x01",
            "勤务员巴克斯师傅吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)
    Jump("loc_4E1")

    label("loc_48F")


    ChrTalk(
        0x105,
        (
            "#044F啊，真的呢。\x01",
            "好像还没有装饰到呢。\x02\x03",
            "#040F我们去告诉\x01",
            "勤务员巴克斯师傅吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E1")


    ChrTalk(
        0x101,
        "#000F嗯，好的。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x15, 30130, 0, 28910, 270)
    SetChrPos(0x101, 22450, 0, 27570, 180)
    SetChrPos(0x105, 21590, 0, 28160, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_553")
    SetChrPos(0x13B, 20300, 0, 27960, 90)

    label("loc_553")

    OP_8C(0x101, 90, 0)
    OP_8C(0x105, 90, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_576")
    OP_8C(0x13B, 90, 0)

    label("loc_576")

    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    SetChrFlags(0x15, 0x40)
    OP_8E(0x15, 0x5F3C, 0x0, 0x6CC0, 0xBB8, 0x0)
    OP_8E(0x15, 0x5BEA, 0x0, 0x6A5E, 0xBB8, 0x0)
    OP_4A(0x15, 255)
    Sleep(400)
    OP_8C(0x15, 225, 400)
    OP_62(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0x15,
        (
            "啊，果然。\x01",
            "很会观察嘛。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x101, 400)

    ChrTalk(
        0x15,
        (
            "好，\x01",
            "我这就开始装饰。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_660")
    TurnDirection(0x13B, 0x101, 400)

    ChrTalk(
        0x13B,
        "#644F我们也来帮忙吧。\x02",
    )

    CloseMessageWindow()

    def lambda_64E():
        TurnDirection(0x105, 0x13B, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_64E)
    TurnDirection(0x101, 0x13B, 400)
    Jump("loc_685")

    label("loc_660")


    ChrTalk(
        0x105,
        (
            "#040F我们也来帮忙吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    label("loc_685")


    ChrTalk(
        0x101,
        "#000F嗯，好的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "啊，谢谢了。\x02",
    )

    CloseMessageWindow()

    def lambda_6B2():
        TurnDirection(0x105, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6B2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D6")

    def lambda_6CE():
        TurnDirection(0x13B, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_6CE)

    label("loc_6D6")

    TurnDirection(0x101, 0x15, 400)

    ChrTalk(
        0x15,
        (
            "那么就\x01",
            "有劳你们了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6FC():
        OP_8E(0x101, 0x57B2, 0x0, 0x6658, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6FC)

    def lambda_717():
        OP_8E(0x105, 0x5456, 0x0, 0x6720, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_717)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_755")

    def lambda_740():
        OP_8E(0x13B, 0x5154, 0xFA, 0x65A4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_740)

    label("loc_755")


    def lambda_75B():
        OP_8E(0x15, 0x5AB4, 0xFA, 0x65B8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_75B)

    def lambda_776():
        OP_6C(135000, 2500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_776)
    OP_6D(22030, 3500, 24930, 1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x105, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7B9")
    WaitChrThread(0x13B, 0x1)

    label("loc_7B9")

    WaitChrThread(0x15, 0x1)
    Sleep(400)
    OP_72(0x1E, 0x4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    Sleep(400)
    OP_28(0x27, 0x1, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AA4")

    ChrTalk(
        0x15,
        (
            "……好。\x01",
            "这样就行了。\x02",
        )
    )

    CloseMessageWindow()
    OP_69(0x101, 0x5DC)
    TurnDirection(0x15, 0x101, 400)

    ChrTalk(
        0x15,
        (
            "呼……\x01",
            "总算是全部解决了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "哎呀～\x01",
            "让你们费心了啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_868():
        TurnDirection(0x105, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_868)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_88C")

    def lambda_884():
        TurnDirection(0x13B, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_884)

    label("loc_88C")

    TurnDirection(0x101, 0x15, 400)

    ChrTalk(
        0x101,
        (
            "#000F没什么，不用介意。\x02\x03",
            "好不容易才有一次学园祭，\x01",
            "不好好准备一下怎么能行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F嗯，是啊。\x02\x03",
            "既然是我们大家的节日，\x01",
            "帮帮忙那是应该的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_96C")
    TurnDirection(0x13B, 0x105, 400)

    ChrTalk(
        0x13B,
        (
            "#644F不愧是科洛丝。\x01",
            "真是说出了我们的心声啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_96C")


    ChrTalk(
        0x15,
        (
            "哈哈～\x01",
            "的确如此啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13B, 0x15, 400)

    ChrTalk(
        0x15,
        (
            "我们也很期待\x01",
            "明天的学园祭呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯！交给我们吧！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9FF")

    ChrTalk(
        0x13B,
        (
            "#649F呵呵，\x01",
            "那就请拭目以待了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A1C")

    label("loc_9FF")


    ChrTalk(
        0x105,
        "#040F我们会竭尽全力的。\x02",
    )

    CloseMessageWindow()

    label("loc_A1C")


    ChrTalk(
        0x15,
        (
            "那么，\x01",
            "你们要好好加油哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x27, 0x1, 0x10)
    OP_28(0x3D, 0x1, 0x200)
    OP_2C(0x3D, 0x1F4)
    OP_2B(0x3D, 0x1)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "学园祭的校园任务\x01",
            "【装饰校园】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jump("loc_B51")

    label("loc_AA4")


    ChrTalk(
        0x15,
        (
            "……好。\x01",
            "这样就行了。\x02",
        )
    )

    CloseMessageWindow()
    OP_69(0x101, 0x5DC)
    TurnDirection(0x15, 0x101, 400)

    ChrTalk(
        0x15,
        (
            "那，如果再看到的话，\x01",
            "也麻烦告诉我。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AFC():
        TurnDirection(0x105, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AFC)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B20")

    def lambda_B18():
        TurnDirection(0x13B, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_B18)

    label("loc_B20")

    TurnDirection(0x101, 0x15, 400)

    ChrTalk(
        0x101,
        "#006F嗯，放心吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F知道了。\x02",
    )

    CloseMessageWindow()

    label("loc_B51")


    def lambda_B57():

        label("loc_B57")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_B57")

    QueueWorkItem2(0x0, 1, lambda_B57)

    def lambda_B68():

        label("loc_B68")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_B68")

    QueueWorkItem2(0x1, 1, lambda_B68)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B92")

    def lambda_B87():

        label("loc_B87")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_B87")

    QueueWorkItem2(0x2, 1, lambda_B87)

    label("loc_B92")

    OP_8E(0x15, 0x6086, 0x0, 0x6E6E, 0xBB8, 0x0)
    OP_8E(0x15, 0x7A30, 0x0, 0x6D60, 0xBB8, 0x0)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BD4")
    OP_44(0x2, 0xFF)

    label("loc_BD4")

    SetChrPos(0x15, 47880, 0, 56070, 135)
    ClearChrFlags(0x15, 0x40)
    OP_4B(0x15, 255)
    OP_64(0x3, 0x1)
    EventEnd(0x0)

    label("loc_BF4")

    TalkEnd(0xFF)
    Return()

    # Function_1_30E end

    def Function_2_BF8(): pass

    label("Function_2_BF8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15B5")
    EventBegin(0x0)
    Fade(1000)
    OP_6C(45000, 0)
    SetChrPos(0x101, 38970, 0, 68950, 90)
    SetChrPos(0x105, 40770, 0, 68550, 45)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C55")
    SetChrPos(0x13B, 38560, 0, 70140, 90)

    label("loc_C55")

    OP_0D()
    OP_62(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0x105,
        "#044F咦……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C9C")

    def lambda_C94():
        TurnDirection(0x13B, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_C94)

    label("loc_C9C")

    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        "#000F怎么了？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        (
            "#044F这里……\x01",
            "按理说这也应该是挂垂幕的地方啊。\x01",
            "　\x02\x03",
            "门的另外一边是挂好了的……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 0, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D36")

    def lambda_D2E():
        OP_8C(0x13B, 0, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_D2E)

    label("loc_D36")

    OP_8C(0x101, 0, 400)
    OP_6D(41580, 2000, 73990, 1500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D76")

    ChrTalk(
        0x13B,
        "#643F啊，没错……\x02",
    )

    CloseMessageWindow()
    Jump("loc_D8D")

    label("loc_D76")


    ChrTalk(
        0x101,
        "#004F啊，真的呢。\x02",
    )

    CloseMessageWindow()

    label("loc_D8D")

    OP_69(0x105, 0x5DC)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DB5")
    Sleep(100)

    def lambda_DAD():
        TurnDirection(0x13B, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_DAD)

    label("loc_DB5")

    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        (
            "#000F那好，\x01",
            "我们去告诉巴克斯师傅吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        "#040F嗯，好的。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x15, 45200, 0, 65300, 270)
    SetChrPos(0x101, 39140, 0, 69780, 135)
    SetChrPos(0x105, 38830, 0, 68410, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E64")
    Sleep(100)
    SetChrPos(0x13B, 37730, 0, 69120, 135)

    label("loc_E64")

    OP_69(0x101, 0x0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_E80():

        label("loc_E80")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_E80")

    QueueWorkItem2(0x0, 1, lambda_E80)

    def lambda_E91():

        label("loc_E91")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_E91")

    QueueWorkItem2(0x1, 1, lambda_E91)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EBB")

    def lambda_EB0():

        label("loc_EB0")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_EB0")

    QueueWorkItem2(0x2, 1, lambda_EB0)

    label("loc_EBB")

    SetChrFlags(0x15, 0x40)
    OP_8E(0x15, 0x9FE2, 0x0, 0x1046E, 0xBB8, 0x0)
    OP_8E(0x15, 0x9F42, 0x0, 0x10BC6, 0xBB8, 0x0)
    OP_4A(0x15, 255)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F06")
    OP_44(0x2, 0xFF)

    label("loc_F06")

    Sleep(400)
    OP_8C(0x15, 45, 400)
    OP_62(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0x15,
        (
            "啊，\x01",
            "这里很明显呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x101, 400)

    ChrTalk(
        0x15,
        (
            "那么我这就\x01",
            "开始装饰吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F9B")

    ChrTalk(
        0x13B,
        "#644F好，我们也来帮忙。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x13B, 400)
    Jump("loc_FC4")

    label("loc_F9B")

    TurnDirection(0x101, 0x15, 400)

    ChrTalk(
        0x101,
        "#000F我们也来帮忙吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x101, 400)

    label("loc_FC4")


    ChrTalk(
        0x15,
        "哦，有劳了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "那就拜托了。\x02",
    )

    CloseMessageWindow()

    def lambda_FEE():
        OP_6C(135000, 4000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_FEE)

    def lambda_FFE():
        OP_8E(0x101, 0xA028, 0x0, 0x111FC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FFE)

    def lambda_1019():
        OP_8E(0x105, 0x9F42, 0x0, 0x10BC6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1019)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1057")

    def lambda_1042():
        OP_8E(0x13B, 0x9CC2, 0x0, 0x10F04, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_1042)

    label("loc_1057")


    def lambda_105D():
        OP_6D(41770, 3500, 69260, 4000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_105D)
    OP_8E(0x15, 0x9FE2, 0x0, 0x107AC, 0x7D0, 0x0)
    OP_8E(0x15, 0x9506, 0x0, 0x109A0, 0x7D0, 0x0)
    FadeToDark(1000, 0, -1)
    OP_8E(0x15, 0x959C, 0x0, 0x11A9E, 0xBB8, 0x0)
    OP_72(0x5, 0x2)
    OP_6F(0x5, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x105, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10DF")
    WaitChrThread(0x13B, 0x1)

    label("loc_10DF")

    WaitChrThread(0x15, 0x1)
    WaitChrThread(0x15, 0x2)
    OP_72(0x12, 0x4)
    SetChrFlags(0x15, 0x40)
    SetChrPos(0x15, 43990, 0, 73850, 270)
    OP_6F(0x5, 60)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_112A")
    SetChrPos(0x13B, 41160, 0, 69290, 90)

    label("loc_112A")

    FadeToBright(1000, 0)
    OP_8E(0x15, 0xA258, 0x1F4, 0x121EC, 0xBB8, 0x0)
    OP_72(0x5, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)
    OP_8E(0x15, 0x959C, 0x0, 0x11A9E, 0xBB8, 0x0)
    OP_8E(0x15, 0x9470, 0x0, 0x10BC6, 0xBB8, 0x0)
    OP_8C(0x15, 90, 400)
    OP_71(0x5, 0x800)
    Sleep(400)
    OP_28(0x27, 0x1, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1460")

    ChrTalk(
        0x15,
        (
            "……好。\x01",
            "这样就行了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x101, 400)

    def lambda_11E1():
        TurnDirection(0x105, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_11E1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1205")

    def lambda_11FD():
        TurnDirection(0x13B, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_11FD)

    label("loc_1205")

    TurnDirection(0x101, 0x15, 400)
    OP_69(0x101, 0x5DC)

    ChrTalk(
        0x15,
        (
            "呼……\x01",
            "总算是全部解决了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "哎呀～\x01",
            "让你们费心了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F没什么，不用介意。\x02\x03",
            "好不容易才有一次学园祭，\x01",
            "不好好准备一下怎么能行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F嗯，是啊。\x02\x03",
            "既然是我们大家的节日，\x01",
            "帮帮忙那是应该的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1328")
    TurnDirection(0x13B, 0x105, 400)

    ChrTalk(
        0x13B,
        (
            "#644F不愧是科洛丝。\x01",
            "真是说出了我们的心声啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1328")


    ChrTalk(
        0x15,
        (
            "哈哈～\x01",
            "的确如此啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13B, 0x15, 400)

    ChrTalk(
        0x15,
        (
            "我们也很期待\x01",
            "明天的学园祭呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯！交给我们吧！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13BB")

    ChrTalk(
        0x13B,
        (
            "#649F呵呵，\x01",
            "那就请拭目以待了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13D8")

    label("loc_13BB")


    ChrTalk(
        0x105,
        "#040F我们会竭尽全力的。\x02",
    )

    CloseMessageWindow()

    label("loc_13D8")


    ChrTalk(
        0x15,
        (
            "那么，\x01",
            "你们要好好加油哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x27, 0x1, 0x10)
    OP_28(0x3D, 0x1, 0x200)
    OP_2C(0x3D, 0x1F4)
    OP_2B(0x3D, 0x1)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "学园祭的校园任务\x01",
            "【装饰校园】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jump("loc_150D")

    label("loc_1460")


    ChrTalk(
        0x15,
        (
            "……好。\x01",
            "这样就行了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1481():
        TurnDirection(0x105, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1481)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14A5")

    def lambda_149D():
        TurnDirection(0x13B, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_149D)

    label("loc_14A5")

    TurnDirection(0x101, 0x15, 400)
    OP_69(0x101, 0x5DC)
    TurnDirection(0x15, 0x101, 400)

    ChrTalk(
        0x15,
        (
            "那，如果再看到的话，\x01",
            "也麻烦告诉我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，放心吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F知道了。\x02",
    )

    CloseMessageWindow()

    label("loc_150D")


    def lambda_1513():

        label("loc_1513")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_1513")

    QueueWorkItem2(0x0, 1, lambda_1513)

    def lambda_1524():

        label("loc_1524")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_1524")

    QueueWorkItem2(0x1, 1, lambda_1524)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_154E")

    def lambda_1543():

        label("loc_1543")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_1543")

    QueueWorkItem2(0x2, 1, lambda_1543)

    label("loc_154E")

    SetChrFlags(0x15, 0x40)
    OP_8E(0x15, 0x9B6E, 0x0, 0xFF32, 0xBB8, 0x0)
    OP_8E(0x15, 0xB4C8, 0x0, 0xFF3C, 0xBB8, 0x0)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1595")
    OP_44(0x2, 0xFF)

    label("loc_1595")

    SetChrPos(0x15, 47880, 0, 56070, 135)
    ClearChrFlags(0x15, 0x40)
    OP_4B(0x15, 255)
    OP_64(0x4, 0x1)
    EventEnd(0x0)

    label("loc_15B5")

    TalkEnd(0xFF)
    Return()

    # Function_2_BF8 end

    def Function_3_15B9(): pass

    label("Function_3_15B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2055")
    OP_28(0x27, 0x1, 0x8)
    EventBegin(0x0)
    Fade(1000)
    OP_6C(270000, 0)
    SetChrPos(0x101, 53860, 0, 28500, 90)
    SetChrPos(0x105, 53290, 0, 29520, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_161C")
    SetChrPos(0x13B, 52540, 0, 30290, 90)

    label("loc_161C")

    OP_69(0x101, 0x0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#004F哎……？\x02\x03",
            "啊，难道……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    OP_94(0x1, 0x101, 0xB4, 0x3E8, 0x7D0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1693")

    def lambda_1686():
        TurnDirection(0x13B, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_1686)
    Sleep(150)

    label("loc_1693")

    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        "#040F怎么了呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F这里没有彩旗。\x02",
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_16D3():

        label("loc_16D3")

        TurnDirection(0x105, 0x101, 0)
        OP_48()
        Jump("loc_16D3")

    QueueWorkItem2(0x105, 1, lambda_16D3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16FD")

    def lambda_16F2():

        label("loc_16F2")

        TurnDirection(0x13B, 0x101, 0)
        OP_48()
        Jump("loc_16F2")

    QueueWorkItem2(0x13B, 1, lambda_16F2)

    label("loc_16FD")

    OP_8E(0x101, 0xC80A, 0x0, 0x6C3E, 0x1770, 0x0)
    Sleep(100)
    Fade(1000)
    OP_6C(135000, 0)
    OP_6D(51210, 0, 27710, 0)
    Sleep(100)
    OP_8C(0x101, 90, 400)
    Sleep(400)

    ChrTalk(
        0x101,
        "#000F你看，反面却是有的。\x02",
    )

    CloseMessageWindow()
    OP_44(0x105, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1796")
    OP_44(0x13B, 0x1)

    def lambda_1781():
        OP_8E(0x13B, 0xCD96, 0x0, 0x73A0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_1781)

    label("loc_1796")

    OP_8E(0x105, 0xCCCE, 0x0, 0x6C66, 0xBB8, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17C6")

    def lambda_17BE():
        OP_8C(0x13B, 315, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_17BE)

    label("loc_17C6")

    OP_8C(0x105, 315, 400)
    Sleep(200)
    OP_8C(0x105, 180, 400)
    Sleep(200)
    OP_62(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x105, 0x101, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1857")

    ChrTalk(
        0x105,
        "#044F啊，真的呢。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13B, 0x101, 400)

    ChrTalk(
        0x13B,
        (
            "#643F不愧是游击士，\x01",
            "观察得这么仔细。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x13B, 400)
    Jump("loc_1890")

    label("loc_1857")


    ChrTalk(
        0x105,
        (
            "#044F啊，真的呢。\x02\x03",
            "艾丝蒂尔，\x01",
            "你很会观察啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    label("loc_1890")


    ChrTalk(
        0x101,
        (
            "#001F嘿嘿，还好啦。\x02\x03",
            "那好，\x01",
            "我们去告诉巴克斯师傅吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#041F嗯，走吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x15, 49850, 0, 28600, 90)
    SetChrPos(0x101, 55720, 0, 29180, 270)
    SetChrPos(0x105, 55170, 0, 30090, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_193C")
    SetChrPos(0x13B, 56220, 0, 30860, 270)

    label("loc_193C")

    Sleep(1000)
    FadeToBright(1000, 0)
    OP_6C(270000, 0)
    OP_6D(54350, 0, 28820, 0)
    OP_0D()

    def lambda_196B():

        label("loc_196B")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_196B")

    QueueWorkItem2(0x0, 1, lambda_196B)

    def lambda_197C():

        label("loc_197C")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_197C")

    QueueWorkItem2(0x1, 1, lambda_197C)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19A6")

    def lambda_199B():

        label("loc_199B")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_199B")

    QueueWorkItem2(0x2, 1, lambda_199B)

    label("loc_19A6")

    SetChrFlags(0x15, 0x40)
    OP_8E(0x15, 0xD598, 0x0, 0x6F04, 0xBB8, 0x0)
    OP_4A(0x15, 255)
    Sleep(400)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19E2")
    OP_44(0x2, 0xFF)

    label("loc_19E2")

    OP_8C(0x15, 270, 400)
    OP_62(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0x15,
        (
            "哦，\x01",
            "这样的细节也能发现啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x101, 400)

    ChrTalk(
        0x15,
        (
            "真是很不起眼的地方呢。\x01",
            "我这就开始装饰吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AB6")

    ChrTalk(
        0x13B,
        "#644F那我们也来帮忙吧。\x02",
    )

    CloseMessageWindow()

    def lambda_1A88():
        TurnDirection(0x105, 0x13B, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1A88)
    TurnDirection(0x101, 0x13B, 400)

    ChrTalk(
        0x105,
        "#040F嗯，当然。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x13B, 400)
    Jump("loc_1AFA")

    label("loc_1AB6")

    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        "#000F好的，我们也来帮忙吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        "#040F嗯，好的。\x02",
    )

    CloseMessageWindow()

    label("loc_1AFA")


    ChrTalk(
        0x15,
        "抱歉，又麻烦你们了。\x02",
    )

    CloseMessageWindow()

    def lambda_1B1A():
        OP_8E(0x15, 0xD764, 0x0, 0x6054, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1B1A)

    def lambda_1B35():
        OP_8E(0x101, 0xDAFC, 0x0, 0x7CD8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B35)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B91")

    def lambda_1B5E():
        OP_8E(0x13B, 0xD7AA, 0x0, 0x7D77, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_1B5E)

    def lambda_1B79():
        OP_8E(0x105, 0xDAD4, 0x0, 0x646E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1B79)
    Jump("loc_1BAC")

    label("loc_1B91")


    def lambda_1B97():
        OP_8E(0x105, 0xD7AA, 0x0, 0x7D77, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1B97)

    label("loc_1BAC")

    OP_6D(54350, 1500, 28820, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x15, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0x105, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BE6")
    OP_44(0x13B, 0x1)

    label("loc_1BE6")

    OP_72(0x1A, 0x4)
    SetChrPos(0x101, 55720, 0, 29180, 270)
    SetChrPos(0x105, 55170, 0, 30090, 270)
    SetChrPos(0x15, 56700, 0, 27700, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C3D")
    SetChrPos(0x13B, 57090, 0, 30560, 270)

    label("loc_1C3D")

    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_28(0x27, 0x1, 0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F14")

    ChrTalk(
        0x15,
        (
            "……好。\x01",
            "这样就行了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x101, 400)

    def lambda_1C95():
        TurnDirection(0x105, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1C95)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CB9")

    def lambda_1CB1():
        TurnDirection(0x13B, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_1CB1)

    label("loc_1CB9")

    TurnDirection(0x101, 0x15, 400)
    OP_69(0x101, 0x5DC)

    ChrTalk(
        0x15,
        (
            "呼……\x01",
            "总算是全部解决了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "哎呀～\x01",
            "让你们费心了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F没什么，不用介意。\x02\x03",
            "好不容易才有一次学园祭，\x01",
            "不好好准备一下怎么能行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F嗯，是啊。\x02\x03",
            "既然是我们大家的节日，\x01",
            "帮帮忙那是应该的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DDC")
    TurnDirection(0x13B, 0x105, 400)

    ChrTalk(
        0x13B,
        (
            "#644F不愧是科洛丝。\x01",
            "真是说出了我们的心声啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DDC")


    ChrTalk(
        0x15,
        (
            "哈哈～\x01",
            "的确如此啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13B, 0x15, 400)

    ChrTalk(
        0x15,
        (
            "我们也很期待\x01",
            "明天的学园祭呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯！交给我们吧！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E6F")

    ChrTalk(
        0x13B,
        (
            "#649F呵呵，\x01",
            "那就请拭目以待了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E8C")

    label("loc_1E6F")


    ChrTalk(
        0x105,
        "#040F我们会竭尽全力的。\x02",
    )

    CloseMessageWindow()

    label("loc_1E8C")


    ChrTalk(
        0x15,
        (
            "那么，\x01",
            "你们要好好加油哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x27, 0x1, 0x10)
    OP_28(0x3D, 0x1, 0x200)
    OP_2C(0x3D, 0x1F4)
    OP_2B(0x3D, 0x1)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "学园祭的校园任务\x01",
            "【装饰校园】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jump("loc_1FC1")

    label("loc_1F14")


    ChrTalk(
        0x15,
        (
            "……好。\x01",
            "这样就行了。\x02",
        )
    )

    CloseMessageWindow()
    OP_69(0x101, 0x5DC)
    TurnDirection(0x15, 0x101, 400)

    def lambda_1F43():
        TurnDirection(0x105, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1F43)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F67")

    def lambda_1F5F():
        TurnDirection(0x13B, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_1F5F)

    label("loc_1F67")

    TurnDirection(0x101, 0x15, 400)

    ChrTalk(
        0x15,
        (
            "那，如果再看到的话，\x01",
            "也麻烦告诉我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，放心吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F知道了。\x02",
    )

    CloseMessageWindow()

    label("loc_1FC1")


    def lambda_1FC7():

        label("loc_1FC7")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_1FC7")

    QueueWorkItem2(0x0, 1, lambda_1FC7)

    def lambda_1FD8():

        label("loc_1FD8")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_1FD8")

    QueueWorkItem2(0x1, 1, lambda_1FD8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2002")

    def lambda_1FF7():

        label("loc_1FF7")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_1FF7")

    QueueWorkItem2(0x2, 1, lambda_1FF7)

    label("loc_2002")

    SetChrFlags(0x15, 0x40)
    OP_8E(0x15, 0xB0C2, 0x0, 0x6DCE, 0xBB8, 0x0)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2035")
    OP_44(0x2, 0xFF)

    label("loc_2035")

    SetChrPos(0x15, 47880, 0, 56070, 135)
    ClearChrFlags(0x15, 0x40)
    OP_4B(0x15, 255)
    OP_64(0x5, 0x1)
    EventEnd(0x0)

    label("loc_2055")

    TalkEnd(0xFF)
    Return()

    # Function_3_15B9 end

    SaveToFile()

Try(main)
