from ScenarioType import *

class ScenarioInfoPort(ScenarioInfo):
    def __init__(self):
        super().__init__()

        self.fs = None
        self.Labels = []        # list of LabelEntry

scena = ScenarioInfoPort()

'''


        self.MapName                    = ''
        self.Location                   = ''
        self.Unknown_14                 = 0
        self.Flags                      = 0
        self.IncludedScenario           = []
        self.NpcNameOffset              = 0
        self.ScnInfoOffset              = []
        self.ScenaFunctionTable         = ScenarioEntry()
        self.UnknownEntry_46            = ScenarioEntry()
        self.Unknown_4A                 = 0
        self.PreInitSectionIndex        = 0
        self.ScnInfoNumber              = []
        self.Unknown_51                 = b''
        self.Information                = b''

'''

def CreateScenaFile(MapName, Location, Unknown_14, Flags, IncludeList, Unknown_4A, PreInitSectionIndex, Unknown_51, Information):
    scena.MapName               = MapName
    scena.Location              = Location
    scena.Unknown_14            = Unknown_14
    scena.Flags                 = Flags
    scena.IncludedScenario      = IncludeList
    scena.Unknown_4A            = Unknown_4A
    scena.PreInitSectionIndex   = PreInitSectionIndex
    scena.Unknown_51            = Unknown_51
    scena.Information           = Information

    scena.fs = open(MapName + '.bin2', 'wb+')
    scena.fs.seek(0x94)


def Npc(X, Y, Z, Unknown1, Unknown2, Unknown, InitScenaIndex, InitSectionIndex, TalkScenaIndex, TalkSectionIndex, Unknown4, Unknown5):

    chrinfo = ScenarioCharInformation()

    chrinfo.X                  = X
    chrinfo.Y                  = Y
    chrinfo.Z                  = Z
    chrinfo.Unknown1           = Unknown1
    chrinfo.Unknown2           = Unknown2
    chrinfo.Unknown            = Unknown
    chrinfo.InitScenaIndex     = InitScenaIndex
    chrinfo.InitSectionIndex   = InitSectionIndex
    chrinfo.TalkScenaIndex     = TalkScenaIndex
    chrinfo.TalkSectionIndex   = TalkSectionIndex
    chrinfo.Unknown4           = Unknown4
    chrinfo.Unknown5           = Unknown5

    if len(scena.ScnInfo[SCN_INFO_NPC_POSITION]) == 0:
        scena.ScnInfoOffset[SCN_INFO_NPC_POSITION] = scena.fs.tell()

    scena.ScnInfo[SCN_INFO_NPC_POSITION].append(chrinfo)

    scena.fs.write(chrinfo.binary())

def ScpFunction(FunctionLabel):
    scena.ScenaFunctions.append(FunctionLabel)
    scena.fs.write(struct.pack('<I', 0xFFFFFFFF))

def label(labelname):
    scena.Labels.append(LabelEntry(labelname, scena.fs.tell()))
