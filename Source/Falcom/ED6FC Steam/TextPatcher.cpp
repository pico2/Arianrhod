#include "ed6fc.h"

using ml::String;

NTSTATUS PatchAllReference(PVOID startAddress, ULONG_PTR searchRange, PVOID textVa, PCSTR newText, ULONG_PTR length)
{
    PVOID endAddress;
    PBYTE reference;

    SEARCH_PATTERN_DATA stub[] =
    {
        ADD_PATTERN(&textVa),
    };

    endAddress = PtrAdd(startAddress, searchRange);

    while (startAddress < endAddress)
    {
        reference = (PBYTE)SearchPattern(stub, countof(stub), startAddress, PtrOffset(endAddress, startAddress));
        if (reference == nullptr)
            break;

        // mov r32, const
        // push const
        if ((reference[-1] & 0xF0) == 0xB0 || reference[-1] == 0x68)
        {
            *(PCSTR *)reference = newText;
        }

        startAddress = reference + sizeof(PVOID);
    }

    return STATUS_SUCCESS;
}

NTSTATUS InitializeTextPatcher(PVOID BaseAddress)
{
    NTSTATUS        status;
    ULONG           count, protection;
    PBYTE           buffer;
    PVOID           startAddress;
    ULONG_PTR       searchRange;
    NtFileMemory*   textbin;

    auto textSection = IMAGE_FIRST_SECTION(ImageNtHeadersFast(BaseAddress));

    startAddress = PtrAdd(BaseAddress, textSection->VirtualAddress);
    searchRange = textSection->Misc.VirtualSize;

    status = Mm::ProtectMemory(CurrentProcess, startAddress, searchRange, PAGE_EXECUTE_READWRITE, &protection);
    FAIL_RETURN(status);

    SCOPE_EXIT
    {
        Mm::ProtectMemory(CurrentProcess, startAddress, searchRange, protection);
    }
    SCOPE_EXIT_END;

    textbin = new NtFileMemory();
    if (textbin == nullptr)
        return STATUS_NO_MEMORY;

    status = textbin->Open(L"ed6fc.text");
    if (NT_FAILED(status))
    {
        delete textbin;
        return status;
    }

    buffer = (PBYTE)textbin->GetBuffer();

    count = *(PULONG)buffer;
    buffer += sizeof(count);

    while (count--)
    {
        ULONG_PTR rva, length;
        
        rva = *(PULONG)buffer;
        buffer += sizeof(ULONG);

        length = *(PUSHORT)buffer;
        buffer += sizeof(USHORT);

        if (rva & 0x80000000)
        {
            *(PVOID *)PtrAdd(BaseAddress, rva & 0x7FFFFFFF) = buffer;
        }
        else
        {
            status = PatchAllReference(
                        startAddress,
                        searchRange,
                        PtrAdd(BaseAddress, rva),
                        (PCSTR)buffer,
                        length
                    );
        }

        buffer += length;
    }

    return status;
}
