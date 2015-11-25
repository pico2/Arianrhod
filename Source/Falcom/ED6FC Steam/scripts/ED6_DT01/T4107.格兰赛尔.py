from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4107   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4107.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60018",
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
        '卡露娜',                               # 9
        '亚妮拉丝',                             # 10
        '库拉茨',                               # 11
        '克鲁茨',                               # 12
        '管家菲利普',                           # 13
        '杜南公爵',                             # 14
        '亚鲁瓦教授',                           # 15
        '朵洛希',                               # 16
        '芭蒂',                                 # 17
        '拉尔夫',                               # 18
        '蒂库',                                 # 19
        '拉尔斯',                               # 20
        '托伊',                                 # 21
        '克劳斯市长',                           # 22
        '观众',                                 # 23
        '观众',                                 # 24
        '观众',                                 # 25
        '观众',                                 # 26
        '观众',                                 # 27
        '观众',                                 # 28
        '观众',                                 # 29
        '观众',                                 # 30
        '观众',                                 # 31
        '观众',                                 # 32
        '观众',                                 # 33
        '观众',                                 # 34
        '观众',                                 # 35
        '观众',                                 # 36
        '观众',                                 # 37
        '观众',                                 # 38
        '观众',                                 # 39
        '观众',                                 # 40
        '观众',                                 # 41
        '观众',                                 # 42
        '观众',                                 # 43
        '观众',                                 # 44
        '观众',                                 # 45
        '观众',                                 # 46
        '观众',                                 # 47
        '观众',                                 # 48
        '观众',                                 # 49
        '观众',                                 # 50
        '观众',                                 # 51
        '观众',                                 # 52
        '观众',                                 # 53
        '观众',                                 # 54
        '观众',                                 # 55
        '观众',                                 # 56
        '观众',                                 # 57
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
        'ED6_DT07/CH01240 ._CH',             # 00
        'ED6_DT07/CH01630 ._CH',             # 01
        'ED6_DT07/CH01260 ._CH',             # 02
        'ED6_DT07/CH01620 ._CH',             # 03
        'ED6_DT07/CH02470 ._CH',             # 04
        'ED6_DT07/CH02140 ._CH',             # 05
        'ED6_DT07/CH02050 ._CH',             # 06
        'ED6_DT06/CH20063 ._CH',             # 07
        'ED6_DT07/CH01030 ._CH',             # 08
        'ED6_DT07/CH01040 ._CH',             # 09
        'ED6_DT07/CH01160 ._CH',             # 0A
        'ED6_DT07/CH01470 ._CH',             # 0B
        'ED6_DT07/CH01060 ._CH',             # 0C
        'ED6_DT07/CH02350 ._CH',             # 0D
        'ED6_DT07/CH01150 ._CH',             # 0E
        'ED6_DT07/CH01020 ._CH',             # 0F
        'ED6_DT07/CH01220 ._CH',             # 10
        'ED6_DT07/CH01460 ._CH',             # 11
        'ED6_DT07/CH01130 ._CH',             # 12
        'ED6_DT07/CH01200 ._CH',             # 13
        'ED6_DT07/CH01210 ._CH',             # 14
        'ED6_DT07/CH01100 ._CH',             # 15
        'ED6_DT07/CH01140 ._CH',             # 16
        'ED6_DT07/CH01680 ._CH',             # 17
        'ED6_DT07/CH01690 ._CH',             # 18
        'ED6_DT07/CH01120 ._CH',             # 19
        'ED6_DT07/CH01180 ._CH',             # 1A
        'ED6_DT07/CH01110 ._CH',             # 1B
        'ED6_DT07/CH01230 ._CH',             # 1C
        'ED6_DT07/CH01490 ._CH',             # 1D
        'ED6_DT07/CH01480 ._CH',             # 1E
        'ED6_DT06/CH20063 ._CH',             # 1F
    )

    AddCharChipPat(
        'ED6_DT07/CH01240P._CP',             # 00
        'ED6_DT07/CH01630P._CP',             # 01
        'ED6_DT07/CH01260P._CP',             # 02
        'ED6_DT07/CH01620P._CP',             # 03
        'ED6_DT07/CH02470P._CP',             # 04
        'ED6_DT07/CH02140P._CP',             # 05
        'ED6_DT07/CH02050P._CP',             # 06
        'ED6_DT06/CH20063P._CP',             # 07
        'ED6_DT07/CH01030P._CP',             # 08
        'ED6_DT07/CH01040P._CP',             # 09
        'ED6_DT07/CH01160P._CP',             # 0A
        'ED6_DT07/CH01470P._CP',             # 0B
        'ED6_DT07/CH01060P._CP',             # 0C
        'ED6_DT07/CH02350P._CP',             # 0D
        'ED6_DT07/CH01150P._CP',             # 0E
        'ED6_DT07/CH01020P._CP',             # 0F
        'ED6_DT07/CH01220P._CP',             # 10
        'ED6_DT07/CH01460P._CP',             # 11
        'ED6_DT07/CH01130P._CP',             # 12
        'ED6_DT07/CH01200P._CP',             # 13
        'ED6_DT07/CH01210P._CP',             # 14
        'ED6_DT07/CH01100P._CP',             # 15
        'ED6_DT07/CH01140P._CP',             # 16
        'ED6_DT07/CH01680P._CP',             # 17
        'ED6_DT07/CH01690P._CP',             # 18
        'ED6_DT07/CH01120P._CP',             # 19
        'ED6_DT07/CH01180P._CP',             # 1A
        'ED6_DT07/CH01110P._CP',             # 1B
        'ED6_DT07/CH01230P._CP',             # 1C
        'ED6_DT07/CH01490P._CP',             # 1D
        'ED6_DT07/CH01480P._CP',             # 1E
        'ED6_DT06/CH20063P._CP',             # 1F
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 40,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 39,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 46,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 49,
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
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 48,
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
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 47,
    )

    DeclNpc(
        X                   = -12680,
        Z                   = 4700,
        Y                   = -4790,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 45,
    )

    DeclNpc(
        X                   = -12660,
        Z                   = 4700,
        Y                   = -3750,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 44,
    )

    DeclNpc(
        X                   = -14750,
        Z                   = 5200,
        Y                   = 3290,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 41,
    )

    DeclNpc(
        X                   = -14750,
        Z                   = 5200,
        Y                   = 3960,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 42,
    )

    DeclNpc(
        X                   = -14750,
        Z                   = 5200,
        Y                   = 4700,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 43,
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
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 38,
    )

    DeclNpc(
        X                   = -14740,
        Z                   = 5200,
        Y                   = -13430,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -15550,
        Z                   = 5450,
        Y                   = -5010,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -12650,
        Z                   = 4700,
        Y                   = 3270,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -15550,
        Z                   = 5450,
        Y                   = -9240,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -15550,
        Z                   = 5450,
        Y                   = 1890,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -12650,
        Z                   = 4700,
        Y                   = -6590,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -12680,
        Z                   = 4700,
        Y                   = -17670,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -14720,
        Z                   = 5200,
        Y                   = -3720,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -12650,
        Z                   = 4700,
        Y                   = 1670,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -13550,
        Z                   = 4950,
        Y                   = -13580,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -14750,
        Z                   = 5200,
        Y                   = -8060,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -14720,
        Z                   = 5200,
        Y                   = 510,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -12660,
        Z                   = 4700,
        Y                   = -9280,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -13550,
        Z                   = 4950,
        Y                   = 4710,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = -14720,
        Z                   = 5200,
        Y                   = 4019,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -14520,
        Z                   = 5200,
        Y                   = -15970,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = -12650,
        Z                   = 4700,
        Y                   = -13490,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = -15610,
        Z                   = 5450,
        Y                   = -17700,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = -15610,
        Z                   = 5450,
        Y                   = -14800,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = -16640,
        Z                   = 5700,
        Y                   = -13560,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = -13520,
        Z                   = 4950,
        Y                   = -9500,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = -13520,
        Z                   = 4950,
        Y                   = -4800,
        Direction           = 91,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = -15440,
        Z                   = 5450,
        Y                   = -5520,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = -15440,
        Z                   = 5450,
        Y                   = -6530,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = -15440,
        Z                   = 5450,
        Y                   = 3270,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = -12650,
        Z                   = 4700,
        Y                   = 520,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = -13520,
        Z                   = 4950,
        Y                   = 3330,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
    )

    DeclNpc(
        X                   = -14520,
        Z                   = 5200,
        Y                   = 1860,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 30,
    )

    DeclNpc(
        X                   = -13520,
        Z                   = 4950,
        Y                   = -8039,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = -15440,
        Z                   = 5450,
        Y                   = 550,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = -12660,
        Z                   = 4700,
        Y                   = 4760,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = -13520,
        Z                   = 4950,
        Y                   = -3700,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = -16620,
        Z                   = 5700,
        Y                   = -3710,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = -15440,
        Z                   = 5450,
        Y                   = 4750,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 36,
    )

    DeclNpc(
        X                   = -12730,
        Z                   = 4700,
        Y                   = -8010,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 37,
    )


    ScpFunction(
        "Function_0_7CA",          # 00, 0
        "Function_1_A1B",          # 01, 1
        "Function_2_A1C",          # 02, 2
        "Function_3_BA4",          # 03, 3
        "Function_4_BC1",          # 04, 4
        "Function_5_BE8",          # 05, 5
        "Function_6_C0B",          # 06, 6
        "Function_7_C3D",          # 07, 7
        "Function_8_C5C",          # 08, 8
        "Function_9_D0E",          # 09, 9
        "Function_10_D32",         # 0A, 10
        "Function_11_D5E",         # 0B, 11
        "Function_12_D83",         # 0C, 12
        "Function_13_DD2",         # 0D, 13
        "Function_14_DFA",         # 0E, 14
        "Function_15_E3E",         # 0F, 15
        "Function_16_E7A",         # 10, 16
        "Function_17_E9B",         # 11, 17
        "Function_18_EC1",         # 12, 18
        "Function_19_EE4",         # 13, 19
        "Function_20_F21",         # 14, 20
        "Function_21_F82",         # 15, 21
        "Function_22_FCF",         # 16, 22
        "Function_23_100D",        # 17, 23
        "Function_24_1058",        # 18, 24
        "Function_25_109C",        # 19, 25
        "Function_26_10BB",        # 1A, 26
        "Function_27_1102",        # 1B, 27
        "Function_28_1140",        # 1C, 28
        "Function_29_1188",        # 1D, 29
        "Function_30_11B8",        # 1E, 30
        "Function_31_1200",        # 1F, 31
        "Function_32_124B",        # 20, 32
        "Function_33_1291",        # 21, 33
        "Function_34_12EE",        # 22, 34
        "Function_35_1339",        # 23, 35
        "Function_36_136E",        # 24, 36
        "Function_37_13D1",        # 25, 37
        "Function_38_140B",        # 26, 38
        "Function_39_1475",        # 27, 39
        "Function_40_155D",        # 28, 40
        "Function_41_1621",        # 29, 41
        "Function_42_163A",        # 2A, 42
        "Function_43_1697",        # 2B, 43
        "Function_44_16B6",        # 2C, 44
        "Function_45_17CE",        # 2D, 45
        "Function_46_19B6",        # 2E, 46
        "Function_47_1A88",        # 2F, 47
        "Function_48_1CB8",        # 30, 48
        "Function_49_1F66",        # 31, 49
    )


    def Function_0_7CA(): pass

    label("Function_0_7CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_85A")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xE, -16580, 5700, -9620, 90)
    SetChrPos(0xF, -10500, 4200, -6510, 90)
    SetChrPos(0x8, -12710, 4700, -15880, 90)
    SetChrPos(0x9, -12670, 4700, -15020, 90)
    SetChrPos(0xA, -12650, 4700, -16690, 90)
    SetChrPos(0xB, -12650, 4700, -17560, 90)

    label("loc_85A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_864")
    Jump("loc_A1A")

    label("loc_864")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_86E")
    Jump("loc_A1A")

    label("loc_86E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_878")
    Jump("loc_A1A")

    label("loc_878")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_882")
    Jump("loc_A1A")

    label("loc_882")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_948")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -12660, 4700, -6420, 90)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -12660, 4700, -5620, 90)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 5)), scpexpr(EXPR_END)), "loc_8E1")
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -14490, 5200, 70, 90)

    label("loc_8E1")

    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x34, 0x80)
    ClearChrFlags(0x35, 0x80)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x37, 0x80)
    ClearChrFlags(0x38, 0x80)
    Jump("loc_A1A")

    label("loc_948")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_952")
    Jump("loc_A1A")

    label("loc_952")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_9C6")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -13550, 4950, -6540, 90)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 4)), scpexpr(EXPR_END)), "loc_9C3")
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 31)
    SetChrPos(0xF, -10500, 4200, -6450, 90)

    label("loc_9C3")

    Jump("loc_A1A")

    label("loc_9C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_9D0")
    Jump("loc_A1A")

    label("loc_9D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_A09")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -12690, 4700, -4810, 90)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    Jump("loc_A1A")

    label("loc_A09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_A13")
    Jump("loc_A1A")

    label("loc_A13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_A1A")

    label("loc_A1A")

    Return()

    # Function_0_7CA end

    def Function_1_A1B(): pass

    label("Function_1_A1B")

    Return()

    # Function_1_A1B end

    def Function_2_A1C(): pass

    label("Function_2_A1C")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A4C")
    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_B8E")

    label("loc_A4C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A65")
    OP_99(0xFE, 0x1, 0x7, 0x514)
    Jump("loc_B8E")

    label("loc_A65")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A7E")
    OP_99(0xFE, 0x2, 0x7, 0x4E2)
    Jump("loc_B8E")

    label("loc_A7E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A97")
    OP_99(0xFE, 0x3, 0x7, 0x4B0)
    Jump("loc_B8E")

    label("loc_A97")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB0")
    OP_99(0xFE, 0x4, 0x7, 0x47E)
    Jump("loc_B8E")

    label("loc_AB0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC9")
    OP_99(0xFE, 0x5, 0x7, 0x44C)
    Jump("loc_B8E")

    label("loc_AC9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE2")
    OP_99(0xFE, 0x6, 0x7, 0x41A)
    Jump("loc_B8E")

    label("loc_AE2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AFB")
    OP_99(0xFE, 0x0, 0x7, 0x54B)
    Jump("loc_B8E")

    label("loc_AFB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B14")
    OP_99(0xFE, 0x1, 0x7, 0x519)
    Jump("loc_B8E")

    label("loc_B14")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B2D")
    OP_99(0xFE, 0x2, 0x7, 0x4E7)
    Jump("loc_B8E")

    label("loc_B2D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B46")
    OP_99(0xFE, 0x3, 0x7, 0x4B5)
    Jump("loc_B8E")

    label("loc_B46")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B5F")
    OP_99(0xFE, 0x4, 0x7, 0x483)
    Jump("loc_B8E")

    label("loc_B5F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B78")
    OP_99(0xFE, 0x5, 0x7, 0x451)
    Jump("loc_B8E")

    label("loc_B78")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8E")
    OP_99(0xFE, 0x6, 0x7, 0x41F)

    label("loc_B8E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BA3")
    OP_99(0xFE, 0x0, 0x7, 0x4B0)
    Jump("loc_B8E")

    label("loc_BA3")

    Return()

    # Function_2_A1C end

    def Function_3_BA4(): pass

    label("Function_3_BA4")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "比赛快点开始吧。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_BA4 end

    def Function_4_BC1(): pass

    label("Function_4_BC1")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "不管是谁取得优胜都很好啊。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_BC1 end

    def Function_5_BE8(): pass

    label("Function_5_BE8")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "我现在已经开始兴奋了。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_BE8 end

    def Function_6_C0B(): pass

    label("Function_6_C0B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "哈～哈，因为兴奋过度，\x01",
            "来得太早了些。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_C0B end

    def Function_7_C3D(): pass

    label("Function_7_C3D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "今年为谁加油好呢？\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_C3D end

    def Function_8_C5C(): pass

    label("Function_8_C5C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_CAA")

    ChrTalk(
        0xFE,
        (
            "好、好像觉得后面\x01",
            "有股很强的杀气……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "是、是我多心了吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_D0A")

    label("loc_CAA")

    OP_A2(0x5)
    OP_62(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "好、好像觉得后面\x01",
            "有股很强的杀气……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "是、是我多心了吧。\x02",
    )

    CloseMessageWindow()

    label("loc_D0A")

    TalkEnd(0xFE)
    Return()

    # Function_8_C5C end

    def Function_9_D0E(): pass

    label("Function_9_D0E")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "完了，\x01",
            "导力相机忘带了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_D0E end

    def Function_10_D32(): pass

    label("Function_10_D32")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "可惜了！\x01",
            "今年亲卫队没有出战呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_D32 end

    def Function_11_D5E(): pass

    label("Function_11_D5E")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "团体赛比想象的要有趣呢。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_D5E end

    def Function_12_D83(): pass

    label("Function_12_D83")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "我想还是特务部队\x01",
            "会取得优胜吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "穿着一身黑装，\x01",
            "看起来就很强。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_D83 end

    def Function_13_DD2(): pass

    label("Function_13_DD2")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "今天的对阵\x01",
            "会是怎么样的呢？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_DD2 end

    def Function_14_DFA(): pass

    label("Function_14_DFA")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "游击士的两个小组\x01",
            "都还没有出局。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "两组都要加油啊～！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_DFA end

    def Function_15_E3E(): pass

    label("Function_15_E3E")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "特务部队虽然让人觉得有些害怕，\x01",
            "但实力相当强啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_E3E end

    def Function_16_E7A(): pass

    label("Function_16_E7A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "比赛怎么还不开始啊。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_E7A end

    def Function_17_E9B(): pass

    label("Function_17_E9B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "每年的比赛\x01",
            "我都很期待呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_E9B end

    def Function_18_EC1(): pass

    label("Function_18_EC1")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "今天是总决赛的日子啊。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_EC1 end

    def Function_19_EE4(): pass

    label("Function_19_EE4")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "哪支小组会取胜呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我心里扑通扑通地响呢。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_EE4 end

    def Function_20_F21(): pass

    label("Function_20_F21")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "我喜欢游击士组里面\x01",
            "那个金色头发的小哥。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "外表英俊潇洒，\x01",
            "而且射击方面也无懈可击。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_F21 end

    def Function_21_F82(): pass

    label("Function_21_F82")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "我想看那个戴着红色面具的哥哥\x01",
            "和那个像熊一样的叔叔\x01",
            "打架的样子呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_F82 end

    def Function_22_FCF(): pass

    label("Function_22_FCF")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "真不愧是总决赛的日子，\x01",
            "一大早就已经有很多人来了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_FCF end

    def Function_23_100D(): pass

    label("Function_23_100D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "双方都是今年\x01",
            "第一次参加比赛，\x01",
            "哪一边会取胜的确是决赛的看点啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_100D end

    def Function_24_1058(): pass

    label("Function_24_1058")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "游击士小组里面\x01",
            "好像有个女孩子呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这可真了不起啊。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_1058 end

    def Function_25_109C(): pass

    label("Function_25_109C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "比赛还没有开始吗。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_109C end

    def Function_26_10BB(): pass

    label("Function_26_10BB")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "每年只有我和老头子\x01",
            "两个人来看比赛，\x01",
            "感到无聊也没有办法啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_10BB end

    def Function_27_1102(): pass

    label("Function_27_1102")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "因为太期待今天的比赛了，\x01",
            "我昨天一夜都睡不着觉呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_1102 end

    def Function_28_1140(): pass

    label("Function_28_1140")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "我还是觉得\x01",
            "特务部队会取胜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "一看名字就知道来头不小嘛。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_1140 end

    def Function_29_1188(): pass

    label("Function_29_1188")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "就算口干舌燥\x01",
            "我也要全力为比赛呐喊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_1188 end

    def Function_30_11B8(): pass

    label("Function_30_11B8")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "我支持游击士组哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以前我也曾受到\x01",
            "游击士的很多关照啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_11B8 end

    def Function_31_1200(): pass

    label("Function_31_1200")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "要是把便当\x01",
            "也带来就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一大早就过来排队，\x01",
            "肚子都饿了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_31_1200 end

    def Function_32_124B(): pass

    label("Function_32_124B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "哎呀，\x01",
            "武术大会果然很有意思啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "光是看就已经爽呆了。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_124B end

    def Function_33_1291(): pass

    label("Function_33_1291")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "游击士组里的那个男孩子\x01",
            "和我儿子的年纪差不多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "无论如何\x01",
            "我也要支持游击士组。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_1291 end

    def Function_34_12EE(): pass

    label("Function_34_12EE")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "如果从综合实力来看的话，\x01",
            "不用说也知道\x01",
            "那个特务部队是最强的了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_34_12EE end

    def Function_35_1339(): pass

    label("Function_35_1339")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "没有想到决赛对阵\x01",
            "会是这样的呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_35_1339 end

    def Function_36_136E(): pass

    label("Function_36_136E")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "王国军和游击士……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我觉得无论哪一方，\x01",
            "都是保卫我们市民的、\x01",
            "值得大家信赖的好战士。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_36_136E end

    def Function_37_13D1(): pass

    label("Function_37_13D1")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "比赛快要开始了……\x01",
            "我会全力为大家呐喊助威的。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_37_13D1 end

    def Function_38_140B(): pass

    label("Function_38_140B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1471")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 5)), scpexpr(EXPR_END)), "loc_1471")

    ChrTalk(
        0x15,
        (
            "#600F我从年轻的时候就喜欢\x01",
            "观看每年一度的武术大会。\x02\x03",
            "加油啊。\x01",
            "艾丝蒂尔、约修亚，\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1471")

    TalkEnd(0xFE)
    Return()

    # Function_38_140B end

    def Function_39_1475(): pass

    label("Function_39_1475")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_14DC")

    ChrTalk(
        0xFE,
        (
            "虽说那些对手\x01",
            "的确不容易对付，\x01",
            "不过我坚信你们一定能够取胜的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我会给你们加油哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1559")

    label("loc_14DC")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        "哟，两位新人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们决赛的对手相当强劲，\x01",
            "不过肯定会有胜算的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我坚信你们一定能够取胜的！\x01",
            "我会给你们加油哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1559")

    TalkEnd(0xFE)
    Return()

    # Function_39_1475 end

    def Function_40_155D(): pass

    label("Function_40_155D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_15B9")

    ChrTalk(
        0xFE,
        (
            "听好，一定要放松，\x01",
            "像往常那样出战就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "就连在气势上也要战胜对手。\x02",
    )

    CloseMessageWindow()
    Jump("loc_161D")

    label("loc_15B9")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        "啊，你们好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "听好，一定要放松，\x01",
            "像往常那样出战就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "就连在气势上也要战胜对手。\x02",
    )

    CloseMessageWindow()

    label("loc_161D")

    TalkEnd(0xFE)
    Return()

    # Function_40_155D end

    def Function_41_1621(): pass

    label("Function_41_1621")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "快点开始吧。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_41_1621 end

    def Function_42_163A(): pass

    label("Function_42_163A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "今天我一大早\x01",
            "就去叫了那两个人，\x01",
            "然后来竞技场了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "因为绝对不能错过总决赛啊。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_42_163A end

    def Function_43_1697(): pass

    label("Function_43_1697")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "哪个小组会取胜呢。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_43_1697 end

    def Function_44_16B6(): pass

    label("Function_44_16B6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_16C3")
    Jump("loc_17CA")

    label("loc_16C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_16CD")
    Jump("loc_17CA")

    label("loc_16CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_16D7")
    Jump("loc_17CA")

    label("loc_16D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_16E1")
    Jump("loc_17CA")

    label("loc_16E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1791")

    ChrTalk(
        0xFE,
        (
            "想拿个观战的好位置，\x01",
            "所以我在门外彻夜排队，\x01",
            "不料被那些巡逻的士兵赶回了家。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "之后，我偷偷地从家里溜出来，\x01",
            "躲在大街上的草丛里等那些士兵撤走，\x01",
            "然后才来排队的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17CA")

    label("loc_1791")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_179B")
    Jump("loc_17CA")

    label("loc_179B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_17A5")
    Jump("loc_17CA")

    label("loc_17A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_17AF")
    Jump("loc_17CA")

    label("loc_17AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_17B9")
    Jump("loc_17CA")

    label("loc_17B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_17C3")
    Jump("loc_17CA")

    label("loc_17C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_17CA")

    label("loc_17CA")

    TalkEnd(0xFE)
    Return()

    # Function_44_16B6 end

    def Function_45_17CE(): pass

    label("Function_45_17CE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_17DB")
    Jump("loc_19B2")

    label("loc_17DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_17E5")
    Jump("loc_19B2")

    label("loc_17E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_17EF")
    Jump("loc_19B2")

    label("loc_17EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_17F9")
    Jump("loc_19B2")

    label("loc_17F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1871")

    ChrTalk(
        0xFE,
        (
            "昨天真是辛苦我丈夫了，\x01",
            "帮我拿到这么一个好位子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽说我的要求很任性，\x01",
            "不过没想到他能为我做到这样……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19B2")

    label("loc_1871")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_187B")
    Jump("loc_19B2")

    label("loc_187B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1968")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_18E0")

    ChrTalk(
        0xFE,
        (
            "最前排正中央\x01",
            "明明一直是我的位子啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看来明天的决赛\x01",
            "我必须来早一点才行！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1965")

    label("loc_18E0")

    OP_A2(0x1)
    OP_62(0xFE, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    OP_22(0x2F, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "唉～遗憾啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最前排正中央\x01",
            "明明一直是我的位子啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看来明天的决赛\x01",
            "我必须来早一点才行！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1965")

    Jump("loc_19B2")

    label("loc_1968")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1972")
    Jump("loc_19B2")

    label("loc_1972")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_19A1")

    ChrTalk(
        0xFE,
        (
            "呵呵呵，\x01",
            "今年又到了这个时候了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19B2")

    label("loc_19A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_19AB")
    Jump("loc_19B2")

    label("loc_19AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_19B2")

    label("loc_19B2")

    TalkEnd(0xFE)
    Return()

    # Function_45_17CE end

    def Function_46_19B6(): pass

    label("Function_46_19B6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_19C3")
    Jump("loc_1A84")

    label("loc_19C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_19CD")
    Jump("loc_1A84")

    label("loc_19CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_19D7")
    Jump("loc_1A84")

    label("loc_19D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_19E1")
    Jump("loc_1A84")

    label("loc_19E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1A4B")

    ChrTalk(
        0xFE,
        (
            "今天大家都来到竞技场\x01",
            "为你们呐喊助威。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "作为游击士协会的代表，\x01",
            "你们一定要为荣誉而战哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A84")

    label("loc_1A4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1A55")
    Jump("loc_1A84")

    label("loc_1A55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1A5F")
    Jump("loc_1A84")

    label("loc_1A5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1A69")
    Jump("loc_1A84")

    label("loc_1A69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1A73")
    Jump("loc_1A84")

    label("loc_1A73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1A7D")
    Jump("loc_1A84")

    label("loc_1A7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1A84")

    label("loc_1A84")

    TalkEnd(0xFE)
    Return()

    # Function_46_19B6 end

    def Function_47_1A88(): pass

    label("Function_47_1A88")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1C4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C16")
    OP_A2(0x633)

    ChrTalk(
        0xF,
        (
            "#151F啊，是小艾你们啊！\x02\x03",
            "真厉害～！\x01",
            "你们打进决赛了～！\x02\x03",
            "我真是兴奋得都要跳起来了～！\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506F哈哈，别这么激动嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F如果不静下心来集中精神的话，\x01",
            "说不定会错过很多精彩的画面哦。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#150F哎嘿，不用担心啦。\x02\x03",
            "因为我只有在静不下心的时候\x01",
            "才能拍下一些好的照片呢～\x02\x03",
            "这样才有自然感哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F是、是这样吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F不愧是朵洛希……\x01",
            "完全是个另类的天才。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C4C")

    label("loc_1C16")


    ChrTalk(
        0xF,
        (
            "#151F小艾你们的精彩表现，\x01",
            "我一定会好好拍下来的～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C4C")

    Jump("loc_1CB4")

    label("loc_1C4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 4)), scpexpr(EXPR_END)), "loc_1CB4")

    ChrTalk(
        0xF,
        (
            "#150F嘿嘿，\x01",
            "因为我是负责报道的记者，\x01",
            "所以拿到了特等席位哦。\x02\x03",
            "好了，\x01",
            "要快点把相机准备好～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CB4")

    TalkEnd(0xF)
    Return()

    # Function_47_1A88 end

    def Function_48_1CB8(): pass

    label("Function_48_1CB8")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F11")
    OP_A2(0x632)

    ChrTalk(
        0xE,
        (
            "#130F你们好啊。\x01",
            "艾丝蒂尔、约修亚，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎，是亚鲁瓦教授！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F您也来观看比赛吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#130F哈哈，\x01",
            "因为受了你们好多的照顾嘛。\x02\x03",
            "今天是恩人出战决赛的日子，\x01",
            "我想无论如何也要来看一看的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F嘿嘿，谢谢啦。\x02\x03",
            "#006F不过，买决赛的门票\x01",
            "肯定花了不少米拉吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#130F哈哈，那也不是。\x02\x03",
            "资料馆的馆长突然有急事，\x01",
            "不能前来观看比赛了。\x02\x03",
            "所以就把这张票免费转让给了我。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506F什～么啊，果然还是没付钱嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#130F哈哈……真是不好意思。\x02\x03",
            "不过，我支持你们的信念\x01",
            "是绝对不会输给其他人的。\x02\x03",
            "请你们一定要加油哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，包在我们身上！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我们必定全力出战。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F62")

    label("loc_1F11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1F62")

    ChrTalk(
        0xE,
        (
            "#130F我支持你们的信念\x01",
            "是绝对不会输给其他人的。\x02\x03",
            "请你们一定要加油哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F62")

    TalkEnd(0xE)
    Return()

    # Function_48_1CB8 end

    def Function_49_1F66(): pass

    label("Function_49_1F66")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23FF")
    OP_A2(0x634)
    OP_8C(0xB, 90, 0)

    ChrTalk(
        0xB,
        "……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F哎……\x01",
            "克鲁茨前辈，你怎么了？\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0xB, 0xF, 0x0, 0x12C, 0xFA0)
    TurnDirection(0xB, 0x0, 400)

    ChrTalk(
        0xB,
        "哎……啊，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "终于到了决赛呢。\x01",
            "我很期待你们的表现哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯，看我的吧！\x02\x03",
            "#505F……不过，克鲁茨前辈，\x01",
            "你的脸色好像有点不对劲啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F是啊。\x01",
            "脸色铁青铁青呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "没什么……\x01",
            "只是从刚才开始就觉得有点头晕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "不过奇怪的是……\x01",
            "我的身体没有什么事啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "……难道是那个时候留下的后遗症……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#580F后、后遗症……\x01",
            "难道是说昨天的比赛吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "哈哈，不是不是。\x01",
            "是三个月之前的一次事故。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "那时候我好像执行任务失败了，\x01",
            "还弄得自己伤痕累累。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F好像执行任务失败了……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F好像是很模糊的说法啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "啊啊，不好意思。\x01",
            "因为那次事故的记忆确实很模糊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "连那是件什么样的工作\x01",
            "也完全记不起来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "虽然医生说，\x01",
            "这是因事故所受的刺激……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F是这样啊……\x02\x03",
            "#002F不过，以这样的状态来参加比赛，\x01",
            "不会有事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "我刚才已经说了，\x01",
            "其实这不是身体上的问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "嗯，跟你们说了一会儿话，\x01",
            "我感觉比刚才舒服多了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "已经没事了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F是、是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F看起来脸色确实好些了呢。\x01",
            "　\x02\x03",
            "不过……\x01",
            "请不要勉强硬撑着啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "嗯，谢谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "你们今天一定要\x01",
            "全力出战获取冠军哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 90, 400)
    Jump("loc_2439")

    label("loc_23FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2439")

    ChrTalk(
        0xFE,
        (
            "要连我们的份也一起加油，\x01",
            "全力出战获取冠军哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2439")

    TalkEnd(0xB)
    Return()

    # Function_49_1F66 end

    SaveToFile()

Try(main)
