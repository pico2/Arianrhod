from ml import *
import InstructionTable

class Instruction:
    def __init__(self):
        self.op = None
        self.operand = []
        self.endofblock = False

    def Disasm(self, buf):
        return 0

class CodeBlock:
    def __init__(self):
        self.op = []
        self.parent = None
        self.blocks = []

    def Instructions(self):
        return self.op

    def CodeBlocks(self):
        return self.blocks

