from BaseType import *

class InstructionTableEntry:
    # operand = 'b,w,d,s'
    # b = byte  w = word    d = dword   s = str
    def __init__(self, op, name = '', operand = '', flags = 0, handler = None):
        self.op         = op
        self.name       = name
        self.operand    = operand
        self.flags      = InstructionFlags(flags)
        self.handler    = handler

def inst(op, operand = '', flags = 0, handler = None):
    name = eval('"OP_%02X' % op + '"')
    return InstructionTableEntry(op, name, operand, flags, handler)

instruction_table_edao = \
[
    inst(0xF0, 'bw'),
]

print(instruction_table_edao[0].op, instruction_table_edao[0].name, instruction_table_edao[0].operand, instruction_table_edao[0].flags, instruction_table_edao[0].handler, sep = '\n')

del inst

input()
