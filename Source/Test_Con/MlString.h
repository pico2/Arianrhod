#ifndef _MLSTRING_H_252d9413_55ca_4d44_976f_c0dcecd5afd4_
#define _MLSTRING_H_252d9413_55ca_4d44_976f_c0dcecd5afd4_

#include "MyLibrary.h"

#define STRING_DEBUG 0
#define USE_TEMPLATE 1

template<typename STRING_LENGTH_TYPE = USHORT, typename LARGE_LENGTH_TYPE = ULONG>
class StringImplementT
{
protected:

    typedef typename STRING_LENGTH_TYPE STRING_LENGTH_TYPE;
    typedef typename LARGE_LENGTH_TYPE  LARGE_LENGTH_TYPE;

    typedef WCHAR           STRING_CHAR_TYPE;
    typedef PWSTR           STRING_POINTER_TYPE;
    typedef PCWSTR          STRING_CONST_POINTER_TYPE;

#if USE_TEMPLATE

#include "MlPackOn.h"

    typedef struct STRING_TYPE
    {
        STRING_LENGTH_TYPE  Length;
        STRING_LENGTH_TYPE  MaximumLength;
        STRING_POINTER_TYPE Buffer;

    } STRING_TYPE, *PSTRING_TYPE;

    typedef const STRING_TYPE* PCSTRING_TYPE;

#include "MlPackOff.h"

#else

    typedef UNICODE_STRING      STRING_TYPE;
    typedef PUNICODE_STRING     PSTRING_TYPE;
    typedef PCUNICODE_STRING    PCSTRING_TYPE;

#endif

    static const LARGE_LENGTH_TYPE  kInvalidIndex   = ~0u;
    static const LARGE_LENGTH_TYPE  kCharSize       = sizeof(STRING_CHAR_TYPE);
    static const LARGE_LENGTH_TYPE  kMaxLength      = ((LARGE_LENGTH_TYPE)1 << bitsof(STRING_LENGTH_TYPE)) - 1 - kCharSize;

#if USE_TEMPLATE
    template<typename, typename>
#endif

    friend class StringT;

protected:

    STRING_TYPE         String;
    STRING_CHAR_TYPE    Buffer[4];

protected:
    StringImplementT()
    {
        Reset();
    }

    VOID Reset()
    {
        RtlInitEmptyString(&this->String);
    }

    operator PCSTRING_TYPE()
    {
        return &this->String;
    }

    operator PSTRING_TYPE()
    {
        return &this->String;
    }

    LONG Compare(StringImplementT *Impl, BOOL CaseInSensitive = FALSE)
    {
        return Compare(*Impl, CaseInSensitive);
    }

    LONG Compare(STRING_CONST_POINTER_TYPE Str, LARGE_LENGTH_TYPE Count, BOOL CaseInSensitive = FALSE)
    {
        STRING_TYPE String;

        String.Buffer           = (STRING_POINTER_TYPE)Str;
        String.Length           = (STRING_LENGTH_TYPE)CountToLength(Count);
        String.MaximumLength    = String.Length;

        return Compare(&String, CaseInSensitive);
    }

    LONG Compare(PCSTRING_TYPE Str, BOOL CaseInSensitive = FALSE)
    {
        UNICODE_STRING Str1, Str2;

        Str1.Length         = GetLength();
        Str1.MaximumLength  = Str1.Length;
        Str1.Buffer         = GetBuffer();

        Str2.Length         = Str->Length;
        Str2.MaximumLength  = Str->MaximumLength;
        Str2.Buffer         = Str->Buffer;

        return RtlCompareUnicodeString(&Str1, &Str2, CaseInSensitive);
    }

    NoInline NTSTATUS Concat(STRING_CONST_POINTER_TYPE Str, LARGE_LENGTH_TYPE Count)
    {
        FAIL_RETURN(VerifyBufferLength(GetCount() + Count));
        CopyString(Str, Count, TRUE);
        return STATUS_SUCCESS;
    }

    NoInline NTSTATUS CopyFrom(STRING_CONST_POINTER_TYPE Str, LARGE_LENGTH_TYPE Count)
    {
        FAIL_RETURN(VerifyBufferLength(Count));
        CopyString(Str, Count, FALSE);
        return STATUS_SUCCESS;
    }

    LARGE_LENGTH_TYPE FormatCountV(STRING_CONST_POINTER_TYPE Format, va_list Arguments)
    {
        return _vscwprintf(Format, Arguments);
    }

    LARGE_LENGTH_TYPE FormatV(STRING_CONST_POINTER_TYPE Format, va_list Arguments)
    {
        LARGE_LENGTH_TYPE Count;

        Count = _vsnwprintf(GetBuffer(), LengthToCount(GetMaxLength()), Format, Arguments);
        this->String.Length = CountToLength(Count);

        return Count;
    }

    LARGE_LENGTH_TYPE GetLength()
    {
        return this->String.Length;
    }

    LARGE_LENGTH_TYPE GetMaxLength()
    {
        return this->String.MaximumLength;
    }

    LARGE_LENGTH_TYPE GetCount()
    {
        return GetLength() / kCharSize;
    }

    STRING_POINTER_TYPE GetBuffer()
    {
        return this->String.Buffer;
    }

    LARGE_LENGTH_TYPE IndexOf(STRING_CONST_POINTER_TYPE Str, LARGE_LENGTH_TYPE StartIndex = 0)
    {
        if (StartIndex >= GetCount())
            return kInvalidIndex;

        STRING_CONST_POINTER_TYPE Begin, End, Found;

        Begin = GetBuffer();
        End = PtrAdd(GetBuffer(), GetLength());

        Found = wcsstr(Begin + StartIndex, Str);

        return Found == NULL ? kInvalidIndex : Found - Begin;
    }

    BOOL IsNullOrEmpty()
    {
        return GetCount() == 0;
    }

    LARGE_LENGTH_TYPE LastIndexOf(STRING_CONST_POINTER_TYPE Str, LARGE_LENGTH_TYPE StartIndex = 0)
    {
        if (StartIndex >= GetCount())
            return kInvalidIndex;

        STRING_CONST_POINTER_TYPE Begin, End, Found, Prev;

        Begin = GetBuffer();
        End = PtrAdd(GetBuffer(), GetLength());

        Prev = NULL;
        Begin += StartIndex;
        while (Begin < End)
        {
            Found = wcsstr(Begin, Str);
            if (Found == NULL)
                break;

            Prev = Found;
            Begin = Found + 1;
        }

        return Prev == NULL ? kInvalidIndex : Prev - GetBuffer();
    }

    VOID ToLower()
    {
        StringLowerW(GetBuffer(), GetCount());
    }

    VOID ToUpper()
    {
        StringUpperW(GetBuffer(), GetCount());
    }


    /************************************************************************
      internal
    ************************************************************************/

    NTSTATUS VerifyBufferLength(LARGE_LENGTH_TYPE Count)
    {
        LARGE_LENGTH_TYPE Length;

        Length = CountToLength(Count);

        if (Length > kMaxLength)
            return STATUS_NAME_TOO_LONG;

        if (Length >= this->String.MaximumLength)
            return STATUS_BUFFER_TOO_SMALL;

        return STATUS_SUCCESS;
    }

    NoInline VOID CopyString(STRING_CONST_POINTER_TYPE Str, LARGE_LENGTH_TYPE Count, BOOL Concat)
    {
        LARGE_LENGTH_TYPE Length;

        if (!Concat)
        {
            this->String.Length = 0;
            AddNull();
        }

        if (Count == 0)
            return;

        Length = CountToLength(Count);
        CopyMemory(GetBuffer() + GetCount(), Str, Length);
        this->String.Length += Length;
        AddNull();
    }

    VOID SetBuffer(STRING_POINTER_TYPE Buffer, LARGE_LENGTH_TYPE MaximumLength)
    {
        this->String.Buffer         = Buffer;
        this->String.Length         = 0;
        this->String.MaximumLength  = (STRING_LENGTH_TYPE)MaximumLength;

        GetBuffer()[0] = 0;
    }

    VOID AddNull()
    {
        *PtrAdd(GetBuffer(), GetLength()) = 0;
    }

    VOID CopyBuffer(StringImplementT *Impl)
    {
        CopyString(Impl->GetBuffer(), Impl->GetCount(), FALSE);
    }


    static ForceInline LARGE_LENGTH_TYPE CountToLength(LARGE_LENGTH_TYPE Count)
    {
        return Count * kCharSize;
    }

    static ForceInline LARGE_LENGTH_TYPE CountToLengthAddNull(LARGE_LENGTH_TYPE Count)
    {
        return Count * kCharSize + kCharSize;
    }

    static ForceInline LARGE_LENGTH_TYPE LengthToCount(LARGE_LENGTH_TYPE Length)
    {
        return Length / kCharSize;
    }

    static LARGE_LENGTH_TYPE GetStringCount(STRING_CONST_POINTER_TYPE Str)
    {
        return StrLengthW(Str);
    }
};


//typedef StringImplementT<> StringImplement;

#if USE_TEMPLATE
template<typename STRING_LENGTH_TYPE = USHORT, typename LARGE_LENGTH_TYPE = ULONG>
#endif

class StringT
{
protected:

    typedef StringImplementT<> StringImplement;

    typedef StringImplement::STRING_LENGTH_TYPE             STRING_LENGTH_TYPE;
    typedef StringImplement::LARGE_LENGTH_TYPE              LARGE_LENGTH_TYPE;

    typedef StringImplement::STRING_CHAR_TYPE               STRING_CHAR_TYPE;
    typedef StringImplement::STRING_TYPE                    STRING_TYPE;
    typedef StringImplement::STRING_POINTER_TYPE            STRING_POINTER_TYPE;
    typedef StringImplement::STRING_CONST_POINTER_TYPE      STRING_CONST_POINTER_TYPE;

    static const LARGE_LENGTH_TYPE  kInvalidIndex   = StringImplement::kInvalidIndex;
    static const LARGE_LENGTH_TYPE  kMaxLength      = StringImplement::kMaxLength;
    static const LARGE_LENGTH_TYPE  kCharSize       = StringImplement::kCharSize;
    static const ULONG_PTR          kStringImplSize = sizeof(StringImplement) - FIELD_SIZE(StringImplement, Buffer);

    StringImplement::STRING_POINTER_TYPE Buffer;

public:
    StringT()
    {
        Reset();
        *this = L"";
    }

    StringT(const StringT& Str)
    {
        Reset();
        *this = Str;
    }

    StringT(STRING_CONST_POINTER_TYPE Str)
    {
        Reset();
        *this = Str;
    }

    StringT(STRING_CHAR_TYPE Chr)
    {
        STRING_CHAR_TYPE Buffer[2];

        Reset();

        Buffer[0] = Chr;
        Buffer[1] = 0;

        *this = Buffer;
    }

    NoInline ~StringT()
    {
        ReleaseBuffer();

#if STRING_DEBUG
        this->Buffer = (STRING_POINTER_TYPE)0xFFEEDDCC;
#endif

    }

    LARGE_LENGTH_TYPE GetCount() const
    {
        return GetImplement()->GetCount();
    }

    STRING_POINTER_TYPE GetBuffer() const
    {
        return GetImplement()->GetBuffer();
    }

    operator STRING_POINTER_TYPE() const
    {
        return GetBuffer();
    }

    operator STRING_CONST_POINTER_TYPE() const
    {
        return GetBuffer();
    }

    NoInline StringT& operator=(STRING_CONST_POINTER_TYPE Str)
    {
        CopyFrom(Str);
        return *this;
    }

    NoInline StringT& operator=(const StringT& Str)
    {
        if (this == &Str)
            return *this;

        CopyFrom(Str.Buffer, Str.GetCount());

        return *this;
    }

    NoInline BOOL operator==(STRING_CONST_POINTER_TYPE Str)
    {
        return Compare(Str) == 0;
    }

    NoInline BOOL operator==(const StringT& Str)
    {
        return Compare(Str.GetBuffer(), Str.GetCount()) == 0;
    }

    NoInline StringT operator+(STRING_CONST_POINTER_TYPE Str)
    {
        return StringT(*this) += Str;
    }

    NoInline StringT operator+(const StringT& Str)
    {
        return StringT(*this) += Str;
    }

    NoInline StringT& operator+=(STRING_CHAR_TYPE Chr)
    {
        STRING_CHAR_TYPE Buffer[2];

        Buffer[0] = Chr;
        Buffer[1] = 0;

        return Concat(Buffer, 1);
    }

    NoInline StringT& operator+=(STRING_CONST_POINTER_TYPE Str)
    {
        return Concat(Str);
    }

    NoInline StringT& operator+=(const StringT& Str)
    {
        return Concat(Str);
    }

    STRING_CHAR_TYPE& operator[](LARGE_LENGTH_TYPE Index)
    {
        //if (Index >= GetCount()) Index = 0;
        return GetBuffer()[Index];
    }

    LONG Compare(STRING_CONST_POINTER_TYPE Str, BOOL CaseInSensitive = FALSE)
    {
        return GetImplement()->Compare(Str, StringImplement::GetStringCount(Str), CaseInSensitive);
    }

    LONG Compare(STRING_CONST_POINTER_TYPE Str, LARGE_LENGTH_TYPE Count, BOOL CaseInSensitive = FALSE)
    {
        return GetImplement()->Compare(Str, Count, CaseInSensitive);
    }

    StringT& Concat(STRING_CONST_POINTER_TYPE Str)
    {
        return Concat(Str, StringImplement::GetStringCount(Str));
    }

    StringT& Concat(const StringT& Str)
    {
        StringImplement *Impl = Str.GetImplement();
        return Concat(Impl->GetBuffer(), Impl->GetCount());
    }

    StringT& Concat(STRING_CONST_POINTER_TYPE Str, LARGE_LENGTH_TYPE Count)
    {
        NTSTATUS Status;

        Status = ResizeBuffer(GetCount() + Count);
        if (NT_FAILED(Status))
            return *this;

        GetImplement()->Concat(Str, Count);

        return *this;
    }

    NoInline StringT Copy()
    {
        return StringT(*this);
    }

    NoInline static StringT Format(STRING_CONST_POINTER_TYPE format, ...)
    {
        va_list Arguments;
        va_start(Arguments, format);
        return FormatV(format, Arguments);
    }

    NoInline static StringT FormatV(STRING_CONST_POINTER_TYPE Format, va_list Arguments)
    {
        NTSTATUS    Status;
        StringT      NewString;

        Status = NewString.ResizeBuffer(NewString.GetImplement()->FormatCountV(Format, Arguments));
        if (NT_FAILED(Status))
            return NewString;

        NewString.GetImplement()->FormatV(Format, Arguments);
        return NewString;
    }

    NoInline LARGE_LENGTH_TYPE IndexOf(STRING_CHAR_TYPE Chr, LARGE_LENGTH_TYPE StartIndex = 0)
    {
        STRING_CHAR_TYPE Buffer[2];

        Buffer[0] = Chr;
        Buffer[1] = 0;

        return IndexOf(Buffer, StartIndex);
    }

    NoInline LARGE_LENGTH_TYPE IndexOf(STRING_CONST_POINTER_TYPE Str, LARGE_LENGTH_TYPE StartIndex = 0)
    {
        return GetImplement()->IndexOf(Str, StartIndex);
    }

    NoInline BOOL IsNullOrEmpty()
    {
        return GetImplement() == NULL ? TRUE : GetImplement()->IsNullOrEmpty();
    }

    NoInline LARGE_LENGTH_TYPE LastIndexOf(STRING_CHAR_TYPE Chr, LARGE_LENGTH_TYPE StartIndex = 0)
    {
        STRING_CHAR_TYPE Buffer[2];

        Buffer[0] = Chr;
        Buffer[1] = 0;

        return LastIndexOf(Buffer, StartIndex);
    }

    NoInline LARGE_LENGTH_TYPE LastIndexOf(STRING_CONST_POINTER_TYPE Str, LARGE_LENGTH_TYPE StartIndex = 0)
    {
        return GetImplement()->LastIndexOf(Str, StartIndex);
    }

    NoInline StringT PadLeft(LARGE_LENGTH_TYPE TotalWidth, STRING_CHAR_TYPE PaddingChar = ' ')
    {
        NTSTATUS            Status;
        StringT              Padded = *this;
        LARGE_LENGTH_TYPE   LengthToPad;

        if (TotalWidth <= Padded.GetCount())
            return Padded;

        LengthToPad = TotalWidth - Padded.GetCount();
        Status = Padded.ResizeBuffer(TotalWidth);
        if (NT_FAILED(Status))
            return Padded;

        Padded = L"";

        for (; LengthToPad; --LengthToPad)
            Padded += PaddingChar;

        Padded += *this;

        return Padded;
    }

    NoInline StringT PadRight(LARGE_LENGTH_TYPE TotalWidth, STRING_CHAR_TYPE PaddingChar = ' ')
    {
        NTSTATUS            Status;
        StringT              Padded = *this;
        LARGE_LENGTH_TYPE   LengthToPad;

        if (TotalWidth <= Padded.GetCount())
            return Padded;

        LengthToPad = TotalWidth - Padded.GetCount();
        Status = Padded.ResizeBuffer(TotalWidth);
        if (NT_FAILED(Status))
            return Padded;

        for (; LengthToPad; --LengthToPad)
            Padded += PaddingChar;

        return Padded;
    }

    NoInline StringT Remove(LARGE_LENGTH_TYPE StartIndex, LARGE_LENGTH_TYPE Count = kInvalidIndex)
    {
        NTSTATUS            Status;
        StringT              NewString;
        StringImplement*    Impl;
        LARGE_LENGTH_TYPE   TailLength;

        if (StartIndex >= GetCount() || StartIndex == 0)
            return NewString;

        if (Count == kInvalidIndex || StartIndex + Count >= GetCount())
            Count = GetCount() - StartIndex;

        TailLength = GetCount() - (StartIndex + Count);

        Status = NewString.ResizeBuffer(StartIndex + TailLength);
        if (NT_FAILED(Status))
            return NewString;

        Impl = NewString.GetImplement();
        Impl->CopyFrom(GetBuffer(), StartIndex);
        Impl->Concat(GetBuffer() + StartIndex + Count, TailLength);

        return NewString;
    }

    NoInline StringT Replace(const StringT& OldValue, const StringT& NewValue)
    {
        return ReplaceWorker(OldValue, OldValue.GetCount(), NewValue, NewValue.GetCount());
    }

    NoInline StringT Replace(STRING_CONST_POINTER_TYPE OldValue, STRING_CONST_POINTER_TYPE NewValue)
    {
        return ReplaceWorker(OldValue, StringImplement::GetStringCount(OldValue), NewValue, StringImplement::GetStringCount(NewValue));
    }

    NoInline StringT Replace(STRING_CHAR_TYPE OldValue, STRING_CHAR_TYPE NewValue)
    {
        STRING_CHAR_TYPE Old[2], New[2];

        Old[0] = OldValue;
        Old[1] = 0;
        New[0] = NewValue;
        New[1] = 0;

        return ReplaceWorker(Old, 1, New, 1);
    }

    NoInline StringT SubString(LARGE_LENGTH_TYPE StartIndex, LARGE_LENGTH_TYPE Count = kInvalidIndex)
    {
        StringT NewString;

        if (StartIndex >= GetCount())
            return NewString;

        if (Count == kInvalidIndex || StartIndex + Count >= GetCount())
            Count = GetCount() - StartIndex;

        NewString.CopyFrom(GetBuffer() + StartIndex, Count);

        return NewString;
    }

    NoInline StringT ToLower()
    {
        StringT NewString = *this;
        NewString.GetImplement()->ToLower();
        return NewString;
    }

    NoInline StringT ToUpper()
    {
        StringT NewString = *this;
        NewString.GetImplement()->ToUpper();
        return NewString;
    }

    NoInline StringT TrimEnd(StringT TrimChars)
    {
        STRING_POINTER_TYPE Begin, End;

        Begin = GetBuffer();
        End = Begin + GetCount();

        while (End > Begin)
        {
            if (TrimChars.IndexOf(End[-1]) == kInvalidIndex)
                break;

            --End;
        }

        if (End <= Begin)
            return StringT();

        return SubString(0, End - Begin);
    }

    NoInline StringT TrimStart(StringT TrimChars)
    {
        STRING_POINTER_TYPE Begin, End;

        Begin = GetBuffer();
        End = Begin + GetCount();

        while (Begin != End)
        {
            if (TrimChars.IndexOf(Begin[0]) == kInvalidIndex)
                break;

            ++Begin;
        }

        if (Begin == End)
            return StringT();

        return SubString(Begin - GetBuffer());
    }

    NoInline StringT Trim(StringT TrimChars)
    {
        return TrimStart(TrimChars).TrimEnd(TrimChars);
    }

protected:
    StringImplement* GetImplement() const
    {
        return this->Buffer == NULL ? NULL : FIELD_BASE(this->Buffer, StringImplement, Buffer);
    }

    VOID SetImplement(StringImplement *Impl)
    {
        this->Buffer = Impl->Buffer;
    }

    VOID Reset()
    {
        this->Buffer = NULL;
    }

    NTSTATUS ReleaseImplement(StringImplement *Impl)
    {
        return FreeMemory(Impl) ? STATUS_SUCCESS : STATUS_UNSUCCESSFUL;
    }

    NTSTATUS ReleaseBuffer()
    {
        StringImplement* Impl = GetImplement();

        ReleaseImplement(Impl);
        Reset();

        return STATUS_SUCCESS;
    }

    NTSTATUS AllocateBuffer(LARGE_LENGTH_TYPE Count)
    {
        return ResizeBuffer(Count);
    }

    NTSTATUS ResizeBuffer(LARGE_LENGTH_TYPE Count)
    {
        LARGE_LENGTH_TYPE   Length, MaxLength;
        STRING_TYPE         Buffer;
        StringImplement     *Impl, *OldImpl;

        Length = StringImplement::CountToLength(Count);
        if (Length > kMaxLength)
            return STATUS_NAME_TOO_LONG;

        OldImpl = GetImplement();

        LOOP_ONCE
        {
            if (OldImpl == NULL)
                break;

            if (OldImpl->GetMaxLength() > Length)
                return STATUS_SUCCESS;
        }

        Length = StringImplement::CountToLengthAddNull(Count);
        MaxLength = ROUND_UP(Length * 3 / 2, kCharSize);
        Impl = (StringImplement *)AllocateMemory(kStringImplSize + MaxLength);
        if (Impl == NULL)
            return STATUS_NO_MEMORY;

        Impl->SetBuffer(Impl->Buffer, MaxLength);

        if (OldImpl != NULL)
        {
            Impl->CopyBuffer(OldImpl);
            ReleaseImplement(OldImpl);
        }

        SetImplement(Impl);

        return STATUS_SUCCESS;
    }

    NTSTATUS CopyFrom(STRING_CONST_POINTER_TYPE Str)
    {
        return CopyFrom(Str, StringImplement::GetStringCount(Str));
    }

    NoInline NTSTATUS CopyFrom(STRING_CONST_POINTER_TYPE Str, LARGE_LENGTH_TYPE Count)
    {
        NTSTATUS Status;

        Status = ResizeBuffer(Count);
        FAIL_RETURN(Status);

        return GetImplement()->CopyFrom(Str, Count);
    }

    StringT
    ReplaceWorker(
        STRING_CONST_POINTER_TYPE   OldValue,
        LARGE_LENGTH_TYPE           OldCount,
        STRING_CONST_POINTER_TYPE   NewValue,
        LARGE_LENGTH_TYPE           NewCount
    )
    {
        StringT                      NewString;
        LARGE_LENGTH_TYPE           StartIndex, Sub;
        STRING_CONST_POINTER_TYPE   Base, Begin, End;
        StringImplement*            Impl;

        Impl = GetImplement();

        Base        = GetBuffer();
        Begin       = Base;
        End         = Begin + GetCount();
        StartIndex  = 0;

        while (Begin < End)
        {
            Sub = Impl->IndexOf(OldValue, StartIndex);
            if (Sub == kInvalidIndex)
                break;

            if (StartIndex != Sub)
                NewString.Concat(Base + StartIndex, Sub - StartIndex);

            NewString.Concat(NewValue, NewCount);

            StartIndex = Sub + OldCount;
            Begin = Base + StartIndex;
        }

        if (Begin < End)
            NewString.Concat(Begin, End - Begin);

        return NewString;
    }

private:
    PVOID AllocateMemory(ULONG_PTR Size)
    {

#if STRING_DEBUG
        ++DebugAllocCount;
#endif

        return AllocateMemoryP(Size);
    }

    BOOL FreeMemory(PVOID Memory)
    {

#if STRING_DEBUG
        --DebugAllocCount;
        if (DebugAllocCount < 0)
            RtlRaiseException(0);
#endif

        return FreeMemoryP(Memory);
    }


#if STRING_DEBUG
    static LONG_PTR DebugAllocCount;
#endif
};

#if STRING_DEBUG

DECL_SELECTANY LONG_PTR StringT::DebugAllocCount = 0;

#endif

#if USE_TEMPLATE

    typedef StringT<> String;
    typedef StringT<ULONG, ULONG64> LargeString;

#else

    typedef StringT String;

#endif


#endif // _MLSTRING_H_252d9413_55ca_4d44_976f_c0dcecd5afd4_
