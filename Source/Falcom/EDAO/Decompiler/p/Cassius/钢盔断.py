from Cassius import *

def main():
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
        LoadEffect(0x4,         "battle/cm006_00.eff")
        LoadChrChip(attackChip, CHR_Cassius_Attack, 0xFF)

    PlayEffect(0xFF, 0xFF, 4, 0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF)
    Sleep(2000)
    Yield()

    FreeEffect(4)
