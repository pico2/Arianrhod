#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker, "/SECTION:.Amano,ERW /MERGE:.text=.Amano")

#include "MyLibrary.h"

_ML_C_HEAD_

NTSTATUS
NTAPI
FmsInitializeEnumerator(
    IN  PFMS_HANDLE Handle,
    IN  ULONG       Flags
)
{
    return 0;
}

NTSTATUS
NTAPI
FmsFreeEnumerator(
    IN OUT PFMS_HANDLE Handle
)
{
    return 0;
}

NTSTATUS
NTAPI
FmsSetFilter(
    IN  FMS_HANDLE          Handle,
    IN  PFMS_FILTER_DATA    FilterData,
    IN  ULONG               NumberOfFilterData
)
{
    return 0;
}

NTSTATUS
NTAPI
FmsGetFilteredPropertyList(
    IN      FMS_HANDLE  Handle,
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
    IN  FMS_HANDLE  Handle,
    OUT PULONG      NumberOfFonts,
    OUT PULONG      FontIdList OPTIONAL
)
{
    return 0;
}

NTSTATUS
NTAPI
FmsGetGDILogFont(
    IN  FMS_HANDLE          Handle,
    IN  ULONG               FontId,
    IN  BOOLEAN             What,
    OUT LPENUMLOGFONTEXW    LogFont,
    OUT PTEXTMETRICW        TextMetric OPTIONAL
)
{
    return 0;
}

NTSTATUS
NTAPI
FmsGetGdiLogicalFont(
    IN  FMS_HANDLE          Handle,
    IN  ULONG               FontId,
    IN  BOOLEAN             What,
    OUT LPENUMLOGFONTEXW    LogFont,
    OUT PTEXTMETRICW        TextMetric  OPTIONAL,
    OUT PULONG              SomeBuffer  OPTIONAL
)
{
    return 0;
}

NTSTATUS
NTAPI
FmsGetFontProperty(
    IN      FMS_HANDLE  Handle,
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
    IN  FMS_HANDLE          Handle,
    IN  ULONG               ReservedZero,
    IN  PCWSTR              FaceName,
    OUT PULONG              FontId
){return 0;}


_ML_C_TAIL_
