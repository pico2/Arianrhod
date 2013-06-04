#pragma comment(lib, "gdiplus.lib")

#include "edao.h"
#include <GdiPlus.h>

/************************************************************************
  EDAO
************************************************************************/

BOOL EDAO::CheckItemEquipped(ULONG ItemId, PULONG EquippedIndex)
{
    switch (ItemId)
    {
        case 0xB7:  // ú—Ä¿
        case 0xB8:  // ÌìÑÛ
        case 0xBB:  // Ì½Öª
            if (EquippedIndex != NULL)
                *EquippedIndex = 0;

            return TRUE;
    }

    return (this->*StubCheckItemEquipped)(ItemId, EquippedIndex);
}


/************************************************************************
  CScript
************************************************************************/

NAKED VOID CScript::NakedInheritSaveData()
{
    INLINE_ASM
    {
        mov     dword ptr [eax + 82BB4h], 0;
        lea     edx, dword ptr [ebp - 0x26454 + 0x1B008];
        mov     ecx, [ebp - 0Ch];
        jmp     CScript::InheritSaveData
    }
}

VOID FASTCALL CScript::InheritSaveData(PBYTE ScenarioFlags)
{
    ULONG_PTR CustomOffset[] =
    {
        0x212,
    };

    PULONG_PTR Offset;

    FOR_EACH(Offset, CustomOffset, countof(CustomOffset))
    {
        *(PBYTE)PtrAdd(this, 0x9C + *Offset) = ScenarioFlags[*Offset];
    }
}

BOOL THISCALL CScript::ScpSaveRestoreParty(PSCENA_ENV_BLOCK Block)
{
    BOOL   Result, NeedRefreshFA;
    USHORT Chr[8];

    enum { Save = 1, Restore = 2 };

    NeedRefreshFA = GetScenaTable()[Block->ScenaIndex][Block->CurrentOffset + 1] == Restore &&
                    RtlCompareMemory(GetActor()->GetPartyListSaved(), GetActor()->GetPartyList(), sizeof(Chr)) != sizeof(Chr);

    Result = (this->*StubScpSaveRestoreParty)(Block);

    if (NeedRefreshFA)
        GetEDAO()->LoadFieldAttackData();

    return Result;
}

/************************************************************************
  misc
************************************************************************/

VOID FASTCALL LoadSaveDataThumbFast(Gdiplus::Bitmap *bitmap, PBYTE RGBBuffer, PBYTE AlphaBuffer, LONG_PTR Stride)
{
    using namespace Gdiplus;

    PBYTE       RawBuffer;
    LONG_PTR    Width, Height;
    COLORREF    Color;
    BitmapData  bitmapData;

    Width = bitmap->GetWidth();
    Height = bitmap->GetHeight();

    Rect rect(0, 0, Width, Height);

    bitmap->LockBits(&rect, ImageLockModeRead, PixelFormat32bppARGB, &bitmapData);

    RawBuffer = (PBYTE)bitmapData.Scan0;
    Stride *= 3;

    for (LONG_PTR h = Height; h; --h)
    {
        PBYTE buf, rgb, alpha;

        buf = RawBuffer;
        rgb = RGBBuffer;
        alpha = AlphaBuffer;

        for (LONG_PTR w = Width; w; --w)
        {
            Color = *(LPCOLORREF)buf;

            rgb[0] = GetRValue(Color);
            rgb[1] = GetGValue(Color);
            rgb[2] = GetBValue(Color);

            alpha[0] = Color >> 24;
            alpha[1] = Color >> 24;
            alpha[2] = Color >> 24;

            buf     += 4;
            rgb     += 3;
            alpha   += 3;
        }

        RawBuffer   += bitmapData.Stride;
        RGBBuffer   += Stride;
        AlphaBuffer += Stride;
    }

    bitmap->UnlockBits(&bitmapData);
}

NAKED VOID EDAO::NakedLoadSaveDataThumb()
{
    INLINE_ASM
    {
        mov     edx, dword ptr [ebp - 0x350];
        push    dword ptr [ebp - 0x234];
        push    dword ptr [ebp - 0x35C];

        call    LoadSaveDataThumbFast
        or      eax, -1;
        ret;
    }
}

VOID FASTCALL SetSaveDataScrollStep(ULONG_PTR RetryCount)
{
    PBOOLEAN ScrollUp10             = (PBOOLEAN)0xDCFA15;
    PBOOLEAN ScrollDown10           = (PBOOLEAN)0xDCFA16;

    PBOOLEAN ScrollUp100            = (PBOOLEAN)0xDCFA1F;
    PBOOLEAN ScrollDown100          = (PBOOLEAN)0xDCFA20;

    PLONG   SaveDataToReadUp        = (PLONG)0xDCF9F8;
    PLONG   SaveDataToReadDown      = (PLONG)0xDCF9F4;

    PLONG   CurrentSaveDataIndex    = (PLONG)0xDCDFD0;
    PLONG   MaximumSaveDataIndex    = (PLONG)0xDCDFFC;

    PLONG   KeyPressCount           = (PLONG)0xDCDFDC;

    LONG MaximumSaveDataToRead = 10;
    LONG Extra = 0;

    static ULONG64 PressTimestamp;

    LOOP_ONCE
    {
        if (*ScrollUp100 | *ScrollUp10)
        {
            if (*CurrentSaveDataIndex == 0)
                continue;

            switch (*SaveDataToReadUp)
            {
                case 10:
                case 100:
                    break;

                default:
                    continue;
            }

            PressTimestamp = NtGetTickCount();

            *CurrentSaveDataIndex = ML_MAX(*CurrentSaveDataIndex - *SaveDataToReadUp, 0) + MaximumSaveDataToRead + Extra;
            *SaveDataToReadUp = MaximumSaveDataToRead + Extra;
            continue;
        }

        if (*ScrollDown100 | *ScrollDown10)
        {
            if (*CurrentSaveDataIndex == *MaximumSaveDataIndex - 1)
                continue;

            switch (*SaveDataToReadDown)
            {
                case 10:
                case 100:
                    break;

                default:
                    continue;
            }

            PressTimestamp = NtGetTickCount();

            *CurrentSaveDataIndex = ML_MIN(*CurrentSaveDataIndex + *SaveDataToReadDown, *MaximumSaveDataIndex - 1) - MaximumSaveDataToRead - Extra;
            *SaveDataToReadDown = MaximumSaveDataToRead + Extra;
            continue;
        }

        return;
    }

    if (RetryCount == 0 && NtGetTickCount() - PressTimestamp > 150)
        *KeyPressCount = 0;
}

NAKED VOID EDAO::NakedSetSaveDataScrollStep()
{
    INLINE_ASM
    {
        mov     dword ptr [ebp-0x174], eax;
        mov     ecx, dword ptr [ebp-0x24]
        jmp     SetSaveDataScrollStep
    }
}
