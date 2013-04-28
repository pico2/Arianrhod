from ml import *

INSTRUCTION_END_BLOCK           = 1 << 0
INSTRUCTION_START_BLOCK         = 1 << 1

class InstructionFlags:
    def __init__(self, flags):
        self.EndBlock = bool(flags & INSTRUCTION_END_BLOCK)
        self.StartBlock = bool(flags & INSTRUCTION_START_BLOCK)

class Instruction:
    def __init__(self, op, operand = [], flags = 0):
        self.op = op
        self.operand = operand
        self.codeblock = None
        self.flags = InstructionFlags(flags)

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

    def AddBlock(self, block):
        self.blocks.append(block)

    def AddInstruction(self, instruction):
        self.op.append(instruction)
