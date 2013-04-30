from BaseType import *
from InstructionTable import *

def plog(*args):
    pass

#plog = print

class Disassembler:
    def __init__(self, InstructionTable):
        self.InstructionTable = InstructionTable

    def DisasmBlock(self, Stream, InstructionTable = None):
        if InstructionTable == None:
            InstructionTable = self.InstructionTable

        DisasmTable = {}

        return self.DisasmBlockWorker(Stream, InstructionTable, DisasmTable)

    def DefaultDisasmInstruction(self, data):
        inst = data.Instruction
        fs = data.FileStream
        entry = data.TableEntry

        for opr in entry.Operand:
            inst.Operand.append(entry.GetOperand(opr, fs))
            if opr.lower() == 'o':
                inst.BranchTargets.append(inst.Operand[-1])

        return inst

    def DisasmInstruction(self, data):
        inst = data.Instruction
        entry = data.TableEntry

        handler = entry.Handler if entry.Handler != None else self.DefaultDisasmInstruction
        return handler(data)

    def DisasmBlockWorker(self, Stream, InstructionTable, DisasmTable):

        block = CodeBlock(Stream.tell())
        if block.Offset in DisasmTable:
            return None

        plog('block: %08X' % block.Offset)

        DisasmTable[block.Offset] = block

        blockref = {}

        while True:
            pos = Stream.tell()
            print('%08X: ' % pos, end = '')
            op = InstructionTable.GetOpCode(Stream)

            print('%02X' % op)

            entry = InstructionTable[op]

            plog('    %08X: %s' % (pos, entry.OpName))

            data = HandlerData(HANDLER_REASON_READ)

            data.Instruction        = Instruction(op)
            data.Instruction.Flags  = entry.Flags
            data.FileStream         = Stream
            data.TableEntry         = entry
            data.Disasm             = self.DisasmInstruction

            inst = self.DisasmInstruction(data)

            block.AddInstruction(inst)

            targets = []

            if inst.Flags.EndBlock:
                if len(inst.BranchTargets) == 0:
                    break
                elif len(inst.BranchTargets) != 1:
                    raise Exception('end block instruction has multiple branch')

                targets = inst.BranchTargets
            elif inst.Flags.StartBlock:
                targets = inst.BranchTargets

            if len(targets) == 0:
                continue

            inst.BranchTargets = []
            for offset in targets:
                blockref[offset] = inst
                #Stream.seek(offset)
                #newblock = self.DisasmBlockWorker(Stream, InstructionTable, DisasmTable)
                #if newblock != None:
                #    inst.BranchTargets.append(newblock)

        plog('block end: %08X' % block.Offset)

        for offset, inst in blockref.items():
            Stream.seek(offset)
            newblock = self.DisasmBlockWorker(Stream, InstructionTable, DisasmTable)
            if newblock != None:
                newblock.Parent = block
                block.AddBlock(newblock)
                inst.BranchTargets.append(newblock)

        return block
