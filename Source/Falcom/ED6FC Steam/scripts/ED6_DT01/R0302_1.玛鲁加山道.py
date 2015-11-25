from ED6ScenarioHelper import *

def main():
    # 玛鲁加山道

    CreateScenaFile(
        FileName            = 'R0302_1 ._SN',
        MapName             = 'rolent',
        Location            = 'R0302.x',
        MapIndex            = 21,
        MapDefaultBGM       = "ed60022",
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

    ScpFunction(
        "Function_0_66",           # 00, 0
        "Function_1_396",          # 01, 1
        "Function_2_FA3",          # 02, 2
        "Function_3_FEB",          # 03, 3
        "Function_4_1033",         # 04, 4
        "Function_5_107B",         # 05, 5
        "Function_6_10AE",         # 06, 6
    )


    def Function_0_66(): pass

    label("Function_0_66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_395")
    SetMapFlags(0x8000000)
    EventBegin(0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_166")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_116")
    TurnDirection(0x102, 0x101, 0)

    ChrTalk(
        0x102,
        (
            "#014F艾丝蒂尔，\x01",
            "那边是玛鲁加矿山啊。\x02\x03",
            "#014F我们先去佛莱迪先生那里汇报一下吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 0)

    ChrTalk(
        0x101,
        "#000F啊，说得没错。\x02",
    )

    CloseMessageWindow()
    Jump("loc_163")

    label("loc_116")


    ChrTalk(
        0x102,
        (
            "#010F这边是玛鲁加矿山啊……\x02\x03",
            "#010F还是先回佛莱迪先生那里汇报一下吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_163")

    Jump("loc_372")

    label("loc_166")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A0")
    OP_A2(0x5)
    TurnDirection(0x102, 0x101, 0)

    ChrTalk(
        0x102,
        (
            "#014F艾丝蒂尔，\x01",
            "那边是玛鲁加矿山啊。\x02\x03",
            "#014F我觉得还是应该先去西边的米尔西街道\x01",
            "把导力灯的更换工作做完比较好吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F难道……你已经忘了？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 0)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#008F真、真讨厌，约修亚。\x02\x03",
            "我怎么可能把委托给忘了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F……这样就好。\x02",
    )

    CloseMessageWindow()
    Jump("loc_309")

    label("loc_2A0")

    TurnDirection(0x102, 0x101, 0)

    ChrTalk(
        0x102,
        (
            "#014F这边是玛鲁加矿山。\x02\x03",
            "#014F还是应该先去西边的米尔西街道\x01",
            "把导力灯的更换工作做完比较好。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_309")

    Jump("loc_372")

    label("loc_30C")


    ChrTalk(
        0x102,
        (
            "#010F这边是玛鲁加矿山啊……\x02\x03",
            "#010F还是应该先去西边的米尔西街道\x01",
            "把导力灯的更换工作做完比较好。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_372")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    ClearMapFlags(0x8000000)
    Jump("loc_395")

    label("loc_395")

    Return()

    # Function_0_66 end

    def Function_1_396(): pass

    label("Function_1_396")

    SetMapFlags(0x8000000)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -113140, 5930, 66530, 208)
    SetChrPos(0x102, -113990, 5950, 67470, 179)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F4")
    SetChrPos(0x2, -112370, 5890, 67560, 236)
    SetChrPos(0x3, -112920, 5990, 68310, 224)

    label("loc_3F4")

    OP_6D(-112920, 5990, 68310, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(800)

    ChrTalk(
        0x101,
        "#004F啊！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)

    ChrTalk(
        0x102,
        (
            "#014F怎么了？\x01",
            "突然叫那么大声。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#502F哼哼哼哼，找到了。\x02\x03",
            "#001F真有成就感呢～⊙\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x384, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "荧光菇\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TurnDirection(0x102, 0x101, 400)
    LoadEffect(0x0, "map\\\\evsepith.eff")
    PlayEffect(0x0, 0x0, 0x101, 0, 1000, 250, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sleep(800)

    ChrTalk(
        0x102,
        "#014F啊，这个蘑菇。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#508F怎么样？就是它没错了吧？\x02\x03",
            "生长在这样的地方，\x01",
            "还依稀发出淡绿色的光～\x02\x03",
            "#001F肯定就是刚才\x01",
            "那个什么大叔说的『荧光菇』！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F委托人叫奥维德。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，对，奥维德先生。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    ChrTalk(
        0x101,
        (
            "#000F虽然感觉有点怪怪的，\x01",
            "不过还真是漂亮的蘑菇呢～\x02\x03",
            "#000F和七耀石一样的光芒。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6CF")
    TurnDirection(0x110, 0x101, 400)

    ChrTalk(
        0x110,
        (
            "#151F嗯嗯～真的呢～\x01",
            "看起来就是那种光呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CF")

    Sleep(400)

    ChrTalk(
        0x102,
        "#014F……七耀石？\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    TurnDirection(0x101, 0x102, 400)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#501F嗯？\x01",
            "怎么了，约修亚？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F也许是我有些多虑了，艾丝蒂尔，\x01",
            "快把那个蘑菇放进包里去。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_8C(0x101, 180, 400)

    ChrTalk(
        0x101,
        "#004F……啊！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_81F")
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_8C(0x102, 180, 400)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x110, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_80D():
        OP_8C(0x10F, 180, 400)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_80D)
    OP_8C(0x110, 180, 400)
    Jump("loc_83D")

    label("loc_81F")

    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_8C(0x102, 180, 400)

    label("loc_83D")

    Sleep(400)
    Fade(1000)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, -113010, 5920, 53930, 130)
    SetChrPos(0x9, -113010, 5920, 53930, 130)
    SetChrPos(0xA, -113010, 5920, 53930, 130)
    SetChrChipByIndex(0x8, 1)
    SetChrChipByIndex(0x9, 1)
    SetChrChipByIndex(0xA, 1)
    OP_6B(3300, 0)
    OP_6D(-115560, 6020, 58870, 0)
    OP_6C(270000, 0)
    OP_8C(0x101, 225, 0)
    OP_8C(0x102, 225, 0)
    OP_82(0x0, 0x0)
    OP_84(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8EA")
    OP_8C(0x2, 225, 0)
    OP_8C(0x3, 225, 0)

    label("loc_8EA")


    def lambda_8F0():
        OP_6D(-114970, 6000, 64120, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_8F0)

    def lambda_908():
        OP_6C(315000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_908)
    OP_0D()

    def lambda_919():
        OP_97(0x8, 0xFFFE4B8E, 0xF172, 0x124F8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_919)

    def lambda_935():

        label("loc_935")

        TurnDirection(0x8, 0x101, 0)
        OP_48()
        Jump("loc_935")

    QueueWorkItem2(0x8, 2, lambda_935)
    Sleep(400)

    def lambda_94B():
        OP_97(0x9, 0xFFFE4B8E, 0xF172, 0xFDE8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_94B)

    def lambda_967():

        label("loc_967")

        TurnDirection(0x9, 0x101, 0)
        OP_48()
        Jump("loc_967")

    QueueWorkItem2(0x9, 2, lambda_967)
    Sleep(400)

    def lambda_97D():
        OP_97(0xA, 0xFFFE4B8E, 0xF172, 0xD6D8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_97D)

    def lambda_999():

        label("loc_999")

        TurnDirection(0xA, 0x101, 0)
        OP_48()
        Jump("loc_999")

    QueueWorkItem2(0xA, 2, lambda_999)
    WaitChrThread(0xA, 0x1)
    OP_43(0xA, 0x0, 0x0, 0x2)
    SetChrChipByIndex(0xA, 0)
    WaitChrThread(0x8, 0x1)
    OP_43(0x8, 0x0, 0x0, 0x2)
    SetChrChipByIndex(0x8, 0)
    Sleep(100)
    OP_43(0x9, 0x0, 0x0, 0x2)
    SetChrChipByIndex(0x9, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#012F果然不出所料。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F难道是这个蘑菇引来的？！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x102, 3)
    TurnDirection(0x102, 0x8, 0)

    ChrTalk(
        0x102,
        "#016F艾丝蒂尔，迎战！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 2)
    TurnDirection(0x101, 0x8, 0)

    def lambda_A51():

        label("loc_A51")

        TurnDirection(0x101, 0x8, 0)
        OP_48()
        Jump("loc_A51")

    QueueWorkItem2(0x101, 1, lambda_A51)

    def lambda_A62():

        label("loc_A62")

        TurnDirection(0x102, 0x8, 0)
        OP_48()
        Jump("loc_A62")

    QueueWorkItem2(0x102, 1, lambda_A62)
    OP_44(0xA, 0x0)
    OP_44(0x9, 0x0)
    OP_44(0x8, 0x0)

    def lambda_A7F():
        OP_6D(-113290, 5960, 66180, 2000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_A7F)

    def lambda_A97():
        OP_6B(2800, 2000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_A97)
    SetChrChipByIndex(0x8, 1)

    def lambda_AAC():
        OP_97(0x8, 0xFFFE340A, 0x10234, 0xFFFE7960, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_AAC)
    Sleep(100)
    SetChrChipByIndex(0x9, 1)

    def lambda_AD2():
        OP_97(0x9, 0xFFFE340A, 0x10234, 0xFFFEC780, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_AD2)
    Sleep(100)
    SetChrChipByIndex(0xA, 1)

    def lambda_AF8():
        OP_97(0xA, 0xFFFE340A, 0x10234, 0xFFFF15A0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_AF8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B76")
    OP_62(0x10F, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x110, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_B46():
        OP_8E(0x10F, 0xFFFE408A, 0x1748, 0x10AB8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_B46)

    def lambda_B61():
        OP_8E(0x110, 0xFFFE3BEE, 0x1752, 0x10A2C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x110, 1, lambda_B61)

    label("loc_B76")

    WaitChrThread(0x8, 0x1)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BA5")
    OP_44(0x2, 0xFF)
    OP_44(0x3, 0xFF)

    label("loc_BA5")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x3EA, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_BC7"),
        (SWITCH_DEFAULT, "loc_BCA"),
    )


    label("loc_BC7")

    OP_B4(0x0)
    Return()

    label("loc_BCA")

    EventBegin(0x0)
    SetChrPos(0x101, -113140, 5930, 66530, 208)
    SetChrPos(0x102, -113990, 5950, 67470, 179)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C1E")
    SetChrPos(0x2, -112370, 5890, 67560, 236)
    SetChrPos(0x3, -112920, 5990, 68310, 224)

    label("loc_C1E")

    OP_6D(-112920, 5990, 68310, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    OP_64(0x1, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C70")
    OP_8C(0x2, 180, 0)
    OP_8C(0x3, 180, 0)

    label("loc_C70")

    OP_0D()
    OP_28(0x5, 0x1, 0x2)

    ChrTalk(
        0x101,
        "#007F呼～吓我一跳。\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x102, 65535)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#012F那个荧光菇还完好吧？\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#006F嗯，还是好的。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DC6")
    TurnDirection(0x10F, 0x102, 400)

    ChrTalk(
        0x10F,
        (
            "#143F怎、怎么回事啊刚才。\x02\x03",
            "为什么会突然有魔兽袭击过来呢？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x10F, 400)

    ChrTalk(
        0x102,
        (
            "#012F七耀石的原石发出的光可以吸引魔兽……\x01",
            "　\x02\x03",
            "而那个蘑菇发出的光\x01",
            "似乎也有相同的效果。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x110, 0x102, 400)

    ChrTalk(
        0x110,
        "#153F哇～～真是厉害的蘑菇呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_E1F")

    label("loc_DC6")


    ChrTalk(
        0x102,
        (
            "#012F七耀石的原石发出的光可以吸引魔兽……\x01",
            "　\x02\x03",
            "那个蘑菇发出的光\x01",
            "似乎也有相同的效果。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E1F")

    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#009F那个狡猾的大叔～～～\x02\x03",
            "#009F对于会发生这种情况的可能性只字不提。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F4B")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#017F我想如果我们提高警惕的话，\x01",
            "拿着回去也应该没什么问题……\x02\x03",
            "回到城里之后，\x01",
            "就立刻把蘑菇交给委托人吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10F,
        (
            "#142F…………………………\x02\x03",
            "……一定不要出什么差错啊。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F9B")

    label("loc_F4B")


    ChrTalk(
        0x102,
        "#012F总之，现在还是先回城里吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F好！\x02\x03",
            "#005F奸商，\x01",
            "给我等着瞧～～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F9B")

    EventEnd(0x0)
    ClearMapFlags(0x8000000)
    Return()

    # Function_1_396 end

    def Function_2_FA3(): pass

    label("Function_2_FA3")

    OP_A6(0x0)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFE3310, 0x1770, 0xE100, 0xBB8, 0x0)
    OP_43(0xFE, 0x2, 0x0, 0x2)
    OP_8C(0xFE, 315, 0)
    OP_A3(0x0)
    OP_A6(0x0)
    OP_8E(0xFE, 0xFFFE2F8C, 0x1770, 0xEA60, 0x1B58, 0x0)
    OP_A3(0x0)
    Return()

    # Function_2_FA3 end

    def Function_3_FEB(): pass

    label("Function_3_FEB")

    OP_A6(0x2)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFE3A18, 0x1770, 0xE290, 0xBB8, 0x0)
    OP_43(0xFE, 0x2, 0x0, 0x2)
    OP_8C(0xFE, 315, 0)
    OP_A3(0x2)
    OP_A6(0x2)
    OP_8E(0xFE, 0xFFFE3504, 0x1770, 0xEB28, 0x1B58, 0x0)
    OP_A3(0x2)
    Return()

    # Function_3_FEB end

    def Function_4_1033(): pass

    label("Function_4_1033")

    OP_A6(0x1)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFE4058, 0x1770, 0xE7A4, 0xBB8, 0x0)
    OP_43(0xFE, 0x2, 0x0, 0x2)
    OP_8C(0xFE, 315, 0)
    OP_A3(0x1)
    OP_A6(0x1)
    OP_8E(0xFE, 0xFFFE37C0, 0x1770, 0xEFD8, 0x1B58, 0x0)
    OP_A3(0x1)
    Return()

    # Function_4_1033 end

    def Function_5_107B(): pass

    label("Function_5_107B")

    OP_A6(0x4)
    Sleep(200)
    OP_8C(0x102, 225, 0)
    Sleep(400)
    OP_8E(0x102, 0xFFFE2EC4, 0x170C, 0xF6AE, 0xBB8, 0x0)
    OP_8C(0x102, 225, 0)
    OP_A3(0x4)
    Return()

    # Function_5_107B end

    def Function_6_10AE(): pass

    label("Function_6_10AE")

    OP_6D(-120100, 5900, 62700, 800)
    Return()

    # Function_6_10AE end

    SaveToFile()

Try(main)
