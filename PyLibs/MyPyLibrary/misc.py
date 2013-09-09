'''

ForceInline ULONG HashAPI(PCChar pszName)
{
    ULONG Hash = 0;

    while (*(PByte)pszName)
    {
        Hash = _rotl(Hash, 0x0D) ^ *(PByte)pszName++;
    }

    return Hash;
}


'''


def RoundDown(Value, Multiple):
    return type(Value)(type(Value)(Value / Multiple) * Multiple)

def RoundUp(Value, Multiple):
    return RoundDown(Value + Multiple - 1, Multiple)

def rol32(val, shift):
    val &= 0xFFFFFFFF
    return ((val << shift) | (val >> (32 - shift))) & 0xFFFFFFFF

def ror32(val, shift):
    val &= 0xFFFFFFFF
    return ((val >> shift) | (val << (32 - shift))) & 0xFFFFFFFF

def HashAPI(str):
    hash = 0
    for ch in str:
        hash = rol32(hash, 0xD) ^ ord(ch)

    return hash & 0xFFFFFFFF
