from EDAOScenaFile import *

def main():
    CreateScenaFile(
        "m9082.bin",                # FileName
        "m9082",                    # MapName
        "m9082",                    # Location
        0x00C3,                     # 戒之领域
        "ed70356",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x18\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0]\x00\x00\xf4\x01\x00\x00\x1e\x00-\x00\x00\x00h\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\xc3\x00\x00\x00\x00\x01',
    )

    BuildStringList((
        "m9082",                  # 0
        "亚里欧斯",               # 1
        "显示台词用模型",         # 2
        "亚里欧斯带领的魔兽",     # 3
        "亚里欧斯带领的魔兽",     # 4
        "表现效果用模型",         # 5
        "bm9069",                 # 6
    ))

    ATBonus("ATBonus_1D8", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_298", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_29C", 3, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A0", 13, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A4", 3, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A8", 13, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_2AC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_278", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_27C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_280", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_284", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_288", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_28C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_290", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_294", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_2B8", 0x0042, 255, 6, 45, 3, 3, 30, 0, "bm9069", 0x00000000, 100, 0, 0, 0,
        (
            ("ms02401.dat", "ms03301.dat", "ms03401.dat", "ms03700.dat", "ms03800.dat", 0, 0, 0, "MonsterBattlePostion_298", "MonsterBattlePostion_278", "ed7527.ogg", "ed7453.ogg", "ATBonus_1D8"),
            (),
            (),
            (),
        )
    )

    AddCharChip(
        "apl/ch51744.itc",                   # 00
    )

    DeclNpc(0,       12000,   211500,  180,  389,  0x0, 0,   0,   0,   255, 255, 0,   2,   255,  0)
    DeclNpc(0,       0,       0,       0,    508,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       13100,   204699,  305,  508,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(b'\x00\x00\x00\x00\x00\x009C\x00\x000A\x00\x00aC\xcd\xccL>\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xab\xaa*>\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xcd\xccL>\x00\x00\x00\x00\x00\x00\x00\x80\xab\xaa\xf6\xc1\xcd\xcc\x0c\xc0\x00\x00\x80?\x00\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

    DeclActor(3500,    0,       155000,  1200,    3500,    1000,    155000,  0x007C, 0,  3,  0x0000)

    ScpFunction((
        "Function_0_3AC",   # 00, 0
        "Function_1_3F8",   # 01, 1
        "Function_2_517",   # 02, 2
        "Function_3_747",   # 03, 3
        "Function_4_82B",   # 04, 4
        "Function_5_AAF",   # 05, 5
        "Function_6_C02",   # 06, 6
        "Function_7_C63",   # 07, 7
        "Function_8_CC4",   # 08, 8
        "Function_9_CD7",   # 09, 9
        "Function_10_5036", # 0A, 10
        "Function_11_5061", # 0B, 11
        "Function_12_508C", # 0C, 12
        "Function_13_50B7", # 0D, 13
        "Function_14_50E2", # 0E, 14
        "Function_15_510D", # 0F, 15
        "Function_16_5131", # 10, 16
        "Function_17_5143", # 11, 17
        "Function_18_5155", # 12, 18
        "Function_19_5167", # 13, 19
        "Function_20_5173", # 14, 20
        "Function_21_51C1", # 15, 21
        "Function_22_520F", # 16, 22
        "Function_23_5238", # 17, 23
        "Function_24_5282", # 18, 24
        "Function_25_52AF", # 19, 25
        "Function_26_52DB", # 1A, 26
        "Function_27_52FE", # 1B, 27
        "Function_28_5347", # 1C, 28
        "Function_29_5390", # 1D, 29
        "Function_30_53AC", # 1E, 30
        "Function_31_5420", # 1F, 31
        "Function_32_6DE5", # 20, 32
        "Function_33_6E2E", # 21, 33
        "Function_34_6E98", # 22, 34
        "Function_35_76A5", # 23, 35
        "Function_36_76B5", # 24, 36
        "Function_37_76C4", # 25, 37
        "Function_38_76D6", # 26, 38
        "Function_39_76E8", # 27, 39
        "Function_40_76F4", # 28, 40
        "Function_41_7742", # 29, 41
        "Function_42_7790", # 2A, 42
        "Function_43_77B7", # 2B, 43
    ))


    label("Function_3_747")

    import TiosBed
    TiosBed.ShowMenu()
    Return()

    # Function_3_747 end


    label("Function_0_3AC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BD")
    Event(0, 4)

    label("loc_3BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, 0x110), scpexpr(EXPR_END)), "loc_3D1")
    OP_AA(0x110)
    Event(0, 31)
    Jump("loc_3F7")

    label("loc_3D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, 0x111), scpexpr(EXPR_END)), "loc_3E5")
    OP_AA(0x111)
    Event(0, 34)
    Jump("loc_3F7")

    label("loc_3E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, 0xD4C), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, 0x112), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F7")
    Event(0, 8)

    label("loc_3F7")

    Return()

    # Function_0_3AC end


    label("Function_1_3F8")

    OP_F0(0x1, 0x320)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, 0xD4C), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, 0x112), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_414")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_414")

    OP_1B(0x1, 0x0, 0x5)
    OP_B7(0x0, 0x0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, 0xD4B), scpexpr(EXPR_TEST_SCENA_FLAGS, 0xD4C), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_431")
    OP_B7(0x1, 0x0, 0x80)

    label("loc_431")

    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_72(0x2, 0x1000)
    OP_73(0x2, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, 0xD4C), scpexpr(EXPR_END)), "loc_4BE")
    OP_72(0x2, 0x4)
    OP_76(0xFF, "magi10_add", 0x1, 0x1)
    OP_76(0xFF, "magi11_add", 0x1, 0x1)
    OP_76(0xFF, "point_add", 0x1, 0x1)
    OP_76(0xFF, "magi_04_add", 0x0, 0x1)
    OP_70(0x1, 0x96)
    Jump("loc_50A")

    label("loc_4BE")

    OP_76(0xFF, "magi10_add", 0x0, 0x1)
    OP_76(0xFF, "magi11_add", 0x0, 0x1)
    OP_76(0xFF, "point_add", 0x0, 0x1)
    OP_76(0xFF, "magi_04_add", 0x1, 0x1)
    OP_70(0x1, 0x3C)

    label("loc_50A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, 0xD4C), scpexpr(EXPR_END)), "loc_516")
    Call(0, 42)

    label("loc_516")

    Return()

    # Function_1_3F8 end


    label("Function_2_517")

    OP_A2(0x8, 0x10)
    OP_53(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, 0xE78), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FE")

    ChrTalk(
        0x8,
        "……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F……完全失去意识了，\x01",
            "似乎没有生命危险。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F真是个惊人的对手啊……\x01",
            "面对我们全体成员，竟然还能战斗到如此程度。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F不愧是『风之剑圣』……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_43(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_621")

    ChrTalk(
        0x10A,
        "#00603F哼……总算战胜他了。\x02",
    )

    CloseMessageWindow()

    label("loc_621")


    ChrTalk(
        0x101,
        (
            "#00003F小滴肯定很担心亚里欧斯先生，\x01",
            "真想马上把他送到梅尔卡瓦……\x02\x03",
            "#00001F……但玛丽亚贝尔小姐和伊安律师\x01",
            "还在前方等着我们。\x02\x03",
            "#00003F虽然有些对不起他，\x01",
            "但这件事还是暂时推后吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F是啊……我们先走吧。\x02",
    )

    CloseMessageWindow()
    OP_A9(0xE78)
    Jump("loc_743")

    label("loc_6FE")


    ChrTalk(
        0x8,
        "……………………………………\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "似乎完全失去意识了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_743")

    OP_54(0x8)
    Return()

    # Function_2_517 end



    label("Function_4_82B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadEffect(0x1, "event/ev202_00.eff")
    OP_68(-340, 13500, 219060, 0)
    OP_6D(0x1D, 0x29, 0x0, 0x0)
    OP_6E(0x258, 0x0)
    OP_6C(0x32AA, 0x0)
    SetChrPos(0x0, 0, 12000, 222000, 180)
    SetChrPos(0x1, 0, 12000, 222000, 180)
    SetChrPos(0x2, 0, 12000, 222000, 180)
    SetChrPos(0x3, 0, 12000, 222000, 180)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_46(0x0, 0x2, 0xB)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_00()
    OP_46(0x0, 0x1, 0x14)
    OP_95(0xFE, 0xFFFFFF10, 0x2EE0, 0x35408, 0x9C4, 0x0)
    OP_00()
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_46(0x1, 0x2, 0xB)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_00()
    OP_46(0x1, 0x1, 0x14)
    OP_95(0xFE, 0xFFFFFA74, 0x2EE0, 0x354A8, 0x9C4, 0x0)
    OP_00()
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_46(0x2, 0x2, 0xB)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_00()
    OP_46(0x2, 0x1, 0x14)
    OP_95(0xFE, 0x424, 0x2EE0, 0x354C6, 0x9C4, 0x0)
    OP_00()
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_46(0x3, 0x2, 0xB)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_00()
    OP_46(0x3, 0x1, 0x14)
    OP_95(0xFE, 0xFFFFF524, 0x2EE0, 0x35638, 0x9C4, 0x0)
    OP_00()
    OP_48(0x3, 0x1)
    Sleep(500)
    OP_E2(0x2)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_4_82B end


    label("Function_5_AAF")

    EventBegin(0x0)
    OP_E2(0x3)
    LoadEffect(0x1, "event/evwarp.eff")
    Sound(936, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_46(0x0, 0x2, 0xB)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    OP_00()
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_46(0x1, 0x2, 0xB)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    OP_00()
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_46(0x2, 0x2, 0xB)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    OP_00()
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_46(0x3, 0x2, 0xB)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    OP_00()
    Sleep(1000)
    NewScene("m9008", 102, 0, 0)
    OP_07()
    Return()

    # Function_5_AAF end


    label("Function_6_C02")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C1A")
    LoadChrToIndex("chr/ch03150.itc", 0x23)

    label("loc_C1A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C32")
    LoadChrToIndex("chr/ch03250.itc", 0x23)

    label("loc_C32")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C4A")
    LoadChrToIndex("chr/ch02950.itc", 0x23)

    label("loc_C4A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C62")
    LoadChrToIndex("chr/ch00950.itc", 0x23)

    label("loc_C62")

    Return()

    # Function_6_C02 end


    label("Function_7_C63")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C7B")
    LoadChrToIndex("chr/ch03150.itc", 0x24)

    label("loc_C7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C93")
    LoadChrToIndex("chr/ch03250.itc", 0x24)

    label("loc_C93")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CAB")
    LoadChrToIndex("chr/ch02950.itc", 0x24)

    label("loc_CAB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CC3")
    LoadChrToIndex("chr/ch00950.itc", 0x24)

    label("loc_CC3")

    Return()

    # Function_7_C63 end


    label("Function_8_CC4")

    EventBegin(0x0)
    OP_21(0xFA0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x5)
    Return()

    # Function_8_CC4 end


    label("Function_9_CD7")

    Battle("BattleInfo_2B8", 0x0, 0x0, 0x100, 0x45, 0xFF)

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01400.itp")
    LoadChrToIndex("apl/ch51233.itc", 0x1E)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    Call(0, 6)
    Call(0, 7)
    LoadChrToIndex("chr/ch02450.itc", 0x25)
    LoadChrToIndex("monster/ch85450.itc", 0x26)
    LoadChrToIndex("monster/ch60051.itc", 0x27)
    LoadChrToIndex("monster/ch85550.itc", 0x28)
    LoadChrToIndex("monster/ch60051.itc", 0x29)
    LoadChrToIndex("apl/ch51743.itc", 0x2A)
    LoadEffect(0x0, "event/ev602_01.eff")
    LoadEffect(0x1, "event/eva06_02.eff")
    LoadEffect(0x2, "event/eva06_01.eff")
    LoadEffect(0x3, "event/ev17013.eff")
    SoundLoad(128)
    SoundLoad(825)
    SoundLoad(832)
    SoundLoad(881)
    SoundLoad(833)
    SoundLoad(4064)
    SoundLoad(4077)
    SoundLoad(4065)
    SoundLoad(4066)
    SoundLoad(4067)
    SetChrPos(0x101, 0, 25000, 181800, 0)
    SetChrPos(0x102, 1100, 25000, 181100, 0)
    SetChrPos(0x103, 200, 25000, 180000, 0)
    SetChrPos(0x104, -1100, 25000, 180750, 0)
    SetChrPos(0xF4, -650, 25000, 179250, 0)
    SetChrPos(0xF5, 850, 25000, 179000, 0)
    OP_A3(0x4, 0x80)
    OP_A5(0x4, 0x8000)
    OP_A3(0x5, 0x80)
    OP_A5(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    OP_A3(0x8, 0x80)
    OP_A2(0x8, 0x8000)
    SetChrPos(0x8, 0, 12000, 210000, 180)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x9, 0x80)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, 0, 12000, 198500, 0)
    SetChrChipByIndex(0xA, 0x26)
    SetChrSubChip(0xA, 0x0)
    OP_A2(0xA, 0x20)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xA, -2500, 12000, 211500, 180)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A3(0xA, 0x80)
    OP_A5(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x0)
    OP_A2(0xB, 0x20)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xB, 2500, 12000, 211500, 180)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A3(0xB, 0x80)
    OP_A5(0xB, 0x8000)
    BeginChrThread(0xA, 2, 0, 29)
    BeginChrThread(0xB, 2, 0, 29)
    OP_A3(0xC, 0x80)
    OP_68(0, 13000, 180500, 0)
    OP_6D(0x0, 0x26, 0x0, 0x0)
    OP_6E(0x258, 0x0)
    OP_6C(0x5208, 0x0)
    Sleep(500)
    OP_68(0, 13000, 188000, 4500)
    OP_6D(0x0, 0x26, 0x0, 0x1194)
    OP_6E(0x258, 0x1194)
    OP_6C(0x5DC0, 0x1194)
    FadeToBright(1000, 0)
    OP_46(0x101, 0x1, 0xF)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
    OP_00()
    Sleep(50)
    OP_46(0x103, 0x1, 0xF)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
    OP_00()
    Sleep(50)
    OP_46(0x102, 0x1, 0xF)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
    OP_00()
    Sleep(50)
    OP_46(0x104, 0x1, 0xF)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
    OP_00()
    Sleep(50)
    OP_46(0xF4, 0x1, 0xF)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
    OP_00()
    Sleep(50)
    OP_46(0xF5, 0x1, 0xF)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
    OP_00()
    OP_0D()
    Sleep(2400)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x8,
        "男性的声音",
        "#4064V#6P#30W#16A你们到了啊。\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_48(0xF5, 0x1)
    OP_6F(0x79)
    PlayBgm("ed7356.ogg", 0)
    BeginChrThread(0x101, 0, 0, 10)
    Sleep(50)
    BeginChrThread(0x102, 0, 0, 11)
    Sleep(50)
    BeginChrThread(0x103, 0, 0, 12)
    Sleep(50)
    BeginChrThread(0x104, 0, 0, 13)
    Sleep(50)
    BeginChrThread(0xF4, 0, 0, 14)
    Sleep(50)
    BeginChrThread(0xF5, 0, 0, 15)
    OP_68(-410, 13300, 205280, 4000)
    OP_6D(0x2F, 0x10, 0x0, 0xFA0)
    OP_6E(0x258, 0xFA0)
    OP_6C(0x3F34, 0xFA0)
    OP_6F(0x79)
    OP_48(0x101, 0x0)
    OP_48(0x104, 0x0)
    OP_48(0x103, 0x0)
    OP_48(0x102, 0x0)
    OP_48(0xF4, 0x0)
    OP_48(0xF5, 0x0)

    ChrTalk(
        0x101,
        "#00001F#12P……亚里欧斯先生。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#12P已经不穿那套\x01",
            "长官制服了啊……？\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_5B(0xE, 0x118, 0x23, 0x3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "虽然库罗伊斯先生诚意邀请，\x01",
            "但对我而言，终究还是太过勉强。\x02\x03",
            "既然独立无效宣言已经发布，\x01",
            "我也就没资格再穿那套衣服了。\x02\x03",
            "如今的我，既不是国防长官也不是游击士……\x02\x03",
            "站在这里的，\x01",
            "只是一名飘泊的剑士。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_43(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_138A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1364")
    OP_FC(0xFFF4)
    Jump("loc_1367")

    label("loc_1364")

    OP_FC(0xC)

    label("loc_1367")


    ChrTalk(
        0x10A,
        "#00600F#13P马克莱因……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_13D9")

    label("loc_138A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_43(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13D9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13B4")
    OP_FC(0xFFF4)
    Jump("loc_13B7")

    label("loc_13B4")

    OP_FC(0xC)

    label("loc_13B7")


    ChrTalk(
        0x109,
        "#10113F#13P亚里欧斯先生……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_13D9")


    ChrTalk(
        0x102,
        "#00108F#12P你为何如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#12P……未免也太古板了。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00004F#12P……哈哈，真没办法啊……\x02\x03",
            "#00008F想问的事情实在太多了，\x01",
            "一时还无法理清思绪……\x02\x03",
            "#00000F不过，我们可以先来\x01",
            "『核对答案』吗……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01404F好#5P——我原本就有这个打算。\x02\x03",
            "#01400F尽管问吧……\x01",
            "除了一件事情之外，\x01",
            "我全都可以回答。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#12P那么……\x02",
    )

    CloseMessageWindow()
    OP_AA(0x3)
    OP_AA(0x0)
    OP_AA(0x1)
    OP_AA(0x2)

    label("loc_154C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, 0x3), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_358B")
    FadeToDark(300, 0, 100)
    OP_0D()
    MenuCmd(0x0, 0x0)
    MenuCmd(0x1, 0x0, "五年前的『事故』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, 0x0), scpexpr(EXPR_END)), "loc_1599")
    MenuCmd(0x1, 0x0, "与伊安律师之间的关系")

    label("loc_1599")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, 0x1), scpexpr(EXPR_END)), "loc_15B8")
    MenuCmd(0x1, 0x0, "黑之竞拍会上的琪雅")

    label("loc_15B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, 0x2), scpexpr(EXPR_END)), "loc_15D5")
    MenuCmd(0x1, 0x0, "盖伊身亡的那一天")

    label("loc_15D5")

    MenuCmd(0x2, 0x0, 0xFFFF, 0xFFFF, 0x0)
    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_160F"),
        (1, "loc_2199"),
        (2, "loc_2ADB"),
        (3, "loc_357E"),
        (SWITCH_DEFAULT, "loc_3586"),
    )


    label("loc_160F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_205A")

    ChrTalk(
        0x101,
        (
            "#00008F#12P……抱歉，要提及\x01",
            "您的沉痛往事了……\x02\x03",
            "#00001F五年前那起『事故』的内情，\x01",
            "可以告诉我们吗……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01403F#5P好……\x01",
            "现在已经没有隐瞒的必要了。\x02\x03",
            "#01400F五年前，在大道上发生了\x01",
            "运输车爆炸事故……\x02\x03",
            "正如你们所觉察到的一样，\x01",
            "那是因帝国与共和国之间的\x01",
            "谍报战而导致的结果。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F#12P果然……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_43(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1880")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1773")
    OP_FC(0xFFF4)
    Jump("loc_1776")

    label("loc_1773")

    OP_FC(0xC)

    label("loc_1776")


    ChrTalk(
        0x10A,
        "#00608F#13P………………………………\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#01402F#5P呵呵，一科肯定\x01",
            "掌握到这一事实了吧？\x02\x03",
            "#01403F但由于高层对帝国派\x01",
            "和共和国派有所顾虑，于是便\x01",
            "理所当然地将这件事压下了……\x02\x03",
            "#01400F虽然我对此感到失望，\x01",
            "但事到如今，已经没有怨恨了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#00606F#13P……我很抱歉。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_1880")


    ChrTalk(
        0x103,
        (
            "#00208F#12P……因为那起事故，亚里欧斯先生的\x01",
            "妻子和小滴才会……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01403F#5P是的……纱绫因此丧命，\x01",
            "滴则失明了。\x02\x03",
            "#01408F自那之后的五年间……\x01",
            "两国的谍报机构日趋完善，\x01",
            "无谓的破坏工作也渐渐绝迹……\x02\x03",
            "#01401F但在长达数十年的暗斗过程中，\x01",
            "曾出现过很多和\x01",
            "纱绫一样的受害者。\x02\x03",
            "#01403F罗伊德，其中也包括你的父母，\x01",
            "还有伊安律师的家人。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#00005F#12P#4S！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00307F#12P什么……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, 0xBE6), scpexpr(EXPR_END)), "loc_1BAA")

    ChrTalk(
        0x102,
        (
            "#00101F#12P罗、罗伊德的父母\x01",
            "不是在某起……！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#12P在十五年前的某起飞船事故中……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12P嗯……我以前和你们说过。\x02\x03",
            "#00008F但我那时刚刚懂事，\x01",
            "几乎没留下什么印象……\x02\x03",
            "#00013F也就是说……\x01",
            "伊安律师的家人也是在那时……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CAB")

    label("loc_1BAA")


    ChrTalk(
        0x102,
        "#00105F#12P罗、罗伊德的父母！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#12P……第一次听说……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12P我的父母……\x01",
            "在十五年前飞船刚开始投入运行时，\x01",
            "遭遇事故而去世了……\x02\x03",
            "#00008F但我那时刚刚懂事，\x01",
            "几乎没留下什么印象……\x02\x03",
            "#00013F也就是说……\x01",
            "伊安律师的家人也是在那时……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CAB")


    ChrTalk(
        0x8,
        (
            "#01403F#5P嗯，他的妻子和孩子\x01",
            "也乘坐了那班飞船。\x02\x03",
            "我至少还有滴……\x01",
            "而他却失去了一切。\x01",
            "那种伤痛，非我所能想象。\x02\x03",
            "#01400F另外，盖伊和伊安律师就是\x01",
            "在当时作为死难者家属而相识的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#12P……………………………………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_43(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DE0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DB5")
    OP_FC(0xFFF4)
    Jump("loc_1DB8")

    label("loc_1DB5")

    OP_FC(0xC)

    label("loc_1DB8")


    ChrTalk(
        0x109,
        "#10106F#13P……竟、竟有这种事……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_1DE0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_43(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E3E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E0A")
    OP_FC(0xFFF4)
    Jump("loc_1E0D")

    label("loc_1E0A")

    OP_FC(0xC)

    label("loc_1E0D")


    ChrTalk(
        0x10A,
        (
            "#00606F#13P这是连一科\x01",
            "都没有掌握的情报……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_1E3E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_43(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1EA6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E68")
    OP_FC(0xFFF4)
    Jump("loc_1E6B")

    label("loc_1E68")

    OP_FC(0xC)

    label("loc_1E6B")


    ChrTalk(
        0x105,
        (
            "#10401F#13P……原来如此，\x01",
            "没想到还有这样一番往事……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_1EA6")


    ChrTalk(
        0x8,
        (
            "#01403F#5P……在五年前的那起事件发生之后，\x01",
            "我辞去了警察一职，\x01",
            "加入游击士协会。\x02\x03",
            "作出这个决定的理由有很多，比如对警察\x01",
            "感到失望，筹措滴的住院费用等等……\x02\x03",
            "#01408F但实际上，我也许只是\x01",
            "想逃避失去纱绫的悲伤罢了。\x02\x03",
            "#01400F为此，我才会一头扎进\x01",
            "没完没了的游击士工作中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#12P亚里欧斯先生……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_43(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2052")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1FFC")
    OP_FC(0xFFF4)
    Jump("loc_1FFF")

    label("loc_1FFC")

    OP_FC(0xC)

    label("loc_1FFF")


    ChrTalk(
        0x106,
        (
            "#10706F#13P（……过去被『银』暗杀的那些人的家人，\x01",
            "　肯定也会如此悲伤吧……）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2052")

    OP_A9(0x0)
    Jump("loc_2194")

    label("loc_205A")


    ChrTalk(
        0x8,
        (
            "#01403F#5P五年前，发生在大路上的\x01",
            "那起运输车爆炸事故\x01",
            "夺走了纱绫的生命和滴的光明……\x02\x03",
            "#01401F那是因帝国与共和国之间的\x01",
            "谍报战而导致的结果。\x02\x03",
            "另外，十五年前的那起飞船事故\x01",
            "也是由于同样的原因而发生的。\x02\x03",
            "#01403F那起事故……使盖伊和你的父母，\x01",
            "还有伊安律师的家人不幸丧生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#12P……………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_2194")

    Jump("loc_3586")

    label("loc_2199")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, 0x1), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A1B")

    ChrTalk(
        0x101,
        (
            "#00006F#12P……有件事情，\x01",
            "我一直怀有疑问。\x02\x03",
            "#00001F那就是您为何会与迪塔先生\x01",
            "他们有所往来。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#01405F#5P哦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#12P……虽然迪塔叔叔和贝尔对\x01",
            "经济、金融，以及与库罗伊斯家族\x01",
            "存在关联的教团了解甚详……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#12P但关于帝国与共和国的暗斗……\x02\x03",
            "#00301F如果连这些情况都了如指掌，\x01",
            "就未免有些奇怪了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#12P双方原本毫不相干……\x02\x03",
            "#00201F然而，迪塔先生就任为总统之后，\x01",
            "却任命亚里欧斯先生为国防长官……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_43(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2423")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_238D")
    OP_FC(0xFFF4)
    Jump("loc_2390")

    label("loc_238D")

    OP_FC(0xC)

    label("loc_2390")


    ChrTalk(
        0x10A,
        (
            "#00606F#13P……原来如此，是这样啊。\x02\x03",
            "#00601F也就是说，将他们联系起来的人\x01",
            "就是伊安律师吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00001F#12P嗯……\x01",
            "亚里欧斯先生，没错吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2588")

    label("loc_2423")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_43(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24E5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_244D")
    OP_FC(0xFFF4)
    Jump("loc_2450")

    label("loc_244D")

    OP_FC(0xC)

    label("loc_2450")


    ChrTalk(
        0x105,
        (
            "#10406F#13P……原来如此，是这样啊。\x02\x03",
            "#10401F也就是说，是那个大胡子熊律师\x01",
            "在中间牵线搭桥啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00001F#12P嗯……\x01",
            "亚里欧斯先生，没错吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2588")

    label("loc_24E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_43(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2588")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_250F")
    OP_FC(0xFFF4)
    Jump("loc_2512")

    label("loc_250F")

    OP_FC(0xC)

    label("loc_2512")


    ChrTalk(
        0x109,
        (
            "#10108F#13P难道……\x02\x03",
            "#10101F将他们联系起来的人\x01",
            "就是伊安律师……？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00001F#12P嗯……\x01",
            "亚里欧斯先生，没错吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2588")


    ChrTalk(
        0x8,
        "#01404F#5P呵呵……正是如此。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    CreatePortrait(0, 224, 0, 480, 256, 10, 16, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02200.itp")
    OP_CB(0x0, 0x3, 0xAAFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    OP_5B(0xE, 0x118, 0xFFFF, 0x3)

    AnonymousTalk(
        0x8,
        (
            "#01402F和你们一样，在从事警察工作时，\x01",
            "我和盖伊也屡受伊安律师的关照，\x01",
            "他提供的情报给我们带来了很大帮助。\x02\x03",
            "在镇压教团据点的作战中，\x01",
            "伊安律师也以民间顾问的身份\x01",
            "给我们提供了协助。\x02\x03",
            "#01403F在我成为游击士之后……\x01",
            "仍然频繁与他交换情报。\x02",
        )
    )

    CloseMessageWindow()
    CreatePortrait(1, 224, 0, 480, 256, 65296, 16, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02800.itp")
    OP_CB(0x1, 0x3, 0xAAFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)
    OP_5B(0xE, 0x118, 0xFFFF, 0x3)

    AnonymousTalk(
        0x8,
        (
            "#01403F#5P而律师通过ＩＢＣ的法务工作，\x01",
            "与库罗伊斯父女交情颇深。\x02\x03",
            "#01401F于是，一切情报与要素\x01",
            "都集中、整合在了律师的手中……\x02\x03",
            "库罗伊斯先生在律师的诱导之下，\x01",
            "通过各种政治工作与『至宝』的力量，\x01",
            "成功实现了克洛斯贝尔的独立。\x02\x03",
            "#01403F但他却不知道，律师先生和玛丽亚贝尔小姐\x01",
            "一直在暗中推进他们的真正计划。\x02",
        )
    )

    CloseMessageWindow()
    FadeToBright(800, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        "#00013F#12P真正计划……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#12P就是『碧零计划』吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01403F#5P不错……律师很快就察觉到了\x01",
            "纱绫那起事故背后的真相。\x02\x03",
            "于是，他向我说明了情况……\x01",
            "而我决定协助他们完成此项计划。\x02\x03",
            "#01400F这就是事情的全部经过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#12P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#12P一切都在伊安律师和\x01",
            "玛丽亚贝尔小姐的掌控之中……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#12P……真是惊人。\x02",
    )

    CloseMessageWindow()
    OP_A9(0x1)
    Jump("loc_2AD6")

    label("loc_2A1B")


    ChrTalk(
        0x8,
        (
            "#01403F#5P将库罗伊斯先生和我这两个\x01",
            "毫无关系的人联系起来的，\x01",
            "正是伊安律师。\x02\x03",
            "伊安律师很快就察觉到了\x01",
            "五年前那起事故的真相，\x01",
            "并邀请我参与『碧零计划』……\x02\x03",
            "#01400F而我也接受了他的邀请。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AD6")

    Jump("loc_3586")

    label("loc_2ADB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, 0x2), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_345B")

    ChrTalk(
        0x101,
        (
            "#00006F#12P……还有一件事，\x01",
            "我也怀有疑问……\x02\x03",
            "#00013F把琪雅从『太阳堡垒』的地下\x01",
            "带出来的人就是您吧？\x02\x03",
            "另外，把她和预计在『黑之竞拍会』拍卖的\x01",
            "罗赞贝尔克人偶调包的人应该也是您吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#12P说、说起来……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#12P这个问题至今都没有\x01",
            "完全解明呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01404F#5P不错，正是如此。\x02\x03",
            "#01402F但这件事情的主导者并非律师，\x01",
            "而是玛丽亚贝尔小姐。\x02",
        )
    )

    CloseMessageWindow()
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis303.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis304.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    OP_5B(0xE, 0x118, 0xFFFF, 0x3)

    AnonymousTalk(
        0x8,
        (
            "#01403F她似乎完全掌握了\x01",
            "约亚西姆的动向……\x02\x03",
            "#01401F凭借她的传送术，我们轻易\x01",
            "抵达了最底层的祭坛，\x01",
            "并把那孩子从摇篮中释放。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    OP_5B(0xE, 0x118, 0xFFFF, 0x3)

    AnonymousTalk(
        0x8,
        (
            "#01403F之后，我把那孩子和\x01",
            "从雷米菲利亚运送过来的\x01",
            "罗赞贝尔克人偶调了包。\x02\x03",
            "#01400F那个罗赞贝尔克人偶也是\x01",
            "玛丽亚贝尔小姐准备的，目的是\x01",
            "为了避免让鲁巴彻的人看出端倪。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xE, 0x118, 0xFFFF, 0x3)

    AnonymousTalk(
        0x102,
        "#00106F……竟连那种事都考虑到了……\x02",
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F#12P不过……\x01",
            "这种行为对于玛丽亚贝尔小姐\x01",
            "又有什么意义呢？\x02\x03",
            "#00013F如果他们为了实现计划，需要得到琪雅，\x01",
            "只要把她看管好不就行了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01403F#5P原因之一，是要把『黑月』牵扯进来，\x01",
            "令鲁巴彻颜面扫地，\x01",
            "踏出自取灭亡的第一步……\x02\x03",
            "#01400F如果那孩子在竞拍会的\x01",
            "现场突然醒来，\x01",
            "玛丽亚贝尔小姐肯定会采取行动。\x02\x03",
            "我想，她应该会在惊讶的客人和\x01",
            "马尔克尼的面前抬出ＩＢＣ的名号，\x01",
            "从而接收那个孩子。\x02\x03",
            "#01404F如果『黑月』在那时采取行动，\x01",
            "情况恐怕会有所不同……\x02\x03",
            "不过，我当时也\x01",
            "潜伏在会场内。\x02\x03",
            "#01402F无论事态如何发展，\x01",
            "我们都足以掌控整个局势。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12P该怎么说呢……\x01",
            "准备得也太周全了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F#12P计划实在太缜密了……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_43(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_315F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_311D")
    OP_FC(0xFFF4)
    Jump("loc_3120")

    label("loc_311D")

    OP_FC(0xC)

    label("loc_3120")


    ChrTalk(
        0x106,
        (
            "#10708F#13P……我当时确实\x01",
            "感觉到还有其他人\x01",
            "潜伏在会场……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_315F")


    ChrTalk(
        0x8,
        (
            "#01403F#5P而另一个原因……\x02\x03",
            "#01401F就是让『至宝』在那种\x01",
            "特殊情况下苏醒，\x01",
            "以便确认她的潜在能力。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#00205F#12P确认琪雅的潜在能力？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#12P什、什么意思……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01403F#5P不清楚，玛丽亚贝尔小姐\x01",
            "只说了这么多。\x02\x03",
            "#01408F那种外部环境，或许也是让\x01",
            "那孩子从长久的沉睡中\x01",
            "苏醒的条件之一吧……\x02\x03",
            "#01400F不管怎么说，不知是女神的引导，\x01",
            "还是单纯的偶然，\x01",
            "她在你们面前苏醒了。\x02\x03",
            "对于玛丽亚贝尔小姐来说，\x01",
            "这自然是出乎意料的状况……\x02\x03",
            "#01403F不过，她似乎毫不介意\x01",
            "那孩子被你们收养，\x01",
            "并与你们一起生活。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#12P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12P……想不明白，\x01",
            "真是莫名其妙啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12P……贝尔……\x01",
            "到底有何打算呢……？\x02",
        )
    )

    CloseMessageWindow()
    OP_A9(0x2)
    Jump("loc_3579")

    label("loc_345B")


    ChrTalk(
        0x8,
        (
            "#01403F#5P从『太阳堡垒』释放琪雅，\x01",
            "并将她带进竞拍会场的行动，\x01",
            "都是在玛丽亚贝尔小姐的主导下进行的。\x02\x03",
            "#01408F其目的是为了\x01",
            "诱导鲁巴彻走向毁灭，\x01",
            "控制住局势的发展……\x02\x03",
            "#01401F同时，也是为了让那孩子\x01",
            "在特殊的情况下苏醒，\x01",
            "以便确认她的潜在能力。\x02\x03",
            "#01403F至于其它事情，\x01",
            "很遗憾，我也不清楚。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3579")

    Jump("loc_3586")

    label("loc_357E")

    OP_A9(0x3)
    Jump("loc_3586")

    label("loc_3586")

    Jump("loc_154C")

    label("loc_358B")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00006F#12P#30W……那么……\x02\x03",
            "#00008F大哥去世那天的真相……\x01",
            "……可以告诉我吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_43(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_363F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3620")
    OP_FC(0xFFF4)
    Jump("loc_3623")

    label("loc_3620")

    OP_FC(0xC)

    label("loc_3623")


    ChrTalk(
        0x10A,
        "#00601F#13P……………\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_363F")


    ChrTalk(
        0x103,
        "#00208F#12P……啊………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01403F#5P#30W………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    ChrTalk(
        0x8,
        "#01400F#5P#30W好。\x02",
    )

    CloseMessageWindow()
    OP_21(0xFA0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22()
    Sound(883, 0, 60, 0)
    Sleep(2300)
    Sound(128, 2, 10, 0)
    Sleep(150)
    OP_25(0x80, 0x14)
    Sleep(150)
    OP_25(0x80, 0x1E)
    Sleep(150)
    OP_25(0x80, 0x28)
    Sleep(150)
    OP_25(0x80, 0x32)
    Sleep(500)
    OP_5B(0xE, 0x118, 0xFFFF, 0x3)

    AnonymousTalk(
        0x8,
        (
            "#3C#30W……纱绫去世，我离开\x01",
            "警察局之后，又过了两年……\x02\x03",
            "在那期间，我参与伊安律师他们的计划，\x01",
            "并完成了几项工作……\x02\x03",
            "全都是些不可告人……\x01",
            "暗藏阴谋的工作。\x02\x03",
            "然而，连同协会成员在内，\x01",
            "大家都没有察觉到\x01",
            "那些情况。\x02\x03",
            "唯一例外的人就是我过去的搭档……\x01",
            "盖伊·班宁斯。\x02",
        )
    )

    CloseMessageWindow()
    PlayBgm("ed7560.ogg", 0)
    CreatePortrait(0, 224, 0, 480, 256, 0, 16, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07800.itp")
    OP_CB(0x0, 0x3, 0xEEFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    OP_5B(0xE, 0x118, 0xFFFF, 0x3)

    AnonymousTalk(
        0x8,
        (
            "#3C#30W盖伊……那家伙凭借着\x01",
            "惊人的直觉和顽强的毅力，\x01",
            "接近了各种阴谋与秘密的核心。\x02\x03",
            "帝国与共和国的暗中斗争……\x02\x03",
            "哈尔特曼议长和鲁巴彻，\x01",
            "以及Ｄ∴Ｇ教团残余势力的动向……\x02\x03",
            "甚至连深藏于幕后的\x01",
            "库罗伊斯家族的计划都……\x02\x03",
            "于是──\x02\x03",
            "在那个雨天，盖伊把我叫到了\x01",
            "当时刚刚开工的兰花塔\x01",
            "施工现场……\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFF000000, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_25(0x80, 0x3C)
    Sleep(200)
    OP_25(0x80, 0x46)
    Sleep(200)
    OP_25(0x80, 0x50)
    Sleep(200)
    OP_25(0x80, 0x5A)
    Sleep(200)
    OP_25(0x80, 0x64)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFF000000, 0x0, "c_vis305.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    OP_5B(0xE, 0x118, 0xFFFF, 0x3)

    AnonymousTalk(
        0x8,
        (
            "#3C#30W当然，盖伊并没有\x01",
            "掌握计划的详细情况……\x02\x03",
            "但他的推测准确得惊人，\x01",
            "基本把握了整个计划的全貌。\x02\x03",
            "包括库罗伊斯家族利用教团和黑手党，\x01",
            "趁势进军政坛……\x02\x03",
            "主导袭击克洛斯贝尔市的行动，\x01",
            "并伪造出是国外势力所为的假象，\x01",
            "以此来煽动民众的独立情绪……\x02\x03",
            "甚至连利用库罗伊斯家族的『某种东西』\x01",
            "来镇压、控制整个大陆的计划都被他……\x02\x03",
            "实在是令人\x01",
            "难以置信。\x02\x03",
            "随后──\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFF000000, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    CreatePortrait(0, 0, 0, 512, 512, 0, 65296, 512, 512, 0, 0, 512, 512, 0xFF000000, 0x0, "c_vis330.itp")
    CreatePortrait(1, 0, 0, 512, 512, 0, 0, 512, 512, 0, 0, 512, 512, 0xFFFFFF, 0x0, "c_vis331.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x7D0, 0x0)
    OP_CC(0x0, 0x0, 0x0)
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0xFFFC5680, 0x7D0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x0)
    OP_CB(0x1, 0x3, 0xFF000000, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sound(534, 0, 80, 0)
    Sleep(100)
    PlayEffect(0x3, 0x3, 0xC, 0x0, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(372, 0, 40, 0)
    Sleep(200)
    Sound(540, 0, 100, 0)
    Sound(511, 0, 100, 0)
    Sleep(400)
    Sound(540, 0, 100, 0)
    Sound(372, 0, 40, 0)
    Sound(566, 0, 50, 0)
    Sleep(200)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFF000000, 0x0, "c_vis306.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    Sleep(50)
    BeginChrThread(0x8, 0, 0, 30)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    OP_5B(0xE, 0x118, 0xFFFF, 0x3)

    AnonymousTalk(
        0x8,
        (
            "#3C#30W……盖伊并没有接受我的劝告，\x01",
            "不答应就此罢手不管……\x02\x03",
            "于是我们就在雨中展开了一场殊死搏斗。\x02\x03",
            "论武术水平，我要略胜一筹……\x01",
            "然而，盖伊凭着坚不可摧的意志，\x01",
            "激发出了自身的最大力量。\x02\x03",
            "我们交战数十个回合，\x01",
            "不断消耗对方的体力，\x01",
            "在雨中持续着死战……\x02\x03",
            "最后──\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFF000000, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(800)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFF000000, 0x0, "c_vis307.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(800)
    OP_5B(0xE, 0x118, 0xFFFF, 0x3)

    AnonymousTalk(
        0x8,
        (
            "#3C#30W盖伊他……\x01",
            "丧命了。\x02\x03",
            "把他的旋棍从现场带走的人\x01",
            "自然就是我。\x02\x03",
            "因为我不想让别人根据旋棍上的无数刀痕\x01",
            "而确定犯人的身份。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_12(0x80, 0x3E8, 0x64)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_43(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3FD5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F7E")
    OP_FC(0xFFF4)
    Jump("loc_3F81")

    label("loc_3F7E")

    OP_FC(0xC)

    label("loc_3F81")


    ChrTalk(
        0x109,
        "#10106F#13P#30W竟有这种事……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        "#00208F#12P#30W……………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_402B")

    label("loc_3FD5")


    ChrTalk(
        0x101,
        "#00008F#12P#30W……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#12P#30W……竟有这种事…………\x02",
    )

    CloseMessageWindow()

    label("loc_402B")

    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#01403F#5P#30W……这就是发生在\x01",
            "那个雨天的事情。\x02\x03",
            "#01408F黑手党的成员随后现身，\x01",
            "并将盖伊的徽章取走，\x01",
            "这倒是出乎我的预料……\x02\x03",
            "#01400F不管怎么说，这样一来，\x01",
            "你的疑问已经基本解明了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#12P不。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#01405F#5P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12P您想必也清楚，\x01",
            "大哥的死因是遭到了枪击。\x02\x03",
            "#00001F关于这一点，\x01",
            "您还没有做出解释吧……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01403F#5P……在当警察的时候，\x01",
            "我学会了使用手枪。\x02\x03",
            "#01401F由于对手太过难缠，\x01",
            "我情急之下就用了枪，\x01",
            "这有什么问题吗……？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_43(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_42F7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_425E")
    OP_FC(0xFFF4)
    Jump("loc_4261")

    label("loc_425E")

    OP_FC(0xC)

    label("loc_4261")


    ChrTalk(
        0x10A,
        (
            "#00606F#13P你在说谎，马克莱因。\x02\x03",
            "#00601F在那种殊死搏斗中，\x01",
            "怎么会有取出\x01",
            "其它武器的余暇。\x02\x03",
            "更何况是在对手的背后\x01",
            "射出致命一击，这更加不可能。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4381")

    label("loc_42F7")


    ChrTalk(
        0x101,
        (
            "#00013F#12P您在说谎。\x02\x03",
            "#00006F在那种殊死搏斗中，\x01",
            "根本就没有取出\x01",
            "其它武器的余暇。\x02\x03",
            "#00001F想在对手背后射出致命一击，\x01",
            "就更是不可能了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4381")

    OP_21(0xFA0)

    ChrTalk(
        0x8,
        "#01401F#5P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F#12P嗯，说得有理。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12P到底是谁开枪\x01",
            "击中了盖伊先生……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#12P……请您告诉我们。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 0, 0, 22)
    OP_48(0x8, 0x0)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    OP_22()
    Sleep(10)
    PlayBgm("ed7356.ogg", 0)
    OP_6D(0x2B, 0xD, 0x0, 0x4E20)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#01403F#5P#30W不管你们怎么说，\x01",
            "导致盖伊死亡的，\x01",
            "不是别人，就是我。\x02\x03",
            "#01400F而我……\x01",
            "不惜牺牲过去的搭档，\x01",
            "也要参与这项计划。\x02\x03",
            "到了如今……\x01",
            "甚至还利用年幼少女的心\x01",
            "而推动此计划。\x02\x03",
            "#01403F这一切都是为了纱绫……\x01",
            "还有滴的未来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#12P……亚里欧斯先生……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12P您觉得……小滴会因为\x01",
            "您这种做法而开心吗……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01403F#5P#30W她当然不可能开心。\x02\x03",
            "#01401F然而，\x01",
            "克洛斯贝尔这片土地上的诅咒\x01",
            "令那个孩子失去了母亲和光明。\x02\x03",
            "只要克洛斯贝尔一直\x01",
            "在大陆中处于这个位置，\x01",
            "诅咒就永远不会消失。\x02\x03",
            "#01403F除非发生某种\x01",
            "超越人间常理的『奇迹』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12P……！？\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 0, 0, 23)
    OP_48(0x8, 0x0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#01400F#5P#30W三年前，盖伊他……\x01",
            "完全没有责备过我，经过一番\x01",
            "殊死搏斗之后，丢掉了性命。\x02\x03",
            "而琪雅在成为『至宝』之后，\x01",
            "治好了滴的眼睛。\x02\x03",
            "#01403F我已经……\x01",
            "没有回头的理由了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_6C(0x3C0A, 0x320)
    BeginChrThread(0x8, 0, 0, 24)
    Sleep(500)
    PlayEffect(0x1, 0x1, 0x8, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(250)
    OP_82(0x64, 0x0, 0xBB8, 0x320)
    Sound(825, 2, 50, 0)
    Sound(832, 2, 100, 0)
    Sound(881, 0, 50, 0)
    Sound(833, 0, 50, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#01403F#5P#30W……如果无法认同，\x01",
            "就凭实力来阻止我吧。\x02\x03",
            "#01401F为了给兄长报仇，并夺回重要的人……\x02\x03",
            "#01407F你就用他留下的旋棍\x01",
            "来开拓前进的\x01",
            "道路吧……！\x02",
        )
    )

    CloseMessageWindow()
    OP_21(0xBB8)

    ChrTalk(
        0x101,
        (
            "#00006F#12P……明白了。\x02\x03",
            "#00001F但是，我完全没有\x01",
            "为大哥报仇的想法。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    BeginChrThread(0x101, 0, 0, 16)
    OP_48(0x101, 0x0)
    PlayEffect(0x2, 0x0, 0x101, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(881, 0, 50, 0)
    Sound(833, 0, 50, 0)
    OP_25(0x339, 0x46)
    OP_22()
    Sleep(10)
    PlayBgm("ed7527.ogg", 0)
    OP_6C(0x47C2, 0x4E20)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00003F#12P作为继承了\x01",
            "盖伊·班宁斯的遗志\x01",
            "而成立的小小部门……\x02\x03",
            "#00001F作为承载了小滴\x01",
            "和大家的期望的\x01",
            "『特别任务支援科』……\x02\x03",
            "#00007F我们一定会跨越您这道『壁障』，\x01",
            "带回琪雅……\x01",
            "在真正意义上解决此次事件！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x8,
        "#01405F#5P……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#12P哈哈……\x01",
            "不愧是我们的队长！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#12P这也是为了在兰花塔\x01",
            "等着我们的小滴……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#12P……我们绝对不能退缩……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_43(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B99")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B65")
    OP_FC(0xFFF4)
    Jump("loc_4B68")

    label("loc_4B65")

    OP_FC(0xC)

    label("loc_4B68")


    ChrTalk(
        0x10A,
        (
            "#00604F#13P哼……\x01",
            "真是一群让人头疼的家伙。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_4B99")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_43(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4BF7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4BC3")
    OP_FC(0xFFF4)
    Jump("loc_4BC6")

    label("loc_4BC3")

    OP_FC(0xC)

    label("loc_4BC6")


    ChrTalk(
        0x105,
        (
            "#10402F#13P呵呵……\x01",
            "支援科就是这种感觉呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_4BF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_43(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4C4A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4C21")
    OP_FC(0xFFF4)
    Jump("loc_4C24")

    label("loc_4C21")

    OP_FC(0xC)

    label("loc_4C24")


    ChrTalk(
        0x109,
        "#10107F#13P我会全力援护大家的！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_4C4A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_43(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4CD8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4C74")
    OP_FC(0xFFF4)
    Jump("loc_4C77")

    label("loc_4C74")

    OP_FC(0xC)

    label("loc_4C77")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_43(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4CB2")

    ChrTalk(
        0x106,
        "#10701F#13P我也会……尽己所能！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_4CD8")

    label("loc_4CB2")


    ChrTalk(
        0x106,
        "#10707F#13P我会全力协助各位的！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_4CD8")

    BeginChrThread(0x102, 0, 0, 17)
    BeginChrThread(0x103, 0, 0, 18)
    BeginChrThread(0x104, 0, 0, 19)
    BeginChrThread(0xF4, 0, 0, 20)
    BeginChrThread(0xF5, 0, 0, 21)
    OP_48(0x102, 0x0)
    OP_48(0x103, 0x0)
    OP_48(0x104, 0x0)
    OP_48(0xF4, 0x0)
    OP_48(0xF5, 0x0)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x8,
        "#01404F#4077V#5P#30W#25A呵呵，很好。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x8, 0, 0, 25)
    OP_48(0x8, 0x0)
    Sound(817, 0, 100, 0)
    BeginChrThread(0xA, 3, 0, 27)
    BeginChrThread(0xB, 3, 0, 28)
    OP_48(0xA, 0x3)
    OP_48(0xB, 0x3)
    OP_68(180, 13300, 207000, 20000)
    OP_6D(0x2B, 0xD, 0x0, 0x4E20)
    OP_6C(0x3728, 0x4E20)
    CreatePortrait(0, 65514, 0, 490, 256, 0, 0, 512, 256, 0, 0, 512, 256, 0xFFFFFF, 0x0, "bu01402.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_5B(0xE, 0x118, 0x23, 0x3)
    Sleep(500)
    BeginChrThread(0x8, 0, 0, 26)

    AnonymousTalk(
        0x8,
        (
            "#4065V#40W#55A八叶一刀流·二型奥义传人，\x01",
            "亚里欧斯·马克莱因……\x02\x03",
            "#4066V#60A出于一己私欲，背离正义，\x01",
            "舍弃道德，坚持一意孤行！\x02\x03",
            "#4067V#30A来吧！特别任务支援科！\x02",
        )
    )

    OP_48(0x8, 0x0)
    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(300)
    OP_5B(0x14A, 0x64, 0xFFFF, 0xFFFF)
    SetChrName("罗伊德等人")
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    AnonymousTalk(
        0xFF,
        "#4S#12A哦哦！\x02",
    )

    Sound(2153, 255, 90, 0)
    Sound(2343, 255, 100, 1)
    Sound(2249, 255, 100, 2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_43(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4F62")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4F59")
    OP_FC(0x4)
    Sound(2478, 255, 100, 4)
    Jump("loc_4F62")

    label("loc_4F59")

    OP_FC(0x3)
    Sound(2478, 255, 100, 3)

    label("loc_4F62")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_43(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4F95")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4F8F")
    Sound(2417, 255, 100, 4)
    Jump("loc_4F95")

    label("loc_4F8F")

    Sound(2417, 255, 100, 3)

    label("loc_4F95")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_43(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4FC8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4FC2")
    Sound(2544, 255, 100, 4)
    Jump("loc_4FC8")

    label("loc_4FC2")

    Sound(2544, 255, 100, 3)

    label("loc_4FC8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_43(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4FFB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4FF5")
    Sound(3174, 255, 100, 4)
    Jump("loc_4FFB")

    label("loc_4FF5")

    Sound(3174, 255, 100, 3)

    label("loc_4FFB")

    Sound(2055, 255, 100, 5)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)
    Battle("BattleInfo_2B8", 0x0, 0x0, 0x100, 0x45, 0xFF)
    FadeToDark(0, 0, -1)
    OP_A2(0xA, 0x80)
    OP_A2(0xB, 0x80)
    Call(0, 31)
    Return()

    # Function_9_CD7 end


    label("Function_10_5036")

    OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x1)
    OP_96(0xFE, 0x0, 0x2EE0, 0x318BC, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_10_5036 end


    label("Function_11_5061")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0x460, 0x2EE0, 0x313E4, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_11_5061 end


    label("Function_12_508C")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0x1A4, 0x2EE0, 0x30EB2, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_12_508C end


    label("Function_13_50B7")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFFFB0A, 0x2EE0, 0x3116E, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_13_50B7 end


    label("Function_14_50E2")

    OP_9B(0x0, 0xFE, 0x0, 0x1996, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFFF614, 0x2EE0, 0x313DA, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_14_50E2 end


    label("Function_15_510D")

    OP_9B(0x0, 0xFE, 0x0, 0x1AC2, 0xFA0, 0x1)
    OP_96(0xFE, 0x9EC, 0x2EE0, 0x31312, 0xFA0, 0x0)
    Return()

    # Function_15_510D end


    label("Function_16_5131")

    Sleep(150)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_16_5131 end


    label("Function_17_5143")

    Sleep(300)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_17_5143 end


    label("Function_18_5155")

    Sleep(450)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_18_5155 end


    label("Function_19_5167")

    Sleep(450)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_19_5167 end


    label("Function_20_5173")

    Sleep(600)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5193")
    Sound(540, 0, 50, 0)
    Jump("loc_51B8")

    label("loc_5193")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_51B8")
    Sound(531, 0, 100, 0)

    label("loc_51B8")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_20_5173 end


    label("Function_21_51C1")

    Sleep(750)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_51E1")
    Sound(540, 0, 50, 0)
    Jump("loc_5206")

    label("loc_51E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5206")
    Sound(531, 0, 100, 0)

    label("loc_5206")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_21_51C1 end


    label("Function_22_520F")

    SetChrChipByIndex(0x8, 0x2A)
    OP_A2(0xFE, 0x1000)
    OP_A2(0xFE, 0x20)
    OP_A2(0xFE, 0x2)
    SetChrSubChip(0xFE, 0x0)
    Sleep(125)
    SetChrSubChip(0xFE, 0x1)
    Sleep(125)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    Return()

    # Function_22_520F end


    label("Function_23_5238")

    SetChrChipByIndex(0x8, 0x2A)
    OP_A2(0xFE, 0x1000)
    OP_A2(0xFE, 0x20)
    OP_A2(0xFE, 0x2)
    SetChrSubChip(0xFE, 0x2)
    Sleep(125)
    Sound(932, 0, 60, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(125)
    SetChrSubChip(0xFE, 0x4)
    Sleep(375)
    SetChrSubChip(0xFE, 0x5)
    Sleep(125)
    Sound(859, 0, 100, 0)
    SetChrSubChip(0xFE, 0x6)
    Sleep(125)
    SetChrSubChip(0xFE, 0x7)
    Sleep(500)
    Return()

    # Function_23_5238 end


    label("Function_24_5282")

    SetChrSubChip(0xFE, 0x7)
    Sleep(125)
    SetChrSubChip(0xFE, 0x8)
    Sleep(125)
    SetChrSubChip(0xFE, 0x9)
    Sleep(125)
    SetChrSubChip(0xFE, 0xA)
    Sleep(125)
    Sound(812, 0, 100, 0)
    Sound(531, 0, 50, 0)
    SetChrSubChip(0xFE, 0xB)
    Return()

    # Function_24_5282 end


    label("Function_25_52AF")

    SetChrSubChip(0xFE, 0xB)
    Sleep(125)
    SetChrSubChip(0xFE, 0xC)
    Sleep(125)
    SetChrSubChip(0xFE, 0xD)
    Sleep(125)
    Sound(531, 0, 50, 0)
    SetChrSubChip(0xFE, 0xE)
    Sleep(250)
    Sound(859, 0, 60, 0)
    Sleep(250)
    Return()

    # Function_25_52AF end


    label("Function_26_52DB")

    SetChrSubChip(0xFE, 0xE)
    Sleep(91)
    Sound(540, 0, 40, 0)
    SetChrSubChip(0xFE, 0xF)
    Sleep(91)
    SetChrSubChip(0xFE, 0x10)
    Sleep(91)
    SetChrSubChip(0xFE, 0x11)
    Sleep(364)
    Return()

    # Function_26_52DB end


    label("Function_27_52FE")

    PlayEffect(0x0, 0x5, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x5, 0x2)
    Return()

    # Function_27_52FE end


    label("Function_28_5347")

    PlayEffect(0x0, 0x6, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x6, 0x2)
    Return()

    # Function_28_5347 end


    label("Function_29_5390")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_53AB")
    OP_A1(0xFE, 0x4B0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_29_5390")

    label("loc_53AB")

    Return()

    # Function_29_5390 end


    label("Function_30_53AC")

    OP_CB(0x0, 0x0, 0xFFFFE0C0, 0x0, 0x6E, 0x0)
    OP_CC(0x0, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x1770, 0x0, 0x5A, 0x0)
    OP_CC(0x0, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFF060, 0x0, 0x46, 0x0)
    OP_CC(0x0, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x7D0, 0x0, 0x32, 0x0)
    OP_CC(0x0, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1E, 0x0)
    OP_CC(0x0, 0x0, 0x0)
    Return()

    # Function_30_53AC end


    label("Function_31_5420")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    Call(0, 6)
    Call(0, 7)
    LoadChrToIndex("apl/ch51744.itc", 0x26)
    LoadEffect(0x0, "event/ev17084.eff")
    LoadEffect(0x1, "event/ev17085.eff")
    SoundLoad(128)
    SoundLoad(4078)
    SoundLoad(4079)
    OP_68(-80, 13300, 209040, 0)
    OP_6D(0x166, 0x13, 0x0, 0x0)
    OP_6E(0x258, 0x0)
    OP_6C(0x4A38, 0x0)
    OP_6C(0x4074, 0x9C4)
    SetChrPos(0x101, 0, 12000, 207440, 0)
    SetChrPos(0x102, 1120, 12000, 206200, 0)
    SetChrPos(0x103, 420, 12000, 204870, 0)
    SetChrPos(0x104, -1270, 12000, 205570, 0)
    SetChrPos(0xF4, -2540, 11990, 206190, 0)
    SetChrPos(0xF5, 2540, 12000, 205990, 0)
    OP_A3(0x4, 0x80)
    OP_A5(0x4, 0x8000)
    OP_A3(0x5, 0x80)
    OP_A5(0x5, 0x8000)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x23)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x24)
    SetChrSubChip(0xF5, 0x0)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_A3(0x8, 0x80)
    OP_A2(0x8, 0x8000)
    OP_A2(0x8, 0x1000)
    OP_A2(0x8, 0x2)
    OP_A2(0x8, 0x800)
    SetChrPos(0x8, 0, 12000, 211500, 180)
    BeginChrThread(0x8, 0, 0, 32)
    OP_68(0, 13000, 210000, 0)
    OP_6D(0x0, 0xF, 0x0, 0x0)
    OP_6E(0x258, 0x0)
    OP_6C(0x445C, 0x0)
    OP_6C(0x3DB8, 0x2EE0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x8,
        (
            "#01404F#4078V#5P#80W#30A………呵呵…………\x02\x03",
            "#4079V#45A罗伊德……还有其他人……\x01",
            "……你们真的变强了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 13100, 208700, 0)
    OP_6D(0x2E, 0x12, 0x0, 0x0)
    OP_6E(0x258, 0x0)
    OP_6C(0x3958, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrSubChip(0x8, 0x1)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006F#12P#40W……呼……呼……\x02\x03",
            "#00008F如果真是如此……那也是因为\x01",
            "我们一直都在以亚里欧斯先生为目标……\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12P#40W的确……如果没有您，\x01",
            "我们恐怕也走不到这一步……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#12P#40W……我有同感……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12P#40W您一直走在遥远的前方，\x01",
            "是我们不断追赶并试图跨越的『壁障』……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01402F#5P#40W呵呵……真是的……\x02\x03",
            "#01404F我哪有接受这种\x01",
            "赞誉的资格……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00003F#12P#30W……亚里欧斯先生。\x02\x03",
            "#00001F那一天，开枪击中大哥的人\x01",
            "是伊安律师吧……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_43(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5951")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_592D")
    OP_FC(0xFFF4)
    Jump("loc_5930")

    label("loc_592D")

    OP_FC(0xC)

    label("loc_5930")


    ChrTalk(
        0x10A,
        "#00605F#13P#30W……！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_59A0")

    label("loc_5951")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_43(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_59A0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_597B")
    OP_FC(0xFFF4)
    Jump("loc_597E")

    label("loc_597B")

    OP_FC(0xC)

    label("loc_597E")


    ChrTalk(
        0x109,
        "#10105F#13P#30W……啊……！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_59A0")


    ChrTalk(
        0x104,
        "#00301F#12P#30W这……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01403F#5P#40W………………………………\x02\x03",
            "#01400F……你为何会这样想……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12P#30W这只是简单的排除法……\x02\x03",
            "#00008F……从事件的背景来考虑……\x01",
            "除了律师之外，嫌疑人就只有\x01",
            "迪塔先生和玛丽亚贝尔小姐了……\x02\x03",
            "#00001F但迪塔先生似乎\x01",
            "并不了解计划的全貌，\x01",
            "而玛丽亚贝尔小姐与大哥没有任何接触……\x02\x03",
            "#00006F只有伊安律师\x01",
            "与大哥来往甚密……\x02\x03",
            "而且……他经常去国外出差，\x01",
            "需要一定的自卫手段，\x01",
            "就算能熟练使用手枪也不足为奇……\x02\x03",
            "#00013F……您的意见如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01403F#5P#40W……六十分吧……\x02\x03",
            "#01402F不过……看来是\x01",
            "不得不承认你及格了……\x02",
        )
    )

    CloseMessageWindow()
    OP_21(0xFA0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    Sound(128, 2, 30, 0)
    Sleep(150)
    OP_25(0x80, 0x28)
    Sleep(150)
    OP_25(0x80, 0x32)
    Sleep(150)
    OP_25(0x80, 0x3C)
    Sleep(150)
    OP_25(0x80, 0x46)
    Sleep(150)
    OP_25(0x80, 0x50)
    Sleep(150)
    OP_25(0x80, 0x5A)
    Sleep(150)
    OP_25(0x80, 0x64)
    Sleep(300)
    Sound(884, 0, 100, 0)
    Sleep(3000)
    OP_22()
    Sleep(10)
    PlayBgm("ed7534.ogg", 0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis308.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis317.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    OP_5B(0x14, 0xA0, 0xFFFF, 0xFFFF)
    SetChrName("盖伊")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x14),
            "#40W呼、呼……\x02\x03",
            "……喂，亚里欧斯……\x02\x03",
            "我们好像都到极限了……\x01",
            "不然就先休战吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_5B(0xE6, 0x8C, 0xFFFF, 0xFFFF)
    SetChrName("亚里欧斯")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x14),
            "#40W……你在说什么蠢话……\x02\x03",
            "既然事情已经败露，\x01",
            "我绝不能让你离开此地……\x02\x03",
            "如果你还想活着迎接下个月的婚礼，\x01",
            "就抱着杀死我的决心攻过来吧……！\x02",
        )
    )

    CloseMessageWindow()
    OP_5B(0x14, 0xA0, 0xFFFF, 0xFFFF)
    SetChrName("盖伊")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x14),
            "#40W我怎么可能那么做……\x02\x03",
            "那样的话，不就无法邀请\x01",
            "你和小滴参加婚礼了吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_5B(0x14A, 0x8C, 0xFFFF, 0xFFFF)
    SetChrName("亚里欧斯")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x14),
            "……！\x02",
        )
    )

    CloseMessageWindow()
    OP_5B(0x14, 0xA0, 0xFFFF, 0xFFFF)
    SetChrName("盖伊")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x14),
            "#40W放心吧……我并没有把\x01",
            "你们的计划告诉任何人……\x02\x03",
            "原本想找达德利\x01",
            "帮忙……\x01",
            "但那家伙是个死脑筋。\x02\x03",
            "另外，我也没和\x01",
            "赛尔盖长官说过呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_5B(0xFA, 0x8C, 0xFFFF, 0xFFFF)
    SetChrName("亚里欧斯")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x14),
            "#40W你……\x02\x03",
            "……你难道就没想过，\x01",
            "我听了这些话之后，\x01",
            "将会下定杀人灭口的决心吗……？\x02",
        )
    )

    CloseMessageWindow()
    OP_5B(0x14, 0xA0, 0xFFFF, 0xFFFF)
    SetChrName("盖伊")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x14),
            "#30W不会啊……\x01",
            "因为你一向很没心机。\x02\x03",
            "不然也不会独身一人\x01",
            "来这种地方赴约了。\x02",
        )
    )

    CloseMessageWindow()
    OP_5B(0x14A, 0x8C, 0xFFFF, 0xFFFF)
    SetChrName("亚里欧斯")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x14),
            "#30W唔……\x02",
        )
    )

    CloseMessageWindow()
    OP_5B(0x14, 0xA0, 0xFFFF, 0xFFFF)
    SetChrName("盖伊")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x14),
            "#30W总之……这件事就先到此为止，\x01",
            "我们一起去喝一杯吧？\x02\x03",
            "最近这两年，我们一直\x01",
            "都没有好好聊过……\x02\x03",
            "你总要给我一个向你炫耀\x01",
            "弟弟和女朋友的机会吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_5B(0xF0, 0x96, 0xFFFF, 0xFFFF)
    SetChrName("亚里欧斯")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x14),
            "#30W呼……你真是老样子啊。\x02\x03",
            "你的弟弟……\x01",
            "已经十五岁了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_5B(0x14, 0xA0, 0xFFFF, 0xFFFF)
    SetChrName("盖伊")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x14),
            "#30W嗯，他完全不像我，非常聪明呢。\x02\x03",
            "我打算送他去\x01",
            "高等学校读书……\x02\x03",
            "……好啦，先不说这些了。\x01",
            "雨还没停，我们不如到『加兰特』——\x02",
        )
    )

    CloseMessageWindow()
    Sound(567, 0, 100, 0)
    Sleep(200)
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    Sleep(500)
    OP_5B(0x50, 0xA0, 0xFFFF, 0xFFFF)
    SetChrName("盖伊")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x14),
            "#60W啊——\x02",
        )
    )

    CloseMessageWindow()
    OP_5B(0x14A, 0x8C, 0xFFFF, 0xFFFF)
    SetChrName("亚里欧斯")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x14),
            "#30W！？\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis309.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x2EE, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    OP_5B(0x14A, 0xA0, 0xFFFF, 0xFFFF)
    SetChrName("亚里欧斯")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x14),
            "#30W律师……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_5B(0xFA, 0xB4, 0xFFFF, 0xFFFF)
    SetChrName("盖伊")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x14),
            "#50W……哈哈……\x02\x03",
            "……原来如此……\x01",
            "幕后黑手原来是你啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sound(885, 0, 80, 0)
    Sound(811, 0, 80, 0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis310.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis318.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis319.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis320.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x2, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    Sleep(1000)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x3, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_5B(0x1E, 0xA0, 0xFFFF, 0xFFFF)
    SetChrName("伊安律师")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x14),
            "#30W……抱歉，盖伊。\x02\x03",
            "考虑到你父母的情况，\x01",
            "原本也想过邀你加入……\x02\x03",
            "但我相信你一定\x01",
            "不会赞同我们。\x02",
        )
    )

    CloseMessageWindow()
    OP_5B(0x15E, 0x8C, 0xFFFF, 0xFFFF)
    SetChrName("亚里欧斯")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x14),
            "#30W……律师先生………\x02",
        )
    )

    CloseMessageWindow()
    OP_5B(0xC8, 0xC8, 0xFFFF, 0xFFFF)
    SetChrName("盖伊")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x14),
            "#50W哈哈……那当然……\x02\x03",
            "……有律师先生在幕后策划，\x01",
            "这个计划……肯定会\x01",
            "进展得很顺利……\x02\x03",
            "但是……代替我的人……\x01",
            "一定会出现的……\x02",
        )
    )

    CloseMessageWindow()
    OP_5B(0x28, 0xA0, 0xFFFF, 0xFFFF)
    SetChrName("伊安律师")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x14),
            "#30W嗯……也许吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5B(0x15E, 0x8C, 0xFFFF, 0xFFFF)
    SetChrName("亚里欧斯")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x14),
            "#30W盖伊……！\x01",
            "……振作点……！\x02",
        )
    )

    CloseMessageWindow()
    OP_5B(0xD2, 0xC8, 0xFFFF, 0xFFFF)
    SetChrName("盖伊")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x14),
            "#60W咳……啊……\x01",
            "……这下可糟了……\x02\x03",
            "#80W早知如此……\x01",
            "真该先向罗伊德……和塞茜尔……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sound(885, 0, 90, 0)
    Sleep(100)
    Sound(811, 0, 90, 0)
    Sound(862, 0, 40, 0)
    OP_21(0x1770)
    Sleep(2000)
    OP_12(0x80, 0x7D0, 0x64)
    OP_22()
    OP_6C(0x3F34, 0xBB8)
    FadeToBright(1500, 0)
    OP_0D()
    OP_6F(0x79)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_43(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6716")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_66E7")
    OP_FC(0xFFF4)
    Jump("loc_66EA")

    label("loc_66E7")

    OP_FC(0xC)

    label("loc_66EA")


    ChrTalk(
        0x10A,
        "#00608F#13P#30W……………………………\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_6716")


    ChrTalk(
        0x103,
        "#00213F#12P#30W………盖伊先生………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#12P#30W……竟有这种事……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00308F#12P#30W真是不幸的往事啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12P#30W……多谢您告诉我\x01",
            "大哥临终时的状况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01404F#5P#40W……不用道谢……\x02\x03",
            "#01400F伊安律师……\x01",
            "恐怕是不会动摇的……\x02\x03",
            "而且……\x01",
            "琪雅的决心似乎也很坚定……\x02\x03",
            "#01404F#50W如果想打动他们二人……\x01",
            "就拼尽一切，放手一搏吧……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Sound(898, 0, 100, 0)
    OP_46(0x8, 0x2, 0x13)
    OP_A6(0xFE, 0x0, 0x23, 0x1F4, 0xBB8)
    OP_00()
    OP_48(0x8, 0x2)
    BeginChrThread(0x8, 0, 0, 33)
    OP_48(0x8, 0x0)
    Sleep(250)
    PlayBgm("ed7356.ogg", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x164), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(700)
    Sound(202, 0, 100, 0)
    Sound(181, 0, 80, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 12050, 208000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    OP_76(0xFF, "magi_04_add", 0x0, 0x1)
    Sleep(2000)
    OP_68(0, 13400, 208000, 0)
    OP_6D(0x1E, 0x14, 0x0, 0x0)
    OP_6E(0x2BC, 0x0)
    OP_6C(0xA410, 0x0)
    Fade(500)
    OP_6C(0xABE0, 0x1388)
    OP_0D()
    Sound(223, 0, 50, 0)
    Sound(293, 0, 60, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -8810, 11000, 195890, 250, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -18740, 11000, 207720, 240, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -8810, 11000, 219990, 277, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 2340, 11000, 226130, 26, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 14640, 11000, 216150, 34, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 14650, 11000, 200000, 64, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    OP_75(0x2, 0x1, 0x7D0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -14190, 4900, 215730, 314, -33, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 3670, 8000, 223960, 85, -33, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 16510, 5300, 208790, 89, -33, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -14840, 11000, 200070, 295, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -14870, 11000, 216410, 326, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -2400, 11000, 226170, 334, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 8990, 11000, 220020, 80, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 18340, 11000, 208220, 120, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 8860, 11000, 195800, 110, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -1580, 4700, 224260, 271, -33, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 16370, 8500, 219180, 44, -33, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 6440, 1300, 196290, 113, -13, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 23440, -900, 210080, 119, -13, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Sleep(100)
    Sleep(100)
    Sleep(100)
    Sleep(100)
    Sleep(100)
    Sleep(100)
    FadeToDark(1500, 0, -1)
    OP_24(0x80)
    OP_0D()
    OP_A9(0x110)
    OP_A9(0x112)
    NewScene("m9008", 0, 0, 0)
    OP_07()
    Return()

    # Function_31_5420 end


    label("Function_32_6DE5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6E2D")
    SetChrSubChip(0xFE, 0x8)
    Sleep(150)
    SetChrSubChip(0xFE, 0x9)
    Sleep(150)
    SetChrSubChip(0xFE, 0xA)
    Sleep(150)
    SetChrSubChip(0xFE, 0xB)
    Sleep(150)
    SetChrSubChip(0xFE, 0xC)
    Sleep(150)
    SetChrSubChip(0xFE, 0xB)
    Sleep(150)
    SetChrSubChip(0xFE, 0xA)
    Sleep(150)
    SetChrSubChip(0xFE, 0x9)
    Sleep(150)
    Jump("Function_32_6DE5")

    label("loc_6E2D")

    Return()

    # Function_32_6DE5 end


    label("Function_33_6E2E")

    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x4)
    Sleep(100)
    SetChrSubChip(0xFE, 0x5)
    Sleep(100)
    SetChrSubChip(0xFE, 0x6)
    Sleep(100)
    SetChrSubChip(0xFE, 0x7)
    Sound(811, 0, 40, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x7)
    Sleep(300)
    SetChrSubChip(0xFE, 0x7)
    Sleep(100)
    SetChrSubChip(0xFE, 0xD)
    Sleep(100)
    SetChrSubChip(0xFE, 0xE)
    Sleep(100)
    Sound(811, 0, 80, 0)
    SetChrSubChip(0xFE, 0xF)
    Sleep(100)
    Sound(862, 0, 30, 0)
    Sleep(300)
    Return()

    # Function_33_6E2E end


    label("Function_34_6E98")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    Call(0, 43)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    Call(0, 6)
    Call(0, 7)
    LoadChrToIndex("chr/ch00056.itc", 0x25)
    LoadEffect(0x0, "event/ev17012.eff")
    SetChrPos(0x101, -430, 12000, 207440, 0)
    SetChrPos(0x102, 470, 12000, 206000, 0)
    SetChrPos(0x103, -1370, 12000, 204870, 0)
    SetChrPos(0x104, 1370, 12000, 204570, 0)
    SetChrPos(0xF4, -2540, 12000, 205690, 0)
    SetChrPos(0xF5, 2400, 12000, 205790, 315)
    OP_A3(0x4, 0x80)
    OP_A5(0x4, 0x8000)
    OP_A3(0x5, 0x80)
    OP_A5(0x5, 0x8000)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x23)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x24)
    SetChrSubChip(0xF5, 0x0)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0xF)
    OP_A3(0x8, 0x80)
    OP_A2(0x8, 0x8000)
    OP_A2(0x8, 0x1000)
    OP_A2(0x8, 0x20)
    OP_A2(0x8, 0x2)
    OP_A2(0x8, 0x800)
    SetChrPos(0x8, 0, 12000, 211500, 180)
    OP_76(0xFF, "magi_04_add", 0x0, 0x1)
    OP_72(0x2, 0x4)
    OP_68(0, 13050, 222000, 0)
    OP_6D(0x10, 0x1C, 0x0, 0x0)
    OP_6E(0x258, 0x0)
    OP_6C(0x7B0C, 0x0)
    OP_6C(0x733C, 0xA28)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 12000, 222000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(935, 0, 80, 0)
    OP_76(0xFF, "magi10_add", 0x1, 0x1)
    OP_76(0xFF, "magi11_add", 0x1, 0x1)
    Sleep(200)
    OP_76(0xFF, "point_add", 0x1, 0x1)
    Sleep(600)
    StopEffect(0x0, 0x2)
    OP_6F(0x79)
    OP_68(0, 12800, 208700, 0)
    OP_6D(0x2E, 0x12, 0x0, 0x0)
    OP_6E(0x258, 0x0)
    OP_6C(0x47EA, 0x0)
    Fade(500)
    OP_0D()
    Sleep(300)
    BeginChrThread(0x101, 0, 0, 36)
    BeginChrThread(0x102, 0, 0, 37)
    BeginChrThread(0x103, 0, 0, 38)
    BeginChrThread(0x104, 0, 0, 39)
    BeginChrThread(0xF4, 0, 0, 40)
    BeginChrThread(0xF5, 0, 0, 41)
    OP_48(0x101, 0x0)
    OP_48(0x102, 0x0)
    OP_48(0x103, 0x0)
    OP_48(0x104, 0x0)
    OP_48(0xF4, 0x0)
    OP_48(0xF5, 0x0)
    Sleep(100)
    OP_68(160, 12800, 209170, 2000)
    OP_6D(0x2C, 0x12, 0x0, 0x7D0)
    OP_6E(0x258, 0x7D0)
    OP_6C(0x4452, 0x7D0)
    BeginChrThread(0x101, 0, 0, 35)
    OP_48(0x101, 0x0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7199")

    ChrTalk(
        0x102,
        "#00108F#12P罗伊德……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7295")

    label("loc_7199")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71D0")

    ChrTalk(
        0x103,
        "#00208F#12P……罗伊德前辈……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7295")

    label("loc_71D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71FF")

    ChrTalk(
        0x104,
        "#00308F#12P罗伊德……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7295")

    label("loc_71FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7232")

    ChrTalk(
        0x105,
        "#10408F#12P……罗伊德……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7295")

    label("loc_7232")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7265")

    ChrTalk(
        0x109,
        "#10108F#12P罗伊德警官……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7295")

    label("loc_7265")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7295")

    ChrTalk(
        0x106,
        "#10708F#12P……罗伊德警官。\x02",
    )

    CloseMessageWindow()

    label("loc_7295")


    ChrTalk(
        0x101,
        (
            "#00004F#11P#30W哈哈……\x02\x03",
            "#00008F……如今……\x01",
            "终于有种追上大哥的感觉了。\x02\x03",
            "#00002F谢谢……\x01",
            "多亏有大家帮忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#12P哈哈……\x01",
            "这叫什么话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#12P……我认为是\x01",
            "罗伊德前辈靠自己的意志打破了\x01",
            "亚里欧斯先生这道『壁障』。\x02\x03",
            "#00208F从而让盖伊先生的死因\x01",
            "时隔多年之后终于真相大白……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#12P是啊……我们只是\x01",
            "从旁协助而已。\x02\x03",
            "#00108F不过，接下来就\x01",
            "不能再说是协助了……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_43(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7447")

    ChrTalk(
        0x106,
        "#10703F#12P……是啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_74A4")

    label("loc_7447")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_43(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7479")

    ChrTalk(
        0x109,
        "#10106F#12P……是啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_74A4")

    label("loc_7479")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_43(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_74A4")

    ChrTalk(
        0x105,
        "#10406F#12P……是啊。\x02",
    )

    CloseMessageWindow()

    label("loc_74A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_43(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_74EC")

    ChrTalk(
        0x104,
        (
            "#00308F#12P贝尔小姐和伊安律师，\x01",
            "还有阿琪……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_7585")

    label("loc_74EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_43(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_753D")

    ChrTalk(
        0x105,
        (
            "#10408F#12P玛丽亚贝尔小姐和大胡子熊律师，\x01",
            "还有琪雅……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7585")

    label("loc_753D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_43(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7585")

    ChrTalk(
        0x109,
        (
            "#10108F#12P玛丽亚贝尔小姐和伊安律师，\x01",
            "还有琪雅……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7585")


    ChrTalk(
        0x101,
        "#00006F#11P#30W……嗯……\x02",
    )

    CloseMessageWindow()
    OP_68(350, 12800, 208640, 1000)
    OP_6D(0x25, 0x11, 0x0, 0x3E8)
    OP_46(0x101, 0x2, 0x7)
    OP_93(0xFE, 0xB4, 0x190)
    OP_00()
    Sleep(300)
    OP_46(0xF4, 0x2, 0x7)
    OP_91(0xFE, 0x101, 0x1F4)
    OP_00()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00003F#5P最后的『领域』也已经开放了。\x02\x03",
            "#00000F总之……\x01",
            "我们先回『神域』的终点吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_6C(0x454C, 0x3E8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A3(0x8, 0x8000)
    SetChrPos(0x0, 0, 12000, 202500, 0)
    OP_A2(0x4, 0x80)
    OP_A4(0x4, 0x8000)
    OP_A2(0x5, 0x80)
    OP_A4(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    OP_37()
    OP_A9(0xD4C)
    OP_29(0xB2, 0x1, 0x8)
    OP_B7(0x0, 0x0, 0x80)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x164), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AA(0x112)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_34_6E98 end


    label("Function_35_76A5")

    OP_9B(0x0, 0xFE, 0x162, 0x320, 0x3E8, 0x0)
    Return()

    # Function_35_76A5 end


    label("Function_36_76B5")

    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_36_76B5 end


    label("Function_37_76C4")

    Sleep(200)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_37_76C4 end


    label("Function_38_76D6")

    Sleep(300)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_38_76D6 end


    label("Function_39_76E8")

    Sleep(100)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_39_76E8 end


    label("Function_40_76F4")

    Sleep(400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7714")
    Sound(540, 0, 50, 0)
    Jump("loc_7739")

    label("loc_7714")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7739")
    Sound(531, 0, 100, 0)

    label("loc_7739")

    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_40_76F4 end


    label("Function_41_7742")

    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7762")
    Sound(540, 0, 50, 0)
    Jump("loc_7787")

    label("loc_7762")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7787")
    Sound(531, 0, 100, 0)

    label("loc_7787")

    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_41_7742 end


    label("Function_42_7790")

    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x10)
    OP_A3(0x8, 0x80)
    OP_A2(0x8, 0x800)
    OP_A2(0x8, 0x8000)
    OP_A2(0x8, 0x2)
    OP_A2(0x8, 0x1000)
    OP_A2(0x8, 0x800)
    Return()

    # Function_42_7790 end


    label("Function_43_77B7")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, 0xD59), scpexpr(EXPR_END)), "loc_77D9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7942")

    label("loc_77D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, 0xD5A), scpexpr(EXPR_END)), "loc_77F1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7942")

    label("loc_77F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, 0xD5B), scpexpr(EXPR_END)), "loc_7809")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7942")

    label("loc_7809")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, 0xD5C), scpexpr(EXPR_EXEC_OP, "OP_43(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_782C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7942")

    label("loc_782C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, 0xD5D), scpexpr(EXPR_EXEC_OP, "OP_43(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_784F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7942")

    label("loc_784F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, 0xD5E), scpexpr(EXPR_EXEC_OP, "OP_43(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7872")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7942")

    label("loc_7872")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7890")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7942")

    label("loc_7890")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78AE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7942")

    label("loc_78AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78CC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7942")

    label("loc_78CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_43(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_78F5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7942")

    label("loc_78F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_43(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_791E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7942")

    label("loc_791E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_43(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7942")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7942")

    Return()

    # Function_43_77B7 end

    SaveToFile()

TryInvoke(main)
