from ED6ScenarioHelper import *

def main():
    # 蔡斯飞艇坪

    CreateScenaFile(
        FileName            = 'T3104   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3104.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        '朵洛希',                               # 9
        '玛多克工房长',                         # 10
        '特莱斯主任',                           # 11
        '海泽尔',                               # 12
        '索黛丽娅',                             # 13
        '阿利瑟',                               # 14
        '米优',                                 # 15
        '斯坦因',                               # 16
        '温丝',                                 # 17
        '埃尔文',                               # 18
        '王',                                   # 19
        '莱恩',                                 # 20
        '科奇莫爷爷',                           # 21
        '莫妮卡',                               # 22
        '布鲁诺',                               # 23
        '伊格尔',                               # 24
        '普利亚姆',                             # 25
        '爱玲',                                 # 26
        '雷曼',                                 # 27
        '鲁迪',                                 # 28
        '菲',                                   # 29
        '埃里克',                               # 30
        '康丝坦茨',                             # 31
        '雨果',                                 # 32
        '安东尼',                               # 33
        '普罗梅笛',                             # 34
        '雷伊',                                 # 35
        '蒂亚利',                               # 36
        '米妮亚姆',                             # 37
        '威尔姆',                               # 38
        '格斯塔夫维修长',                       # 39
        ' ',                                    # 40
        '蔡斯飞艇坪方向',                       # 41
        '蔡斯市街区方向',                       # 42
    )

    DeclEntryPoint(
        Unknown_00              = -32000,
        Unknown_04              = 10000,
        Unknown_08              = 58000,
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
        'ED6_DT07/CH02070 ._CH',             # 00
        'ED6_DT07/CH02620 ._CH',             # 01
        'ED6_DT07/CH01000 ._CH',             # 02
        'ED6_DT07/CH01050 ._CH',             # 03
        'ED6_DT07/CH01030 ._CH',             # 04
        'ED6_DT07/CH01130 ._CH',             # 05
        'ED6_DT07/CH01050 ._CH',             # 06
        'ED6_DT07/CH01200 ._CH',             # 07
        'ED6_DT07/CH01470 ._CH',             # 08
        'ED6_DT07/CH01040 ._CH',             # 09
        'ED6_DT07/CH01620 ._CH',             # 0A
        'ED6_DT07/CH01450 ._CH',             # 0B
        'ED6_DT07/CH01100 ._CH',             # 0C
        'ED6_DT07/CH02490 ._CH',             # 0D
        'ED6_DT07/CH01530 ._CH',             # 0E
        'ED6_DT07/CH01250 ._CH',             # 0F
        'ED6_DT07/CH01140 ._CH',             # 10
        'ED6_DT07/CH01150 ._CH',             # 11
        'ED6_DT07/CH01450 ._CH',             # 12
        'ED6_DT07/CH01500 ._CH',             # 13
        'ED6_DT07/CH01550 ._CH',             # 14
        'ED6_DT07/CH01450 ._CH',             # 15
        'ED6_DT07/CH01230 ._CH',             # 16
        'ED6_DT07/CH01680 ._CH',             # 17
        'ED6_DT07/CH01700 ._CH',             # 18
        'ED6_DT07/CH01100 ._CH',             # 19
        'ED6_DT07/CH01220 ._CH',             # 1A
        'ED6_DT07/CH01660 ._CH',             # 1B
        'ED6_DT07/CH01430 ._CH',             # 1C
        'ED6_DT07/CH01450 ._CH',             # 1D
        'ED6_DT07/CH02440 ._CH',             # 1E
    )

    AddCharChipPat(
        'ED6_DT07/CH02070P._CP',             # 00
        'ED6_DT07/CH02620P._CP',             # 01
        'ED6_DT07/CH01000P._CP',             # 02
        'ED6_DT07/CH01050P._CP',             # 03
        'ED6_DT07/CH01030P._CP',             # 04
        'ED6_DT07/CH01130P._CP',             # 05
        'ED6_DT07/CH01050P._CP',             # 06
        'ED6_DT07/CH01200P._CP',             # 07
        'ED6_DT07/CH01470P._CP',             # 08
        'ED6_DT07/CH01040P._CP',             # 09
        'ED6_DT07/CH01620P._CP',             # 0A
        'ED6_DT07/CH01450P._CP',             # 0B
        'ED6_DT07/CH01100P._CP',             # 0C
        'ED6_DT07/CH02490P._CP',             # 0D
        'ED6_DT07/CH01530P._CP',             # 0E
        'ED6_DT07/CH01250P._CP',             # 0F
        'ED6_DT07/CH01140P._CP',             # 10
        'ED6_DT07/CH01150P._CP',             # 11
        'ED6_DT07/CH01450P._CP',             # 12
        'ED6_DT07/CH01500P._CP',             # 13
        'ED6_DT07/CH01550P._CP',             # 14
        'ED6_DT07/CH01450P._CP',             # 15
        'ED6_DT07/CH01230P._CP',             # 16
        'ED6_DT07/CH01680P._CP',             # 17
        'ED6_DT07/CH01700P._CP',             # 18
        'ED6_DT07/CH01100P._CP',             # 19
        'ED6_DT07/CH01220P._CP',             # 1A
        'ED6_DT07/CH01660P._CP',             # 1B
        'ED6_DT07/CH01430P._CP',             # 1C
        'ED6_DT07/CH01450P._CP',             # 1D
        'ED6_DT07/CH02440P._CP',             # 1E
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
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
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 36,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 37,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 38,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 39,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 40,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 41,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 30,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        X                   = -23030,
        Z                   = 8000,
        Y                   = 86970,
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

    DeclNpc(
        X                   = 28060,
        Z                   = 8000,
        Y                   = 58980,
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
        X                   = -35690,
        Y                   = 9750,
        Z                   = 58940,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 42,
    )

    DeclEvent(
        X                   = -23010,
        Y                   = 7750,
        Z                   = 74850,
        Range               = 1500,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 43,
    )

    DeclEvent(
        X                   = -50430,
        Y                   = 24000,
        Z                   = 53980,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 44,
    )


    ScpFunction(
        "Function_0_642",          # 00, 0
        "Function_1_BFC",          # 01, 1
        "Function_2_C40",          # 02, 2
        "Function_3_C76",          # 03, 3
        "Function_4_DF3",          # 04, 4
        "Function_5_E17",          # 05, 5
        "Function_6_E3B",          # 06, 6
        "Function_7_E5F",          # 07, 7
        "Function_8_E83",          # 08, 8
        "Function_9_EA7",          # 09, 9
        "Function_10_ECB",         # 0A, 10
        "Function_11_EEF",         # 0B, 11
        "Function_12_F3F",         # 0C, 12
        "Function_13_F95",         # 0D, 13
        "Function_14_FEB",         # 0E, 14
        "Function_15_1030",        # 0F, 15
        "Function_16_1082",        # 10, 16
        "Function_17_111B",        # 11, 17
        "Function_18_118A",        # 12, 18
        "Function_19_128E",        # 13, 19
        "Function_20_1319",        # 14, 20
        "Function_21_133C",        # 15, 21
        "Function_22_1389",        # 16, 22
        "Function_23_13EC",        # 17, 23
        "Function_24_143F",        # 18, 24
        "Function_25_148C",        # 19, 25
        "Function_26_14FA",        # 1A, 26
        "Function_27_151E",        # 1B, 27
        "Function_28_1580",        # 1C, 28
        "Function_29_1704",        # 1D, 29
        "Function_30_1DD3",        # 1E, 30
        "Function_31_21C1",        # 1F, 31
        "Function_32_224C",        # 20, 32
        "Function_33_2340",        # 21, 33
        "Function_34_2347",        # 22, 34
        "Function_35_234E",        # 23, 35
        "Function_36_23C9",        # 24, 36
        "Function_37_266C",        # 25, 37
        "Function_38_272D",        # 26, 38
        "Function_39_2776",        # 27, 39
        "Function_40_2911",        # 28, 40
        "Function_41_2B9B",        # 29, 41
        "Function_42_2EC6",        # 2A, 42
        "Function_43_2ECA",        # 2B, 43
        "Function_44_2ECE",        # 2C, 44
    )


    def Function_0_642(): pass

    label("Function_0_642")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_69A")
    SetChrPos(0xD, -14600, 8000, 63040, 6)
    SetChrPos(0x10, -15440, 8000, 63040, 3)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)
    Jump("loc_BE7")

    label("loc_69A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_734")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -15510, 8000, 54720, 275)
    SetChrPos(0xD, -16920, 8000, 54780, 91)
    SetChrPos(0x10, -16950, 8000, 55940, 148)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -15680, 8000, 55990, 243)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -30230, 10000, 47900, 298)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)
    Jump("loc_BE7")

    label("loc_734")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_76A")
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)
    Jump("loc_BE7")

    label("loc_76A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_7A0")
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -25190, 8000, 66790, 275)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -17150, 8000, 63800, 358)
    Jump("loc_BE7")

    label("loc_7A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_879")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -34110, 10000, 62990, 166)
    OP_43(0x11, 0x0, 0x0, 0x4)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -23170, 8000, 59080, 91)
    OP_43(0x12, 0x0, 0x0, 0x5)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -25200, 8000, 67400, 272)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -31870, 10000, 49240, 326)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -33120, 10000, 50470, 135)
    SetChrFlags(0x17, 0x10)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -23610, 8000, 70240, 5)
    OP_43(0x1A, 0x0, 0x0, 0x6)
    Jump("loc_BE7")

    label("loc_879")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_A7B")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -30660, 9000, 60810, 69)
    OP_43(0xA, 0x0, 0x0, 0x3)
    ClearChrFlags(0x25, 0x80)
    SetChrPos(0x25, -24500, 8750, 51360, 18)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -34110, 10000, 62990, 166)
    OP_43(0x11, 0x0, 0x0, 0x4)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -23610, 8000, 70240, 5)
    OP_43(0x1A, 0x0, 0x0, 0x6)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, -27110, 8000, 60420, 69)
    SetChrFlags(0x1B, 0x10)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, -27070, 8000, 59620, 359)
    SetChrFlags(0x1C, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -33870, 10000, 57010, 292)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, -30810, 10000, 48800, 320)
    OP_43(0x1D, 0x0, 0x0, 0x7)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -32630, 10000, 58920, 255)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, -26600, 8000, 55790, 279)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1F, -23180, 8000, 58380, 82)
    OP_43(0x1F, 0x0, 0x0, 0x8)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -29430, 8000, 57220, 85)
    SetChrFlags(0x17, 0x10)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, -22660, 8000, 61960, 82)
    OP_43(0x21, 0x0, 0x0, 0xA)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x22, -33530, 10000, 52430, 296)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x23, -33770, 10000, 51140, 330)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, -25860, 8000, 60310, 263)
    ClearChrFlags(0x26, 0x80)
    SetChrPos(0x26, -21670, 8000, 66490, 242)
    ClearChrFlags(0x20, 0x80)
    SetChrPos(0x20, -23200, 10000, 47850, 272)
    OP_43(0x20, 0x0, 0x0, 0x9)
    Jump("loc_BE7")

    label("loc_A7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_ACE")
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -23610, 8000, 70240, 5)
    OP_43(0x1A, 0x0, 0x0, 0x6)
    Jump("loc_BE7")

    label("loc_ACE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_B04")
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)
    Jump("loc_BE7")

    label("loc_B04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_B3A")
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)
    Jump("loc_BE7")

    label("loc_B3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_B92")
    SetChrPos(0xD, -14600, 8000, 63040, 6)
    SetChrPos(0x10, -15440, 8000, 63040, 3)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)
    Jump("loc_BE7")

    label("loc_B92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_BE7")
    SetChrPos(0xD, -14600, 8000, 63040, 6)
    SetChrPos(0x10, -15440, 8000, 63040, 3)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -26340, 8000, 65489, 74)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -18800, 8000, 64430, 164)

    label("loc_BE7")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (104, "loc_BF3"),
        (SWITCH_DEFAULT, "loc_BFB"),
    )


    label("loc_BF3")

    OP_22(0xE, 0x0, 0x64)
    Jump("loc_BFB")

    label("loc_BFB")

    Return()

    # Function_0_642 end

    def Function_1_BFC(): pass

    label("Function_1_BFC")

    OP_16(0x2, 0xFA0, 0xFFFDB228, 0xFFFEF278, 0x30052)
    OP_6F(0x5, 40)
    OP_70(0x5, 0x0)
    SoundDistance(0xA0, 0xFFFFEDF4, 0x14C8, 0xE790, 0x2710, 0x9C40, 0x64, 0x0)
    OP_43(0x27, 0x0, 0x0, 0x2)
    Return()

    # Function_1_BFC end

    def Function_2_C40(): pass

    label("Function_2_C40")

    OP_72(0x5, 0x20)
    OP_72(0x4, 0x20)

    label("loc_C4A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C75")
    OP_6F(0x5, 40)
    OP_70(0x5, 0x0)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x28)
    OP_73(0x5)
    Jump("loc_C4A")

    label("loc_C75")

    Return()

    # Function_2_C40 end

    def Function_3_C76(): pass

    label("Function_3_C76")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C9B")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_DDD")

    label("loc_C9B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB4")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_DDD")

    label("loc_CB4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CCD")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_DDD")

    label("loc_CCD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE6")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_DDD")

    label("loc_CE6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CFF")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_DDD")

    label("loc_CFF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D18")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_DDD")

    label("loc_D18")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D31")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_DDD")

    label("loc_D31")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D4A")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_DDD")

    label("loc_D4A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D63")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_DDD")

    label("loc_D63")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D7C")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_DDD")

    label("loc_D7C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D95")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_DDD")

    label("loc_D95")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DAE")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_DDD")

    label("loc_DAE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DC7")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_DDD")

    label("loc_DC7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DDD")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_DDD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DF2")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_DDD")

    label("loc_DF2")

    Return()

    # Function_3_C76 end

    def Function_4_DF3(): pass

    label("Function_4_DF3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E16")
    OP_8D(0xFE, -35270, 61360, -33040, 64150, 3000)
    Jump("Function_4_DF3")

    label("loc_E16")

    Return()

    # Function_4_DF3 end

    def Function_5_E17(): pass

    label("Function_5_E17")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E3A")
    OP_8D(0xFE, -26390, 55950, -19770, 61950, 3000)
    Jump("Function_5_E17")

    label("loc_E3A")

    Return()

    # Function_5_E17 end

    def Function_6_E3B(): pass

    label("Function_6_E3B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E5E")
    OP_8D(0xFE, -25190, 68440, -20920, 71850, 3000)
    Jump("Function_6_E3B")

    label("loc_E5E")

    Return()

    # Function_6_E3B end

    def Function_7_E5F(): pass

    label("Function_7_E5F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E82")
    OP_8D(0xFE, -32689, 46510, -30620, 50700, 3000)
    Jump("Function_7_E5F")

    label("loc_E82")

    Return()

    # Function_7_E5F end

    def Function_8_E83(): pass

    label("Function_8_E83")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EA6")
    OP_8D(0xFE, -25190, 54660, -20780, 60740, 3000)
    Jump("Function_8_E83")

    label("loc_EA6")

    Return()

    # Function_8_E83 end

    def Function_9_EA7(): pass

    label("Function_9_EA7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_ECA")
    OP_8D(0xFE, -26510, 46520, -19100, 49060, 3000)
    Jump("Function_9_EA7")

    label("loc_ECA")

    Return()

    # Function_9_EA7 end

    def Function_10_ECB(): pass

    label("Function_10_ECB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EEE")
    OP_8D(0xFE, -23960, 59250, -21170, 66410, 3000)
    Jump("Function_10_ECB")

    label("loc_EEE")

    Return()

    # Function_10_ECB end

    def Function_11_EEF(): pass

    label("Function_11_EEF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_F3B")

    ChrTalk(
        0xFE,
        (
            "#690F这烟真是好大啊。\x02\x03",
            "连中央工房的换气能力\x01",
            "也应付不过来……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F3B")

    TalkEnd(0xFE)
    Return()

    # Function_11_EEF end

    def Function_12_F3F(): pass

    label("Function_12_F3F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_F91")

    ChrTalk(
        0xFE,
        (
            "啊，\x01",
            "好久没有这么拼命地奔跑了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊啊，真糟糕。\x01",
            "情况糟透了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F91")

    TalkEnd(0xFE)
    Return()

    # Function_12_F3F end

    def Function_13_F95(): pass

    label("Function_13_F95")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_FE7")

    ChrTalk(
        0xFE,
        (
            "工房里面\x01",
            "已经到处是浓烟了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼呼～～～～\x01",
            "我还以为死定了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FE7")

    TalkEnd(0xFE)
    Return()

    # Function_13_F95 end

    def Function_14_FEB(): pass

    label("Function_14_FEB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_102C")

    ChrTalk(
        0xFE,
        "有没有受伤的人？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果有的话\x01",
            "要马上通知我啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_102C")

    TalkEnd(0xFE)
    Return()

    # Function_14_FEB end

    def Function_15_1030(): pass

    label("Function_15_1030")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_107E")

    ChrTalk(
        0xFE,
        (
            "前、前辈！\x01",
            "怎么办呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "发生火灾的话，\x01",
            "研究数据就要毁掉了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_107E")

    TalkEnd(0xFE)
    Return()

    # Function_15_1030 end

    def Function_16_1082(): pass

    label("Function_16_1082")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1117")

    ChrTalk(
        0xFE,
        "……呼，好奇怪。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "无论怎么看\x01",
            "都不像火灾所冒出的烟啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "大家也都没有能冒烟的实验装置。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么这些烟\x01",
            "是从哪里出来的？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1117")

    TalkEnd(0xFE)
    Return()

    # Function_16_1082 end

    def Function_17_111B(): pass

    label("Function_17_111B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1186")

    ChrTalk(
        0xFE,
        (
            "我都不清楚\x01",
            "自己是怎么逃出来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在逃生的途中\x01",
            "我突然想起了空贼事件……\x01",
            "脚差点踩空了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1186")

    TalkEnd(0xFE)
    Return()

    # Function_17_111B end

    def Function_18_118A(): pass

    label("Function_18_118A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_124E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_11F6")

    ChrTalk(
        0xFE,
        (
            "说起来\x01",
            "的确没有看到拉赛尔呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过那家伙应该不用让人担心。\x01",
            "肯定已经逃出来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_124B")

    label("loc_11F6")

    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "紧急通道也是很有用处的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没那玩意儿的话\x01",
            "就只能从阳台上跳下来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_124B")

    Jump("loc_128A")

    label("loc_124E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_128A")

    ChrTalk(
        0xFE,
        "痛、痛痛痛……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不小心踏空楼梯，\x01",
            "扭到腰了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_128A")

    TalkEnd(0xFE)
    Return()

    # Function_18_118A end

    def Function_19_128E(): pass

    label("Function_19_128E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1315")

    ChrTalk(
        0xFE,
        (
            "我正在做实验的时候，\x01",
            "突然冒起了漫天烟雾……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不管怎么说，\x01",
            "我是拼命逃出来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我想大家也\x01",
            "应该都逃出来了吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1315")

    TalkEnd(0xFE)
    Return()

    # Function_19_128E end

    def Function_20_1319(): pass

    label("Function_20_1319")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1338")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0xFE,
        "喵呀～噢！\x02",
    )

    CloseMessageWindow()

    label("loc_1338")

    TalkEnd(0xFE)
    Return()

    # Function_20_1319 end

    def Function_21_133C(): pass

    label("Function_21_133C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1385")

    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "好久没有这样剧烈运动过了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哎呀哎呀，痛啊……\x02",
    )

    CloseMessageWindow()

    label("loc_1385")

    TalkEnd(0xFE)
    Return()

    # Function_21_133C end

    def Function_22_1389(): pass

    label("Function_22_1389")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_13E8")

    ChrTalk(
        0x9,
        (
            "#800F博士应该在三楼的工作室。\x01",
            "　\x02\x03",
            "首先去那里确认一下。\x01",
            "如果危险的话就马上撤离。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13E8")

    TalkEnd(0xFE)
    Return()

    # Function_22_1389 end

    def Function_23_13EC(): pass

    label("Function_23_13EC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_143B")

    ChrTalk(
        0x110,
        (
            "#150F我也想一起去呀。\x01",
            "但没办法了……\x02\x03",
            "小艾你们千万要小心呀。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_143B")

    TalkEnd(0xFE)
    Return()

    # Function_23_13EC end

    def Function_24_143F(): pass

    label("Function_24_143F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1488")

    ChrTalk(
        0xFE,
        (
            "客、客人，\x01",
            "你们都顺利逃出来了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这、这烟也太大了。\x02",
    )

    CloseMessageWindow()

    label("loc_1488")

    TalkEnd(0xFE)
    Return()

    # Function_24_143F end

    def Function_25_148C(): pass

    label("Function_25_148C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_14F6")

    ChrTalk(
        0xFE,
        (
            "哪里都找不到\x01",
            "拉赛尔博士啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说不定……\x01",
            "难道还在工房里面吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊，该怎么办才好。\x02",
    )

    CloseMessageWindow()

    label("loc_14F6")

    TalkEnd(0xFE)
    Return()

    # Function_25_148C end

    def Function_26_14FA(): pass

    label("Function_26_14FA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_151A")

    ChrTalk(
        0xFE,
        "鲁迪，你没事吧？\x02",
    )

    CloseMessageWindow()

    label("loc_151A")

    TalkEnd(0xFE)
    Return()

    # Function_26_14FA end

    def Function_27_151E(): pass

    label("Function_27_151E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_157C")

    ChrTalk(
        0xFE,
        "咳咳、咳咳。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "烟、烟……\x01",
            "咳咳、咳咳咳、咳咳。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "肺、肺……\x01",
            "咳咳、咳咳！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_157C")

    TalkEnd(0xFE)
    Return()

    # Function_27_151E end

    def Function_28_1580(): pass

    label("Function_28_1580")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1652")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_15F9")

    ChrTalk(
        0xFE,
        (
            "不过……\x01",
            "那些从里面出来的\x01",
            "穿着军装的家伙是谁呀？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "明明那么大的烟，\x01",
            "他们却好像一点事也没有。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_164F")

    label("loc_15F9")

    OP_A2(0xD)

    ChrTalk(
        0xFE,
        (
            "中央工房\x01",
            "开始冒烟的时候，\x01",
            "我可紧张坏了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，都怪这烟，\x01",
            "喉咙又开始渴了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_164F")

    Jump("loc_1700")

    label("loc_1652")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1695")

    ChrTalk(
        0xFE,
        "啊啊啊，怎么会这样！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "到、到底\x01",
            "发生什么事情了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1700")

    label("loc_1695")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1700")

    ChrTalk(
        0xFE,
        (
            "在整个王国中，\x01",
            "穿着作业服的驾驶员也只有我一个了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，这和衣服没有关系，\x01",
            "关键在于技术。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1700")

    TalkEnd(0xFE)
    Return()

    # Function_28_1580 end

    def Function_29_1704(): pass

    label("Function_29_1704")

    TalkBegin(0x18)
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
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1765")
    OP_0D()
    OP_A9(0x4D)
    OP_56(0x0)
    TalkEnd(0x18)
    Return()

    label("loc_1765")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1776")
    TalkEnd(0x18)
    Return()

    label("loc_1776")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_END)), "loc_17D0")

    ChrTalk(
        0x18,
        (
            "军队的警备飞艇\x01",
            "好像停在港口呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "又没有发生什么事件，\x01",
            "实在是很少见呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DCF")

    label("loc_17D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1855")

    ChrTalk(
        0x18,
        "哟，辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "前些日子，\x01",
            "进出工房船的人好频繁呢，\x01",
            "不过这两天又恢复平静了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "今天的飞艇坪\x01",
            "从早上开始就很安静。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DCF")

    label("loc_1855")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_18E3")

    ChrTalk(
        0x18,
        "哟，你们今天也很忙嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "说到忙，\x01",
            "刚才雷曼那家伙\x01",
            "慌张地跑向飞艇坪了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "看来很着急\x01",
            "要出动工房船的样子。\x01",
            "他还真是辛苦呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DCF")

    label("loc_18E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_1926")

    ChrTalk(
        0x18,
        "哟，早上好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "早上最好还是\x01",
            "喝杯营养丰富的饮料。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DCF")

    label("loc_1926")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_199C")

    ChrTalk(
        0x18,
        "哟，这么晚还在辛苦工作啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "哎呀哎呀，\x01",
            "今天也累得要命。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "差不多该关店了，\x01",
            "想要什么就快点选吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DCF")

    label("loc_199C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1A6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_1A12")

    ChrTalk(
        0x18,
        (
            "从中央工房出来的\x01",
            "穿蓝色军装的家伙，\x01",
            "到底是什么人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "不知道那些军人\x01",
            "在工房里面干了些什么。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A69")

    label("loc_1A12")

    OP_A2(0xB)

    ChrTalk(
        0x18,
        (
            "呼～\x01",
            "看来骚动总算结束了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "说起来，那些军人\x01",
            "在那么浓重的烟雾里干了什么呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A69")

    Jump("loc_1DCF")

    label("loc_1A6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1ACF")

    ChrTalk(
        0x18,
        (
            "这、这种时候\x01",
            "必须冷静地行动！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "那么，\x01",
            "大家请先喝点清凉的饮料，\x01",
            "稍微冷静一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DCF")

    label("loc_1ACF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1BC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_1B51")

    ChrTalk(
        0x18,
        (
            "那边的雷曼\x01",
            "其实是飞艇的驾驶员。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "我说的飞艇\x01",
            "不是定期船而是工房船。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "嗯，\x01",
            "反正都是在天上飞的家伙啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC1")

    label("loc_1B51")

    OP_A2(0xB)

    ChrTalk(
        0x18,
        (
            "那边的雷曼\x01",
            "怎么看都是个维修员吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "不过，\x01",
            "其实他是飞艇的驾驶员哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "哈哈哈～\x01",
            "真是人不可貌相啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BC1")

    Jump("loc_1DCF")

    label("loc_1BC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_1CDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_1C4C")

    ChrTalk(
        0x18,
        (
            "做生意不只是买卖商品，\x01",
            "还必须要考虑经营的手段。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "想开间有人情味的店，\x01",
            "嘴上说起来简单，\x01",
            "但是实现起来却很难呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CDB")

    label("loc_1C4C")

    OP_A2(0xB)

    ChrTalk(
        0x18,
        (
            "我们的愿望是\x01",
            "拥有一间属于我们自己的店子，\x01",
            "就算规模很小也好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "可以的话，最好能开间\x01",
            "像这座城里的『贝尔杂货店』\x01",
            "那样有人情味的小店。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CDB")

    Jump("loc_1DCF")

    label("loc_1CDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_1D36")

    ChrTalk(
        0x18,
        (
            "对面卖花的爱玲\x01",
            "是我的妹妹。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "如果可以的话，\x01",
            "希望大家也到那边去看看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DCF")

    label("loc_1D36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1DCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_1D9B")

    ChrTalk(
        0x18,
        (
            "要不要喝点\x01",
            "清凉的饮料呀？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "我这里卖的饮料不仅美味，\x01",
            "对身体也很有益哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DCF")

    label("loc_1D9B")

    OP_A2(0xB)

    ChrTalk(
        0x18,
        "哟，辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "要不要喝点\x01",
            "清凉的饮料呀？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DCF")

    TalkEnd(0x18)
    Return()

    # Function_29_1704 end

    def Function_30_1DD3(): pass

    label("Function_30_1DD3")

    TalkBegin(0x19)
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
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E34")
    OP_0D()
    OP_A9(0x4E)
    OP_56(0x0)
    TalkEnd(0x19)
    Return()

    label("loc_1E34")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E45")
    TalkEnd(0x19)
    Return()

    label("loc_1E45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_END)), "loc_1E92")

    ChrTalk(
        0x19,
        (
            "哎，从飞艇坪那边\x01",
            "传来了汽笛的声音……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "……发生什么事了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_21BD")

    label("loc_1E92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1EF4")

    ChrTalk(
        0x19,
        (
            "来，请看一看。\x01",
            "这里卖的都是很漂亮的花哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "忘记讨厌的事，\x01",
            "买一盆来舒缓心情吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21BD")

    label("loc_1EF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1F70")

    ChrTalk(
        0x19,
        (
            "啊，客人们都在议论最近的事情，\x01",
            "没人来好好欣赏花了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "毕竟发生了那样的事情……\x01",
            "不过我还是觉得有些寂寞呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21BD")

    label("loc_1F70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_1FC4")

    ChrTalk(
        0x19,
        "啊，早上好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "请随意看吧。\x01",
            "就算是只闻闻花香\x01",
            "也能让你心情愉快的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21BD")

    label("loc_1FC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_2015")

    ChrTalk(
        0x19,
        "啊，晚上好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "虽然马上要关店了，\x01",
            "不过趁现在挑选鲜花也没关系。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21BD")

    label("loc_2015")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2075")

    ChrTalk(
        0x19,
        (
            "我正想着烟可能快要散了，\x01",
            "工房里就出来了几位军人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "难道是他们\x01",
            "把烟止住的吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21BD")

    label("loc_2075")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_209E")

    ChrTalk(
        0x19,
        (
            "不、不好了！\x01",
            "怎么回事！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21BD")

    label("loc_209E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2109")

    ChrTalk(
        0x19,
        (
            "蔡斯城里的绿色\x01",
            "越来越少了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "就算一次也好，\x01",
            "好想去参观一下那个\x01",
            "以花闻名的玛诺利亚村啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21BD")

    label("loc_2109")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2171")

    ChrTalk(
        0x19,
        (
            "那边卖饮料的\x01",
            "是我的哥哥哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "我们的梦想是兄妹一起加油，\x01",
            "将来开间属于自己的店子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21BD")

    label("loc_2171")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_21BD")

    ChrTalk(
        0x19,
        "欢迎光临～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "这里有各种漂亮的鲜花，\x01",
            "请各位客人慢慢观赏。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21BD")

    TalkEnd(0x19)
    Return()

    # Function_30_1DD3 end

    def Function_31_21C1(): pass

    label("Function_31_21C1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2248")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2204")

    ChrTalk(
        0xFE,
        "呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "喝了点饮料，\x01",
            "终于放松下来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2248")

    label("loc_2204")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        "呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个案件真是让人震惊啊。\x01",
            "没办法安心回去工作了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2248")

    TalkEnd(0xFE)
    Return()

    # Function_31_21C1 end

    def Function_32_224C(): pass

    label("Function_32_224C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_233C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_22E3")

    ChrTalk(
        0xFE,
        (
            "你们没事实在是太好了，\x01",
            "不过没看到拉赛尔呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然如果他没事的时候\x01",
            "就会给别人带来各种各样的麻烦，\x01",
            "不过还是有点担心他啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_233C")

    label("loc_22E3")

    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "哦哦，伊格尔。\x01",
            "你没受伤真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是从紧急楼梯下来的吗？\x01",
            "想必一定很累吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_233C")

    TalkEnd(0xFE)
    Return()

    # Function_32_224C end

    def Function_33_2340(): pass

    label("Function_33_2340")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_33_2340 end

    def Function_34_2347(): pass

    label("Function_34_2347")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_34_2347 end

    def Function_35_234E(): pass

    label("Function_35_234E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_23C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_238B")

    ChrTalk(
        0xFE,
        (
            "亲卫队的制服……\x01",
            "的确是让人在意呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23C5")

    label("loc_238B")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "哎哎！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "工房袭击犯竟然\x01",
            "穿着亲卫队的制服吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23C5")

    TalkEnd(0xFE)
    Return()

    # Function_35_234E end

    def Function_36_23C9(): pass

    label("Function_36_23C9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_248B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_241B")

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "越来越想不明白了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "买盆花来\x01",
            "调节一下心情吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2488")

    label("loc_241B")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "尽管如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "袭击中央工房的犯人\x01",
            "到现在都还没抓到吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "王国军和游击士协会\x01",
            "到底都在干什么呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2488")

    Jump("loc_2668")

    label("loc_248B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_250E")

    ChrTalk(
        0xFE,
        (
            "很多人都说\x01",
            "从工房出来的是穿蓝色军装的军人，\x01",
            "所以应该是不会有错的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且温丝也说他看见了。\x01",
            "亲卫队果然很可疑啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2668")

    label("loc_250E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_2625")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_256D")

    ChrTalk(
        0xFE,
        (
            "我一要买什么，\x01",
            "温丝就处处有意见。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是的，\x01",
            "这个孩子就喜欢斤斤计较。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2622")

    label("loc_256D")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "呀，提妲，\x01",
            "在为客人带路吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F啊，您好，阿利瑟阿姨。\x02\x03",
            "在挑选鲜花吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哎，是呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我一要买什么，\x01",
            "温丝就处处有意见。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是的，\x01",
            "这个孩子就喜欢斤斤计较。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2622")

    Jump("loc_2668")

    label("loc_2625")


    ChrTalk(
        0xFE,
        "哇，好漂亮的花呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过种在阳台上的话，\x01",
            "颜色有些不合适。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2668")

    TalkEnd(0xFE)
    Return()

    # Function_36_23C9 end

    def Function_37_266C(): pass

    label("Function_37_266C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2729")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_26F1")

    ChrTalk(
        0xFE,
        (
            "就连亲卫队\x01",
            "也在这里出现了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果顺利的话，\x01",
            "我就会出名啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "决定了！\x01",
            "我一定要成为工房的接待小姐。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2729")

    label("loc_26F1")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "哎！亲卫队！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果顺利的话，\x01",
            "我就会出名啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2729")

    TalkEnd(0xFE)
    Return()

    # Function_37_266C end

    def Function_38_272D(): pass

    label("Function_38_272D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2772")

    ChrTalk(
        0xFE,
        (
            "看起来\x01",
            "不像是火灾呀……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "但那么多烟是怎么回事呢？\x02",
    )

    CloseMessageWindow()

    label("loc_2772")

    TalkEnd(0xFE)
    Return()

    # Function_38_272D end

    def Function_39_2776(): pass

    label("Function_39_2776")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2834")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_27D6")

    ChrTalk(
        0xFE,
        (
            "结果最后还是不知道\x01",
            "那些穿军装的人的真面目。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他们到底\x01",
            "是什么人呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2831")

    label("loc_27D6")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "妈妈，王国军和协会\x01",
            "都已经尽力去调查了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只不过那些情况\x01",
            "是不可能让我们知道的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2831")

    Jump("loc_290D")

    label("loc_2834")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2890")

    ChrTalk(
        0xFE,
        (
            "妈妈，我看见的是\x01",
            "『穿蓝色军装的军人』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我可没说过\x01",
            "我看见的是亲卫队哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_290D")

    label("loc_2890")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_28E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_28CA")

    ChrTalk(
        0xFE,
        (
            "不是我斤斤计较，\x01",
            "而是妈妈太浪费啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28E1")

    label("loc_28CA")


    ChrTalk(
        0xFE,
        (
            "提妲，\x01",
            "早上好啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28E1")

    Jump("loc_290D")

    label("loc_28E4")


    ChrTalk(
        0xFE,
        (
            "妈妈，\x01",
            "阳台的花坛已经放满花盆了呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_290D")

    TalkEnd(0xFE)
    Return()

    # Function_39_2776 end

    def Function_40_2911(): pass

    label("Function_40_2911")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2A48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_29A6")

    ChrTalk(
        0xFE,
        (
            "好了，\x01",
            "我也差不多该回店里去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "擅自把商品分发给大家，\x01",
            "妻子一定会很生气吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但能对大家有点用，\x01",
            "我就非常满足了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A45")

    label("loc_29A6")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "看来烟总算是散了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "听说没有人受伤，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然有东西被偷走了，\x01",
            "只要再做个一样的不就行了吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好了，\x01",
            "我也差不多该回店里去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A45")

    Jump("loc_2B97")

    label("loc_2A48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2B97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2A9A")

    ChrTalk(
        0xFE,
        (
            "遇到有困难的人\x01",
            "一定要帮助他们啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那么，你们要小心哦！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B97")

    label("loc_2A9A")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        "你们没事吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我是杂货店的埃尔文。\x01",
            "一听到有事就赶来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我从店里带来很多东西，\x01",
            "想要什么就尽管说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在这种非常时刻，\x01",
            "当然不会收你们钱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "好，这个就给你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果遇到有困难的人\x01",
            "一定要帮助他们啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那么，你们要小心哦！\x02",
    )

    CloseMessageWindow()

    label("loc_2B97")

    TalkEnd(0xFE)
    Return()

    # Function_40_2911 end

    def Function_41_2B9B(): pass

    label("Function_41_2B9B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2EC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2C1D")

    ChrTalk(
        0xFE,
        (
            "可是，我不在的时候\x01",
            "竟然发生这样的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "冈多夫先生外出时让我留守，\x01",
            "发生了这样的事，我简直没脸见他。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EC2")

    label("loc_2C1D")

    OP_A2(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 4)), scpexpr(EXPR_END)), "loc_2E6A")

    ChrTalk(
        0xFE,
        "啊！是你们！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，是王先生……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我、我刚刚\x01",
            "才回到蔡斯……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这到底发生什么事了！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，其实啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#050F喂，你在干什么。\x02\x03",
            "赶快回协会去吧。\x01",
            "我们可没时间再磨蹭了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F唔唔……\x02\x03",
            "哼，虽然不甘心，\x01",
            "但阿加特说得没错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F……有什么不甘心的。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x12, 400)

    ChrTalk(
        0x106,
        (
            "#050F还有你。\x02\x03",
            "作为游击士，\x01",
            "应该自己去确认当前的状况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……确实是这样。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不好意思，\x01",
            "我有点自乱阵脚了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#050F呼……\x02\x03",
            "算了，既然已经发生了，\x01",
            "现在就考虑一下对策吧。\x02\x03",
            "……喂，走啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F回头见，王先生……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊啊，刚刚真是对不起。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那么我们就告辞了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2EC2")

    label("loc_2E6A")


    ChrTalk(
        0xFE,
        (
            "工房被袭击了……\x01",
            "竟然会发生这样的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总之要先回协会，\x01",
            "确认一下状况才行……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EC2")

    TalkEnd(0xFE)
    Return()

    # Function_41_2B9B end

    def Function_42_2EC6(): pass

    label("Function_42_2EC6")

    SetPlaceName(0x85) # 蔡斯飞艇坪
    Return()

    # Function_42_2EC6 end

    def Function_43_2ECA(): pass

    label("Function_43_2ECA")

    SetPlaceName(0x81) # 蔡斯飞艇坪
    Return()

    # Function_43_2ECA end

    def Function_44_2ECE(): pass

    label("Function_44_2ECE")

    OP_A3(0x540)
    OP_A3(0x541)
    OP_A3(0x546)
    OP_A3(0x543)
    OP_A3(0x544)
    OP_A3(0x545)
    OP_A2(0x546)
    Return()

    # Function_44_2ECE end

    SaveToFile()

Try(main)
