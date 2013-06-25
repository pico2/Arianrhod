#ifndef _MLSTRING_H_252d9413_55ca_4d44_976f_c0dcecd5afd4_
#define _MLSTRING_H_252d9413_55ca_4d44_976f_c0dcecd5afd4_

#include "MyLibrary.h"

class StringImplement
{
public:
    typedef USHORT          STRING_LENGTH_TYPE;
    typedef ULONG_PTR       LARGE_LENGTH_TYPE;
    typedef UNICODE_STRING  STRING_TYPE;
    typedef PWSTR           STRING_POINTER_TYPE;
    typedef PCWSTR          STRING_CONST_POINTER_TYPE;

    static const STRING_LENGTH_TYPE kMaxLength  = 0xFFFF;
    static const LARGE_LENGTH_TYPE  kCharSize   = sizeof(WCHAR);

    friend class String;

protected:

    STRING_TYPE String;
    WCHAR       Buffer[1];

public:
    StringImplement()
    {
        Reset();
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

    NoInline NTSTATUS CopyFrom(STRING_CONST_POINTER_TYPE Str, LARGE_LENGTH_TYPE Count)
    {
        FAIL_RETURN(VerifyBufferLength(Count));
        CopyString(Str, Count);
        return STATUS_SUCCESS;
    }

    NoInline NTSTATUS Concat(STRING_CONST_POINTER_TYPE Str, LARGE_LENGTH_TYPE Count)
    {
        FAIL_RETURN(VerifyBufferLength(GetCount() + Count));
        CopyString(Str, Count);
        return STATUS_SUCCESS;
    }

protected:
    static ForceInline LARGE_LENGTH_TYPE CountToLength(LARGE_LENGTH_TYPE Count)
    {
        return Count * kCharSize;
    }

    static ForceInline LARGE_LENGTH_TYPE CountToLengthAddNull(LARGE_LENGTH_TYPE Count)
    {
        return Count * kCharSize + kCharSize;
    }

    static LARGE_LENGTH_TYPE GetStringCount(STRING_CONST_POINTER_TYPE Str)
    {
        return StrLengthW(Str);
    }

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

    NoInline VOID CopyString(STRING_CONST_POINTER_TYPE Str, LARGE_LENGTH_TYPE Count)
    {
        LARGE_LENGTH_TYPE Length;

        if (Count == 0)
            return;

        Length = CountToLength(Count);
        CopyMemory(GetBuffer() + GetCount(), Str, Length);
        this->String.Length += Length;
        AddNull();
    }

    VOID Reset()
    {
        RtlInitEmptyString(&this->String);
    }

    VOID SetBuffer(STRING_POINTER_TYPE Buffer, LARGE_LENGTH_TYPE MaximumLength)
    {
        this->String.Buffer         = Buffer;
        this->String.Length         = 0;
        this->String.MaximumLength  = (STRING_LENGTH_TYPE)MaximumLength;
    }

    VOID AddNull()
    {
        *PtrAdd(GetBuffer(), GetLength()) = 0;
    }

    VOID CopyBuffer(StringImplement *Impl)
    {
        CopyString(Impl->GetBuffer(), Impl->GetCount());
    }
};


class String
{
protected:
    typedef StringImplement::STRING_LENGTH_TYPE             STRING_LENGTH_TYPE;
    typedef StringImplement::LARGE_LENGTH_TYPE              LARGE_LENGTH_TYPE;
    typedef StringImplement::STRING_TYPE                    STRING_TYPE;
    typedef StringImplement::STRING_POINTER_TYPE            STRING_POINTER_TYPE;
    typedef StringImplement::STRING_CONST_POINTER_TYPE      STRING_CONST_POINTER_TYPE;

    static const STRING_LENGTH_TYPE     kMaxLength      = StringImplement::kMaxLength;
    static const STRING_LENGTH_TYPE     kCharSize       = StringImplement::kCharSize;
    static const ULONG_PTR              kStringImplSize = FIELD_SIZE(StringImplement, String);

    friend String operator+(const String& str, String::STRING_CONST_POINTER_TYPE StrToAppend);

    StringImplement::STRING_POINTER_TYPE Buffer;

public:
    String()
    {
        Reset();
        *this = L"";
    }

    String(const String& Str)
    {
        Reset();
        *this = Str;
    }

    String(STRING_CONST_POINTER_TYPE Str)
    {
        Reset();
        *this = Str;
    }

    ~String()
    {
        ReleaseBuffer();
    }

    NoInline String& operator=(STRING_CONST_POINTER_TYPE Str)
    {
        CopyFrom(Str);
        return *this;
    }

    NoInline String& operator=(const String& Str)
    {
        if (this == &Str)
            return *this;

        CopyFrom(Str.Buffer, Str.GetCount());

        return *this;
    }

    NoInline String operator+(String::STRING_CONST_POINTER_TYPE Str)
    {
        return String(*this) += Str;
    }

    NoInline String operator+(const String& Str)
    {
        return String(*this) += Str;
    }

    NoInline String& operator+=(STRING_CONST_POINTER_TYPE Str)
    {
        return Concat(Str);
    }

    NoInline String& operator+=(const String& Str)
    {
        return Concat(Str);
    }

    String& Concat(STRING_CONST_POINTER_TYPE Str)
    {
        return Concat(Str, StringImplement::GetStringCount(Str));
    }

    String& Concat(const String& Str)
    {
        StringImplement *Impl = Str.GetImplement();
        return Concat(Impl->GetBuffer(), Impl->GetCount());
    }

    String& Concat(STRING_CONST_POINTER_TYPE Str, LARGE_LENGTH_TYPE Count)
    {
        NTSTATUS Status;

        Status = ResizeBuffer(GetCount() + Count);
        if (NT_FAILED(Status))
            return *this;

        GetImplement()->Concat(Str, Count);

        return *this;
    }

    LARGE_LENGTH_TYPE GetCount() const
    {
        return GetImplement()->GetCount();
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
        return FreeMemoryP(Impl) ? STATUS_SUCCESS : STATUS_UNSUCCESSFUL;
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
        LARGE_LENGTH_TYPE   Length;
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

            if (OldImpl->GetMaxLength() >= Length)
                return STATUS_SUCCESS;
        }

        Length = StringImplement::CountToLengthAddNull(Count);
        Impl = (StringImplement *)AllocateMemoryP(kStringImplSize + Length);
        if (Impl == NULL)
            return STATUS_NO_MEMORY;

        Impl->SetBuffer(Impl->Buffer, Length);

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

    NTSTATUS CopyFrom(STRING_CONST_POINTER_TYPE Str, LARGE_LENGTH_TYPE Count)
    {
        NTSTATUS Status;

        Status = ResizeBuffer(Count);
        FAIL_RETURN(Status);

        return GetImplement()->CopyFrom(Str, Count);
    }
};

#endif // _MLSTRING_H_252d9413_55ca_4d44_976f_c0dcecd5afd4_
