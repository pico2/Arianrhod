from ED6ScenarioHelper import *

def main():
    # 柏斯

    CreateScenaFile(
        FileName            = 'T1210   ._SN',
        MapName             = 'Bose',
        Location            = 'T1210.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T1210   ._SN',
            'ED6_DT01/T1210_1 ._SN',
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
        '奥兰橘婆婆',                           # 9
        '库赖老人',                             # 10
        '莱森村长',                             # 11
        '碧尔奈婆婆',                           # 12
        '鲁伊',                                 # 13
        '菲戈',                                 # 14
        '罗亚',                                 # 15
        '贝斯卡',                               # 16
        '库赖老人',                             # 17
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
        'ED6_DT07/CH01010 ._CH',             # 00
        'ED6_DT07/CH01000 ._CH',             # 01
        'ED6_DT07/CH01490 ._CH',             # 02
        'ED6_DT07/CH01180 ._CH',             # 03
        'ED6_DT07/CH01470 ._CH',             # 04
        'ED6_DT07/CH01020 ._CH',             # 05
        'ED6_DT07/CH01123 ._CH',             # 06
        'ED6_DT07/CH01143 ._CH',             # 07
        'ED6_DT07/CH00003 ._CH',             # 08
        'ED6_DT07/CH00013 ._CH',             # 09
        'ED6_DT07/CH00023 ._CH',             # 0A
        'ED6_DT07/CH01003 ._CH',             # 0B
        'ED6_DT07/CH01493 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT07/CH01010P._CP',             # 00
        'ED6_DT07/CH01000P._CP',             # 01
        'ED6_DT07/CH01490P._CP',             # 02
        'ED6_DT07/CH01180P._CP',             # 03
        'ED6_DT07/CH01470P._CP',             # 04
        'ED6_DT07/CH01020P._CP',             # 05
        'ED6_DT07/CH01123P._CP',             # 06
        'ED6_DT07/CH01143P._CP',             # 07
        'ED6_DT07/CH00003P._CP',             # 08
        'ED6_DT07/CH00013P._CP',             # 09
        'ED6_DT07/CH00023P._CP',             # 0A
        'ED6_DT07/CH01003P._CP',             # 0B
        'ED6_DT07/CH01493P._CP',             # 0C
    )

    DeclNpc(
        X                   = -31600,
        Z                   = 0,
        Y                   = 2900,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -25500,
        Z                   = 0,
        Y                   = 8700,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -1880,
        Z                   = 0,
        Y                   = 48500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 7500,
        Z                   = 0,
        Y                   = 46200,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -1430,
        Z                   = 0,
        Y                   = 3310,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 360,
        Z                   = 0,
        Y                   = 6440,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 4650,
        Z                   = 100,
        Y                   = 45830,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 3300,
        Z                   = 200,
        Y                   = 48070,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 3430,
        Z                   = 150,
        Y                   = 45650,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )


    ScpFunction(
        "Function_0_232",          # 00, 0
        "Function_1_338",          # 01, 1
        "Function_2_339",          # 02, 2
        "Function_3_34F",          # 03, 3
        "Function_4_373",          # 04, 4
        "Function_5_8C3",          # 05, 5
        "Function_6_9D3",          # 06, 6
        "Function_7_1764",         # 07, 7
        "Function_8_1CA0",         # 08, 8
        "Function_9_1F27",         # 09, 9
        "Function_10_23D9",        # 0A, 10
        "Function_11_2474",        # 0B, 11
        "Function_12_2555",        # 0C, 12
    )


    def Function_0_232(): pass

    label("Function_0_232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_27C")
    SetChrPos(0x9, 3300, -1000, 45700, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xA, 6180, 0, 49500, 0)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_318")

    label("loc_27C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_2A1")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -780, 0, 5750, 0)
    Jump("loc_318")

    label("loc_2A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_2C6")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -780, 0, 5750, 0)
    Jump("loc_318")

    label("loc_2C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_2E6")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -780, 0, 5750, 0)
    Jump("loc_318")

    label("loc_2E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_318")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -1820, 0, 47460, 0)
    SetChrPos(0xA, -1880, 0, 48500, 180)

    label("loc_318")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_329")
    SetChrFlags(0xA, 0x80)

    label("loc_329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_337")
    OP_A3(0x3FA)
    Event(0, 12)

    label("loc_337")

    Return()

    # Function_0_232 end

    def Function_1_338(): pass

    label("Function_1_338")

    Return()

    # Function_1_338 end

    def Function_2_339(): pass

    label("Function_2_339")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_34E")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_339")

    label("loc_34E")

    Return()

    # Function_2_339 end

    def Function_3_34F(): pass

    label("Function_3_34F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_372")
    OP_8D(0xFE, -2590, 3920, 2730, 920, 1500)
    Jump("Function_3_34F")

    label("loc_372")

    Return()

    # Function_3_34F end

    def Function_4_373(): pass

    label("Function_4_373")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_3BB")

    ChrTalk(
        0xFE,
        "你们是来选购水果的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我家老头子\x01",
            "到村长家去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BF")

    label("loc_3BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_493")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_456")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "希望老头子能找个机会\x01",
            "和村里的人们一起\x01",
            "坐下来好好谈谈。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是老头子很久以前\x01",
            "就非常顽固……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "希望有人能够\x01",
            "在其中调解一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_490")

    label("loc_456")


    ChrTalk(
        0xFE,
        (
            "希望能够找个机会\x01",
            "让老头子和村里的人\x01",
            "坐下来好好谈谈。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_490")

    Jump("loc_8BF")

    label("loc_493")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_58E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52D")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "又有军队的人\x01",
            "来这个村子里调查案件了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "和之前来的士兵不同，\x01",
            "他们的动作非常迅速干脆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那肯定是因为\x01",
            "指挥他们的人换了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58B")

    label("loc_52D")


    ChrTalk(
        0xFE,
        (
            "又有军队的人\x01",
            "来这个村子里调查案件了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "和之前来的士兵不同，\x01",
            "他们的动作非常迅速干脆。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58B")

    Jump("loc_8BF")

    label("loc_58E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_67C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63D")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "我可不觉得\x01",
            "老头子的意见有什么错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为他培育出了这个村里最好吃的东西，\x01",
            "这可是事实。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，\x01",
            "如果能稍微采纳一些其他的方法，\x01",
            "是不是会更好呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_679")

    label("loc_63D")


    ChrTalk(
        0xFE,
        (
            "老头子如果能稍微\x01",
            "采纳一些其他的方法，\x01",
            "是不是会更好呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_679")

    Jump("loc_8BF")

    label("loc_67C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_75F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70C")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "我家的老头子，\x01",
            "头脑真是有点硬呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一直拘泥于\x01",
            "以前流传下来的古老方法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "和现在的年轻人\x01",
            "所提出的意见总是不合。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_75C")

    label("loc_70C")


    ChrTalk(
        0xFE,
        (
            "我家的老头子，\x01",
            "头脑真是有点硬呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "希望年轻人们\x01",
            "不要因此望而生畏才好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_75C")

    Jump("loc_8BF")

    label("loc_75F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_864")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FD")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "我们家的老头子啊，\x01",
            "总是呆在果园里面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "即使去叫他回来吃饭，\x01",
            "也要过一个小时才能看到他回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要等到饭菜都凉了，\x01",
            "他才会回来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_861")

    label("loc_7FD")


    ChrTalk(
        0xFE,
        (
            "我们家的老头子啊，\x01",
            "总是呆在果园里面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "即使去叫他回来吃饭，\x01",
            "也要过一个小时才能看到他回来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_861")

    Jump("loc_8BF")

    label("loc_864")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_8BF")

    ChrTalk(
        0xFE,
        (
            "难不成\x01",
            "你们是来买水果的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真抱歉，老头子出去了。\x01",
            "应该是到果树园那里去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BF")

    TalkEnd(0x8)
    Return()

    # Function_4_373 end

    def Function_5_8C3(): pass

    label("Function_5_8C3")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_913")

    ChrTalk(
        0xFE,
        (
            "我想用我自己的方法\x01",
            "来种出美味的水果。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我不赞同那种做法。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9CF")

    label("loc_913")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_959")

    ChrTalk(
        0xFE,
        (
            "下次开会时，\x01",
            "我要让村里的年轻人\x01",
            "再注意一下做法才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CF")

    label("loc_959")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_9CF")

    ChrTalk(
        0xFE,
        (
            "我要让大家知道\x01",
            "尽量让果树保持自然生长，\x01",
            "这才是最重要的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就是要肯花时间，\x01",
            "它们才能结出美味的果实。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9CF")

    TalkEnd(0x9)
    Return()

    # Function_5_8C3 end

    def Function_6_9D3(): pass

    label("Function_6_9D3")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_A05")

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "好像大家的意见无法统一啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1760")

    label("loc_A05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_AD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A8B")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "乍一看这个村子\x01",
            "可能非常平静……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是还存在着\x01",
            "好多隐藏的问题啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "也只有一个一个来解决它们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD5")

    label("loc_A8B")


    ChrTalk(
        0xFE,
        (
            "乍一看这个村子\x01",
            "可能非常平静……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是还存在着\x01",
            "好多隐藏的问题啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AD5")

    Jump("loc_1760")

    label("loc_AD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_BA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B3E")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "哦哦，是各位游击士啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那之后你们被王国军带走了，\x01",
            "我还真替你们担心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA5")

    label("loc_B3E")


    ChrTalk(
        0xFE,
        (
            "没想到飞艇\x01",
            "真的藏在那种地方……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为那些犯人\x01",
            "很有可能还会再回来，\x01",
            "所以废坑就由军队来接管了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA5")

    Jump("loc_1760")

    label("loc_BA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_C10")
    OP_4A(0xFE, 255)

    ChrTalk(
        0xFE,
        (
            "要是在废坑中\x01",
            "可以找到什么线索就好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果你们知道了什么，\x01",
            "一定要回来告诉我。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1760")

    label("loc_C10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_CC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C8E")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "鲁伊所看到的空中飞影……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "难道说是『他』……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不会……不可能……\x01",
            "已经好几十年没有发生过了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CC1")

    label("loc_C8E")


    ChrTalk(
        0xFE,
        (
            "不会……不可能……\x01",
            "已经好几十年没有发生过了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CC1")

    Jump("loc_1760")

    label("loc_CC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_143E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13EF")
    OP_A2(0x31B)
    OP_28(0x36, 0x1, 0x4)
    EventBegin(0x0)
    OP_69(0xFE, 0x3E8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_F4E")

    ChrTalk(
        0xFE,
        (
            "哦哦～\x01",
            "你们都来了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天有什么事？\x01",
            "大家是来这里玩的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F不是，我们还有工作要忙。\x02\x03",
            "有些遗憾呢，\x01",
            "其实我很想喝一杯果实酒再走。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呵、呵、呵。\x01",
            "这个世上，有许多事不会随着你的想法而进行的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对了，\x01",
            "之前我忘了问了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难道，\x01",
            "你们是阿加特的同事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F嗯，虽然是同行，\x01",
            "但并不代表我们会一起行动。\x02\x03",
            "充其量也就是认识而已吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "是这样吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "他依旧还是独来独往啊……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "村长幽寂地闭上了眼睛。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        (
            "#501F？？？\x02\x03",
            "怎么了，村长？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊，不好意思，失礼了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "到这种偏僻的村庄有什么事呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难道又是为了\x01",
            "被通缉的魔兽而来的？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1182")

    label("loc_F4E")


    ChrTalk(
        0xFE,
        (
            "啊，几位客人。\x01",
            "是来买水果的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F不，我们不是商人。\x01",
            "我们是游击士协会的人。\x02\x03",
            "您是这个村子的村长吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯，是的。\x01",
            "也算是本村的负责人吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "刚才是说游击士协会对吧。\x01",
            "难道你们是阿加特的同事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F嗯，虽然是同行，\x01",
            "但并不代表我们会一起行动。\x02\x03",
            "充其量也就是认识而已吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "是这样吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "他依旧还是独来独往啊……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "村长幽寂地闭上了眼睛。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        (
            "#501F？？？\x02\x03",
            "怎么了，村长？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊，不好意思，失礼了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，各位游击士，\x01",
            "到这种偏僻的村庄有什么事呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难道说，是为了消灭\x01",
            "这附近被通缉的魔兽而来的？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1182")


    ChrTalk(
        0x102,
        (
            "#010F不是的，其实……\x01",
            "我们正在调查\x01",
            "失踪定期船的事件。\x02\x03",
            "听说这里有目击者，\x01",
            "所以前来打扰一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "什么，是说这个啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "前几天，\x01",
            "王国军的士兵已经来调查过了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他们把这附近都搜查了一遍，\x01",
            "结果还不是两手空空地回去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F果然是这样啊……\x02\x03",
            "顺便问一下，那个目击到\x01",
            "夜空中飞过的黑影的人是谁啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是村里的孩子。\x01",
            "一个叫鲁伊的男孩子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "事件发生的那个晚上，\x01",
            "他好像看到了奇怪的影子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过毕竟还是个小孩子……\x01",
            "说不定是睡糊涂了梦见的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F嗯～是梦吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F总之，\x01",
            "还是当面听那个孩子说说比较好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯，也对。\x02\x03",
            "村长，打扰您了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没事没事。\x01",
            "还有什么事情的话就过来吧。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_143B")

    label("loc_13EF")


    ChrTalk(
        0xFE,
        (
            "鲁伊那小子\x01",
            "肯定就在村子里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个村子很小，\x01",
            "应该很快就能找到他的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_143B")

    Jump("loc_1760")

    label("loc_143E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_1760")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_145F")
    Call(1, 0)
    Jump("loc_1760")

    label("loc_145F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x1, 0x800)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_159B")
    OP_28(0xE, 0x1, 0x800)
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "哦哦，\x01",
            "是游击士们啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我都听说了，\x01",
            "魔兽已经被你们消灭了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，总算是成功了。\x01",
            "它可是个颇强的对手呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "这样一来，\x01",
            "我们今年就可以\x01",
            "安安心心地种植树苗了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "各位，\x01",
            "真的是辛苦你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们这个偏僻的小村，\x01",
            "随时都欢迎你们的到来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F嗯，谢谢村长爷爷。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1760")

    label("loc_159B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1607")

    ChrTalk(
        0xFE,
        (
            "各位能帮我们消灭魔兽，\x01",
            "真的是太感谢你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们这个偏僻的小村，\x01",
            "随时都欢迎你们的到来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1760")

    label("loc_1607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16F9")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "哦哦，是各位游击士啊。\x01",
            "辛苦你们消灭魔兽了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "请进请进，\x01",
            "不要客气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，现在村子的这个样子，\x01",
            "我想都不敢想……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在１０年前的战争中，\x01",
            "这里受到了很大的伤害。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "从战后的情况来看，\x01",
            "这里竟然能够\x01",
            "复兴到这个地步。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1760")

    label("loc_16F9")


    ChrTalk(
        0xFE,
        (
            "从战后的情况来看，\x01",
            "这个村子能够走到这步，\x01",
            "复兴到这个地步。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这一切都要归功于\x01",
            "村民们的努力啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1760")

    TalkEnd(0xA)
    Return()

    # Function_6_9D3 end

    def Function_7_1764(): pass

    label("Function_7_1764")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_17F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17CA")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "唉……\x01",
            "这次集会终于结束了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那两个人只要一见面，\x01",
            "总会演变成那样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17F5")

    label("loc_17CA")


    ChrTalk(
        0xFE,
        (
            "那两个人只要一见面，\x01",
            "总会演变成那样。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17F5")

    Jump("loc_1C9C")

    label("loc_17F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_18F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1896")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "虽然很痛苦，\x01",
            "但是我们也不能忘记１０年前的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "既为了不再让\x01",
            "同样的错误重蹈覆辙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "也要尽可能让下一代\x01",
            "将这件事铭记于心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18F2")

    label("loc_1896")


    ChrTalk(
        0xFE,
        (
            "虽然很痛苦，\x01",
            "但是我们也不能忘记１０年前的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了不再让\x01",
            "同样的错误重蹈覆辙……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18F2")

    Jump("loc_1C9C")

    label("loc_18F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_19C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_197B")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "看到这些士兵，\x01",
            "我就会想起１０年前的事，\x01",
            "然后就会感到揪心地痛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是不想见到他们\x01",
            "在这个村子进进出出的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19BF")

    label("loc_197B")


    ChrTalk(
        0xFE,
        (
            "看到这些士兵，\x01",
            "我就会想起１０年前的事，\x01",
            "然后就会感到揪心地痛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19BF")

    Jump("loc_1C9C")

    label("loc_19C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 6)), scpexpr(EXPR_END)), "loc_1A7E")

    ChrTalk(
        0xFE,
        (
            "以前矿山很景气的时候，\x01",
            "这个村子也非常繁荣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "到处都是矿工和商人，\x01",
            "人多得都可以和大城市相提并论了，\x01",
            "村子非常有活力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "自从战争开始到现在，\x01",
            "这里已经变得非常冷清了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C9C")

    label("loc_1A7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_1AC5")

    ChrTalk(
        0xFE,
        "在找村长吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "平时这个时候，\x01",
            "我想他应该在那里的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C9C")

    label("loc_1AC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_1B25")

    ChrTalk(
        0xFE,
        (
            "我们夫妇每天\x01",
            "都会去山岗上扫墓。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "希望能够不使那些\x01",
            "当时死去的村民们感到寂寞。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C9C")

    label("loc_1B25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_1C2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BCD")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "能将皮肤烤焦的热气，\x01",
            "满屋子被烧焦的味道……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "村民们的悲泣声此起彼伏，\x01",
            "还有孩子们的哭叫声……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不管过了多久，\x01",
            "我都无法忘却这一情景……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C29")

    label("loc_1BCD")


    ChrTalk(
        0xFE,
        (
            "说起来那个孩子\x01",
            "好久才回来一次啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "跟我说一声的话，\x01",
            "我可以早点去那家打扫一下的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C29")

    Jump("loc_1C9C")

    label("loc_1C2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_1C9C")

    ChrTalk(
        0xFE,
        (
            "这个村的人都是\x01",
            "在１０年前的战火中\x01",
            "幸存下来的村民。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "大家都希望以后能够和睦相处，\x01",
            "生活代代安定。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C9C")

    TalkEnd(0xB)
    Return()

    # Function_7_1764 end

    def Function_8_1CA0(): pass

    label("Function_8_1CA0")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1F23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 6)), scpexpr(EXPR_END)), "loc_1D02")

    ChrTalk(
        0xFE,
        (
            "废坑现在还处在\x01",
            "军队的大叔们看管之下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他们好像\x01",
            "调查到了很多东西呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F23")

    label("loc_1D02")

    TurnDirection(0xFE, 0x101, 0)
    OP_A2(0x38E)

    ChrTalk(
        0xFE,
        "啊，是姐姐啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F你好啊～鲁伊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那之后，\x01",
            "军队就来把姐姐们带走了，\x01",
            "把我吓死了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "姐姐们明明\x01",
            "什么坏事也没有做啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没什么事吧？\x01",
            "他们没有刁难你们吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F哎呀呀，\x01",
            "让你为我们担心了……\x02\x03",
            "#006F没事啦，\x01",
            "你看我现在不是很有活力吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嗯，那就好……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我所看到的那个，\x01",
            "果然是飞艇啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "姐姐， \x01",
            "谢谢你为我作证！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F嗯……\x02\x03",
            "不过最后反正会被\x01",
            "王国军证明清楚，\x01",
            "我的心里还真不是滋味啊……\x02\x03",
            "他们还把我们\x01",
            "误认为空贼而抓走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F算了，\x01",
            "这次虽然有些丢脸，\x01",
            "不过我们还是守住了约定……\x02\x03",
            "这不是挺好吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F23")

    TalkEnd(0xC)
    Return()

    # Function_8_1CA0 end

    def Function_9_1F27(): pass

    label("Function_9_1F27")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1F71")

    ChrTalk(
        0xFE,
        "呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "种苗的栽插结束了，\x01",
            "我也终于可以休息一下了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23D5")

    label("loc_1F71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_208E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_201C")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "拉文努村果树园\x01",
            "是由全体村民来管理的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过呢，\x01",
            "最初是由个人进行管理的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "果树栽培非常需要人手，\x01",
            "所以我觉得还是\x01",
            "全体村民一起来干比较好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_208B")

    label("loc_201C")


    ChrTalk(
        0xFE,
        (
            "拉文努村果树园\x01",
            "是由全体村民来管理的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "果树栽培非常需要人手，\x01",
            "所以我觉得还是\x01",
            "全体村民一起来干比较好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_208B")

    Jump("loc_23D5")

    label("loc_208E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_20EC")

    ChrTalk(
        0xFE,
        (
            "鲁伊是在战争结束之后\x01",
            "才出生的孩子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我可不想让那孩子\x01",
            "经历那种恐怖的体验。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23D5")

    label("loc_20EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_2133")

    ChrTalk(
        0xFE,
        (
            "鲁伊那家伙\x01",
            "看起来心情似乎很好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "遇到什么好事了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_23D5")

    label("loc_2133")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_2223")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21D2")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "鲁伊那家伙\x01",
            "好像又在哭了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他说他看见夜空中\x01",
            "有黑影在飞也确实有点……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我想他可能是\x01",
            "看到动物或是别的什么，\x01",
            "于是就误会了吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2220")

    label("loc_21D2")


    ChrTalk(
        0xFE,
        (
            "鲁伊那家伙\x01",
            "好像又在哭了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他说他看见夜空中\x01",
            "有黑影在飞也确实有点……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2220")

    Jump("loc_23D5")

    label("loc_2223")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_232D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22E1")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        "去看过村里的墓地了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那些墓碑下的人\x01",
            "是在百日战役中的牺牲者。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "１０年前的某一天，\x01",
            "这里经历了战争的洗礼……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "直到今日，\x01",
            "我仍然能够在梦中见到那幅惨景。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_232A")

    label("loc_22E1")


    ChrTalk(
        0xFE,
        "去看过村里的墓地了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那些墓碑下的人\x01",
            "是在百日战役中的牺牲者。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_232A")

    Jump("loc_23D5")

    label("loc_232D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_23D5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x1, 0x1000)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_23D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_238F")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        "呀，辛苦你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我已经向村长\x01",
            "说明事情的经过了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23D5")

    label("loc_238F")


    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "魔兽也已经被消灭了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "接下来就要\x01",
            "开始挑选树苗了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23D5")

    TalkEnd(0xD)
    Return()

    # Function_9_1F27 end

    def Function_10_23D9(): pass

    label("Function_10_23D9")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_2470")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_243F")
    OP_A2(0x7)

    ChrTalk(
        0xFE,
        "唉……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果他们两个\x01",
            "能够融洽相处的话，\x01",
            "我就能够放心地去柏斯城里了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2470")

    label("loc_243F")


    ChrTalk(
        0xFE,
        (
            "真的很想早点跟\x01",
            "在柏斯的老婆和孩子见面呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2470")

    TalkEnd(0xE)
    Return()

    # Function_10_23D9 end

    def Function_11_2474(): pass

    label("Function_11_2474")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_2551")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24EB")
    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "我们当然不是要\x01",
            "舍弃口味而增加\x01",
            "水果的出货量啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们是主张更加有效地\x01",
            "生产美味的水果。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2551")

    label("loc_24EB")


    ChrTalk(
        0xFE,
        (
            "为什么他就是\x01",
            "不能明白我们的意思呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果能得到库赖爷爷的合作，\x01",
            "栽培就能更顺利地进行了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2551")

    TalkEnd(0xF)
    Return()

    # Function_11_2474 end

    def Function_12_2555(): pass

    label("Function_12_2555")

    OP_A2(0x31E)
    OP_28(0x36, 0x1, 0x80)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(5700, 0, 48496, 0)
    OP_67(0, 7080, -10000, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x10)
    SetChrChipByIndex(0xA, 12)
    SetChrSubChip(0xA, 0)
    OP_4A(0xA, 255)
    SetChrPos(0xB, 1450, 0, 41600, 90)
    SetChrPos(0xA, 5990, 200, 46960, 270)
    SetChrPos(0x101, 4561, 200, 48200, 180)
    SetChrPos(0x102, 3391, 200, 48200, 180)
    SetChrPos(0x103, 4561, 200, 45845, 0)
    SetChrChipByIndex(0x101, 8)
    SetChrChipByIndex(0x102, 9)
    SetChrChipByIndex(0x103, 10)
    SetChrSubChip(0x101, 1)
    SetChrSubChip(0x102, 1)
    SetChrSubChip(0x103, 2)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "#2P嗯，是说那个废坑里\x01",
            "可能会有什么线索吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2P……我记得王国军的士兵\x01",
            "的确没有调查过废坑的内部。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F#1P听了鲁伊那个孩子的话，\x01",
            "实在是很在意……\x02\x03",
            "为了以防万一想要调查一下。\x01",
            "能不能把入口的钥匙借给我们呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2P那个挂锁的钥匙吗。\x01",
            "你们在这儿稍等一下……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x103, 2)
    SetChrPos(0xA, 5660, 0, 46450, 180)
    SetChrChipByIndex(0xA, 2)
    SetChrSubChip(0xA, 0)
    OP_0D()

    def lambda_2777():
        OP_6D(4094, 2000, 41516, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2777)
    OP_8E(0xA, 0x1F3A, 0x0, 0xA998, 0xBB8, 0x0)
    ClearChrFlags(0xA, 0x4)
    OP_8E(0xA, 0x1F3A, 0x7D0, 0x9CA2, 0xBB8, 0x0)
    OP_8E(0xA, 0x10CA, 0x7D0, 0x9EDB, 0xBB8, 0x0)
    OP_8C(0xA, 0, 400)

    ChrTalk(
        0xA,
        "记得是放在抽屉里了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "噢，找到了，找到了。\x02",
    )

    CloseMessageWindow()

    def lambda_280D():
        OP_6D(5700, 0, 48496, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_280D)
    OP_8E(0xA, 0x1F3A, 0x7D0, 0x9CA2, 0xBB8, 0x0)
    OP_8E(0xA, 0x1F3A, 0x0, 0xA998, 0xBB8, 0x0)
    OP_8E(0xA, 0x161C, 0x0, 0xB572, 0xBB8, 0x0)
    Fade(1000)
    SetChrSubChip(0x101, 1)
    SetChrSubChip(0x102, 1)
    SetChrSubChip(0x103, 2)
    SetChrFlags(0xA, 0x4)
    SetChrPos(0xA, 5990, 200, 46960, 270)
    SetChrChipByIndex(0xA, 12)
    SetChrSubChip(0xA, 0)
    OP_44(0xA, 0xFF)
    OP_0D()

    ChrTalk(
        0xA,
        "#2P给，这就行了吧？\x02",
    )

    CloseMessageWindow()
    OP_3E(0x32E, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "废坑的钥匙\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        (
            "#004F#1P哇，好粗糙的钥匙……\x02\x03",
            "#001F谢谢您，村长！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#3P真是非常感谢您。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2P哪里哪里，\x01",
            "我们总是受到游击士协会的关照。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#2P现在帮点忙也是应该的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#021F呵呵……\x01",
            "我们也经常受到\x01",
            "像村长这样的好人相助呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#3P如果发现了什么，\x01",
            "我们一定会来向您报告的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#2P嗯，那么就拜托你们了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0xA, 0xFF)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    OP_6D(720, 0, 45250, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x103, 0)
    SetChrPos(0x101, 720, 0, 45250, 180)
    SetChrPos(0x102, 720, 0, 45250, 180)
    SetChrPos(0x103, 720, 0, 45250, 180)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0x102, 65535)
    OP_69(0x101, 0x0)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x10)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_12_2555 end

    SaveToFile()

Try(main)
