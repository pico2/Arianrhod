from EDAOBase import *

INVALID_DROP_ITEM_ID        = 0xFFFF
MAXIMUM_MAGIC_NUMBER        = 80
MAXIMUM_CRAFT_NUMBER        = 16
MAXIMUM_SCRAFT_NUMBER       = 5
MAXIMUM_CRAFT_INFO_NUMBER   = 16

class CraftTarget:
    def __init__(self):

        self.Enemy  = 0x12

    def GetFlags(self):
        pass

class CraftAttribute:
    Chi  = 0
    Mizu = 1
    Hono = 3
    Kaze = 2
    Toki = 4
    Sora = 5
    Gen  = 6

CraftAttributeNames = {}

for attr in dir(CraftAttribute):
    if attr[:2] == '__' and attr[-2:] == '__':
        continue

    expr = 'CraftAttributeNames[0x%X] = "CraftAttribute.%s"' % (getattr(CraftAttribute, attr), attr)
    exec(expr)

class CraftRange:
    Target                     = 0x01
    CircleOnTarget             = 0x02
    LineOnTarget               = 0x03
    TargetWithoutMove          = 0x04

    CircleOnLocation           = 0x0B
    LineOnLocation             = 0x0C
    FullMap                    = 0x0D
    CircleOnSelf               = 0x0E
    CircleOnLocationExclude    = 0x0F

    LineOnLocationIncludeSelf  = 0x11
    CircleOnLocationIncludeAll = 0x12

    SelectLocation             = 0x32

CraftRangeNames = {}

for attr in dir(CraftRange):
    if attr[:2] == '__' and attr[-2:] == '__':
        continue

    expr = 'CraftRangeNames[0x%X] = "CraftRange.%s"' % (getattr(CraftRange, attr), attr)
    exec(expr)

class CraftState:
    NoneState               = 0x00

    Physical                = 0x01
    PhysicalForce           = 0x02
    Arts                    = 0x03

    Poison                  = 0x04
    Frozen                  = 0x05
    Burning                 = 0x06
    BanCraft                = 0x07
    BanMagic                = 0x08
    Darkness                = 0x09
    Sleep                   = 0x0A
    Confusion               = 0x0B
    Stun                    = 0x0D
    Petrifaction            = 0x0E

    OnehitKill              = 0x0F
    Vanish                  = 0x10
    ATDelay                 = 0x11
    InterruptMagicAria      = 0x12
    Fat                     = 0x13

    LeechHP                 = 0x16
    LeechEP                 = 0x17
    LeechCP                 = 0x18
    DamageToHP              = 0x19
    DamageToEP              = 0x1A
    HPHeal                  = 0x1B
    EPHeal                  = 0x1C
    CPHeal                  = 0x1D

    HealPoison              = 0x1E
    HealFrozen              = 0x1F
    HealBurning             = 0x20
    HealBanCraft            = 0x21
    HealBanMagic            = 0x22
    HealDarkness            = 0x23
    HealSleep               = 0x24
    HealConfusion           = 0x25
    HealStun                = 0x26
    HealPetrifaction        = 0x27

    Stealth                 = 0x38
    CraftGuard              = 0x39
    ArtsGuard               = 0x3A
    ArtsReflection          = 0x3B
    Guard                   = 0x3C

    QueryMonsterInfo        = 0x50

CraftStateNames = {}

for attr in dir(CraftState):
    if attr[:2] == '__' and attr[-2:] == '__':
        continue

    expr = 'CraftStateNames[0x%X] = "CraftState.%s"' % (getattr(CraftState, attr), attr)
    exec(expr)


CUSTOM_CRAFT_INDEX_BASE = 0x3E8

class BattleCraftInfo:

    # size = 0x18

    def __init__(self, index = 0, fs = None):

        if fs == None:
            return

        self.Index                  = CUSTOM_CRAFT_INDEX_BASE + index
        self.ActionIndex            = fs.ushort()   # 0x00
        self.Target                 = fs.byte()     # 0x02       # in fact, this is an ushort
        self.Unknown_3              = fs.byte()     # 0x03
        self.Attribute              = fs.byte()     # 0x04
        self.RangeType              = fs.byte()     # 0x05       # CraftRange
        self.State1                 = fs.byte()     # 0x06       # CraftState
        self.State2                 = fs.byte()     # 0x07       # CraftState
        self.RNG                    = fs.byte()     # 0x08
        self.RangeSize              = fs.byte()     # 0x09
        self.AriaTime               = fs.byte()     # 0x0A
        self.SkillTime              = fs.byte()     # 0x0B
        self.EP_CP                  = fs.ushort()   # 0x0C
        self.Unknown_0E             = fs.ushort()   # 0x0E
        self.State1Parameter        = fs.ushort()   # 0x10      e.g. damage factor
        self.State1Time             = fs.ushort()   # 0x12      e.g. frozen AT
        self.State2Parameter        = fs.ushort()   # 0x14
        self.State2Time             = fs.ushort()   # 0x16

        self.Name = fs.astr()
        self.Description = fs.astr()

    def param(self):
        return '"%s", "%s", 0x%02X, 0x%X, 0x%X, %s, %s, %s, %s, %d, %d, %d, %d, %d, 0x%X, 0x%04X, %d, 0x%04X, %d' % (
                    self.Name,
                    self.Description,
                    self.ActionIndex,
                    self.Target,
                    self.Unknown_3,
                    CraftAttributeNames[self.Attribute],
                    CraftRangeNames[self.RangeType],
                    CraftStateNames[self.State1],
                    CraftStateNames[self.State2],
                    self.RNG,
                    self.RangeSize,
                    self.AriaTime,
                    self.SkillTime,
                    self.EP_CP,
                    self.Unknown_0E,
                    self.State1Parameter,
                    self.State1Time,
                    self.State2Parameter,
                    self.State2Time
                )

__CreatedCraftNumber__ = 0
__Craft_List__ = []

def CreateCraft(
        Name,
        Description,
        ActionIndex,
        Target,
        Unknown_3,
        Attribute,
        RangeType,
        State1,
        State2,
        RNG,
        RangeSize,
        AriaTime,
        SkillTime,
        EP_CP,
        Unknown_0E,
        State1Parameter,
        State1Time,
        State2Parameter,
        State2Time
    ):

    global __CreatedCraftNumber__

    info = BattleCraftInfo()

    info.Name               = Name
    info.Description        = Description
    info.Index              = __CreatedCraftNumber__ + CUSTOM_CRAFT_INDEX_BASE
    info.ActionIndex        = ActionIndex
    info.Target             = Target
    info.Unknown_3          = Unknown_3
    info.Attribute          = Attribute
    info.RangeType          = RangeType
    info.State1             = State1
    info.State2             = State2
    info.RNG                = RNG
    info.RangeSize          = RangeSize
    info.AriaTime           = AriaTime
    info.SkillTime          = SkillTime
    info.EP_CP              = EP_CP
    info.Unknown_0E         = Unknown_0E
    info.State1Parameter    = State1Parameter
    info.State1Time         = State1Time
    info.State2Parameter    = State2Parameter
    info.State2Time         = State2Time

    __Craft_List__.append(info)

    __CreatedCraftNumber__ += 1

    return info

class BattleCraftAIInfo:

    # size = 0x18:

    def __init__(self, fs = None):

        if fs == None:
            return

        self.Condition                  = fs.byte()
        self.Probability                = fs.byte()
        self.Target                     = fs.byte()
        self.TargetCondition            = fs.byte()
        self.MagicAriaActionIndex       = fs.byte()
        self.ActionIndex                = fs.byte()
        self.CraftIndex                 = fs.ushort()
        self.Parameter                  = [0] * 4

        for i in range(len(self.Parameter)):
            self.Parameter[i] = fs.ulong()

    def param(self):
        return '0x%X, %d, 0x%X, 0x%X, 0x%02X, 0x%02X, 0x%04X, [0x%08X, 0x%08X, 0x%08X, 0x%08X]' % (
                    self.Condition, self.Probability, self.Target, self.TargetCondition,
                    self.MagicAriaActionIndex, self.ActionIndex, self.CraftIndex,
                    self.Parameter[0], self.Parameter[1], self.Parameter[2], self.Parameter[3]
                )

__AI_List__ = []

def CreateAI(Condition, Probability, Target, TargetCondition, MagicAriaActionIndex, ActionIndex, CraftIndex, Parameters):
    if type(Parameters) != tuple and type(Parameters) != list:
        raise Exception('Parameters must be list or tuple')

    if len(Parameters) > 4:
        Parameters = Parameters[:4]
    elif len(Parameters) < 4:
        Parameters += (4 - len(Parameters)) * [0]

    ai = BattleCraftAIInfo()

    ai.Condition                = Condition
    ai.Probability              = Probability
    ai.Target                   = Target
    ai.TargetCondition          = TargetCondition
    ai.MagicAriaActionIndex     = MagicAriaActionIndex
    ai.ActionIndex              = ActionIndex
    ai.CraftIndex               = CraftIndex
    ai.Parameter                = Parameters

    __AI_List__.append(ai)

    return ai

class BattleMonsterScriptInfo:

    def __init__(self):

        self.ASFile                 = BattleScriptFileIndex()

        self.Level                  = 0                     # 0x04

        self.MaximumHP              = 0                     # 0x06
        self.InitialHP              = 0                     # 0x0A
        self.MaximumEP              = 0                     # 0x0E
        self.InitialEP              = 0                     # 0x10
        self.MaximumCP              = 0                     # 0x12
        self.InitialCP              = 0                     # 0x14

        self.SPD                    = 0                     # 0x16
        self.MoveSPD                = 0                     # 0x18
        self.MOV                    = 0                     # 0x1A
        self.STR                    = 0                     # 0x1C
        self.DEF                    = 0                     # 0x1E
        self.ATS                    = 0                     # 0x20
        self.ADF                    = 0                     # 0x22
        self.DEX                    = 0                     # 0x24
        self.AGL                    = 0                     # 0x26
        self.RNG                    = 0                     # 0x28

        self.Unknown_2A             = 0                     # 0x2A
        self.EXP                    = 0                     # 0x2C  (Target.Level - self.Level) * EXP
        self.Unknown_2E             = 0                     # 0x2E
        self.Unknown_30             = 0                     # 0x30
        self.AIType                 = 0                     # 0x31  00 01 02 10 13 14 FF
        self.Unknown_33             = 0                     # 0x33
        self.Unknown_35             = 0                     # 0x35
        self.Unknown_36             = 0                     # 0x36  ignore ?
        self.EnemyFlags             = 0                     # 0x38  0x10: enemy  0x40: self
        self.BattleFlags            = 0                     # 0x3A  0x04    死后留在战场上
                                                            #       0x0800  抵抗 ATDelay
                                                            #       0x0200  不被击退
                                                            #       0x0100  被攻击不转身(3D)
        self.Unknown_3C             = 0                     # 0x3C
        self.Unknown_3E             = 0                     # 0x3E
        self.Sex                    = 0                     # 0x40  1: male     0: female
        self.Unknown_41             = 0                     # 0x41
        self.Unknown_42             = 0                     # 0x42
        self.Unknown_46             = 0                     # 0x46
        self.CharSize               = 0                     # 0x4A  / 2 / 400
        self.Unknown_4E             = 0                     # 0x4E
        self.Unknown_52             = 0                     # 0x52
        self.Unknown_53             = 0                     # 0x53
        self.Unknown_54             = 0                     # 0x54
        self.Unknown_55             = 0                     # 0x55
        self.Symbol            = SymbolFileIndex(0)    # 0x56
        self.Resistance             = 0                     # 0x5A  异常状态抵抗
        self.AttributeRate          = [0] * 7               # 0x5E  USHORT [7]
        self.Sepith                 = [0] * 7               # 0x6C  BYTE [7]
        self.DropItem               = [0] * 2               # 0x73  USHORT [2]
        self.DropRate               = [0] * 2               # 0x77  BYTE[2]
        self.Equipment              = [0] * 5               # 0x79
        self.Orbment                = [0] * 4               # 0x83

        self.Attack                 = BattleCraftAIInfo()   # 0x8B
        self.MagicNumber            = 0                     # 0x8B + sizeof(BattleCraftAIInfo), BYTE
        self.Magic                  = []                    # MagicNumber * BattleCraftAIInfo
        self.CraftNumber            = 0
        self.Craft                  = []
        self.SCraftNumber           = 0
        self.SCraft                 = []
        self.SupportCraftNumber     = 0
        self.SupportCraft           = []
        self.CraftInfoNumber        = 0
        self.CraftInfo              = []

        self.RunawayType            = 0                     # BYTE  0, 1, 2, 3
        self.RunawayRate            = 0                     # BYTE  percent
        self.RunawayParam1          = 0                     # BYTE
        self.Reserve1               = 0                     # BYTE

        self.Name            = ''
        self.Description     = ''


    def open(self, msfilename):

        fs = BytesStream()
        fs.open(msfilename)

        self.ASFile                 = BattleScriptFileIndex(fs.ulong())

        self.Level                  = fs.ushort()

        self.MaximumHP              = fs.ulong()
        self.InitialHP              = fs.ulong()
        self.MaximumEP              = fs.ushort()
        self.InitialEP              = fs.ushort()
        self.MaximumCP              = fs.ushort()
        self.InitialCP              = fs.ushort()

        self.SPD                    = fs.ushort()
        self.MoveSPD                = fs.ushort()
        self.MOV                    = fs.ushort()
        self.STR                    = fs.ushort()
        self.DEF                    = fs.ushort()
        self.ATS                    = fs.ushort()
        self.ADF                    = fs.ushort()
        self.DEX                    = fs.ushort()
        self.AGL                    = fs.ushort()
        self.RNG                    = fs.ushort()

        self.Unknown_2A             = fs.ushort()
        self.EXP                    = fs.ushort()
        self.Unknown_2E             = fs.ushort()
        self.Unknown_30             = fs.byte()
        self.AIType                 = fs.ushort()
        self.Unknown_33             = fs.ushort()
        self.Unknown_35             = fs.byte()
        self.Unknown_36             = fs.ushort()
        self.EnemyFlags             = fs.ushort()
        self.BattleFlags            = fs.ushort()
        self.Unknown_3C             = fs.ushort()
        self.Unknown_3E             = fs.ushort()

        self.Sex                    = fs.byte()
        self.Unknown_41             = fs.byte()
        self.Unknown_42             = fs.ulong()
        self.Unknown_46             = fs.ulong()
        self.CharSize               = fs.ulong()
        self.Unknown_4E             = fs.ulong()
        self.Unknown_52             = fs.byte()
        self.Unknown_53             = fs.byte()
        self.Unknown_54             = fs.byte()
        self.Unknown_55             = fs.byte()

        self.Symbol            = SymbolFileIndex(fs.ulong())
        self.Resistance             = fs.ulong()
        self.AttributeRate          = struct.unpack('<HHHHHHH', fs.read(2 * 7))
        self.Sepith                 = list(fs.read(7))
        self.DropItem               = [ fs.ushort(), fs.ushort() ]
        self.DropRate               = list(fs.read(2))
        self.Equipment              = struct.unpack('<HHHHH', fs.read(2 * 5))
        self.Orbment                = struct.unpack('<HHHH', fs.read(2 * 4))

        self.Attack                 = BattleCraftAIInfo(fs)

        self.MagicNumber = fs.byte()
        for i in range(self.MagicNumber):
            self.Magic.append(BattleCraftAIInfo(fs))

        self.CraftNumber = fs.byte()
        for i in range(self.CraftNumber):
            self.Craft.append(BattleCraftAIInfo(fs))

        self.SCraftNumber = fs.byte()
        for i in range(self.SCraftNumber):
            self.SCraft.append(BattleCraftAIInfo(fs))

        self.SupportCraftNumber = fs.byte()
        for i in range(self.SupportCraftNumber):
            self.SupportCraft.append(BattleCraftAIInfo(fs))

        index = 0
        self.CraftInfoNumber = fs.byte()
        for i in range(self.CraftInfoNumber):
            info = BattleCraftInfo(index, fs)
            self.CraftInfo.append(info)
            index += 1

        self.RunawayType            = fs.byte()
        self.RunawayRate            = fs.byte()
        self.RunawayParam1          = fs.byte()
        self.Reserve1               = fs.byte()

        self.Name                   = fs.astr()
        self.Description            = fs.astr()

    def SaveTo(self, filename):
        lines = []
        header = []

        def add(l):
            lines.append(l)

        def fmtlist(l, fmt = '%d'):
            tmp = []
            for rate in l:
                tmp.append(fmt % rate)

            return ', '.join(tmp)

        header.append('from %s import *' % os.path.splitext(os.path.basename(__file__))[0])
        header.append('')
        header.append('def main():')

        add('Name               = "%s"' % self.Name.replace('\\', '\\\\'))
        add('Description        = "%s"' % self.Description.replace('\\', '\\\\'))
        add('ASFile             = "%s"' % self.ASFile.Name())
        add('Symbol             = "%s"' % self.Symbol.Name())
        add('')
        add('Level              = %d' % self.Level)
        add('MaximumHP          = %d' % self.MaximumHP)
        add('InitialHP          = %d' % self.InitialHP)
        add('MaximumEP          = %d' % self.MaximumEP)
        add('InitialEP          = %d' % self.InitialEP)
        add('MaximumCP          = %d' % self.MaximumCP)
        add('InitialCP          = %d' % self.InitialCP)
        add('')
        add('SPD                = %d' % self.SPD)
        add('MoveSPD            = %d' % self.MoveSPD)
        add('MOV                = %d' % self.MOV)
        add('STR                = %d' % self.STR)
        add('DEF                = %d' % self.DEF)
        add('ATS                = %d' % self.ATS)
        add('ADF                = %d' % self.ADF)
        add('DEX                = %d' % self.DEX)
        add('AGL                = %d' % self.AGL)
        add('RNG                = %d' % self.RNG)
        add('')
        add('Unknown_2A         = 0x%X' % self.Unknown_2A)
        add('EXP                = %d' % self.EXP)
        add('Unknown_2E         = 0x%X' % self.Unknown_2E)
        add('Unknown_30         = 0x%X' % self.Unknown_30)
        add('AIType             = 0x%X' % self.AIType)
        add('Unknown_33         = 0x%X' % self.Unknown_33)
        add('Unknown_35         = 0x%X' % self.Unknown_35)
        add('Unknown_36         = 0x%X' % self.Unknown_36)
        add('EnemyFlags         = 0x%04X' % self.EnemyFlags)
        add('BattleFlags        = 0x%04X' % self.BattleFlags)
        add('')
        add('Unknown_3C         = 0x%X' % self.Unknown_3C)
        add('Unknown_3E         = 0x%X' % self.Unknown_3E)
        add('Sex                = %d' % self.Sex)
        add('Unknown_41         = 0x%X' % self.Unknown_41)
        add('Unknown_42         = 0x%X' % self.Unknown_42)
        add('Unknown_46         = 0x%X' % self.Unknown_46)
        add('CharSize           = %d' % self.CharSize)
        add('Unknown_4E         = 0x%X' % self.Unknown_4E)
        add('Unknown_52         = 0x%X' % self.Unknown_52)
        add('Unknown_53         = 0x%X' % self.Unknown_53)
        add('Unknown_54         = 0x%X' % self.Unknown_54)
        add('Unknown_55         = 0x%X' % self.Unknown_55)
        add('Resistance         = 0x%08X' % self.Resistance)
        add('AttributeRate      = [ %s ]' % fmtlist(self.AttributeRate))
        add('Sepith             = [ %s ]' % fmtlist(self.Sepith))
        add('DropItem           = [ %s ]' % fmtlist(self.DropItem, '0x%04X'))
        add('DropRate           = [ %s ]' % fmtlist(self.DropRate))
        add('Equipment          = [ %s ]' % fmtlist(self.Equipment, '0x%04X'))
        add('Orbment            = [ %s ]' % fmtlist(self.Orbment, '0x%04X'))
        add('')
        add('RunawayType        = %d' % self.RunawayType)
        add('RunawayRate        = %d' % self.RunawayRate)
        add('RunawayParam1      = %d' % self.RunawayParam1)
        add('Reserve1           = %d' % self.Reserve1)
        add('')

        def fmtai(ai):
            s = 'CreateAI(%s)' % ai.param()
            return s.replace(', 0x%04X, ' % ai.CraftIndex, ', Creaft_%04X.Index, ' % ai.CraftIndex)

        def fmtcraft(cft):
            return 'CreateCraft(%s)' % cft.param()

        def gencraft(craftlist):
            for craft in craftlist:
                #name = craft.Name
                #if name == '' or name == ' ':
                name = '%04X' % craft.Index

                add('Creaft_%s = %s' % (name, fmtcraft(craft)))

        def genai(prefix, ailist):
            index = 0
            for ai in ailist:
                add('%s_AI_%d = %s' % (prefix, index, fmtai(ai)))
                index += 1

        add('Crafts = []')
        gencraft(self.CraftInfo)
        add('')
        genai('Magic', self.Magic)
        genai('Craft', self.Craft)
        genai('SCraft', self.SCraft)
        genai('SupportCraft', self.SupportCraft)

        add('')
        add('SaveToMS("%s", locals())' % (os.path.splitext(filename)[0] + '.dat'))

        for l in lines:
            if l != '':
                l = '    ' + l
            header.append(l)

        header.append('')
        header.append('TryInvoke(main)')

        open(filename, 'wb').write('\r\n'.join(header).encode('utf_8_sig'))

    def __str__(self):

        l = []
        l.append('Level             = %d' % self.Level)
        l.append('HP                = %d / %d' % (self.InitialHP, self.MaximumHP))
        l.append('EP                = %d / %d' % (self.InitialEP, self.MaximumEP))
        l.append('CP                = %d / %d' % (self.InitialCP, self.MaximumCP))
        l.append('')
        l.append('SPD               = %d' % self.SPD)
        l.append('MoveSPD           = %d' % self.MoveSPD)
        l.append('MOV               = %d' % self.MOV)
        l.append('STR               = %d' % self.STR)
        l.append('DEF               = %d' % self.DEF)
        l.append('ATS               = %d' % self.ATS)
        l.append('ADF               = %d' % self.ADF)
        l.append('DEX               = %d' % self.DEX)
        l.append('AGL               = %d' % self.AGL)
        l.append('RNG               = %d' % self.RNG)
        l.append('')
        l.append('EXP               = %d' % self.EXP)
        l.append('AIType            = %X' % self.AIType)
        l.append('Resistance        = %08X' % self.Resistance)
        l.append('AttributeRate     = %d, %d, %d, %d, %d, %d, %d' % (self.AttributeRate[0], self.AttributeRate[1], self.AttributeRate[2], self.AttributeRate[3], self.AttributeRate[4], self.AttributeRate[5], self.AttributeRate[6]))
        l.append('Sepith            = %d, %d, %d, %d, %d, %d, %d' % (self.Sepith[0], self.Sepith[1], self.Sepith[2], self.Sepith[3], self.Sepith[4], self.Sepith[5], self.Sepith[6]))
        l.append('DropItem          = %04X (%d), %04X (%d)' % (self.DropItem[0], self.DropRate[0], self.DropItem[1], self.DropRate[1]))
        l.append('Equipment         = %04X, %04X, %04X, %04X, %04X' % (self.Equipment[0], self.Equipment[1], self.Equipment[2], self.Equipment[3], self.Equipment[4]))
        l.append('Orbment           = %04X, %04X, %04X, %04X' % (self.Orbment[0], self.Orbment[1], self.Orbment[2], self.Orbment[3]))

        l.append('')
        l.append('%s' % self.Name)
        l.append('%s' % self.Description)
        l.append('')
        l.append('%s' % self.ASFile.Name())
        l.append('%s' % self.Symbol.Name())
        l.append('')

        l.append('CraftInfo: %d' % self.CraftInfoNumber)
        for cftinfo in self.CraftInfo:
            l.append('    %s: %s' % (cftinfo.Name, cftinfo.Description))

        return '\r\n'.join(l)

def SaveToMS(filename, locals):
    pass

def main():
    if len(sys.argv) < 2:
        return

    ms = BattleMonsterScriptInfo()
    f = sys.argv[1]
    ms.open(f)
    ms.SaveTo(os.path.splitext(f)[0] + '.py')

TryInvoke(main)
