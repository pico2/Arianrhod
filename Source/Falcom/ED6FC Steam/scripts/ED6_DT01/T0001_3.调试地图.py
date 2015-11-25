from ED6ScenarioHelper import *

def main():
    # 调试地图

    CreateScenaFile(
        FileName            = 'T0001_3 ._SN',
        MapName             = 'map',
        Location            = 'T0001.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T0001   ._SN',
            'ED6_DT01/T0001_1 ._SN',
            'ED6_DT01/T0001_2 ._SN',
            'ED6_DT01/T0001_3 ._SN',
            'ED6_DT01/T0001_4 ._SN',
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
        InitFunctionIndex       = 1,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 2,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_287",          # 01, 1
        "Function_2_61B",          # 02, 2
        "Function_3_6F3",          # 03, 3
        "Function_4_A54",          # 04, 4
        "Function_5_E1E",          # 05, 5
        "Function_6_1352",         # 06, 6
        "Function_7_17A6",         # 07, 7
        "Function_8_1BC9",         # 08, 8
    )


    def Function_0_AA(): pass

    label("Function_0_AA")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪个？\x02",
        )
    )


    label("loc_B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_277")

    Menu(
        1,
        10,
        100,
        1,
        (
            "30泛用ＮＰＬ\x01",                                                 # 0
            "31我方队员和专用ＮＰＬ\x01",                                       # 1
            "32泛用ＮＰＬ和专用ＮＰＬ２＿ＡＰＬ\x01",                           # 2
            "33PT战斗艾丝蒂尔、约修亚、金、阿加特、奥利维尔\x01",               # 3
            "34PT战斗约修亚、雪拉、提妲、科洛丝\x01",                           # 4
            "35NPC战斗男女游击士、流氓、空贼\x01",                              # 5
            "36NPC战斗流氓、男女游击士２\x01",                                  # 6
            "37NPC战斗王国士兵、军官、特务兵、洛伦斯、理查德、凯诺娜\x01",      # 7
            "39坐着的角色\x01",                                                 # 8
            "取消\x01",                                                         # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_219"),
        (1, "loc_222"),
        (2, "loc_22B"),
        (3, "loc_234"),
        (4, "loc_23D"),
        (5, "loc_246"),
        (6, "loc_24F"),
        (7, "loc_258"),
        (8, "loc_261"),
        (SWITCH_DEFAULT, "loc_26A"),
    )


    label("loc_219")

    NewScene("ED6_DT01/T0030   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_222")

    NewScene("ED6_DT01/T0031   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_22B")

    NewScene("ED6_DT01/T0032   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_234")

    NewScene("ED6_DT01/T0033   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_23D")

    NewScene("ED6_DT01/T0034   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_246")

    NewScene("ED6_DT01/T0035   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_24F")

    NewScene("ED6_DT01/T0036   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_258")

    NewScene("ED6_DT01/T0037   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_261")

    NewScene("ED6_DT01/T0039   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_26A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B4")

    label("loc_277")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_AA end

    def Function_1_287(): pass

    label("Function_1_287")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪个？\x02",
        )
    )


    label("loc_291")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_60B")

    Menu(
        1,
        10,
        32,
        1,
        (
            "40魔兽列表(10000-10290)\x01",      # 0
            "41魔兽列表(10300-10590)\x01",      # 1
            "42魔兽列表(10600-10890)\x01",      # 2
            "57魔兽列表(10900-11040)\x01",      # 3
            "60魔兽列表(11050-11190)\x01",      # 4
            "43魔兽动作(10000-10050)\x01",      # 5
            "44魔兽动作(10060-10140)\x01",      # 6
            "45魔兽动作(10150-10210)\x01",      # 7
            "46魔兽动作(10220-10290)\x01",      # 8
            "47魔兽动作(10300-10380)\x01",      # 9
            "48魔兽动作(10390-10450)\x01",      # 10
            "49魔兽动作(10460-10530)\x01",      # 11
            "50魔兽动作(10540-10610)\x01",      # 12
            "51魔兽动作(10620-10690)\x01",      # 13
            "52魔兽动作(10700-10770)\x01",      # 14
            "53魔兽动作(10780-10850)\x01",      # 15
            "54魔兽动作(10860-10900)\x01",      # 16
            "55魔兽动作(10910-10940)\x01",      # 17
            "56魔兽动作(10950-10990)\x01",      # 18
            "58魔兽动作(11000-11060)\x01",      # 19
            "59魔兽动作(11070-11110)\x01",      # 20
            "61魔兽动作(11120-11150)\x01",      # 21
            "62魔兽动作(11160-11190)\x01",      # 22
            "取消\x01",                         # 23
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_538"),
        (1, "loc_541"),
        (2, "loc_54A"),
        (3, "loc_553"),
        (4, "loc_55C"),
        (5, "loc_565"),
        (6, "loc_56E"),
        (7, "loc_577"),
        (8, "loc_580"),
        (9, "loc_589"),
        (10, "loc_592"),
        (11, "loc_59B"),
        (12, "loc_5A4"),
        (13, "loc_5AD"),
        (14, "loc_5B6"),
        (15, "loc_5BF"),
        (16, "loc_5C8"),
        (17, "loc_5D1"),
        (18, "loc_5DA"),
        (19, "loc_5E3"),
        (20, "loc_5EC"),
        (21, "loc_5F5"),
        (SWITCH_DEFAULT, "loc_5FE"),
    )


    label("loc_538")

    NewScene("ED6_DT01/T0040   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_541")

    NewScene("ED6_DT01/T0041   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_54A")

    NewScene("ED6_DT01/T0042   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_553")

    NewScene("ED6_DT01/T0057   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_55C")

    NewScene("ED6_DT01/T0060   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_565")

    NewScene("ED6_DT01/T0043   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_56E")

    NewScene("ED6_DT01/T0044   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_577")

    NewScene("ED6_DT01/T0045   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_580")

    NewScene("ED6_DT01/T0046   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_589")

    NewScene("ED6_DT01/T0047   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_592")

    NewScene("ED6_DT01/T0048   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_59B")

    NewScene("ED6_DT01/T0049   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_5A4")

    NewScene("ED6_DT01/T0050   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_5AD")

    NewScene("ED6_DT01/T0051   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_5B6")

    NewScene("ED6_DT01/T0052   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_5BF")

    NewScene("ED6_DT01/T0053   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_5C8")

    NewScene("ED6_DT01/T0054   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_5D1")

    NewScene("ED6_DT01/T0055   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_5DA")

    NewScene("ED6_DT01/T0056   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_5E3")

    NewScene("ED6_DT01/T0058   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_5EC")

    NewScene("ED6_DT01/T0059   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_5F5")

    NewScene("ED6_DT01/T0061   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_5FE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_291")

    label("loc_60B")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_287 end

    def Function_2_61B(): pass

    label("Function_2_61B")


    AnonymousTalk(
        (
            scpstr(0x6),
            "这些是地图。选一个吧。\x02",
        )
    )


    label("loc_635")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6E3")

    Menu(
        1,
        10,
        100,
        1,
        (
            "洛连特地区\x01",        # 0
            "柏斯地区\x01",          # 1
            "卢安地区\x01",          # 2
            "蔡斯地区\x01",          # 3
            "格兰赛尔地区\x01",      # 4
            "其它\x01",              # 5
            "取消\x01",              # 6
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6AC"),
        (1, "loc_6B3"),
        (2, "loc_6BA"),
        (3, "loc_6C1"),
        (4, "loc_6C8"),
        (5, "loc_6CF"),
        (SWITCH_DEFAULT, "loc_6D6"),
    )


    label("loc_6AC")

    Call(3, 3)
    Jump("loc_6E0")

    label("loc_6B3")

    Call(3, 4)
    Jump("loc_6E0")

    label("loc_6BA")

    Call(3, 5)
    Jump("loc_6E0")

    label("loc_6C1")

    Call(3, 6)
    Jump("loc_6E0")

    label("loc_6C8")

    Call(3, 7)
    Jump("loc_6E0")

    label("loc_6CF")

    Call(3, 8)
    Jump("loc_6E0")

    label("loc_6D6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6E0")

    Jump("loc_635")

    label("loc_6E3")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_2_61B end

    def Function_3_6F3(): pass

    label("Function_3_6F3")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    label("loc_6FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A44")

    Menu(
        2,
        10,
        100,
        1,
        (
            "城里\x01",      # 0
            "迷宫\x01",      # 1
            "街道\x01",      # 2
            "夜\x01",        # 3
            "取消\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_746"),
        (1, "loc_843"),
        (2, "loc_972"),
        (3, "loc_9F0"),
        (SWITCH_DEFAULT, "loc_A37"),
    )


    label("loc_746")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        120,
        1,
        (
            "洛连特\x01",                  # 0
            "市长官邸\x01",                # 1
            "布莱特家\x01",                # 2
            "帕赛尔农场\x01",              # 3
            "帕赛尔农场（夜晚）\x01",      # 4
            "威尔特关所\x01",              # 5
            "飞行场\x01",                  # 6
            "布莱特家\x01",                # 7
            "格鲁纳门\x01",                # 8
            "取消\x01",                    # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7E9"),
        (1, "loc_7F2"),
        (2, "loc_7FB"),
        (3, "loc_804"),
        (4, "loc_80D"),
        (5, "loc_816"),
        (6, "loc_81F"),
        (7, "loc_828"),
        (8, "loc_831"),
        (SWITCH_DEFAULT, "loc_83A"),
    )


    label("loc_7E9")

    NewScene("ED6_DT01/T0100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_7F2")

    NewScene("ED6_DT01/T0200   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_7FB")

    NewScene("ED6_DT01/T0300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_804")

    NewScene("ED6_DT01/T0400   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_80D")

    NewScene("ED6_DT01/T0401   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_816")

    NewScene("ED6_DT01/T0500   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_81F")

    NewScene("ED6_DT01/T0700   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_828")

    NewScene("ED6_DT01/T0300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_831")

    NewScene("ED6_DT01/T0600   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_83A")

    OP_5F(0x3)
    Jump("loc_840")

    label("loc_840")

    Jump("loc_A41")

    label("loc_843")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        120,
        1,
        (
            "玛鲁加矿山\x01",              # 0
            "神秘森林\x01",                # 1
            "翡翠之塔（后半）\x01",        # 2
            "地下水路\x01",                # 3
            "翡翠之塔1F（前半）\x01",      # 4
            "翡翠之塔2F（前半）\x01",      # 5
            "翡翠之塔3F（前半）\x01",      # 6
            "翡翠之塔4F（前半）\x01",      # 7
            "翡翠之塔5F（前半）\x01",      # 8
            "取消\x01",                    # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_918"),
        (1, "loc_921"),
        (2, "loc_92A"),
        (3, "loc_933"),
        (4, "loc_93C"),
        (5, "loc_945"),
        (6, "loc_94E"),
        (7, "loc_957"),
        (8, "loc_960"),
        (SWITCH_DEFAULT, "loc_969"),
    )


    label("loc_918")

    NewScene("ED6_DT01/C0100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_921")

    NewScene("ED6_DT01/C0300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_92A")

    NewScene("ED6_DT01/C0400   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_933")

    NewScene("ED6_DT01/C0500   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_93C")

    NewScene("ED6_DT01/C0411   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_945")

    NewScene("ED6_DT01/C0412   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_94E")

    NewScene("ED6_DT01/C0413   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_957")

    NewScene("ED6_DT01/C0414   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_960")

    NewScene("ED6_DT01/C0415   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_969")

    OP_5F(0x3)
    Jump("loc_96F")

    label("loc_96F")

    Jump("loc_A41")

    label("loc_972")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        120,
        1,
        (
            "艾利兹街道\x01",      # 0
            "米尔西街道\x01",      # 1
            "玛鲁加山道\x01",      # 2
            "取消\x01",            # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9C3"),
        (1, "loc_9CF"),
        (2, "loc_9DB"),
        (SWITCH_DEFAULT, "loc_9E7"),
    )


    label("loc_9C3")

    NewScene("ED6_DT01/R0100   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_9ED")

    label("loc_9CF")

    NewScene("ED6_DT01/R0200   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_9ED")

    label("loc_9DB")

    NewScene("ED6_DT01/R0300   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_9ED")

    label("loc_9E7")

    OP_5F(0x3)
    Jump("loc_9ED")

    label("loc_9ED")

    Jump("loc_A41")

    label("loc_9F0")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        120,
        1,
        "布莱特家·外观\x01",
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A22"),
        (SWITCH_DEFAULT, "loc_A2E"),
    )


    label("loc_A22")

    NewScene("ED6_DT01/T0311   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_A34")

    label("loc_A2E")

    OP_5F(0x3)
    Jump("loc_A34")

    label("loc_A34")

    Jump("loc_A41")

    label("loc_A37")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A41")

    Jump("loc_6FD")

    label("loc_A44")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_3_6F3 end

    def Function_4_A54(): pass

    label("Function_4_A54")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    label("loc_A5E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E0E")

    Menu(
        2,
        10,
        100,
        1,
        (
            "城里\x01",      # 0
            "迷宫\x01",      # 1
            "街道\x01",      # 2
            "夜\x01",        # 3
            "取消\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_AA7"),
        (1, "loc_B9A"),
        (2, "loc_CC9"),
        (3, "loc_DA2"),
        (SWITCH_DEFAULT, "loc_DFE"),
    )


    label("loc_AA7")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "柏斯市南口\x01",              # 0
            "柏斯市民家\x01",              # 1
            "古罗尼关所\x01",              # 2
            "古罗尼关所（夜晚）\x01",      # 3
            "柏斯国际空港\x01",            # 4
            "拉文努村\x01",                # 5
            "哈肯要塞\x01",                # 6
            "湖畔的旅店\x01",              # 7
            "取消\x01",                    # 8
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B49"),
        (1, "loc_B52"),
        (2, "loc_B5B"),
        (3, "loc_B64"),
        (4, "loc_B6D"),
        (5, "loc_B76"),
        (6, "loc_B7F"),
        (7, "loc_B88"),
        (SWITCH_DEFAULT, "loc_B91"),
    )


    label("loc_B49")

    NewScene("ED6_DT01/T1100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_B52")

    NewScene("ED6_DT01/T1110   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_B5B")

    NewScene("ED6_DT01/T1300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_B64")

    NewScene("ED6_DT01/T1301   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_B6D")

    NewScene("ED6_DT01/T1102   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_B76")

    NewScene("ED6_DT01/T1200   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_B7F")

    NewScene("ED6_DT01/T1400   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_B88")

    NewScene("ED6_DT01/T1500   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_B91")

    OP_5F(0x3)
    Jump("loc_B97")

    label("loc_B97")

    Jump("loc_E0B")

    label("loc_B9A")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "琥珀之塔（后半）\x01",        # 0
            "迷雾峡谷\x01",                # 1
            "拉文努废坑\x01",              # 2
            "空贼要塞\x01",                # 3
            "琥珀之塔1F（前半）\x01",      # 4
            "琥珀之塔2F（前半）\x01",      # 5
            "琥珀之塔3F（前半）\x01",      # 6
            "琥珀之塔4F（前半）\x01",      # 7
            "琥珀之塔5F（前半）\x01",      # 8
            "取消\x01",                    # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C6F"),
        (1, "loc_C78"),
        (2, "loc_C81"),
        (3, "loc_C8A"),
        (4, "loc_C93"),
        (5, "loc_C9C"),
        (6, "loc_CA5"),
        (7, "loc_CAE"),
        (8, "loc_CB7"),
        (SWITCH_DEFAULT, "loc_CC0"),
    )


    label("loc_C6F")

    NewScene("ED6_DT01/C1200   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_C78")

    NewScene("ED6_DT01/C1400   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_C81")

    NewScene("ED6_DT01/C1100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_C8A")

    NewScene("ED6_DT01/C1300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_C93")

    NewScene("ED6_DT01/C1211   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_C9C")

    NewScene("ED6_DT01/C1212   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_CA5")

    NewScene("ED6_DT01/C1213   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_CAE")

    NewScene("ED6_DT01/C1214   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_CB7")

    NewScene("ED6_DT01/C1215   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_CC0")

    OP_5F(0x3)
    Jump("loc_CC6")

    label("loc_CC6")

    Jump("loc_E0B")

    label("loc_CC9")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "古罗尼山道\x01",            # 0
            "钢壁之路\x01",              # 1
            "东柏斯街道\x01",            # 2
            "西柏斯街道\x01",            # 3
            "安塞尔新街\x01",            # 4
            "安塞尔新街(夜晚)\x01",      # 5
            "拉文努山道\x01",            # 6
            "取消\x01",                  # 7
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D5A"),
        (1, "loc_D63"),
        (2, "loc_D6C"),
        (3, "loc_D75"),
        (4, "loc_D7E"),
        (5, "loc_D87"),
        (6, "loc_D90"),
        (SWITCH_DEFAULT, "loc_D99"),
    )


    label("loc_D5A")

    NewScene("ED6_DT01/C1500   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_D63")

    NewScene("ED6_DT01/R1300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_D6C")

    NewScene("ED6_DT01/R1100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_D75")

    NewScene("ED6_DT01/R1200   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_D7E")

    NewScene("ED6_DT01/R1400   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_D87")

    NewScene("ED6_DT01/R1403   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_D90")

    NewScene("ED6_DT01/R1500   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_D99")

    OP_5F(0x3)
    Jump("loc_D9F")

    label("loc_D9F")

    Jump("loc_E0B")

    label("loc_DA2")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        120,
        1,
        (
            "哈肯大门\x01",        # 0
            "古罗尼关所\x01",      # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_DDD"),
        (1, "loc_DE9"),
        (SWITCH_DEFAULT, "loc_DF5"),
    )


    label("loc_DDD")

    NewScene("ED6_DT01/T1401   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_DFB")

    label("loc_DE9")

    NewScene("ED6_DT01/T1311   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_DFB")

    label("loc_DF5")

    OP_5F(0x3)
    Jump("loc_DFB")

    label("loc_DFB")

    Jump("loc_E0B")

    label("loc_DFE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E0B")

    label("loc_E0B")

    Jump("loc_A5E")

    label("loc_E0E")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_4_A54 end

    def Function_5_E1E(): pass

    label("Function_5_E1E")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    label("loc_E28")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1342")

    Menu(
        2,
        10,
        100,
        1,
        (
            "城里\x01",      # 0
            "迷宫\x01",      # 1
            "街道\x01",      # 2
            "夜\x01",        # 3
            "其它\x01",      # 4
            "取消\x01",      # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E7A"),
        (1, "loc_106E"),
        (2, "loc_11AD"),
        (3, "loc_1250"),
        (4, "loc_12E0"),
        (SWITCH_DEFAULT, "loc_1332"),
    )


    label("loc_E7A")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "卢安市\x01",                         # 0
            "飞行场\x01",                         # 1
            "市长官邸\x01",                       # 2
            "王立学院 旧校舍\x01",                # 3
            "王立学院 主楼\x01",                  # 4
            "王立学院 主楼 学园祭\x01",           # 5
            "王立学院 主楼 学园祭准备\x01",       # 6
            "玛西亚孤儿院\x01",                   # 7
            "玛西亚孤儿院（火灾后）\x01",         # 8
            "玛西亚孤儿院（再建后）\x01",         # 9
            "民家\x01",                           # 10
            "店\x01",                             # 11
            "教会\x01",                           # 12
            "酒馆、赌场\x01",                     # 13
            "艾尔·雷登关所\x01",                 # 14
            "玛诺利亚村\x01",                     # 15
            "玛西亚孤儿院内部（火灾中)\x01",      # 16
            "取消\x01",                           # 17
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_FCC"),
        (1, "loc_FD5"),
        (2, "loc_FDE"),
        (3, "loc_FE7"),
        (4, "loc_FF0"),
        (5, "loc_FF9"),
        (6, "loc_1002"),
        (7, "loc_100B"),
        (8, "loc_1014"),
        (9, "loc_101D"),
        (10, "loc_1026"),
        (11, "loc_102F"),
        (12, "loc_1038"),
        (13, "loc_1041"),
        (14, "loc_104A"),
        (15, "loc_1053"),
        (16, "loc_105C"),
        (SWITCH_DEFAULT, "loc_1065"),
    )


    label("loc_FCC")

    NewScene("ED6_DT01/T2100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_FD5")

    NewScene("ED6_DT01/T2102   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_FDE")

    NewScene("ED6_DT01/T2200   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_FE7")

    NewScene("ED6_DT01/T2600   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_FF0")

    NewScene("ED6_DT01/T2510   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_FF9")

    NewScene("ED6_DT01/T2520   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1002")

    NewScene("ED6_DT01/T2530   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_100B")

    NewScene("ED6_DT01/T2400   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1014")

    NewScene("ED6_DT01/T2401   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_101D")

    NewScene("ED6_DT01/T2402   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1026")

    NewScene("ED6_DT01/T2110   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_102F")

    NewScene("ED6_DT01/T2120   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1038")

    NewScene("ED6_DT01/T2130   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1041")

    NewScene("ED6_DT01/T2131   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_104A")

    NewScene("ED6_DT01/T2700   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1053")

    NewScene("ED6_DT01/T2300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_105C")

    NewScene("ED6_DT01/T2411   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1065")

    OP_5F(0x3)
    Jump("loc_106B")

    label("loc_106B")

    Jump("loc_133F")

    label("loc_106E")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "绀碧之塔（后半）\x01",        # 0
            "巴伦诺灯塔\x01",              # 1
            "巴伦诺灯塔（夜晚）\x01",      # 2
            "旧校舍地下遗迹\x01",          # 3
            "绀碧之塔1F（前半）\x01",      # 4
            "绀碧之塔2F（前半）\x01",      # 5
            "绀碧之塔3F（前半）\x01",      # 6
            "绀碧之塔4F（前半）\x01",      # 7
            "绀碧之塔5F（前半）\x01",      # 8
            "取消\x01",                    # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1153"),
        (1, "loc_115C"),
        (2, "loc_1165"),
        (3, "loc_116E"),
        (4, "loc_1177"),
        (5, "loc_1180"),
        (6, "loc_1189"),
        (7, "loc_1192"),
        (8, "loc_119B"),
        (SWITCH_DEFAULT, "loc_11A4"),
    )


    label("loc_1153")

    NewScene("ED6_DT01/C2100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_115C")

    NewScene("ED6_DT01/C2209   ._SN", 1, 0, 0)
    IdleLoop()

    label("loc_1165")

    NewScene("ED6_DT01/C2200   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_116E")

    NewScene("ED6_DT01/C2400   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1177")

    NewScene("ED6_DT01/C2111   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1180")

    NewScene("ED6_DT01/C2112   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1189")

    NewScene("ED6_DT01/C2113   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1192")

    NewScene("ED6_DT01/C2114   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_119B")

    NewScene("ED6_DT01/C2115   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_11A4")

    OP_5F(0x3)
    Jump("loc_11AA")

    label("loc_11AA")

    Jump("loc_133F")

    label("loc_11AD")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "古罗尼山道\x01",        # 0
            "玛诺利亚间道\x01",      # 1
            "阿伊纳街道\x01",        # 2
            "梅威海道\x01",          # 3
            "街景林道\x01",          # 4
            "取消\x01",              # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_121A"),
        (1, "loc_1223"),
        (2, "loc_122C"),
        (3, "loc_1235"),
        (4, "loc_123E"),
        (SWITCH_DEFAULT, "loc_1247"),
    )


    label("loc_121A")

    NewScene("ED6_DT01/C1501   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1223")

    NewScene("ED6_DT01/R2100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_122C")

    NewScene("ED6_DT01/R2400   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1235")

    NewScene("ED6_DT01/R2200   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_123E")

    NewScene("ED6_DT01/R2300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1247")

    OP_5F(0x3)
    Jump("loc_124D")

    label("loc_124D")

    Jump("loc_133F")

    label("loc_1250")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        120,
        1,
        (
            "玛诺利亚\x01",          # 0
            "玛诺利亚海岸\x01",      # 1
            "孤儿院\x01",            # 2
            "阿伊纳街道\x01",        # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_12A7"),
        (1, "loc_12B3"),
        (2, "loc_12BF"),
        (3, "loc_12CB"),
        (SWITCH_DEFAULT, "loc_12D7"),
    )


    label("loc_12A7")

    NewScene("ED6_DT01/T2301   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_12DD")

    label("loc_12B3")

    NewScene("ED6_DT01/R2111   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_12DD")

    label("loc_12BF")

    NewScene("ED6_DT01/T2403   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_12DD")

    label("loc_12CB")

    NewScene("ED6_DT01/R2412   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_12DD")

    label("loc_12D7")

    OP_5F(0x3)
    Jump("loc_12DD")

    label("loc_12DD")

    Jump("loc_133F")

    label("loc_12E0")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        120,
        1,
        (
            "海卷轴\x01",      # 0
            "海\x01",          # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1311"),
        (1, "loc_131D"),
        (SWITCH_DEFAULT, "loc_1329"),
    )


    label("loc_1311")

    NewScene("ED6_DT01/T2103   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_132F")

    label("loc_131D")

    NewScene("ED6_DT01/T2104   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_132F")

    label("loc_1329")

    OP_5F(0x3)
    Jump("loc_132F")

    label("loc_132F")

    Jump("loc_133F")

    label("loc_1332")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_133F")

    label("loc_133F")

    Jump("loc_E28")

    label("loc_1342")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_5_E1E end

    def Function_6_1352(): pass

    label("Function_6_1352")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    label("loc_135C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1796")

    Menu(
        2,
        10,
        100,
        1,
        (
            "城里\x01",      # 0
            "迷宫\x01",      # 1
            "街道\x01",      # 2
            "夜\x01",        # 3
            "取消\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_13A5"),
        (1, "loc_1506"),
        (2, "loc_1698"),
        (3, "loc_1730"),
        (SWITCH_DEFAULT, "loc_1786"),
    )


    label("loc_13A5")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "蔡斯市\x01",                    # 0
            "蔡斯市民家１～３室内\x01",      # 1
            "中央工房　室内\x01",            # 2
            "沃尔费堡垒\x01",                # 3
            "蔡斯教会\x01",                  # 4
            "武器店\x01",                    # 5
            "拉赛尔工房\x01",                # 6
            "亚尔摩村外部\x01",              # 7
            "亚尔摩村外部（夜晚）\x01",      # 8
            "圣海姆门\x01",                  # 9
            "蔡斯市(夜晚)\x01",              # 10
            "蔡斯市（停电）\x01",            # 11
            "取消\x01",                      # 12
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1491"),
        (1, "loc_149A"),
        (2, "loc_14A3"),
        (3, "loc_14AC"),
        (4, "loc_14B5"),
        (5, "loc_14BE"),
        (6, "loc_14C7"),
        (7, "loc_14D0"),
        (8, "loc_14D9"),
        (9, "loc_14E2"),
        (10, "loc_14EB"),
        (11, "loc_14F4"),
        (SWITCH_DEFAULT, "loc_14FD"),
    )


    label("loc_1491")

    NewScene("ED6_DT01/T3100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_149A")

    NewScene("ED6_DT01/T3110   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_14A3")

    NewScene("ED6_DT01/T3111   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_14AC")

    NewScene("ED6_DT01/T3300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_14B5")

    NewScene("ED6_DT01/T3130   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_14BE")

    NewScene("ED6_DT01/T3120   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_14C7")

    NewScene("ED6_DT01/T3133   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_14D0")

    NewScene("ED6_DT01/T3200   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_14D9")

    NewScene("ED6_DT01/T3201   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_14E2")

    NewScene("ED6_DT01/T3400   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_14EB")

    NewScene("ED6_DT01/T3103   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_14F4")

    NewScene("ED6_DT01/T3106   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_14FD")

    OP_5F(0x3)
    Jump("loc_1503")

    label("loc_1503")

    Jump("loc_1793")

    label("loc_1506")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "红莲之塔（后半）\x01",                # 0
            "雷斯顿水上要塞外\x01",                # 1
            "雷斯顿水上要塞中\x01",                # 2
            "雷斯顿水上要塞外（夜晚)\x01",         # 3
            "卡鲁迪亚大钟乳洞\x01",                # 4
            "卡鲁迪亚大钟乳洞　BOSS房间\x01",      # 5
            "红莲之塔1F（前半）\x01",              # 6
            "红莲之塔2F（前半）\x01",              # 7
            "红莲之塔3F（前半）\x01",              # 8
            "红莲之塔4F（前半）\x01",              # 9
            "红莲之塔5F（前半）\x01",              # 10
            "取消\x01",                            # 11
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_162C"),
        (1, "loc_1635"),
        (2, "loc_163E"),
        (3, "loc_1647"),
        (4, "loc_1650"),
        (5, "loc_1659"),
        (6, "loc_1662"),
        (7, "loc_166B"),
        (8, "loc_1674"),
        (9, "loc_167D"),
        (10, "loc_1686"),
        (SWITCH_DEFAULT, "loc_168F"),
    )


    label("loc_162C")

    NewScene("ED6_DT01/C3500   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1635")

    NewScene("ED6_DT01/C3100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_163E")

    NewScene("ED6_DT01/C3110   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1647")

    NewScene("ED6_DT01/C3104   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1650")

    NewScene("ED6_DT01/C3300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1659")

    NewScene("ED6_DT01/C3303   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1662")

    NewScene("ED6_DT01/C3511   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_166B")

    NewScene("ED6_DT01/C3512   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1674")

    NewScene("ED6_DT01/C3513   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_167D")

    NewScene("ED6_DT01/C3514   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1686")

    NewScene("ED6_DT01/C3515   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_168F")

    OP_5F(0x3)
    Jump("loc_1695")

    label("loc_1695")

    Jump("loc_1793")

    label("loc_1698")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "佐达特军用道\x01",             # 0
            "卡鲁迪亚隧道（隧道)\x01",      # 1
            "托兰特平原道\x01",             # 2
            "利塔街道\x01",                 # 3
            "取消\x01",                     # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1703"),
        (1, "loc_170C"),
        (2, "loc_1715"),
        (3, "loc_171E"),
        (SWITCH_DEFAULT, "loc_1727"),
    )


    label("loc_1703")

    NewScene("ED6_DT01/R3300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_170C")

    NewScene("ED6_DT01/R3400   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1715")

    NewScene("ED6_DT01/R3100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_171E")

    NewScene("ED6_DT01/R3200   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1727")

    OP_5F(0x3)
    Jump("loc_172D")

    label("loc_172D")

    Jump("loc_1793")

    label("loc_1730")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        120,
        1,
        (
            "蔡斯\x01",          # 0
            "中央工房\x01",      # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1765"),
        (1, "loc_1771"),
        (SWITCH_DEFAULT, "loc_177D"),
    )


    label("loc_1765")

    NewScene("ED6_DT01/T3103   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1783")

    label("loc_1771")

    NewScene("ED6_DT01/T3104   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1783")

    label("loc_177D")

    OP_5F(0x3)
    Jump("loc_1783")

    label("loc_1783")

    Jump("loc_1793")

    label("loc_1786")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1793")

    label("loc_1793")

    Jump("loc_135C")

    label("loc_1796")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_6_1352 end

    def Function_7_17A6(): pass

    label("Function_7_17A6")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    label("loc_17B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BB9")

    Menu(
        2,
        10,
        100,
        1,
        (
            "城里\x01",      # 0
            "迷宫\x01",      # 1
            "街道\x01",      # 2
            "夜\x01",        # 3
            "取消\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_17F9"),
        (1, "loc_18CE"),
        (2, "loc_1995"),
        (3, "loc_19F2"),
        (SWITCH_DEFAULT, "loc_1BA9"),
    )


    label("loc_17F9")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "格兰赛尔\x01",            # 0
            "格兰赛尔城\x01",          # 1
            "艾尔贝离宫\x01",          # 2
            "旅馆（夜晚）\x01",        # 3
            "大圣堂（夜晚）\x01",      # 4
            "历史资料馆\x01",          # 5
            "竞技场\x01",              # 6
            "取消\x01",                # 7
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1886"),
        (1, "loc_188F"),
        (2, "loc_1898"),
        (3, "loc_18A1"),
        (4, "loc_18AA"),
        (5, "loc_18B3"),
        (6, "loc_18BC"),
        (SWITCH_DEFAULT, "loc_18C5"),
    )


    label("loc_1886")

    NewScene("ED6_DT01/T4100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_188F")

    NewScene("ED6_DT01/T4200   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1898")

    NewScene("ED6_DT01/T4300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_18A1")

    NewScene("ED6_DT01/T4133   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_18AA")

    NewScene("ED6_DT01/T4134   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_18B3")

    NewScene("ED6_DT01/T4135   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_18BC")

    NewScene("ED6_DT01/T4136   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_18C5")

    OP_5F(0x3)
    Jump("loc_18CB")

    label("loc_18CB")

    Jump("loc_1BB6")

    label("loc_18CE")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "地下水路Ａ\x01",          # 0
            "地下水路Ｂ\x01",          # 1
            "地下水路Ｃ\x01",          # 2
            "封印区域最上层\x01",      # 3
            "封印区域中层\x01",        # 4
            "封印区域最下层\x01",      # 5
            "取消\x01",                # 6
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1956"),
        (1, "loc_195F"),
        (2, "loc_1968"),
        (3, "loc_1971"),
        (4, "loc_197A"),
        (5, "loc_1983"),
        (SWITCH_DEFAULT, "loc_198C"),
    )


    label("loc_1956")

    NewScene("ED6_DT01/C4200   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_195F")

    NewScene("ED6_DT01/C4202   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1968")

    NewScene("ED6_DT01/C4204   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1971")

    NewScene("ED6_DT01/C4300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_197A")

    NewScene("ED6_DT01/C4301   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1983")

    NewScene("ED6_DT01/C4302   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_198C")

    OP_5F(0x3)
    Jump("loc_1992")

    label("loc_1992")

    Jump("loc_1BB6")

    label("loc_1995")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "艾尔贝周游道\x01",      # 0
            "庭园大道\x01",          # 1
            "取消\x01",              # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_19D7"),
        (1, "loc_19E0"),
        (SWITCH_DEFAULT, "loc_19E9"),
    )


    label("loc_19D7")

    NewScene("ED6_DT01/C4100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_19E0")

    NewScene("ED6_DT01/R4100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_19E9")

    OP_5F(0x3)
    Jump("loc_19EF")

    label("loc_19EF")

    Jump("loc_1BB6")

    label("loc_19F2")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        120,
        1,
        (
            "艾尔贝周游道 C4111\x01",         # 0
            "艾尔贝周游道 C4113\x01",         # 1
            "艾尔贝离宫 入口庭园\x01",        # 2
            "艾尔贝离宫 中庭、回廊\x01",      # 3
            "艾尔贝离宫 大厅～\x01",          # 4
            "艾尔贝离宫 客室～\x01",          # 5
            "格兰赛尔 南街区\x01",            # 6
            "格兰赛尔 东街区\x01",            # 7
            "格兰赛尔 西街区\x01",            # 8
            "格兰赛尔 北街区\x01",            # 9
            "格兰赛尔城\x01",                 # 10
            "格兰赛尔城 室内\x01",            # 11
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1B10"),
        (1, "loc_1B1C"),
        (2, "loc_1B28"),
        (3, "loc_1B34"),
        (4, "loc_1B40"),
        (5, "loc_1B4C"),
        (6, "loc_1B58"),
        (7, "loc_1B64"),
        (8, "loc_1B70"),
        (9, "loc_1B7C"),
        (10, "loc_1B88"),
        (11, "loc_1B94"),
        (SWITCH_DEFAULT, "loc_1BA0"),
    )


    label("loc_1B10")

    NewScene("ED6_DT01/C4111   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1BA6")

    label("loc_1B1C")

    NewScene("ED6_DT01/C4113   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1BA6")

    label("loc_1B28")

    NewScene("ED6_DT01/T4302   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1BA6")

    label("loc_1B34")

    NewScene("ED6_DT01/T4303   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1BA6")

    label("loc_1B40")

    NewScene("ED6_DT01/T4312   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1BA6")

    label("loc_1B4C")

    NewScene("ED6_DT01/T4313   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1BA6")

    label("loc_1B58")

    NewScene("ED6_DT01/T4150   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1BA6")

    label("loc_1B64")

    NewScene("ED6_DT01/T4151   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1BA6")

    label("loc_1B70")

    NewScene("ED6_DT01/T4152   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1BA6")

    label("loc_1B7C")

    NewScene("ED6_DT01/T4153   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1BA6")

    label("loc_1B88")

    NewScene("ED6_DT01/T4203   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1BA6")

    label("loc_1B94")

    NewScene("ED6_DT01/T4250   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1BA6")

    label("loc_1BA0")

    OP_5F(0x3)
    Jump("loc_1BA6")

    label("loc_1BA6")

    Jump("loc_1BB6")

    label("loc_1BA9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BB6")

    label("loc_1BB6")

    Jump("loc_17B0")

    label("loc_1BB9")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_7_17A6 end

    def Function_8_1BC9(): pass

    label("Function_8_1BC9")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    label("loc_1BD3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D34")

    Menu(
        2,
        10,
        100,
        1,
        (
            "船\x01",        # 0
            "天空\x01",      # 1
            "取消\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1C0A"),
        (1, "loc_1CE5"),
        (SWITCH_DEFAULT, "loc_1D24"),
    )


    label("loc_1C0A")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "定期船\x01",          # 0
            "定期船绿色\x01",      # 1
            "工房船\x01",          # 2
            "空贼艇\x01",          # 3
            "军用两栖舰\x01",      # 4
            "埃尔赛尤外\x01",      # 5
            "特务艇\x01",          # 6
            "空内装置\x01",        # 7
            "取消\x01",            # 8
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1C94"),
        (1, "loc_1C9D"),
        (2, "loc_1CA6"),
        (3, "loc_1CAF"),
        (4, "loc_1CB8"),
        (5, "loc_1CC1"),
        (6, "loc_1CCA"),
        (7, "loc_1CD3"),
        (SWITCH_DEFAULT, "loc_1CDC"),
    )


    label("loc_1C94")

    NewScene("ED6_DT01/E0000   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1C9D")

    NewScene("ED6_DT01/E0001   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1CA6")

    NewScene("ED6_DT01/E0002   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1CAF")

    NewScene("ED6_DT01/E0100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1CB8")

    NewScene("ED6_DT01/E0200   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1CC1")

    NewScene("ED6_DT01/E0300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1CCA")

    NewScene("ED6_DT01/E0400   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1CD3")

    NewScene("ED6_DT01/E0111   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1CDC")

    OP_5F(0x3)
    Jump("loc_1CE2")

    label("loc_1CE2")

    Jump("loc_1D31")

    label("loc_1CE5")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪里？\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "天空\x01",      # 0
            "取消\x01",      # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1D12"),
        (SWITCH_DEFAULT, "loc_1D1B"),
    )


    label("loc_1D12")

    NewScene("ED6_DT01/E0500   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1D1B")

    OP_5F(0x3)
    Jump("loc_1D21")

    label("loc_1D21")

    Jump("loc_1D31")

    label("loc_1D24")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D31")

    label("loc_1D31")

    Jump("loc_1BD3")

    label("loc_1D34")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_8_1BC9 end

    SaveToFile()

Try(main)
