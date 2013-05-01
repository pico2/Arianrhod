from ml import *

INSTRUCTION_END_BLOCK                   = 1 << 0
INSTRUCTION_START_BLOCK                 = 1 << 1
INSTRUCTION_FORMAT_ARG_NEW_LINE         = 1 << 2
INSTRUCTION_FORMAT_EMPTY_LINE           = 1 << 3

class InstructionFlags:
    def __init__(self, flags):
        self.Flags      = flags
        self.EndBlock   = bool(flags & INSTRUCTION_END_BLOCK)
        self.StartBlock = bool(flags & INSTRUCTION_START_BLOCK)
        self.ArgNewLine = bool(flags & INSTRUCTION_FORMAT_ARG_NEW_LINE)

class InstructionOperand:
    def __init__(self, operand, size):
        self.Operand = operand
        self.Size = size

class LabelEntry:
    def __init__(self, label, offset):
        self.Label = label          # label name
        self.Offset = offset        # label offset in instruction

class Instruction:
    def __init__(self, op = None, operand = None, flags = 0):
        self.OpCode             = op
        self.Operand            = operand if operand != None else []
        self.OperandFormat      = None
        self.BranchTargets      = []
        self.Flags              = InstructionFlags(flags)
        self.Labels             = []
        self.RefCount           = 0
        self.Offset             = -1
        self.Text               = ''

class CodeBlock:
    def __init__(self, Offset = -1):
        self.Offset = Offset
        self.Instructions = []
        self.Parent = None
        self.CodeBlocks = []
        self.Name = None

    def AddBlock(self, block):
        self.CodeBlocks.append(block)

    def AddInstruction(self, instruction):
        self.Instructions.append(instruction)
