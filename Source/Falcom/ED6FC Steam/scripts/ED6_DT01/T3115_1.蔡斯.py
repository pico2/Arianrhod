from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3115_1 ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3115.x',
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
        "Function_3_3BB",          # 03, 3
        "Function_4_CE1",          # 04, 4
        "Function_5_144D",         # 05, 5
        "Function_6_1FD0",         # 06, 6
        "Function_7_2727",         # 07, 7
        "Function_8_30AE",         # 08, 8
        "Function_9_3476",         # 09, 9
        "Function_10_3A47",        # 0A, 10
        "Function_11_3F3A",        # 0B, 11
        "Function_12_45A5",        # 0C, 12
        "Function_13_460E",        # 0D, 13
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
    Fade(1000)
    OP_6D(2300, 0, 2540, 0)
    SetChrPos(0x101, 1850, 0, 1780, 0)
    SetChrPos(0x102, 3300, 0, 2100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_105")
    SetChrPos(0x107, 2650, 0, 1120, 0)

    label("loc_105")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_124")
    SetChrPos(0x13C, 2530, 0, 3050, 359)

    label("loc_124")

    OP_0D()

    ChrTalk(
        0x8,
        "#800F咦，怎么回事？\x02",
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0x13C,
        "喵呀～～噢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#802F哦，安东尼。\x02\x03",
            "你那样叫，\x01",
            "是想说些什么吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0x13C,
        (
            "喵～噢，\x01",
            "喵呀～～噢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(120)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x107, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        "#509F唔，这么说……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F怎么看都很有嫌疑啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#561F是啊～……\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x8,
        (
            "#802F？？？\x02\x03",
            "你们在说什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F工房长先生，\x01",
            "今天你去过医务室吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#802F啊…………！？\x02\x03",
            "#805F没、没有……\x01",
            "没有去过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F我们正在寻找\x01",
            "被人从医务室里带走的香烟。\x02\x03",
            "让我们对这个房间\x01",
            "进行一下调查好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#806F唔、哦，\x01",
            "倒是没什么不行的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#507F那就不用顾虑了，\x01",
            "让我们好好调查一番吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x2C, 0x1, 0x200)
    EventEnd(0x0)
    Return()

    # Function_2_AC end

    def Function_3_3BB(): pass

    label("Function_3_3BB")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-102680, 0, 106860, 0)
    SetChrPos(0x101, -103170, 0, 107210, 90)
    SetChrPos(0x102, -102910, 0, 106140, 40)
    SetChrPos(0x107, -104120, 0, 106520, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_425")
    SetChrPos(0x13C, -104780, 0, 107680, 90)

    label("loc_425")

    OP_0D()
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#000F不好意思，可以打扰一下吗？\x02\x03",
            "您是普罗梅笛先生……吧？\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x13, 0x10)
    TalkBegin(0x13)
    ClearChrFlags(0x13, 0x10)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    OP_4A(0xFE, 255)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "我就是普罗梅笛……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "有什么事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯，有点小事情。\x02\x03",
            "是这样的，\x01",
            "我们在找运输车用的导力引擎。\x02\x03",
            "想问一下普罗梅笛先生，\x01",
            "如果您知道放在哪里的话，\x01",
            "可以告诉我们吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "运输车用的\x01",
            "导力引擎吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "实在很抱歉，\x01",
            "我完全不知道放在哪。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        "#004F咦？怎么会呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F我们听说普罗梅笛先生您\x01",
            "是负责管理运输车的啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "啊～～\x01",
            "那是很久以前的事情了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那个职务是轮流担当的，\x01",
            "会定期更换人员。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "而且………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果问我现在的负责人是谁，\x01",
            "老实说我也不知道。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F呼………………\x01",
            "想问的他都抢先回答了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，这样就行了吧？\x01",
            "我还有很多事情要做。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F非常抱歉，\x01",
            "在您百忙之中前来打扰。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嗯，那我先去忙别的了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x13, 360, 400)
    OP_4B(0xFE, 255)

    def lambda_759():
        OP_6D(-103770, 0, 106670, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_759)
    OP_8C(0x101, 223, 400)
    OP_8C(0x102, 286, 400)
    WaitChrThread(0xFE, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x29, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_915")

    ChrTalk(
        0x101,
        (
            "#003F唔……\x01",
            "怎么和之前说的不一样啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#561F不、不好意思。\x02\x03",
            "因为设备的管理\x01",
            "是件相当麻烦的工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F普罗梅笛先生不知道的话……\x01",
            "　\x02\x03",
            "就只剩在『卡佩尔』上\x01",
            "看到过的那个线索了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F嗯，\x01",
            "应该在地下工场的入口……\x01",
            "资料上面是这么记载的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F啊，\x01",
            "那是卡鲁迪亚隧道的出口。\x01",
            "　\x02\x03",
            "那片区域放置了各种各样的零部件。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F好，\x01",
            "那么我们就到地下去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，好的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_CCA")

    label("loc_915")


    ChrTalk(
        0x101,
        (
            "#003F唔……这下麻烦了。\x02\x03",
            "怎么和之前说的不一样啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#561F不、不好意思。\x02\x03",
            "因为设备的管理\x01",
            "是件相当麻烦的工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F算了，这也是没办法事。\x02\x03",
            "我们还是想想其他办法\x01",
            "去调查一下运输车的事情吧。\x02\x03",
            "我想应该会有其他线索的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x29, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_BFA")
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#505F别的办法……吗……\x02\x03",
            "…………………………\x02\x03",
            "#004F……啊，我想起来了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A74():
        TurnDirection(0x107, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_A74)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#014F什么？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#002F你想想，\x01",
            "不久之前我们不是利用了一个\x01",
            "什么导力器收集了不少信息吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F是演算导力器『卡佩尔』对吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(
        0x101,
        (
            "#000F对对，就是它。\x02\x03",
            "#505F我记得那个时候\x01",
            "好像看到了有关运输车的事项……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x107, 400)

    ChrTalk(
        0x102,
        (
            "#014F对啊…………\x02\x03",
            "『卡佩尔』里面的确应该有\x01",
            "运输车的相关记录。\x02\x03",
            "#010F我们立刻就去调查吧，\x01",
            "演算室在五楼哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#508F好！\x02",
    )

    CloseMessageWindow()
    OP_28(0x29, 0x1, 0x4)
    Jump("loc_CCA")

    label("loc_BFA")


    ChrTalk(
        0x101,
        (
            "#505F找其他的方法……\x02\x03",
            "话是这么说，\x01",
            "可应该不会那么简单的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F不过，\x01",
            "在这里干着急也不是办法。\x02\x03",
            "也许会有线索的。\x01",
            "总之先在工房里转转看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#060F嗯，好～的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F是啊……\x02\x03",
            "那我们走吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CCA")

    Sleep(400)
    OP_28(0x29, 0x1, 0x1)
    OP_28(0x29, 0x1, 0x2)
    OP_A2(0xC)
    EventEnd(0x0)
    Return()

    # Function_3_3BB end

    def Function_4_CE1(): pass

    label("Function_4_CE1")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-101090, 0, 5020, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -102420, 0, 3650, 45)
    SetChrPos(0x102, -101580, 0, 3120, 41)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D66")
    SetChrPos(0x107, -102560, 0, 2630, 45)

    label("loc_D66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D85")
    SetChrPos(0x106, -103730, 0, 3450, 45)

    label("loc_D85")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DA4")
    SetChrPos(0x13C, -103730, 0, 3450, 45)

    label("loc_DA4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DC3")
    SetChrPos(0x110, -103380, 0, 2360, 45)

    label("loc_DC3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DDD")

    def lambda_DD5():
        TurnDirection(0x0, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_DD5)

    label("loc_DDD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DF7")

    def lambda_DEF():
        TurnDirection(0x1, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_DEF)

    label("loc_DF7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E11")

    def lambda_E09():
        TurnDirection(0x2, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_E09)

    label("loc_E11")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E2B")

    def lambda_E23():
        TurnDirection(0x3, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_E23)

    label("loc_E2B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E45")

    def lambda_E3D():
        TurnDirection(0x4, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_E3D)

    label("loc_E45")

    TurnDirection(0x10, 0x101, 400)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1034")

    ChrTalk(
        0x101,
        (
            "#000F嗯～打扰一下好吗？\x02\x03",
            "我们两个是看了公告板而来的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_F00")

    ChrTalk(
        0xFE,
        "啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "来得好晚呀。\x01",
            "我还以为你们不来了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F对不起啊，\x01",
            "因为有重要任务在身。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1008")

    label("loc_F00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_F8D")

    ChrTalk(
        0xFE,
        (
            "啊……\x01",
            "你们终于来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，游击士协会\x01",
            "哪个支部都是人手不足，\x01",
            "这也是没办法的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F对不起啊，\x01",
            "因为有重要任务在身。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1008")

    label("loc_F8D")


    ChrTalk(
        0xFE,
        (
            "啊……\x01",
            "来得好快呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我刚刚才\x01",
            "把委托贴上去呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F呵呵呵⊙\x02\x03",
            "#006F我们也是刚调到这里来的，\x01",
            "所以干劲十足呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1008")


    ChrTalk(
        0xFE,
        (
            "我这就把任务内容予以说明，\x01",
            "可以吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_107C")

    label("loc_1034")


    ChrTalk(
        0xFE,
        (
            "咦，是你们。\x01",
            "终于来了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我这就把任务内容予以说明，\x01",
            "可以吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_107C")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_115A")

    ChrTalk(
        0x101,
        (
            "#501F啊，对不起。\x01",
            "现在还不行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊，是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么等你们办完事了\x01",
            "就再到这里来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，我知道了。\x02",
    )

    CloseMessageWindow()
    OP_28(0x2D, 0x1, 0x4000)

    def lambda_114F():
        OP_8C(0x10, 0, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_114F)
    EventEnd(0x0)
    Return()

    label("loc_115A")


    ChrTalk(
        0x101,
        "#006F嗯，明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F募集临时图书馆员……\x01",
            "没错吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        "嗯，是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "有一些让人\x01",
            "束手无策的麻烦事呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F束手无策？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "啊，这个我们之后再说。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在此之前，\x01",
            "还有件事情想让你们解决。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我先拜托你们\x01",
            "这件事情好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F是什么样的事情呢？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "工房的研究室\x01",
            "经常从资料室这里借书……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是有时期限到了，\x01",
            "书却还没有归还。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "首先你们就去\x01",
            "把那些书找回来吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0x101,
        (
            "#000F这样啊，很简单嘛。\x01",
            "大致到哪里去找呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嗯，借书人的所在地有……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "三楼的设计室以及\x01",
            "四楼的实验室和医务室。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F三楼的设计室以及\x01",
            "四楼的实验室和医务室……嗯。\x02\x03",
            "………………就这些吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嗯，是呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "请尽快地找回来。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F嗯，知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我们会很快找回来的。\x02",
    )

    CloseMessageWindow()
    OP_28(0x2D, 0x4, 0x4)
    OP_28(0x2D, 0x4, 0x8)
    OP_28(0x2D, 0x1, 0x1)
    OP_28(0x2D, 0x1, 0x2)
    Call(1, 13)

    def lambda_1442():
        OP_8C(0x10, 0, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1442)
    EventEnd(0x0)
    Return()

    # Function_4_CE1 end

    def Function_5_144D(): pass

    label("Function_5_144D")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-101090, 0, 5020, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -102420, 0, 3650, 45)
    SetChrPos(0x102, -101580, 0, 3120, 41)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14D2")
    SetChrPos(0x107, -102560, 0, 2630, 45)

    label("loc_14D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14F1")
    SetChrPos(0x106, -103730, 0, 3450, 45)

    label("loc_14F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1510")
    SetChrPos(0x13C, -103730, 0, 3450, 45)

    label("loc_1510")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_152F")
    SetChrPos(0x110, -103380, 0, 2360, 45)

    label("loc_152F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1549")

    def lambda_1541():
        TurnDirection(0x0, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1541)

    label("loc_1549")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1563")

    def lambda_155B():
        TurnDirection(0x1, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_155B)

    label("loc_1563")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_157D")

    def lambda_1575():
        TurnDirection(0x2, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1575)

    label("loc_157D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1597")

    def lambda_158F():
        TurnDirection(0x3, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_158F)

    label("loc_1597")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15B1")

    def lambda_15A9():
        TurnDirection(0x4, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_15A9)

    label("loc_15B1")

    TurnDirection(0x10, 0x101, 400)
    OP_0D()

    ChrTalk(
        0xFE,
        (
            "怎么样？\x01",
            "任务进展的如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F呵呵呵～⊙\x01",
            "拿来了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x342)"), scpexpr(EXPR_END)), "loc_1654")
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "归还了\x07\x02",
            "结晶光学论集\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x342, 1)

    label("loc_1654")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x341)"), scpexpr(EXPR_END)), "loc_16A9")
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "归还了\x07\x02",
            "明日料理\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x341, 1)

    label("loc_16A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x340)"), scpexpr(EXPR_END)), "loc_1706")
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "归还了\x07\x02",
            "猫语日常会话入门\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x340, 1)

    label("loc_1706")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F41")
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "全部的书都归还了！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【募集临时图书馆员】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(
        0xFE,
        "嗯……没错……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这么一来，\x01",
            "所有的书都找回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "辛苦你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#502F哼哼，这种工作简直轻而易举。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F的确是小事一桩。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哎呀，果然很靠得住呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么我就立刻\x01",
            "把正式的任务拜托给你们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F啊，这样啊。\x02\x03",
            "就是刚才所说的\x01",
            "让人束手无策的麻烦事吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F究竟是什么样的任务呢？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "基本的目的还是和刚才一样，\x01",
            "找回过了归还期限的资料。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "需要去寻找的书名为\x01",
            "《艾尔贝啄木鸟的生态》。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#015F先记录下来吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，好的好的…………\x01",
            "《啄木鸟的生态》……对吧。\x02\x03",
            "#505F与鸟有关的书……吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1A2A")

    ChrTalk(
        0x107,
        (
            "#060F嗯。\x01",
            "也许是～吧。\x02\x03",
            "因为艾尔贝啄木鸟是\x01",
            "在很久很久以前出现过的鸟的名字。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A81")

    label("loc_1A2A")


    ChrTalk(
        0x107,
        (
            "#060F啊，是的。\x01",
            "我觉得没错～\x02\x03",
            "因为艾尔贝啄木鸟是\x01",
            "在很久很久以前出现过的鸟的名字。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A81")

    TurnDirection(0x101, 0x107, 400)

    ChrTalk(
        0x101,
        "#000F呼～原来是这样啊。\x02",
    )

    CloseMessageWindow()

    label("loc_1AA5")

    TurnDirection(0x102, 0xFE, 400)

    ChrTalk(
        0x102,
        "#010F那么，有什么线索吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嗯，线索是有的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……请看这个。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 400)
    Sleep(100)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "到山村的　池中伫立的　石人\x01",
            "旁边看看吧　会有收获的\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#505F虽然记下来了……\x02\x03",
            "…………这是什么意思呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "是这本书的借书卡\x01",
            "上面写的文字。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总而言之，\x01",
            "这个好像就是书的隐藏地点的相关提示。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F隐藏地点的提示……吗。\x02\x03",
            "这么说来，\x01",
            "一开始借书时就打算把书藏起来了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯，好像是的。\x01",
            "这是过去的研究员所做的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "至于为什么要把书藏起来，\x01",
            "我就怎么也想不明白了……\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，奇怪的人是很多的，\x01",
            "这已经可算是这里的传统了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D4B")
    OP_62(0x107, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x107,
        "#067F啊，啊哈哈…………\x02",
    )

    CloseMessageWindow()

    label("loc_1D4B")


    ChrTalk(
        0xFE,
        (
            "那么接下来就拜托你们了。\x01",
            "好好加油去找吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#004F等、等一下，\x01",
            "就只有这点线索吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊，就只有这些哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "正因为如此，\x01",
            "我才会委托游击士协会嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#007F呼………………\x02\x03",
            "这、这么一说，\x01",
            "我就觉得没希望了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F……我明白了。\x02\x03",
            "困难的任务更要\x01",
            "加倍地努力去做才行。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "就在蔡斯周围的地区调查，\x01",
            "一定可以找到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我会在这里等着的。\x01",
            "找到书之后就把它拿来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F呼…………\x01",
            "只有加油干了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哦呵呵，我很期待哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F89")

    label("loc_1F41")


    ChrTalk(
        0xFE,
        "嗯……没错……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "剩下的书也拜托了。\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 13)

    def lambda_1F7E():
        OP_8C(0x10, 0, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1F7E)
    EventEnd(0x0)
    Return()

    label("loc_1F89")

    Call(1, 13)

    def lambda_1F93():
        OP_8C(0x10, 0, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1F93)
    OP_28(0x2D, 0x4, 0x10)
    OP_28(0x2D, 0x1, 0x20)
    OP_28(0x2E, 0x4, 0x2)
    OP_28(0x2E, 0x4, 0x4)
    OP_28(0x2E, 0x4, 0x8)
    OP_28(0x2E, 0x1, 0x1)
    OP_28(0x2E, 0x1, 0x2)
    OP_28(0x2E, 0x1, 0x4)
    OP_28(0x2E, 0x1, 0x8)
    EventEnd(0x0)
    Return()

    # Function_5_144D end

    def Function_6_1FD0(): pass

    label("Function_6_1FD0")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-101090, 0, 5020, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -102420, 0, 3650, 45)
    SetChrPos(0x102, -101580, 0, 3120, 41)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2055")
    SetChrPos(0x107, -102560, 0, 2630, 45)

    label("loc_2055")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2074")
    SetChrPos(0x106, -103730, 0, 3450, 45)

    label("loc_2074")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2093")
    SetChrPos(0x13C, -103730, 0, 3450, 45)

    label("loc_2093")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20B2")
    SetChrPos(0x110, -103380, 0, 2360, 45)

    label("loc_20B2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_20CC")

    def lambda_20C4():
        TurnDirection(0x0, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_20C4)

    label("loc_20CC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_20E6")

    def lambda_20DE():
        TurnDirection(0x1, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_20DE)

    label("loc_20E6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2100")

    def lambda_20F8():
        TurnDirection(0x2, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_20F8)

    label("loc_2100")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_211A")

    def lambda_2112():
        TurnDirection(0x3, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2112)

    label("loc_211A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2134")

    def lambda_212C():
        TurnDirection(0x4, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_212C)

    label("loc_2134")

    TurnDirection(0x10, 0x101, 400)
    OP_0D()

    ChrTalk(
        0xFE,
        "哎呀……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "把书拿回来了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#508F嗯，拿来了。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x342)"), scpexpr(EXPR_END)), "loc_21E1")
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "归还了\x07\x02",
            "结晶光学论集\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x342, 1)

    label("loc_21E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x341)"), scpexpr(EXPR_END)), "loc_2236")
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "归还了\x07\x02",
            "明日料理\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x341, 1)

    label("loc_2236")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x340)"), scpexpr(EXPR_END)), "loc_2293")
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "归还了\x07\x02",
            "猫语日常会话入门\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x340, 1)

    label("loc_2293")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24B5")
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "全部的书都归还了！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【募集临时图书馆员】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(
        0xFE,
        "嗯……没错……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这么一来，\x01",
            "所有的书都找回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "辛苦你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F对不起，\x01",
            "这么晚才来……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "没关系，\x01",
            "你们还有别的重要工作嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在你们最忙的时候\x01",
            "还是能坚持完成了任务，\x01",
            "我已经很感谢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F嗯……谢谢。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "彼此彼此，非常感谢你们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那你们以后也要继续努力哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F感谢最近一段时间\x01",
            "您对我们的诸多照顾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F再见。\x02",
    )

    CloseMessageWindow()
    OP_28(0x2D, 0x4, 0x10)
    OP_28(0x2D, 0x1, 0x20)
    Jump("loc_2707")

    label("loc_24B5")


    ChrTalk(
        0xFE,
        "嗯，没错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对了，\x01",
            "剩下的书我已经收回来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "所以，\x01",
            "委托就此中止了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F咦……怎么会？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我从协会那里听说了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们马上就要\x01",
            "调到别的支部去了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "所以调离之前，\x01",
            "必须将委托的事宜整理好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F是吗……\x02\x03",
            "对不起。\x01",
            "工作半途而废了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F真的很抱歉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哎呀，不用在意的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们还有别的重要工作嘛。\x01",
            "这也是没办法的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯……谢谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "感谢你们的帮忙。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "要打起精神哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F感谢最近一段时间\x01",
            "您对我们的诸多照顾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#508F再见了。\x02",
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【募集临时图书馆员】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x2D, 0x4, 0x10)
    OP_28(0x2D, 0x1, 0x40)
    Call(1, 13)

    label("loc_2707")

    OP_28(0x2D, 0x4, 0x10)
    OP_28(0x2D, 0x1, 0x4000)
    Call(1, 13)

    def lambda_271C():
        OP_8C(0x10, 0, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_271C)
    EventEnd(0x0)
    Return()

    # Function_6_1FD0 end

    def Function_7_2727(): pass

    label("Function_7_2727")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-101090, 0, 5020, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -102420, 0, 3650, 45)
    SetChrPos(0x102, -101580, 0, 3120, 41)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27AC")
    SetChrPos(0x107, -102560, 0, 2630, 45)

    label("loc_27AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27CB")
    SetChrPos(0x106, -103730, 0, 3450, 45)

    label("loc_27CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27EA")
    SetChrPos(0x13C, -103730, 0, 3450, 45)

    label("loc_27EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2809")
    SetChrPos(0x110, -103380, 0, 2360, 45)

    label("loc_2809")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2823")

    def lambda_281B():
        TurnDirection(0x0, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_281B)

    label("loc_2823")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_283D")

    def lambda_2835():
        TurnDirection(0x1, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2835)

    label("loc_283D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2857")

    def lambda_284F():
        TurnDirection(0x2, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_284F)

    label("loc_2857")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2871")

    def lambda_2869():
        TurnDirection(0x3, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2869)

    label("loc_2871")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_288B")

    def lambda_2883():
        TurnDirection(0x4, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_2883)

    label("loc_288B")

    TurnDirection(0x10, 0x101, 400)
    OP_0D()

    ChrTalk(
        0xFE,
        (
            "啊……\x01",
            "有什么进展吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F嗯，很顺利。\x02\x03",
            "#006F书已经带回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F请您确认一下。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "归还了\x07\x02",
            "艾尔贝啄木鸟的生态\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【临时图书馆员的加班】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x343, 1)
    Sleep(100)

    ChrTalk(
        0xFE,
        "……哎呀，真让我惊讶。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "的确是这本书呢。\x01",
            "终于找回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#502F呵呵呵。\x01",
            "我们还只是小试牛刀而已呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说实话，\x01",
            "我一直认为已经不可能找回来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "能够找回来\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样一来，我就可以放心地\x01",
            "把剩下的任务交给你们了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#004F啊……………！？\x02\x03",
            "……什么，剩下的任务？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F……还有其他的？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "那个研究员隐藏起来的书\x01",
            "一共有三本呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就是说，\x01",
            "还剩下后面的两本哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……我之前没有说过吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F完全没有，根本就是头一次听说。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "哎呀，这可真是奇怪了呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过这样也不错嘛。\x01",
            "现在你们已经是骑虎难下了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就请你们\x01",
            "坚持到最后吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F好吧，\x01",
            "这倒是没什么关系…………\x02\x03",
            "只要别再出现那种含义不明的文字就行了，\x01",
            "那东西真是让人摸不着头脑呢……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_2CB2")

    ChrTalk(
        0x102,
        (
            "#017F说起来，\x01",
            "在卢安也遇到过这样的事情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CB2")


    ChrTalk(
        0xFE,
        (
            "哎呀，\x01",
            "你们不用担心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这本书的提示\x01",
            "并不是什么文字。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊，真的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "事实胜于雄辩，\x01",
            "我这就让你们看看吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "　● 　 ●　\x01",
            "　　 ×\x01",
            "　● 　 ●　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x101)

    ChrTalk(
        0x101,
        (
            "#509F…………………………\x02\x03",
            "……我、我无话可说了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F……一点说明都没有呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2E53")

    ChrTalk(
        0x107,
        (
            "#063F……●和×吗……\x02\x03",
            "唔～是说×记号的地方\x01",
            "就是书的所在地吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E97")

    label("loc_2E53")


    ChrTalk(
        0x107,
        (
            "#063F……●和×吗……\x02\x03",
            "唔～是说×记号的地方\x01",
            "就是书的所在地吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E97")


    ChrTalk(
        0xFE,
        (
            "要寻找的这本书名为\x01",
            "《哈茨少年冒险记·下》哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F好的好的，\x01",
            "《哈茨少年冒险记·下》对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "资料室里只留有上卷，\x01",
            "『下卷在哪里？』想看的人经常这么嚷。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好了，\x01",
            "你们就鼓足干劲去找吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F话虽如此，\x01",
            "这次的更难解决啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F与现在这个相比，\x01",
            "反而觉得有文字的要简单一些呢。\x02\x03",
            "……算了，不管写了什么，\x01",
            "都还是要去找啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "就请你们继续努力寻找吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "和刚才一样，\x01",
            "我会在这里等着的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那么我们就出发吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F好的，加油干吧。\x02",
    )

    CloseMessageWindow()
    OP_28(0x2E, 0x4, 0x10)
    OP_28(0x2E, 0x1, 0x20)
    OP_28(0x2F, 0x4, 0x2)
    OP_28(0x2F, 0x4, 0x4)
    OP_28(0x2F, 0x4, 0x8)
    OP_28(0x2F, 0x1, 0x1)
    OP_28(0x2F, 0x1, 0x2)
    OP_28(0x2F, 0x1, 0x4)
    Call(1, 13)

    def lambda_30A3():
        OP_8C(0x10, 0, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_30A3)
    EventEnd(0x0)
    Return()

    # Function_7_2727 end

    def Function_8_30AE(): pass

    label("Function_8_30AE")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-101090, 0, 5020, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -102420, 0, 3650, 45)
    SetChrPos(0x102, -101580, 0, 3120, 41)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3133")
    SetChrPos(0x107, -102560, 0, 2630, 45)

    label("loc_3133")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3152")
    SetChrPos(0x106, -103730, 0, 3450, 45)

    label("loc_3152")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3171")
    SetChrPos(0x13C, -103730, 0, 3450, 45)

    label("loc_3171")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3190")
    SetChrPos(0x110, -103380, 0, 2360, 45)

    label("loc_3190")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31AA")

    def lambda_31A2():
        TurnDirection(0x0, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_31A2)

    label("loc_31AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31C4")

    def lambda_31BC():
        TurnDirection(0x1, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_31BC)

    label("loc_31C4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31DE")

    def lambda_31D6():
        TurnDirection(0x2, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_31D6)

    label("loc_31DE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31F8")

    def lambda_31F0():
        TurnDirection(0x3, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_31F0)

    label("loc_31F8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3212")

    def lambda_320A():
        TurnDirection(0x4, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_320A)

    label("loc_3212")

    TurnDirection(0x10, 0x101, 400)
    OP_0D()

    ChrTalk(
        0xFE,
        (
            "啊……\x01",
            "你们把书拿来了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，对啊，\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F请您确认一下。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "归还了\x07\x02",
            "艾尔贝啄木鸟的生态\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【临时图书馆员的加班】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x343, 1)
    Sleep(100)

    ChrTalk(
        0xFE,
        "……哎呀，真让我惊讶。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "的确是这本书呢。\x01",
            "终于找回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F对不起，\x01",
            "这么晚才来……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "没关系，\x01",
            "你们还有别的重要工作嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在你们最忙的时候\x01",
            "还是能完成了任务，\x01",
            "我已经很感谢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯……谢谢。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "那再见吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "各位请慢走。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F感谢最近一段时间\x01",
            "您对我们的诸多照顾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#508F再见了。\x02",
    )

    CloseMessageWindow()
    OP_28(0x2E, 0x4, 0x10)
    OP_28(0x2E, 0x1, 0x20)
    OP_28(0x2D, 0x1, 0x4000)
    Call(1, 13)

    def lambda_346B():
        OP_8C(0x10, 0, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_346B)
    EventEnd(0x0)
    Return()

    # Function_8_30AE end

    def Function_9_3476(): pass

    label("Function_9_3476")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-101090, 0, 5020, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -102420, 0, 3650, 45)
    SetChrPos(0x102, -101580, 0, 3120, 41)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34FB")
    SetChrPos(0x107, -102560, 0, 2630, 45)

    label("loc_34FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_351A")
    SetChrPos(0x106, -103730, 0, 3450, 45)

    label("loc_351A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3539")
    SetChrPos(0x13C, -103730, 0, 3450, 45)

    label("loc_3539")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3558")
    SetChrPos(0x110, -103380, 0, 2360, 45)

    label("loc_3558")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3572")

    def lambda_356A():
        TurnDirection(0x0, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_356A)

    label("loc_3572")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_358C")

    def lambda_3584():
        TurnDirection(0x1, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3584)

    label("loc_358C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_35A6")

    def lambda_359E():
        TurnDirection(0x2, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_359E)

    label("loc_35A6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_35C0")

    def lambda_35B8():
        TurnDirection(0x3, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_35B8)

    label("loc_35C0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_35DA")

    def lambda_35D2():
        TurnDirection(0x4, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_35D2)

    label("loc_35DA")

    TurnDirection(0x10, 0x101, 400)
    OP_0D()

    ChrTalk(
        0xFE,
        "哎呀…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……难道，\x01",
            "你们已经找到书了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#502F呵呵呵，的确找到了哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F请您确认一下。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "归还了\x07\x02",
            "哈茨少年冒险记·下\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【续·临时图书馆员的加班】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x344, 1)
    Sleep(100)

    ChrTalk(
        0xFE,
        "……嗯，确实是这本呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "这样就只剩最后一本了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F呼，好歹也让我喘口气吧。\x02\x03",
            "#006F那么，\x01",
            "接下来要找的是什么书呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哦呵呵，不要着急，\x01",
            "我这就告诉你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最后要找的是名为\x01",
            "《３１棵丝柏树》的书。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……这是它对应的借书卡，\x01",
            "在这上面又写着\x01",
            "一些含义不明的文字。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "　去问风景今何在\x01",
            "　呀，山上耸立３\x01",
            "　１棵丝柏。钟楼\x01",
            "　宁远音，隔世的\x01",
            "　饱经之苦如斜木\x01",
            "　之坡上滚落酒桶\x01",
            "　长阵，接近梦中\x01",
            "　沉眠不绝的我。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#509F这次的更古怪啊～\x02\x03",
            "#007F算了，\x01",
            "不管怎么说都只有知难而进了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F又是谜语吗？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3971")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_395A")

    ChrTalk(
        0x107,
        "#062F嗯，好像是～呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3971")

    label("loc_395A")


    ChrTalk(
        0x107,
        "#062F好像是～呢。\x02",
    )

    CloseMessageWindow()

    label("loc_3971")


    ChrTalk(
        0xFE,
        (
            "已经对这个\x01",
            "驾轻就熟了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呵呵……\x01",
            "这样就可以一气呵成了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了彻底达到目标，\x01",
            "好好地加油吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#508F那我们就出发了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F告辞了。\x02",
    )

    CloseMessageWindow()
    OP_28(0x2F, 0x4, 0x10)
    OP_28(0x2F, 0x1, 0x10)
    OP_28(0x30, 0x4, 0x2)
    OP_28(0x30, 0x4, 0x4)
    OP_28(0x30, 0x4, 0x8)
    OP_28(0x30, 0x1, 0x1)
    OP_28(0x30, 0x1, 0x2)
    Call(1, 13)

    def lambda_3A3C():
        OP_8C(0x10, 0, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3A3C)
    EventEnd(0x0)
    Return()

    # Function_9_3476 end

    def Function_10_3A47(): pass

    label("Function_10_3A47")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-101090, 0, 5020, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -102420, 0, 3650, 45)
    SetChrPos(0x102, -101580, 0, 3120, 41)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3ACC")
    SetChrPos(0x107, -102560, 0, 2630, 45)

    label("loc_3ACC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AEB")
    SetChrPos(0x106, -103730, 0, 3450, 45)

    label("loc_3AEB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B0A")
    SetChrPos(0x13C, -103730, 0, 3450, 45)

    label("loc_3B0A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B29")
    SetChrPos(0x110, -103380, 0, 2360, 45)

    label("loc_3B29")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B43")

    def lambda_3B3B():
        TurnDirection(0x0, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3B3B)

    label("loc_3B43")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B5D")

    def lambda_3B55():
        TurnDirection(0x1, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3B55)

    label("loc_3B5D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B77")

    def lambda_3B6F():
        TurnDirection(0x2, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3B6F)

    label("loc_3B77")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B91")

    def lambda_3B89():
        TurnDirection(0x3, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3B89)

    label("loc_3B91")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3BAB")

    def lambda_3BA3():
        TurnDirection(0x4, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_3BA3)

    label("loc_3BAB")

    TurnDirection(0x10, 0x101, 400)
    OP_0D()

    ChrTalk(
        0xFE,
        "哎呀…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你们把书拿来了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#508F嗯，是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F请您确认一下。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "归还了\x07\x02",
            "哈茨少年冒险记·下\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【续·临时图书馆员的加班】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x344, 1)
    Sleep(100)

    ChrTalk(
        0xFE,
        "……哎呀，真让我惊讶。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "的确是这本书呢。\x01",
            "终于找回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样嘛，\x01",
            "委托就此中止了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F咦……为什么？\x02\x03",
            "不是说还有书没有收回来吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我从协会那里听说了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们马上就要\x01",
            "调到别的支部去了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "所以调离之前，\x01",
            "必须将委托的事宜整理好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F是吗……\x02\x03",
            "对不起。\x01",
            "工作半途而废了……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "你们还有别的重要工作嘛。\x01",
            "这也是没办法的事啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们能做到这个份上\x01",
            "已经足够了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "剩下的工作\x01",
            "由蔡斯支部的其他人\x01",
            "去完成就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯……谢谢。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "彼此彼此，非常感谢你们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那你们以后也要继续努力哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F感谢最近一段时间\x01",
            "您对我们的诸多照顾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F再见。\x02",
    )

    CloseMessageWindow()
    OP_28(0x2F, 0x4, 0x10)
    OP_28(0x2F, 0x1, 0x10)
    OP_28(0x2F, 0x1, 0x20)
    OP_28(0x2D, 0x1, 0x4000)
    Call(1, 13)

    def lambda_3F2F():
        OP_8C(0x10, 0, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3F2F)
    EventEnd(0x0)
    Return()

    # Function_10_3A47 end

    def Function_11_3F3A(): pass

    label("Function_11_3F3A")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-101090, 0, 5020, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -102420, 0, 3650, 45)
    SetChrPos(0x102, -101580, 0, 3120, 41)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FBF")
    SetChrPos(0x107, -102560, 0, 2630, 45)

    label("loc_3FBF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FDE")
    SetChrPos(0x106, -103730, 0, 3450, 45)

    label("loc_3FDE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FFD")
    SetChrPos(0x13C, -103730, 0, 3450, 45)

    label("loc_3FFD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_401C")
    SetChrPos(0x110, -103380, 0, 2360, 45)

    label("loc_401C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4036")

    def lambda_402E():
        TurnDirection(0x0, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_402E)

    label("loc_4036")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4050")

    def lambda_4048():
        TurnDirection(0x1, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4048)

    label("loc_4050")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_406A")

    def lambda_4062():
        TurnDirection(0x2, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4062)

    label("loc_406A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4084")

    def lambda_407C():
        TurnDirection(0x3, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_407C)

    label("loc_4084")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_409E")

    def lambda_4096():
        TurnDirection(0x4, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_4096)

    label("loc_409E")

    TurnDirection(0x10, 0x101, 400)
    OP_0D()

    ChrTalk(
        0xFE,
        "哎呀…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……难道？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯，\x01",
            "最后一本书也已经找到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F为了慎重起见，\x01",
            "还请您确认一下。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "归还了\x07\x02",
            "３１棵丝柏树\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【再续·临时图书管理员的加班】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x345, 1)
    Sleep(100)

    ChrTalk(
        0xFE,
        "……嗯，就是它没错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好厉害呀，\x01",
            "真的把３本都找到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F嘿嘿，\x01",
            "因为我们很努力地找啊找啊。\x02\x03",
            "#000F啊，对了……\x01",
            "我们还找到了其他的东西呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是和书放在一起的……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "约修亚说明了找到犯人留下的字条\x01",
            "和结晶回路的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(
        0xFE,
        (
            "呼～\x01",
            "竟然是出于这样的动机。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，不管是什么样的理由，\x01",
            "也不能给别人制造这么大的麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那个结晶回路\x01",
            "你们就拿去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为让你们费了不少功夫，\x01",
            "就算是回报吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F嗯，非常感谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F那么，到现在为止，\x01",
            "任务已经做完了吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "嗯，是呀。\x01",
            "任务已经全部完成了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F呼，太好了～\x02\x03",
            "我到现在都还觉得\x01",
            "会有新任务冒出来。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4458")

    ChrTalk(
        0x107,
        "#061F嘿嘿，是啊……\x02",
    )

    CloseMessageWindow()

    label("loc_4458")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "由于你们的努力，\x01",
            "麻烦事已经全部解决了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呵呵，\x01",
            "真的很感谢你们哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "托你们的福，\x01",
            "最近一段时间我也没事了，太好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F啊？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "……没、没什么。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，辛苦你们了。\x01",
            "如果再有事情还要麻烦你们哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F嗯，交给我们吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F承蒙您多方的关照，\x01",
            "告辞了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    OP_28(0x30, 0x4, 0x10)
    OP_28(0x30, 0x1, 0x8)
    Call(1, 13)

    def lambda_459A():
        OP_8C(0x10, 0, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_459A)
    EventEnd(0x0)
    Return()

    # Function_11_3F3A end

    def Function_12_45A5(): pass

    label("Function_12_45A5")

    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "结晶光学论集\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x342, 1)
    SetChrFlags(0x18, 0x80)
    OP_64(0x7, 0x1)
    OP_28(0x2D, 0x1, 0x4)
    TalkEnd(0xFF)
    Return()

    # Function_12_45A5 end

    def Function_13_460E(): pass

    label("Function_13_460E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2E, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_461D")
    OP_65(0xD, 0x1)

    label("loc_461D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2F, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_462C")
    OP_65(0x9, 0x1)

    label("loc_462C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_463B")
    OP_65(0xE, 0x1)

    label("loc_463B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x342)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4650")
    OP_65(0xA, 0x1)

    label("loc_4650")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x341)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4665")
    OP_65(0xB, 0x1)

    label("loc_4665")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x340)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_467A")
    OP_65(0xC, 0x1)

    label("loc_467A")

    Return()

    # Function_13_460E end

    SaveToFile()

Try(main)
