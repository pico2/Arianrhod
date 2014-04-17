#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker, "/SECTION:.Amano,ERW /MERGE:.text=.Amano")

#include "MyLibrary.h"

_ML_C_HEAD_

NTSTATUS
NTAPI
FmsSetDefaultFilter(
    IN FMS_ENUMERATOR Enumerator
)
{
    return 0;
}

NTSTATUS
NTAPI
FmsResetEnumerator(
    IN FMS_ENUMERATOR Enumerator
)
{
    return 0;
}

NTSTATUS
NTAPI
FmsMapGdiLogicalFont(
    IN  FMS_ENUMERATOR      Enumerator,
    IN  ULONG               FontId,
    OUT LPENUMLOGFONTEXW    EnumLogFontEx
)
{
    return 0;
}

NTSTATUS
NTAPI
FmsInitializeEnumerator(
    IN  PFMS_ENUMERATOR Handle,
    IN  ULONG       Flags
)
{
    return 0;
}

NTSTATUS
NTAPI
FmsFreeEnumerator(
    IN OUT PFMS_ENUMERATOR Handle
)
{
    return 0;
}

NTSTATUS
NTAPI
FmsSetFilter(
    IN  FMS_ENUMERATOR          Handle,
    IN  PFMS_FILTER_DATA    FilterData,
    IN  ULONG               NumberOfFilterData
)
{
    return 0;
}

NTSTATUS
NTAPI
FmsAddFilter(
    IN  FMS_ENUMERATOR      Enumerator,
    IN  PFMS_FILTER_DATA    FilterData,
    IN  ULONG               NumberOfFilterData
)
{
    return 0;
}

NTSTATUS
NTAPI
FmsGetFilteredPropertyList(
    IN      FMS_ENUMERATOR  Handle,
    IN      ULONG       PropertyType,
    OUT     PULONG      NumberofProperty,
    IN OUT  PULONG      PropertySize,
    OUT     PVOID       Property    OPTIONAL
)
{
    return 0;
}

NTSTATUS
NTAPI
FmsGetFilteredFontList(
    IN  FMS_ENUMERATOR  Handle,
    OUT PULONG      NumberOfFonts,
    OUT PULONG      FontIdList OPTIONAL
)
{
    return 0;
}

NTSTATUS
NTAPI
FmsGetGDILogFont(
    IN  FMS_ENUMERATOR      Handle,
    IN  ULONG               FontId,
    IN  BOOLEAN             What,
    OUT LPENUMLOGFONTEXW    LogFont,
    OUT PFMS_TEXTMETRIC     TextMetric OPTIONAL
)
{
    return 0;
}

NTSTATUS
NTAPI
FmsGetGdiLogicalFont(
    IN  FMS_ENUMERATOR      Enumerator,
    IN  ULONG               FontId,
    IN  BOOLEAN             WhatTrue,
    OUT LPENUMLOGFONTEXW    EnumLogFontEx,
    OUT PFMS_TEXTMETRIC     FmsTextMetric  OPTIONAL,
    OUT PULONG              SomeBuffer  OPTIONAL
)
{
    return 0;
}

NTSTATUS
NTAPI
FmsGetFontProperty(
    IN      FMS_ENUMERATOR  Handle,
    IN      ULONG       FontId,
    IN      ULONG       PropertyType,
    IN OUT  PULONG      PropertySize,
    IN OUT  PVOID       PropertyBuffer
)
{
    return 0;
}

NTSTATUS
NTAPI
FmsGetBestMatchInFamily(
    IN  FMS_ENUMERATOR          Handle,
    IN  ULONG               ReservedZero,
    IN  PCWSTR              FaceName,
    OUT PULONG              FontId
){return 0;}


_ML_C_TAIL_
