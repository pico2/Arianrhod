from ml import *

INSTRUCTION_END_BLOCK           = 1 << 0
INSTRUCTION_START_BLOCK         = 1 << 1

class InstructionFlags:
    def __init__(self, flags):
        self.Flags = flags
        self.EndBlock = bool(flags & INSTRUCTION_END_BLOCK)
        self.StartBlock = bool(flags & INSTRUCTION_START_BLOCK)

class InstructionOperand:
    def __init__(self, operand, size):
        self.Operand = operand
        self.Size = size

class LabelEntry:
    def __init__(self, label, offset):
        self.Label = label          # label name
        self.Offset = offset        # label offset in instruction

class Instruction:
    def __init__(self, op, operand = [], flags = 0):
        self.OpCode         = op
        self.Operand        = operand
        self.BranchTargets  = []
        self.Flags          = InstructionFlags(flags)
        self.Labels         = []

    def Disasm(self, buf):
        return 0

class CodeBlock:
    def __init__(self):
        self.Instructions = []
        self.Parent = None
        self.CodeBlocks = []
        self.Namw = ''

    def AddBlock(self, block):
        self.CodeBlocks.append(block)

    def AddInstruction(self, instruction):
        self.Instructions.append(instruction)
