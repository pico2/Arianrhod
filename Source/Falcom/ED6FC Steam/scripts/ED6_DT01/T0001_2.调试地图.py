from ED6ScenarioHelper import *

def main():
    # 调试地图

    CreateScenaFile(
        FileName            = 'T0001_2 ._SN',
        MapName             = 'map',
        Location            = 'T0001.x',
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
        InitFunctionIndex       = 1,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 2,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_15E",          # 01, 1
        "Function_2_28A",          # 02, 2
        "Function_3_328",          # 03, 3
        "Function_4_421",          # 04, 4
        "Function_5_506",          # 05, 5
        "Function_6_5DE",          # 06, 6
        "Function_7_6F8",          # 07, 7
        "Function_8_7D0",          # 08, 8
        "Function_9_8A8",          # 09, 9
        "Function_10_A45",         # 0A, 10
        "Function_11_B21",         # 0B, 11
        "Function_12_BF9",         # 0C, 12
        "Function_13_CD1",         # 0D, 13
        "Function_14_DA9",         # 0E, 14
        "Function_15_E81",         # 0F, 15
        "Function_16_F59",         # 10, 16
        "Function_17_1031",        # 11, 17
        "Function_18_1109",        # 12, 18
        "Function_19_11E5",        # 13, 19
        "Function_20_12BD",        # 14, 20
        "Function_21_143F",        # 15, 21
        "Function_22_1517",        # 16, 22
        "Function_23_1662",        # 17, 23
        "Function_24_17E9",        # 18, 24
        "Function_25_18C1",        # 19, 25
        "Function_26_1999",        # 1A, 26
        "Function_27_1A80",        # 1B, 27
        "Function_28_1B97",        # 1C, 28
        "Function_29_1C6F",        # 1D, 29
        "Function_30_1DA2",        # 1E, 30
        "Function_31_1E7A",        # 1F, 31
        "Function_32_1FE3",        # 20, 32
        "Function_33_20BB",        # 21, 33
        "Function_34_2193",        # 22, 34
        "Function_35_2290",        # 23, 35
        "Function_36_2432",        # 24, 36
        "Function_37_250A",        # 25, 37
        "Function_38_2656",        # 26, 38
        "Function_39_27BF",        # 27, 39
        "Function_40_2897",        # 28, 40
        "Function_41_296F",        # 29, 41
        "Function_42_2A47",        # 2A, 42
        "Function_43_2B1F",        # 2B, 43
        "Function_44_2BF7",        # 2C, 44
        "Function_45_2CE1",        # 2D, 45
        "Function_46_2DBB",        # 2E, 46
        "Function_47_2E93",        # 2F, 47
        "Function_48_30F2",        # 30, 48
    )


    def Function_0_AA(): pass

    label("Function_0_AA")


    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    label("loc_B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14E")

    Menu(
        1,
        10,
        100,
        1,
        (
            "洛连特\x01",        # 0
            "柏斯\x01",          # 1
            "卢安\x01",          # 2
            "蔡斯\x01",          # 3
            "格兰赛尔\x01",      # 4
            "其它\x01",          # 5
            "取消\x01",          # 6
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_117"),
        (1, "loc_11E"),
        (2, "loc_125"),
        (3, "loc_12C"),
        (4, "loc_133"),
        (5, "loc_13A"),
        (SWITCH_DEFAULT, "loc_141"),
    )


    label("loc_117")

    Call(2, 1)
    Jump("loc_14B")

    label("loc_11E")

    Call(2, 9)
    Jump("loc_14B")

    label("loc_125")

    Call(2, 20)
    Jump("loc_14B")

    label("loc_12C")

    Call(2, 27)
    Jump("loc_14B")

    label("loc_133")

    Call(2, 35)
    Jump("loc_14B")

    label("loc_13A")

    Call(2, 46)
    Jump("loc_14B")

    label("loc_141")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14B")

    Jump("loc_B4")

    label("loc_14E")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_AA end

    def Function_1_15E(): pass

    label("Function_1_15E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27C")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        2,
        10,
        80,
        1,
        (
            "玛鲁加矿山\x01",              # 0
            "神秘森林\x01",                # 1
            "翡翠之塔\x01",                # 2
            "艾利兹街道\x01",              # 3
            "米尔西街道\x01",              # 4
            "玛鲁加山道\x01",              # 5
            "地下水路\x01",                # 6
            "帕赛尔农场（夜晚）\x01",      # 7
            "威尔特桥关所外部\x01",        # 8
            "取消\x01",                    # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_21E"),
        (1, "loc_225"),
        (2, "loc_22C"),
        (3, "loc_233"),
        (4, "loc_23A"),
        (5, "loc_241"),
        (6, "loc_248"),
        (7, "loc_24F"),
        (8, "loc_25F"),
        (SWITCH_DEFAULT, "loc_26F"),
    )


    label("loc_21E")

    Call(2, 2)
    Jump("loc_279")

    label("loc_225")

    Call(2, 3)
    Jump("loc_279")

    label("loc_22C")

    Call(2, 4)
    Jump("loc_279")

    label("loc_233")

    Call(2, 5)
    Jump("loc_279")

    label("loc_23A")

    Call(2, 6)
    Jump("loc_279")

    label("loc_241")

    Call(2, 7)
    Jump("loc_279")

    label("loc_248")

    Call(2, 8)
    Jump("loc_279")

    label("loc_24F")

    Battle(0x393, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_279")

    label("loc_25F")

    Battle(0x3ED, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_279")

    label("loc_26F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_279")

    Jump("Function_1_15E")

    label("loc_27C")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_15E end

    def Function_2_28A(): pass

    label("Function_2_28A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31A")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C0100_01\x01",      # 0
            "C0100_02\x01",      # 1
            "C0100_03\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2DD"),
        (1, "loc_2ED"),
        (2, "loc_2FD"),
        (SWITCH_DEFAULT, "loc_30D"),
    )


    label("loc_2DD")

    Battle(0x56, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_317")

    label("loc_2ED")

    Battle(0x57, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_317")

    label("loc_2FD")

    Battle(0x58, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_317")

    label("loc_30D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_317")

    Jump("Function_2_28A")

    label("loc_31A")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_2_28A end

    def Function_3_328(): pass

    label("Function_3_328")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_413")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C0100_01\x01",          # 0
            "C0100_02\x01",          # 1
            "C0100_03\x01",          # 2
            "C0100_20\x01",          # 3
            "C0100_11\x01",          # 4
            "BTL_EVENT001\x01",      # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3A6"),
        (1, "loc_3B6"),
        (2, "loc_3C6"),
        (3, "loc_3D6"),
        (4, "loc_3E6"),
        (5, "loc_3F6"),
        (SWITCH_DEFAULT, "loc_406"),
    )


    label("loc_3A6")

    Battle(0x3E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_410")

    label("loc_3B6")

    Battle(0x3F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_410")

    label("loc_3C6")

    Battle(0x40, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_410")

    label("loc_3D6")

    Battle(0x51, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_410")

    label("loc_3E6")

    Battle(0x48, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_410")

    label("loc_3F6")

    Battle(0x385, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_410")

    label("loc_406")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_410")

    Jump("Function_3_328")

    label("loc_413")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_3_328 end

    def Function_4_421(): pass

    label("Function_4_421")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F8")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C0400_01\x01",          # 0
            "C0400_02\x01",          # 1
            "C0400_07\x01",          # 2
            "C0400_13\x01",          # 3
            "C0400_10\x01",          # 4
            "BTL_EVENT002\x01",      # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_49B"),
        (1, "loc_4AB"),
        (2, "loc_4BB"),
        (3, "loc_4CB"),
        (4, "loc_4DB"),
        (SWITCH_DEFAULT, "loc_4EB"),
    )


    label("loc_49B")

    Battle(0x31, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_4F5")

    label("loc_4AB")

    Battle(0x32, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_4F5")

    label("loc_4BB")

    Battle(0x37, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_4F5")

    label("loc_4CB")

    Battle(0x3D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_4F5")

    label("loc_4DB")

    Battle(0x3A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_4F5")

    label("loc_4EB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4F5")

    Jump("Function_4_421")

    label("loc_4F8")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_4_421 end

    def Function_5_506(): pass

    label("Function_5_506")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D0")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R0100_02\x01",      # 0
            "R0100_05\x01",      # 1
            "R0100_09\x01",      # 2
            "R0100_11\x01",      # 3
            "R0100_14\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_573"),
        (1, "loc_583"),
        (2, "loc_593"),
        (3, "loc_5A3"),
        (4, "loc_5B3"),
        (SWITCH_DEFAULT, "loc_5C3"),
    )


    label("loc_573")

    Battle(0x15, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_5CD")

    label("loc_583")

    Battle(0x18, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_5CD")

    label("loc_593")

    Battle(0x1C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_5CD")

    label("loc_5A3")

    Battle(0x1E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_5CD")

    label("loc_5B3")

    Battle(0x21, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_5CD")

    label("loc_5C3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5CD")

    Jump("Function_5_506")

    label("loc_5D0")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_5_506 end

    def Function_6_5DE(): pass

    label("Function_6_5DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6EA")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R0200_02\x01",          # 0
            "R0200_06\x01",          # 1
            "R0200_09\x01",          # 2
            "R0200_11\x01",          # 3
            "R0200_17\x01",          # 4
            "BTL_QUEST003\x01",      # 5
            "BTL_QUEST004\x01",      # 6
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_66D"),
        (1, "loc_67D"),
        (2, "loc_68D"),
        (3, "loc_69D"),
        (4, "loc_6AD"),
        (5, "loc_6BD"),
        (6, "loc_6CD"),
        (SWITCH_DEFAULT, "loc_6DD"),
    )


    label("loc_66D")

    Battle(0x7A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_6E7")

    label("loc_67D")

    Battle(0x7E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_6E7")

    label("loc_68D")

    Battle(0x81, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_6E7")

    label("loc_69D")

    Battle(0x83, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_6E7")

    label("loc_6AD")

    Battle(0x89, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_6E7")

    label("loc_6BD")

    Battle(0x3EB, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_6E7")

    label("loc_6CD")

    Battle(0x3EC, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_6E7")

    label("loc_6DD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6E7")

    Jump("Function_6_5DE")

    label("loc_6EA")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_6_5DE end

    def Function_7_6F8(): pass

    label("Function_7_6F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7C2")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R0300_02\x01",      # 0
            "R0300_06\x01",      # 1
            "R0300_09\x01",      # 2
            "R0300_12\x01",      # 3
            "R0300_17\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_765"),
        (1, "loc_775"),
        (2, "loc_785"),
        (3, "loc_795"),
        (4, "loc_7A5"),
        (SWITCH_DEFAULT, "loc_7B5"),
    )


    label("loc_765")

    Battle(0x65, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_7BF")

    label("loc_775")

    Battle(0x69, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_7BF")

    label("loc_785")

    Battle(0x6C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_7BF")

    label("loc_795")

    Battle(0x6F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_7BF")

    label("loc_7A5")

    Battle(0x74, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_7BF")

    label("loc_7B5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7BF")

    Jump("Function_7_6F8")

    label("loc_7C2")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_7_6F8 end

    def Function_8_7D0(): pass

    label("Function_8_7D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_89A")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C0500_01\x01",      # 0
            "C0500_02\x01",      # 1
            "C0500_03\x01",      # 2
            "C0500_04\x01",      # 3
            "C0500_07\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_83D"),
        (1, "loc_84D"),
        (2, "loc_85D"),
        (3, "loc_86D"),
        (4, "loc_87D"),
        (SWITCH_DEFAULT, "loc_88D"),
    )


    label("loc_83D")

    Battle(0x2A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_897")

    label("loc_84D")

    Battle(0x2B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_897")

    label("loc_85D")

    Battle(0x2C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_897")

    label("loc_86D")

    Battle(0x2D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_897")

    label("loc_87D")

    Battle(0x30, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_897")

    label("loc_88D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_897")

    Jump("Function_8_7D0")

    label("loc_89A")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_8_7D0 end

    def Function_9_8A8(): pass

    label("Function_9_8A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A37")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        2,
        10,
        60,
        1,
        (
            "琥珀之塔\x01",                        # 0
            "空贼要塞\x01",                        # 1
            "迷雾峡谷\x01",                        # 2
            "古罗尼山顶\x01",                      # 3
            "东柏斯街道\x01",                      # 4
            "西柏斯街道\x01",                      # 5
            "钢壁之路\x01",                        # 6
            "安塞尔新街\x01",                      # 7
            "拉文努山道\x01",                      # 8
            "拉文努废坑\x01",                      # 9
            "拉文努废坑中央广场（吉尔）\x01",      # 10
            "空贼要塞（多伦）\x01",                # 11
            "古罗尼关所外部（犬）\x01",            # 12
            "取消\x01",                            # 13
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9B4"),
        (1, "loc_9BB"),
        (2, "loc_9C2"),
        (3, "loc_9C9"),
        (4, "loc_9D0"),
        (5, "loc_9D7"),
        (6, "loc_9DE"),
        (7, "loc_9E5"),
        (8, "loc_9EC"),
        (9, "loc_9F3"),
        (10, "loc_9FA"),
        (11, "loc_A0A"),
        (12, "loc_A1A"),
        (SWITCH_DEFAULT, "loc_A2A"),
    )


    label("loc_9B4")

    Call(2, 10)
    Jump("loc_A34")

    label("loc_9BB")

    Call(2, 11)
    Jump("loc_A34")

    label("loc_9C2")

    Call(2, 12)
    Jump("loc_A34")

    label("loc_9C9")

    Call(2, 13)
    Jump("loc_A34")

    label("loc_9D0")

    Call(2, 14)
    Jump("loc_A34")

    label("loc_9D7")

    Call(2, 15)
    Jump("loc_A34")

    label("loc_9DE")

    Call(2, 16)
    Jump("loc_A34")

    label("loc_9E5")

    Call(2, 17)
    Jump("loc_A34")

    label("loc_9EC")

    Call(2, 18)
    Jump("loc_A34")

    label("loc_9F3")

    Call(2, 19)
    Jump("loc_A34")

    label("loc_9FA")

    Battle(0x387, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_A34")

    label("loc_A0A")

    Battle(0x389, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_A34")

    label("loc_A1A")

    Battle(0x396, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_A34")

    label("loc_A2A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A34")

    Jump("Function_9_8A8")

    label("loc_A37")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_9_8A8 end

    def Function_10_A45(): pass

    label("Function_10_A45")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B13")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C1211_01\x01",          # 0
            "C1211_02\x01",          # 1
            "C1211_03\x01",          # 2
            "C1211_04\x01",          # 3
            "BTL_QUEST007\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_AB6"),
        (1, "loc_AC6"),
        (2, "loc_AD6"),
        (3, "loc_AE6"),
        (4, "loc_AF6"),
        (SWITCH_DEFAULT, "loc_B06"),
    )


    label("loc_AB6")

    Battle(0x8E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_B10")

    label("loc_AC6")

    Battle(0x8F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_B10")

    label("loc_AD6")

    Battle(0x90, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_B10")

    label("loc_AE6")

    Battle(0x91, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_B10")

    label("loc_AF6")

    Battle(0x3EF, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_B10")

    label("loc_B06")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B10")

    Jump("Function_10_A45")

    label("loc_B13")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_10_A45 end

    def Function_11_B21(): pass

    label("Function_11_B21")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BEB")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C1300_01\x01",      # 0
            "C1300_02\x01",      # 1
            "C1300_03\x01",      # 2
            "C1300_04\x01",      # 3
            "C1300_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B8E"),
        (1, "loc_B9E"),
        (2, "loc_BAE"),
        (3, "loc_BBE"),
        (4, "loc_BCE"),
        (SWITCH_DEFAULT, "loc_BDE"),
    )


    label("loc_B8E")

    Battle(0xA1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_BE8")

    label("loc_B9E")

    Battle(0xA2, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_BE8")

    label("loc_BAE")

    Battle(0xA3, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_BE8")

    label("loc_BBE")

    Battle(0xA4, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_BE8")

    label("loc_BCE")

    Battle(0xA5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_BE8")

    label("loc_BDE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BE8")

    Jump("Function_11_B21")

    label("loc_BEB")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_11_B21 end

    def Function_12_BF9(): pass

    label("Function_12_BF9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CC3")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C1400_01\x01",      # 0
            "C1400_02\x01",      # 1
            "C1400_03\x01",      # 2
            "C1400_04\x01",      # 3
            "C1400_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C66"),
        (1, "loc_C76"),
        (2, "loc_C86"),
        (3, "loc_C96"),
        (4, "loc_CA6"),
        (SWITCH_DEFAULT, "loc_CB6"),
    )


    label("loc_C66")

    Battle(0xB5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_CC0")

    label("loc_C76")

    Battle(0xB6, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_CC0")

    label("loc_C86")

    Battle(0xB7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_CC0")

    label("loc_C96")

    Battle(0xB8, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_CC0")

    label("loc_CA6")

    Battle(0xB9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_CC0")

    label("loc_CB6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CC0")

    Jump("Function_12_BF9")

    label("loc_CC3")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_12_BF9 end

    def Function_13_CD1(): pass

    label("Function_13_CD1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D9B")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C1500_01\x01",      # 0
            "C1500_02\x01",      # 1
            "C1500_03\x01",      # 2
            "C1500_04\x01",      # 3
            "C1500_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D3E"),
        (1, "loc_D4E"),
        (2, "loc_D5E"),
        (3, "loc_D6E"),
        (4, "loc_D7E"),
        (SWITCH_DEFAULT, "loc_D8E"),
    )


    label("loc_D3E")

    Battle(0xC9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_D98")

    label("loc_D4E")

    Battle(0xCA, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_D98")

    label("loc_D5E")

    Battle(0xCB, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_D98")

    label("loc_D6E")

    Battle(0xCC, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_D98")

    label("loc_D7E")

    Battle(0xCD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_D98")

    label("loc_D8E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D98")

    Jump("Function_13_CD1")

    label("loc_D9B")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_13_CD1 end

    def Function_14_DA9(): pass

    label("Function_14_DA9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E73")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R1100_01\x01",      # 0
            "R1100_02\x01",      # 1
            "R1100_20\x01",      # 2
            "R1100_04\x01",      # 3
            "R1100_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E16"),
        (1, "loc_E26"),
        (2, "loc_E36"),
        (3, "loc_E46"),
        (4, "loc_E56"),
        (SWITCH_DEFAULT, "loc_E66"),
    )


    label("loc_E16")

    Battle(0xDD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_E70")

    label("loc_E26")

    Battle(0xDE, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_E70")

    label("loc_E36")

    Battle(0xF0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_E70")

    label("loc_E46")

    Battle(0xE0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_E70")

    label("loc_E56")

    Battle(0xE1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_E70")

    label("loc_E66")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E70")

    Jump("Function_14_DA9")

    label("loc_E73")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_14_DA9 end

    def Function_15_E81(): pass

    label("Function_15_E81")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F4B")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R1200_01\x01",      # 0
            "R1200_02\x01",      # 1
            "R1200_03\x01",      # 2
            "R1200_04\x01",      # 3
            "R1200_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_EEE"),
        (1, "loc_EFE"),
        (2, "loc_F0E"),
        (3, "loc_F1E"),
        (4, "loc_F2E"),
        (SWITCH_DEFAULT, "loc_F3E"),
    )


    label("loc_EEE")

    Battle(0xF1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_F48")

    label("loc_EFE")

    Battle(0xF2, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_F48")

    label("loc_F0E")

    Battle(0xF3, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_F48")

    label("loc_F1E")

    Battle(0xF4, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_F48")

    label("loc_F2E")

    Battle(0xF5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_F48")

    label("loc_F3E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F48")

    Jump("Function_15_E81")

    label("loc_F4B")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_15_E81 end

    def Function_16_F59(): pass

    label("Function_16_F59")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1023")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R1300_01\x01",      # 0
            "R1300_02\x01",      # 1
            "R1300_03\x01",      # 2
            "R1300_04\x01",      # 3
            "R1300_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_FC6"),
        (1, "loc_FD6"),
        (2, "loc_FE6"),
        (3, "loc_FF6"),
        (4, "loc_1006"),
        (SWITCH_DEFAULT, "loc_1016"),
    )


    label("loc_FC6")

    Battle(0x105, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1020")

    label("loc_FD6")

    Battle(0x106, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1020")

    label("loc_FE6")

    Battle(0x107, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1020")

    label("loc_FF6")

    Battle(0x108, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1020")

    label("loc_1006")

    Battle(0x109, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1020")

    label("loc_1016")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1020")

    Jump("Function_16_F59")

    label("loc_1023")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_16_F59 end

    def Function_17_1031(): pass

    label("Function_17_1031")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10FB")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R1400_01\x01",      # 0
            "R1400_02\x01",      # 1
            "R1400_03\x01",      # 2
            "R1400_04\x01",      # 3
            "R1400_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_109E"),
        (1, "loc_10AE"),
        (2, "loc_10BE"),
        (3, "loc_10CE"),
        (4, "loc_10DE"),
        (SWITCH_DEFAULT, "loc_10EE"),
    )


    label("loc_109E")

    Battle(0x119, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_10F8")

    label("loc_10AE")

    Battle(0x11A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_10F8")

    label("loc_10BE")

    Battle(0x11B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_10F8")

    label("loc_10CE")

    Battle(0x11C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_10F8")

    label("loc_10DE")

    Battle(0x11D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_10F8")

    label("loc_10EE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10F8")

    Jump("Function_17_1031")

    label("loc_10FB")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_17_1031 end

    def Function_18_1109(): pass

    label("Function_18_1109")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11D7")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R1500_01\x01",          # 0
            "R1500_02\x01",          # 1
            "R1500_03\x01",          # 2
            "R1500_04\x01",          # 3
            "BTL_QUEST006\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_117A"),
        (1, "loc_118A"),
        (2, "loc_119A"),
        (3, "loc_11AA"),
        (4, "loc_11BA"),
        (SWITCH_DEFAULT, "loc_11CA"),
    )


    label("loc_117A")

    Battle(0x12D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_11D4")

    label("loc_118A")

    Battle(0x12E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_11D4")

    label("loc_119A")

    Battle(0x12F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_11D4")

    label("loc_11AA")

    Battle(0x130, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_11D4")

    label("loc_11BA")

    Battle(0x3EE, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_11D4")

    label("loc_11CA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11D4")

    Jump("Function_18_1109")

    label("loc_11D7")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_18_1109 end

    def Function_19_11E5(): pass

    label("Function_19_11E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12AF")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C1100_01\x01",      # 0
            "C1100_02\x01",      # 1
            "C1100_03\x01",      # 2
            "C1100_04\x01",      # 3
            "C1100_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1252"),
        (1, "loc_1262"),
        (2, "loc_1272"),
        (3, "loc_1282"),
        (4, "loc_1292"),
        (SWITCH_DEFAULT, "loc_12A2"),
    )


    label("loc_1252")

    Battle(0x141, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_12AC")

    label("loc_1262")

    Battle(0x142, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_12AC")

    label("loc_1272")

    Battle(0x143, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_12AC")

    label("loc_1282")

    Battle(0x144, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_12AC")

    label("loc_1292")

    Battle(0x145, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_12AC")

    label("loc_12A2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12AC")

    Jump("Function_19_11E5")

    label("loc_12AF")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_19_11E5 end

    def Function_20_12BD(): pass

    label("Function_20_12BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1431")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        2,
        10,
        60,
        1,
        (
            "玛诺利亚间道\x01",                  # 0
            "梅威海道\x01",                      # 1
            "街景林道\x01",                      # 2
            "阿伊纳街道\x01",                    # 3
            "绀碧之塔\x01",                      # 4
            "卢安市长官邸内部（事件）\x01",      # 5
            "巴伦诺灯塔夜晚（事件）\x01",        # 6
            "卢安仓库内部（渡鸦帮）\x01",        # 7
            "旧校舍内部（事件）\x01",            # 8
            "巴伦诺灯塔白天（任务）\x01",        # 9
            "取消\x01",                          # 10
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_13BA"),
        (1, "loc_13C1"),
        (2, "loc_13C8"),
        (3, "loc_13CF"),
        (4, "loc_13D6"),
        (5, "loc_13DD"),
        (6, "loc_13ED"),
        (7, "loc_13F4"),
        (8, "loc_1404"),
        (9, "loc_1414"),
        (SWITCH_DEFAULT, "loc_1424"),
    )


    label("loc_13BA")

    Call(2, 21)
    Jump("loc_142E")

    label("loc_13C1")

    Call(2, 22)
    Jump("loc_142E")

    label("loc_13C8")

    Call(2, 23)
    Jump("loc_142E")

    label("loc_13CF")

    Call(2, 24)
    Jump("loc_142E")

    label("loc_13D6")

    Call(2, 25)
    Jump("loc_142E")

    label("loc_13DD")

    Battle(0x394, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_142E")

    label("loc_13ED")

    Call(2, 26)
    Jump("loc_142E")

    label("loc_13F4")

    Battle(0x397, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_142E")

    label("loc_1404")

    Battle(0x399, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_142E")

    label("loc_1414")

    Battle(0x3F2, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_142E")

    label("loc_1424")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_142E")

    Jump("Function_20_12BD")

    label("loc_1431")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_20_12BD end

    def Function_21_143F(): pass

    label("Function_21_143F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1509")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R2100_01\x01",      # 0
            "R2100_02\x01",      # 1
            "R2100_03\x01",      # 2
            "R2100_04\x01",      # 3
            "R2100_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_14AC"),
        (1, "loc_14BC"),
        (2, "loc_14CC"),
        (3, "loc_14DC"),
        (4, "loc_14EC"),
        (SWITCH_DEFAULT, "loc_14FC"),
    )


    label("loc_14AC")

    Battle(0x169, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1506")

    label("loc_14BC")

    Battle(0x16A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1506")

    label("loc_14CC")

    Battle(0x16B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1506")

    label("loc_14DC")

    Battle(0x16C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1506")

    label("loc_14EC")

    Battle(0x16D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1506")

    label("loc_14FC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1506")

    Jump("Function_21_143F")

    label("loc_1509")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_21_143F end

    def Function_22_1517(): pass

    label("Function_22_1517")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1654")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R2200_01主要\x01",            # 0
            "R2200_02\x01",                # 1
            "R2201_01沙滩\x01",            # 2
            "R2201_02\x01",                # 3
            "R2202_01主要(傍晚)\x01",      # 4
            "R2202_02\x01",                # 5
            "R2203_01沙滩(傍晚)\x01",      # 6
            "R2203_02\x01",                # 7
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_15C7"),
        (1, "loc_15D7"),
        (2, "loc_15E7"),
        (3, "loc_15F7"),
        (4, "loc_1607"),
        (5, "loc_1617"),
        (6, "loc_1627"),
        (7, "loc_1637"),
        (SWITCH_DEFAULT, "loc_1647"),
    )


    label("loc_15C7")

    Battle(0x17D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1651")

    label("loc_15D7")

    Battle(0x17E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1651")

    label("loc_15E7")

    Battle(0x187, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1651")

    label("loc_15F7")

    Battle(0x188, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1651")

    label("loc_1607")

    Battle(0x321, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1651")

    label("loc_1617")

    Battle(0x322, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1651")

    label("loc_1627")

    Battle(0x32B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1651")

    label("loc_1637")

    Battle(0x32C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1651")

    label("loc_1647")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1651")

    Jump("Function_22_1517")

    label("loc_1654")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_22_1517 end

    def Function_23_1662(): pass

    label("Function_23_1662")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17DB")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R2300_01\x01",            # 0
            "R2300_02\x01",            # 1
            "R2300_03\x01",            # 2
            "R2300_04\x01",            # 3
            "R2300_05\x01",            # 4
            "R2301_01(傍晚)\x01",      # 5
            "R2301_02(傍晚)\x01",      # 6
            "R2301_03(傍晚)\x01",      # 7
            "R2301_04(傍晚)\x01",      # 8
            "R2301_05(傍晚)\x01",      # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_172E"),
        (1, "loc_173E"),
        (2, "loc_174E"),
        (3, "loc_175E"),
        (4, "loc_176E"),
        (5, "loc_177E"),
        (6, "loc_178E"),
        (7, "loc_179E"),
        (8, "loc_17AE"),
        (9, "loc_17BE"),
        (SWITCH_DEFAULT, "loc_17CE"),
    )


    label("loc_172E")

    Battle(0x191, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_17D8")

    label("loc_173E")

    Battle(0x192, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_17D8")

    label("loc_174E")

    Battle(0x193, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_17D8")

    label("loc_175E")

    Battle(0x194, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_17D8")

    label("loc_176E")

    Battle(0x195, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_17D8")

    label("loc_177E")

    Battle(0x335, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_17D8")

    label("loc_178E")

    Battle(0x336, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_17D8")

    label("loc_179E")

    Battle(0x337, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_17D8")

    label("loc_17AE")

    Battle(0x338, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_17D8")

    label("loc_17BE")

    Battle(0x339, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_17D8")

    label("loc_17CE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17D8")

    Jump("Function_23_1662")

    label("loc_17DB")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_23_1662 end

    def Function_24_17E9(): pass

    label("Function_24_17E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18B3")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R2400_01\x01",      # 0
            "R2400_02\x01",      # 1
            "R2400_03\x01",      # 2
            "R2400_04\x01",      # 3
            "R2400_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1856"),
        (1, "loc_1866"),
        (2, "loc_1876"),
        (3, "loc_1886"),
        (4, "loc_1896"),
        (SWITCH_DEFAULT, "loc_18A6"),
    )


    label("loc_1856")

    Battle(0x1A5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_18B0")

    label("loc_1866")

    Battle(0x1A6, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_18B0")

    label("loc_1876")

    Battle(0x1A7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_18B0")

    label("loc_1886")

    Battle(0x1A8, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_18B0")

    label("loc_1896")

    Battle(0x1A9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_18B0")

    label("loc_18A6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18B0")

    Jump("Function_24_17E9")

    label("loc_18B3")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_24_17E9 end

    def Function_25_18C1(): pass

    label("Function_25_18C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_198B")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C2111_01\x01",      # 0
            "C2111_02\x01",      # 1
            "C2111_03\x01",      # 2
            "C2111_04\x01",      # 3
            "C2111_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_192E"),
        (1, "loc_193E"),
        (2, "loc_194E"),
        (3, "loc_195E"),
        (4, "loc_196E"),
        (SWITCH_DEFAULT, "loc_197E"),
    )


    label("loc_192E")

    Battle(0x1B9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1988")

    label("loc_193E")

    Battle(0x1BA, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1988")

    label("loc_194E")

    Battle(0x1BB, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1988")

    label("loc_195E")

    Battle(0x1BC, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1988")

    label("loc_196E")

    Battle(0x1BD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1988")

    label("loc_197E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1988")

    Jump("Function_25_18C1")

    label("loc_198B")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_25_18C1 end

    def Function_26_1999(): pass

    label("Function_26_1999")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A72")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "BTL_EVENT011(迪恩)\x01",          # 0
            "BTL_EVENT012(雷斯)\x01",          # 1
            "BTL_EVENT013(洛克)\x01",          # 2
            "BTL_EVENT014(黑衣男子)\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1A25"),
        (1, "loc_1A35"),
        (2, "loc_1A45"),
        (3, "loc_1A55"),
        (SWITCH_DEFAULT, "loc_1A65"),
    )


    label("loc_1A25")

    Battle(0x38F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1A6F")

    label("loc_1A35")

    Battle(0x390, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1A6F")

    label("loc_1A45")

    Battle(0x391, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1A6F")

    label("loc_1A55")

    Battle(0x392, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1A6F")

    label("loc_1A65")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A6F")

    Jump("Function_26_1999")

    label("loc_1A72")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_26_1999 end

    def Function_27_1A80(): pass

    label("Function_27_1A80")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B89")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        2,
        10,
        80,
        1,
        (
            "卡鲁迪亚隧道\x01",          # 0
            "卡鲁迪亚大钟乳洞\x01",      # 1
            "红莲之塔\x01",              # 2
            "托兰特平原道\x01",          # 3
            "利塔街道\x01",              # 4
            "佐达特军用道\x01",          # 5
            "雷斯顿水上要塞\x01",        # 6
            "红莲之塔（事件）\x01",      # 7
            "取消\x01",                  # 8
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1B3B"),
        (1, "loc_1B42"),
        (2, "loc_1B49"),
        (3, "loc_1B50"),
        (4, "loc_1B57"),
        (5, "loc_1B5E"),
        (6, "loc_1B65"),
        (7, "loc_1B6C"),
        (SWITCH_DEFAULT, "loc_1B7C"),
    )


    label("loc_1B3B")

    Call(2, 28)
    Jump("loc_1B86")

    label("loc_1B42")

    Call(2, 29)
    Jump("loc_1B86")

    label("loc_1B49")

    Call(2, 30)
    Jump("loc_1B86")

    label("loc_1B50")

    Call(2, 31)
    Jump("loc_1B86")

    label("loc_1B57")

    Call(2, 32)
    Jump("loc_1B86")

    label("loc_1B5E")

    Call(2, 33)
    Jump("loc_1B86")

    label("loc_1B65")

    Call(2, 34)
    Jump("loc_1B86")

    label("loc_1B6C")

    Battle(0x3A0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1B86")

    label("loc_1B7C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1B86")

    Jump("Function_27_1A80")

    label("loc_1B89")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_27_1A80 end

    def Function_28_1B97(): pass

    label("Function_28_1B97")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C61")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R3400_01\x01",      # 0
            "R3400_02\x01",      # 1
            "R3400_03\x01",      # 2
            "R3400_04\x01",      # 3
            "R3400_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1C04"),
        (1, "loc_1C14"),
        (2, "loc_1C24"),
        (3, "loc_1C34"),
        (4, "loc_1C44"),
        (SWITCH_DEFAULT, "loc_1C54"),
    )


    label("loc_1C04")

    Battle(0x1CD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1C5E")

    label("loc_1C14")

    Battle(0x1CE, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1C5E")

    label("loc_1C24")

    Battle(0x1CF, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1C5E")

    label("loc_1C34")

    Battle(0x1D0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1C5E")

    label("loc_1C44")

    Battle(0x1D1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1C5E")

    label("loc_1C54")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1C5E")

    Jump("Function_28_1B97")

    label("loc_1C61")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_28_1B97 end

    def Function_29_1C6F(): pass

    label("Function_29_1C6F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D94")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C3300_01\x01",          # 0
            "C3300_02\x01",          # 1
            "C3300_03\x01",          # 2
            "C3300_04\x01",          # 3
            "C3300_05\x01",          # 4
            "C3300_06\x01",          # 5
            "C3300_07\x01",          # 6
            "BTL_EVENT020\x01",      # 7
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1D07"),
        (1, "loc_1D17"),
        (2, "loc_1D27"),
        (3, "loc_1D37"),
        (4, "loc_1D47"),
        (5, "loc_1D57"),
        (6, "loc_1D67"),
        (7, "loc_1D77"),
        (SWITCH_DEFAULT, "loc_1D87"),
    )


    label("loc_1D07")

    Battle(0x1E1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1D91")

    label("loc_1D17")

    Battle(0x1E2, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1D91")

    label("loc_1D27")

    Battle(0x1E3, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1D91")

    label("loc_1D37")

    Battle(0x1E4, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1D91")

    label("loc_1D47")

    Battle(0x1E5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1D91")

    label("loc_1D57")

    Battle(0x1E6, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1D91")

    label("loc_1D67")

    Battle(0x1E7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1D91")

    label("loc_1D77")

    Battle(0x398, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1D91")

    label("loc_1D87")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D91")

    Jump("Function_29_1C6F")

    label("loc_1D94")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_29_1C6F end

    def Function_30_1DA2(): pass

    label("Function_30_1DA2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E6C")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C3511_01\x01",      # 0
            "C3511_02\x01",      # 1
            "C3511_03\x01",      # 2
            "C3511_04\x01",      # 3
            "C3511_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1E0F"),
        (1, "loc_1E1F"),
        (2, "loc_1E2F"),
        (3, "loc_1E3F"),
        (4, "loc_1E4F"),
        (SWITCH_DEFAULT, "loc_1E5F"),
    )


    label("loc_1E0F")

    Battle(0x1F5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1E69")

    label("loc_1E1F")

    Battle(0x1F6, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1E69")

    label("loc_1E2F")

    Battle(0x1F7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1E69")

    label("loc_1E3F")

    Battle(0x1F8, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1E69")

    label("loc_1E4F")

    Battle(0x1F9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1E69")

    label("loc_1E5F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E69")

    Jump("Function_30_1DA2")

    label("loc_1E6C")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_30_1DA2 end

    def Function_31_1E7A(): pass

    label("Function_31_1E7A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FD5")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R3100_01\x01",      # 0
            "R3100_02\x01",      # 1
            "R3100_03\x01",      # 2
            "R3100_04\x01",      # 3
            "R3101_05\x01",      # 4
            "R3101_01\x01",      # 5
            "R3101_02\x01",      # 6
            "R3101_03\x01",      # 7
            "R3101_04\x01",      # 8
            "R3101_05\x01",      # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1F28"),
        (1, "loc_1F38"),
        (2, "loc_1F48"),
        (3, "loc_1F58"),
        (4, "loc_1F68"),
        (5, "loc_1F78"),
        (6, "loc_1F88"),
        (7, "loc_1F98"),
        (8, "loc_1FA8"),
        (9, "loc_1FB8"),
        (SWITCH_DEFAULT, "loc_1FC8"),
    )


    label("loc_1F28")

    Battle(0x209, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1FD2")

    label("loc_1F38")

    Battle(0x20A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1FD2")

    label("loc_1F48")

    Battle(0x20B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1FD2")

    label("loc_1F58")

    Battle(0x20C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1FD2")

    label("loc_1F68")

    Battle(0x20D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1FD2")

    label("loc_1F78")

    Battle(0x349, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1FD2")

    label("loc_1F88")

    Battle(0x34A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1FD2")

    label("loc_1F98")

    Battle(0x34B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1FD2")

    label("loc_1FA8")

    Battle(0x34C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1FD2")

    label("loc_1FB8")

    Battle(0x34D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1FD2")

    label("loc_1FC8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1FD2")

    Jump("Function_31_1E7A")

    label("loc_1FD5")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_31_1E7A end

    def Function_32_1FE3(): pass

    label("Function_32_1FE3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20AD")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R3200_01\x01",      # 0
            "R3200_02\x01",      # 1
            "R3200_03\x01",      # 2
            "R3200_04\x01",      # 3
            "R3200_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2050"),
        (1, "loc_2060"),
        (2, "loc_2070"),
        (3, "loc_2080"),
        (4, "loc_2090"),
        (SWITCH_DEFAULT, "loc_20A0"),
    )


    label("loc_2050")

    Battle(0x21D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_20AA")

    label("loc_2060")

    Battle(0x21E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_20AA")

    label("loc_2070")

    Battle(0x21F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_20AA")

    label("loc_2080")

    Battle(0x220, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_20AA")

    label("loc_2090")

    Battle(0x221, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_20AA")

    label("loc_20A0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_20AA")

    Jump("Function_32_1FE3")

    label("loc_20AD")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_32_1FE3 end

    def Function_33_20BB(): pass

    label("Function_33_20BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2185")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R3300_01\x01",      # 0
            "R3300_02\x01",      # 1
            "R3300_03\x01",      # 2
            "R3300_04\x01",      # 3
            "R3300_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2128"),
        (1, "loc_2138"),
        (2, "loc_2148"),
        (3, "loc_2158"),
        (4, "loc_2168"),
        (SWITCH_DEFAULT, "loc_2178"),
    )


    label("loc_2128")

    Battle(0x231, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2182")

    label("loc_2138")

    Battle(0x232, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2182")

    label("loc_2148")

    Battle(0x233, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2182")

    label("loc_2158")

    Battle(0x234, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2182")

    label("loc_2168")

    Battle(0x235, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2182")

    label("loc_2178")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2182")

    Jump("Function_33_20BB")

    label("loc_2185")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_33_20BB end

    def Function_34_2193(): pass

    label("Function_34_2193")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2282")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C3107_01\x01",              # 0
            "C3107_02\x01",              # 1
            "C3107_10\x01",              # 2
            "C3107_11\x01",              # 3
            "C3107_12\x01",              # 4
            "C3107_14特务兵Ｃ\x01",      # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2215"),
        (1, "loc_2225"),
        (2, "loc_2235"),
        (3, "loc_2245"),
        (4, "loc_2255"),
        (5, "loc_2265"),
        (SWITCH_DEFAULT, "loc_2275"),
    )


    label("loc_2215")

    Battle(0x245, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_227F")

    label("loc_2225")

    Battle(0x246, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_227F")

    label("loc_2235")

    Battle(0x24E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_227F")

    label("loc_2245")

    Battle(0x24F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_227F")

    label("loc_2255")

    Battle(0x250, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_227F")

    label("loc_2265")

    Battle(0x252, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_227F")

    label("loc_2275")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_227F")

    Jump("Function_34_2193")

    label("loc_2282")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_34_2193 end

    def Function_35_2290(): pass

    label("Function_35_2290")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2424")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        2,
        10,
        80,
        1,
        (
            "艾尔贝周游道\x01",                                  # 0
            "地下水路\x01",                                      # 1
            "封印区域\x01",                                      # 2
            "庭园大道\x01",                                      # 3
            "艾尔贝离宫外部　中庭、回廊（夜晚）\x01",            # 4
            "艾尔贝离宫外部　内部（夜晚）\x01",                  # 5
            "格兰赛尔城内部、中庭、女王宫内\x01",                # 6
            "格兰赛尔城内部、空中庭园\x01",                      # 7
            "封印区域BOSS其它(凯诺娜、理查德、洛伦斯)\x01",      # 8
            "王都格兰赛尔外部（竞技场内部）\x01",                # 9
            "取消\x01",                                          # 10
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_23D1"),
        (1, "loc_23D8"),
        (2, "loc_23DF"),
        (3, "loc_23E6"),
        (4, "loc_23ED"),
        (5, "loc_23F4"),
        (6, "loc_23FB"),
        (7, "loc_2402"),
        (8, "loc_2409"),
        (9, "loc_2410"),
        (SWITCH_DEFAULT, "loc_2417"),
    )


    label("loc_23D1")

    Call(2, 36)
    Jump("loc_2421")

    label("loc_23D8")

    Call(2, 37)
    Jump("loc_2421")

    label("loc_23DF")

    Call(2, 38)
    Jump("loc_2421")

    label("loc_23E6")

    Call(2, 39)
    Jump("loc_2421")

    label("loc_23ED")

    Call(2, 40)
    Jump("loc_2421")

    label("loc_23F4")

    Call(2, 41)
    Jump("loc_2421")

    label("loc_23FB")

    Call(2, 42)
    Jump("loc_2421")

    label("loc_2402")

    Call(2, 43)
    Jump("loc_2421")

    label("loc_2409")

    Call(2, 44)
    Jump("loc_2421")

    label("loc_2410")

    Call(2, 45)
    Jump("loc_2421")

    label("loc_2417")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2421")

    Jump("Function_35_2290")

    label("loc_2424")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_35_2290 end

    def Function_36_2432(): pass

    label("Function_36_2432")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24FC")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C4100_01\x01",      # 0
            "C4100_02\x01",      # 1
            "C4100_03\x01",      # 2
            "C4100_04\x01",      # 3
            "C4100_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_249F"),
        (1, "loc_24AF"),
        (2, "loc_24BF"),
        (3, "loc_24CF"),
        (4, "loc_24DF"),
        (SWITCH_DEFAULT, "loc_24EF"),
    )


    label("loc_249F")

    Battle(0x259, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_24F9")

    label("loc_24AF")

    Battle(0x25A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_24F9")

    label("loc_24BF")

    Battle(0x25B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_24F9")

    label("loc_24CF")

    Battle(0x25C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_24F9")

    label("loc_24DF")

    Battle(0x25D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_24F9")

    label("loc_24EF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_24F9")

    Jump("Function_36_2432")

    label("loc_24FC")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_36_2432 end

    def Function_37_250A(): pass

    label("Function_37_250A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2648")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C4200_01\x01",      # 0
            "C4200_02\x01",      # 1
            "C4200_03\x01",      # 2
            "C4200_04\x01",      # 3
            "C4200_05\x01",      # 4
            "C4200_06\x01",      # 5
            "C4200_07\x01",      # 6
            "C4200_08\x01",      # 7
            "C4200_09\x01",      # 8
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_25AB"),
        (1, "loc_25BB"),
        (2, "loc_25CB"),
        (3, "loc_25DB"),
        (4, "loc_25EB"),
        (5, "loc_25FB"),
        (6, "loc_260B"),
        (7, "loc_261B"),
        (8, "loc_262B"),
        (SWITCH_DEFAULT, "loc_263B"),
    )


    label("loc_25AB")

    Battle(0x26D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2645")

    label("loc_25BB")

    Battle(0x26E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2645")

    label("loc_25CB")

    Battle(0x26F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2645")

    label("loc_25DB")

    Battle(0x270, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2645")

    label("loc_25EB")

    Battle(0x271, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2645")

    label("loc_25FB")

    Battle(0x272, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2645")

    label("loc_260B")

    Battle(0x273, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2645")

    label("loc_261B")

    Battle(0x274, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2645")

    label("loc_262B")

    Battle(0x275, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2645")

    label("loc_263B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2645")

    Jump("Function_37_250A")

    label("loc_2648")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_37_250A end

    def Function_38_2656(): pass

    label("Function_38_2656")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27B1")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C4300_01\x01",      # 0
            "C4300_02\x01",      # 1
            "C4300_03\x01",      # 2
            "C4300_04\x01",      # 3
            "C4300_05\x01",      # 4
            "C4300_06\x01",      # 5
            "C4300_07\x01",      # 6
            "C4300_08\x01",      # 7
            "C4300_09\x01",      # 8
            "C4300_10\x01",      # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2704"),
        (1, "loc_2714"),
        (2, "loc_2724"),
        (3, "loc_2734"),
        (4, "loc_2744"),
        (5, "loc_2754"),
        (6, "loc_2764"),
        (7, "loc_2774"),
        (8, "loc_2784"),
        (9, "loc_2794"),
        (SWITCH_DEFAULT, "loc_27A4"),
    )


    label("loc_2704")

    Battle(0x281, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27AE")

    label("loc_2714")

    Battle(0x282, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27AE")

    label("loc_2724")

    Battle(0x283, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27AE")

    label("loc_2734")

    Battle(0x284, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27AE")

    label("loc_2744")

    Battle(0x285, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27AE")

    label("loc_2754")

    Battle(0x286, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27AE")

    label("loc_2764")

    Battle(0x287, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27AE")

    label("loc_2774")

    Battle(0x288, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27AE")

    label("loc_2784")

    Battle(0x289, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27AE")

    label("loc_2794")

    Battle(0x28A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27AE")

    label("loc_27A4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_27AE")

    Jump("Function_38_2656")

    label("loc_27B1")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_38_2656 end

    def Function_39_27BF(): pass

    label("Function_39_27BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2889")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R4100_01\x01",      # 0
            "R4100_02\x01",      # 1
            "R4100_03\x01",      # 2
            "R4100_04\x01",      # 3
            "R4100_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_282C"),
        (1, "loc_283C"),
        (2, "loc_284C"),
        (3, "loc_285C"),
        (4, "loc_286C"),
        (SWITCH_DEFAULT, "loc_287C"),
    )


    label("loc_282C")

    Battle(0x295, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2886")

    label("loc_283C")

    Battle(0x296, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2886")

    label("loc_284C")

    Battle(0x297, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2886")

    label("loc_285C")

    Battle(0x298, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2886")

    label("loc_286C")

    Battle(0x299, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2886")

    label("loc_287C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2886")

    Jump("Function_39_27BF")

    label("loc_2889")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_39_27BF end

    def Function_40_2897(): pass

    label("Function_40_2897")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2961")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "T4301_01\x01",      # 0
            "T4301_02\x01",      # 1
            "T4301_03\x01",      # 2
            "T4301_04\x01",      # 3
            "T4301_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2904"),
        (1, "loc_2914"),
        (2, "loc_2924"),
        (3, "loc_2934"),
        (4, "loc_2944"),
        (SWITCH_DEFAULT, "loc_2954"),
    )


    label("loc_2904")

    Battle(0x2BD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_295E")

    label("loc_2914")

    Battle(0x2BE, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_295E")

    label("loc_2924")

    Battle(0x2BF, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_295E")

    label("loc_2934")

    Battle(0x2C0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_295E")

    label("loc_2944")

    Battle(0x2C1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_295E")

    label("loc_2954")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_295E")

    Jump("Function_40_2897")

    label("loc_2961")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_40_2897 end

    def Function_41_296F(): pass

    label("Function_41_296F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A39")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "T4310_01\x01",      # 0
            "T4310_02\x01",      # 1
            "T4310_03\x01",      # 2
            "T4310_04\x01",      # 3
            "T4310_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_29DC"),
        (1, "loc_29EC"),
        (2, "loc_29FC"),
        (3, "loc_2A0C"),
        (4, "loc_2A1C"),
        (SWITCH_DEFAULT, "loc_2A2C"),
    )


    label("loc_29DC")

    Battle(0x2D1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2A36")

    label("loc_29EC")

    Battle(0x2D2, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2A36")

    label("loc_29FC")

    Battle(0x2D3, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2A36")

    label("loc_2A0C")

    Battle(0x2D4, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2A36")

    label("loc_2A1C")

    Battle(0x2D5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2A36")

    label("loc_2A2C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2A36")

    Jump("Function_41_296F")

    label("loc_2A39")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_41_296F end

    def Function_42_2A47(): pass

    label("Function_42_2A47")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B11")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "T4210_01\x01",      # 0
            "T4210_02\x01",      # 1
            "T4210_03\x01",      # 2
            "T4210_04\x01",      # 3
            "T4210_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2AB4"),
        (1, "loc_2AC4"),
        (2, "loc_2AD4"),
        (3, "loc_2AE4"),
        (4, "loc_2AF4"),
        (SWITCH_DEFAULT, "loc_2B04"),
    )


    label("loc_2AB4")

    Battle(0x2E5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B0E")

    label("loc_2AC4")

    Battle(0x2E6, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B0E")

    label("loc_2AD4")

    Battle(0x2E7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B0E")

    label("loc_2AE4")

    Battle(0x2E8, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B0E")

    label("loc_2AF4")

    Battle(0x2E9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B0E")

    label("loc_2B04")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2B0E")

    Jump("Function_42_2A47")

    label("loc_2B11")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_42_2A47 end

    def Function_43_2B1F(): pass

    label("Function_43_2B1F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BE9")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "T4201_01\x01",      # 0
            "T4201_02\x01",      # 1
            "T4201_03\x01",      # 2
            "T4201_04\x01",      # 3
            "T4201_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2B8C"),
        (1, "loc_2B9C"),
        (2, "loc_2BAC"),
        (3, "loc_2BBC"),
        (4, "loc_2BCC"),
        (SWITCH_DEFAULT, "loc_2BDC"),
    )


    label("loc_2B8C")

    Battle(0x2F9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2BE6")

    label("loc_2B9C")

    Battle(0x2FA, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2BE6")

    label("loc_2BAC")

    Battle(0x2FB, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2BE6")

    label("loc_2BBC")

    Battle(0x2FC, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2BE6")

    label("loc_2BCC")

    Battle(0x2FD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2BE6")

    label("loc_2BDC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2BE6")

    Jump("Function_43_2B1F")

    label("loc_2BE9")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_43_2B1F end

    def Function_44_2BF7(): pass

    label("Function_44_2BF7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CD3")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "洛伦斯\x01",                # 0
            "凯诺娜\x01",                # 1
            "理查德\x01",                # 2
            "最终BOSS第一形态\x01",      # 3
            "最终BOSS第二形态\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2C6E"),
        (1, "loc_2C7E"),
        (2, "loc_2C8E"),
        (3, "loc_2C9E"),
        (4, "loc_2CB2"),
        (SWITCH_DEFAULT, "loc_2CC6"),
    )


    label("loc_2C6E")

    Battle(0x39A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2CD0")

    label("loc_2C7E")

    Battle(0x39B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2CD0")

    label("loc_2C8E")

    Battle(0x39C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2CD0")

    label("loc_2C9E")

    Call(2, 48)
    Battle(0x3A1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2CD0")

    label("loc_2CB2")

    Call(2, 48)
    Battle(0x3A2, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2CD0")

    label("loc_2CC6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2CD0")

    Jump("Function_44_2BF7")

    label("loc_2CD3")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_44_2BF7 end

    def Function_45_2CE1(): pass

    label("Function_45_2CE1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DAD")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "迪恩、雷斯、洛克、杂鱼\x01",                # 0
            "克鲁茨、库拉茨、卡露娜、亚妮拉丝\x01",      # 1
            "洛伦斯、特务兵、特务兵、特务兵\x01",        # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2D70"),
        (1, "loc_2D80"),
        (2, "loc_2D90"),
        (SWITCH_DEFAULT, "loc_2DA0"),
    )


    label("loc_2D70")

    Battle(0x39D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2DAA")

    label("loc_2D80")

    Battle(0x39E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2DAA")

    label("loc_2D90")

    Battle(0x39F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2DAA")

    label("loc_2DA0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2DAA")

    Jump("Function_45_2CE1")

    label("loc_2DAD")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_45_2CE1 end

    def Function_46_2DBB(): pass

    label("Function_46_2DBB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E85")

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R4100_21\x01",      # 0
            "R4100_22\x01",      # 1
            "R4100_23\x01",      # 2
            "R4100_24\x01",      # 3
            "R4100_25\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2E28"),
        (1, "loc_2E38"),
        (2, "loc_2E48"),
        (3, "loc_2E58"),
        (4, "loc_2E68"),
        (SWITCH_DEFAULT, "loc_2E78"),
    )


    label("loc_2E28")

    Battle(0x2A9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2E82")

    label("loc_2E38")

    Battle(0x2AA, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2E82")

    label("loc_2E48")

    Battle(0x2AB, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2E82")

    label("loc_2E58")

    Battle(0x2AC, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2E82")

    label("loc_2E68")

    Battle(0x2AD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2E82")

    label("loc_2E78")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E82")

    Jump("Function_46_2DBB")

    label("loc_2E85")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_46_2DBB end

    def Function_47_2E93(): pass

    label("Function_47_2E93")

    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x0, 0x5, 0x0)
    OP_31(0x1, 0x5, 0x0)

    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择\x02",
        )
    )


    label("loc_2EB1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30E2")

    Menu(
        1,
        10,
        100,
        1,
        (
            "杂鱼中的杂鱼\x01",        # 0
            "爆种铃兰\x01",            # 1
            "事件战斗、田鼠\x01",      # 2
            "波波＋食人鲨\x01",        # 3
            "有NPC的战斗\x01",         # 4
            "空贼战\x01",              # 5
            "自动战斗１\x01",          # 6
            "竞技场①\x01",            # 7
            "竞技场②\x01",            # 8
            "竞技场③\x01",            # 9
            "竞技场④\x01",            # 10
            "竞技场⑤\x01",            # 11
            "竞技场⑥\x01",            # 12
            "取消\x01",                # 13
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2F92"),
        (1, "loc_2FA2"),
        (2, "loc_2FB2"),
        (3, "loc_2FE6"),
        (4, "loc_2FF6"),
        (5, "loc_300C"),
        (6, "loc_301C"),
        (7, "loc_3035"),
        (8, "loc_304E"),
        (9, "loc_3067"),
        (10, "loc_3080"),
        (11, "loc_3099"),
        (12, "loc_30B2"),
        (SWITCH_DEFAULT, "loc_30CB"),
    )


    label("loc_2F92")

    Battle(0x7A, 0x0, 0x0, 0x2, 0xFF)
    Jump("loc_30D5")

    label("loc_2FA2")

    Battle(0x18, 0x0, 0x0, 0x2, 0xFF)
    Jump("loc_30D5")

    label("loc_2FB2")


    AnonymousTalk(
        "这是事件战斗，请打倒所有的敌人。\x02",
    )

    CloseMessageWindow()
    Battle(0x393, 0x0, 0x0, 0x2, 0xFF)
    Jump("loc_30D5")

    label("loc_2FE6")

    Battle(0x38, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_30D5")

    label("loc_2FF6")

    AddParty(0xE, 0xFF)
    AddParty(0xF, 0xFF)
    Battle(0x7A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_30D5")

    label("loc_300C")

    Battle(0x387, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_30D5")

    label("loc_301C")

    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0xBB8, 0x100001, 0x0, 0x200, 0xFF)
    Jump("loc_30D5")

    label("loc_3035")

    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0xBB9, 0x100002, 0x0, 0x200, 0xFF)
    Jump("loc_30D5")

    label("loc_304E")

    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0xBBA, 0x100003, 0x0, 0x200, 0xFF)
    Jump("loc_30D5")

    label("loc_3067")

    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0xBBB, 0x100004, 0x0, 0x200, 0xFF)
    Jump("loc_30D5")

    label("loc_3080")

    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0xBBC, 0x100005, 0x0, 0x200, 0xFF)
    Jump("loc_30D5")

    label("loc_3099")

    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0xBBD, 0x100006, 0x0, 0x200, 0xFF)
    Jump("loc_30D5")

    label("loc_30B2")

    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0xBBE, 0x100007, 0x0, 0x200, 0xFF)
    Jump("loc_30D5")

    label("loc_30CB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_30D5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2EB1")

    label("loc_30E2")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_47_2E93 end

    def Function_48_30F2(): pass

    label("Function_48_30F2")

    OP_31(0x0, 0x0, 0x27)
    OP_31(0x1, 0x0, 0x27)
    OP_31(0x2, 0x0, 0x27)
    OP_31(0x3, 0x0, 0x27)
    OP_31(0x6, 0x0, 0x27)
    OP_31(0x4, 0x0, 0x27)
    OP_31(0x5, 0x0, 0x27)
    OP_31(0x7, 0x0, 0x27)
    OP_31(0x0, 0x5, 0x64)
    OP_31(0x1, 0x5, 0x64)
    OP_31(0x2, 0x5, 0x64)
    OP_31(0x3, 0x5, 0x64)
    OP_31(0x6, 0x5, 0x64)
    OP_31(0x4, 0x5, 0x64)
    OP_31(0x5, 0x5, 0x64)
    OP_31(0x7, 0x5, 0x64)
    OP_3E(0x1F5, 99)
    OP_3E(0x1F6, 99)
    OP_3E(0x1F7, 99)
    OP_3E(0x1FB, 99)
    OP_3E(0x1FC, 99)
    OP_3E(0x1FD, 10)
    OP_3E(0x1FF, 99)
    OP_3E(0x1FF, 99)
    OP_34(0x1, 0x3C)
    OP_34(0x1, 0x3E)
    OP_34(0x1, 0x41)
    OP_34(0x1, 0x3F)
    OP_34(0x1, 0x5F)
    OP_34(0x1, 0x60)
    OP_34(0x1, 0x69)
    OP_34(0x1, 0x6A)
    OP_34(0x0, 0x1E)
    OP_34(0x0, 0x1F)
    OP_34(0x0, 0x20)
    OP_34(0x0, 0x23)
    OP_34(0x0, 0x25)
    OP_34(0x0, 0x6E)
    OP_34(0x0, 0x6F)
    OP_34(0x0, 0x70)
    OP_34(0x0, 0x76)
    OP_34(0x0, 0x77)
    OP_34(0x0, 0x78)
    OP_34(0x2, 0x32)
    OP_34(0x2, 0x33)
    OP_34(0x2, 0x34)
    OP_34(0x2, 0x36)
    OP_34(0x2, 0x37)
    OP_34(0x3, 0x64)
    OP_34(0x3, 0x69)
    OP_34(0x3, 0x69)
    OP_34(0x3, 0x4B)
    OP_34(0x3, 0x4C)
    OP_34(0x4, 0x6E)
    OP_34(0x4, 0x6F)
    OP_34(0x4, 0x70)
    OP_34(0x4, 0x72)
    OP_34(0x4, 0x73)
    OP_34(0x4, 0x76)
    OP_34(0x4, 0x77)
    OP_34(0x4, 0x78)
    OP_34(0x5, 0x1E)
    OP_34(0x5, 0x1F)
    OP_34(0x5, 0x20)
    OP_34(0x6, 0x56)
    OP_34(0x6, 0x57)
    OP_34(0x6, 0x58)
    OP_34(0x6, 0x6E)
    OP_34(0x6, 0x6F)
    OP_34(0x6, 0x76)
    OP_34(0x7, 0xB)
    OP_34(0x7, 0xD)
    OP_34(0x7, 0x10)
    OP_34(0x7, 0x4B)
    OP_34(0x7, 0x4C)
    OP_41(0x0, 0xA)
    OP_41(0x0, 0xFE)
    OP_41(0x0, 0x119)
    OP_41(0x1, 0x29)
    OP_41(0x1, 0xFD)
    OP_41(0x1, 0x11A)
    OP_41(0x2, 0x41)
    OP_41(0x2, 0xFE)
    OP_41(0x2, 0x119)
    OP_41(0x3, 0x62)
    OP_41(0x3, 0xFD)
    OP_41(0x3, 0x11A)
    OP_41(0x4, 0x80)
    OP_41(0x4, 0xFE)
    OP_41(0x4, 0x119)
    OP_41(0x5, 0x9D)
    OP_41(0x5, 0xFD)
    OP_41(0x5, 0x11A)
    OP_41(0x6, 0xBB)
    OP_41(0x6, 0xFE)
    OP_41(0x6, 0x119)
    OP_41(0x7, 0xD9)
    OP_41(0x7, 0xFD)
    OP_41(0x7, 0x11A)
    Return()

    # Function_48_30F2 end

    SaveToFile()

Try(main)
