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
        'site-packages\\PyQt',
        'site-packages\\IPython',
        'site-packages\\ipdb',
        'site-packages\\pyreadline',
        'site-packages\\readline.py',
    ]

    copytrees = \
    [
        (False, 'site-packages\\MyPyLibrary\\PyOcrHelper'),
        (False, 'site-packages\\PIL'),
        (False, 'site-packages\\Crypto'),
        (True,  'lib2to3'),
    ]

    optimize = 2

    ignores += [p[1] for p in copytrees]

    for i in range(len(ignores)):
        ignores[i] = (pylib + '\\' + ignores[i]).lower()

    for do_not_compile, x in copytrees:
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

            SetConsoleTitle(f)

            o = f.replace(src, dst, 1)
            os.makedirs(os.path.dirname(o), exist_ok = True)

            if f.lower().endswith('.pyd'):
                continue

            if do_not_compile is False and f.lower().endswith('.py'):
                pyo = os.path.splitext(o)[0] + '.pyc'
                ret = py_compile.compile(f, pyo, optimize = optimize)
                if ret is None:
                    raise Exception('error occured while compiling %s -> %s' % (f, pyo))
            else:
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
        pyo = os.path.splitext(file)[0].replace(pylib, pyodir) + '.pyc'
        os.makedirs(os.path.dirname(pyo), exist_ok = True)
        ret = py_compile.compile(file, pyo, optimize = optimize)
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
