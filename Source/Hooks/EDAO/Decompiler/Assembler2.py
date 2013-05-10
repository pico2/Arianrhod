from BaseType import *
from InstructionTable import *

def plog(*args):
    pass

#plog = print

offsetlist = {}
disasmtbl = {}
fuck = False

class Disassembler:
    class DisasmData:
        Stream              = None
        DisasmTable         = None
        Block               = None
        InstructionTable    = None
        EndOffset           = INVALID_OFFSET

    def __init__(self, InstructionTable, DiasmInstructionCallback = None):
        self.InstructionTable           = InstructionTable
        self.DiasmInstructionCallback   = DiasmInstructionCallback
        self.DisasmTable                = {}
        self.LabelMap                   = {}
        self.FormattedBlock             = {}

    def DisasmBlock(self, Stream, InstructionTable = None, DisasmTable = None):
        if InstructionTable == None:
            InstructionTable = self.InstructionTable

        if DisasmTable == None:
            DisasmTable = {}

        data = self.DisasmData()

        data.Stream             = Stream
        data.InstructionTable   = InstructionTable
        data.DisasmTable        = DisasmTable
        data.Block              = CodeBlock(Stream.tell())

        ret = self.DisasmBlockWorker(data)

        #for offset, inst in DisasmTable.items(): disasmtbl[offset] = inst

        return data.Block

    def DefaultDisasmInstruction(self, data):
        inst = data.Instruction
        fs = data.FileStream
        entry = data.TableEntry

        for opr in inst.OperandFormat:
            inst.Operand.append(entry.GetOperand(opr, fs))
            if opr.lower() == 'o':
                inst.BranchTargets.append(inst.Operand[-1])

        return inst

    def DisasmInstruction(self, data):
        inst = data.Instruction
        entry = data.TableEntry

        inst.OperandFormat = entry.Operand

        handler = entry.Handler if entry.Handler != None else self.DefaultDisasmInstruction
        inst = handler(data)
        if inst == None:
            inst = self.DefaultDisasmInstruction(data)

        if self.DiasmInstructionCallback:
            self.DiasmInstructionCallback(inst, data.FileStream)

        return inst

    def DisasmBlockWorker(self, data):

        InstructionTable = data.InstructionTable
        Stream = data.Stream
        DisasmTable = data.DisasmTable

        block = data.Block

        pos = Stream.tell()

        if pos in DisasmTable:
            DisasmTable[pos].RefCount += 1
            return None

        plog('block: %08X' % block.Offset)

        blockref = []

        fileend = Stream.size()

        while True:
            pos = Stream.tell()
            if pos in DisasmTable: break
            if pos >= fileend: break

            offsetlist[pos] = True

            #print('%08X: ' % pos, end = '')
            op = InstructionTable.GetOpCode(Stream)
            #print('%02X' % op)

            entry = InstructionTable[op]

            plog('    %08X: %s' % (pos, entry.OpName))

            handlerdata = HandlerData(HANDLER_REASON_READ)

            handlerdata.Instruction        = Instruction(op)
            handlerdata.Instruction.Flags  = entry.Flags
            handlerdata.Instruction.Offset = pos
            handlerdata.FileStream         = Stream
            handlerdata.TableEntry         = entry
            handlerdata.Disasm             = self.DisasmInstruction

            inst = self.DisasmInstruction(handlerdata)

            if inst == None:
                raise Exception('disasm op %02X @ %08X failed' % (op, pos))

            inst.Size = Stream.tell() - pos

            for i in range(pos, Stream.tell()): offsetlist[i] = True

            DisasmTable[inst.Offset] = inst
            block.AddInstruction(inst)

            if not inst.Flags.EndBlock and not inst.Flags.StartBlock:
                continue

            targets = inst.BranchTargets
            inst.BranchTargets = []

            for offset in targets:
                blockref.append((offset, inst))
                #blockref[offset] = inst

            if inst.Flags.EndBlock:
                break

        plog('block end: %08X' % block.Offset)

        for ref in blockref:
            offset, inst = ref
            Stream.seek(offset)
            newblock = self.DisasmBlock(Stream, InstructionTable, DisasmTable)
            if newblock == None or len(newblock.Instructions) == 0:
                continue

            newblock.Instructions[0].RefCount += 1

            if offset >= block.Instructions[-1].Offset or offset < block.Instructions[0].Offset:
                block.Instructions += newblock.Instructions
            else:
                for i in range(len(block.Instructions)):
                    if offset >= block.Instructions[i].Offset:
                        continue

                    block.Instructions = block.Instructions[:i] + newblock.Instructions + block.Instructions[i:]
                    break

        return block

    def DefaultFormatInstruction(self, data):
        inst = data.Instruction
        entry = data.TableEntry

        opname = entry.OpName
        oprlist = entry.FormatAllOperand(
                        BuildFormatOperandParameterList(
                            inst.OperandFormat,
                            inst.Operand,
                            inst.Flags,
                            data.LabelMap
                        )
                    )

        return '%s(%s)' % (opname, oprlist)

    def FormatInstruction(self, data):
        inst = data.Instruction
        entry = data.TableEntry

        handler = entry.Handler if entry.Handler != None else self.DefaultFormatInstruction
        inst = handler(data)
        if inst == None:
            inst = self.DefaultFormatInstruction(data)

        return inst

    class FormatData:
        Block               = None
        LabelMap            = {}
        FormattedBlock      = {}
        InstructionTable    = None

    def FormatCodeBlock(self, block, LabelMap = None, FormattedBlock = None, InstructionTable = None):

        data = self.FormatData()

        data.Block              = block
        data.LabelMap           = LabelMap if LabelMap != None else self.LabelMap
        data.FormattedBlock     = FormattedBlock if FormattedBlock != None else self.FormattedBlock
        data.InstructionTable   = InstructionTable if InstructionTable != None else self.InstructionTable

        return self.FormatCodeBlockWorker(data)

    def FormatCodeBlockWorker(self, data):
        InstructionTable    = data.InstructionTable
        LabelMap            = data.LabelMap
        FormattedBlock      = data.FormattedBlock
        block               = data.Block

        if block.Offset in FormattedBlock: return

        FormattedBlock[block.Offset] = True

        text = []

        def AddLabel(name):
            text.append('')
            text.append('label("%s")' % name)
            text.append('')

        def EndLabel(name):
            text.append('')
            text.append('# %s end' % name)

        blockname = None
        if block.Offset not in LabelMap:
            blockname = block.Name if block.Name != None else InstructionTable.GetLabelName(block.Offset)
            AddLabel(blockname)
            LabelMap[block.Offset] = block.Name

        for inst in block.Instructions:

            if inst.Offset != block.Offset and inst.Offset in self.FormattedBlock:
                continue

            FormattedBlock[inst.Offset] = True

            handlerdata = HandlerData(HANDLER_REASON_FORMAT)

            handlerdata.Instruction     = inst
            handlerdata.TableEntry      = InstructionTable[inst.OpCode]
            handlerdata.Format          = self.FormatInstruction
            handlerdata.LabelMap        = LabelMap
            handlerdata.CodeBlock       = block

            #print('%08X' % inst.Offset)
            #del disasmtbl[inst.Offset]

            #print('%08X %02X: ' % (inst.Offset, inst.OpCode), end  = '')
            symbol = self.FormatInstruction(handlerdata)
            #print(symbol)

            if inst.RefCount != 0:
                name = InstructionTable.GetLabelName(inst.Offset)
                if inst.Offset not in LabelMap:
                    AddLabel(name)
                    LabelMap[inst.Offset] = name

            text.append(symbol)

        if blockname != None:
            EndLabel(blockname)

        text.append('')

        for subblock in block.CodeBlocks:
            text += self.FormatCodeBlock(subblock, LabelMap, FormattedBlock, InstructionTable)

        return text
