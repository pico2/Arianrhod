@echo off

set game=E:\Desktop\yx\RoyalGems\data\font

move/y 24*.xml %game%
move/y 24*.png %game%

move/y 32*.xml %game%
move/y 32*.png %game%

move/y 42*.xml %game%
move/y 42*.png %game%

del %game%\*.fnt
ren %game%\*.xml *.fnt
