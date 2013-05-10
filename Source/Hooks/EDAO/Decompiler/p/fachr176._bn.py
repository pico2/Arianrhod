from FieldAttackChr import *

def main():
    CreateFieldAttack("fachr176._bn", "chr/ch04258.itc", "sysatk05")

    SetChrSubChip(0)
    Sleep(120)
    SetChrSubChip(1)
    Sleep(90)
    Voice(3867, 3866, 3876, 0)
    Sound(248)
    #FA_0A(0x0, 0xA)
    #FA_0B(300)
    PlayEffect(0x0, 600, 0, 0, 0, 0, 0x0)
    SetChrSubChip(2)
    FA_0C(0x64, 0xC8)
    FA_0A(0x0, 0x5)
    Sleep(90)
    SetChrSubChip(3)
    Sleep(90)
    SetChrSubChip(4)
    Sleep(90)
    SetChrSubChip(5)
    Sleep(90)
    SetChrSubChip(6)
    Sleep(250)
    Return()

TryInvoke(main)
