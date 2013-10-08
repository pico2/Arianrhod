from ml import *

def main():
    indir =  os.path.dirname(__file__) + '\\UserSite\\'
    #indir = r'E:\Python\Lib\site-packages\PyQt5'

    def proc(file):
        print(file)
        fs = BytesStream().open(file, 'rb+')

        buf = fs.read()
        if buf[:2] != b'MZ':
            return

        python33 = buf.find(b'python33.dll')
        if python33 == -1:
            return

        buf = bytearray(buf)
        buf[python33 + len('python3')] = ord('4')


        fs.seek(0)
        fs.write(buf)

    ForEachFile(indir, proc)

if __name__ == '__main__':
    TryInvoke(main)
