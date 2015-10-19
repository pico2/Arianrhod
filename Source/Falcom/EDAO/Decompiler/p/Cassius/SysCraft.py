from ActionHelper import *

def init():
    #LoadEffect(0x80, "battle/mgaria0.eff")
    #LoadEffect(0x81, "battle/mgaria1.eff")

    LoadEffect(0x80, "event/ev10006.eff")
    LoadEffect(0x81, "event/ev10007.eff")

    LoadEffect(0x82, "battle/cr035000.eff")
    LoadEffect(0x83, "battle/cr035100.eff")

    #PlayEffect(0xFF, 0xFF, 0x37, 0x41, 0, 1100, 0, 0, 0, 0, 1000, 1000, 1000, 0xA)
    Jc(0x9, 0x1, 0x107, "loc_48A")
    AS_74(0x0, 0x100)
    Jump("loc_48E")

    label("loc_48A")

    AS_74(0x0, 0x20)

    label("loc_48E")

    AS_6E(0x400000)

def stand():
    label("SysCraft_Stand")

    Call('clear_all_debuff')

    SetChrChip(0xFF, 0x0)
    SetChrSubChip(0xFF, 0x0)
    Sleep(130)
    Yield()
    SetChrSubChip(0xFF, 0x1)
    Sleep(130)
    Yield()
    SetChrSubChip(0xFF, 0x2)
    Sleep(130)
    Yield()
    SetChrSubChip(0xFF, 0x1)
    Sleep(130)
    Yield()
    SetChrSubChip(0xFF, 0x0)
    Sleep(130)
    Yield()
    SetChrSubChip(0xFF, 0x3)
    Sleep(130)
    Yield()
    SetChrSubChip(0xFF, 0x4)
    Sleep(130)
    Yield()
    SetChrSubChip(0xFF, 0x3)
    Sleep(130)
    Yield()
    Jump("SysCraft_Stand")

def move():
    label("SysCraft_Move")

    SetChrChip(0xFF, 0x1)
    SetChrSubChip(0xFF, 0x0)
    Sleep(40)
    Yield()
    SetChrSubChip(0xFF, 0x1)
    Sleep(40)
    Yield()
    SetChrSubChip(0xFF, 0x2)
    Sleep(40)
    Yield()
    SetChrSubChip(0xFF, 0x3)
    Sleep(40)
    Yield()
    SetChrSubChip(0xFF, 0x4)
    Sleep(40)
    Yield()
    SetChrSubChip(0xFF, 0x5)
    Sleep(40)
    Yield()
    SetChrSubChip(0xFF, 0x6)
    Sleep(40)
    Yield()
    SetChrSubChip(0xFF, 0x7)
    Sleep(40)
    Yield()
    Jump("SysCraft_Move")

def underAttack():
    AS_78(1)
    LoadEffect(1, "eff/trapdmg2.eff")
    AS_78(0)

    Knockback(0)
    SoundEx(115, 0)
    PlayEffect(0xFF, 0xFF, 1, 0, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF)
    SetChrChip(CraftTarget.Self, 4)
    SetChrSubChip(CraftTarget.Self, 3)
    Sleep(1000)
    Yield()

    FreeEffect(1)

def dead():
    AS_6C()

    SoundEx(3868, 0)
    SetChrChip(0xFF, 0)
    SetChrSubChip(0xFF, 0)
    Sleep(1000)
    Yield()

    StopSound(3868)
    Yield()

    Return()

def artsAria():
    TurnDirection(0xFF, 0xFB, 0x0, 500, 0x0)
    Jc(0x8, 0x1, 0x0, "arts_effect_end")
    Jc(0x2D, 0x1, 0x1, "other_voice")
    PlayEffect(0xFF, 0xFF, 0x80, 0x41, 0, 50, 0, 0, 0, 0, -1, -1, -1, arts_aria_eff_id)
    AS_A9(0xFF, 0x0, 0xFFFF0000)
    Jump("arts_effect_end")

    label("other_voice")

    PlayEffect(0xFF, 0xFF, 0x80, 0x41, 0, 50, 0, 0, 0, 0, -1, -1, -1, arts_aria_eff_id)
    Voice(0x0, 3864, 3883, 3884, 0, 0xFE)
    SoundEx(509, 0x0)

    label("arts_effect_end")

    SendMessage(0x1)
    Call("set_arts_chip")
    Return()

    label("set_arts_chip")

    SetChrChip(0xFF, 0x3)

    label("arts_chip_loop")

    SetChrSubChip(0xFF, 0x0)
    Sleep(130)
    Yield()
    SetChrSubChip(0xFF, 0x1)
    Sleep(130)
    Yield()
    SetChrSubChip(0xFF, 0x2)
    Sleep(130)
    Yield()
    SetChrSubChip(0xFF, 0x1)
    Sleep(130)
    Yield()
    Jump("arts_chip_loop")

def artsCast():
    Jc(0x2D, 0x3, 0x2, "arts_cast_skip_voice")
    #PlayEffect(0xFF, 0xF9, 0x81, 0x0, 0, 50, 0, 0, 0, 0, -1, -1, -1, 0)
    CancelEffect(0xFF, arts_aria_eff_id)
    SoundEx(510, 0x0)
    TurnDirection(0xFF, 0xFB, 0, 500, 0x0)
    Sleep(200)
    Yield()
    SetChrChip(0xFF, 0x3)
    SetChrSubChip(0xFF, 0x3)
    Sleep(300)
    Yield()
    Voice(0x0, 3875, 3876, 0, 0, 0xFE)
    SetChrSubChip(0xFF, 0x4)
    Sleep(0)
    Yield()

    label("arts_cast_skip_voice")

    ArtsUsing(0xFFFF)
    ArtsEnd()
    Return()

def enterBattle():
    BeginChrThread(0xFF, 1, "SysCraft_Stand", 0x0)
    Voice(0x0, 3881, 3882, 0, 0, 0xFE)
    Yield()
    EndChrThread(0xFF, 1)
    Return()

def battleWin():
    pass

def useItem():
    SetChrChip(0xFF, 0x3)
    SetChrSubChip(0xFF, 0x0)
    Sleep(300)
    Yield()
    Voice(0x0, 3881, 3906, 0, 0, 0xFE)
    SetChrSubChip(0xFF, 0x4)
    Sleep(300)
    Yield()
    PlayEffect(0xFF, 0xFF, 0x2A, 0x2, 0, 1000, 500, 0, 0, 0, 65535, 65535, 65535, 0xFF)
    Sleep(500)
    Yield()
    UseItemBegin()
    UseItemEnd()
    Return()

def normalAttack():
    AS_78(0x1)
    LoadChrChip(0x7, "chr/ch04672.itc", 0xFF)
    LoadEffect(0x0, "battle/ms00001.eff")
    AS_78(0x0)

    ResetTarget()
    ResetLookingTargetData()
    LookingTargetAdd(0xFF, "", 0x0)
    LookingTargetAdd(0xFC, "", 0x0)
    LookingTarget(100, 20, 30)
    BeginChrThread(0xFF, 1, "SysCraft_Move", 0x0)
    AS_1E(0xFFFFFFFF)
    EndChrThread(0xFF, 1)
    TurnDirection(0xFF, 0xFE, 0, 0, 0x0)
    AS_89(0xFF)
    AS_6D(0x200000)
    SetChrChip(0xFF, 0x7)
    SetChrSubChip(0xFF, 0x0)
    Sleep(0x5A)
    Yield()

    # PlayEffect(0xFF, 0xFF, 0x82, 0x3, 0, 850, 0, 0, 0, 0, 900, 900, 900, -1)
    ShakeScreen(50, 50, 50, 500)
    Yield()

    SetChrSubChip(0xFF, 0x1)
    Sleep(0x50)
    Yield()

    AS_05(0xFF, 0x0, 0x0)
    Voice(0x0, 3987, 0, 0, 0, 0xFE)

    for i in range(2, 7):
        SetChrSubChip(CraftTarget.Self, i)
        Sleep(0x50)
        Yield()

    Knockback(2)
    ResetLookingTargetData()
    DamageAnime(0xFE, 0x1, 0x32)
    DamageCue(0xFE)
    ResetLookingTargetData()

    LookingTargetAdd(0xFF, "", 0x0)
    LookingTargetAdd(0xFC, "", 0x0)
    LookingTarget(100, 20, 30)
    AS_21(0x1, 0xFF, 150, 2000)
    Sleep(500)
    Yield()

    for i in range(7, 10):
        SetChrSubChip(CraftTarget.Self, i)
        Sleep(32)
        Yield()

    Sleep(200)
    Yield()

    for i in range(10, 12):
        SetChrSubChip(CraftTarget.Self, i)
        Sleep(32)
        Yield()

    ChrMove(0xFF, 0xF0, 0, 0, 0, 100, 0x0)
    BeginChrThread(0xFF, 1, "SysCraft_Stand", 0x0)
    AS_8F(0x0)
    EndChrThread(0xFF, 1)
    AS_6E(0x200000)
    AS_6B()
    Return()