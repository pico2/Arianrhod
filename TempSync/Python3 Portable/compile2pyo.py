from ml import *
import py_compile, zipfile, shutil

def main():

    pylib = None
    for x in sys.path:
        if x.lower().endswith('\lib'):
            pylib = x
            break

    if pylib is None:
        return

    selfpath =  os.path.dirname(__file__) + '\\'
    pyodir = selfpath + os.path.basename(pylib)

    pythonzip = zipfile.ZipFile(selfpath + 'python.zip', 'w')

    ignores = \
    [
        'test',
        #'lib2to3',
        'site-packages\\PyQt',
        'site-packages\\PIL',
        'site-packages\\Crypto',
        'site-packages\\IPython',
        'site-packages\\ipdb',
        'site-packages\\pyreadline',
        'site-packages\\readline.py',
    ]

    copytrees = \
    [
        #'site-packages\\MyPyLibrary\\AMFHelper',
        'site-packages\\MyPyLibrary\\PyOcrHelper',
        'lib2to3',
    ]

    ignores += copytrees

    for i in range(len(ignores)):
        ignores[i] = (pylib + '\\' + ignores[i]).lower()

    for x in copytrees:
        src = pylib + '\\' + x + '\\'
        dst = selfpath + 'UserSite\\' + os.path.basename(x) + '\\'
        ignore_patterns = ['__pycache__']
        for f in EnumDirectoryFiles(src):
            found = False
            for ignore in ignore_patterns:
                if f.lower().find(ignore.lower()) != -1:
                    found = True
                    break

            if found:
                continue

            o = f.replace(src, dst, 1)
            os.makedirs(os.path.dirname(o), exist_ok = True)
            try:
                samefile = os.path.samefile(f, o)
            except FileNotFoundError:
                samefile = False

            if not samefile:
                shutil.copy2(f, o)

    def proc(file):
        for x in ignores:
            if file.lower().startswith(x):
                return

        SetConsoleTitle(file)
        pyo = os.path.splitext(file)[0].replace(pylib, pyodir) + '.pyo'
        os.makedirs(os.path.dirname(pyo), exist_ok = True)
        ret = py_compile.compile(file, pyo, optimize = 2)
        if ret is None:
            return

        pythonzip.write(
            filename = pyo,
            arcname = pyo.replace(pyodir + '\\', ''),
            compress_type = zipfile.ZIP_DEFLATED
        )

    ForEachFile(pylib, proc, '*.py')

    shutil.rmtree(pyodir)
    pythonzip.close()

if __name__ == '__main__':
    TryInvoke(main)
