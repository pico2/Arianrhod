from ED6ScenarioHelper import *

def main():
    # 卢安

    CreateScenaFile(
        FileName            = 'T2401   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2401.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60083",
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
        '扎古',                                 # 9
        '索雷诺',                               # 10
        '梅威海道方向',                         # 11
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
        'ED6_DT07/CH01460 ._CH',             # 00
        'ED6_DT07/CH01040 ._CH',             # 01
        'ED6_DT06/CH20059 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01460P._CP',             # 00
        'ED6_DT07/CH01040P._CP',             # 01
        'ED6_DT06/CH20059P._CP',             # 02
    )

    DeclNpc(
        X                   = -7120,
        Z                   = 0,
        Y                   = 37380,
        Direction           = 315,
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
        X                   = -6060,
        Z                   = 0,
        Y                   = 37610,
        Direction           = 13,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 1060,
        Z                   = 0,
        Y                   = -23220,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -2580,
        Y                   = 2000,
        Z                   = 3190,
        Range               = 2800,
        Unknown_10          = 0xFFFFF448,
        Unknown_14          = 0x578,
        Unknown_18          = 0x0,
        Unknown_1C          = 15,
    )


    DeclActor(
        TriggerX            = 1370,
        TriggerZ            = 0,
        TriggerY            = 30050,
        TriggerRange        = 1000,
        ActorX              = 1370,
        ActorZ              = 0,
        ActorY              = 30050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3480,
        TriggerZ            = 0,
        TriggerY            = 34330,
        TriggerRange        = 1000,
        ActorX              = 3480,
        ActorZ              = 0,
        ActorY              = 34330,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 6440,
        TriggerZ            = 160,
        TriggerY            = 23740,
        TriggerRange        = 1200,
        ActorX              = 6440,
        ActorZ              = 1000,
        ActorY              = 23740,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 12030,
        TriggerZ            = 0,
        TriggerY            = 18180,
        TriggerRange        = 1200,
        ActorX              = 12030,
        ActorZ              = 0,
        ActorY              = 18180,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3580,
        TriggerZ            = 0,
        TriggerY            = 7000,
        TriggerRange        = 1000,
        ActorX              = 3580,
        ActorZ              = 0,
        ActorY              = 7000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -3040,
        TriggerZ            = 0,
        TriggerY            = 8250,
        TriggerRange        = 1000,
        ActorX              = -3040,
        ActorZ              = 0,
        ActorY              = 8250,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 12390,
        TriggerZ            = 0,
        TriggerY            = 25680,
        TriggerRange        = 1000,
        ActorX              = 12390,
        ActorZ              = 500,
        ActorY              = 25680,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7430,
        TriggerZ            = 0,
        TriggerY            = 39210,
        TriggerRange        = 1000,
        ActorX              = 7430,
        ActorZ              = 700,
        ActorY              = 39210,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -8700,
        TriggerZ            = 0,
        TriggerY            = 35870,
        TriggerRange        = 1000,
        ActorX              = -8700,
        ActorZ              = 700,
        ActorY              = 35870,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -5150,
        TriggerZ            = -200,
        TriggerY            = 15360,
        TriggerRange        = 1000,
        ActorX              = -5150,
        ActorZ              = -200,
        ActorY              = 15360,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 5610,
        TriggerZ            = -280,
        TriggerY            = 16930,
        TriggerRange        = 1000,
        ActorX              = 5610,
        ActorZ              = -280,
        ActorY              = 16930,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -4980,
        TriggerZ            = -350,
        TriggerY            = 23150,
        TriggerRange        = 1000,
        ActorX              = -4980,
        ActorZ              = -350,
        ActorY              = 23150,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2F2",          # 00, 0
        "Function_1_32C",          # 01, 1
        "Function_2_397",          # 02, 2
        "Function_3_3AD",          # 03, 3
        "Function_4_55D",          # 04, 4
        "Function_5_765",          # 05, 5
        "Function_6_E17",          # 06, 6
        "Function_7_F31",          # 07, 7
        "Function_8_10AA",         # 08, 8
        "Function_9_10F8",         # 09, 9
        "Function_10_1150",        # 0A, 10
        "Function_11_11A6",        # 0B, 11
        "Function_12_11E9",        # 0C, 12
        "Function_13_123B",        # 0D, 13
        "Function_14_1280",        # 0E, 14
        "Function_15_1FDA",        # 0F, 15
    )


    def Function_0_2F2(): pass

    label("Function_0_2F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_30D")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)

    label("loc_30D")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_319"),
        (SWITCH_DEFAULT, "loc_32B"),
    )


    label("loc_319")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_328")
    OP_A2(0x420)
    Event(0, 5)

    label("loc_328")

    Jump("loc_32B")

    label("loc_32B")

    Return()

    # Function_0_2F2 end

    def Function_1_32C(): pass

    label("Function_1_32C")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE5A20, 0x30068)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_356")
    OP_B1("t2401_y")
    Jump("loc_35F")

    label("loc_356")

    OP_B1("t2401_n")

    label("loc_35F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 7)), scpexpr(EXPR_END)), "loc_396")
    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    OP_64(0x5, 0x1)
    OP_64(0x6, 0x1)
    OP_64(0x7, 0x1)
    OP_64(0x8, 0x1)
    OP_64(0x9, 0x1)
    OP_64(0xA, 0x1)
    OP_64(0xB, 0x1)

    label("loc_396")

    Return()

    # Function_1_32C end

    def Function_2_397(): pass

    label("Function_2_397")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3AC")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_397")

    label("loc_3AC")

    Return()

    # Function_2_397 end

    def Function_3_3AD(): pass

    label("Function_3_3AD")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44E")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "啊，昨天真的把我吓死了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "东边的天空变得通红，\x01",
            "在玛诺利亚村那里也看得见。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然已经采取了紧急措施，\x01",
            "但还是没有控制住火势。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BA")

    label("loc_44E")

    OP_A3(0x1)

    ChrTalk(
        0xFE,
        (
            "话说回来， \x01",
            "怎么会弄得这么乱？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "昨天来的时候这里太暗，\x01",
            "什么都看不清楚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "药草田也一塌糊涂。\x02",
    )

    CloseMessageWindow()

    label("loc_4BA")

    OP_A2(0x424)
    Call(0, 14)
    Jump("loc_559")

    label("loc_4C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_52D")

    ChrTalk(
        0xFE,
        (
            "呼……\x01",
            "已经烧得不剩什么了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我还想要是孩子们的\x01",
            "东西留下什么的话，\x01",
            "就给他们带回去呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_559")

    label("loc_52D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 7)), scpexpr(EXPR_END)), "loc_559")

    ChrTalk(
        0xFE,
        (
            "怎么样，游击士。\x01",
            "明白什么了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_559")

    TalkEnd(0x9)
    Return()

    # Function_3_3AD end

    def Function_4_55D(): pass

    label("Function_4_55D")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_657")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DA")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "烧得这么彻底，\x01",
            "看来要重新建造一间才行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看来要花费很大一笔钱，\x01",
            "特蕾莎院长打算怎么做呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64D")

    label("loc_5DA")

    OP_A3(0x0)

    ChrTalk(
        0xFE,
        (
            "特蕾莎院长也在\x01",
            "教玛诺利亚村的孩子们念书。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我也从小受她照顾。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "正是这种时候，\x01",
            "我要向她好好报恩啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64D")

    OP_A2(0x425)
    Call(0, 14)
    Jump("loc_761")

    label("loc_657")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_6A9")

    ChrTalk(
        0xFE,
        (
            "这里已经\x01",
            "大致收拾完了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "接下来就只能等待\x01",
            "你们的调查结果了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_761")

    label("loc_6A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 7)), scpexpr(EXPR_END)), "loc_761")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71F")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "我小时候\x01",
            "就认识特蕾莎院长……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "收拾火后残局\x01",
            "还真是累人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "怎么会发生\x01",
            "这么惨的事啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_761")

    label("loc_71F")


    ChrTalk(
        0xFE,
        (
            "我小时候\x01",
            "就认识特蕾莎院长……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "收拾火后残局\x01",
            "还真是累人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_761")

    TalkEnd(0x8)
    Return()

    # Function_4_55D end

    def Function_5_765(): pass

    label("Function_5_765")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_28(0x3B, 0x1, 0x1)
    OP_28(0x3B, 0x1, 0x2)
    OP_28(0x3B, 0x1, 0x4)
    OP_6D(-490, 8000, 30040, 0)
    OP_6C(45000, 0)
    SetChrPos(0x101, 850, 0, 15900, 0)
    SetChrPos(0x102, -290, 0, 15900, 0)
    FadeToBright(2000, 0)

    def lambda_7C9():
        OP_6C(0, 8000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7C9)
    OP_67(0, 17000, -10000, 0)
    OP_67(0, 9500, -10000, 5000)

    def lambda_7FB():
        OP_8E(0xFE, 0x352, 0x0, 0x60E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7FB)
    Sleep(500)

    def lambda_81B():
        OP_8E(0xFE, 0xFFFFFEDE, 0x14, 0x5E88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_81B)
    OP_6D(190, 0, 25000, 4000)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        "#003F太、太惨了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F房子完全被烧毁了啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#4P哎？你们两个……\x02",
    )

    CloseMessageWindow()
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)

    def lambda_8A7():

        label("loc_8A7")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_8A7")

    QueueWorkItem2(0x101, 1, lambda_8A7)

    def lambda_8B8():

        label("loc_8B8")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_8B8")

    QueueWorkItem2(0x102, 1, lambda_8B8)

    def lambda_8C9():
        OP_6D(-450, 40, 26930, 1500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8C9)

    def lambda_8E1():
        OP_8E(0xFE, 0xFFFFEC00, 0x78, 0x78E6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8E1)
    Sleep(600)

    def lambda_901():
        OP_8E(0xFE, 0xFFFFEC00, 0x78, 0x78E6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_901)
    WaitChrThread(0x8, 0x1)

    def lambda_921():
        OP_8E(0xFE, 0x276, 0x0, 0x6A36, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_921)
    WaitChrThread(0x9, 0x1)

    def lambda_941():
        OP_8E(0xFE, 0xFFFFFE5C, 0x1E, 0x6A36, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_941)
    WaitChrThread(0x8, 0x2)
    OP_8C(0x8, 180, 400)
    WaitChrThread(0x9, 0x2)
    OP_8C(0x9, 180, 400)

    ChrTalk(
        0x9,
        (
            "莫非你们就是\x01",
            "游击士协会派来的人？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F嗯、是的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F你们是玛诺利亚村的人吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "是啊……\x01",
            "我们正在清理瓦砾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "昨天半夜突然起火，\x01",
            "我们就慌忙赶过来救火……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "唉，如你们所见，\x01",
            "房子已经被烧了个精光啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F那、那么……\x01",
            "特蕾莎院长和孩子们呢！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "还好，大家都平安无事。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "他们现在正在\x01",
            "玛诺利亚的旅店里休息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "虽然遇到那么大的火灾，\x01",
            "但是大家最后还是平安无事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F太、太好了～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#011F嗯……真是不幸中的大幸。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我们还要在这里\x01",
            "做一下清理的工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "你们有什么打算呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F啊，我想尽快赶去旅店\x01",
            "看看那些孩子……\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x102, 0x1)
    OP_8C(0x102, 45, 400)

    ChrTalk(
        0x102,
        "#015F艾丝蒂尔，现在还不能去。\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0x1)
    OP_8C(0x101, 225, 400)

    ChrTalk(
        0x101,
        "#004F哎！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F这个现场，光是粗略一看，\x01",
            "就可以发现很多可疑的地方。\x02\x03",
            "而作为案件的线索，\x01",
            "时间一久就会消失的。\x02\x03",
            "……你的心情我很明白，\x01",
            "不过现在要以现场取证为先。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F……………………………\x02\x03",
            "#500F好吧……\x01",
            "谁让我们是游击士呢。\x02\x03",
            "#002F一定把事情查个水落石出。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯……\x01",
            "那就抓紧时间在房子周围调查一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "你们似乎商量好了吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "那就拜托你们了！\x02",
    )

    CloseMessageWindow()

    def lambda_D5B():

        label("loc_D5B")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_D5B")

    QueueWorkItem2(0x101, 1, lambda_D5B)

    def lambda_D6C():

        label("loc_D6C")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_D6C")

    QueueWorkItem2(0x102, 1, lambda_D6C)

    def lambda_D7D():
        OP_6D(190, 0, 24500, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D7D)
    OP_8C(0x9, 315, 400)

    def lambda_D9C():
        OP_8E(0xFE, 0xFFFFE67E, 0x0, 0x812E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_D9C)
    Sleep(300)
    OP_8C(0x8, 315, 400)

    def lambda_DC3():
        OP_8E(0xFE, 0xFFFFE67E, 0x0, 0x812E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_DC3)
    WaitChrThread(0x9, 0x1)
    SetChrPos(0x9, -6060, 0, 37610, 13)
    WaitChrThread(0x8, 0x1)
    SetChrPos(0x8, -7120, 0, 37380, 315)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    EventEnd(0x0)
    Return()

    # Function_5_765 end

    def Function_6_E17(): pass

    label("Function_6_E17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ED0")
    EventBegin(0x0)
    OP_6D(3480, 0, 34330, 1000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "石壁完全倒塌。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        (
            "#002F这里……\x01",
            "塌得特别厉害呢。\x02\x03",
            "还有……\x01",
            "你闻到什么古怪的味道吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F是啊。\x01",
            "这难道是……\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_F20")

    label("loc_ED0")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "石壁完全倒塌，\x01",
            "附近漂着一股刺激性气味。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_F20")

    OP_A2(0x8)
    OP_A2(0x422)
    OP_28(0x3B, 0x1, 0x10)
    Call(0, 14)
    Return()

    # Function_6_E17 end

    def Function_7_F31(): pass

    label("Function_7_F31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1047")
    EventBegin(0x0)
    OP_6D(1240, 0, 30880, 1000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门的残骸倒在地上。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        (
            "#004F哇……\x01",
            "都被烧得黑乎乎了。\x02\x03",
            "#002F哎……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F可能是我多心了……\x02\x03",
            "你觉不觉得\x01",
            "门锁的部分坏得很特别？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F……的确。\x02\x03",
            "感觉就像是\x01",
            "起火前就已经被破坏了。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_1099")

    label("loc_1047")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "已经变成残骸的门，\x01",
            "门锁的部分坏得很特别。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_1099")

    OP_A2(0x9)
    OP_A2(0x423)
    OP_28(0x3B, 0x1, 0x8)
    Call(0, 14)
    Return()

    # Function_7_F31 end

    def Function_8_10AA(): pass

    label("Function_8_10AA")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "种植的香草\x01",
            "被连根拔起且四处散落。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x3)
    TalkEnd(0xFF)
    Return()

    # Function_8_10AA end

    def Function_9_10F8(): pass

    label("Function_9_10F8")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "室外用的餐桌周围\x01",
            "散落着东倒西歪的圆木椅子。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x2)
    TalkEnd(0xFF)
    Return()

    # Function_9_10F8 end

    def Function_10_1150(): pass

    label("Function_10_1150")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "花坛里的泥土\x01",
            "在周围的地面上撒得满处都是。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x4)
    TalkEnd(0xFF)
    Return()

    # Function_10_1150 end

    def Function_11_11A6(): pass

    label("Function_11_11A6")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "暖炉用的木柴散落一地。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x5)
    TalkEnd(0xFF)
    Return()

    # Function_11_11A6 end

    def Function_12_11E9(): pass

    label("Function_12_11E9")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "倒下的牛奶桶\x01",
            "已经没有一滴牛奶剩下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x6)
    TalkEnd(0xFF)
    Return()

    # Function_12_11E9 end

    def Function_13_123B(): pass

    label("Function_13_123B")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "装食物的木桶被烧得漆黑。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x7)
    TalkEnd(0xFF)
    Return()

    # Function_13_123B end

    def Function_14_1280(): pass

    label("Function_14_1280")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FD9")
    OP_A2(0x427)
    OP_28(0x3B, 0x1, 0x20)
    OP_28(0x3B, 0x1, 0x40)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(1740, 0, 29000, 0)
    OP_6C(0, 0)
    AddParty(0x35, 0xFF)
    SetChrPos(0x101, 1070, 0, 28010, 90)
    SetChrPos(0x102, 2840, 0, 27990, 270)
    SetChrPos(0x136, 1810, 0, 26160, 45)
    SetChrFlags(0x136, 0x80)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#012F#2P好了……\x01",
            "已经发现不少线索了。\x02\x03",
            "#012F就在这附近\x01",
            "整理一下思绪吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F#1P嗯，好的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#2P首先，关于起火地点……\x01",
            "从现场可以推断不是在屋内发生的。\x02\x03",
            "在屋外的可能性很高。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#1P屋外？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F#2P嗯，是这里。\x02",
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_1419():
        OP_6D(3590, 0, 34040, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1419)

    def lambda_1431():
        OP_6C(315000, 2500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1431)

    def lambda_1441():
        OP_8E(0xFE, 0x105E, 0x0, 0x82E6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1441)
    Sleep(500)
    OP_8E(0x101, 0xC08, 0x0, 0x712A, 0xBB8, 0x0)

    def lambda_1475():
        OP_8E(0xFE, 0x10D6, 0x0, 0x7DC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1475)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 315, 400)

    ChrTalk(
        0x102,
        (
            "#012F#4P……火大概是从这一带开始，\x01",
            "然后逐渐包围了整座房子吧。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#004F啊……\x01",
            "是石壁倒塌的地方呢。\x02\x03",
            "#002F但是……\x01",
            "你怎么知道这里就是起火地点呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#4P因为这里地面的烧焦程度\x01",
            "比其它地方都要厉害。\x02\x03",
            "和周围比较一下就知道了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    Sleep(200)
    OP_8C(0x101, 90, 400)
    Sleep(200)
    OP_8C(0x101, 180, 400)
    Sleep(500)

    ChrTalk(
        0x101,
        "#002F啊，真的呢……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F#2P火势是由屋外\x01",
            "向屋内逐渐蔓延的……\x02\x03",
            "你知道这意味着什么吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#002F这、这就是说……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【森林火灾造成的意外】\x01",            # 0
            "【人为的纵火案件】\x01",                # 1
            "【照明工具的过热引起的事故】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_16CE"),
        (1, "loc_17D0"),
        (2, "loc_185E"),
        (SWITCH_DEFAULT, "loc_1989"),
    )


    label("loc_16CE")


    ChrTalk(
        0x102,
        (
            "#013F#2P虽然房屋附近的树木\x01",
            "也被烧得焦黑……\x02\x03",
            "不过我想只是火从房屋\x01",
            "蔓延到那里去了而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F那么，难道是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F很明显是有人放火。\x02\x03",
            "#012F#2P附近飘散着的这股气味……\x01",
            "是一种可燃性极高的油。\x02\x03",
            "估计是在这附近洒满油之后，\x01",
            "再点火引燃的吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x3B, 0x1)
    Jump("loc_1989")

    label("loc_17D0")


    ChrTalk(
        0x102,
        (
            "#015F#2P嗯，我也是这么想。\x02\x03",
            "#012F#2P附近飘散着的这股气味……\x01",
            "是一种可燃性极高的油。\x02\x03",
            "估计是在这附近洒满油之后，\x01",
            "再点火引燃的吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x3B, 0x2)
    Jump("loc_1989")

    label("loc_185E")


    ChrTalk(
        0x102,
        (
            "#013F#2P确实，由这个原因\x01",
            "引起火灾的可能性也不是没有。\x02\x03",
            "不过根据我的记忆，\x01",
            "这个地方应该没有照明工具。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F你、你记得还真清楚啊。\x02\x03",
            "#004F那么，难道是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#2P很明显是有人放火。\x02\x03",
            "#012F#2P附近飘散着的这股气味……\x01",
            "是一种可燃性极高的油。\x02\x03",
            "估计是在这附近洒满油之后，\x01",
            "再点火引燃的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1989")

    label("loc_1989")


    ChrTalk(
        0x101,
        "#003F怎、怎么会……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#2P还有，屋子四周乱七八糟的样子，\x01",
            "这一点也很让人觉得可疑。\x02\x03",
            "连跟救火完全没关系的\x01",
            "香草田也被弄得一塌糊涂。\x02\x03",
            "我想这一定也是人为造成的。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x136,
        "女孩的声音",
        "#2P这是……真的吗……？\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    ClearChrFlags(0x136, 0x80)

    def lambda_1A98():
        OP_6D(4110, 0, 29630, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1A98)

    def lambda_1AB0():
        OP_6C(0, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1AB0)
    OP_8C(0x101, 225, 400)
    TurnDirection(0x102, 0x136, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x101,
        "#004F啊，科洛丝！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F你也来了啊……\x02",
    )

    CloseMessageWindow()

    def lambda_1B05():
        OP_6D(2000, 0, 27550, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1B05)

    def lambda_1B1D():
        OP_8E(0xFE, 0xA50, 0x0, 0x691E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B1D)
    Sleep(300)

    def lambda_1B3D():
        OP_8E(0xFE, 0xDCA, 0x0, 0x6978, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1B3D)
    WaitChrThread(0x101, 0x1)

    def lambda_1B5D():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1B5D)
    WaitChrThread(0x102, 0x1)

    def lambda_1B70():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1B70)

    ChrTalk(
        0x136,
        (
            "#049F为什么……\x01",
            "是谁……竟然做出这种事……\x02\x03",
            "这地方充满了\x01",
            "多少无可替代的珍贵回忆……\x02\x03",
            "#046F为什么……这么……\x01",
            "残忍的事也能做出来……！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F#2P科洛丝……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F#2P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#049F…………………………\x02\x03",
            "对不起……\x01",
            "……我现在心情很乱……\x02\x03",
            "我……我…………\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x101, 0x136, 0x258, 0x3E8, 0x0)
    Fade(500)
    SetChrPos(0x136, 2060, 0, 26360, 45)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x136, 0x2)
    ClearChrFlags(0x136, 0x1)
    SetChrChipByIndex(0x136, 2)
    SetChrSubChip(0x136, 1)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#003F#2P我明白的。\x02\x03",
            "连我这个刚认识他们不久的人\x01",
            "都觉得非常难受……\x02\x03",
            "……简直无法相信。\x01",
            "竟然会有人做出这种事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#043F艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#2P不过，好在特蕾莎院长\x01",
            "和那些孩子都平安无事……\x02\x03",
            "所以呢，没事了。\x01",
            "我这样说你可以放心了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#049F……………………………\x02\x03",
            "#047F……谢谢你。\x01",
            "我觉得现在镇定了很多。\x02\x03",
            "早上我在上课的时候，\x01",
            "校长突然跑过来……\x02\x03",
            "告诉我孤儿院\x01",
            "昨晚发生了火灾……\x02\x03",
            "在来到这里之前……\x01",
            "我整个人简直快要崩溃了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F#2P是吗……\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrPos(0x136, 1810, 0, 26160, 45)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x136, 0x2)
    SetChrFlags(0x136, 0x1)
    SetChrChipByIndex(0x136, 65535)
    SetChrSubChip(0x136, 0)
    OP_0D()
    OP_94(0x1, 0x101, 0xB4, 0x1F4, 0x3E8, 0x0)

    ChrTalk(
        0x102,
        (
            "#010F#2P听说特蕾莎院长和孩子们\x01",
            "都在玛诺利亚的旅店里休息。\x02\x03",
            "现场取证也结束了， \x01",
            "就让我们陪你一起去看望他们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#048F嗯，好呢……\x01",
            "这样我真是求之不得了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#2P那么，\x01",
            "我们就赶快去玛诺利亚村吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    OP_64(0x5, 0x1)
    OP_64(0x6, 0x1)
    OP_64(0x7, 0x1)
    OP_64(0x8, 0x1)
    OP_64(0x9, 0x1)
    OP_64(0xA, 0x1)
    OP_64(0xB, 0x1)
    EventEnd(0x0)

    label("loc_1FD9")

    Return()

    # Function_14_1280 end

    def Function_15_1FDA(): pass

    label("Function_15_1FDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20B1")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2050")

    ChrTalk(
        0x102,
        (
            "#013F你的心情我可以理解，\x01",
            "不过还是等一会儿再去探望他们吧。\x02\x03",
            "现在要紧的是调查火灾的原因……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2050")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2096")

    ChrTalk(
        0x102,
        (
            "#012F（总之调查的范围\x01",
            "　还是限定在这附近比较好……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2096")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_20B1")

    Return()

    # Function_15_1FDA end

    SaveToFile()

Try(main)
