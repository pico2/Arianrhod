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
        'lib2to3',
        'site-packages\\PyQt',
        'site-packages\\PIL',
        'site-packages\\Crypto',
        'site-packages\\IPython',
        'site-packages\\pyreadline',
        'site-packages\\readline.py',
    ]

    for i in range(len(ignores)):
        ignores[i] = (pylib + '\\' + ignores[i]).lower()

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
