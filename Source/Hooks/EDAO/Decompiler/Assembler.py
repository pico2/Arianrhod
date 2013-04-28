from BaseType import *

class Disassembler:
    def __init__(self, InstructionTable):
        self.InstructionTable = InstructionTable

    def DisasmBlock(self, Buffer, BeginOffset, InstructionTable):
        if InstructionTable == None:
            InstructionTable = self.InstructionTable

        blocks = []
