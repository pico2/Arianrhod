from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'R3403   ._SN',
        MapName             = 'Zeiss',
        Location            = 'R3403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60030",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/R3403   ._SN',
            'ED6_DT01/R3403_1 ._SN',
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
        '鲁迪',                                 # 9
        '安东尼',                               # 10
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
        'ED6_DT07/CH01500 ._CH',             # 00
        'ED6_DT07/CH01700 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01500P._CP',             # 00
        'ED6_DT07/CH01700P._CP',             # 01
    )

    DeclNpc(
        X                   = 612030,
        Z                   = -50,
        Y                   = -62600,
        Direction           = 359,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
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
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 602300,
        Y                   = -1000,
        Z                   = -48740,
        Range               = 599000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF13E8,
        Unknown_18          = 0x0,
        Unknown_1C          = 7,
    )


    ScpFunction(
        "Function_0_11A",          # 00, 0
        "Function_1_208",          # 01, 1
        "Function_2_21B",          # 02, 2
        "Function_3_231",          # 03, 3
        "Function_4_544",          # 04, 4
        "Function_5_54F",          # 05, 5
        "Function_6_8DE",          # 06, 6
        "Function_7_A09",          # 07, 7
    )


    def Function_0_11A(): pass

    label("Function_0_11A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_129")
    Jump("loc_156")

    label("loc_129")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_141")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_156")

    label("loc_141")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_156")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_156")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_166"),
        (101, "loc_178"),
        (SWITCH_DEFAULT, "loc_198"),
    )


    label("loc_166")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_175")
    OP_A2(0x507)
    Event(0, 5)

    label("loc_175")

    Jump("loc_198")

    label("loc_178")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_195")
    SetMapFlags(0x10000000)
    OP_A2(0x534)
    Event(0, 6)

    label("loc_195")

    Jump("loc_198")

    label("loc_198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1A7")
    ClearChrFlags(0x8, 0x80)
    Jump("loc_207")

    label("loc_1A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_1B1")
    Jump("loc_207")

    label("loc_1B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1BB")
    Jump("loc_207")

    label("loc_1BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1DB")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 610200, -40, -62060, 180)
    Jump("loc_207")

    label("loc_1DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1E5")
    Jump("loc_207")

    label("loc_1E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_207")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0x8, 618600, -10, -47550, 46)

    label("loc_207")

    Return()

    # Function_0_11A end

    def Function_1_208(): pass

    label("Function_1_208")

    OP_16(0x2, 0xFA0, 0x76E58, 0xFFFD40E0, 0x3003A)
    Return()

    # Function_1_208 end

    def Function_2_21B(): pass

    label("Function_2_21B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_230")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_21B")

    label("loc_230")

    Return()

    # Function_2_21B end

    def Function_3_231(): pass

    label("Function_3_231")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_29E")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "从工房船回来之后，\x01",
            "菲前辈还是没什么精神啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难、难道说，\x01",
            "她和原男友的关系又有变化了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_540")

    label("loc_29E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_4C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_338")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "再见了，\x01",
            "你们也要小心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为库存已经所剩不多了，\x01",
            "所以你们一定要送到啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼…………\x01",
            "我也要打起精神来，\x01",
            "好好工作才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C3")

    label("loc_338")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x29, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x29, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_353")
    Call(1, 2)
    Jump("loc_4C3")

    label("loc_353")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_40A")

    ChrTalk(
        0xFE,
        (
            "刚才在工作的时候\x01",
            "又被菲前辈骂了一顿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "肯定是因为前辈\x01",
            "认为我是个没用的家伙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呜呜，\x01",
            "好不容易前辈和男友分手，\x01",
            "我以为会有机会的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "唉～我真是没用啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C3")

    label("loc_40A")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "唉～～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "刚才在工作的时候\x01",
            "又被菲前辈骂了一顿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "肯定是因为前辈\x01",
            "认为我是个没用的家伙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呜呜，\x01",
            "好不容易前辈和男友分手，\x01",
            "我以为会有机会的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "唉～我真是没用啊。\x02",
    )

    CloseMessageWindow()

    label("loc_4C3")

    Jump("loc_540")

    label("loc_4C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_540")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "唔，\x01",
            "加上这罐的话总共就有８罐了………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "好了，和清单上的一样。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "接下来就交给工场那边检查吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_540")

    TalkEnd(0xFE)
    Return()

    # Function_3_231 end

    def Function_4_544(): pass

    label("Function_4_544")

    ClearMapFlags(0x800)
    OP_1B(0x0, 0x0, 0xFFFF)
    Return()

    # Function_4_544 end

    def Function_5_54F(): pass

    label("Function_5_54F")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(600200, 0, -54800, 0)
    OP_6C(0, 0)
    SetChrPos(0x101, 596400, 0, -54800, 90)
    SetChrPos(0x102, 595000, 0, -53500, 90)
    SetChrPos(0x107, 595000, 0, -55200, 90)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#004F啊……！\x02",
    )

    CloseMessageWindow()

    def lambda_5C6():
        OP_8E(0xFE, 0x967D0, 0x0, 0xFFFF29F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5C6)
    Sleep(200)

    def lambda_5E6():
        OP_8E(0xFE, 0x96258, 0x0, 0xFFFF2B80, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5E6)
    Sleep(500)

    def lambda_606():
        OP_8E(0xFE, 0x962BC, 0x0, 0xFFFF25A4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_606)

    def lambda_621():
        OP_6D(618500, 0, -53800, 3500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_621)

    def lambda_639():
        OP_6C(45000, 3300)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_639)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#501F到隧道的尽头了……\x02\x03",
            "这么说……\x01",
            "这里就是蔡斯市的入口了？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x107, 0x1)
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(
        0x107,
        (
            "#060F嗯，是的。\x02\x03",
            "准确地来说，\x01",
            "是到了中央工房的地下区域了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6E1():
        OP_6D(615770, -90, -54810, 1200)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6E1)
    OP_8C(0x101, 270, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x101,
        "#006F中央工房是……？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 135, 400)

    ChrTalk(
        0x102,
        (
            "#015F『中央工房』——\x01",
            "顾名思义就是工房都市蔡斯\x01",
            "引以为傲的导力器技术殿堂对吧。\x02\x03",
            "#010F以前就听说这里是\x01",
            "一座极为庞大的建筑物……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#061F那当然了～\x01",
            "而且这里不是一般的大呢。\x02\x03",
            "很多客人第一次来这里\x01",
            "都免不得会迷路一番的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F哇……\x01",
            "那可真是太大了啊。\x02\x03",
            "#007F看来我开始担心\x01",
            "能不能平安到达游击士协会了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F没问题的。\x01",
            "上了一楼就有通往城镇的入口呢。\x02\x03",
            "我来为姐姐你们带路吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F谢谢，那就拜托了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那我们进去吧。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_5_54F end

    def Function_6_8DE(): pass

    label("Function_6_8DE")

    EventBegin(0x0)
    OP_6D(619220, 250, -53680, 0)
    SetChrPos(0x106, 618640, 0, -54820, 270)
    SetChrPos(0x101, 619650, 750, -54420, 270)
    SetChrPos(0x102, 619020, 250, -55970, 270)
    SetChrPos(0x107, 620220, 1000, -55430, 270)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#002F那些家伙们，\x01",
            "是往这边逃走了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#552F不，应该不是……\x01",
            "没有看到新的脚印。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F而且也没有事先作伪装的时间。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#065F也就是说……他们到一楼去了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F嗯，赶快！\x02",
    )

    CloseMessageWindow()
    ClearMapFlags(0x10000000)
    NewScene("ED6_DT01/T3111   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_6_8DE end

    def Function_7_A09(): pass

    label("Function_7_A09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A91")
    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F首先我们要去飞艇坪\x01",
            "把搭乘手续取消掉。\x02\x03",
            "如果不取消的话，\x01",
            "售票员会很困扰的。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_1664")

    label("loc_A91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B91")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B1E")
    OP_A2(0x0)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F这边是卡鲁迪亚隧道啊。\x02\x03",
            "为了不耽误乘坐定期船，\x01",
            "还是不要跑得太远吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F啊，对了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B73")

    label("loc_B1E")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F这边是卡鲁迪亚隧道啊。\x02\x03",
            "为了不耽误乘坐定期船，\x01",
            "还是不要跑得太远吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B73")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_1664")

    label("loc_B91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D50")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C40")
    OP_A2(0x0)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#017F艾丝蒂尔，你要去哪儿？\x02\x03",
            "去雷斯顿要塞的话，\x01",
            "要从城东门出去啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#004F啊？\x01",
            "是、是吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F……真是的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_C93")

    label("loc_C40")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#017F去雷斯顿要塞的话，\x01",
            "要从城东门出去才行啊。\x02\x03",
            "你刚才不是记下来了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C93")

    Jump("loc_D32")

    label("loc_C96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CEA")
    OP_A2(0x0)

    ChrTalk(
        0x102,
        (
            "#012F这边是卡鲁迪亚隧道啊。\x02\x03",
            "去雷斯顿要塞的话，\x01",
            "要从城东门出去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D32")

    label("loc_CEA")


    ChrTalk(
        0x102,
        (
            "#012F这边是卡鲁迪亚隧道啊……\x02\x03",
            "去雷斯顿要塞的话，\x01",
            "要从城东门出去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D32")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_1664")

    label("loc_D50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F39")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DED")
    OP_A2(0x0)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F啊，\x01",
            "总之现在要先回协会。\x02\x03",
            "在没有情报的情况下\x01",
            "是不能随便行动的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F是啊。\x01",
            "赶快走吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E36")

    label("loc_DED")


    ChrTalk(
        0x101,
        (
            "#000F总之，\x01",
            "现在要先回协会。\x02\x03",
            "在没有情报的情况下\x01",
            "是不能随便行动的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E36")

    Jump("loc_F1B")

    label("loc_E39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EBF")
    OP_A2(0x0)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F总之现在先回协会\x01",
            "听听雾香小姐怎么说。\x02\x03",
            "说不定能发现什么有价值的线索呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F嗯，走吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_F1B")

    label("loc_EBF")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F总之现在先回协会\x01",
            "听听雾香小姐怎么说。\x02\x03",
            "说不定能发现什么有价值的线索呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F1B")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_1664")

    label("loc_F39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_114A")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FF0")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F艾丝蒂尔，等一下。\x02\x03",
            "首先还是回协会\x01",
            "调查一下以前的记录吧。\x02\x03",
            "关于『塞姆里亚苔藓』的情报\x01",
            "我们还知道得太少。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#002F啊，说得也对。\x02",
    )

    CloseMessageWindow()
    Jump("loc_112C")

    label("loc_FF0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_109B")
    TurnDirection(0x102, 0x107, 400)

    ChrTalk(
        0x102,
        (
            "#012F提妲，先等一下。\x02\x03",
            "首先还是回协会\x01",
            "调查一下以前的记录吧。\x02\x03",
            "关于『塞姆里亚苔藓』的情报\x01",
            "我们还知道得太少。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x102, 400)

    ChrTalk(
        0x107,
        "#060F啊、嗯，我明白了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_112C")

    label("loc_109B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_112C")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10BD")
    TurnDirection(0x102, 0x1, 400)
    Jump("loc_10C4")

    label("loc_10BD")

    TurnDirection(0x102, 0x0, 400)

    label("loc_10C4")


    ChrTalk(
        0x102,
        (
            "#012F教区长也说了，\x01",
            "首先还是回协会\x01",
            "调查一下以前的记录吧。\x02\x03",
            "关于『塞姆里亚苔藓』\x01",
            "要多收集一些情报。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_112C")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_1664")

    label("loc_114A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12A9")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_119F")

    ChrTalk(
        0x101,
        (
            "#002F（啊，这边是隧道……\x01",
            "　现在要赶快去礼拜堂。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_128B")

    label("loc_119F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11E2")

    ChrTalk(
        0x102,
        (
            "#012F（这边是隧道……\x01",
            "　现在要赶快去礼拜堂。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_128B")

    label("loc_11E2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1229")

    ChrTalk(
        0x107,
        (
            "#062F（啊，这边是出口……\x01",
            "　要赶快去礼拜堂才行。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_128B")

    label("loc_1229")


    ChrTalk(
        0x108,
        (
            "#070F（唔，这边是隧道的入口吗。）\x02\x03",
            "（虽然是个不错的修行场所，\x01",
            "　不过现在要紧的是去礼拜堂。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_128B")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_1664")

    label("loc_12A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13B3")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1344")
    OP_A2(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_130D")

    ChrTalk(
        0x106,
        (
            "#050F嘁……\x01",
            "现在再追也不会有线索的。\x02\x03",
            "总之先回协会吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1341")

    label("loc_130D")

    TurnDirection(0x106, 0x0, 400)

    ChrTalk(
        0x106,
        (
            "#050F喂，你们去哪儿。\x02\x03",
            "赶快回协会去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1341")

    Jump("loc_1395")

    label("loc_1344")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_135A")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_1361")

    label("loc_135A")

    TurnDirection(0x106, 0x0, 400)

    label("loc_1361")


    ChrTalk(
        0x106,
        (
            "#050F往那边追也不会有线索的。\x01",
            "总之先回协会吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1395")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_1664")

    label("loc_13B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14D7")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1465")
    TurnDirection(0x102, 0x101, 400)
    OP_A2(0x0)

    ChrTalk(
        0x102,
        (
            "#010F博士要的东西还没有送过去呢。\x01",
            "　\x02\x03",
            "……委托的事情，\x01",
            "你有没有好好记下来啊？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#009F真、真讨厌～\x02\x03",
            "这不是清清楚楚地记下来了吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14B9")

    label("loc_1465")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F博士要的东西还没有送过去呢。\x01",
            "　\x02\x03",
            "总之现在要帮忙工作机械的改造。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14B9")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_1664")

    label("loc_14D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_155D")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14FB")
    TurnDirection(0x102, 0x1, 400)
    Jump("loc_1502")

    label("loc_14FB")

    TurnDirection(0x102, 0x0, 400)

    label("loc_1502")


    ChrTalk(
        0x102,
        (
            "#010F这边是卡鲁迪亚隧道。\x02\x03",
            "现在我们还是快去博士那里吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_1664")

    label("loc_155D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1664")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15B0")

    ChrTalk(
        0x101,
        (
            "#006F（这边是回隧道的路。\x01",
            "　现在要先去提妲家。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1649")

    label("loc_15B0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15F5")

    ChrTalk(
        0x102,
        (
            "#010F（这边是卡鲁迪亚隧道。\x01",
            "　先到提妲家去吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1649")

    label("loc_15F5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1649")

    ChrTalk(
        0x107,
        (
            "#065F（不行……\x01",
            "　这边是卡鲁迪亚隧道。）\x02\x03",
            "（先招待他们去我家吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1649")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_1664")

    Return()

    # Function_7_A09 end

    SaveToFile()

Try(main)
