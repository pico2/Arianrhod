from ED6ScenarioHelper import *

def main():
    # 主楼　社会系教室

    CreateScenaFile(
        FileName            = 'T2520   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2520.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60075",
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
        '科林兹校长',                           # 9
        '波利',                                 # 10
        '特蕾莎院长',                           # 11
        '达尼艾尔',                             # 12
        '玛丽',                                 # 13
        '克拉姆',                               # 14
        '基库',                                 # 15
        '珐奥娜',                               # 16
        '拉迪奥老师',                           # 17
        '碧欧拉老师',                           # 18
        '米丽亚老师',                           # 19
        '艾福托老师',                           # 20
        '罗迪',                                 # 21
        '坎诺',                                 # 22
        '雅莉丝',                               # 23
        '黛拉',                                 # 24
        '帕布尔',                               # 25
        '罗基克',                               # 26
        '亚吉鲁',                               # 27
        '罗伊斯',                               # 28
        '莫妮卡',                               # 29
        '塞尔玛',                               # 30
        '莉秋尔',                               # 31
        '巴托姆',                               # 32
        '基诺奇奥',                             # 33
        '妮吉塔',                               # 34
        '芙拉瑟',                               # 35
        '蕾娜',                                 # 36
        '梅贝尔市长',                           # 37
        '杜南公爵',                             # 38
        '管家菲利普',                           # 39
        '奈尔',                                 # 40
        '卡露娜',                               # 41
        '亚鲁瓦教授',                           # 42
        '希艾尔',                               # 43
        '爱蕾塔',                               # 44
        '爱珐',                                 # 45
        '西加罗',                               # 46
        '艾德尔',                               # 47
        '波尔多斯',                             # 48
        '诺莉雅',                               # 49
        '丽泽',                                 # 50
        '托尼奥',                               # 51
        '莉拉',                                 # 52
        '戴尔蒙市长',                           # 53
        '参观客',                               # 54
        '参观客',                               # 55
        '参观客',                               # 56
        '参观客',                               # 57
        '参观客',                               # 58
        '参观客',                               # 59
        '参观客',                               # 60
        '参观客',                               # 61
        '参观客',                               # 62
        'CH22000',                              # 63
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
        'ED6_DT07/CH02390 ._CH',             # 00
        'ED6_DT07/CH02590 ._CH',             # 01
        'ED6_DT07/CH02640 ._CH',             # 02
        'ED6_DT07/CH02630 ._CH',             # 03
        'ED6_DT07/CH02570 ._CH',             # 04
        'ED6_DT07/CH02320 ._CH',             # 05
        'ED6_DT07/CH02490 ._CH',             # 06
        'ED6_DT07/CH01660 ._CH',             # 07
        'ED6_DT07/CH01210 ._CH',             # 08
        'ED6_DT07/CH01430 ._CH',             # 09
        'ED6_DT07/CH01460 ._CH',             # 0A
        'ED6_DT07/CH02600 ._CH',             # 0B
        'ED6_DT07/CH01360 ._CH',             # 0C
        'ED6_DT07/CH01580 ._CH',             # 0D
        'ED6_DT07/CH01590 ._CH',             # 0E
        'ED6_DT07/CH01370 ._CH',             # 0F
        'ED6_DT07/CH01090 ._CH',             # 10
        'ED6_DT07/CH01080 ._CH',             # 11
        'ED6_DT07/CH01360 ._CH',             # 12
        'ED6_DT07/CH01590 ._CH',             # 13
        'ED6_DT07/CH02360 ._CH',             # 14
        'ED6_DT07/CH02140 ._CH',             # 15
        'ED6_DT07/CH02470 ._CH',             # 16
        'ED6_DT07/CH02060 ._CH',             # 17
        'ED6_DT07/CH01240 ._CH',             # 18
        'ED6_DT07/CH02050 ._CH',             # 19
        'ED6_DT07/CH01540 ._CH',             # 1A
        'ED6_DT07/CH01170 ._CH',             # 1B
        'ED6_DT07/CH01210 ._CH',             # 1C
        'ED6_DT07/CH01040 ._CH',             # 1D
        'ED6_DT07/CH01130 ._CH',             # 1E
        'ED6_DT07/CH01680 ._CH',             # 1F
        'ED6_DT07/CH01030 ._CH',             # 20
        'ED6_DT07/CH02410 ._CH',             # 21
        'ED6_DT07/CH02370 ._CH',             # 22
        'ED6_DT07/CH02500 ._CH',             # 23
        'ED6_DT06/CH20021 ._CH',             # 24
        'ED6_DT07/CH01200 ._CH',             # 25
        'ED6_DT07/CH02480 ._CH',             # 26
        'ED6_DT07/CH01120 ._CH',             # 27
        'ED6_DT07/CH01030 ._CH',             # 28
        'ED6_DT07/CH01130 ._CH',             # 29
        'ED6_DT07/CH01140 ._CH',             # 2A
        'ED6_DT07/CH01100 ._CH',             # 2B
        'ED6_DT07/CH01180 ._CH',             # 2C
        'ED6_DT07/CH01470 ._CH',             # 2D
        'ED6_DT07/CH01770 ._CH',             # 2E
        'ED6_DT07/CH01780 ._CH',             # 2F
        'ED6_DT07/CH02363 ._CH',             # 30
        'ED6_DT07/CH01373 ._CH',             # 31
        'ED6_DT07/CH01213 ._CH',             # 32
        'ED6_DT07/CH01593 ._CH',             # 33
        'ED6_DT07/CH01043 ._CH',             # 34
        'ED6_DT07/CH01033 ._CH',             # 35
        'ED6_DT07/CH01363 ._CH',             # 36
        'ED6_DT07/CH01690 ._CH',             # 37
    )

    AddCharChipPat(
        'ED6_DT07/CH02390P._CP',             # 00
        'ED6_DT07/CH02590P._CP',             # 01
        'ED6_DT07/CH02640P._CP',             # 02
        'ED6_DT07/CH02630P._CP',             # 03
        'ED6_DT07/CH02570P._CP',             # 04
        'ED6_DT07/CH02320P._CP',             # 05
        'ED6_DT07/CH02490P._CP',             # 06
        'ED6_DT07/CH01660P._CP',             # 07
        'ED6_DT07/CH01210P._CP',             # 08
        'ED6_DT07/CH01430P._CP',             # 09
        'ED6_DT07/CH01460P._CP',             # 0A
        'ED6_DT07/CH02600P._CP',             # 0B
        'ED6_DT07/CH01360P._CP',             # 0C
        'ED6_DT07/CH01580P._CP',             # 0D
        'ED6_DT07/CH01590P._CP',             # 0E
        'ED6_DT07/CH01370P._CP',             # 0F
        'ED6_DT07/CH01090P._CP',             # 10
        'ED6_DT07/CH01080P._CP',             # 11
        'ED6_DT07/CH01360P._CP',             # 12
        'ED6_DT07/CH01590P._CP',             # 13
        'ED6_DT07/CH02360P._CP',             # 14
        'ED6_DT07/CH02140P._CP',             # 15
        'ED6_DT07/CH02470P._CP',             # 16
        'ED6_DT07/CH02060P._CP',             # 17
        'ED6_DT07/CH01240P._CP',             # 18
        'ED6_DT07/CH02050P._CP',             # 19
        'ED6_DT07/CH01540P._CP',             # 1A
        'ED6_DT07/CH01170P._CP',             # 1B
        'ED6_DT07/CH01210P._CP',             # 1C
        'ED6_DT07/CH01040P._CP',             # 1D
        'ED6_DT07/CH01210P._CP',             # 1E
        'ED6_DT07/CH01680P._CP',             # 1F
        'ED6_DT07/CH01030P._CP',             # 20
        'ED6_DT07/CH02410P._CP',             # 21
        'ED6_DT07/CH02370P._CP',             # 22
        'ED6_DT07/CH02500P._CP',             # 23
        'ED6_DT06/CH20021P._CP',             # 24
        'ED6_DT07/CH01200P._CP',             # 25
        'ED6_DT07/CH02480P._CP',             # 26
        'ED6_DT07/CH01120P._CP',             # 27
        'ED6_DT07/CH01030P._CP',             # 28
        'ED6_DT07/CH01130P._CP',             # 29
        'ED6_DT07/CH01140P._CP',             # 2A
        'ED6_DT07/CH01100P._CP',             # 2B
        'ED6_DT07/CH01180P._CP',             # 2C
        'ED6_DT07/CH01470P._CP',             # 2D
        'ED6_DT07/CH01770P._CP',             # 2E
        'ED6_DT07/CH01780P._CP',             # 2F
        'ED6_DT07/CH02363P._CP',             # 30
        'ED6_DT07/CH01373P._CP',             # 31
        'ED6_DT07/CH01213P._CP',             # 32
        'ED6_DT07/CH01593P._CP',             # 33
        'ED6_DT07/CH01043P._CP',             # 34
        'ED6_DT07/CH01033P._CP',             # 35
        'ED6_DT07/CH01363P._CP',             # 36
        'ED6_DT07/CH01690P._CP',             # 37
    )

    DeclNpc(
        X                   = 116010,
        Z                   = 0,
        Y                   = 4800,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 5800,
        Z                   = 0,
        Y                   = 23600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 35,
        ChipIndex           = 0x23,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 33500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 6000,
        Z                   = 200,
        Y                   = 22200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 5800,
        Z                   = 0,
        Y                   = 23600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4300,
        Z                   = 200,
        Y                   = 22900,
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

    DeclNpc(
        X                   = 800,
        Z                   = 6000,
        Y                   = -13810,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 41400,
        Z                   = 0,
        Y                   = 7500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 87700,
        Z                   = 0,
        Y                   = 1000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 87700,
        Z                   = 0,
        Y                   = 2800,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 84400,
        Z                   = 0,
        Y                   = 1000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 89260,
        Z                   = 0,
        Y                   = 1520,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 3100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = -2800,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = -700,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 3500,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = -3100,
        Z                   = 0,
        Y                   = 5400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = -2900,
        Z                   = 0,
        Y                   = 30000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = -5500,
        Z                   = 0,
        Y                   = 35500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = -3400,
        Z                   = 0,
        Y                   = 28800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = -2000,
        Z                   = 0,
        Y                   = 700,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 1500,
        Z                   = 0,
        Y                   = 34700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = -6000,
        Z                   = 0,
        Y                   = 700,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = 82700,
        Z                   = 0,
        Y                   = 33000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 90900,
        Z                   = 0,
        Y                   = 33400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
    )

    DeclNpc(
        X                   = 92300,
        Z                   = 0,
        Y                   = 33400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 30,
    )

    DeclNpc(
        X                   = 85900,
        Z                   = 0,
        Y                   = 30400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = 83500,
        Z                   = 0,
        Y                   = 30000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = -3900,
        Z                   = 0,
        Y                   = 3100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = -3900,
        Z                   = 0,
        Y                   = 34700,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = -3000,
        Z                   = 0,
        Y                   = 34100,
        Direction           = 315,
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
        X                   = 45300,
        Z                   = 0,
        Y                   = 32600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 36,
    )

    DeclNpc(
        X                   = 43480,
        Z                   = 0,
        Y                   = 5500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 37,
    )

    DeclNpc(
        X                   = 2700,
        Z                   = 0,
        Y                   = 32500,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 38,
    )

    DeclNpc(
        X                   = 89800,
        Z                   = 0,
        Y                   = 29200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 39,
    )

    DeclNpc(
        X                   = 88400,
        Z                   = 0,
        Y                   = 30800,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 40,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 41,
    )

    DeclNpc(
        X                   = -6100,
        Z                   = 0,
        Y                   = 34900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 42,
    )

    DeclNpc(
        X                   = 3060,
        Z                   = 0,
        Y                   = 30300,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 43,
    )

    DeclNpc(
        X                   = -500,
        Z                   = 0,
        Y                   = 30900,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 44,
    )

    DeclNpc(
        X                   = -100,
        Z                   = 0,
        Y                   = 32600,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 55,
        ChipIndex           = 0x37,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 45,
    )

    DeclNpc(
        X                   = 300,
        Z                   = 0,
        Y                   = 29800,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 47,
    )

    DeclNpc(
        X                   = 3090,
        Z                   = 0,
        Y                   = 32340,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 46,
    )

    DeclNpc(
        X                   = -5900,
        Z                   = 0,
        Y                   = -300,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 49,
    )

    DeclNpc(
        X                   = 41520,
        Z                   = 0,
        Y                   = 1170,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 48,
    )

    DeclNpc(
        X                   = 30590,
        Z                   = 0,
        Y                   = 1500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 37,
        ChipIndex           = 0x25,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 50,
    )

    DeclNpc(
        X                   = 38380,
        Z                   = 0,
        Y                   = 1600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 51,
    )

    DeclNpc(
        X                   = 26440,
        Z                   = 0,
        Y                   = -160,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 52,
    )

    DeclNpc(
        X                   = 39730,
        Z                   = 0,
        Y                   = 31370,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 40,
        ChipIndex           = 0x28,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 53,
    )

    DeclNpc(
        X                   = 28810,
        Z                   = 0,
        Y                   = 31500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 41,
        ChipIndex           = 0x29,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 54,
    )

    DeclNpc(
        X                   = 45020,
        Z                   = 0,
        Y                   = 30260,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 42,
        ChipIndex           = 0x2A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 55,
    )

    DeclNpc(
        X                   = 57380,
        Z                   = 0,
        Y                   = 30950,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 43,
        ChipIndex           = 0x2B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 56,
    )

    DeclNpc(
        X                   = 43840,
        Z                   = 0,
        Y                   = 35940,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 44,
        ChipIndex           = 0x2C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 57,
    )

    DeclNpc(
        X                   = 24710,
        Z                   = 0,
        Y                   = 29820,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 45,
        ChipIndex           = 0x2D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 58,
    )

    DeclNpc(
        X                   = 85590,
        Z                   = 700,
        Y                   = 3050,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835044,
        ChipIndex           = 0x24,
        NpcIndex            = 0x166,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 51000,
        Y                   = 0,
        Z                   = 1400,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 75,
    )

    DeclEvent(
        X                   = 59000,
        Y                   = 0,
        Z                   = 1400,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 76,
    )

    DeclEvent(
        X                   = 33000,
        Y                   = 0,
        Z                   = 1400,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 77,
    )

    DeclEvent(
        X                   = 58990,
        Y                   = 0,
        Z                   = 31330,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 78,
    )

    DeclEvent(
        X                   = 33000,
        Y                   = 0,
        Z                   = 31400,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 79,
    )


    DeclActor(
        TriggerX            = 41160,
        TriggerZ            = 0,
        TriggerY            = 6230,
        TriggerRange        = 400,
        ActorX              = 41400,
        ActorZ              = 1500,
        ActorY              = 7500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 85590,
        TriggerZ            = 700,
        TriggerY            = 3400,
        TriggerRange        = 1000,
        ActorX              = 85590,
        ActorZ              = 1000,
        ActorY              = 3050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 61,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 48200,
        TriggerZ            = 0,
        TriggerY            = 0,
        TriggerRange        = 800,
        ActorX              = 48200,
        ActorZ              = 1000,
        ActorY              = 0,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 62,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 31580,
        TriggerZ            = 0,
        TriggerY            = 1450,
        TriggerRange        = 800,
        ActorX              = 31580,
        ActorZ              = 1000,
        ActorY              = 1450,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 63,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 51020,
        TriggerZ            = 0,
        TriggerY            = 31860,
        TriggerRange        = 800,
        ActorX              = 51020,
        ActorZ              = 1500,
        ActorY              = 31860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 64,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 57380,
        TriggerZ            = 0,
        TriggerY            = 31460,
        TriggerRange        = 800,
        ActorX              = 57380,
        ActorZ              = 1000,
        ActorY              = 31460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 65,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 31630,
        TriggerZ            = 0,
        TriggerY            = 31460,
        TriggerRange        = 800,
        ActorX              = 31630,
        ActorZ              = 1000,
        ActorY              = 31460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 66,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3420,
        TriggerZ            = 0,
        TriggerY            = 0,
        TriggerRange        = 800,
        ActorX              = 3420,
        ActorZ              = 1000,
        ActorY              = 0,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 67,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3570,
        TriggerZ            = 0,
        TriggerY            = 34450,
        TriggerRange        = 800,
        ActorX              = 3570,
        ActorZ              = 1200,
        ActorY              = 34450,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 68,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 790,
        TriggerZ            = 0,
        TriggerY            = 35530,
        TriggerRange        = 800,
        ActorX              = 790,
        ActorZ              = 1200,
        ActorY              = 35530,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 69,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -5010,
        TriggerZ            = 0,
        TriggerY            = 29180,
        TriggerRange        = 800,
        ActorX              = -5010,
        ActorZ              = 1200,
        ActorY              = 29180,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 70,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1970,
        TriggerZ            = 0,
        TriggerY            = 30780,
        TriggerRange        = 800,
        ActorX              = -1970,
        ActorZ              = 1200,
        ActorY              = 30780,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 71,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 93560,
        TriggerZ            = 0,
        TriggerY            = 33350,
        TriggerRange        = 800,
        ActorX              = 93560,
        ActorZ              = 1000,
        ActorY              = 33350,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 72,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 87220,
        TriggerZ            = 0,
        TriggerY            = 34060,
        TriggerRange        = 800,
        ActorX              = 87220,
        ActorZ              = 1000,
        ActorY              = 34060,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 73,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 85030,
        TriggerZ            = 0,
        TriggerY            = 33920,
        TriggerRange        = 800,
        ActorX              = 85030,
        ActorZ              = 1000,
        ActorY              = 33920,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 74,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_C06",          # 00, 0
        "Function_1_1308",         # 01, 1
        "Function_2_1340",         # 02, 2
        "Function_3_14EE",         # 03, 3
        "Function_4_153B",         # 04, 4
        "Function_5_1640",         # 05, 5
        "Function_6_1664",         # 06, 6
        "Function_7_1688",         # 07, 7
        "Function_8_16AC",         # 08, 8
        "Function_9_16D0",         # 09, 9
        "Function_10_1C20",        # 0A, 10
        "Function_11_1C25",        # 0B, 11
        "Function_12_228A",        # 0C, 12
        "Function_13_24A7",        # 0D, 13
        "Function_14_2765",        # 0E, 14
        "Function_15_2A6D",        # 0F, 15
        "Function_16_2D45",        # 10, 16
        "Function_17_2E7B",        # 11, 17
        "Function_18_2E80",        # 12, 18
        "Function_19_3149",        # 13, 19
        "Function_20_32C3",        # 14, 20
        "Function_21_3455",        # 15, 21
        "Function_22_34D6",        # 16, 22
        "Function_23_3ABA",        # 17, 23
        "Function_24_3AF8",        # 18, 24
        "Function_25_3DE0",        # 19, 25
        "Function_26_3E87",        # 1A, 26
        "Function_27_3FAC",        # 1B, 27
        "Function_28_3FFB",        # 1C, 28
        "Function_29_404C",        # 1D, 29
        "Function_30_4130",        # 1E, 30
        "Function_31_424C",        # 1F, 31
        "Function_32_42D5",        # 20, 32
        "Function_33_4342",        # 21, 33
        "Function_34_468F",        # 22, 34
        "Function_35_48C8",        # 23, 35
        "Function_36_4993",        # 24, 36
        "Function_37_4A86",        # 25, 37
        "Function_38_4CEC",        # 26, 38
        "Function_39_4D29",        # 27, 39
        "Function_40_4E33",        # 28, 40
        "Function_41_4E8F",        # 29, 41
        "Function_42_4F4E",        # 2A, 42
        "Function_43_4F82",        # 2B, 43
        "Function_44_4FB0",        # 2C, 44
        "Function_45_4FE0",        # 2D, 45
        "Function_46_5030",        # 2E, 46
        "Function_47_50BF",        # 2F, 47
        "Function_48_5175",        # 30, 48
        "Function_49_529C",        # 31, 49
        "Function_50_5604",        # 32, 50
        "Function_51_56B3",        # 33, 51
        "Function_52_574E",        # 34, 52
        "Function_53_5805",        # 35, 53
        "Function_54_586D",        # 36, 54
        "Function_55_58D2",        # 37, 55
        "Function_56_595E",        # 38, 56
        "Function_57_59E4",        # 39, 57
        "Function_58_5A48",        # 3A, 58
        "Function_59_5AB9",        # 3B, 59
        "Function_60_5DBA",        # 3C, 60
        "Function_61_6C0B",        # 3D, 61
        "Function_62_6C71",        # 3E, 62
        "Function_63_6CDB",        # 3F, 63
        "Function_64_6D2B",        # 40, 64
        "Function_65_6DB7",        # 41, 65
        "Function_66_6E0F",        # 42, 66
        "Function_67_6E6D",        # 43, 67
        "Function_68_6EC1",        # 44, 68
        "Function_69_6F14",        # 45, 69
        "Function_70_6F6D",        # 46, 70
        "Function_71_6FC2",        # 47, 71
        "Function_72_700F",        # 48, 72
        "Function_73_708C",        # 49, 73
        "Function_74_70E3",        # 4A, 74
        "Function_75_838E",        # 4B, 75
        "Function_76_8392",        # 4C, 76
        "Function_77_8396",        # 4D, 77
        "Function_78_839A",        # 4E, 78
        "Function_79_839E",        # 4F, 79
    )


    def Function_0_C06(): pass

    label("Function_0_C06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_C14")
    OP_A3(0x3FA)
    Event(0, 59)

    label("loc_C14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_C7B")
    SetChrPos(0x10, 5320, 250, 2110, 270)
    SetChrPos(0x11, 5300, 250, 32080, 267)
    SetChrFlags(0x11, 0x10)
    SetChrFlags(0x13, 0x80)
    SetChrPos(0x14, 400, 0, 0, 90)
    SetChrFlags(0x14, 0x4)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrPos(0x19, -2900, 0, 30000, 90)
    Jump("loc_12BA")

    label("loc_C7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_CBC")
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1D, 0x80)
    Jump("loc_12BA")

    label("loc_CBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_F31")
    SetChrPos(0x12, 95370, 250, 34220, 225)
    SetChrPos(0x8, 43470, 0, 5280, 225)
    OP_43(0x8, 0x0, 0x0, 0x2)
    ClearChrFlags(0x25, 0x80)
    SetChrPos(0x25, 42090, 0, 3930, 45)
    ClearChrFlags(0x26, 0x80)
    SetChrPos(0x26, 42970, 0, 2640, 0)
    SetChrPos(0x17, -1590, 0, 34700, 0)
    SetChrPos(0x10, 2790, 0, 5460, 225)
    SetChrPos(0x15, 4500, 250, 2970, 270)
    SetChrPos(0x16, -990, 0, -1260, 0)
    SetChrChipByIndex(0x16, 47)
    OP_43(0x16, 0x0, 0x0, 0x3)
    SetChrPos(0x18, -4990, 0, 5010, 180)
    SetChrChipByIndex(0x18, 46)
    OP_43(0x18, 0x0, 0x0, 0x4)
    ClearChrFlags(0x1E, 0x80)
    SetChrChipByIndex(0x1E, 51)
    SetChrPos(0x1E, -6000, 100, 700, 90)
    OP_44(0x1E, 0xFF)
    SetChrFlags(0x1E, 0x4)
    SetChrFlags(0x1E, 0x10)
    ClearChrFlags(0x32, 0x80)
    SetChrChipByIndex(0x32, 52)
    SetChrPos(0x32, -5960, 0, 3010, 90)
    OP_44(0x32, 0xFF)
    SetChrFlags(0x32, 0x4)
    SetChrFlags(0x32, 0x10)
    ClearChrFlags(0x31, 0x80)
    SetChrPos(0x31, -4000, 0, 4100, 270)
    SetChrChipByIndex(0x31, 53)
    OP_44(0x31, 0xFF)
    SetChrFlags(0x31, 0x4)
    SetChrFlags(0x31, 0x10)
    SetChrPos(0x14, -70, 0, 3050, 270)
    SetChrChipByIndex(0x14, 54)
    OP_44(0x14, 0xFF)
    SetChrFlags(0x14, 0x4)
    SetChrFlags(0x14, 0x10)
    SetChrPos(0x11, -6910, 0, 33220, 90)
    SetChrPos(0x19, 1300, 0, 28510, 90)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, 89110, 0, 29220, 90)
    SetChrFlags(0x21, 0x10)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 89160, 0, 34290, 0)
    ClearChrFlags(0x33, 0x80)
    SetChrPos(0x33, 85890, 0, 32890, 315)
    ClearChrFlags(0x2C, 0x80)
    SetChrPos(0x2C, 90550, 0, 29250, 270)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x27, 0x10)
    ClearChrFlags(0x2A, 0x80)
    SetChrPos(0x2A, 31660, 0, 100, 0)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2B, 0x10)
    SetChrPos(0x2B, 32619, 0, 320, 270)
    ClearChrFlags(0x35, 0x80)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x37, 0x80)
    ClearChrFlags(0x38, 0x80)
    ClearChrFlags(0x39, 0x80)
    ClearChrFlags(0x3A, 0x80)
    ClearChrFlags(0x3B, 0x80)
    ClearChrFlags(0x3C, 0x80)
    ClearChrFlags(0x3D, 0x80)
    Jump("loc_12BA")

    label("loc_F31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_1143")
    SetChrPos(0x11, -6910, 0, 33220, 90)
    SetChrPos(0x12, 95370, 250, 34220, 225)
    SetChrPos(0x8, 42940, 0, 1070, 270)
    SetChrFlags(0x8, 0x10)
    OP_43(0x8, 0x0, 0x0, 0x2)
    ClearChrFlags(0x34, 0x80)
    SetChrFlags(0x34, 0x10)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrPos(0x10, 2790, 0, 5460, 225)
    SetChrPos(0x15, 4500, 250, 2970, 270)
    SetChrPos(0x16, -990, 0, -1260, 0)
    SetChrChipByIndex(0x16, 47)
    OP_43(0x16, 0x0, 0x0, 0x3)
    SetChrPos(0x18, -4990, 0, 5010, 180)
    SetChrChipByIndex(0x18, 46)
    OP_43(0x18, 0x0, 0x0, 0x4)
    ClearChrFlags(0x24, 0x80)
    SetChrChipByIndex(0x24, 48)
    SetChrPos(0x24, -4019, 100, 3080, 270)
    OP_44(0x24, 0xFF)
    SetChrFlags(0x24, 0x4)
    SetChrFlags(0x24, 0x10)
    ClearChrFlags(0x33, 0x80)
    SetChrPos(0x33, -5040, 100, 2050, 0)
    ClearChrFlags(0x2C, 0x80)
    SetChrChipByIndex(0x2C, 50)
    SetChrPos(0x2C, -130, 0, 4000, 270)
    OP_44(0x2C, 0xFF)
    SetChrFlags(0x2C, 0x4)
    SetChrFlags(0x2C, 0x10)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, -1960, 0, -300, 90)
    SetChrChipByIndex(0x1C, 49)
    OP_44(0x1C, 0xFF)
    SetChrFlags(0x1C, 0x4)
    SetChrFlags(0x1C, 0x10)
    SetChrPos(0x19, 1300, 0, 28510, 90)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x10)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x10)
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x10)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x35, 0x80)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x37, 0x80)
    ClearChrFlags(0x38, 0x80)
    ClearChrFlags(0x39, 0x80)
    ClearChrFlags(0x3A, 0x80)
    ClearChrFlags(0x3B, 0x80)
    ClearChrFlags(0x3C, 0x80)
    ClearChrFlags(0x3D, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8B, 2)), scpexpr(EXPR_END)), "loc_1140")
    SetChrPos(0x25, 88600, 0, 34670, 0)
    SetChrPos(0x26, 89570, 0, 34410, 270)
    SetChrPos(0x29, -1680, 0, 34680, 0)
    ClearChrFlags(0x29, 0x80)

    label("loc_1140")

    Jump("loc_12BA")

    label("loc_1143")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_1199")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrPos(0x15, -5200, 0, 2050, 0)
    SetChrPos(0x16, 4500, 250, 4019, 270)
    SetChrPos(0x19, 790, 0, 34680, 0)
    Jump("loc_12BA")

    label("loc_1199")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_11C8")
    SetChrPos(0x11, 5300, 250, 32080, 267)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    Jump("loc_12BA")

    label("loc_11C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_11FF")
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    Jump("loc_12BA")

    label("loc_11FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_123B")
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    Jump("loc_12BA")

    label("loc_123B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_127C")
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    Jump("loc_12BA")

    label("loc_127C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_12BA")
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)

    label("loc_12BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12D4")
    OP_A2(0x443)

    label("loc_12D4")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (110, "loc_12E0"),
        (SWITCH_DEFAULT, "loc_12F6"),
    )


    label("loc_12E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8B, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12F3")
    OP_A2(0x432)
    Event(0, 60)

    label("loc_12F3")

    Jump("loc_12F6")

    label("loc_12F6")

    OP_51(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_C06 end

    def Function_1_1308(): pass

    label("Function_1_1308")

    OP_64(0x1, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_131B")
    OP_65(0x1, 0x1)

    label("loc_131B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x80)"), scpexpr(EXPR_END)), "loc_132F")
    OP_64(0x1, 0x1)
    SetChrFlags(0x3E, 0x80)

    label("loc_132F")

    OP_75(0x6, 0x0, 0x0)
    OP_74(0x6, 0x0, 0x0)
    Return()

    # Function_1_1308 end

    def Function_2_1340(): pass

    label("Function_2_1340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_134A")
    Jump("loc_1371")

    label("loc_134A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_135F")
    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1371")

    label("loc_135F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_1371")
    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1371")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1396")
    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_14D8")

    label("loc_1396")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13AF")
    OP_99(0xFE, 0x1, 0x7, 0x514)
    Jump("loc_14D8")

    label("loc_13AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13C8")
    OP_99(0xFE, 0x2, 0x7, 0x4E2)
    Jump("loc_14D8")

    label("loc_13C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E1")
    OP_99(0xFE, 0x3, 0x7, 0x4B0)
    Jump("loc_14D8")

    label("loc_13E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13FA")
    OP_99(0xFE, 0x4, 0x7, 0x47E)
    Jump("loc_14D8")

    label("loc_13FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1413")
    OP_99(0xFE, 0x5, 0x7, 0x44C)
    Jump("loc_14D8")

    label("loc_1413")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_142C")
    OP_99(0xFE, 0x6, 0x7, 0x41A)
    Jump("loc_14D8")

    label("loc_142C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1445")
    OP_99(0xFE, 0x0, 0x7, 0x54B)
    Jump("loc_14D8")

    label("loc_1445")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_145E")
    OP_99(0xFE, 0x1, 0x7, 0x519)
    Jump("loc_14D8")

    label("loc_145E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1477")
    OP_99(0xFE, 0x2, 0x7, 0x4E7)
    Jump("loc_14D8")

    label("loc_1477")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1490")
    OP_99(0xFE, 0x3, 0x7, 0x4B5)
    Jump("loc_14D8")

    label("loc_1490")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14A9")
    OP_99(0xFE, 0x4, 0x7, 0x483)
    Jump("loc_14D8")

    label("loc_14A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14C2")
    OP_99(0xFE, 0x5, 0x7, 0x451)
    Jump("loc_14D8")

    label("loc_14C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D8")
    OP_99(0xFE, 0x6, 0x7, 0x41F)

    label("loc_14D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_14ED")
    OP_99(0xFE, 0x0, 0x7, 0x4B0)
    Jump("loc_14D8")

    label("loc_14ED")

    Return()

    # Function_2_1340 end

    def Function_3_14EE(): pass

    label("Function_3_14EE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_153A")
    OP_8E(0xFE, 0xFFFFEC5A, 0x0, 0xFFFFFB14, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    OP_8E(0xFE, 0xFFFFFC22, 0x0, 0xFFFFFB14, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    Jump("Function_3_14EE")

    label("loc_153A")

    Return()

    # Function_3_14EE end

    def Function_4_153B(): pass

    label("Function_4_153B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_163F")
    OP_8E(0xFE, 0xFFFFFC0E, 0x0, 0x1356, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(3000)
    OP_8E(0xFE, 0x5D2, 0x0, 0x1356, 0x7D0, 0x0)
    OP_8E(0xFE, 0x5D2, 0x0, 0xD98, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7C6, 0x0, 0xC12, 0x7D0, 0x0)
    OP_8E(0xFE, 0x9EC, 0x0, 0xB86, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(3000)
    OP_8E(0xFE, 0x7C6, 0x0, 0xC12, 0x7D0, 0x0)
    OP_8E(0xFE, 0x5D2, 0x0, 0xD98, 0x7D0, 0x0)
    OP_8E(0xFE, 0x5D2, 0x0, 0x1356, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFC0E, 0x0, 0x1356, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(3000)
    OP_8E(0xFE, 0xFFFFEC82, 0x0, 0x1392, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(3000)
    Jump("Function_4_153B")

    label("loc_163F")

    Return()

    # Function_4_153B end

    def Function_5_1640(): pass

    label("Function_5_1640")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1663")
    OP_8D(0xFE, 24420, 1500, 29350, -1300, 1500)
    Jump("Function_5_1640")

    label("loc_1663")

    Return()

    # Function_5_1640 end

    def Function_6_1664(): pass

    label("Function_6_1664")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1687")
    OP_8D(0xFE, 38740, 33660, 43330, 28250, 1500)
    Jump("Function_6_1664")

    label("loc_1687")

    Return()

    # Function_6_1664 end

    def Function_7_1688(): pass

    label("Function_7_1688")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_16AB")
    OP_8D(0xFE, 42670, 31640, 49420, 28690, 2000)
    Jump("Function_7_1688")

    label("loc_16AB")

    Return()

    # Function_7_1688 end

    def Function_8_16AC(): pass

    label("Function_8_16AC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_16CF")
    OP_8D(0xFE, 23100, 31490, 27030, 28520, 3000)
    Jump("Function_8_16AC")

    label("loc_16CF")

    Return()

    # Function_8_16AC end

    def Function_9_16D0(): pass

    label("Function_9_16D0")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_17B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1757")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "#780F是艾丝蒂尔和约修亚啊。\x02\x03",
            "犯人总算给逮捕归案了，\x01",
            "实在是太好了。\x02\x03",
            "等会儿我想听你们\x01",
            "说明一下事情的经过。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17B4")

    label("loc_1757")


    ChrTalk(
        0xFE,
        (
            "#780F抓到袭击孤儿院的犯人\x01",
            "总算是让大家安心了。\x02\x03",
            "你们等会儿可以把\x01",
            "把事情的经过告诉我吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17B4")

    Jump("loc_1C1C")

    label("loc_17B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_1897")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_184A")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "#780F艾丝蒂尔、约修亚……\x02\x03",
            "我听说特蕾莎院长的事情了。\x02\x03",
            "怎么说呢……\x01",
            "实在是很过分的事啊……\x02\x03",
            "这件事实在无法用语言表达……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1894")

    label("loc_184A")


    ChrTalk(
        0xFE,
        (
            "#780F我听说特蕾莎院长的事情了。\x02\x03",
            "怎么说呢……\x01",
            "实在是很过分的事啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1894")

    Jump("loc_1C1C")

    label("loc_1897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_19B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1959")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "#780F艾丝蒂尔、约修亚，\x01",
            "这次真是麻烦你们了。\x02\x03",
            "舞台剧的演出很成功。\x01",
            "特别是约修亚饰演的塞茜莉亚公主，\x01",
            "演技和扮相实在是太感人了。\x02\x03",
            "下次有机会的话\x01",
            "请务必再到我们学院来玩。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19B4")

    label("loc_1959")


    ChrTalk(
        0xFE,
        (
            "#780F艾丝蒂尔、约修亚，\x01",
            "这次真是麻烦你们了。\x02\x03",
            "下次有机会的话\x01",
            "请务必再到我们学院来玩。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19B4")

    Jump("loc_1C1C")

    label("loc_19B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_1A6D")
    ClearChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A32")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "#780F哦，是你们。\x01",
            "这次真是史无前例的盛况啊。\x02\x03",
            "大家都很期待舞台剧，\x01",
            "请务必让学园祭圆满成功。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A6A")

    label("loc_1A32")


    ChrTalk(
        0xFE,
        (
            "#780F大家都很期待舞台剧。\x01",
            "请务必让学园祭圆满成功。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A6A")

    Jump("loc_1C1C")

    label("loc_1A6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_1BB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B45")
    OP_A2(0x457)
    OP_4A(0x34, 255)

    ChrTalk(
        0x8,
        (
            "#781F戴尔蒙市长，\x01",
            "自从去年的王国会议之后我们也好久不见了。\x02\x03",
            "这段时间，你身体怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x34,
        (
            "#661F就像你看到的，结实着呢。\x01",
            "科林兹校长也很精神嘛。\x02\x03",
            "今天我打算好好放松一下。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x34, 0x10)
    OP_4B(0x34, 255)
    Jump("loc_1BB5")

    label("loc_1B45")


    ChrTalk(
        0x8,
        (
            "#781F我还要找时间和市长先生谈谈\x01",
            "关于学院运营的事情呢。\x01",
            "　\x02\x03",
            "虽说是王立的教育机构，\x01",
            "但也要重视地方上的建议。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BB5")

    Jump("loc_1C1C")

    label("loc_1BB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_1C1C")

    ChrTalk(
        0xFE,
        (
            "#780F你们住宿的地方我们已经给安排好了。\x01",
            "　\x02\x03",
            "学院里也有食堂，\x01",
            "你们就安心准备好舞台剧吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C1C")

    TalkEnd(0x8)
    Return()

    # Function_9_16D0 end

    def Function_10_1C20(): pass

    label("Function_10_1C20")

    Call(0, 11)
    Return()

    # Function_10_1C20 end

    def Function_11_1C25(): pass

    label("Function_11_1C25")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1CBC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C98")
    OP_A2(0x2)

    ChrTalk(
        0xF,
        (
            "啊，怎么了？\x01",
            "你们要找人吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "现在正好是\x01",
            "上课结束的时间。\x01",
            "你们可以去和同学们见面。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CB9")

    label("loc_1C98")


    ChrTalk(
        0xF,
        (
            "啊，怎么了？\x01",
            "你们要找人吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CB9")

    Jump("loc_2286")

    label("loc_1CBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_1D07")

    ChrTalk(
        0xF,
        "呵呵，学园祭很成功呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "学生们正在\x01",
            "礼堂那里庆祝胜利呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2286")

    label("loc_1D07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_1D65")

    ChrTalk(
        0xF,
        (
            "说起来\x01",
            "真是出乎意料的盛况啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "很多人还带了孩子来，\x01",
            "要是有小孩迷路就糟了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2286")

    label("loc_1D65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_1E40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DF3")
    OP_A2(0x2)

    ChrTalk(
        0xF,
        (
            "各种活动都在\x01",
            "校园和主楼里进行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "下午礼堂那边\x01",
            "预定要演出舞台剧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "食堂作为休息场所开放，\x01",
            "你们可以好好利用。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E3D")

    label("loc_1DF3")


    ChrTalk(
        0xF,
        (
            "各种活动都在\x01",
            "校园和主楼里进行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "下午礼堂那边\x01",
            "预定要演出舞台剧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E3D")

    Jump("loc_2286")

    label("loc_1E40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_1ED1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EA5")
    OP_A2(0x2)

    ChrTalk(
        0xF,
        (
            "准备完成了吗？\x01",
            "明天就要正式表演了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "到了明天\x01",
            "就会有许多客人来参观了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ECE")

    label("loc_1EA5")


    ChrTalk(
        0xF,
        (
            "准备完成了吗？\x01",
            "明天就要正式表演了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ECE")

    Jump("loc_2286")

    label("loc_1ED1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_1F8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F52")
    OP_A2(0x2)

    ChrTalk(
        0xF,
        (
            "呵呵，一到下课时间，\x01",
            "校园里就会变得热闹起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "学园祭就要开始了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "希望同学们\x01",
            "都能加油哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F87")

    label("loc_1F52")


    ChrTalk(
        0xF,
        (
            "呵呵，一到下课时间，\x01",
            "校园里就会变得热闹起来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F87")

    Jump("loc_2286")

    label("loc_1F8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_20A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_205E")
    OP_A2(0x2)

    ChrTalk(
        0xF,
        (
            "啊，科洛丝。\x01",
            "你回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F对不起，\x01",
            "我到现在才回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "呵呵，回来就好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "要找校长的话，\x01",
            "他就在办公室里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "他也很担心\x01",
            "科洛丝你呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F啊，是的。\x01",
            "我们现在就过去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20A0")

    label("loc_205E")


    ChrTalk(
        0xF,
        (
            "要找校长的话，\x01",
            "他就在办公室里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "他也很担心\x01",
            "科洛丝你呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20A0")

    Jump("loc_2286")

    label("loc_20A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_215C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2136")
    OP_A2(0x2)

    ChrTalk(
        0xF,
        (
            "啊，科洛丝。\x01",
            "你们外出回来了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F啊，不是的……\x02\x03",
            "对不起，\x01",
            "我们还没有办完事呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "是吗。\x01",
            "外出时请务必要小心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2159")

    label("loc_2136")


    ChrTalk(
        0xF,
        (
            "科洛丝，\x01",
            "外出时请务必要小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2159")

    Jump("loc_2286")

    label("loc_215C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_21AE")

    ChrTalk(
        0xF,
        "啊，是想参观吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "很抱歉，\x01",
            "现在学生们正在上课，\x01",
            "不能带您参观。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2286")

    label("loc_21AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_2286")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2256")
    OP_A2(0x2)

    ChrTalk(
        0xF,
        (
            "啊，科洛丝。\x01",
            "已经回来了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F不是，\x01",
            "我正要带这两位朋友去卢安呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "是吗，难得的假日，\x01",
            "就好好地放松一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F嗯，谢谢了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2286")

    label("loc_2256")


    ChrTalk(
        0xF,
        (
            "科洛丝，\x01",
            "难得的假日，\x01",
            "就好好地放松一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2286")

    TalkEnd(0xF)
    Return()

    # Function_11_1C25 end

    def Function_12_228A(): pass

    label("Function_12_228A")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_22C6")

    ChrTalk(
        0xFE,
        (
            "课虽然上完了，\x01",
            "但还有学生们的问题要回答。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24A3")

    label("loc_22C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_2318")

    ChrTalk(
        0xFE,
        (
            "唔，\x01",
            "我们班的同学干劲热火朝天啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "大家做布景\x01",
            "也非常地努力嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24A3")

    label("loc_2318")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_2368")

    ChrTalk(
        0xFE,
        (
            "学园祭的主角\x01",
            "果然还是学生们啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "大家都比平时\x01",
            "要活跃许多呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24A3")

    label("loc_2368")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_2448")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2406")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "你们好像是\x01",
            "从洛连特来的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "其实我也是\x01",
            "洛连特出身的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说起来我父母\x01",
            "也要来参观学园祭呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……我要是能招待他们就好了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2445")

    label("loc_2406")


    ChrTalk(
        0xFE,
        (
            "对了对了……\x01",
            "舞台剧表演我也看了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那天真是很开心啊。\x02",
    )

    CloseMessageWindow()

    label("loc_2445")

    Jump("loc_24A3")

    label("loc_2448")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_24A3")

    ChrTalk(
        0xFE,
        (
            "学园祭快到了，\x01",
            "同学们就连上课\x01",
            "都开始坐不安定了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "呵呵，这也是没办法的呀。\x02",
    )

    CloseMessageWindow()

    label("loc_24A3")

    TalkEnd(0x10)
    Return()

    # Function_12_228A end

    def Function_13_24A7(): pass

    label("Function_13_24A7")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_2537")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_250D")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "唔唔，\x01",
            "这个问题……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "怎么做好呢？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x10)
    Jump("loc_2534")

    label("loc_250D")


    ChrTalk(
        0xFE,
        (
            "呼，这里的学生\x01",
            "都很热心于学习呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2534")

    Jump("loc_2761")

    label("loc_2537")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_2599")

    ChrTalk(
        0xFE,
        (
            "呼，真没劲……\x01",
            "还没到演出的时间吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "拜托你们二位了！\x01",
            "我相信一定能取得成功的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2761")

    label("loc_2599")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_2647")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2623")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "我们班的同学相当认真呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然我觉得\x01",
            "研究发表什么的太朴素了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过这样也好，\x01",
            "有很多客人来看呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2644")

    label("loc_2623")


    ChrTalk(
        0xFE,
        (
            "决不能输给\x01",
            "米丽亚的班级……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2644")

    Jump("loc_2761")

    label("loc_2647")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_2761")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_273A")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "啊，科洛丝。\x01",
            "你回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F碧欧拉老师，\x01",
            "我刚刚才回来。\x02\x03",
            "对不起，\x01",
            "我又没来上课。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "呵呵，没关系。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你不是有重要的事情吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "有时间的话来一下办公室，\x01",
            "我给你漏下的上课笔记。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F嗯，我过会儿就去。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2761")

    label("loc_273A")


    ChrTalk(
        0xFE,
        (
            "我还是趁现在\x01",
            "批改一下考试卷子吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2761")

    TalkEnd(0x11)
    Return()

    # Function_13_24A7 end

    def Function_14_2765(): pass

    label("Function_14_2765")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_27BB")

    ChrTalk(
        0xFE,
        (
            "我是今年\x01",
            "入学考试的出题老师。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "呵呵……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我已经跃跃欲试了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A69")

    label("loc_27BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_28B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2855")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "为什么我们班的同学\x01",
            "尽办些游戏和占卜的活动……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "维奥拉的班级\x01",
            "都是很正经的东西呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那个班的老师不行，\x01",
            "学生们却都很优秀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28AF")

    label("loc_2855")


    ChrTalk(
        0xFE,
        (
            "为什么我们班的同学\x01",
            "尽办些游戏和占卜的活动……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "维奥拉的班级\x01",
            "都是很正经的东西呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28AF")

    Jump("loc_2A69")

    label("loc_28B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_28E6")

    ChrTalk(
        0xFE,
        "人还真是多呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "大家都很闲吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A69")

    label("loc_28E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_2983")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2951")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "嗯，明天就能好好看到\x01",
            "同学们努力的成果了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "无论怎样，\x01",
            "那天我可不能再啰嗦了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2980")

    label("loc_2951")


    ChrTalk(
        0xFE,
        (
            "嗯，明天就能好好看到\x01",
            "同学们努力的成果了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2980")

    Jump("loc_2A69")

    label("loc_2983")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_2A69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A13")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "在学园祭的准备期间，\x01",
            "大家学习都提不起精神来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就算在课上\x01",
            "也开始不愿动脑筋了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要不要明天\x01",
            "来次突击测验呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A69")

    label("loc_2A13")


    ChrTalk(
        0xFE,
        (
            "在学园祭的准备期间，\x01",
            "大家学习都提不起精神来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要不要明天\x01",
            "来次突击测验呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A69")

    TalkEnd(0x12)
    Return()

    # Function_14_2765 end

    def Function_15_2A6D(): pass

    label("Function_15_2A6D")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_2ABB")

    ChrTalk(
        0xFE,
        "嗯，差不多该去巡视了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我要看看\x01",
            "有没有同学太过懒散了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D41")

    label("loc_2ABB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_2BAB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_2B39")

    ChrTalk(
        0xFE,
        "哦，昨天真是辛苦你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我真是个不称职的老师啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了防止再发生突发事件，\x01",
            "我在这里待命。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BA8")

    label("loc_2B39")


    ChrTalk(
        0xFE,
        (
            "昨天，\x01",
            "有学生说在旧校舍看到了魔兽。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了慎重起见，\x01",
            "我把旧校舍的门锁紧了。\x01",
            "不过一会儿还是再去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BA8")

    Jump("loc_2D41")

    label("loc_2BAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_2CB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C4D")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "这个学园一共设立了\x01",
            "三个方向的专业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我教的科目则是\x01",
            "所有专业都必修的科目——体育。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在这个时候我没有课，\x01",
            "就来整理一下教案了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CB1")

    label("loc_2C4D")


    ChrTalk(
        0xFE,
        (
            "我教的科目则是\x01",
            "所有专业都必修的科目——体育。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在这个时候我没有课，\x01",
            "就来整理一下教案了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CB1")

    Jump("loc_2D41")

    label("loc_2CB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2D41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D20")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "唔，怎么，\x01",
            "你们是哪个班的学生？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在正在上课哦。\x01",
            "要有外出许可证\x01",
            "才能出去哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D41")

    label("loc_2D20")


    ChrTalk(
        0xFE,
        (
            "要有外出许可证\x01",
            "才能出去哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D41")

    TalkEnd(0x13)
    Return()

    # Function_15_2A6D end

    def Function_16_2D45(): pass

    label("Function_16_2D45")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_2DB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D99")
    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "呼～\x01",
            "今天的课总算上完了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "下午的课\x01",
            "一定会睡着的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DB6")

    label("loc_2D99")


    ChrTalk(
        0xFE,
        (
            "下午的课\x01",
            "一定会睡着的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DB6")

    Jump("loc_2E77")

    label("loc_2DB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_2E77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E31")
    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "我一直在照顾\x01",
            "我们社团的店面呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "班里的活动\x01",
            "就没办法参加了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "感觉真是很充实呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E77")

    label("loc_2E31")


    ChrTalk(
        0xFE,
        (
            "我一直在照顾\x01",
            "我们社团的店面呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "都顾不上照顾\x01",
            "班里的茶座了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E77")

    TalkEnd(0x14)
    Return()

    # Function_16_2D45 end

    def Function_17_2E7B(): pass

    label("Function_17_2E7B")

    Call(0, 18)
    Return()

    # Function_17_2E7B end

    def Function_18_2E80(): pass

    label("Function_18_2E80")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_2E8D")
    Jump("loc_2F06")

    label("loc_2E8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_2F06")
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

    MenuEnd(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EF2")
    OP_0D()
    OP_A9(0x31)
    OP_56(0x0)
    TalkEnd(0x15)
    Return()

    label("loc_2EF2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F03")
    TalkEnd(0x15)
    Return()

    label("loc_2F03")

    Jump("loc_2F06")

    label("loc_2F06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_2F4F")

    ChrTalk(
        0x15,
        "那么，该去社团活动了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "今天要把\x01",
            "画到一半的绘画完成！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3145")

    label("loc_2F4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_2F92")

    ChrTalk(
        0x15,
        (
            "嗯，\x01",
            "茶座还是要办成这样才对啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "辛苦也值得了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3145")

    label("loc_2F92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_2FF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FD2")
    OP_A2(0x8)

    ChrTalk(
        0x15,
        (
            "……那边桌子的客人\x01",
            "难道是真正的女佣？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FF5")

    label("loc_2FD2")


    ChrTalk(
        0x15,
        (
            "因为通宵工作，\x01",
            "现在好困啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FF5")

    Jump("loc_3145")

    label("loc_2FF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_3092")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3047")
    OP_A2(0x8)

    ChrTalk(
        0x15,
        (
            "唔哇哇！\x01",
            "怎么回事！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "呆在这里\x01",
            "会来不及准备的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_308F")

    label("loc_3047")


    ChrTalk(
        0x15,
        (
            "……难道说\x01",
            "这样下去要通宵赶工了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "呼，\x01",
            "做衣服花了太多时间了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_308F")

    Jump("loc_3145")

    label("loc_3092")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_3145")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3127")
    OP_A2(0x8)

    ChrTalk(
        0x15,
        "啦啦啦～～⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "我正在做\x01",
            "摆摊时穿的衣服。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "唔～就是要在这种时候集中精力！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "因为做这种东西\x01",
            "是我最喜欢干的事情了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3145")

    label("loc_3127")


    ChrTalk(
        0x15,
        "接下来还要做房间的装饰。\x02",
    )

    CloseMessageWindow()

    label("loc_3145")

    TalkEnd(0x15)
    Return()

    # Function_18_2E80 end

    def Function_19_3149(): pass

    label("Function_19_3149")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_318F")

    ChrTalk(
        0xFE,
        "欢迎光临～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果需要的话，\x01",
            "我可以帮你们找空位。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32BF")

    label("loc_318F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_31D5")

    ChrTalk(
        0xFE,
        "嘿嘿，这件制服很可爱吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "坎诺还为我准备了好多呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_32BF")

    label("loc_31D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_323F")

    ChrTalk(
        0xFE,
        (
            "一想时间还很充裕\x01",
            "就不由自主地松懈了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过应该还来得及。\x01",
            "努力把店面打扮得漂亮一些吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32BF")

    label("loc_323F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_32BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3290")
    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "坎诺君的手\x01",
            "可巧啦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这次他缝了个\x01",
            "布娃娃给我呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32BF")

    label("loc_3290")


    ChrTalk(
        0xFE,
        (
            "就算是演出用的女佣服装\x01",
            "也是他自己做的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32BF")

    TalkEnd(0x16)
    Return()

    # Function_19_3149 end

    def Function_20_32C3(): pass

    label("Function_20_32C3")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_3380")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_334F")
    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "刚才讲的课，\x01",
            "有一些地方不明白……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "我还想问问老师呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "米丽亚老师\x01",
            "才刚上完课\x01",
            "就马上回办公室了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_337D")

    label("loc_334F")


    ChrTalk(
        0xFE,
        (
            "米丽亚老师\x01",
            "才刚上完课\x01",
            "就马上回办公室了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_337D")

    Jump("loc_3451")

    label("loc_3380")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_3451")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_340C")
    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "社会系各位的作品\x01",
            "都是研究成果发表啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哇……真是厉害啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们系的同学\x01",
            "只会办茶座或者\x01",
            "鬼怪屋什么的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3451")

    label("loc_340C")


    ChrTalk(
        0xFE,
        (
            "社会系各位的作品\x01",
            "都是研究成果发表啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哇……真是厉害啊……\x02",
    )

    CloseMessageWindow()

    label("loc_3451")

    TalkEnd(0x17)
    Return()

    # Function_20_32C3 end

    def Function_21_3455(): pass

    label("Function_21_3455")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_348F")

    ChrTalk(
        0xFE,
        (
            "欢迎光临。\x01",
            "这里是我们的茶座『芳塔娜』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34D2")

    label("loc_348F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_34D2")

    ChrTalk(
        0xFE,
        (
            "穿成这个样子\x01",
            "虽然有点不好意思，\x01",
            "但为了学园祭，忍了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34D2")

    TalkEnd(0x18)
    Return()

    # Function_21_3455 end

    def Function_22_34D6(): pass

    label("Function_22_34D6")

    TalkBegin(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_350A")

    ChrTalk(
        0xFE,
        (
            "唔，\x01",
            "今天也是很有意义的一课啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AB6")

    label("loc_350A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_361D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35B4")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "有很多前辈\x01",
            "和市民们前来参观。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然办娱乐活动很有意思，\x01",
            "不过公布我们的研究成果也是很重要的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……虽说如此，\x01",
            "考试也不会得到更高的分数。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_361A")

    label("loc_35B4")


    ChrTalk(
        0xFE,
        (
            "有很多前辈\x01",
            "和市民们前来参观。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然办娱乐活动很有意思，\x01",
            "不过公布我们的研究成果也是很重要的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_361A")

    Jump("loc_3AB6")

    label("loc_361D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_38BC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_370A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36E4")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "我们社会系发表了\x01",
            "从各种产业的经济指标上\x01",
            "进行经济动向的预测的研究。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且也收集了\x01",
            "通俗易懂的关于卢安地区\x01",
            "历史和发展的资料。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果有兴趣的话\x01",
            "就请看一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3707")

    label("loc_36E4")


    ChrTalk(
        0xFE,
        (
            "如果有兴趣的话\x01",
            "就请看一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3707")

    Jump("loc_38B9")

    label("loc_370A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_380F")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "我们社会系发表了\x01",
            "从各种产业的经济指标上\x01",
            "进行经济动向的预测的研究。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且也收集了\x01",
            "通俗易懂的关于卢安地区\x01",
            "历史和发展的资料。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然有几份资料没到手，\x01",
            "但在这么点时间里，\x01",
            "能做成这么完善的内容也算不错了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果有兴趣的话\x01",
            "就请看一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38B9")

    label("loc_380F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_3897")

    ChrTalk(
        0xFE,
        (
            "虽然没赶上这次发表，\x01",
            "但是《卢安经济史》是很贵重的资料。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果你们看到那三本书的话，\x01",
            "麻烦帮我放回资料室的书架上。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38B9")

    label("loc_3897")


    ChrTalk(
        0xFE,
        "如果有兴趣的话就请看一下吧。\x02",
    )

    CloseMessageWindow()

    label("loc_38B9")

    Jump("loc_3AB6")

    label("loc_38BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_3973")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3947")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "唔，还是需要一些\x01",
            "辅助研究的资料啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "时间不够了啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过在有限的时间里，\x01",
            "内容已经可算是做得很完善了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3970")

    label("loc_3947")


    ChrTalk(
        0xFE,
        (
            "唔，还是需要一些\x01",
            "辅助研究的资料啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3970")

    Jump("loc_3AB6")

    label("loc_3973")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_3AB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A98")
    OP_A2(0xC)

    ChrTalk(
        0xFE,
        (
            "啊，科洛丝。\x01",
            "你终于回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们班级的节目\x01",
            "准备工作进展得很顺利啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你们舞台剧方面怎么样了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "听说连主要演员\x01",
            "都还没决定下来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F呵呵，罗基克，\x01",
            "那件事已经解决了。\x02\x03",
            "舞台剧方面我们不会输的。\x01",
            "敬请期待哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哦，是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那我们互相加油吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AB6")

    label("loc_3A98")


    ChrTalk(
        0xFE,
        "科洛丝，我们互相加油吧。\x02",
    )

    CloseMessageWindow()

    label("loc_3AB6")

    TalkEnd(0x19)
    Return()

    # Function_22_34D6 end

    def Function_23_3ABA(): pass

    label("Function_23_3ABA")

    TalkBegin(0x1A)

    ChrTalk(
        0xFE,
        (
            "今年怎么没有\x01",
            "鬼怪屋呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这明明是惯例的……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x1A)
    Return()

    # Function_23_3ABA end

    def Function_24_3AF8(): pass

    label("Function_24_3AF8")

    TalkBegin(0x1B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_3B51")

    ChrTalk(
        0xFE,
        (
            "这次的女王诞辰庆典上\x01",
            "要召开武术大会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们的击剑部\x01",
            "也好想参加啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DDC")

    label("loc_3B51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_3C1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BCD")
    OP_A2(0xE)

    ChrTalk(
        0xFE,
        (
            "我太过忙于这里的活动，\x01",
            "连社团开的店\x01",
            "都没能去帮上忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "等到店员需要换班的时候\x01",
            "我再过去看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C1B")

    label("loc_3BCD")


    ChrTalk(
        0xFE,
        (
            "来这里参观的人\x01",
            "真是多啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "还有热心人向我们\x01",
            "提出不少尖锐的问题呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C1B")

    Jump("loc_3DDC")

    label("loc_3C1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_3D0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CB2")
    OP_A2(0xE)

    ChrTalk(
        0xFE,
        (
            "我是从卡尔瓦德共和国\x01",
            "来这里进修的留学生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这次我从研究发表的\x01",
            "准备中也学到不少。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我认为这是\x01",
            "很有意义的一件事情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D0C")

    label("loc_3CB2")


    ChrTalk(
        0xFE,
        (
            "我是从卡尔瓦德共和国\x01",
            "来这里进修的留学生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这次我从研究发表的\x01",
            "准备中也学到不少。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D0C")

    Jump("loc_3DDC")

    label("loc_3D0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_3DDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D89")
    OP_A2(0xE)

    ChrTalk(
        0xFE,
        "啊，科洛丝。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们班的活动\x01",
            "大致都准备好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过罗基克\x01",
            "好像还有些不放心，\x01",
            "去了资料室。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DDC")

    label("loc_3D89")


    ChrTalk(
        0xFE,
        (
            "我们班的活动\x01",
            "大致都准备好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过罗基克\x01",
            "好像还有些不放心，\x01",
            "去了资料室。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DDC")

    TalkEnd(0x1B)
    Return()

    # Function_24_3AF8 end

    def Function_25_3DE0(): pass

    label("Function_25_3DE0")

    TalkBegin(0x1C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E35")
    OP_A2(0xF)

    ChrTalk(
        0xFE,
        (
            "下午我就要\x01",
            "为社团去看店了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因此我只有\x01",
            "趁现在可以玩一会。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E83")

    label("loc_3E35")


    ChrTalk(
        0xFE,
        (
            "上午是同社团的\x01",
            "罗迪在看店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为太热闹了，\x01",
            "所以我想很快就能知道了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E83")

    TalkEnd(0x1C)
    Return()

    # Function_25_3DE0 end

    def Function_26_3E87(): pass

    label("Function_26_3E87")

    TalkBegin(0x1D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_3EE8")

    ChrTalk(
        0xFE,
        (
            "……碧欧拉老师\x01",
            "从刚才开始就在打哈欠。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难得她那么漂亮，\x01",
            "可以吸引客人来……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FA8")

    label("loc_3EE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_3FA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F64")
    OP_A2(0x10)

    ChrTalk(
        0xFE,
        (
            "呵呵，\x01",
            "今天我们给客人当导游。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "根据大家的需要，\x01",
            "我们会对社会系的研究成果\x01",
            "进行浅显易懂的说明。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FA8")

    label("loc_3F64")


    ChrTalk(
        0xFE,
        (
            "根据大家的需要，\x01",
            "我们会对社会系的研究成果\x01",
            "进行浅显易懂的说明。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FA8")

    TalkEnd(0x1D)
    Return()

    # Function_26_3E87 end

    def Function_27_3FAC(): pass

    label("Function_27_3FAC")

    TalkBegin(0x1E)

    ChrTalk(
        0xFE,
        "啊，是前辈们呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嘿嘿，我呀，\x01",
            "上午负责看店，\x01",
            "下午就可以玩了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x1E)
    Return()

    # Function_27_3FAC end

    def Function_28_3FFB(): pass

    label("Function_28_3FFB")

    TalkBegin(0x1F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_4048")

    ChrTalk(
        0xFE,
        "呵呵，我知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真让人欣慰呀，\x01",
            "连基诺奇奥也做得很好……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4048")

    TalkEnd(0x1F)
    Return()

    # Function_28_3FFB end

    def Function_29_404C(): pass

    label("Function_29_404C")

    TalkBegin(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_40DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40B8")
    OP_A2(0x13)

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "好像比我想象的更加有趣呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不知道提出这个方案的人\x01",
            "是怎么想出来的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40DA")

    label("loc_40B8")


    ChrTalk(
        0xFE,
        "呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "唔……好困呀……\x02",
    )

    CloseMessageWindow()

    label("loc_40DA")

    Jump("loc_412C")

    label("loc_40DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_412C")

    ChrTalk(
        0xFE,
        (
            "哎……\x01",
            "为什么妈妈和妹妹会来呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不是说因为工作\x01",
            "不能来了吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_412C")

    TalkEnd(0x20)
    Return()

    # Function_29_404C end

    def Function_30_4130(): pass

    label("Function_30_4130")

    TalkBegin(0x21)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_4164")

    ChrTalk(
        0xFE,
        (
            "姐姐！？\x01",
            "家里的店没人管不要紧吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4248")

    label("loc_4164")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_4248")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41F8")
    OP_A2(0x14)

    ChrTalk(
        0xFE,
        (
            "结果昨天我们\x01",
            "还是没能完成展示的准备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是今天早上来看，\x01",
            "已经全部完成了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "昨天回去的时候\x01",
            "的确是只做到一半啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4248")

    label("loc_41F8")


    ChrTalk(
        0xFE,
        (
            "昨天回去的时候\x01",
            "的确还没有完成啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我问过大家，\x01",
            "但每个人都说不知道。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4248")

    TalkEnd(0x21)
    Return()

    # Function_30_4130 end

    def Function_31_424C(): pass

    label("Function_31_424C")

    TalkBegin(0x22)

    ChrTalk(
        0xFE,
        (
            "我和蕾娜不仅\x01",
            "属于同一个班级和社团，\x01",
            "就连宿舍也是在同一个房间……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "这可真是受不了呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只有现在\x01",
            "才能享受点自由。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x22)
    Return()

    # Function_31_424C end

    def Function_32_42D5(): pass

    label("Function_32_42D5")

    TalkBegin(0x23)

    ChrTalk(
        0xFE,
        (
            "差不多把展示的\x01",
            "所有内容都看完了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过把看店的芙拉瑟给冷落了……\x01",
            "不，要好好地鼓励她才行。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x23)
    Return()

    # Function_32_42D5 end

    def Function_33_4342(): pass

    label("Function_33_4342")

    TalkBegin(0x24)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_4392")

    ChrTalk(
        0xFE,
        (
            "#610F呵呵，\x01",
            "这个真是很有趣呢。\x02\x03",
            "演出是在下午吧，\x01",
            "我很期待哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_468B")

    label("loc_4392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_468B")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_43BB")
    SetChrSubChip(0xFE, 2)
    Jump("loc_43EC")

    label("loc_43BB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_43D1")
    SetChrSubChip(0xFE, 1)
    Jump("loc_43EC")

    label("loc_43D1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_43E7")
    SetChrSubChip(0xFE, 0)
    Jump("loc_43EC")

    label("loc_43E7")

    SetChrSubChip(0xFE, 2)

    label("loc_43EC")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_461A")
    OP_A2(0x453)

    ChrTalk(
        0x101,
        "#004F啊，梅贝尔市长！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#613F啊，\x01",
            "这不是艾丝蒂尔和约修亚吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F市长您为什么会在这里呢？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#611F呵呵，\x01",
            "其实我是这个学院的毕业生。\x02\x03",
            "每年的学园祭都要来出席的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哦，是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#610F那么你们俩是为什么来这儿的啊？\x01",
            "　\x02\x03",
            "难道是为了协会的工作？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F嘿嘿，其实呢……\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔\x01",
            "向梅贝尔市长说明了事情的经过。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(
        0xFE,
        (
            "#613F哦，是协助演出啊。\x02\x03",
            "#611F我也认为演出是很考功夫的。\x01",
            "　\x02\x03",
            "呵呵，连艾丝蒂尔\x01",
            "和约修亚也参加演出的话，\x01",
            "那我真要好好看看才行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F（唔，真不想让\x01",
            "　认识的人看到啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4686")

    label("loc_461A")


    ChrTalk(
        0xFE,
        (
            "#610F我也认为演出是很考功夫的。\x01",
            "　\x02\x03",
            "呵呵，连艾丝蒂尔\x01",
            "和约修亚也参加演出的话，\x01",
            "那我真要好好看看才行呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4686")

    SetChrSubChip(0xFE, 0)

    label("loc_468B")

    TalkEnd(0x24)
    Return()

    # Function_33_4342 end

    def Function_34_468F(): pass

    label("Function_34_468F")

    TalkBegin(0x25)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_4785")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_472A")
    OP_A2(0x18)

    ChrTalk(
        0xFE,
        (
            "#220F哦，下午要演出啊。\x02\x03",
            "虽然这里及不上\x01",
            "在王都举办的华丽舞台剧……\x02\x03",
            "毕竟应酬还是应酬啊，\x01",
            "哈哈，身为未来国王的我就凑合看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4782")

    label("loc_472A")


    ChrTalk(
        0x117,
        (
            "#220F哦，下午要演出啊。\x02\x03",
            "毕竟应酬还是应酬啊。\x01",
            "哈哈，身为未来国王的我就凑合看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4782")

    Jump("loc_48C4")

    label("loc_4785")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_48C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4877")
    OP_A2(0x454)

    ChrTalk(
        0xFE,
        (
            "#220F这里可是王家出钱办的学院。\x01",
            "　\x02\x03",
            "我作为女王的外甥，\x01",
            "一定要好好视察。\x02\x03",
            "#221F呵呵呵，想必这里的学生\x01",
            "一定感到万分的光荣吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F（怎么把这个大叔也邀请过来了……）\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F（嗯，\x01",
            "　好像不邀请也不行啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48C4")

    label("loc_4877")


    ChrTalk(
        0x117,
        (
            "#220F这里可是王家出钱办的学院。\x01",
            "　\x02\x03",
            "我作为女王的外甥，\x01",
            "一定要好好视察。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48C4")

    TalkEnd(0x25)
    Return()

    # Function_34_468F end

    def Function_35_48C8(): pass

    label("Function_35_48C8")

    TalkBegin(0x26)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_4924")

    ChrTalk(
        0xFE,
        (
            "#720F这里真不愧是杰尼丝王立学院啊。\x01",
            "　\x02\x03",
            "就连学园祭也办得像模像样的……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_498F")

    label("loc_4924")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_498F")
    OP_62(0x26, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "#722F大、大人，\x01",
            "请恕冒昧直言……\x02\x03",
            "在公众面前，\x01",
            "请务必注意一下您的言词。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_498F")

    TalkEnd(0x26)
    Return()

    # Function_35_48C8 end

    def Function_36_4993(): pass

    label("Function_36_4993")

    TalkBegin(0x27)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A24")
    OP_A2(0x1A)

    ChrTalk(
        0xFE,
        (
            "#140F原来下午有演出啊。\x02\x03",
            "#142F而且还是古典名作『白花恋诗』……\x01",
            "　\x02\x03",
            "不过话说回来，这舞台剧对\x01",
            "学生们来说是不是有点太难了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A82")

    label("loc_4A24")


    ChrTalk(
        0xFE,
        (
            "#142F演出剧目是『白花恋诗』啊。\x02\x03",
            "不过话说回来，这舞台剧对\x01",
            "学生们来说是不是有点太难了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A82")

    TalkEnd(0x27)
    Return()

    # Function_36_4993 end

    def Function_37_4A86(): pass

    label("Function_37_4A86")

    TalkBegin(0x28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CB1")
    OP_A2(0x456)

    ChrTalk(
        0x101,
        "#000F啊，是卡露娜姐姐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F您好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呀，是你们啊……\x01",
            "我听嘉恩说了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们是来给\x01",
            "学园祭帮忙的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嘿嘿，差不多这样啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F卡露娜前辈\x01",
            "是来做警卫之类的工作吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "没错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这里的毕业生大多都是\x01",
            "在利贝尔各界活跃的著名人士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "每年的学园祭，\x01",
            "他们都会作为客人被邀请到在这里来聚会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "担任警卫的我\x01",
            "必须要十分仔细才行。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 3)), scpexpr(EXPR_END)), "loc_4C38")

    ChrTalk(
        0x102,
        (
            "#010F说起来，\x01",
            "梅贝尔市长也是这里的毕业生呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C70")

    label("loc_4C38")


    ChrTalk(
        0x101,
        (
            "#000F哎……说起来，\x01",
            "那个谁好像也是这里的毕业生……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C70")


    ChrTalk(
        0xFE,
        (
            "嗯，警备方面就交给我，\x01",
            "你们就尽心帮助学院其他工作吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x456)
    Jump("loc_4CE8")

    label("loc_4CB1")


    ChrTalk(
        0xFE,
        (
            "警备工作就交给我，\x01",
            "你们就尽心帮助学院其他工作吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CE8")

    TalkEnd(0x28)
    Return()

    # Function_37_4A86 end

    def Function_38_4CEC(): pass

    label("Function_38_4CEC")

    TalkBegin(0x29)

    ChrTalk(
        0xFE,
        (
            "#130F哦哦……\x02\x03",
            "原来如此，\x01",
            "学生们调查得很详细啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x29)
    Return()

    # Function_38_4CEC end

    def Function_39_4D29(): pass

    label("Function_39_4D29")

    TalkBegin(0x2A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_4D57")

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "在这里稍微休息一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E2F")

    label("loc_4D57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_4E2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DDF")
    OP_A2(0x1C)

    ChrTalk(
        0xFE,
        (
            "今天特地请假\x01",
            "来看我儿子的英姿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "爱蕾塔好像\x01",
            "也玩得十分开心呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在开始我要\x01",
            "显出更具母亲魅力的样子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E2F")

    label("loc_4DDF")


    ChrTalk(
        0xFE,
        (
            "今天特地请假\x01",
            "来看我儿子的英姿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在开始我要\x01",
            "显出更具母亲魅力的样子。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E2F")

    TalkEnd(0x2A)
    Return()

    # Function_39_4D29 end

    def Function_40_4E33(): pass

    label("Function_40_4E33")

    TalkBegin(0x2B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_4E63")

    ChrTalk(
        0xFE,
        (
            "爱蕾塔渴了，\x01",
            "好想喝果汁啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E8B")

    label("loc_4E63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_4E8B")

    ChrTalk(
        0xFE,
        (
            "嘿嘿，哥哥～\x01",
            "我们来玩了～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E8B")

    TalkEnd(0x2B)
    Return()

    # Function_40_4E33 end

    def Function_41_4E8F(): pass

    label("Function_41_4E8F")

    TalkBegin(0x2C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_4EDB")

    ChrTalk(
        0xFE,
        "呼，找到妹妹了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "她在学校里\x01",
            "也和基诺奇奥很要好呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F4A")

    label("loc_4EDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_4F4A")

    ChrTalk(
        0xFE,
        (
            "呼，只有在这个时候\x01",
            "才能进到学院里面看看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔，妹妹的教室在哪呢……\x01",
            "作为监护人我有应尽的义务。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F4A")

    TalkEnd(0x2C)
    Return()

    # Function_41_4E8F end

    def Function_42_4F4E(): pass

    label("Function_42_4F4E")

    TalkBegin(0x2D)

    ChrTalk(
        0xFE,
        (
            "唔唔，\x01",
            "百日战役后经济发展的相关考察……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x2D)
    Return()

    # Function_42_4F4E end

    def Function_43_4F82(): pass

    label("Function_43_4F82")

    TalkBegin(0x2E)

    ChrTalk(
        0xFE,
        (
            "啊，\x01",
            "好想在什么地方休息一下啊……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x2E)
    Return()

    # Function_43_4F82 end

    def Function_44_4FB0(): pass

    label("Function_44_4FB0")

    TalkBegin(0x2F)

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "好像都是些十分深奥的东西啊……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x2F)
    Return()

    # Function_44_4FB0 end

    def Function_45_4FE0(): pass

    label("Function_45_4FE0")

    TalkBegin(0x30)

    ChrTalk(
        0xFE,
        "虽然在学校学习是很好……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我还是想把孩子\x01",
            "培育得更加富有感情些。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x30)
    Return()

    # Function_45_4FE0 end

    def Function_46_5030(): pass

    label("Function_46_5030")

    TalkBegin(0x32)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_508F")

    ChrTalk(
        0xFE,
        (
            "母亲老是对\x01",
            "入学的事唠叨个不停。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "必须要考试合格\x01",
            "才能进来这里读书的啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50BB")

    label("loc_508F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_50BB")

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "平时就是在这里上课的吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50BB")

    TalkEnd(0x32)
    Return()

    # Function_46_5030 end

    def Function_47_50BF(): pass

    label("Function_47_50BF")

    TalkBegin(0x31)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_5114")

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "学园祭的活动好充实啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "越来越想让我的孩子\x01",
            "来这儿读书了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5171")

    label("loc_5114")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_5171")

    ChrTalk(
        0xFE,
        (
            "今天我和儿子一起来\x01",
            "侦察著名的王立学院。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他以明年的考试为目标，\x01",
            "信心很足呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5171")

    TalkEnd(0x31)
    Return()

    # Function_47_50BF end

    def Function_48_5175(): pass

    label("Function_48_5175")

    TalkBegin(0x34)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_5298")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5250")
    OP_A2(0x457)
    OP_4A(0x8, 255)

    ChrTalk(
        0x8,
        (
            "#781F戴尔蒙市长，\x01",
            "自从去年的王国会议之后我们也好久不见了。\x02\x03",
            "这段时间，你身体怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x34,
        (
            "#661F就像你看到的，结实着呢。\x01",
            "科林兹校长也很精神嘛。\x02\x03",
            "今天我打算好好放松一下。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x34, 0x10)
    OP_4B(0x8, 255)
    Jump("loc_5298")

    label("loc_5250")


    ChrTalk(
        0x34,
        (
            "#661F啊，你们也来了。\x02\x03",
            "我每年都受到王立学院的邀请来参加学园祭。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5298")

    TalkEnd(0x34)
    Return()

    # Function_48_5175 end

    def Function_49_529C(): pass

    label("Function_49_529C")

    TalkBegin(0x33)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_52ED")

    ChrTalk(
        0xFE,
        (
            "#620F刚才看到约修亚先生\x01",
            "一脸紧张地走过去……\x02\x03",
            "发生了什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5600")

    label("loc_52ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_5600")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55CA")
    OP_A2(0x453)

    ChrTalk(
        0x101,
        "#004F啊，莉拉小姐！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#621F……二位真是好久没见了。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x24, 0x10)
    TurnDirection(0x24, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x24, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_535F")
    SetChrSubChip(0x24, 2)
    Jump("loc_5390")

    label("loc_535F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x24, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5375")
    SetChrSubChip(0x24, 1)
    Jump("loc_5390")

    label("loc_5375")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x24, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_538B")
    SetChrSubChip(0x24, 0)
    Jump("loc_5390")

    label("loc_538B")

    SetChrSubChip(0x24, 2)

    label("loc_5390")

    OP_8C(0x24, 270, 0)
    SetChrFlags(0x24, 0x10)

    ChrTalk(
        0x24,
        (
            "#613F啊，这不是\x01",
            "艾丝蒂尔和约修亚吗。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x24, 0)
    TurnDirection(0x102, 0x24, 0)
    TurnDirection(0x105, 0x24, 0)

    ChrTalk(
        0x101,
        (
            "#004F啊，梅贝尔市长也在！？\x02\x03",
            "你们两位为什么会在这里呢？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#611F呵呵，\x01",
            "其实我是这个学院的毕业生。\x02\x03",
            "每年的学园祭都要来出席的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哦，是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#610F那么你们俩是为什么来这儿的啊？\x01",
            "　\x02\x03",
            "难道是为了协会的工作？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F嘿嘿，其实呢……\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔\x01",
            "向梅贝尔市长说明了事情的经过。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(
        0x24,
        (
            "#613F哦，是协助演出啊。\x02\x03",
            "#611F我也认为演出是很考功夫的。\x01",
            "　\x02\x03",
            "呵呵，连艾丝蒂尔\x01",
            "和约修亚也参加演出的话，\x01",
            "那我真要好好看看才行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F（唔，真不想让\x01",
            "　认识的人看到啊……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x24, 0)
    Jump("loc_5600")

    label("loc_55CA")


    ChrTalk(
        0xFE,
        (
            "#621F……二位真是好久没见了。\x01",
            "还是那么有精神呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5600")

    TalkEnd(0x33)
    Return()

    # Function_49_529C end

    def Function_50_5604(): pass

    label("Function_50_5604")

    TalkBegin(0x35)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_5652")

    ChrTalk(
        0xFE,
        (
            "过去的学园祭，\x01",
            "班级展示全都是研究发表……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "时代变迁啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_56AF")

    label("loc_5652")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_56AF")

    ChrTalk(
        0xFE,
        (
            "在我们的学生时代，\x01",
            "还没有这个校舍呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在这北面的古老建筑物\x01",
            "就是以前的校舍。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56AF")

    TalkEnd(0x35)
    Return()

    # Function_50_5604 end

    def Function_51_56B3(): pass

    label("Function_51_56B3")

    TalkBegin(0x36)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_5716")

    ChrTalk(
        0xFE,
        (
            "……期末考试成绩优秀者\x01",
            "……科洛丝·琳希……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎，\x01",
            "她和乔儿那孩子都好厉害……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_574A")

    label("loc_5716")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_574A")

    ChrTalk(
        0xFE,
        (
            "和主日学校相比，\x01",
            "这里的学习更专业呀……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_574A")

    TalkEnd(0x36)
    Return()

    # Function_51_56B3 end

    def Function_52_574E(): pass

    label("Function_52_574E")

    TalkBegin(0x37)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_57B1")

    ChrTalk(
        0xFE,
        (
            "下午的舞台剧\x01",
            "好像有很有趣的看点呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然我问过女儿，\x01",
            "但她没告诉我详细情况。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5801")

    label("loc_57B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_5801")

    ChrTalk(
        0xFE,
        "这里就是学院啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然女儿在这里上学，\x01",
            "不过我还是第一次来呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5801")

    TalkEnd(0x37)
    Return()

    # Function_52_574E end

    def Function_53_5805(): pass

    label("Function_53_5805")

    TalkBegin(0x38)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_5839")

    ChrTalk(
        0xFE,
        (
            "走得好累呀，\x01",
            "去茶座休息一下吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5869")

    label("loc_5839")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_5869")

    ChrTalk(
        0xFE,
        (
            "在二楼的是自然系\x01",
            "和社会系的教室……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5869")

    TalkEnd(0x38)
    Return()

    # Function_53_5805 end

    def Function_54_586D(): pass

    label("Function_54_586D")

    TalkBegin(0x39)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_58A9")

    ChrTalk(
        0xFE,
        (
            "各种展示都很有趣啊，\x01",
            "孩子们也感到很开心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58CE")

    label("loc_58A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_58CE")

    ChrTalk(
        0xFE,
        "从什么地方开始看好呢……\x02",
    )

    CloseMessageWindow()

    label("loc_58CE")

    TalkEnd(0x39)
    Return()

    # Function_54_586D end

    def Function_55_58D2(): pass

    label("Function_55_58D2")

    TalkBegin(0x3A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_592A")

    ChrTalk(
        0xFE,
        "我看了很多展示。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不仅很有趣，\x01",
            "也能从中看到学生们平时的学习成果。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_595A")

    label("loc_592A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_595A")

    ChrTalk(
        0xFE,
        (
            "真没想到这个建筑物里\x01",
            "有这么多地方。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_595A")

    TalkEnd(0x3A)
    Return()

    # Function_55_58D2 end

    def Function_56_595E(): pass

    label("Function_56_595E")

    TalkBegin(0x3B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_59B2")

    ChrTalk(
        0xFE,
        "哎呀，这个班级真让人吃惊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那些学生竟然\x01",
            "能做出那种东西来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59E0")

    label("loc_59B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_59E0")

    ChrTalk(
        0xFE,
        (
            "呵呵……\x01",
            "这里就是自然系的教室啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59E0")

    TalkEnd(0x3B)
    Return()

    # Function_56_595E end

    def Function_57_59E4(): pass

    label("Function_57_59E4")

    TalkBegin(0x3C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_5A1C")

    ChrTalk(
        0xFE,
        (
            "展示好像快要结束了，\x01",
            "要快点看完才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A44")

    label("loc_5A1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_5A44")

    ChrTalk(
        0xFE,
        (
            "今年来的人\x01",
            "好像特别多啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A44")

    TalkEnd(0x3C)
    Return()

    # Function_57_59E4 end

    def Function_58_5A48(): pass

    label("Function_58_5A48")

    TalkBegin(0x3D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_5A85")

    ChrTalk(
        0xFE,
        "一早我就在想着舞台剧了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "快点开始吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5AB5")

    label("loc_5A85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_5AB5")

    ChrTalk(
        0xFE,
        (
            "这里是学习的地方？\x01",
            "不是玩的地方啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5AB5")

    TalkEnd(0x3D)
    Return()

    # Function_58_5A48 end

    def Function_59_5AB9(): pass

    label("Function_59_5AB9")

    EventBegin(0x0)
    OP_6D(-5190, 0, 34000, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x31, 3150, 0, 31480, 90)
    SetChrPos(0x19, -5600, 0, 29020, 90)
    SetChrPos(0x25, 88600, 0, 34670, 0)
    SetChrPos(0x26, 89570, 0, 34410, 270)
    ClearChrFlags(0x29, 0x80)
    OP_4A(0x29, 255)
    SetChrPos(0x101, 2630, 0, 29470, 0)
    SetChrPos(0x102, 2510, 0, 28440, 0)
    SetChrPos(0x105, 1400, 0, 28920, 0)
    SetChrPos(0x29, 1690, 0, 30250, 0)
    FadeToBright(2000, 0)
    OP_6D(2050, 0, 29480, 4000)

    ChrTalk(
        0x29,
        (
            "#132F呀～这里就是了。\x01",
            "的确是十分正规的展览啊。\x02\x03",
            "从历史到经济，\x01",
            "各个领域的作品都有啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x29, 180, 400)

    ChrTalk(
        0x29,
        (
            "#130F哎呀，真是太好了。\x01",
            "我对这里的展览十分感兴趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#048F您太过奖了。\x02\x03",
            "我也是社会系专业的，\x01",
            "十分荣幸您会对展览感兴趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F嗯～不过我对这种复杂的东西\x01",
            "就比较头痛了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F唉，我说你啊，\x01",
            "偶尔也该对这类东西有点兴趣嘛。\x02\x03",
            "#010F因为游击士也经常\x01",
            "会用到各种各样的知识哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F哼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        (
            "#130F哈哈，\x01",
            "那么我这就开始参观了。\x02\x03",
            "真是感谢你们带我来这里。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x29, 315, 400)

    def lambda_5D83():
        OP_6D(1000, 0, 31440, 2000)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_5D83)
    OP_8E(0x29, 0xFFFFF970, 0x0, 0x8778, 0x7D0, 0x0)
    OP_8C(0x29, 0, 400)
    OP_4B(0x29, 255)
    OP_A2(0x45A)
    EventEnd(0x0)
    Return()

    # Function_59_5AB9 end

    def Function_60_5DBA(): pass

    label("Function_60_5DBA")

    EventBegin(0x0)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x34, 0x80)
    SetChrFlags(0x8, 0x80)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    SetChrPos(0x9, 41350, -250, -3330, 0)
    SetChrPos(0xA, 40790, -250, -4570, 0)
    SetChrPos(0xB, 39420, 0, -2040, 0)
    SetChrPos(0xC, 41420, -250, -2220, 0)
    SetChrPos(0xD, 40840, 0, -1870, 0)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xA, 0x40)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x101, 46630, 2000, 7580, 180)
    SetChrPos(0x102, 46550, 2000, 8570, 180)
    SetChrPos(0x105, 45690, 2000, 8960, 180)
    OP_0D()

    ChrTalk(
        0xD,
        "#1P啊，是姐姐他们！\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_5EFE():
        OP_6D(44200, 0, 1160, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5EFE)
    WaitChrThread(0x101, 0x1)

    def lambda_5F1B():
        OP_8E(0xFE, 0xB27A, 0x0, 0xEE2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5F1B)

    def lambda_5F36():
        OP_8E(0xFE, 0xA7C6, 0x0, 0x5A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5F36)
    Sleep(200)

    def lambda_5F56():
        OP_8E(0xFE, 0xABC2, 0x0, 0xFFFFFD6C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5F56)

    def lambda_5F71():
        OP_8E(0xFE, 0xA4CE, 0x0, 0x10E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5F71)
    Sleep(200)

    def lambda_5F91():
        OP_8E(0xFE, 0xA848, 0x0, 0xFFFFFD44, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5F91)
    Sleep(100)

    def lambda_5FB1():
        OP_8E(0xFE, 0xB798, 0x0, 0xBEA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5FB1)
    Sleep(500)

    def lambda_5FD1():
        OP_8E(0xFE, 0xB27A, 0x0, 0xEE2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5FD1)
    WaitChrThread(0x101, 0x1)

    def lambda_5FF1():
        OP_8E(0xFE, 0xA870, 0x0, 0x618, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5FF1)
    WaitChrThread(0x102, 0x1)

    def lambda_6011():
        OP_8E(0xFE, 0xAF28, 0x0, 0x1A4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6011)
    WaitChrThread(0x105, 0x1)

    def lambda_6031():
        OP_8E(0xFE, 0xAD02, 0x0, 0x55A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6031)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 180, 400)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 225, 400)
    WaitChrThread(0x105, 0x1)
    OP_8C(0x105, 225, 400)

    ChrTalk(
        0x105,
        (
            "#041F孩子们……\x01",
            "你们来了啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F#1P你们终于来了，小家伙们⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F#2P怎么样，玩得开心吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "嗯～！\x01",
            "很开心哦～⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "我今天吃了\x01",
            "好多好多点心呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "你就知道吃，\x01",
            "去哪儿吃到哪儿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#048F呵呵……\x01",
            "你们是和特蕾莎老师一起来的吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xA, 400)

    ChrTalk(
        0xD,
        (
            "#770F嗯，\x01",
            "她在那边和别人聊天……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xD,
        "#771F啊，来啦来啦⊙\x02",
    )

    CloseMessageWindow()

    def lambda_61C6():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_61C6)

    def lambda_61D4():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_61D4)

    def lambda_61E2():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_61E2)

    def lambda_61F0():

        label("loc_61F0")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_61F0")

    QueueWorkItem2(0x101, 2, lambda_61F0)

    def lambda_6201():

        label("loc_6201")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_6201")

    QueueWorkItem2(0x102, 2, lambda_6201)

    def lambda_6212():

        label("loc_6212")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_6212")

    QueueWorkItem2(0x105, 2, lambda_6212)
    ClearChrFlags(0xA, 0x80)
    OP_8E(0xA, 0xA410, 0x0, 0xFFFFFBB4, 0x7D0, 0x0)
    TurnDirection(0xA, 0x105, 400)
    OP_44(0x102, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)

    ChrTalk(
        0xA,
        "#750F呵呵，你们好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#1P啊，特蕾莎院长！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#048F老师……您好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#751F今天邀请我们来参加学园祭，\x01",
            "真的是感谢你啊。\x02\x03",
            "我和孩子们\x01",
            "今天真的玩得很开心。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x105, 400)

    ChrTalk(
        0xD,
        (
            "#770F对了，科洛丝姐姐。\x02\x03",
            "姐姐演的舞台剧\x01",
            "什么时候才开始啊？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_633D():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_633D)

    def lambda_634B():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_634B)

    def lambda_6359():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_6359)
    TurnDirection(0xC, 0x105, 400)

    ChrTalk(
        0xC,
        (
            "对啊对啊。\x01",
            "我们都很期待呢☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F是啊……\x01",
            "还要再等一会儿哦。\x02\x03",
            "#041F顺便说一句，不光是我，\x01",
            "艾丝蒂尔他们也会参加演出哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(
        0xB,
        (
            "真的？\x01",
            "哇，好期待呢～！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(
        0x9,
        (
            "约修亚哥哥\x01",
            "演的是什么角色啊～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#018F#2P这个……\x01",
            "该怎么说好呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F#1P啊哈哈……\x01",
            "总之你们看了一定会喜欢的㈱\x02\x03",
            "#000F对了，特蕾莎院长。\x01",
            "你们还住在玛诺利亚吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#750F是的，承蒙旅店主人的好意，\x01",
            "让我们用很便宜的价钱租了个房间。\x02\x03",
            "#757F但是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F#1P？？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#2P…………………………\x02\x03",
            "#010F好了，孩子们。\x01",
            "想去看看舞台剧的服装吗？\x02\x03",
            "有好多漂亮的\x01",
            "晚礼服和骑士装哦。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_65A3():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_65A3)

    def lambda_65B1():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_65B1)

    def lambda_65BF():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_65BF)

    def lambda_65CD():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_65CD)
    TurnDirection(0xC, 0x102, 400)

    ChrTalk(
        0xC,
        "漂亮的晚礼服！？\x02",
    )

    CloseMessageWindow()

    def lambda_65F8():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_65F8)
    TurnDirection(0xD, 0x102, 400)

    ChrTalk(
        0xD,
        "#774F骑士装！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F呵呵……\x01",
            "看来你们很有兴趣啊。\x02\x03",
            "那么哥哥就破例，\x01",
            "带你们到舞台后面参观一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "好呀！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "波利也要去～\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F（我们先到舞台休息室去，\x01",
            "　你们待会儿过来吧。）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_66D8():

        label("loc_66D8")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_66D8")

    QueueWorkItem2(0x105, 1, lambda_66D8)

    def lambda_66E9():

        label("loc_66E9")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_66E9")

    QueueWorkItem2(0x101, 1, lambda_66E9)

    def lambda_66FA():

        label("loc_66FA")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_66FA")

    QueueWorkItem2(0xA, 1, lambda_66FA)

    def lambda_670B():

        label("loc_670B")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_670B")

    QueueWorkItem2(0xD, 1, lambda_670B)

    def lambda_671C():

        label("loc_671C")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_671C")

    QueueWorkItem2(0xC, 1, lambda_671C)

    def lambda_672D():

        label("loc_672D")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_672D")

    QueueWorkItem2(0x9, 1, lambda_672D)

    def lambda_673E():

        label("loc_673E")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_673E")

    QueueWorkItem2(0xB, 1, lambda_673E)
    SetChrFlags(0x102, 0x4)
    OP_8C(0x102, 180, 400)
    OP_8E(0x102, 0xB004, 0x0, 0xFFFFFC68, 0x7D0, 0x0)
    OP_8E(0x102, 0xA8B6, 0x0, 0xFFFFF902, 0x7D0, 0x0)
    TurnDirection(0x102, 0xD, 400)

    ChrTalk(
        0x102,
        "#010F那么大家跟我来吧。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 225, 400)
    OP_8E(0x102, 0xA438, 0xFFFFFF06, 0xFFFFF5EC, 0x7D0, 0x0)
    ClearChrFlags(0x102, 0x4)

    def lambda_67C7():
        OP_8E(0xFE, 0xA438, 0xFFFFFF06, 0xFFFFEC14, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_67C7)

    def lambda_67E2():
        OP_8E(0xFE, 0xA438, 0xFFFFFF06, 0xFFFFEC14, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_67E2)
    Sleep(700)

    def lambda_6802():
        OP_8E(0xFE, 0xA622, 0xFFFFFF06, 0xFFFFF6FA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6802)
    WaitChrThread(0x102, 0x1)
    SetChrFlags(0x102, 0x80)

    def lambda_6827():
        OP_8E(0xFE, 0xA438, 0xFFFFFF06, 0xFFFFEC14, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6827)

    def lambda_6842():
        OP_8E(0xFE, 0xA438, 0xFFFFFF06, 0xFFFFEC14, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6842)
    WaitChrThread(0xC, 0x1)
    SetChrFlags(0xC, 0x80)

    def lambda_6867():
        OP_8E(0xFE, 0xA136, 0x0, 0xFFFFFCCC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6867)
    WaitChrThread(0xB, 0x1)

    def lambda_6887():
        OP_8E(0xFE, 0xA438, 0xFFFFFF06, 0xFFFFEC14, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6887)
    WaitChrThread(0x9, 0x1)
    SetChrFlags(0x9, 0x80)
    WaitChrThread(0xD, 0x1)
    SetChrFlags(0xD, 0x80)
    WaitChrThread(0xB, 0x1)
    SetChrFlags(0xB, 0x80)
    Sleep(1000)
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0xA, 0xFF)

    def lambda_68D1():
        OP_6D(42780, 0, 270, 2000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_68D1)

    def lambda_68E9():
        OP_8E(0xFE, 0xA8FC, 0x0, 0xFFFFFFBA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_68E9)
    Sleep(400)

    def lambda_6909():
        OP_8E(0xFE, 0xA474, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6909)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0xA, 400)
    WaitChrThread(0xA, 0x1)

    ChrTalk(
        0xA,
        (
            "#750F呵呵，\x01",
            "约修亚真是个敏锐的孩子呢。\x02\x03",
            "#757F其实我是有些话\x01",
            "不方便在孩子们面前说……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_698F():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_698F)
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(
        0x101,
        "#002F#1P这么说，难道……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(
        0xA,
        (
            "#754F嗯，因为已经考虑了好几天，\x01",
            "所以我还是决定接受市长的提议。\x02\x03",
            "毕竟不能再给\x01",
            "玛诺利亚的村民们添麻烦了。\x02\x03",
            "#750F今天的学园祭结束之后，\x01",
            "我就会告诉孩子们这件事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#049F#2P这样……啊……\x02\x03",
            "虽然以后会很寂寞……\x01",
            "但我尊重老师您的决定……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#751F呵呵，别这么没精打采嘛。\x02\x03",
            "虽说要搬到王都，\x01",
            "但坐定期船的话一下子就到了。\x02\x03",
            "#750F而且我打算\x01",
            "到了王都之后去找份工作。\x02\x03",
            "我会慢慢地赚钱，\x01",
            "总有一天孤儿院能再重建的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F#1P特蕾莎院长……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#049F#2P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#751F好了……\x01",
            "你们不去找那些孩子吗？\x02\x03",
            "怎么说也不能把孩子们\x01",
            "全扔给约修亚一个人管啊。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T2523   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_60_5DBA end

    def Function_61_6C0B(): pass

    label("Function_61_6C0B")

    OP_22(0x11, 0x0, 0x64)
    SetChrFlags(0x3E, 0x80)
    OP_64(0x1, 0x1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "卢安经济史·中\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x33E, 1)
    OP_28(0x27, 0x1, 0x80)
    TalkEnd(0xFF)
    Return()

    # Function_61_6C0B end

    def Function_62_6C71(): pass

    label("Function_62_6C71")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　　前面是校长室和办公室　　　　\x01",
            "※谢绝外来人员进入。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_62_6C71 end

    def Function_63_6CDB(): pass

    label("Function_63_6CDB")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "人文系模拟店铺\x01",
            "茶座『芳塔娜』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_63_6CDB end

    def Function_64_6D2B(): pass

    label("Function_64_6D2B")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　走　\x01",
            "　　廊　\x01",
            "　　里　\x01",
            "　　请　\x01",
            "　　保　\x01",
            "　学持　\x01",
            "　生安　\x01",
            "　指静　\x01",
            "　导！　\x01",
            "　部　　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_64_6D2B end

    def Function_65_6DB7(): pass

    label("Function_65_6DB7")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "自然系成果展示\x01",
            "『结晶回路与导力技术』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_65_6DB7 end

    def Function_66_6E0F(): pass

    label("Function_66_6E0F")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　社会系成果展示\x01",
            "『卢安地区的历史与经济』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_66_6E0F end

    def Function_67_6E6D(): pass

    label("Function_67_6E6D")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "欢迎光临！\x01",
            "这里是茶座『芳塔娜』！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_67_6E6D end

    def Function_68_6EC1(): pass

    label("Function_68_6EC1")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这里分析了导力器产业的发展动向。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_68_6EC1 end

    def Function_69_6F14(): pass

    label("Function_69_6F14")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这里用图表展示了每年观光客数量的变化。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_69_6F14 end

    def Function_70_6F6D(): pass

    label("Function_70_6F6D")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这里整理了国内主要产品的出口方向。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_70_6F6D end

    def Function_71_6FC2(): pass

    label("Function_71_6FC2")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这里归纳了人口移动的情况。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_71_6FC2 end

    def Function_72_700F(): pass

    label("Function_72_700F")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　《导力演算器的存储装置》　　\x01",
            "※这个展示品是从\x01",
            "　蔡斯的中央工房借来的。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_72_700F end

    def Function_73_708C(): pass

    label("Function_73_708C")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "《导力相性占卜机》\x01",
            "　 ※好评工作中！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_73_708C end

    def Function_74_70E3(): pass

    label("Function_74_70E3")

    EventBegin(0x0)
    Fade(1000)

    def lambda_70F0():
        OP_6D(84960, 1650, 32920, 1000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_70F0)

    def lambda_7108():
        OP_67(0, 1300, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_7108)

    def lambda_7120():
        OP_6B(1400, 1000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_7120)

    def lambda_7130():
        OP_6C(0, 1000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_7130)

    def lambda_7140():
        OP_6E(262, 1000)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_7140)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_7168")
    Jump("loc_71B5")

    label("loc_7168")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_7172")
    Jump("loc_71B5")

    label("loc_7172")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_719A")
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x33, 0x80)
    SetChrFlags(0x2C, 0x80)
    Jump("loc_71B5")

    label("loc_719A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_71B5")
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)

    label("loc_71B5")

    Sleep(1000)
    Sleep(500)
    OP_22(0x9D, 0x0, 0x64)
    Fade(500)
    OP_74(0x6, 0x0, 0x1)
    OP_0D()
    Sleep(500)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "导力相性占卜机\x01",
            "Version:1.0014.4082\x01",
            "(C)Genis Royal School 1202\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 290, 56, 3)
    SetChrName("占卜机")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "想要占卜一下吗？\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7257")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_82FB")
    SetMessageWindowPos(72, 290, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x1)
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_72AE"),
        (1, "loc_72B1"),
        (SWITCH_DEFAULT, "loc_72BE"),
    )


    label("loc_72AE")

    Jump("loc_72CB")

    label("loc_72B1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7257")

    label("loc_72BE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7257")

    label("loc_72CB")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "要输入谁的资料呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        55,
        80,
        0,
        (
            "【艾丝蒂尔】\x01",      # 0
            "【约修亚】\x01",        # 1
            "【雪拉扎德】\x01",      # 2
            "【奥利维尔】\x01",      # 3
            "【科洛丝】\x01",        # 4
            "【奈尔】\x01",          # 5
            "【朵洛希】\x01",        # 6
        )
    )

    MenuEnd(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_7378"),
        (1, "loc_73C0"),
        (2, "loc_740A"),
        (3, "loc_7454"),
        (4, "loc_749E"),
        (5, "loc_74E6"),
        (6, "loc_752C"),
        (SWITCH_DEFAULT, "loc_7574"),
    )


    label("loc_7378")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【艾丝蒂尔·布莱特】\x01",
            "七耀历１１８６年８月７日出生……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7574")

    label("loc_73C0")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【约修亚·布莱特】\x01",
            "七耀历１１８５年１２月２０日出生……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7574")

    label("loc_740A")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【雪拉扎德·哈维】\x01",
            "七耀历１１７９年５月１４日生出生……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7574")

    label("loc_7454")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【奥利维尔·朗海姆】\x01",
            "七耀历１１７７年４月１日生出生……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7574")

    label("loc_749E")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【科洛丝·琳希】\x01",
            "七耀历１１８６年１０月１１日出生……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7574")

    label("loc_74E6")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【奈尔·班兹】\x01",
            "七耀历１１７２年１１月２５日出生……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7574")

    label("loc_752C")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【朵洛希·海娅特】\x01",
            "七耀历１１８２年１月２２日出生……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7574")

    label("loc_7574")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "接下来请输入\x01",
            "对方的资料。\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        426,
        80,
        0,
        (
            "【艾丝蒂尔】\x01",      # 0
            "【约修亚】\x01",        # 1
            "【雪拉扎德】\x01",      # 2
            "【奥利维尔】\x01",      # 3
            "【科洛丝】\x01",        # 4
            "【奈尔】\x01",          # 5
            "【朵洛希】\x01",        # 6
        )
    )

    MenuEnd(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_7628"),
        (1, "loc_7670"),
        (2, "loc_76BA"),
        (3, "loc_7704"),
        (4, "loc_774E"),
        (5, "loc_7796"),
        (6, "loc_77DC"),
        (SWITCH_DEFAULT, "loc_7824"),
    )


    label("loc_7628")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【艾丝蒂尔·布莱特】\x01",
            "七耀历１１８６年８月７日出生……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_7824")

    label("loc_7670")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【约修亚·布莱特】\x01",
            "七耀历１１８５年１２月２０日出生……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_7824")

    label("loc_76BA")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【雪拉扎德·哈维】\x01",
            "七耀历１１７９年５月１４日生出生……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_7824")

    label("loc_7704")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【奥利维尔·朗海姆】\x01",
            "七耀历１１７７年４月１日生出生……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_7824")

    label("loc_774E")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【科洛丝·琳希】\x01",
            "七耀历１１８６年１０月１１日出生……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_7824")

    label("loc_7796")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【奈尔·班兹】\x01",
            "七耀历１１７２年１１月２５日出生……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_7824")

    label("loc_77DC")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "【朵洛希·海娅特】\x01",
            "七耀历１１８２年１月２２日出生……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_7824")

    label("loc_7824")

    SetChrName("占卜机")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "那么，占卜现在开始。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x27, 0x0, 0x64)
    OP_75(0x6, 0x0, 0x0)
    Sleep(50)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x1)
    Sleep(60)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x2)
    Sleep(70)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x3)
    Sleep(80)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x4)
    Sleep(90)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x5)
    Sleep(100)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x6)
    Sleep(110)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x7)
    Sleep(120)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x1)
    Sleep(130)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x2)
    Sleep(140)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x3)
    Sleep(150)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x4)
    Sleep(160)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x5)
    Sleep(170)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x6)
    Sleep(180)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x7)
    Sleep(190)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x1)
    Sleep(200)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x2)
    Sleep(210)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x3)
    Sleep(220)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x4)
    Sleep(230)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x5)
    Sleep(240)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x6)
    Sleep(250)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x7)
    Sleep(260)
    SetChrName("占卜机")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (4, "loc_7ABD"),
        (40, "loc_7ABD"),
        (12, "loc_7ABD"),
        (21, "loc_7ABD"),
        (24, "loc_7ABD"),
        (42, "loc_7ABD"),
        (36, "loc_7ABD"),
        (63, "loc_7ABD"),
        (5, "loc_7BE8"),
        (50, "loc_7BE8"),
        (14, "loc_7BE8"),
        (41, "loc_7BE8"),
        (26, "loc_7BE8"),
        (62, "loc_7BE8"),
        (2, "loc_7D06"),
        (20, "loc_7D06"),
        (6, "loc_7D06"),
        (60, "loc_7D06"),
        (15, "loc_7D06"),
        (51, "loc_7D06"),
        (1, "loc_7E26"),
        (10, "loc_7E26"),
        (13, "loc_7E26"),
        (31, "loc_7E26"),
        (25, "loc_7E26"),
        (52, "loc_7E26"),
        (46, "loc_7E26"),
        (64, "loc_7E26"),
        (16, "loc_7F35"),
        (61, "loc_7F35"),
        (23, "loc_7F35"),
        (32, "loc_7F35"),
        (34, "loc_7F35"),
        (43, "loc_7F35"),
        (56, "loc_7F35"),
        (65, "loc_7F35"),
        (3, "loc_806E"),
        (30, "loc_806E"),
        (35, "loc_806E"),
        (53, "loc_806E"),
        (45, "loc_806E"),
        (54, "loc_806E"),
        (0, "loc_8186"),
        (11, "loc_8186"),
        (22, "loc_8186"),
        (33, "loc_8186"),
        (44, "loc_8186"),
        (55, "loc_8186"),
        (66, "loc_8186"),
        (SWITCH_DEFAULT, "loc_82C4"),
    )


    label("loc_7ABD")

    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x3)
    Sleep(250)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x6)
    Sleep(1000)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "今天是你们\x01",
            "彼此都很主动的一天。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "要主动采取行动，\x01",
            "这样两人应该能度过快乐的一天。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "谈话很容易投机，\x01",
            "只要能够两人独处，\x01",
            "很快就能得到对方的心。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "如果被邀请的话，\x01",
            "不要犹豫，马上接受。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有共同兴趣和目的的情况下，\x01",
            "两人的关系会发展得十分顺利。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_82C4")

    label("loc_7BE8")

    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x4)
    Sleep(250)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x7)
    Sleep(1000)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "今天两人的意识很协调，\x01",
            "能度过开心的一天。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在两人中的一个遇到麻烦的情况下，\x01",
            "不要嫌麻烦，马上帮助对方。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有共同意识的情况下，\x01",
            "能知道对方隐蔽的一面，\x01",
            "两人的友情也会进一步加深。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "今天两人会有爱情\x01",
            "或注意到对方是特别的朋友这种意识。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_82C4")

    label("loc_7D06")

    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x1)
    Sleep(250)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x5)
    Sleep(1000)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "今天两人会对\x01",
            "事物的看法非常乐观。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "即使各自的主张\x01",
            "有出入也没有关系，\x01",
            "很快就能安稳度过的。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "平时可能有一方会\x01",
            "将自己的意见强加于对方，\x01",
            "使关系变得紧张……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "不过在这一天\x01",
            "两人的情绪会非常安定。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "平时不能说的话，\x01",
            "今天就有机会说了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_82C4")

    label("loc_7E26")

    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x7)
    Sleep(250)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x2)
    Sleep(1000)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "今天两人非常主动。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "如果有两人都想做的事，\x01",
            "一起来做是个\x01",
            "绝好的机会。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "不过，不要太过\x01",
            "把自己的意见强加于对方，\x01",
            "这一点必须要注意。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "尊重对方的步调，\x01",
            "关系会有快速进展的机会。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "总之首先考虑\x01",
            "对方的心情是最重要的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_82C4")

    label("loc_7F35")

    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x7)
    Sleep(250)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x4)
    Sleep(1000)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "今天两人就算在一起，\x01",
            "无论到哪儿都会是不顺利的一天。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "隐藏的秘密会暴露，\x01",
            "如果欺骗对方的话，\x01",
            "会让对方感到不可信任。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "找不到共同的话题，\x01",
            "谈话也总是不投机。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这样的日子还是不要硬靠近，\x01",
            "下决心做其他的事吧。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "留出距离和时间，\x01",
            "应该能再确认一下对方的重要性。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_82C4")

    label("loc_806E")

    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x6)
    Sleep(250)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x3)
    Sleep(1000)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "今天两人会\x01",
            "对某事都不做出让步，\x01",
            "可能会导致吵架。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "吵架拖太长的话，\x01",
            "可能会发展到非本意的离别。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这样的日子最好\x01",
            "不要两人单独相处，\x01",
            "应该和共同的朋友一起行动。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "如果对方说了什么不好的话，\x01",
            "不要太过在意，\x01",
            "要用自己宽容的心去听。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_82C4")

    label("loc_8186")

    OP_74(0x6, 0x0, 0x0)
    OP_22(0xEC, 0x0, 0x64)
    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    OP_22(0xF7, 0x0, 0x64)
    OP_20(0x0)
    FadeToDark(500, 0, -1)
    OP_5F(0x1)
    OP_5F(0x0)
    OP_56(0x0)
    OP_0D()
    Sleep(500)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "4 Error(s)...  0 Warning(s)...\x01",
            "导力相性占卜机...强制中止\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "导力相性占卜机\x01",
            "Version:1.0014.4082\x01",
            "(C)Genis Royal School 1202\x01",
            "#200W　#20W\x01",
            "MEMORY_CHECK#100W..........#20WOK!\x01",
            "#200W　#20W\x01",
            "重启动\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 290, 56, 3)
    SetChrName("占卜机")
    OP_56(0x0)
    FadeToBright(500, 0)
    OP_1E()
    OP_22(0x9D, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x1)
    OP_0D()
    Jump("loc_82C4")

    label("loc_82C4")

    SetMessageWindowPos(72, 290, 56, 3)
    OP_5F(0x1)
    OP_5F(0x0)
    OP_74(0x6, 0x0, 0x1)
    SetChrName("占卜机")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "要继续占卜吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7257")

    label("loc_82FB")

    SetMessageWindowPos(72, 320, 56, 3)
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Fade(1000)
    OP_74(0x6, 0x0, 0x0)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_833E")
    Jump("loc_838B")

    label("loc_833E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_8348")
    Jump("loc_838B")

    label("loc_8348")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_8370")
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x2C, 0x80)
    Jump("loc_838B")

    label("loc_8370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_838B")
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)

    label("loc_838B")

    EventEnd(0x1)
    Return()

    # Function_74_70E3 end

    def Function_75_838E(): pass

    label("Function_75_838E")

    SetPlaceName(0x6F) # 主楼　社会系教室
    Return()

    # Function_75_838E end

    def Function_76_8392(): pass

    label("Function_76_8392")

    SetPlaceName(0x5E) # 主楼　社会系教室
    Return()

    # Function_76_8392 end

    def Function_77_8396(): pass

    label("Function_77_8396")

    SetPlaceName(0x6E) # 主楼　社会系教室
    Return()

    # Function_77_8396 end

    def Function_78_839A(): pass

    label("Function_78_839A")

    SetPlaceName(0x74) # 主楼　社会系教室
    Return()

    # Function_78_839A end

    def Function_79_839E(): pass

    label("Function_79_839E")

    SetPlaceName(0x73) # 主楼　社会系教室
    Return()

    # Function_79_839E end

    SaveToFile()

Try(main)
