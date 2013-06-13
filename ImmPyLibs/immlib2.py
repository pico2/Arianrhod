import pefile, debugger, os, sys, struct, traceback
from immlib import *
from wintypes2 import *
from libhook import *
from immhelper import *

MODULE_INFO_BASE        = 0
MODULE_INFO_SIZE        = 1
MODULE_INFO_ENTRY_POINT = 2

class Debugger2(Debugger):
    def __init__(self):
        Debugger.__init__(self)

    def Detach2(self):
        return debugger.asuna_detach()

    def sendshortcut(self, where, msg, ctrl, shift, vk):
        return debugger.sendshortcut(int(where), int(msg), int(ctrl), int(shift), int(vk))

    def erun(self):
        return self.sendshortcut(PM_MAIN, WM_KEYDOWN, 0, 1, VK_F9)

    def asuna_log(self, msg, address = 0xbadf00d ,highlight = False, gray = False , focus = 0):
        """
            Adds a single line of ASCII text to the log window.  

            @type  msg: STRING
            @param msg: Message (max size is 255 bytes)

            @type  address: DWORD
            @param address: Address associated with the message

            @type  highlight: BOOLEAN
            @param highlight: Set highlight text

            @type  gray: BOOLEAN
            @param gray: Set gray text
            """
        if gray and not highlight:
            highlight = -1

        if type(msg) == unicode:
            msg = msg.encode('936')

        return debugger.add_to_list(address, int(highlight), str(msg)[:255], focus)

    def deleteHbIndex(self, index):
        return debugger.DeleteHardBreakpointByIndex(index)

    def deleteHbAddr(self, addr, type = HB_FREE):
        """ 
            if type equal HB_FREE, ignore type
            """
        return debugger.DeleteHardBreakpointByAddr(addr, type)

    def clearHardbreakpoints(self):
        for index in range(0, 4):
            debugger.DeleteHardBreakpointByIndex(index)

    def refreshModules(self):
        debugger.RefreshModules()

    def readWString2(self,address):
        """
            Read a unicode string from the remote process

            @type  address: DWORD
            @param address: Address of the unicode string

            @rtype:  str
            @return: Unicode String
            """

        blocksize = 64
        wstring = ""
        while True:
            read = self.readMemory(address, blocksize)
            if len(read) < 2:
                break

            address += blocksize
            if (len(read) & 1) != 0:
                read = read[0:-1]

            index = 0
            while index < len(read):
                if read[index:index + 2] == '\x00\x00':
                    break

                index += 2

            if index != len(read):
                wstring += read[0:index]
                break

            wstring += read

        return wstring

    def QueryAllModules(self):
        return debugger.get_all_modules()

    def QueryModuleByName(self, modname):
        modname = mbcs(modname).lower()
        modulos = self.QueryAllModules()
        for name, mod in modulos.iteritems():
            if modname in os.path.splitext(os.path.basename(name))[0].lower():
                return Module(name, mod[MODULE_INFO_BASE], mod[MODULE_INFO_SIZE], mod[MODULE_INFO_ENTRY_POINT])

        return None

    log = asuna_log
    Detach = Detach2
    readWString = readWString2
