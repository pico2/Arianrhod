from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4132   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4132.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        '奈尔',                                 # 9
        '克鲁茨',                               # 10
        '福立兹',                               # 11
        '乔儿',                                 # 12
        '汉斯',                                 # 13
        '科洛丝',                               # 14
        '米亚尔',                               # 15
        '科林兹校长',                           # 16
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
        'ED6_DT07/CH02060 ._CH',             # 00
        'ED6_DT07/CH01620 ._CH',             # 01
        'ED6_DT07/CH00175 ._CH',             # 02
        'ED6_DT07/CH00176 ._CH',             # 03
        'ED6_DT06/CH20041 ._CH',             # 04
        'ED6_DT06/CH20047 ._CH',             # 05
        'ED6_DT07/CH01220 ._CH',             # 06
        'ED6_DT07/CH02390 ._CH',             # 07
        'ED6_DT07/CH02550 ._CH',             # 08
        'ED6_DT07/CH00040 ._CH',             # 09
        'ED6_DT07/CH01040 ._CH',             # 0A
        'ED6_DT07/CH02600 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT07/CH02060P._CP',             # 00
        'ED6_DT07/CH01620P._CP',             # 01
        'ED6_DT07/CH00175P._CP',             # 02
        'ED6_DT07/CH00176P._CP',             # 03
        'ED6_DT06/CH20041P._CP',             # 04
        'ED6_DT06/CH20047P._CP',             # 05
        'ED6_DT07/CH01220P._CP',             # 06
        'ED6_DT07/CH02390P._CP',             # 07
        'ED6_DT07/CH02550P._CP',             # 08
        'ED6_DT07/CH00040P._CP',             # 09
        'ED6_DT07/CH01040P._CP',             # 0A
        'ED6_DT07/CH02600P._CP',             # 0B
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 6940,
        Z                   = 0,
        Y                   = 3300,
        Direction           = 166,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 6140,
        Z                   = 0,
        Y                   = -1760,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 7770,
        Z                   = 0,
        Y                   = -1720,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 6920,
        Z                   = 0,
        Y                   = -260,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 36400,
        Z                   = 0,
        Y                   = 50700,
        Direction           = 106,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 4320,
        Z                   = 0,
        Y                   = 1060,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )


    DeclActor(
        TriggerX            = 7060,
        TriggerZ            = 0,
        TriggerY            = 1700,
        TriggerRange        = 800,
        ActorX              = 6940,
        ActorZ              = 1500,
        ActorY              = 3300,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7000,
        TriggerZ            = 0,
        TriggerY            = 4890,
        TriggerRange        = 800,
        ActorX              = 7000,
        ActorZ              = 1000,
        ActorY              = 4890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_252",          # 00, 0
        "Function_1_3A0",          # 01, 1
        "Function_2_3ED",          # 02, 2
        "Function_3_403",          # 03, 3
        "Function_4_427",          # 04, 4
        "Function_5_493",          # 05, 5
        "Function_6_727",          # 06, 6
        "Function_7_93B",          # 07, 7
        "Function_8_A5A",          # 08, 8
        "Function_9_AB8",          # 09, 9
        "Function_10_ABD",         # 0A, 10
        "Function_11_1420",        # 0B, 11
        "Function_12_16B2",        # 0C, 12
        "Function_13_1D12",        # 0D, 13
        "Function_14_222B",        # 0E, 14
        "Function_15_2585",        # 0F, 15
        "Function_16_2918",        # 10, 16
        "Function_17_3B57",        # 11, 17
    )


    def Function_0_252(): pass

    label("Function_0_252")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_269")
    OP_A3(0x3FA)
    Event(0, 12)
    OP_B1("t4132_n")

    label("loc_269")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_280")
    OP_A3(0x3FB)
    Event(0, 14)
    OP_B1("t4132_n")

    label("loc_280")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_2A0")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FC)
    Event(0, 15)
    OP_B1("t4132_n")

    label("loc_2A0")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_2B0"),
        (120, "loc_2CB"),
        (SWITCH_DEFAULT, "loc_2E1"),
    )


    label("loc_2B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C8")
    SetMapFlags(0x10000000)
    OP_A2(0x620)
    Event(0, 13)

    label("loc_2C8")

    Jump("loc_2E1")

    label("loc_2CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DE")
    OP_A2(0x64D)
    Event(0, 16)

    label("loc_2DE")

    Jump("loc_2E1")

    label("loc_2E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2FF")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_39F")

    label("loc_2FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_30E")
    ClearChrFlags(0xE, 0x80)
    Jump("loc_39F")

    label("loc_30E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_318")
    Jump("loc_39F")

    label("loc_318")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_322")
    Jump("loc_39F")

    label("loc_322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_32C")
    Jump("loc_39F")

    label("loc_32C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_353")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 32009, 0, 115490, 0)
    OP_43(0x9, 0x0, 0x0, 0x2)
    Jump("loc_39F")

    label("loc_353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_35D")
    Jump("loc_39F")

    label("loc_35D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_384")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 32009, 0, 115490, 0)
    OP_43(0x9, 0x0, 0x0, 0x2)
    Jump("loc_39F")

    label("loc_384")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_38E")
    Jump("loc_39F")

    label("loc_38E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_398")
    Jump("loc_39F")

    label("loc_398")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_39F")

    label("loc_39F")

    Return()

    # Function_0_252 end

    def Function_1_3A0(): pass

    label("Function_1_3A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D3")
    OP_B1("t4132_y")
    Jump("loc_3DC")

    label("loc_3D3")

    OP_B1("t4132_n")

    label("loc_3DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_3EC")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3EC")

    Return()

    # Function_1_3A0 end

    def Function_2_3ED(): pass

    label("Function_2_3ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_402")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3ED")

    label("loc_402")

    Return()

    # Function_2_3ED end

    def Function_3_403(): pass

    label("Function_3_403")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_426")
    OP_8D(0xFE, 153520, 48510, 156020, 53700, 3000)
    Jump("Function_3_403")

    label("loc_426")

    Return()

    # Function_3_403 end

    def Function_4_427(): pass

    label("Function_4_427")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "诞辰庆典之前的这几天\x01",
            "就在这个酒店里\x01",
            "舒舒服服地度过吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不愧是王国最大的酒店。\x01",
            "真是豪华啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_427 end

    def Function_5_493(): pass

    label("Function_5_493")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4E2")

    ChrTalk(
        0xD,
        (
            "#040F艾丝蒂尔、约修亚。\x02\x03",
            "能够遇到你们两个，\x01",
            "我真是太幸福了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_723")

    label("loc_4E2")

    OP_A2(0x4)
    OP_A2(0x6F2)

    ChrTalk(
        0xD,
        "#040F艾丝蒂尔、约修亚。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F科洛丝，原来你在这里啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#045F嗯，是啊。\x01",
            "我听说校长、乔儿和汉斯他们都来这里了……\x01",
            "　\x02\x03",
            "所以就从王城里面偷偷跑了出来。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F啊哈哈，真看不出来，\x01",
            "科洛丝你也会做出这么大胆的行动呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#041F呵呵，这次真是多谢你们了。\x01",
            "　\x02\x03",
            "我从头到尾一直都承蒙你们两位的关照。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F嗯～我觉得倒是\x01",
            "科洛丝你教会了我许多东西。\x02\x03",
            "待人温柔，意志坚强……\x01",
            "　\x02\x03",
            "#008F对不起，我不太会说话，\x01",
            "所以说不出什么好的……\x02\x03",
            "#006F总之，我们以后继续像现在这样\x01",
            "互相帮助，一起努力就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#044F艾丝蒂尔……\x02\x03",
            "#048F能够遇到你们两个，\x01",
            "我真是太幸福了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_723")

    TalkEnd(0xFE)
    Return()

    # Function_5_493 end

    def Function_6_727(): pass

    label("Function_6_727")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_7A7")

    ChrTalk(
        0xFE,
        (
            "#730F虽然发生了许多的事情，\x01",
            "不过看到你们俩这么有精神，我就放心了。\x02\x03",
            "如果再到卢安来的话，\x01",
            "记得到学院来玩玩哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_937")

    label("loc_7A7")

    OP_A2(0x3)
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        "#730F哟，约修亚。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F这不是汉斯吗。\x02\x03",
            "为什么会在这里呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#734F喂喂……\x01",
            "这么久没见面了，\x01",
            "你却说出这样绝情的话来。\x02\x03",
            "#730F自从学园祭之后，\x01",
            "又回到独自过夜的生活真是寂寞啊……\x02\x03",
            "#731F因为对你难以忘怀，\x01",
            "所以千里迢迢追到王都来了哦。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F哈哈，你还是老样子。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#730F嗯，虽然发生了许多的事情，\x01",
            "不过看到你这么有精神，我就放心了。\x02\x03",
            "如果再到卢安来的话，\x01",
            "记得到学院来玩玩哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_937")

    TalkEnd(0xFE)
    Return()

    # Function_6_727 end

    def Function_7_93B(): pass

    label("Function_7_93B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_9A1")

    ChrTalk(
        0xFE,
        (
            "#640F我从科洛丝那里听说了，\x01",
            "你们这次真是大显神威啊。\x02\x03",
            "#648F不愧是红骑士尤利乌斯哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A56")

    label("loc_9A1")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "#640F艾丝蒂尔、约修亚！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊，乔儿！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#641F好久不见了啦～\x02\x03",
            "我从科洛丝那里听说了，\x01",
            "你们这次真是大显神威啊。\x02\x03",
            "#648F不愧是红骑士尤利乌斯哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F哈哈哈……\x02",
    )

    CloseMessageWindow()

    label("loc_A56")

    TalkEnd(0xFE)
    Return()

    # Function_7_93B end

    def Function_8_A5A(): pass

    label("Function_8_A5A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "#780F呵呵，好久不见了。\x02\x03",
            "我和学院的学生代表乔儿还有汉斯一起\x01",
            "来参加诞辰庆典了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_A5A end

    def Function_9_AB8(): pass

    label("Function_9_AB8")

    Call(0, 10)
    Return()

    # Function_9_AB8 end

    def Function_10_ABD(): pass

    label("Function_10_ABD")

    TalkBegin(0xA)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B1C")
    OP_0D()
    OP_A9(0x5F)
    OP_56(0x0)
    TalkEnd(0xA)
    Return()

    label("loc_B1C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B2D")
    TalkEnd(0xA)
    Return()

    label("loc_B2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_BA4")

    ChrTalk(
        0xA,
        (
            "不愧是诞辰庆典啊，\x01",
            "比武术大会还要热闹许多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "从外国来的客人\x01",
            "也比历年的要多很多，\x01",
            "真是快忙不过来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_141C")

    label("loc_BA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_C17")

    ChrTalk(
        0xA,
        (
            "正规军撤离了，\x01",
            "取而代之是黑衣士兵\x01",
            "在街上巡逻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "虽然诞辰庆典将近了，\x01",
            "令人不安的事情却接踵而至。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_141C")

    label("loc_C17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 5)), scpexpr(EXPR_END)), "loc_C65")

    ChrTalk(
        0xA,
        (
            "克鲁茨先生\x01",
            "刚才到外面去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "他的身体\x01",
            "已经没有问题了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_141C")

    label("loc_C65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_D1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_CBC")

    ChrTalk(
        0xA,
        (
            "刚才游击士\x01",
            "克鲁茨先生回来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "但他的脸色\x01",
            "似乎不是很好……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D19")

    label("loc_CBC")

    OP_A2(0x1)

    ChrTalk(
        0xA,
        (
            "刚才游击士\x01",
            "克鲁茨先生回来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "但他的脸色\x01",
            "似乎不是很好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "应该没事吧……\x02",
    )

    CloseMessageWindow()

    label("loc_D19")

    Jump("loc_141C")

    label("loc_D1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_EAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_D94")

    ChrTalk(
        0xA,
        (
            "恭喜你们二人取得\x01",
            "这次武术大会的优胜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "你们就不用在意\x01",
            "这边的安排了。\x01",
            "请好好享受王城的晚宴吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EAA")

    label("loc_D94")

    OP_A2(0x1)

    ChrTalk(
        0x101,
        "#000F啊，福立兹先生。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "哦，艾丝蒂尔小姐，\x01",
            "有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F今天晚上我们准备住在别的地方了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "嗯，\x01",
            "之前艾南先生已经告知我了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "恭喜你们取得\x01",
            "武术大会的优胜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "不用在意这边的安排，\x01",
            "请好好享受王城的晚宴吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F不愧是艾南先生啊，\x01",
            "动作这么快。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EAA")

    Jump("loc_141C")

    label("loc_EAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_F21")

    ChrTalk(
        0xA,
        (
            "艾丝蒂尔小姐，约修亚先生，\x01",
            "今天是武术大会的决赛吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "我会在这里默默支持各位的。\x01",
            "请你们路上慢走。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_141C")

    label("loc_F21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_105A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_FA3")

    ChrTalk(
        0xA,
        (
            "听说从今天起\x01",
            "士兵就要严加巡逻了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "虽然给你们带来种种不便，\x01",
            "但是请不要在外面待得太晚，\x01",
            "一定要早点回来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1057")

    label("loc_FA3")

    OP_A2(0x1)

    ChrTalk(
        0xA,
        (
            "艾丝蒂尔小姐，约修亚先生，\x01",
            "刚才收到了\x01",
            "王国军发来的联络……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "听说从今天起\x01",
            "他们就要严加巡逻了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "虽然给你们带来种种不便，\x01",
            "但是请不要在外面待得太晚，\x01",
            "一定要早点回来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1057")

    Jump("loc_141C")

    label("loc_105A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_10A8")

    ChrTalk(
        0xA,
        (
            "怎么样，\x01",
            "昨晚睡得好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "今天是准决赛吧。\x01",
            "请你们路上慢走。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_141C")

    label("loc_10A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1186")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1105")

    ChrTalk(
        0xA,
        (
            "对了，\x01",
            "还有另外两位游击士\x01",
            "现在也住在酒店里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "你们见到他们了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1183")

    label("loc_1105")

    OP_A2(0x1)

    ChrTalk(
        0xA,
        (
            "艾丝蒂尔小姐，约修亚先生，\x01",
            "欢迎你们回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "对了，\x01",
            "还有另外两位游击士\x01",
            "现在也住在酒店里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "你们见到他们了吗？\x02",
    )

    CloseMessageWindow()

    label("loc_1183")

    Jump("loc_141C")

    label("loc_1186")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_11D7")

    ChrTalk(
        0xA,
        "各位是大会的出场选手吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "期待你们大显身手，\x01",
            "祝你们一路顺风。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_141C")

    label("loc_11D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_13A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_1241")

    ChrTalk(
        0xA,
        (
            "两位的房间\x01",
            "在楼上走廊尽头的\x01",
            "２０２号室。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "如果有什么需要的话，\x01",
            "请来前台告诉我。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13A2")

    label("loc_1241")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_12CA")

    ChrTalk(
        0xA,
        (
            "尊敬的客人，非常抱歉。\x01",
            "现在还不能为你们安排房间，\x01",
            "因为房间还没有清扫完毕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "想要在这里登记住宿的话，\x01",
            "请三点以后再来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13A2")

    label("loc_12CA")

    OP_A2(0x1)

    ChrTalk(
        0xA,
        (
            "尊敬的客人，非常抱歉。\x01",
            "现在还不能为你们安排房间，\x01",
            "因为房间还没有清扫完毕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "想要在这里登记住宿的话，\x01",
            "请三点以后再来。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F待会儿来登记吧，\x01",
            "还是先去找到金先生再说。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#001FＯＫ。\x02",
    )

    CloseMessageWindow()

    label("loc_13A2")

    Jump("loc_141C")

    label("loc_13A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_141C")

    ChrTalk(
        0xA,
        (
            "有许多客人\x01",
            "都是从很远的地方\x01",
            "赶来参加武术大会的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "我们也非常欢迎\x01",
            "参加大会的选手\x01",
            "前来光顾我们的酒店呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_141C")

    TalkEnd(0xA)
    Return()

    # Function_10_ABD end

    def Function_11_1420(): pass

    label("Function_11_1420")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_142D")
    Jump("loc_16AE")

    label("loc_142D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1437")
    Jump("loc_16AE")

    label("loc_1437")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1441")
    Jump("loc_16AE")

    label("loc_1441")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_144B")
    Jump("loc_16AE")

    label("loc_144B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1455")
    Jump("loc_16AE")

    label("loc_1455")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_150D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1497")

    ChrTalk(
        0xFE,
        (
            "『不动金』自不用说，\x01",
            "你们的战斗也十分出色。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_150A")

    label("loc_1497")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "哦，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "『不动金』自不用说，\x01",
            "你们的战斗也十分出色。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "每个人的技术都不错，\x01",
            "配合也相当熟练。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_150A")

    Jump("loc_16AE")

    label("loc_150D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1517")
    Jump("loc_16AE")

    label("loc_1517")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1693")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1573")

    ChrTalk(
        0xFE,
        (
            "我们两组今天都能成功晋级，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我很期待与你们的对战哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1690")

    label("loc_1573")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "哟，这不是艾丝蒂尔和约修亚嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，克鲁茨前辈。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们两组今天都能成功晋级，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然之前也听卡露娜说过，\x01",
            "不过这次是亲眼见到你们的实力了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F哪里，我们还在修行中。\x02\x03",
            "我们要在这次大会里\x01",
            "多向前辈们学习才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈哈，\x01",
            "我很期待与你们的对战哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1690")

    Jump("loc_16AE")

    label("loc_1693")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_169D")
    Jump("loc_16AE")

    label("loc_169D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_16A7")
    Jump("loc_16AE")

    label("loc_16A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_16AE")

    label("loc_16AE")

    TalkEnd(0xFE)
    Return()

    # Function_11_1420 end

    def Function_12_16B2(): pass

    label("Function_12_16B2")

    ClearMapFlags(0x10000000)
    EventBegin(0x0)
    OP_31(0x3, 0x0, 0x1E)
    OP_B5(0x3, 0x0)
    OP_B5(0x3, 0x1)
    OP_B5(0x3, 0x2)
    OP_B5(0x3, 0x3)
    OP_B5(0x3, 0x4)
    OP_B5(0x3, 0x5)
    OP_41(0x3, 0x5E)
    OP_41(0x3, 0xF5)
    OP_41(0x3, 0x113)
    OP_41(0x3, 0x25C, 0x0)
    OP_41(0x3, 0x26B, 0x1)
    OP_41(0x3, 0x25F, 0x2)
    OP_41(0x3, 0x262, 0x2)
    OP_35(0x3, 0xB4)
    OP_35(0x3, 0xB5)
    OP_36(0x3, 0xF5)
    OP_6D(12040, 2000, 7430, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    AddParty(0x3, 0xFF)
    AddParty(0x7, 0xFF)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    SetChrPos(0x101, 11710, 2000, 7600, 0)
    SetChrPos(0x102, 12480, 2000, 8230, 0)
    SetChrPos(0x108, 8480, 0, -1270, 135)
    SetChrPos(0x104, 7240, -250, -7700, 135)
    SetChrFlags(0x104, 0x80)

    def lambda_17B3():

        label("loc_17B3")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_17B3")

    QueueWorkItem2(0x101, 1, lambda_17B3)

    def lambda_17C4():

        label("loc_17C4")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_17C4")

    QueueWorkItem2(0x102, 1, lambda_17C4)

    def lambda_17D5():
        OP_8E(0xFE, 0x2DB4, 0x0, 0x122, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_17D5)

    def lambda_17F0():
        OP_8E(0xFE, 0x30D4, 0x0, 0x3B6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_17F0)

    def lambda_180B():

        label("loc_180B")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_180B")

    QueueWorkItem2(0x108, 1, lambda_180B)
    OP_6D(10650, 0, 1690, 3000)

    ChrTalk(
        0x108,
        "#070F#5P哟，起得真早。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F啊，早上好～金先生！\x02",
    )

    CloseMessageWindow()

    def lambda_1868():
        OP_8E(0xFE, 0x25EE, 0x0, 0xFFFFF7CC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1868)

    def lambda_1883():
        OP_8E(0xFE, 0x2508, 0x0, 0xFFFFFC90, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1883)
    OP_6D(8570, 0, -1520, 2000)
    WaitChrThread(0x102, 0x2)

    ChrTalk(
        0x102,
        (
            "#010F真是抱歉，\x01",
            "让您特地来接我们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F没什么啦。\x02\x03",
            "不管怎么说，\x01",
            "比赛之前还是要做好各种准备啊。\x02\x03",
            "最好把工房、武器店和\x01",
            "百货店什么的都通通逛一遍。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F这就是所谓的『有备无患』吧。\x02\x03",
            "#505F对了……\x01",
            "奥利维尔那家伙怎么还没来？\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    Sleep(200)

    ChrTalk(
        0x104,
        "#2P早上好啊～亲爱的各位㈱\x02",
    )

    CloseMessageWindow()

    def lambda_19C9():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_19C9)

    def lambda_19D7():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_19D7)

    def lambda_19E5():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_19E5)
    ClearChrFlags(0x104, 0x80)
    OP_9F(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1A03():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1A03)
    OP_8E(0x104, 0x1C0C, 0xFFFFFF06, 0xFFFFE732, 0x7D0, 0x0)

    def lambda_1A29():

        label("loc_1A29")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_1A29")

    QueueWorkItem2(0x108, 1, lambda_1A29)

    def lambda_1A3A():

        label("loc_1A3A")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_1A3A")

    QueueWorkItem2(0x101, 1, lambda_1A3A)

    def lambda_1A4B():

        label("loc_1A4B")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_1A4B")

    QueueWorkItem2(0x102, 1, lambda_1A4B)

    def lambda_1A5C():
        OP_8E(0xFE, 0x20EE, 0x0, 0xFFFFF65A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1A5C)
    WaitChrThread(0x104, 0x1)

    ChrTalk(
        0x104,
        (
            "#031F哈·哈·哈。\x01",
            "如此清爽的早晨，\x01",
            "给我们的初次上阵增色不少呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F又是这样……\x01",
            "老是算好时间突然出现人家面前……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F早上好，奥利维尔。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F早上好。\x01",
            "这样人员已经到齐了。\x02\x03",
            "那就赶快出发吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F我记得武术大会\x01",
            "应该是从中午开始的吧。\x02\x03",
            "现在还很早，\x01",
            "我们要怎样打发时间呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x108, 0xFF)
    OP_8C(0x108, 135, 400)

    ChrTalk(
        0x108,
        (
            "#070F刚才说过了，\x01",
            "我们最好去商店补充一下不足的装备。\x02\x03",
            "而且，为了让身体活动开，\x01",
            "去城外街道上打打魔兽也不错。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x104, 0, 400)

    ChrTalk(
        0x104,
        (
            "#030F原来如此，就算是热身啦。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F确实，很有必要在比赛之前\x01",
            "找找团体战斗的感觉呢。\x02\x03",
            "以这样的阵容作战，还是第一次呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F那就这样决定吧，我们出发吧！\x02\x03",
            "做好准备之后就去竞技场吧！\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    OP_A2(0x619)
    OP_28(0x47, 0x4, 0x2)
    OP_28(0x47, 0x4, 0x4)
    OP_28(0x47, 0x1, 0x1)
    OP_28(0x47, 0x1, 0x2)
    EventEnd(0x0)
    Return()

    # Function_12_16B2 end

    def Function_13_1D12(): pass

    label("Function_13_1D12")

    ClearMapFlags(0x10000000)
    EventBegin(0x0)
    OP_6D(7340, -250, -5730, 0)
    OP_67(0, 5960, -10000, 0)
    OP_6B(3010, 0)
    SetChrPos(0x8, 4320, 0, 1700, 180)
    TurnDirection(0x8, 0x101, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x101, 6490, -250, -5810, 0)
    SetChrPos(0x102, 7740, -250, -5800, 0)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(
        0x8,
        "男人的声音",
        "#6P终于回来了啊。\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "男人的声音",
        "#6P真是让我好等啊。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_1E0C():

        label("loc_1E0C")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_1E0C")

    QueueWorkItem2(0x101, 1, lambda_1E0C)

    ChrTalk(
        0x101,
        "#501F这个声音……\x02",
    )

    CloseMessageWindow()

    def lambda_1E34():
        OP_6D(4450, 0, 1130, 2000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1E34)

    def lambda_1E4C():
        OP_8E(0xFE, 0xFFA, 0x0, 0xFFFFFF74, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1E4C)
    Sleep(300)

    def lambda_1E6C():
        OP_8E(0xFE, 0x145A, 0x0, 0xFFFFFEA2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1E6C)
    WaitChrThread(0x102, 0x1)

    ChrTalk(
        0x102,
        "#010F#6P很久不见了，奈尔先生。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F哇～是奈尔啊。\x02\x03",
            "怎么，是特地来拜访我们的吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#141F嗯。就是特地来拜访你们的。\x01",
            "　\x02\x03",
            "据对武术大会进行取材的同事说，\x01",
            "有两位年轻有为的少年参加了比赛。\x02\x03",
            "听说了详细情况之后，\x01",
            "不管怎么想都觉得是你们啊。\x02\x03",
            "所以我才来到王都这里，\x01",
            "在酒店门口等着你们回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F哈哈……看来你还是老样子，\x01",
            "无论什么时候消息都是那么的灵通。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#6P虽然很高兴您能来看我们……\x01",
            "　\x02\x03",
            "不过奈尔先生，\x01",
            "恐怕您是有事才来这里的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F啊，又是在寻找新闻素材吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#145F啊～真是可叹啊。\x02\x03",
            "这次特地抛开利益得失来维持我们的友情，\x01",
            "你们就这么不明白大哥我的苦心吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F说谎～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F#6P而且，说自己是大哥，\x01",
            "年纪也似乎相差得太远了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#144F哼，别提啦。\x02\x03",
            "不说这个啦，\x01",
            "我们赶快出去吃饭吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#6P又这么突然……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F可以是可以，\x01",
            "不过是谁请客你应该清楚吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#145F呜……算了。\x02\x03",
            "#141F那么我们就去杂志社附近的酒馆吧。\x01",
            "　\x02\x03",
            "就在那里吃晚饭好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x47, 0x1, 0x400)
    OP_20(0x5DC)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4152   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_1D12 end

    def Function_14_222B(): pass

    label("Function_14_222B")

    EventBegin(0x0)
    OP_6D(6960, 0, 4490, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(287, 0)
    AddParty(0x3, 0xFF)
    AddParty(0x7, 0xFF)
    SetChrPos(0x108, 8480, 0, -1270, 90)
    SetChrPos(0x104, 8430, 0, -2470, 45)
    SetChrPos(0x101, 9710, 0, -2100, 270)
    SetChrPos(0x102, 9480, 0, -880, 270)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    FadeToBright(2000, 0)
    OP_6D(8570, 0, -1520, 3000)

    ChrTalk(
        0x104,
        (
            "#031F呵呵，大家都到齐了。\x02\x03",
            "我们赶快出发吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F和昨天一样，比赛是从中午开始，\x01",
            "上午我们可以自由行动。\x02\x03",
            "在商店里整理装备也好，\x01",
            "去街道上打魔兽活动一下筋骨也好。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F啊，如果是这样的话，\x01",
            "我这里有一个非常好的地方呢。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔向金和奥利维尔说明了\x01",
            "从渡鸦帮成员那里得到地下水路钥匙的事情。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0x108,
        (
            "#073F哦，还真是有意思啊。\x02\x03",
            "有比较强的魔兽的话，\x01",
            "正好可以用来当练习的对手。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F美丽高贵的王都地下\x01",
            "布满了古代的地下水路……\x02\x03",
            "呵呵，真是浪漫啊。\x01",
            "这不是在刺激我的冒险之心嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F如果有空的话，\x01",
            "中午以前去看看吧。\x02\x03",
            "地下水路的入口处就在\x01",
            "西街区住宅区外围的城墙上。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x621)
    OP_28(0x48, 0x4, 0x2)
    OP_28(0x48, 0x4, 0x4)
    OP_28(0x48, 0x1, 0x1)
    OP_28(0x48, 0x1, 0x2)
    EventEnd(0x0)
    Return()

    # Function_14_222B end

    def Function_15_2585(): pass

    label("Function_15_2585")

    EventBegin(0x0)
    OP_6D(6960, 0, 4490, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(287, 0)
    AddParty(0x3, 0xFF)
    AddParty(0x7, 0xFF)
    SetChrPos(0x108, 8480, 0, -1270, 90)
    SetChrPos(0x104, 8430, 0, -2470, 45)
    SetChrPos(0x101, 9710, 0, -2100, 270)
    SetChrPos(0x102, 9480, 0, -880, 270)
    FadeToDark(0, 0, -1)
    OP_20(0x0)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1E()
    FadeToBright(2000, 0)
    OP_6D(8570, 0, -1520, 3000)

    ChrTalk(
        0x104,
        (
            "#034F昨天真是不走运啊。\x02\x03",
            "要是回大使馆的时候装成喝醉的样子，\x01",
            "就不会被那些士兵诘难了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F据说，好像是针对恐怖活动的对策，\x01",
            "强化夜间巡逻也是没办法的事啊。\x01",
            "　\x02\x03",
            "你们没事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F嗯，昨天早早地就休息了，\x01",
            "没有发生什么问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F而、而且我们还从艾南哥哥那里\x01",
            "借到了好东西呢。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔和约修亚向金和奥利维尔说明了\x01",
            "从艾南那里借到另外一把地下水路钥匙的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0x108,
        (
            "#071F哦哦，这还真是帮大忙了。\x02\x03",
            "那个小哥，虽然还很年轻,\x01",
            "不过考虑事情都很周到嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F这样的话，中午之前\x01",
            "我们就去地下水路锻炼一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F另外一个入口就在竞技场的旁边。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F呼，为了我的晚宴，\x01",
            "就做一下最后的努力吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x62F)
    OP_28(0x49, 0x4, 0x2)
    OP_28(0x49, 0x4, 0x4)
    OP_28(0x49, 0x1, 0x1)
    OP_28(0x49, 0x1, 0x2)
    EventEnd(0x0)
    Return()

    # Function_15_2585 end

    def Function_16_2918(): pass

    label("Function_16_2918")

    EventBegin(0x0)
    SetChrPos(0x9, 35140, 0, 114000, 0)
    OP_6D(35210, 0, 115000, 0)
    OP_67(0, 4890, -10000, 0)
    OP_6B(1680, 0)
    OP_6C(320000, 0)
    OP_6E(509, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x108, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x101, 35130, 0, 107040, 180)
    SetChrPos(0x102, 35130, 0, 107040, 180)
    SetChrPos(0x108, 35130, 0, 107040, 180)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x9,
        "#5P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P那个时候的记忆……\x01",
            "后来还是回想起来了一点……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5P模模糊糊的一点都不清晰……\x02",
    )

    CloseMessageWindow()

    def lambda_2A49():
        OP_6D(35210, 0, 113750, 2000)
        ExitThread()

    QueueWorkItem(0x108, 3, lambda_2A49)

    def lambda_2A61():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2A61)

    def lambda_2A73():
        OP_8E(0xFE, 0x87BE, 0x0, 0x1B6C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A73)
    Sleep(600)

    def lambda_2A93():
        OP_8E(0xFE, 0x8BA6, 0x0, 0x1B652, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2A93)

    def lambda_2AAE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2AAE)
    Sleep(600)

    def lambda_2AC5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_2AC5)

    def lambda_2AD7():
        OP_8E(0xFE, 0x8958, 0x0, 0x1B1E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2AD7)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        "#501F啊，克鲁茨大哥……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)

    ChrTalk(
        0x102,
        "#010F太好了，您在这里啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x108, 400)

    ChrTalk(
        0x9,
        (
            "咦……\x01",
            "是艾丝蒂尔和约修亚啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "金大哥也在，到底怎么回事了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F我们几个昨晚到王城里参加了晚宴的\x01",
            "这件事情你应该知道吧？\x02\x03",
            "在那时，这两位新来的游击士\x01",
            "接受了一个非常重大的委托。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "非常重大的委托……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们给克鲁茨大哥您说明一下情况吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "说明了至今为止发生的事情和女王的委托。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x9,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "……这是……真的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F当然是了。\x02\x03",
            "因此我们也需要克鲁茨大哥来帮忙。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "不……我不是说这个。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "女王陛下的委托\x01",
            "的确让我深感震惊……\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)

    ChrTalk(
        0x9,
        (
            "但是，理查德上校\x01",
            "得到的那个黑色导力器\x01",
            "真的……存在吗……？\x02",
        )
    )

    CloseMessageWindow()
    OP_21()
    OP_1D(0x51)

    ChrTalk(
        0x101,
        (
            "#505F……克鲁茨大哥？\x02\x03",
            "你、你怎么了？\x01",
            "为什么脸都发青了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#10A呜呜呜……\x05\x02",
    )

    OP_9E(0x9, 0x1E, 0x0, 0x3E8, 0xBB8)
    SetChrFlags(0x9, 0x20)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 4)

    def lambda_2DFF():
        OP_99(0xFE, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2DFF)
    Sleep(500)

    ChrTalk(
        0x9,
        "#10A#3S啊啊啊啊啊啊啊啊……\x05\x02",
    )

    OP_9E(0x9, 0x1E, 0x0, 0x3E8, 0xFA0)

    def lambda_2E48():

        label("loc_2E48")

        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0x1770)
        OP_48()
        Jump("loc_2E48")

    QueueWorkItem2(0x9, 1, lambda_2E48)
    Sleep(800)

    ChrTalk(
        0x9,
        "#5S哦啊啊啊啊啊啊！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F哇啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F这、这是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#072F呼……你们让开一下。\x02",
    )

    CloseMessageWindow()

    def lambda_2EDB():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2EDB)
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(
        0x101,
        "#004F咦……\x02",
    )

    CloseMessageWindow()

    def lambda_2F01():

        label("loc_2F01")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_2F01")

    QueueWorkItem2(0x102, 1, lambda_2F01)

    def lambda_2F12():

        label("loc_2F12")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_2F12")

    QueueWorkItem2(0x101, 1, lambda_2F12)

    def lambda_2F23():
        OP_8F(0xFE, 0x8412, 0x0, 0x1B3A0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2F23)

    def lambda_2F3E():
        OP_8F(0xFE, 0x8DF4, 0x0, 0x1B314, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2F3E)
    Sleep(300)
    OP_8E(0x108, 0x88CC, 0x0, 0x1B7D8, 0x7D0, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    Sleep(500)

    ChrTalk(
        0x108,
        "#074F嘿咿咿唔唔唔唔唔唔……\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x108, 2)
    OP_0D()

    ChrTalk(
        0x108,
        "#076F#20A#3S哈～……\x05\x02",
    )


    def lambda_2FC5():

        label("loc_2FC5")

        OP_99(0xFE, 0x0, 0x3, 0x3E8)
        OP_48()
        Jump("loc_2FC5")

    QueueWorkItem2(0x108, 1, lambda_2FC5)
    OP_6B(1600, 3000)
    OP_44(0x108, 0xFF)
    OP_51(0x108, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x108, 3)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 5)
    OP_44(0x9, 0xFF)
    SetChrFlags(0x9, 0x800)

    def lambda_300E():
        OP_6D(35130, 0, 115000, 500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_300E)

    def lambda_3026():
        OP_8F(0xFE, 0x893A, 0x0, 0x1C32C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3026)

    def lambda_3041():
        OP_94(0x1, 0xFE, 0xB4, 0x258, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3041)

    def lambda_3057():
        OP_94(0x1, 0xFE, 0xB4, 0x258, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3057)

    ChrTalk(
        0x108,
        "#077F#3P#10A#5S喝！\x05\x02",
    )

    OP_22(0x1FB, 0x0, 0x64)
    OP_22(0x217, 0x0, 0x64)
    WaitChrThread(0x9, 0x1)
    OP_22(0x22A, 0x0, 0x64)

    ChrTalk(
        0x9,
        "#2P#10A#3S啊！\x05\x02",
    )

    OP_6B(1700, 0)
    OP_6B(1670, 100)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 4)

    def lambda_30D0():
        OP_99(0xFE, 0x0, 0x3, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_30D0)
    Sleep(2000)
    SetChrFlags(0x9, 0x800)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x101,
        (
            "#004F#5P刚、刚才那是……\x02\x03",
            "虽然没有接触到身体，\x01",
            "但却听到了啪的一声呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F刚才那是气功……\x02\x03",
            "虽然没有接触到身体，\x01",
            "但可以对肉体直接作用……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#074F#5P因为事出突然，\x01",
            "所以只有采取这种粗鲁的方式。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_51(0x108, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x108, 65535)
    OP_0D()

    def lambda_31E0():
        OP_8F(0xFE, 0x8552, 0x0, 0x1C020, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_31E0)
    Sleep(300)

    def lambda_3200():
        OP_6D(35130, 0, 115500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3200)
    Sleep(300)
    SetChrFlags(0x101, 0x4)

    def lambda_3222():
        OP_8E(0xFE, 0x88A4, 0x0, 0x1BB2A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3222)
    Sleep(200)

    def lambda_3242():
        OP_8E(0xFE, 0x8C00, 0x0, 0x1BBAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3242)
    WaitChrThread(0x108, 0x1)
    OP_8C(0x108, 90, 400)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 0, 400)
    ClearChrFlags(0x101, 0x4)

    ChrTalk(
        0x108,
        "#070F感觉如何？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "是啊……\x01",
            "对不起，已经没事了。\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x9, 0x3, 0x0, 0x3E8)
    Sleep(200)
    SetChrChipByIndex(0x9, 1)

    ChrTalk(
        0x9,
        (
            "虽然不是全部……\x01",
            "但终于回想起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "如果没有这一震，\x01",
            "身体就会不听使唤了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F回、回想起来了什么……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "之前也说过的吧？\x01",
            "三个月前的那起事故……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F克鲁茨大哥在任务中失去记忆的事。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "是啊……\x01",
            "那时有一个人委托我调查\x01",
            "黑衣人一伙的事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "然后我夺取了那伙人运送的\x01",
            "一个可疑物品。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "那就是黑色导力器。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F那个委托您的人难道是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "是啊……\x01",
            "就是你们的父亲卡西乌斯先生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我急忙把那个导力器\x01",
            "用小包裹装着寄给了卡西乌斯先生……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "到这里为止，之后的我就想不起来了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#580F这、这么说！\x01",
            "寄小包裹的『Ｋ』就是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "啊……就是我。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我记得还写了让拉赛尔博士\x01",
            "分析这东西的讯息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "哦，那个小包裹\x01",
            "是你们收到的啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F克鲁茨大哥……\x01",
            "那之后的记忆呢？\x02\x03",
            "把小包裹寄给父亲之后，\x01",
            "你又遇到了什么事情呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "啊……离开了飞艇坪后，\x01",
            "好像听到有人在背后叫我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "然后……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "………………………………\x01",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "不行啊，记忆模模糊糊的，\x01",
            "完全记不起来啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#072F不要太勉强了，记不起来就算了。\x01",
            "　\x02\x03",
            "这样只会增加身体的负担。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "……啊，我明白了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "总之，那时的事情\x01",
            "我就只能记起这么多了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F可是……\x01",
            "到底是谁做出的这种事情……\x02\x03",
            "果然和那些特务兵有所关系吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F有这种可能性……\x02\x03",
            "#013F让阿加特兄深受煎熬的\x01",
            "神经性毒药也是这样……\x02\x03",
            "看来是开发了特殊的药品\x01",
            "然后以此来作为测试。\x02\x03",
            "#012F也许是使用了可以让记忆超负荷的药品。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F让、让人有些毛骨悚然呢。\x02\x03",
            "#002F这么说来，空贼的头目\x01",
            "和戴尔蒙市长也是这样的了。\x02\x03",
            "我们也必须小心才行……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "抱歉……\x01",
            "关键的事情还没有说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "陛下委托的事情我知道了，\x01",
            "无论如何我也要尽一份力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F可、可是……\x01",
            "克鲁茨大哥你的身体行吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "啊，取回了记忆，\x01",
            "感觉轻松了不少啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "就算是为了报这个仇也好，\x01",
            "请务必让我尽一份力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F这样的状况来看已经没问题了。\x02\x03",
            "作战会议即将开始了，\x01",
            "还请你先回协会稍等一会吧。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x20)

    def lambda_39B8():

        label("loc_39B8")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_39B8")

    QueueWorkItem2(0x9, 1, lambda_39B8)

    ChrTalk(
        0x9,
        "我明白了……多谢您刚才的相助！\x02",
    )

    CloseMessageWindow()
    OP_44(0x9, 0xFF)

    def lambda_39F1():

        label("loc_39F1")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_39F1")

    QueueWorkItem2(0x101, 1, lambda_39F1)

    def lambda_3A02():

        label("loc_3A02")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_3A02")

    QueueWorkItem2(0x102, 1, lambda_3A02)

    def lambda_3A13():

        label("loc_3A13")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_3A13")

    QueueWorkItem2(0x108, 1, lambda_3A13)

    def lambda_3A24():
        OP_6D(34710, 0, 112900, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3A24)
    OP_8E(0x9, 0x8606, 0x0, 0x1BB2A, 0xBB8, 0x0)
    OP_8E(0x9, 0x8912, 0x0, 0x1A298, 0xBB8, 0x0)

    def lambda_3A64():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3A64)
    SetChrFlags(0x9, 0x4)
    OP_8E(0x9, 0x88C2, 0x0, 0x19B36, 0xBB8, 0x0)
    SetChrFlags(0x9, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    OP_28(0x4B, 0x1, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x1, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x1, 0x20)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x1, 0x40)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x4B, 0x1, 0x80)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AC9")
    OP_28(0x4B, 0x1, 0x100)

    label("loc_3AC9")

    OP_20(0x3E8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(34980, 0, 113450, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 34980, 0, 113450, 180)
    SetChrPos(0x102, 34980, 0, 113450, 180)
    SetChrPos(0x108, 34980, 0, 113450, 180)
    FadeToBright(1000, 0)
    OP_1D(0xE)
    EventEnd(0x0)
    Return()

    # Function_16_2918 end

    def Function_17_3B57(): pass

    label("Function_17_3B57")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　　　　　　事务室　　　　　　　\x01",
            "※工作人员以外禁止进入。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_17_3B57 end

    SaveToFile()

Try(main)
