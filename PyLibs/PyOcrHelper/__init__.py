#from PyOcrHelper.PyOcrHelper import *
import subprocess, os

class PyOcrHelper:
    def __init__(self):
        self.ModiOcrHelper = os.path.join(os.path.dirname(__file__), 'ModiOcrHelper.exe')

    def Ocr(self, tiff):
        proc = subprocess.Popen('"%s" "%s" STD_OUTPUT_IS_PIPE' % (self.ModiOcrHelper, tiff), stdout = subprocess.PIPE)
        proc.wait()

        return proc.stdout.read().decode('U16')
