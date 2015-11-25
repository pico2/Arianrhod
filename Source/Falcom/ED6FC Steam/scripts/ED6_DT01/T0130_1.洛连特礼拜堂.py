from ED6ScenarioHelper import *

def main():
    # 洛连特礼拜堂

    CreateScenaFile(
        FileName            = 'T0130_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T0130.x',
        MapIndex            = 3,
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

    ScpFunction(
        "Function_0_66",           # 00, 0
        "Function_1_2B5",          # 01, 1
        "Function_2_776",          # 02, 2
        "Function_3_AD3",          # 03, 3
        "Function_4_E1C",          # 04, 4
        "Function_5_11DB",         # 05, 5
        "Function_6_15AF",         # 06, 6
        "Function_7_193C",         # 07, 7
        "Function_8_1E8A",         # 08, 8
        "Function_9_1EB0",         # 09, 9
    )


    def Function_0_66(): pass

    label("Function_0_66")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A3")
    OP_28(0x7, 0x1, 0x8000)

    ChrTalk(
        0x8,
        (
            "哦，看你们的样子……\x01",
            "是要出去旅行吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x101,
        (
            "#000F嗯，是啊。\x01",
            "我们要去柏斯。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        "原来是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "如果可以的话，\x01",
            "能不能帮我一个忙呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我这有一封给柏斯的豪尔斯教区长的信，\x01",
            "因为定期船停航的缘故没法寄出，\x01",
            "正在为这事发愁。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "如果方便的话，\x01",
            "请在旅途中顺便帮我送去好吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AD")

    label("loc_1A3")


    ChrTalk(
        0x8,
        (
            "……对了。\x01",
            "你们说要去柏斯吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x101,
        "#000F是啊，怎么了？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "这样的话我还有一件事要拜托你们，\x01",
            "能不能帮个忙呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我有一封给柏斯的豪尔斯教区长的信，\x01",
            "因为定期船停航的缘故没法寄出，\x01",
            "正在为这事发愁。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "如果方便的话，\x01",
            "请在旅途中顺便帮我送去好吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AD")

    Call(1, 3)
    TalkEnd(0x8)
    Return()

    # Function_0_66 end

    def Function_1_2B5(): pass

    label("Function_1_2B5")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    Fade(1000)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xE678), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_30C")
    SetChrPos(0x101, 60600, 1000, 52500, 270)
    SetChrPos(0x102, 60600, 1000, 51300, 315)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_309")
    SetChrPos(0x103, 61600, 1000, 50200, 315)

    label("loc_309")

    Jump("loc_346")

    label("loc_30C")

    SetChrPos(0x101, 57400, 1000, 52500, 90)
    SetChrPos(0x102, 57400, 1000, 51300, 45)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_346")
    SetChrPos(0x103, 56400, 1000, 50200, 45)

    label("loc_346")

    OP_69(0x101, 0x7D0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40E")
    OP_28(0x7, 0x1, 0x8000)
    OP_4A(0x8, 255)
    TurnDirection(0x8, 0x0, 400)

    ChrTalk(
        0x8,
        (
            "哦，看你们的样子……\x01",
            "是要出去旅行吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x101,
        (
            "#000F嗯，是啊。\x02\x03",
            "虽然我们马上要去柏斯了，\x01",
            "不过在出发前有些东西\x01",
            "必须要交给教区长。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        "给我……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A0")

    label("loc_40E")

    OP_4A(0x8, 255)
    TurnDirection(0x8, 0x0, 400)

    ChrTalk(
        0x8,
        (
            "哦，看你们的样子……\x01",
            "你们还没出发吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x101,
        (
            "#000F嗯，是啊。\x02\x03",
            "其实在出发前有些东西\x01",
            "必须要交给教区长。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        "给我……？\x02",
    )

    CloseMessageWindow()

    label("loc_4A0")

    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "熊刺草\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "魔兽羽翼\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_62(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)

    ChrTalk(
        0x8,
        "这不就是……！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0x102,
        (
            "#010F『熊刺草』和『魔兽羽翼』。\x01",
            "您需要的药材。\x02\x03",
            "是您委托游击士协会去采集的吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        "哦，确实是我委托的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不过，\x01",
            "没想到是由你们去采集的啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "艾丝蒂尔、约修亚。\x01",
            "真的十分感谢你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "你们两个，\x01",
            "都能尽心尽力去完成工作呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "这样我就放心了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯⊙\x01",
            "以后我们也会全心全意努力的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        "这样我就放心了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "以后的旅途中，\x01",
            "也一定要小心谨慎啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "愿你们能\x01",
            "常受女神的保佑。\x02",
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
            "任务【采集药材】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x386, 1)
    OP_3F(0x39F, 1)
    OP_28(0x7, 0x4, 0x10)
    OP_28(0x7, 0x1, 0x1)
    OP_A2(0x1)
    OP_8C(0x8, 180, 0)
    EventEnd(0x0)
    OP_4B(0x8, 255)
    Return()

    # Function_1_2B5 end

    def Function_2_776(): pass

    label("Function_2_776")

    TalkBegin(0x8)

    ChrTalk(
        0x8,
        "哦，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "难道是有空帮我送信了吗？\x02",
    )

    CloseMessageWindow()

    label("loc_7A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AC5")
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

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_80D"),
        (1, "loc_9E1"),
        (SWITCH_DEFAULT, "loc_AC2"),
    )


    label("loc_80D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_28(0xD, 0x4, 0x8)
    OP_28(0xD, 0x1, 0x1)
    OP_3E(0x329, 1)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x101,
        "#000F嗯，好的。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_879")

    ChrTalk(
        0x103,
        (
            "#020F反正也是举手之劳，\x01",
            "您就别客气了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_879")

    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        "谢谢你们的帮忙。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "嗯，\x01",
            "那么就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "教区长的亲笔信\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0x102,
        (
            "#010F交给柏斯的豪尔斯教区长\x01",
            "就可以了吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        (
            "是的。\x01",
            "教会在柏斯市的东侧，\x01",
            "进城后很容易就可以找到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "周游各地的时候\x01",
            "增长的见识和经历，\x01",
            "可以变为自身的财富。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "愿你们能\x01",
            "常受女神的保佑。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC2")

    label("loc_9E1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_28(0xD, 0x1, 0x8000)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x101,
        (
            "#003F嗯～对不起，\x01",
            "现在有些困难……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "是这样啊。\x01",
            "那就只能先不送了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "……但是，你们越是着急，\x01",
            "就越容易发生危险。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "所以在旅途中\x01",
            "一定要小心谨慎啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那么，\x01",
            "愿你们常受女神的保佑。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC2")

    label("loc_AC2")

    Jump("loc_7A9")

    label("loc_AC5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0x8)
    Return()

    # Function_2_776 end

    def Function_3_AD3(): pass

    label("Function_3_AD3")

    OP_28(0xD, 0x4, 0x4)
    OP_28(0xD, 0x4, 0x2)

    label("loc_ADD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E0E")
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

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B41"),
        (1, "loc_D00"),
        (SWITCH_DEFAULT, "loc_E0B"),
    )


    label("loc_B41")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_28(0xD, 0x4, 0x8)
    OP_28(0xD, 0x1, 0x1)
    OP_3E(0x329, 1)

    ChrTalk(
        0x101,
        "#000F嗯，好的。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_BA6")

    ChrTalk(
        0x103,
        (
            "#020F反正也是举手之劳，\x01",
            "您就别客气了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA6")


    ChrTalk(
        0x8,
        "谢谢你们的帮忙。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "嗯，\x01",
            "那么就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "教区长的亲笔信\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#010F交给柏斯的豪尔斯教区长\x01",
            "就可以了吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 0)

    ChrTalk(
        0x8,
        (
            "是的。\x01",
            "教会在柏斯市的东侧，\x01",
            "进城后很容易就可以找到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "周游各地的时候\x01",
            "增长的见识和经历，\x01",
            "可以变为自身的财富。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "愿你们能\x01",
            "常受女神的保佑。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E0B")

    label("loc_D00")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_28(0xD, 0x1, 0x8000)

    ChrTalk(
        0x101,
        (
            "#003F对不起，教区长。\x01",
            "我们还有很急的事情要去办……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "是这样啊。\x01",
            "那就只能先不送了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "……但是，你们越是着急，\x01",
            "就越容易发生危险。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "所以在旅途中\x01",
            "一定要小心谨慎啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F……嗯，我们会注意的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那么，\x01",
            "愿你们常受女神的保佑。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E0B")

    label("loc_E0B")

    Jump("loc_ADD")

    label("loc_E0E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0x8)
    Return()

    # Function_3_AD3 end

    def Function_4_E1C(): pass

    label("Function_4_E1C")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    Fade(1000)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xE678), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_ECF")
    SetChrPos(0x101, 60600, 1000, 52500, 270)
    SetChrPos(0x102, 60600, 1000, 51300, 315)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E8B")
    SetChrPos(0x2, 61600, 1000, 51500, 270)
    SetChrPos(0x3, 61600, 1000, 50200, 315)
    Jump("loc_ECC")

    label("loc_E8B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EAD")
    SetChrPos(0x2, 61600, 1000, 51500, 270)
    Jump("loc_ECC")

    label("loc_EAD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ECC")
    SetChrPos(0x103, 61600, 1000, 51500, 270)

    label("loc_ECC")

    Jump("loc_F65")

    label("loc_ECF")

    SetChrPos(0x101, 57400, 1000, 52500, 90)
    SetChrPos(0x102, 57400, 1000, 51300, 45)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F24")
    SetChrPos(0x2, 56400, 1000, 51500, 90)
    SetChrPos(0x3, 56400, 1000, 50200, 45)
    Jump("loc_F65")

    label("loc_F24")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F46")
    SetChrPos(0x2, 56400, 1000, 51500, 90)
    Jump("loc_F65")

    label("loc_F46")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F65")
    SetChrPos(0x103, 56400, 1000, 51500, 90)

    label("loc_F65")

    OP_69(0x101, 0x7D0)
    OP_0D()
    TurnDirection(0x8, 0x101, 400)
    OP_4A(0x8, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FCB")

    ChrTalk(
        0x8,
        (
            "哦？是艾丝蒂尔啊。\x01",
            "有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F请收下这些，教区长。\x02",
    )

    CloseMessageWindow()
    Jump("loc_104B")

    label("loc_FCB")


    ChrTalk(
        0x8,
        "哦？是艾丝蒂尔啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "今天依旧是\x01",
            "那么的活泼开朗啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#001F嘿嘿嘿。\x02\x03",
            "请收下这些，教区长。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_104B")

    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "熊刺草\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "魔兽羽翼\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_62(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)

    ChrTalk(
        0x8,
        "这不就是……！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0x102,
        (
            "#010F『熊刺草』和『魔兽羽翼』。\x01",
            "您需要的药材。\x02\x03",
            "是您委托游击士协会去采集的吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        "哦，确实是我委托的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不过，\x01",
            "没想到是由你们去采集的啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "艾丝蒂尔、约修亚，\x01",
            "你们没有受伤吧？\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 5)
    Return()

    # Function_4_E1C end

    def Function_5_11DB(): pass

    label("Function_5_11DB")


    ChrTalk(
        0x101,
        (
            "#001F没事，完好无损⊙\x02\x03",
            "#000F……不信您看看。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        "……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "……你们的状况\x01",
            "让我有些担心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F啊～～！？\x01",
            "不用担心、不用担心啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "我以前应该也对你们说过的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "一件事情若能顺利的进行，\x01",
            "固然很令人高兴……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "但是在这种时候，\x01",
            "尤其要提高警觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F好～～的。\x01",
            "我以后会注意的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "唔……\x01",
            "时间还很充裕啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "机会难得，我就给你们来一堂特别讲义如何……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#004F（不会吧……）\x02\x03",
            "#506F对、对不起啊教区长。\x01",
            "我们现在必须得走了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1405")

    ChrTalk(
        0x102,
        (
            "#010F抱歉，教区长。\x01",
            "其实我们还有紧急任务。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1497")

    label("loc_1405")

    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#506F对吧，约修亚。\x01",
            "我们还有其他工作呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F（……真拿她没办法。）\x02\x03",
            "#010F抱歉，教区长。\x01",
            "我们得回游击士协会了……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_148F():
        TurnDirection(0x101, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_148F)

    label("loc_1497")

    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        (
            "是这样啊，真是太遗憾了。\x01",
            "不过工作是一定要完成的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "艾丝蒂尔、约修亚，\x01",
            "辛苦了，真是非常感谢你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "在你们二人走过的蓝天之下，\x01",
            "空之女神会常伴左右。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【采集药材】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x386, 1)
    OP_3F(0x39F, 1)
    OP_28(0x7, 0x4, 0x10)
    OP_28(0x7, 0x1, 0x1)
    OP_A2(0x1)
    OP_8C(0x8, 180, 0)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_5_11DB end

    def Function_6_15AF(): pass

    label("Function_6_15AF")

    EventBegin(0x0)
    SetMapFlags(0x400000)
    ClearMapFlags(0x1)
    SetChrPos(0xE, 59100, 0, 45800, 0)
    SetChrFlags(0xD, 0x40)
    SetChrPos(0x101, 59800, 0, 41000, 0)
    SetChrPos(0x102, 58700, 0, 40000, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1626")
    SetChrPos(0x2, 59600, 0, 39000, 0)
    SetChrPos(0x3, 58600, 0, 38500, 0)
    Jump("loc_1645")

    label("loc_1626")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1645")
    SetChrPos(0x2, 59600, 0, 39000, 0)

    label("loc_1645")

    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x102, 0x40)
    OP_6D(59100, 0, 45800, 3000)
    TurnDirection(0xE, 0x101, 0)
    OP_62(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0xE, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#507F嘿嘿嘿嘿……\x01",
            "这下逃不掉了吧。\x02\x03",
            "老老实实束手就擒吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    OP_8C(0xE, 135, 400)
    Sleep(500)
    OP_8C(0xE, 225, 400)
    Sleep(500)
    SetChrPos(0xD, 59100, 0, 45800, 180)
    ClearChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x8)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x8)
    SetChrFlags(0xD, 0x40)
    OP_8F(0xD, 0xE6DC, 0x0, 0xB6D0, 0xBB8, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17D0")

    def lambda_1756():

        label("loc_1756")

        TurnDirection(0x101, 0xD, 0)
        OP_48()
        Jump("loc_1756")

    QueueWorkItem2(0x101, 1, lambda_1756)

    def lambda_1767():

        label("loc_1767")

        TurnDirection(0x102, 0xD, 0)
        OP_48()
        Jump("loc_1767")

    QueueWorkItem2(0x102, 1, lambda_1767)

    def lambda_1778():

        label("loc_1778")

        TurnDirection(0x8, 0xD, 0)
        OP_48()
        Jump("loc_1778")

    QueueWorkItem2(0x8, 1, lambda_1778)

    def lambda_1789():

        label("loc_1789")

        TurnDirection(0x10F, 0xD, 0)
        OP_48()
        Jump("loc_1789")

    QueueWorkItem2(0x10F, 1, lambda_1789)

    def lambda_179A():

        label("loc_179A")

        TurnDirection(0x110, 0xD, 0)
        OP_48()
        Jump("loc_179A")

    QueueWorkItem2(0x110, 1, lambda_179A)
    OP_8E(0xD, 0xC224, 0x0, 0xC8C8, 0x1B58, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x10F, 0xFF)
    OP_44(0x110, 0xFF)
    Jump("loc_1895")

    label("loc_17D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_END)), "loc_1842")

    def lambda_17DD():

        label("loc_17DD")

        TurnDirection(0x101, 0xD, 0)
        OP_48()
        Jump("loc_17DD")

    QueueWorkItem2(0x101, 1, lambda_17DD)

    def lambda_17EE():

        label("loc_17EE")

        TurnDirection(0x102, 0xD, 0)
        OP_48()
        Jump("loc_17EE")

    QueueWorkItem2(0x102, 1, lambda_17EE)

    def lambda_17FF():

        label("loc_17FF")

        TurnDirection(0x8, 0xD, 0)
        OP_48()
        Jump("loc_17FF")

    QueueWorkItem2(0x8, 1, lambda_17FF)

    def lambda_1810():

        label("loc_1810")

        TurnDirection(0x10F, 0xD, 0)
        OP_48()
        Jump("loc_1810")

    QueueWorkItem2(0x10F, 1, lambda_1810)
    OP_8E(0xD, 0xC224, 0x0, 0xC8C8, 0x1B58, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x10F, 0xFF)
    Jump("loc_1895")

    label("loc_1842")


    def lambda_1848():

        label("loc_1848")

        TurnDirection(0x101, 0xD, 0)
        OP_48()
        Jump("loc_1848")

    QueueWorkItem2(0x101, 1, lambda_1848)

    def lambda_1859():

        label("loc_1859")

        TurnDirection(0x102, 0xD, 0)
        OP_48()
        Jump("loc_1859")

    QueueWorkItem2(0x102, 1, lambda_1859)

    def lambda_186A():

        label("loc_186A")

        TurnDirection(0x8, 0xD, 0)
        OP_48()
        Jump("loc_186A")

    QueueWorkItem2(0x8, 1, lambda_186A)
    OP_8E(0xD, 0xC224, 0x0, 0xC8C8, 0x1B58, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x8, 0xFF)

    label("loc_1895")

    SetChrPos(0xD, 0, 0, 0, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18EC")

    def lambda_18B7():
        OP_92(0x10F, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_18B7)

    def lambda_18CC():
        OP_92(0x110, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x110, 1, lambda_18CC)
    OP_92(0x1, 0x0, 0x0, 0xBB8, 0x0)
    Jump("loc_1927")

    label("loc_18EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_END)), "loc_1919")

    def lambda_18F9():
        OP_92(0x10F, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_18F9)
    OP_92(0x1, 0x0, 0x0, 0xBB8, 0x0)
    Jump("loc_1927")

    label("loc_1919")

    OP_92(0x1, 0x0, 0x0, 0xBB8, 0x0)

    label("loc_1927")

    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x102, 0x40)
    OP_85(0x8)
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    Return()

    # Function_6_15AF end

    def Function_7_193C(): pass

    label("Function_7_193C")

    EventBegin(0x0)
    SetMapFlags(0x400000)
    ClearMapFlags(0x1)
    FadeToBright(1000, 0)
    OP_6D(46700, 5000, 49700, 0)
    SetChrPos(0xE, 52100, 5000, 48000, 90)
    SetChrFlags(0xE, 0x40)
    ClearChrFlags(0xE, 0x8)
    SetChrPos(0x101, 51700, 5000, 50300, 180)
    SetChrPos(0x102, 52100, 5000, 50800, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19D2")
    SetChrPos(0x2, 51500, 5000, 51300, 180)
    SetChrPos(0x3, 52100, 5000, 51700, 180)
    Jump("loc_19F1")

    label("loc_19D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19F1")
    SetChrPos(0x2, 51500, 5000, 51300, 180)

    label("loc_19F1")

    OP_6D(51500, 5000, 49200, 3000)
    TurnDirection(0xE, 0x101, 0)
    OP_62(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0xE, 0x0, 0x0, 0x0, 0x320, 0x2EE0)

    ChrTalk(
        0x101,
        (
            "#002F好孩子～\x01",
            "要乖乖地听话哦。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_8E(0x101, 0xC9F4, 0x1388, 0xC418, 0x7D0, 0x0)
    OP_8F(0xE, 0xCB84, 0x1388, 0xBA54, 0xBB8, 0x0)
    Sleep(1000)

    def lambda_1A93():
        OP_8E(0x101, 0xC9F4, 0x1388, 0xC2EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A93)
    OP_62(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(200)

    def lambda_1AC5():
        OP_8F(0xE, 0xCB84, 0x1388, 0xB928, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1AC5)
    Sleep(800)

    ChrTalk(
        0x101,
        "#002F不要动哦～\x02",
    )

    CloseMessageWindow()

    def lambda_1AFA():
        OP_8E(0x101, 0xC9F4, 0x1388, 0xC15C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1AFA)
    OP_63(0xE)
    OP_62(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(200)

    def lambda_1B2F():
        OP_8F(0xE, 0xCB84, 0x1388, 0xB5A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1B2F)
    OP_63(0xE)
    OP_62(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xE, 45, 0)
    Sleep(50)
    OP_8C(0xE, 90, 0)
    Sleep(50)
    OP_8C(0xE, 135, 0)
    Sleep(50)
    OP_8C(0xE, 180, 0)
    Sleep(50)
    OP_8C(0xE, 225, 0)
    Sleep(50)
    OP_8C(0xE, 270, 0)
    Sleep(50)
    OP_8C(0xE, 315, 0)
    Sleep(50)
    OP_8C(0xE, 0, 0)
    OP_8C(0xE, 315, 0)
    Sleep(50)
    OP_8C(0xE, 270, 0)
    Sleep(50)
    OP_8C(0xE, 225, 0)
    Sleep(50)
    OP_8C(0xE, 180, 0)
    Sleep(50)
    OP_8C(0xE, 135, 0)
    Sleep(50)
    OP_8C(0xE, 90, 0)
    Sleep(50)
    OP_8C(0xE, 45, 0)
    Sleep(50)
    OP_8C(0xE, 0, 0)
    OP_8C(0xE, 45, 0)
    Sleep(50)
    OP_8C(0xE, 90, 0)
    Sleep(50)
    OP_8C(0xE, 135, 0)
    Sleep(50)
    OP_8C(0xE, 180, 0)
    Sleep(200)
    OP_43(0xE, 0x1, 0x1, 0x8)
    OP_A2(0x6)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#014F艾丝蒂尔，\x01",
            "不要把它逼急了啊。\x02\x03",
            "如果它从这里跳下去，\x01",
            "那可怎么办？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#009F我、我知道啦，\x01",
            "可是它怎么也不听话啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1CD6():

        label("loc_1CD6")

        TurnDirection(0x101, 0x102, 0)
        OP_48()
        Jump("loc_1CD6")

    QueueWorkItem2(0x101, 1, lambda_1CD6)
    OP_8E(0x102, 0xCB84, 0x1388, 0xBD10, 0x3E8, 0x0)
    OP_44(0x101, 0xFF)
    Sleep(400)
    Fade(500)
    SetChrChipByIndex(0x102, 13)
    OP_0D()

    ChrTalk(
        0x102,
        "#011F小安莉尔，乖，到我这里来。\x02",
    )

    CloseMessageWindow()
    OP_A3(0x6)
    Sleep(800)
    TurnDirection(0xE, 0x102, 600)
    Sleep(200)
    OP_62(0xE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(600)

    ChrTalk(
        0x102,
        "#011F真是对不起，吓着你了。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        "#009F（哼。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F乖，别跑。\x01",
            "和我们回阿姨那里去。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_62(0xE, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1500)

    def lambda_1DFA():
        OP_8E(0xE, 0xCB20, 0x1388, 0xB98C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1DFA)
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0xE,
        "喵喵～～\x02",
    )

    CloseMessageWindow()
    Sleep(600)

    ChrTalk(
        0x102,
        (
            "#019F对，就是这样。安莉尔真是乖孩子。\x02\x03",
            "我们回家吧，\x01",
            "阿姨在等着你呢。\x02",
        )
    )

    CloseMessageWindow()
    ClearMapFlags(0x400000)
    FadeToDark(500, 0, -1)
    NewScene("ED6_DT01/T0100   ._SN", 1, 0, 0)
    IdleLoop()
    Return()

    # Function_7_193C end

    def Function_8_1E8A(): pass

    label("Function_8_1E8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1EAF")
    OP_63(0xE)
    OP_62(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(600)
    OP_48()
    Jump("Function_8_1E8A")

    label("loc_1EAF")

    Return()

    # Function_8_1E8A end

    def Function_9_1EB0(): pass

    label("Function_9_1EB0")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F03")

    ChrTalk(
        0x101,
        (
            "#006F先把那只小猫抓住再说吧。\x02\x03",
            "好不容易把它追进这里来了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F63")

    label("loc_1F03")

    TurnDirection(0x102, 0x1, 400)

    ChrTalk(
        0x102,
        (
            "#010F既然来到这里了，\x01",
            "还是先把小猫抓住比较好。\x02\x03",
            "如果这样放着不管，\x01",
            "会惹出麻烦来的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F63")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_9_1EB0 end

    SaveToFile()

Try(main)
