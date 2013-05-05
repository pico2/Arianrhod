from ml import *

scena = 'J:\\Falcom\\ED_AO\\data\\scena\\'
offset = 0x48

for f in os.listdir(scena):
    fs = BytesStream()
    fs.open(scena + f, 'rb')
    fs.seek(offset)
    if fs.byte() != 0:
        print(f)
        input()
