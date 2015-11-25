from ED6ScenarioHelper import *

def main():
    # 洛连特

    CreateScenaFile(
        FileName            = 'T1132_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T1132.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
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
        "Function_1_106",          # 01, 1
        "Function_2_3B8",          # 02, 2
        "Function_3_591",          # 03, 3
    )


    def Function_0_66(): pass

    label("Function_0_66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_78")
    Call(1, 2)
    Jump("loc_105")

    label("loc_78")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_89")
    Call(1, 1)
    Jump("loc_105")

    label("loc_89")

    SetChrFlags(0xA, 0x10)
    TalkBegin(0xA)

    ChrTalk(
        0xFE,
        (
            "呼，受不了了。\x01",
            "这种时候定期船居然停航了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "算了算了，麻烦这种东西\x01",
            "就是只会在最紧急的时候跳出来。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    ClearChrFlags(0xA, 0x10)

    label("loc_105")

    Return()

    # Function_0_66 end

    def Function_1_106(): pass

    label("Function_1_106")

    EventBegin(0x0)
    Fade(1000)

    def lambda_113():
        OP_6D(-86090, 0, 119620, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_113)
    SetChrPos(0x101, -85900, 0, 119750, 270)
    SetChrPos(0x102, -84500, 0, 119350, 270)
    SetChrPos(0x103, -84900, 0, 120550, 270)
    SetChrFlags(0xA, 0x10)
    OP_4A(0xA, 255)
    OP_0D()
    WaitChrThread(0x0, 0x1)
    Sleep(400)
    OP_28(0x10, 0x4, 0x4)
    OP_28(0x10, 0x1, 0x1)

    ChrTalk(
        0x101,
        (
            "#000F打扰一下可以吗？\x02\x03",
            "您就是哈尔德先生吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0xA,
        "嗯……？\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 90, 400)

    ChrTalk(
        0xA,
        (
            "难道，\x01",
            "你们是看了公告板而来的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "呼～终于来了啊。\x01",
            "我都快等不及了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "我有非常要紧的事情要赶去卢安办理。\x01",
            "希望你们能护送我到古罗尼的山顶关所。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "如何，你们愿意吗？\x02",
    )

    CloseMessageWindow()

    label("loc_29C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A7")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【接受】\x01",      # 0
            "【拒绝】\x01",      # 1
        )
    )

    MenuEnd(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_300"),
        (1, "loc_314"),
        (SWITCH_DEFAULT, "loc_3A4"),
    )


    label("loc_300")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Call(1, 3)
    Jump("loc_3A4")

    label("loc_314")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_28(0x10, 0x1, 0x8000)

    ChrTalk(
        0x101,
        (
            "#000F对不起，\x01",
            "我们还有些事情要办。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "啊～～怎么、怎么会这样～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "唉，这么一来，\x01",
            "这次的生意就谈不成了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 270, 0)
    Jump("loc_3A4")

    label("loc_3A4")

    Jump("loc_29C")

    label("loc_3A7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4B(0xA, 255)
    EventEnd(0x0)
    Return()

    # Function_1_106 end

    def Function_2_3B8(): pass

    label("Function_2_3B8")

    EventBegin(0x0)
    Fade(1000)

    def lambda_3C5():
        OP_6D(-86090, 0, 119620, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3C5)
    SetChrPos(0x101, -85900, 0, 119750, 270)
    SetChrPos(0x102, -84500, 0, 119350, 270)
    SetChrPos(0x103, -84900, 0, 120550, 270)
    SetChrFlags(0xA, 0x10)
    OP_0D()
    WaitChrThread(0x0, 0x1)
    OP_4A(0xA, 255)
    OP_8C(0xA, 90, 400)
    Sleep(400)

    ChrTalk(
        0xA,
        "哦，是游击士们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "怎么样？\x01",
            "能护送我到古罗尼的山顶关所吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_57B")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【接受】\x01",      # 0
            "【拒绝】\x01",      # 1
        )
    )

    MenuEnd(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_4CE"),
        (1, "loc_4E2"),
        (SWITCH_DEFAULT, "loc_578"),
    )


    label("loc_4CE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Call(1, 3)
    Jump("loc_578")

    label("loc_4E2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_28(0x10, 0x1, 0x8000)

    ChrTalk(
        0x101,
        (
            "#505F唔～对不起……\x01",
            "我们还有些事情要办。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "啊～～怎么、怎么会这样～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "唉，这么一来，\x01",
            "这次的生意就谈不成了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 270, 0)
    Jump("loc_578")

    label("loc_578")

    Jump("loc_46A")

    label("loc_57B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4B(0xA, 255)
    ClearChrFlags(0xA, 0x10)
    EventEnd(0x0)
    Return()

    # Function_2_3B8 end

    def Function_3_591(): pass

    label("Function_3_591")

    OP_28(0x10, 0x1, 0x2)

    ChrTalk(
        0x101,
        "#006F嗯，没问题。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "太好了～\x01",
            "啊～～你们真是我的救星啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "山道上的魔兽非常多，\x01",
            "只有我一个人的话实在是有点害怕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F可是过了关所后又要怎么办呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "啊，\x01",
            "我也委托了那边的游击士协会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "卢安支部会派游击士\x01",
            "接我过去的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F原来是这样啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xA, 400)

    ChrTalk(
        0x102,
        (
            "#010F那么，接下来怎么做？\x02\x03",
            "现在就出发吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 400)

    ChrTalk(
        0x103,
        (
            "#020F不要急，我们先各自行动，\x01",
            "待会儿再汇合。\x02\x03",
            "因为我们也要先\x01",
            "做好各种准备才能出发。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 45, 400)

    ChrTalk(
        0xA,
        "嗯，没关系的。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 90, 400)

    ChrTalk(
        0xA,
        (
            "那我就在城的西门等着，\x01",
            "你们好好准备吧，待会儿就拜托了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    def lambda_79E():

        label("loc_79E")

        TurnDirection(0x101, 0xA, 0)
        OP_48()
        Jump("loc_79E")

    QueueWorkItem2(0x101, 1, lambda_79E)

    def lambda_7AF():

        label("loc_7AF")

        TurnDirection(0x102, 0xA, 0)
        OP_48()
        Jump("loc_7AF")

    QueueWorkItem2(0x102, 1, lambda_7AF)

    def lambda_7C0():

        label("loc_7C0")

        TurnDirection(0x103, 0xA, 0)
        OP_48()
        Jump("loc_7C0")

    QueueWorkItem2(0x103, 1, lambda_7C0)

    def lambda_7D1():
        OP_90(0x101, 0x0, 0x0, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7D1)

    def lambda_7EC():
        OP_90(0x102, 0x0, 0x0, 0xFFFFFC18, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7EC)
    SetChrFlags(0xA, 0x40)
    OP_8E(0xA, 0xFFFEBBC8, 0x0, 0x1D0D8, 0x7D0, 0x0)
    OP_8E(0xA, 0xFFFEC26C, 0x0, 0x1D2CC, 0x7D0, 0x0)

    def lambda_834():
        OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_834)
    OP_8E(0xA, 0xFFFECA3C, 0x0, 0x1D2CC, 0x7D0, 0x0)
    SetChrFlags(0xA, 0x80)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0x103, 0x1)
    Sleep(800)

    def lambda_870():
        OP_90(0x101, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_870)

    def lambda_88B():
        OP_90(0x102, 0x0, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_88B)
    WaitChrThread(0x102, 0x2)

    def lambda_8AB():
        OP_8C(0x101, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8AB)
    TurnDirection(0x102, 0x101, 400)
    Sleep(800)

    ChrTalk(
        0x102,
        (
            "#010F城的西门就在梅贝尔市长官邸的旁边吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(
        0x103,
        (
            "#020F嗯，没错。\x01",
            "那么我们就开始工作吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F好～的。\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_3_591 end

    SaveToFile()

Try(main)
