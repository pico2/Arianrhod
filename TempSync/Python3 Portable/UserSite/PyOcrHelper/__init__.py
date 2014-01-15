from ml import *
import subprocess, os, struct, threading

class PyOcrHelper:
    mutex = threading.Lock()

    def __init__(self):
        self.HelperProcess = None
        ModiOcrHelper = os.path.join(os.path.dirname(__file__), 'ModiOcrHelper.exe')
        self.HelperProcess = subprocess.Popen(
                                '"%s" %d USE_STDIN_AS_INPUT' % (ModiOcrHelper, os.getpid()),
                                stdin = subprocess.PIPE,
                                stderr = subprocess.PIPE
                            )

    def __del__(self):
        if self.HelperProcess is not None:
            self.HelperProcess.terminate()
            self.HelperProcess = None

    def Close(self):
        self.__del__()

    def Ocr(self, tiff):
        tiff = tiff.encode('U16')[2:]
        with self.mutex:
            self.HelperProcess.stdin.write(tiff)
            self.HelperProcess.stdin.flush()

            retlen = self.HelperProcess.stderr.read(8)
            retlen = struct.unpack('<Q', retlen)[0]
            if retlen == 0:
                return ''

            return self.HelperProcess.stderr.read(retlen).decode('U16')
