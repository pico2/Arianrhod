from ScenarioHelper import *

def main():
    CreateScenaFile(
        "e9990.bin",                # FileName
        "e4600",                    # MapName
        "e4600",                    # Location
        0x0000,                     # MapIndex
        "ed70000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e4600",                  # 0
        "小丑肯帕雷拉",           # 1
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(188, 0)                                        # 0

    ScpFunction((
        "Function_0_BC",           # 00, 0
        "Function_1_CC",           # 01, 1
        "Function_2_CD",           # 02, 2
    ))


    def Function_0_BC(): pass

    label("Function_0_BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_CB")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)
    Return()

    label("loc_CB")

    OP_72(0x1, 0x1000)
    OP_76(0x1, "piller", 0x2, "loop")
    OP_76(0x1, "model4", 0x2, "loop")
    OP_72(6, 0x4)
    OP_72(7, 0x4)

    Return()

    # Function_0_BC end

    def Function_1_CC(): pass

    label("Function_1_CC")

    Return()

    # Function_1_CC end

    def Function_2_CD(): pass

    label("Function_2_CD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03600.itc", 0x1E)
    LoadEffect(0x0, "event/ev14000.eff")
    SoundLoad(3885)
    SoundLoad(3886)
    SoundLoad(969)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 0, -3000, 0)
    OP_72(0x1, 0x1000)
    OP_76(0x1, "piller", 0x2, "loop")
    OP_76(0x1, "model4", 0x2, "loop")
    OP_72(0x6, 0x1000)
    OP_76(0x6, "piller", 0x2, "loop")
    OP_76(0x6, "model4", 0x2, "loop")
    OP_72(0x7, 0x4)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_F3(0x186A0)
    Sleep(1000)
    OP_5B(0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF)
    SetChrName("声音")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "#30W原来如此，\x01",
            "看来进展得很顺利呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayBGM("ed70580", 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 3800, 12000, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, -10000, 3800, -8000, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    OP_68(-330, 2000, -1650, 0)
    OP_6D(0x130, 0x1D, 0x0, 0x0)
    OP_6E(0x320, 0x0)
    OP_6C(0x7530, 0x0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_6C(0x4650, 0x1388)
    FadeToBright(1500, 0)
    OP_0D()
    OP_6F(0x79)
    CancelBlur(1000)
    Fade(500)
    OP_68(0, 7250, 0, 0)
    OP_6D(0x0, 0xFFF6, 0x0, 0x0)
    OP_6E(0x320, 0x0)
    OP_6C(0x79AE, 0x0)
    OP_68(0, 10900, 0, 0)
    OP_6D(0x166, 0xFFF7, 0x0, 0x0)
    OP_6E(0x320, 0x0)
    OP_6C(0x5EF6, 0x0)
    OP_68(0, 7250, 0, 8000)
    OP_6D(0x0, 0xFFFB, 0x0, 0x1F40)
    OP_6E(0x320, 0x1F40)
    OP_6C(0x4EB6, 0x1F40)
    PlaceName2(0x154, 0xC8, "c_plac64", 0x0, 0x7D0)
    OP_6F(0x79)
    Fade(500)
    OP_93(0x8, 0x13B, 0x0)
    OP_68(-5610, 2000, -2300, 0)
    OP_6D(0x8, 0x4, 0x0, 0x0)
    OP_6E(0x320, 0x0)
    OP_6C(0x4C90, 0x0)
    OP_6D(0x167, 0x4, 0x0, 0x7530)
    OP_0D()
    Sleep(500)
    OP_5B(0x3, 0x78, 0xFFFF, 0xFFFF)
    SetChrName("第六柱")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "嗯，我这边的准备工作\x01",
            "也已经完成九成了。\x02\x03",
            "总算是可以如期\x01",
            "完成这次的订单。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5B(0x12C, 0x64, 0xFFFF, 0xFFFF)
    SetChrName("第一柱")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "辛苦了，博士。\x02\x03",
            "肯帕雷拉，\x01",
            "各位『执行者』的动向如何？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    ChrTalk(
        0x8,
        (
            "#04804F#12P布卢布兰在不久前\x01",
            "玩了些游戏，\x01",
            "但似乎已经收手了。\x02\x03",
            "#04800F玲已经前往利贝尔，\x01",
            "好像并没有回来的意向。\x02\x03",
            "#04806F至于『她』……\x01",
            "算啦，继续看看她的意思再说吧。\x02\x03",
            "#04802F她虽然将式神借给了我，\x01",
            "但这次好像完全\x01",
            "不打算介入呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_5B(0x12C, 0x64, 0xFFFF, 0xFFFF)
    SetChrName("第一柱")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "嗯，我知道了。\x02\x03",
            "和约鲁古大师一样，\x01",
            "凡事都让他们自行决定即可。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5B(0x3, 0x78, 0xFFFF, 0xFFFF)
    SetChrName("第六柱")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "话说回来，竟然赋予『执行者』\x01",
            "完全的行动自由权……\x02\x03",
            "虽说是那位大人的决定，\x01",
            "但这条规章真是有些没道理呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5B(0x12C, 0x64, 0xFFFF, 0xFFFF)
    SetChrName("第一柱")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "我们要遵循『盟主』的全部意愿……\x01",
            "没有质疑对错的必要。\x02\x03",
            "先不说这些了——\x01",
            "她好像来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5B(0x3, 0x78, 0xFFFF, 0xFFFF)
    SetChrName("第六柱")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "呀，来了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_93(0x8, 0x87, 0x1F4)

    ChrTalk(
        0x8,
        "#04809F#5P呵呵，真准时呢。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(10000, -1000, -8000, 0)
    OP_6D(0x64, 0x50, 0x0, 0x0)
    OP_6E(0x320, 0x0)
    OP_6C(0x3A98, 0x0)
    OP_68(10000, 2500, -8000, 5000)
    OP_6D(0x61, 0xC, 0x0, 0x1388)
    OP_6E(0x320, 0x1388)
    OP_6C(0x4650, 0x1388)
    Sound(969, 2, 100, 0)
    OP_73(0x7, 0x4)
    OP_72(0x7, 0x1000)
    OP_76(0x7, "piller", 0x2, "up")
    OP_76(0x7, "model4", 0x2, "up")
    Sleep(5000)
    StopSound(969, 1000, 100)
    Sleep(1000)
    Sound(970, 0, 100, 0)
    OP_76(0x7, "piller", 0x2, "open")
    OP_76(0x7, "model4", 0x2, "open")
    OP_6C(0x3E80, 0x3E8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(300)
    OP_76(0x7, "model4", 0x2, "loop")
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 10000, 3800, -8000, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sleep(500)
    OP_6F(0x79)
    CancelBlur(1000)
    OP_C9(0x0, 0x80000000)
    OP_5B(0xEB, 0x82, 0xFFFF, 0xFFFF)
    SetChrName("第七柱")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "#3885V#40W让各位久等了。\x02\x03",
            "#3886V会谈好像已经开始了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF2E)
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    OP_5B(0x0, 0x64, 0xFFFF, 0xFFFF)
    SetChrName("第一柱")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "哪里，刚刚开始而已。\x02\x03",
            "那件事情已经\x01",
            "办妥了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xFA, 0x82, 0xFFFF, 0xFFFF)
    SetChrName("第七柱")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "嗯，后面的事情就\x01",
            "全部交给『破戒』大人了。\x02\x03",
            "说起来，\x01",
            "『克洛斯贝尔』……\x02\x03",
            "我也已经很久没有\x01",
            "去过此地了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#04804F#6P#N呵呵，你说不定会被那翻天覆地的变化\x01",
            "震惊到目瞪口呆哦。\x02\x03",
            "#04800F那里可是现代导力文明\x01",
            "最为发达的大都市呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0x82, 0xAA, 0xFFFF, 0xFFFF)
    SetChrName("第六柱")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "在彻底完工之前，\x01",
            "我准备再去那里露一面。\x02\x03",
            "如何？机会难得，\x01",
            "不如就在那边会合吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xFA, 0x82, 0xFFFF, 0xFFFF)
    SetChrName("第七柱")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "嗯，我没有异议。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_93(0x8, 0x0, 0x0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(310, 5500, -5790, 0)
    OP_6D(0x167, 0xFFFB, 0x0, 0x0)
    OP_6E(0x320, 0x0)
    OP_6C(0x6784, 0x0)
    OP_6C(0x639C, 0x5DC)
    OP_6F(0x79)
    CancelBlur(1000)
    OP_6C(0x5BCC, 0xC350)
    OP_5B(0xFFFF, 0x78, 0xFFFF, 0xFFFF)
    SetChrName("第一柱")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "那么，二位，\x01",
            "接下来的任务就全部交给你们了。\x02\x03",
            "『幻焰计划』……\x01",
            "为了实现那位大人的最终计划，\x01",
            "这是必不可少的一个环节。\x02\x03",
            "第一阶段的工作\x01",
            "就拜托二位了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5B(0x0, 0xAA, 0xFFFF, 0xFFFF)
    SetChrName("第六柱")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "呵呵，明白了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5B(0x12C, 0xAA, 0xFFFF, 0xFFFF)
    SetChrName("第七柱")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "一切都遵从『盟主』的意志。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)
    OP_6C(0x5BCC, 0x9C4)
    FadeToDark(2500, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_21(0x1388)
    WaitBGM()
    SetScenarioFlags(0x22, 2)
    NewScene("c1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_CD end

    SaveToFile()

TryInvoke(main)
