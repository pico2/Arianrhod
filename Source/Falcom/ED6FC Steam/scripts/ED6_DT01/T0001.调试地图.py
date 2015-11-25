from ED6ScenarioHelper import *

def main():
    # 调试地图

    CreateScenaFile(
        FileName            = 'T0001   ._SN',
        MapName             = 'map1',
        Location            = 'T0001.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
        Flags               = 0,
        EntryFunctionIndex  = 16,
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
        '市民１',                               # 9
        '喵呜',                                 # 10
        '地图物体0',                            # 11
        '宝箱',                                 # 12
        '宝箱',                                 # 13
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 1,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 2,
    )


    AddCharChip(
        'ED6_DT07/CH01000 ._CH',             # 00
        'ED6_DT09/CH10000 ._CH',             # 01
        'ED6_DT09/CH10001 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01000P._CP',             # 00
        'ED6_DT09/CH10000P._CP',             # 01
        'ED6_DT09/CH10001P._CP',             # 02
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = -4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -4000,
        Z                   = 0,
        Y                   = -2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x100,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -4000,
        Z                   = 0,
        Y                   = -4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x0,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -5000,
        Z                   = 0,
        Y                   = -6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x0,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 10000,
        Z                   = 0,
        Y                   = -4000,
        Unknown_0C          = 0,
        Unknown_0E          = 1,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7D0,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 10000,
        Y                   = 0,
        Z                   = -1000,
        Range               = 11000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x0,
        Unknown_1C          = 11,
    )


    DeclActor(
        TriggerX            = -2000,
        TriggerZ            = 1000,
        TriggerY            = 0,
        TriggerRange        = 1000,
        ActorX              = -2000,
        ActorZ              = 1000,
        ActorY              = 0,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -18000,
        TriggerZ            = 1000,
        TriggerY            = 18000,
        TriggerRange        = 1000,
        ActorX              = -2000,
        ActorZ              = 1000,
        ActorY              = 0,
        Flags               = 0x7E,
        TalkScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1E6",          # 00, 0
        "Function_1_1E7",          # 01, 1
        "Function_2_5D3",          # 02, 2
        "Function_3_5D4",          # 03, 3
        "Function_4_61F",          # 04, 4
        "Function_5_620",          # 05, 5
        "Function_6_625",          # 06, 6
        "Function_7_8C2",          # 07, 7
        "Function_8_A14",          # 08, 8
        "Function_9_A50",          # 09, 9
        "Function_10_A65",         # 0A, 10
        "Function_11_A89",         # 0B, 11
        "Function_12_CCC",         # 0C, 12
        "Function_13_DE4",         # 0D, 13
        "Function_14_E62",         # 0E, 14
        "Function_15_E70",         # 0F, 15
        "Function_16_E7A",         # 10, 16
        "Function_17_E94",         # 11, 17
        "Function_18_10F2",        # 12, 18
        "Function_19_1101",        # 13, 19
        "Function_20_11C2",        # 14, 20
        "Function_21_11DD",        # 15, 21
        "Function_22_11F8",        # 16, 22
        "Function_23_1211",        # 17, 23
    )


    def Function_0_1E6(): pass

    label("Function_0_1E6")

    Return()

    # Function_0_1E6 end

    def Function_1_1E7(): pass

    label("Function_1_1E7")

    OP_A3(0x21E)
    Event(0, 11)
    OP_62(0x9, 0xFFFFFDA8, 300, 0x80, 0x21, 0xFA, 0x0)
    SetChrFlags(0x9, 0x6)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x9, -4000, 1000, -2000, 0)
    OP_51(0x9, 0x2A, (scpexpr(EXPR_PUSH_LONG, 0x7530), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x2B, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x2C, (scpexpr(EXPR_PUSH_LONG, 0x15F90), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C3")
    OP_A2(0x219)
    RemoveParty(0x0, 0xFF)
    AddParty(0x1, 0x0)
    AddParty(0x0, 0x1)
    AddParty(0x5, 0x2)
    AddParty(0x7, 0x3)
    OP_31(0x3, 0x0, 0x3)
    OP_31(0x4, 0x0, 0x3)
    OP_31(0x6, 0x0, 0x3)
    OP_31(0x2, 0x0, 0x3)
    OP_31(0x0, 0x7, 0x4)
    OP_31(0x0, 0x0, 0x3)
    OP_31(0x1, 0x7, 0x3)
    OP_31(0x1, 0x0, 0x3)
    OP_31(0x0, 0x7, 0x3)
    OP_34(0x0, 0x6E)
    OP_34(0x0, 0x6F)
    OP_34(0x0, 0x74)
    OP_34(0x0, 0x76)
    OP_34(0x0, 0xA)
    OP_34(0x0, 0xB)
    OP_34(0x0, 0xD)
    OP_34(0x0, 0x10)
    OP_34(0x0, 0x14)
    OP_34(0x0, 0x18)
    OP_34(0x0, 0x32)
    OP_34(0x0, 0x33)
    OP_34(0x0, 0x34)
    OP_34(0x0, 0x36)
    OP_34(0x0, 0x3E)
    OP_34(0x0, 0x3F)
    OP_34(0x0, 0x4B)
    OP_34(0x0, 0x4C)
    OP_34(0x0, 0x50)
    OP_34(0x0, 0x64)
    OP_34(0x0, 0x69)
    OP_34(0x1, 0x6E)
    OP_34(0x1, 0x6F)
    OP_34(0x1, 0x70)
    OP_34(0x1, 0xA)
    OP_34(0x1, 0xC)
    OP_34(0x1, 0xD)
    OP_34(0x1, 0x14)
    OP_34(0x1, 0x15)
    OP_34(0x1, 0x17)
    OP_34(0x1, 0x32)
    OP_34(0x1, 0x33)
    OP_34(0x1, 0x34)
    OP_34(0x1, 0x36)
    OP_34(0x1, 0x37)
    OP_34(0x1, 0x3C)
    OP_34(0x1, 0x3E)
    OP_34(0x1, 0x3F)
    OP_34(0x1, 0x4B)
    OP_34(0x1, 0x4C)
    OP_34(0x1, 0x50)
    OP_34(0x1, 0x64)
    OP_34(0x1, 0x69)
    OP_34(0x2, 0x78)
    OP_34(0x3, 0x78)
    OP_35(0x0, 0x96)
    OP_35(0x0, 0x97)
    OP_35(0x0, 0x98)
    OP_35(0x0, 0x99)
    OP_35(0x0, 0x9A)
    OP_35(0x1, 0xA0)
    OP_35(0x1, 0xA1)
    OP_35(0x1, 0xA2)
    OP_35(0x1, 0xA3)
    OP_35(0x1, 0xA4)
    OP_35(0x2, 0xAA)
    OP_35(0x2, 0xAB)
    OP_35(0x2, 0xAC)
    OP_35(0x3, 0xB4)
    OP_35(0x3, 0xB5)
    OP_35(0x3, 0xB6)
    OP_35(0x4, 0xBE)
    OP_35(0x4, 0xBF)
    OP_35(0x5, 0xC8)
    OP_35(0x5, 0xC9)
    OP_35(0x5, 0xCA)
    OP_35(0x5, 0xCB)
    OP_35(0x6, 0xD2)
    OP_35(0x6, 0xD3)
    OP_35(0x7, 0xDD)
    OP_35(0x7, 0xDE)
    OP_35(0x7, 0xDC)
    OP_36(0x0, 0xE6)
    OP_36(0x0, 0xE7)
    OP_36(0x1, 0xEB)
    OP_36(0x1, 0xEC)
    OP_36(0x2, 0xF0)
    OP_36(0x3, 0xF5)
    OP_36(0x4, 0xFA)
    OP_36(0x5, 0xFF)
    OP_36(0x5, 0x100)
    OP_36(0x6, 0x104)
    OP_36(0x7, 0x109)
    OP_36(0x7, 0x10A)
    OP_41(0x0, 0x1)
    OP_41(0x1, 0x1F)
    OP_41(0x5, 0x97)
    OP_41(0x2, 0x3D)
    OP_41(0x4, 0x79)
    OP_41(0x6, 0xB5)
    OP_41(0x3, 0x5B)
    OP_41(0x7, 0x3E8)
    AddSepith(0x0, 0x14)
    AddSepith(0x1, 0x14)
    AddSepith(0x2, 0x14)
    AddSepith(0x3, 0x14)
    OP_37(0x0, 0x0)
    OP_37(0x1, 0x0)
    OP_3E(0x258, 1)
    OP_3E(0x259, 1)
    OP_3E(0x25E, 1)
    OP_41(0x0, 0xF1)
    OP_41(0x1, 0xF1)
    OP_41(0x0, 0x10F)
    OP_41(0x1, 0x10F)
    OP_3E(0x1F5, 50)
    OP_3E(0x12D, 2)
    OP_3E(0x12E, 2)
    OP_3E(0x12F, 2)
    OP_3E(0x130, 2)
    OP_3E(0x131, 2)
    OP_3E(0x132, 2)
    OP_3E(0x133, 2)
    OP_3E(0x134, 2)
    OP_3E(0x135, 2)
    OP_3E(0x136, 2)
    OP_3E(0x137, 2)
    OP_3E(0x138, 2)
    OP_3E(0x139, 2)
    OP_3E(0x13A, 2)
    OP_3E(0x13B, 2)
    OP_3E(0x13C, 2)
    OP_3E(0x13D, 2)
    OP_3E(0x13E, 2)
    OP_3E(0x13F, 2)
    OP_3E(0x140, 2)
    OP_3E(0x141, 2)
    OP_3E(0x142, 2)
    OP_3E(0x143, 2)
    OP_3E(0x144, 2)
    OP_3E(0x145, 2)
    OP_3E(0x146, 2)
    OP_3E(0x147, 2)
    OP_3E(0x258, 4)
    OP_3E(0x25B, 4)
    OP_3E(0x25E, 4)
    OP_3E(0x261, 4)
    OP_3E(0x264, 4)
    OP_3E(0x267, 4)
    OP_3E(0x26A, 4)
    OP_3E(0x26D, 4)
    OP_3E(0x270, 4)
    OP_3E(0x273, 4)
    OP_3E(0x276, 4)
    OP_3E(0x279, 1)
    OP_3E(0x27A, 1)
    OP_3E(0x27B, 1)
    OP_3E(0x27C, 1)
    OP_3E(0x285, 1)
    OP_3E(0x286, 1)
    OP_3E(0x287, 1)
    OP_3E(0x27D, 1)
    OP_3E(0x27E, 1)
    OP_3E(0x27F, 1)
    OP_3E(0x280, 1)
    OP_3E(0x281, 1)
    OP_3E(0x282, 1)
    OP_3E(0x283, 1)
    OP_3E(0x28A, 2)
    OP_3E(0x28B, 2)
    OP_3E(0x28D, 4)
    OP_3E(0x294, 4)
    OP_3E(0x296, 4)
    OP_3E(0x2B2, 4)
    OP_3E(0x2BC, 2)
    OP_3E(0x2BD, 2)
    OP_3E(0x2BE, 2)
    OP_3E(0x2C6, 2)
    OP_3E(0x2C8, 2)
    OP_3E(0x2C1, 2)
    OP_3E(0x28C, 2)
    OP_3E(0x291, 2)
    OP_3E(0x2D0, 1)
    OP_3E(0x2D1, 1)
    OP_3E(0x2D2, 1)
    OP_3E(0x2D3, 1)
    OP_3E(0x2D4, 1)
    SetMapFlags(0x1000000)
    SetMapFlags(0x800000)

    label("loc_5C3")

    SetMapFlags(0x1)
    ClearMapFlags(0x20)
    ClearMapFlags(0x400000)
    Return()

    # Function_1_1E7 end

    def Function_2_5D3(): pass

    label("Function_2_5D3")

    Return()

    # Function_2_5D3 end

    def Function_3_5D4(): pass

    label("Function_3_5D4")

    SetChrPos(0xC, 2000, 0, 2000, 0)
    OP_A1(0xC, 0x6)
    Sleep(1)
    SetChrBattleFlags(0x8, 0x20)
    OP_89(0x8, 2000, 2000, 2000, 0)
    Sleep(3000)
    OP_8F(0xC, 0xFA0, 0x3E8, 0x7D0, 0x7D0, 0x0)
    Return()

    # Function_3_5D4 end

    def Function_4_61F(): pass

    label("Function_4_61F")

    Return()

    # Function_4_61F end

    def Function_5_620(): pass

    label("Function_5_620")

    Call(0, 11)
    Return()

    # Function_5_620 end

    def Function_6_625(): pass

    label("Function_6_625")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_647")

    ChrTalk(
        0xFE,
        "设立local flag哦～\x02",
    )

    CloseMessageWindow()

    label("loc_647")

    OP_A2(0x12)
    SetMessageWindowPos(100, 100, 15, 2)

    AnonymousTalk(
        (
            "#200W可以指定坐标显示哦。\x02\x01",
            "#W是真的哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            "#20A等两秒～\x02",
            "#A如果不指定坐标，\x01",
            "就会在画面中央显示哦～\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(
        "请指定恢复时的默认坐标。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(
        0xFE,
        "#010F#1P靠近左上\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#010F#2P靠近右上\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#010F#3P靠近左下\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#010F#4P靠近右下\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#010F#5P靠近上方\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#010F#6P靠近下方\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你知道吗？按下F11，\x01",
            "就可以看到事件区域了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#010F我啊、和爱娜！结婚了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1,
        "#020F哦哦？哈～哈哈哈哈哈。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1,
        (
            "#020F没想到在这里见到\x01",
            "爱娜朝思暮想的人。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("约修亚")

    AnonymousTalk(
        (
            "#000F暑假已经结束了。\x02\x01",
            "#4Sあああああ\x02",
        )
    )

    CloseMessageWindow()
    OP_61(0x101)

    AnonymousTalk(
        (
            "#F#2Sあいうえお#10R a   i   u   e   o#\x02\x01",
            "かきくけこ#10R ka  ki  ku  ke  ko#さしすせそ#10R sa  si  su  se  so#\x01",
            "真是的。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_625 end

    def Function_7_8C2(): pass

    label("Function_7_8C2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8E6")
    OP_8D(0xFE, 5000, -5000, 15000, 9000, 2000)
    OP_48()
    Jump("Function_7_8C2")

    label("loc_8E6")

    Return()

    # Function_7_8C2 end

    def Function_8_A14(): pass

    label("Function_8_A14")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A4F")
    OP_70(0x1, 0x32)
    OP_8D(0xFE, -10000, -10000, 1000, 1000, 2000)
    OP_6F(0x1, 0)
    OP_72(0x1, 0x8)
    Sleep(2000)
    Jump("Function_8_A14")

    label("loc_A4F")

    Return()

    # Function_8_A14 end

    def Function_9_A50(): pass

    label("Function_9_A50")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A64")
    OP_8C(0xFE, 180, 5000)
    OP_48()
    Jump("Function_9_A50")

    label("loc_A64")

    Return()

    # Function_9_A50 end

    def Function_10_A65(): pass

    label("Function_10_A65")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A88")
    OP_8D(0x0, 10000, 10000, -10000, -10000, 2000)
    Jump("Function_10_A65")

    label("loc_A88")

    Return()

    # Function_10_A65 end

    def Function_11_A89(): pass

    label("Function_11_A89")

    OP_16(0x1)
    EventBegin(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrName("跳转君")

    AnonymousTalk(
        "请选择地图。\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AB7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CB6")

    Menu(
        0,
        10,
        10,
        1,
        (
            "测试地图\x01",                  # 0
            "游戏地图\x01",                  # 1
            "角色一览\x01",                  # 2
            "魔兽一览\x01",                  # 3
            "地图对象一览\x01",              # 4
            "战斗\x01",                      # 5
            "战斗（魔兽计算测试）\x01",      # 6
            "战斗（确认地图）\x01",          # 7
            "战斗（检测用）\x01",            # 8
            "事件列表\x01",                  # 9
            "商店测试\x01",                  # 10
            "存档菜单\x01",                  # 11
            "绝对模式视角测试\x01",          # 12
            "返回标题画面\x01",              # 13
            "影像播放·停止\x01",            # 14
            "取消\x01",                      # 15
        )
    )

    MenuEnd(0x0)
    OP_16(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_BCF"),
        (1, "loc_BD6"),
        (2, "loc_BDD"),
        (3, "loc_BE4"),
        (4, "loc_BEB"),
        (5, "loc_BF2"),
        (6, "loc_BF9"),
        (7, "loc_C00"),
        (8, "loc_C07"),
        (9, "loc_C0E"),
        (10, "loc_C15"),
        (11, "loc_C21"),
        (12, "loc_C25"),
        (13, "loc_C80"),
        (14, "loc_C85"),
        (SWITCH_DEFAULT, "loc_CA6"),
    )


    label("loc_BCF")

    Call(0, 12)
    Jump("loc_CB3")

    label("loc_BD6")

    Call(3, 2)
    Jump("loc_CB3")

    label("loc_BDD")

    Call(3, 0)
    Jump("loc_CB3")

    label("loc_BE4")

    Call(3, 1)
    Jump("loc_CB3")

    label("loc_BEB")

    Call(0, 13)
    Jump("loc_CB3")

    label("loc_BF2")

    Call(0, 17)
    Jump("loc_CB3")

    label("loc_BF9")

    Call(1, 0)
    Jump("loc_CB3")

    label("loc_C00")

    Call(2, 0)
    Jump("loc_CB3")

    label("loc_C07")

    Call(2, 47)
    Jump("loc_CB3")

    label("loc_C0E")

    Call(4, 0)
    Jump("loc_CB3")

    label("loc_C15")

    OP_5F(0x0)
    OP_56(0x0)
    Call(0, 19)
    Jump("loc_CB3")

    label("loc_C21")

    ShowSaveMenu()
    Jump("loc_CB3")

    label("loc_C25")

    OP_5F(0x0)
    OP_56(0x0)
    Sleep(500)
    ClearMapFlags(0x1)
    OP_66(0x0)
    OP_67(-15000, 10000, -10000, 1000)
    OP_69(0x8, 0x3E8)
    OP_69(0x0, 0x3E8)
    OP_66(0x1)
    OP_67(0, 8000, -10000, 1000)
    OP_6C(45000, 1000)
    SetMapFlags(0x1)
    Sleep(500)
    Jump("loc_CB3")

    label("loc_C80")

    OP_B4(0x0)
    Jump("loc_CB3")

    label("loc_C85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_C95")
    PlayMovie(0x1, "")
    OP_A3(0x15)
    Jump("loc_CA3")

    label("loc_C95")

    PlayMovie(0x0, "logo.avi")
    OP_A2(0x15)

    label("loc_CA3")

    Jump("loc_CB3")

    label("loc_CA6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CB3")

    label("loc_CB3")

    Jump("loc_AB7")

    label("loc_CB6")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_11_A89 end

    def Function_12_CCC(): pass

    label("Function_12_CCC")


    AnonymousTalk(
        (
            scpstr(0x6),
            "请选择测试地图。\x02",
        )
    )


    label("loc_CE0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DD4")

    Menu(
        1,
        10,
        100,
        1,
        (
            "测试地图20\x01",      # 0
            "测试地图21\x01",      # 1
            "测试地图22\x01",      # 2
            "测试地图23\x01",      # 3
            "测试地图24\x01",      # 4
            "测试地图25\x01",      # 5
            "测试地图26\x01",      # 6
            "测试地图27\x01",      # 7
            "取消\x01",            # 8
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D7F"),
        (1, "loc_D88"),
        (2, "loc_D91"),
        (3, "loc_D9A"),
        (4, "loc_DA3"),
        (5, "loc_DAC"),
        (6, "loc_DB5"),
        (7, "loc_DBE"),
        (SWITCH_DEFAULT, "loc_DC7"),
    )


    label("loc_D7F")

    NewScene("ED6_DT01/T0020   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_D88")

    NewScene("ED6_DT01/T0021   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_D91")

    NewScene("ED6_DT01/T0022   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_D9A")

    NewScene("ED6_DT01/T0023   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_DA3")

    NewScene("ED6_DT01/T0024   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_DAC")

    NewScene("ED6_DT01/T0025   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_DB5")

    NewScene("ED6_DT01/T0026   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_DBE")

    NewScene("ED6_DT01/T0027   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_DC7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CE0")

    label("loc_DD4")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_12_CCC end

    def Function_13_DE4(): pass

    label("Function_13_DE4")


    AnonymousTalk(
        (
            scpstr(0x6),
            "哪个？\x02",
        )
    )


    label("loc_DEE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E52")

    Menu(
        1,
        10,
        100,
        1,
        (
            "地图对象１\x01",      # 0
            "地图对象２\x01",      # 1
            "取消\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E33"),
        (1, "loc_E3C"),
        (SWITCH_DEFAULT, "loc_E45"),
    )


    label("loc_E33")

    NewScene("ED6_DT01/T0070   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_E3C")

    NewScene("ED6_DT01/T0071   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_E45")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DEE")

    label("loc_E52")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_13_DE4 end

    def Function_14_E62(): pass

    label("Function_14_E62")

    OP_6B(5000, 3000)
    Call(0, 15)
    Return()

    # Function_14_E62 end

    def Function_15_E70(): pass

    label("Function_15_E70")

    OP_6C(0, 20000)
    Return()

    # Function_15_E70 end

    def Function_16_E7A(): pass

    label("Function_16_E7A")

    EventBegin(0x0)
    OP_62(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Return()

    # Function_16_E7A end

    def Function_17_E94(): pass

    label("Function_17_E94")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10E4")

    Menu(
        1,
        10,
        100,
        1,
        (
            "测试\x01",                  # 0
            "对角测试\x01",              # 1
            "直线攻击测试\x01",          # 2
            "测试地图2\x01",             # 3
            "10000-10070\x01",           # 4
            "10080-10150\x01",           # 5
            "10160-10220\x01",           # 6
            "00260-00330\x01",           # 7
            "00340-00410\x01",           # 8
            "最终BOSS第１形态\x01",      # 9
            "最终BOSS第２形态\x01",      # 10
            "最终BOSS第３形态\x01",      # 11
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_F7A"),
        (1, "loc_F8A"),
        (2, "loc_F9A"),
        (3, "loc_FAA"),
        (4, "loc_FBA"),
        (5, "loc_FCA"),
        (6, "loc_FDA"),
        (7, "loc_FEA"),
        (8, "loc_FFA"),
        (9, "loc_100A"),
        (10, "loc_1020"),
        (11, "loc_1036"),
        (SWITCH_DEFAULT, "loc_109C"),
    )


    label("loc_F7A")

    Battle(0x7DA, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_109F")

    label("loc_F8A")

    Battle(0x7E3, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_109F")

    label("loc_F9A")

    Battle(0x7E4, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_109F")

    label("loc_FAA")

    Battle(0x7E6, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_109F")

    label("loc_FBA")

    Battle(0x7D3, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_109F")

    label("loc_FCA")

    Battle(0x7D4, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_109F")

    label("loc_FDA")

    Battle(0x7D5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_109F")

    label("loc_FEA")

    Battle(0x7DB, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_109F")

    label("loc_FFA")

    Battle(0x7DC, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_109F")

    label("loc_100A")

    OP_1D(0x2D)
    Call(2, 48)
    Battle(0x3A1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_109F")

    label("loc_1020")

    OP_1D(0x2E)
    Call(2, 48)
    Battle(0x3A2, 0x100008, 0x0, 0x0, 0xFF)
    Jump("loc_109F")

    label("loc_1036")

    OP_1D(0x2B)
    Call(2, 48)
    OP_31(0x0, 0xFA, 0x1)
    OP_31(0x1, 0xFA, 0x1)
    OP_31(0x2, 0xFA, 0x1)
    OP_31(0x3, 0xFA, 0x1)
    OP_31(0x4, 0xFA, 0x1)
    OP_31(0x5, 0xFA, 0x1)
    OP_31(0x6, 0xFA, 0x1)
    OP_31(0x7, 0xFA, 0x1)
    OP_31(0x0, 0x5, 0xC8)
    OP_31(0x1, 0x5, 0xC8)
    OP_31(0x2, 0x5, 0xC8)
    OP_31(0x3, 0x5, 0xC8)
    OP_31(0x4, 0x5, 0xC8)
    OP_31(0x5, 0x5, 0xC8)
    OP_31(0x6, 0x5, 0xC8)
    OP_31(0x7, 0x5, 0xC8)
    Battle(0x3B3, 0x10000A, 0x0, 0x0, 0xFF)
    Jump("loc_109F")

    label("loc_109C")

    Jump("loc_109F")

    label("loc_109F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_10B6"),
        (SWITCH_DEFAULT, "loc_10E1"),
    )


    label("loc_10B6")

    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    Jump("loc_10E1")

    label("loc_10E1")

    Jump("Function_17_E94")

    label("loc_10E4")

    OP_5F(0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_17_E94 end

    def Function_18_10F2(): pass

    label("Function_18_10F2")


    ChrTalk(
        0x0,
        "欢迎\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A9(0x0)
    Return()

    # Function_18_10F2 end

    def Function_19_1101(): pass

    label("Function_19_1101")

    SetChrName("商店君")

    AnonymousTalk(
        (
            scpstr(0x6),
            "哪个商店？\x02",
        )
    )


    Menu(
        1,
        10,
        100,
        1,
        (
            "工房\x01",                      # 0
            "武器店\x01",                    # 1
            "道具店\x01",                    # 2
            "旅馆\x01",                      # 3
            "游击士协会\x01",                # 4
            "读书（利贝尔通讯１）\x01",      # 5
            "取消\x01",                      # 6
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1189"),
        (1, "loc_1190"),
        (2, "loc_1197"),
        (3, "loc_119E"),
        (4, "loc_11A5"),
        (5, "loc_11AC"),
        (SWITCH_DEFAULT, "loc_11B4"),
    )


    label("loc_1189")

    Call(0, 18)
    Jump("loc_11B7")

    label("loc_1190")

    Call(0, 20)
    Jump("loc_11B7")

    label("loc_1197")

    Call(0, 21)
    Jump("loc_11B7")

    label("loc_119E")

    Call(0, 22)
    Jump("loc_11B7")

    label("loc_11A5")

    Call(0, 23)
    Jump("loc_11B7")

    label("loc_11AC")

    OP_B9(0x347, 0x0)
    Jump("loc_11B7")

    label("loc_11B4")

    Jump("loc_11B7")

    label("loc_11B7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_19_1101 end

    def Function_20_11C2(): pass

    label("Function_20_11C2")


    ChrTalk(
        0x0,
        "欢迎来到武器店！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A9(0x1)
    Return()

    # Function_20_11C2 end

    def Function_21_11DD(): pass

    label("Function_21_11DD")


    ChrTalk(
        0x0,
        "欢迎来到道具店！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A9(0x2)
    Return()

    # Function_21_11DD end

    def Function_22_11F8(): pass

    label("Function_22_11F8")


    ChrTalk(
        0x0,
        "欢迎来到旅馆！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A9(0x3)
    Return()

    # Function_22_11F8 end

    def Function_23_1211(): pass

    label("Function_23_1211")


    ChrTalk(
        0x0,
        "欢迎来到协会！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_2A(0x1, 0x2, 0x3, 0xFFFF)
    Return()

    # Function_23_1211 end

    SaveToFile()

Try(main)
