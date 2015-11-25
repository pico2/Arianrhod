from ED6ScenarioHelper import *

def main():
    # 格鲁纳门

    CreateScenaFile(
        FileName            = 'T0610   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0610.x',
        MapIndex            = 17,
        MapDefaultBGM       = "ed60016",
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
        '罗宾队长',                             # 9
        '古利乌副长',                           # 10
        '士兵安顿',                             # 11
        '萨姆',                                 # 12
        '亚米丽',                               # 13
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
        Unknown_3A              = 17,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT07/CH01310 ._CH',             # 01
        'ED6_DT07/CH01300 ._CH',             # 02
        'ED6_DT07/CH01020 ._CH',             # 03
        'ED6_DT07/CH01150 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01310P._CP',             # 01
        'ED6_DT07/CH01300P._CP',             # 02
        'ED6_DT07/CH01020P._CP',             # 03
        'ED6_DT07/CH01150P._CP',             # 04
    )

    DeclNpc(
        X                   = -19380,
        Z                   = 0,
        Y                   = -980,
        Direction           = 98,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -111940,
        Z                   = 0,
        Y                   = 21850,
        Direction           = 87,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -7220,
        Z                   = 0,
        Y                   = 2820,
        Direction           = 162,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -90130,
        Z                   = 0,
        Y                   = -22320,
        Direction           = 253,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -57740,
        Z                   = 0,
        Y                   = -21510,
        Direction           = 352,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )


    DeclActor(
        TriggerX            = -7430,
        TriggerZ            = 0,
        TriggerY            = 900,
        TriggerRange        = 1000,
        ActorX              = -7220,
        ActorZ              = 1500,
        ActorY              = 2820,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -109840,
        TriggerZ            = 0,
        TriggerY            = 21450,
        TriggerRange        = 1000,
        ActorX              = -111940,
        ActorZ              = 1500,
        ActorY              = 21850,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -92220,
        TriggerZ            = 0,
        TriggerY            = -22040,
        TriggerRange        = 1000,
        ActorX              = -90130,
        ActorZ              = 1500,
        ActorY              = -22320,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1DE",          # 00, 0
        "Function_1_218",          # 01, 1
        "Function_2_232",          # 02, 2
        "Function_3_248",          # 03, 3
        "Function_4_26C",          # 04, 4
        "Function_5_271",          # 05, 5
        "Function_6_80E",          # 06, 6
        "Function_7_FBB",          # 07, 7
        "Function_8_FC0",          # 08, 8
        "Function_9_178B",         # 09, 9
        "Function_10_1790",        # 0A, 10
        "Function_11_1E8D",        # 0B, 11
        "Function_12_2612",        # 0C, 12
        "Function_13_2767",        # 0D, 13
        "Function_14_2985",        # 0E, 14
    )


    def Function_0_1DE(): pass

    label("Function_0_1DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1E8")
    Jump("loc_217")

    label("loc_1E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1F2")
    Jump("loc_217")

    label("loc_1F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1FC")
    Jump("loc_217")

    label("loc_1FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_206")
    Jump("loc_217")

    label("loc_206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_210")
    Jump("loc_217")

    label("loc_210")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_217")

    label("loc_217")

    Return()

    # Function_0_1DE end

    def Function_1_218(): pass

    label("Function_1_218")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_227")
    OP_1B(0x0, 0x0, 0xC)
    Jump("loc_22C")

    label("loc_227")

    OP_1B(0x1, 0x0, 0xD)

    label("loc_22C")

    OP_1C(0x5, 0x0, 0xE)
    Return()

    # Function_1_218 end

    def Function_2_232(): pass

    label("Function_2_232")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_247")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_232")

    label("loc_247")

    Return()

    # Function_2_232 end

    def Function_3_248(): pass

    label("Function_3_248")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_26B")
    OP_8D(0xFE, -22660, -4810, -14730, 1940, 3000)
    Jump("Function_3_248")

    label("loc_26B")

    Return()

    # Function_3_248 end

    def Function_4_26C(): pass

    label("Function_4_26C")

    Call(0, 5)
    Return()

    # Function_4_26C end

    def Function_5_271(): pass

    label("Function_5_271")

    TalkBegin(0xB)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",      # 0
            "休息\x01",      # 1
            "离开\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DC")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_2D1")
    OP_A9(0x66)
    Jump("loc_2D3")

    label("loc_2D1")

    OP_A9(0x64)

    label("loc_2D3")

    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_2DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2ED")
    TalkEnd(0xB)
    Return()

    label("loc_2ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_33E")

    ChrTalk(
        0xB,
        (
            "军队里的士兵\x01",
            "都以一种很可怕的脸色在谈话呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "发生什么事了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_80A")

    label("loc_33E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_39A")

    ChrTalk(
        0xB,
        "武术大会今天结束了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "诞辰庆典快要举行了，\x01",
            "各地的旅客又会\x01",
            "开始多起来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80A")

    label("loc_39A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_40F")

    ChrTalk(
        0xB,
        (
            "军队的士兵好像都很忙，\x01",
            "只有我好空，这也是没办法的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "这里什么娱乐活动都没有，\x01",
            "怎么回事啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A1")

    label("loc_40F")

    OP_A2(0x4)

    ChrTalk(
        0xB,
        "呼啊～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "军队的士兵好像都很忙，\x01",
            "只有我好空，这也是没办法的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "大扫除已经\x01",
            "完成了大部分了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "没有客人，也没有娱乐。\x01",
            "怎么回事啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A1")

    Jump("loc_80A")

    label("loc_4A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_51D")

    ChrTalk(
        0xB,
        (
            "武术大会的决赛一开始，\x01",
            "客人就明显减少。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "今天我想关门大吉，\x01",
            "然后跑去王都那里观战，\x01",
            "不过我不能这么做。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80A")

    label("loc_51D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_579")

    ChrTalk(
        0xB,
        (
            "说起来\x01",
            "没想到那支亲卫队竟然是恐怖集团。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "王都那里肯定\x01",
            "引起很大的骚动吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80A")

    label("loc_579")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_5D3")

    ChrTalk(
        0xB,
        (
            "不久之前来的客人\x01",
            "都准备去格兰赛尔呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "那么，趁今天有空\x01",
            "开始大扫除吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80A")

    label("loc_5D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_633")

    ChrTalk(
        0xB,
        (
            "突然觉得通过关所的人\x01",
            "增加了不少。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "距诞辰庆典还有段日子，\x01",
            "发生什么事情了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80A")

    label("loc_633")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_67A")

    ChrTalk(
        0xB,
        "哟，终于来了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "最近客人特别少，\x01",
            "我觉得好无聊啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80A")

    label("loc_67A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_6D3")

    ChrTalk(
        0xB,
        "今天的客人真少啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "就是这种时候，\x01",
            "才能搞搞平时无法完成的大扫除啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80A")

    label("loc_6D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_71C")

    ChrTalk(
        0xB,
        "您好，欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "要住宿的话，\x01",
            "过来跟我说一声就行了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80A")

    label("loc_71C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_78F")

    ChrTalk(
        0xB,
        (
            "那么，趁今天这个好天气，\x01",
            "把被单收集起来洗一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "机会这么难得， \x01",
            "我也想让客人睡得舒服一点啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80A")

    label("loc_78F")


    ChrTalk(
        0xB,
        (
            "您好，欢迎光临。\x01",
            "这里是谁都可以使用的\x01",
            "旅行者专用旅馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "隔壁还有一个食堂。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "觉得不错的话，\x01",
            "就在这里住一晚吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80A")

    TalkEnd(0xB)
    Return()

    # Function_5_271 end

    def Function_6_80E(): pass

    label("Function_6_80E")

    TalkBegin(0xC)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86F")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x65)
    OP_56(0x0)
    TalkEnd(0xC)
    Return()

    label("loc_86F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_889")
    FadeToBright(300, 0)
    TalkEnd(0xC)
    Return()

    label("loc_889")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_8F1")

    ChrTalk(
        0xC,
        (
            "士兵们都\x01",
            "慌慌张张的，\x01",
            "局势果然很紧张啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "希望能够平安\x01",
            "迎来诞辰庆典就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FB7")

    label("loc_8F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_9F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_968")

    ChrTalk(
        0xC,
        (
            "虽然我想挑战制作新的菜式，\x01",
            "但是又失败了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "唔～顺利的话，我觉得可以\x01",
            "往菜单里添加新的菜式了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F4")

    label("loc_968")

    OP_A2(0x5)

    ChrTalk(
        0xC,
        (
            "虽然我想挑战制作新的菜式，\x01",
            "但是又失败了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "唔～顺利的话，我觉得可以\x01",
            "往菜单里添加新的菜式了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "趁着还有时间，\x01",
            "多尝试一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F4")

    Jump("loc_FB7")

    label("loc_9F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_AD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_A5C")

    ChrTalk(
        0xC,
        (
            "今天都没有什么客人，\x01",
            "好寂寞啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "但是，可以有机会\x01",
            "一个人享受品茶时光呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD4")

    label("loc_A5C")

    OP_A2(0x5)

    ChrTalk(
        0xC,
        (
            "今天都没有什么客人，\x01",
            "好寂寞啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "但是，可以有机会\x01",
            "一个人享受品茶时光呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "今天来挑战一下\x01",
            "新的菜式吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AD4")

    Jump("loc_FB7")

    label("loc_AD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_B29")

    ChrTalk(
        0xC,
        (
            "有时间的话，\x01",
            "来烧制一些小点心吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "给繁忙的士兵们\x01",
            "送点补品吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FB7")

    label("loc_B29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_C1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_B98")

    ChrTalk(
        0xC,
        (
            "亲卫队的尤莉亚中尉，\x01",
            "身为女性的我也非常仰慕她。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "又帅气，又有礼貌，\x01",
            "而且实力非常强。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C1A")

    label("loc_B98")

    OP_A2(0x5)

    ChrTalk(
        0xC,
        (
            "亲卫队的尤莉亚中尉，\x01",
            "身为女性的我也非常仰慕她。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "又帅气，又有礼貌，\x01",
            "而且实力非常强。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "听说她是\x01",
            "向老师学习剑术的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C1A")

    Jump("loc_FB7")

    label("loc_C1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_CEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_C82")

    ChrTalk(
        0xC,
        (
            "几位客人是从\x01",
            "王都那里过来的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "这种时候从格兰赛尔那边\x01",
            "过来还真是少见呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE9")

    label("loc_C82")

    OP_A2(0x5)

    ChrTalk(
        0xC,
        "欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "几位客人是从\x01",
            "王都那里过来的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "这种时候从格兰赛尔那边\x01",
            "过来还真是少见呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CE9")

    Jump("loc_FB7")

    label("loc_CEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_D8F")

    ChrTalk(
        0xFE,
        (
            "最近，除了利贝尔\x01",
            "和帝国的料理之外， \x01",
            "东方的料理也广受关注呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "下次去王都的时候，\x01",
            "也应该买本什么书回来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "会有怎样的料理，\x01",
            "我好有兴趣啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FB7")

    label("loc_D8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_E18")

    ChrTalk(
        0xFE,
        (
            "这里的士兵们都非常善良，\x01",
            "即使味道不太好，\x01",
            "他们也都会说很好吃。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "某种意义上来说我很高兴，\x01",
            "但是我也想听听直率的意见……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FB7")

    label("loc_E18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_E81")

    ChrTalk(
        0xFE,
        (
            "呼，这个时候\x01",
            "有点无聊啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "正是这种时候，\x01",
            "才应该有效地利用它，\x01",
            "好好地配置一下菜单吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FB7")

    label("loc_E81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_EAF")

    ChrTalk(
        0xFE,
        "欢迎光临，请问你们想吃点什么？\x02",
    )

    CloseMessageWindow()
    Jump("loc_FB7")

    label("loc_EAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_F72")

    ChrTalk(
        0xFE,
        (
            "煎锅这东西越使用\x01",
            "越觉得是一件上乘之品。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "随着烧菜时间的增长，\x01",
            "而产生的黑色光泽，\x01",
            "让我觉得无比愉快。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对于厨师来说，这就好像是\x01",
            "刻入自己年轮的东西，\x01",
            "换句话说，就和勋章一样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FB7")

    label("loc_F72")


    ChrTalk(
        0xFE,
        (
            "欢迎光临。\x01",
            "欢迎来到格鲁纳门的食堂。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "喜欢吃什么请随便点吧。\x02",
    )

    CloseMessageWindow()

    label("loc_FB7")

    TalkEnd(0xC)
    Return()

    # Function_6_80E end

    def Function_7_FBB(): pass

    label("Function_7_FBB")

    Call(0, 8)
    Return()

    # Function_7_FBB end

    def Function_8_FC0(): pass

    label("Function_8_FC0")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1034")

    ChrTalk(
        0xA,
        (
            "现在所有的关所\x01",
            "都完全禁止通行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "真抱歉，这也是为了\x01",
            "防止正在潜逃的恐怖分子们\x01",
            "有不轨的行动啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1787")

    label("loc_1034")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1129")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_10A8")

    ChrTalk(
        0xA,
        (
            "情报部的士兵们\x01",
            "和亲卫队不同，\x01",
            "态度是非常威严傲慢的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "唉，真不知道\x01",
            "到底哪边才是恐怖分子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1126")

    label("loc_10A8")

    OP_A2(0x3)

    ChrTalk(
        0xA,
        (
            "情报部的士兵们\x01",
            "好像巡逻回来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "和亲卫队不同，\x01",
            "态度是非常威严傲慢的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "唉，真不知道\x01",
            "到底哪边才是恐怖分子。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1126")

    Jump("loc_1787")

    label("loc_1129")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_11C0")

    ChrTalk(
        0xA,
        (
            "从今天开始， \x01",
            "如果通行者没有可以证明\x01",
            "自己身份的东西，就无法通过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "对不起，如果要通过的话，\x01",
            "请出示能够证明身份的书信\x01",
            "或者其他物品。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1787")

    label("loc_11C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1252")

    ChrTalk(
        0xA,
        (
            "我想你们一眼就能看出来了，\x01",
            "这座门是利用亚宁堡的一部分\x01",
            "制作而成的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "虽然能感受到历史的氛围\x01",
            "和它的万种风情，\x01",
            "但也带了许多不便。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1787")

    label("loc_1252")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_12D0")

    ChrTalk(
        0xA,
        (
            "这座门的通行者没有对面的\x01",
            "圣海姆门的人多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "只有像举办武术大会或者诞辰庆典\x01",
            "这样的活动时通行的人才会多起来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1787")

    label("loc_12D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_1326")

    ChrTalk(
        0xA,
        (
            "咦……\x01",
            "你们是旅行者吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "武术大会的时候基本没有\x01",
            "什么人来洛连特的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1787")

    label("loc_1326")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_13B7")

    ChrTalk(
        0xA,
        (
            "定期船停航的话，\x01",
            "从这里通过的人多了不少。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "因为急事要去王都的人，\x01",
            "只能从这个关所通过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "好像又回到没有\x01",
            "飞艇的时代了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1787")

    label("loc_13B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_1428")

    ChrTalk(
        0xA,
        (
            "神秘森林就在\x01",
            "比这边还要北一点的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "从街道向东走，\x01",
            "会有一条小道，\x01",
            "走的时候可不要错过了呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1787")

    label("loc_1428")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1488")

    ChrTalk(
        0xA,
        (
            "北方的神秘森林\x01",
            "是洛连特林业的中心地带。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "那里的工作人员\x01",
            "有时候会来这里休息。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1787")

    label("loc_1488")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1585")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1528")
    OP_A2(0x3)

    ChrTalk(
        0xA,
        (
            "听说游击士可以自己\x01",
            "选择所属的支部？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "真好啊，我们士兵\x01",
            "可没有选择工作地点的权利。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "不过，如果可以这样的话，\x01",
            "或许会变得很糟糕。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1582")

    label("loc_1528")


    ChrTalk(
        0xA,
        (
            "听说游击士可以自己\x01",
            "选择所属的支部？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "真好啊，我们士兵\x01",
            "可没有选择工作地点的权利。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1582")

    Jump("loc_1787")

    label("loc_1585")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_1639")

    ChrTalk(
        0xA,
        (
            "王国的各个地方边境\x01",
            "肯定会有像这样的关所。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "百日战役以来，\x01",
            "检查要出入各个地区的人\x01",
            "也是为了地区的安全和稳定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "就是和在飞艇坪买票的时候\x01",
            "需要身份证明是一样的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1787")

    label("loc_1639")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1714")
    OP_A2(0x3)

    ChrTalk(
        0xA,
        (
            "啊呀，难道你们\x01",
            "要去格兰赛尔？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，不是的。\x01",
            "我们并没有这个打算……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "是这样啊。\x01",
            "最近来往于洛连特和王都\x01",
            "之间的定期船已经成为主流。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "像以前一样步行前来\x01",
            "通过关所的旅行者\x01",
            "已经很少很少了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1787")

    label("loc_1714")


    ChrTalk(
        0xA,
        (
            "最近来往于洛连特和王都\x01",
            "之间的定期船已经成为主流。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "像以前一样步行前来\x01",
            "通过关所的旅行者\x01",
            "已经少了很多了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1787")

    TalkEnd(0xA)
    Return()

    # Function_8_FC0 end

    def Function_9_178B(): pass

    label("Function_9_178B")

    Call(0, 10)
    Return()

    # Function_9_178B end

    def Function_10_1790(): pass

    label("Function_10_1790")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_180D")

    ChrTalk(
        0x9,
        (
            "昨天， \x01",
            "本部传来通告， \x01",
            "要求完全封锁关所。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "真是非常抱歉，\x01",
            "除军队相关人员之外，\x01",
            "连一只猫都不能放进去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E89")

    label("loc_180D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_185A")

    ChrTalk(
        0x9,
        "今天武术大会就结束了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我想王城那边\x01",
            "也该有新的行动了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E89")

    label("loc_185A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_18C4")

    ChrTalk(
        0x9,
        (
            "今天开始，警戒体制的等级\x01",
            "向上提升一级了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "要将通行者的身份完全\x01",
            "确认之后，才能放行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E89")

    label("loc_18C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_19DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_193F")

    ChrTalk(
        0x9,
        (
            "利贝尔王国的交通\x01",
            "现在是以定期船为主要工具。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "航空被封锁之后，\x01",
            "旅客和货物的通行就变得非常困难了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19DB")

    label("loc_193F")

    OP_A2(0x2)

    ChrTalk(
        0x9,
        (
            "王国军的管制\x01",
            "给人们带来了许多不便。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "利贝尔王国的交通\x01",
            "现在是以定期船为主要工具。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "果然，航空被封锁之后，\x01",
            "旅客和货物的通行就变得非常困难了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19DB")

    Jump("loc_1E89")

    label("loc_19DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1A59")

    ChrTalk(
        0x9,
        (
            "我在演习的时候\x01",
            "见过亲卫队的成员，\x01",
            "他们作为守护陛下的人真的很称职。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "没想到竟然是他们\x01",
            "引起的恐怖事件……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E89")

    label("loc_1A59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_1B24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1AB3")

    ChrTalk(
        0x9,
        (
            "我记得圣海姆门那里\x01",
            "好像刚刚征召了一些新兵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "那边一定很辛苦吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B21")

    label("loc_1AB3")

    OP_A2(0x2)

    ChrTalk(
        0x9,
        (
            "因为现在处于警戒状态，\x01",
            "全队的演习全部中止了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "这座格鲁纳门\x01",
            "聚集了许多老兵，\x01",
            "没有什么可以担心的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B21")

    Jump("loc_1E89")

    label("loc_1B24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_1BE9")

    ChrTalk(
        0x9,
        (
            "柏斯那边的定期船\x01",
            "好像消失了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我好担心飞艇上的乘客，\x01",
            "希望他们平安无事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "不过，在柏斯地区\x01",
            "也有一支聚集了王国军中\x01",
            "很多精英的国境守备队。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我想他们一定能够\x01",
            "把飞艇找出来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E89")

    label("loc_1BE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_1C8B")

    ChrTalk(
        0x9,
        (
            "那么……\x01",
            "今天一天也要加油。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "只有在和平的时候才应该\x01",
            "随时待命，以备不时之需。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "这句话是队长说的，\x01",
            "虽然我是现学现卖，\x01",
            "不过觉得这话说得真好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E89")

    label("loc_1C8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1CF5")

    ChrTalk(
        0x9,
        (
            "百日战役结束以来，\x01",
            "今年是第１０个年头了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "看着现在和平的王国，\x01",
            "就想到很久以前的光景。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E89")

    label("loc_1CF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1D9A")

    ChrTalk(
        0x9,
        (
            "洛连特市长\x01",
            "来过这里实地视察，\x01",
            "他真是个好人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "市长让人感觉很亲切，\x01",
            "就像是隔壁家的老爷爷。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "他对待市民也\x01",
            "非常和蔼可亲，\x01",
            "那样的话一定很得民心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E89")

    label("loc_1D9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_1E1F")

    ChrTalk(
        0x9,
        (
            "最近，在王都\x01",
            "聚集了许多喜爱钓鱼的人，\x01",
            "好像已经形成了组织。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我也非常喜欢钓鱼，\x01",
            "所以对那是个怎样的组织非常有兴趣。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E89")

    label("loc_1E1F")


    ChrTalk(
        0x9,
        (
            "哟，你们好。\x01",
            "是来观光，还是来做其他事情的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "这里的设施任何人都可以使用，\x01",
            "你们可以好好休息一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E89")

    TalkEnd(0x9)
    Return()

    # Function_10_1790 end

    def Function_11_1E8D(): pass

    label("Function_11_1E8D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1F17")

    ChrTalk(
        0xFE,
        (
            "终于，各关所被完全封锁，\x01",
            "定期船也全都停止航行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就算是理查德上校，\x01",
            "没有女王陛下的许可\x01",
            "就这样做，到底行不行啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_260E")

    label("loc_1F17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1F94")

    ChrTalk(
        0xFE,
        (
            "传闻中，自称是游击士的\x01",
            "恐怖分子相当厉害。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一对一恐怕无法取胜，\x01",
            "所以要考虑一下\x01",
            "把现在警备体制联合起来……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_260E")

    label("loc_1F94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_20C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_201D")

    ChrTalk(
        0xFE,
        (
            "听说在蔡斯出现的\x01",
            "恐怖分子们穿着\x01",
            "亲卫队的制服。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "即使假设犯人是亲卫队，\x01",
            "他们为什么要在犯案时\x01",
            "特地穿着制服呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20BF")

    label("loc_201D")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "听说在蔡斯出现的\x01",
            "恐怖分子们穿着\x01",
            "亲卫队的制服。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "亲卫队集中了王国军中\x01",
            "最优秀的人才。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "即使假设他们是犯人，\x01",
            "他们为什么要在犯案时\x01",
            "特地穿着制服呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20BF")

    Jump("loc_260E")

    label("loc_20C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_21E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2131")

    ChrTalk(
        0xFE,
        (
            "现在洛连特地区\x01",
            "也没有发生什么重大事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，为了以防万一，\x01",
            "应该随时处于出动状态。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21E0")

    label("loc_2131")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "游击士协会的洛连特支部中\x01",
            "好像有一位非常能干的女性游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了以防万一，\x01",
            "现在洛连特地区\x01",
            "也没有发生什么重大事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，为了以防万一，\x01",
            "应该随时处于出动状态。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21E0")

    Jump("loc_260E")

    label("loc_21E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2282")

    ChrTalk(
        0xFE,
        (
            "有报告说是这次的恐怖事件\x01",
            "是亲卫队干的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "也听说是恐怖分子装扮成\x01",
            "亲卫队和游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "到底哪个是真的呢。\x01",
            "真希望能够尽早得到正确的情报啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_260E")

    label("loc_2282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_22F5")

    ChrTalk(
        0xFE,
        (
            "军队在全国\x01",
            "都采取这样的警备状态\x01",
            "还是百日战役以来的第一次啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……我想起了\x01",
            "那个时候的许多事情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_260E")

    label("loc_22F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_2389")

    ChrTalk(
        0xFE,
        (
            "神秘森林上空\x01",
            "有奇怪的飞艇飞来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "调查的结果也显示， \x01",
            "过去曾有好几次起飞降落的形迹。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要赶快向雷斯顿要塞总部\x01",
            "报告这件事情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_260E")

    label("loc_2389")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_242D")

    ChrTalk(
        0xFE,
        (
            "洛连特原本\x01",
            "是不太会发生什么大事的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，即使这么说，\x01",
            "我们也不能保证\x01",
            "今后不会发生什么大事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不管地区的守备多么坚固，\x01",
            "也不能放松警惕。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_260E")

    label("loc_242D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_24C0")

    ChrTalk(
        0xFE,
        (
            "今天也没有\x01",
            "发生什么大事件呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然和平是件好事，\x01",
            "但正是这样才应该防患于未然，\x01",
            "要认真进行演习才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "因为这是我们的工作啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_260E")

    label("loc_24C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_2553")

    ChrTalk(
        0xFE,
        (
            "正因为这个\x01",
            "关所通向王都，\x01",
            "所以都分配了经验丰富的老兵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "威尔特桥的关所却相反，\x01",
            "分配的全都是新兵……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "阿斯顿队长没问题吧……\x02",
    )

    CloseMessageWindow()
    Jump("loc_260E")

    label("loc_2553")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_25BC")

    ChrTalk(
        0xFE,
        (
            "在王都，为女王陛下的诞辰庆典\x01",
            "所做的准备正在有条不紊地进行中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我从现在开始就很期待。\x02",
    )

    CloseMessageWindow()
    Jump("loc_260E")

    label("loc_25BC")


    ChrTalk(
        0xFE,
        (
            "哟，你们是游击士吗。\x01",
            "你们也辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果发生什么事件，\x01",
            "我们互相帮助吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_260E")

    TalkEnd(0xFE)
    Return()

    # Function_11_1E8D end

    def Function_12_2612(): pass

    label("Function_12_2612")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2766")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_268C")
    TurnDirection(0x102, 0x101, 400)

    def lambda_263D():
        TurnDirection(0x101, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_263D)

    ChrTalk(
        0x102,
        (
            "#010F这边是洛连特吧。\x02\x03",
            "要回去的话…………\x01",
            "现在这个时候还不行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_274B")

    label("loc_268C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26F8")

    ChrTalk(
        0x104,
        (
            "#030F哦，\x01",
            "这边不就是令人怀念的洛连特吗。\x02\x03",
            "虽然我还想再去拜访一下，\x01",
            "不过现在还不是时候。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_274B")

    label("loc_26F8")


    ChrTalk(
        0x108,
        (
            "#070F哦，\x01",
            "这边是通往其他地区的出口。\x02\x03",
            "被士兵缠上就麻烦了。\x01",
            "还是乖乖地回去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_274B")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_2766")

    Return()

    # Function_12_2612 end

    def Function_13_2767(): pass

    label("Function_13_2767")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2984")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2857")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27F3")
    OP_A2(0x0)
    TurnDirection(0x102, 0x101, 400)

    def lambda_279E():
        TurnDirection(0x101, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_279E)

    ChrTalk(
        0x102,
        (
            "#010F这边是格兰赛尔地区呢。\x02\x03",
            "我们没有通行许可证，\x01",
            "是不能通过这里的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2854")

    label("loc_27F3")

    TurnDirection(0x102, 0x101, 400)

    def lambda_2800():
        TurnDirection(0x101, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2800)

    ChrTalk(
        0x102,
        (
            "#010F前面就是格兰赛尔地区了。\x02\x03",
            "我们没有通行许可证，\x01",
            "是不能通过这里的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2854")

    Jump("loc_2969")

    label("loc_2857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28DD")
    TurnDirection(0x103, 0x101, 400)

    def lambda_286C():
        TurnDirection(0x102, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_286C)

    def lambda_287A():
        TurnDirection(0x101, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_287A)

    ChrTalk(
        0x103,
        (
            "#020F前面就是格兰赛尔地区了。\x01",
            "要通过关所就需要许可证。\x02\x03",
            "不过，现在也没有去的必要。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2969")

    label("loc_28DD")

    TurnDirection(0x103, 0x101, 400)

    def lambda_28EA():
        TurnDirection(0x102, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_28EA)

    def lambda_28F8():
        TurnDirection(0x101, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_28F8)

    ChrTalk(
        0x103,
        (
            "#020F前面就是格兰赛尔地区了。\x01",
            "要通过关所就需要许可证。\x02\x03",
            "我们要去的威尔特桥也和这里一样，\x01",
            "要注意啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2969")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_2984")

    Return()

    # Function_13_2767 end

    def Function_14_2985(): pass

    label("Function_14_2985")

    TalkBegin(0xFF)
    Sleep(400)
    TalkEnd(0xFF)
    Return()

    # Function_14_2985 end

    SaveToFile()

Try(main)
