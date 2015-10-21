from Cassius import *

def main():
    Self = CraftTarget.Self
    TargetChr = CraftTarget.TargetChr
    TargetPos = CraftTarget.TargetPos

    attackChip      = 7

    showupEff       = 0
    turnAroundEff   = 1
    kickEff         = 2
    hitEff          = 3

    effList = [
        showupEff,
        turnAroundEff,
        kickEff,
        hitEff,
    ]

    with ResourceLock:
        LoadEffect(0x4,         "battle/cr432000.eff")
        LoadChrChip(attackChip, CHR_Cassius_Attack, 0xFF)

    ResetLookingTargetData()
    LookingTargetAdd(Self, "", 0x0)
    LookingTarget(500, 0x8, 0xF)
    Sleep(50)
    Yield()

    TurnDirection(Self, TargetPos, 0, 0, 0x0)
    SetChrChip(Self, attackChip)
    SetChrSubChip(Self, 5)
    Sleep(60)
    Yield()

    SetChrSubChip(Self, 8)
    Sleep(100)
    Yield()

    ShakeScreen(200, 200, 200, 500)
    # jump eff
    # jump eff

    Voice(0, 卡西乌斯_钢盔断_起跳, 0, 0, 0, 0xFE)
    SoundEx(卡西乌斯_音效_钢盔断_起跳, 0)
    ShowChrTrails(Self, 50, 200)

    def attackInTheSky():
        SoundEx(256, 0)

        # SetChrSubChip(Self, 6)
        # Sleep(60)
        # Yield()
        SetChrSubChip(Self, 7)
        Sleep(30)
        Yield()
        SetChrSubChip(Self, 8)
        Sleep(500)
        Yield()

        for i in range(9, 12):
            SetChrSubChip(Self, i)
            Sleep(50)
            Yield()

        Return()

    def jumpInTheSky():
        SetChrSubChip(Self, 6)
        Sleep(598)
        Yield()
        SetChrSubChip(Self, 5)
        Sleep(100)
        Yield()
        SetChrSubChip(Self, 4)
        Sleep(100)
        Yield()
        SetChrSubChip(Self, 5)
        Sleep(100)
        Yield()
        Return()

    QueueWorkItem(Self, 1, jumpInTheSky)
    ChrJump(Self, Self, 0, 0, 0, 3000, 2000)
    WaitChrThread(Self, 1)
    QueueWorkItem(Self, 1, attackInTheSky)

    HideChrTrails(Self)
    ShakeScreen(200, 200, 200, 500)
    # CancelEffect(Self, jump eff 2)
    BlurSwitch(0, 0xBBFFFFFF, 0, 1, 3)

    def damage():
        Sleep(100)
        Yield()

        SortTarget(0)
        ResetTarget()

        label('钢盔断_next_target')

        ForeachTarget('钢盔断_next_target_end')
        TurnDirection(TargetChr, Self, 0, 0, 0x0)
        DamageAnime(TargetChr, 0, 30)

        def underattack():
            AS_89(Self)
            ShowInfoText('before jump', 500)
            ChrJump(Self, Self, 0, 0, 0, 3000, 1000)
            ShowInfoText('after jump', 1000)
            ChrMove(Self, 0xF0, 0, 0, 0, 0, 0)
            # WaitChrThread(Self, 0)
            AS_9C(Self)
            Yield()
            Return()

        QueueWorkItem(TargetChr, 1, underattack)

        # ShowEff(0x1:b, 0xFF:b, Target, 0x3:s, 0x0:i, 0x0:i, 0x0:i, 0x0:s, 0x0:s, 0x0:s, 0x3E8:s, 0x3E8:s, 0x3E8:s, 0xFF:b)
        Sleep(50)
        Yield()
        NextTarget()
        Jump('钢盔断_next_target')

        label('钢盔断_next_target_end')

        # WaitChrThread(0xFC, 1)
        # WaitChrThread(0xFC, 2)

        ResetTarget()

        label('钢盔断_damage_next_target')

        ForeachTarget('钢盔断_damage_next_target_end')
        WaitChrThread(TargetChr, 1)
        DamageCue(TargetChr)
        Yield()
        NextTarget()
        Jump('钢盔断_damage_next_target')

        label('钢盔断_damage_next_target_end')

        # AS_8F(0)
        Return()

    for _ in range(2):
        PlayEffect(Self, Self, 4, 5, 0, 0, 0, 0, 0, 0, 800, 800, 800, 0xFF)
        PlayEffect(Self, Self, 4, 5, 1000, 0, 0, 0, 0, 0, 800, 800, 800, 0xFF)
        PlayEffect(Self, Self, 4, 5, -1000, 0, 0, 0, 0, 0, 800, 800, 800, 0xFF)
        Sleep(50)
        Yield()

    ResetLookingTargetData()
    LookingTargetAdd(0xFC, "", 0)
    LookingTargetAdd(Self, "", 0)
    LookingTarget(500, 0x8, 0xF)
    CancelBlur(1500)

    QueueWorkItem(Self, 2, damage)
    # damage()
    Sleep(500)
    Yield()

    WaitChrThread(Self, 1)
    WaitChrThread(Self, 2)
    SetChrChip(Self, 0)
    SetChrSubChip(Self, 0)
    Sleep(500)
    Yield()

    FreeEffect(4)
