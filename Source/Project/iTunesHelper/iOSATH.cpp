#include "stdafx.h"

using namespace iTunesApi::ATH;

iOSATH::iOSATH(iOSDevice& device) : device(device)
{
    this->Connection = nullptr;
    this->Flags = 0;
}

iOSATH::~iOSATH()
{
    this->Disconnect();
}

NTSTATUS iOSATH::Connect()
{
    if (this->Connection != nullptr)
        return kAMDSuccess;

    NTSTATUS Status;
    auto Udid = CFSTR(device.GetUniqueDeviceID().Encode(CP_UTF8));

    this->LibraryID = CFSTR(GetLibraryID().Encode(CP_UTF8));
    DebugLog(L"GetLibraryID done");

    this->Connection = ATHostConnectionCreateWithLibrary(
                            this->LibraryID,
                            Udid,
                            nullptr
                        );

    if (this->Connection == nullptr)
        return kAMDNotConnectedError;

    this->ReadThreadHandle = nullptr;
    this->Exiting = FALSE;
    Status = Ps::CreateThread(StaticReadMessageThread, this, FALSE, CurrentProcess, &this->ReadThreadHandle);
    if (NT_FAILED(Status))
        return Status;

    return kAMDSuccess;
}

NTSTATUS iOSATH::Disconnect()
{
    if (this->Connection == nullptr)
        return kAMDNotConnectedError;

    this->Exiting = TRUE;
    this->Ping();

    NtWaitForSingleObject(this->ReadThreadHandle, FALSE, nullptr);
    NtClose(this->ReadThreadHandle);

    ATHostConnectionDestroy(this->Connection);
    this->Connection = nullptr;

    return kAMDSuccess;
}

ULONG iOSATH::GetGrappaSessionId()
{
    return ATHostConnectionGetGrappaSessionId(*this);
}

ULONG iOSATH::ReadMessageThread()
{
    static struct
    {
        PCSTR Name;
        VOID (iOSATH::*Handler)(CFPropertyList message);
    } MessageNameTable[] =
    {
        { "InstalledAssets",    &iOSATH::HandleInstalledAssets },
        { "SyncAllowed",        &iOSATH::HandleSyncAllowed },
        { "RequestingSync",     &iOSATH::HandleRequestingSync },
        { "ReadyForSync",       &iOSATH::HandleReadyForSync },
        { "SyncFinished",       &iOSATH::HandleSyncFinished },
        { "AssetManifest",      nullptr },
        { "SyncFailed",         &iOSATH::HandleSyncFailed },
        { "Progress",           nullptr },
        { "Ping",               nullptr },
        { "FileError",          nullptr },
    };

    while (this->Exiting == FALSE)
    {
        CFPropertyList message = ATHostConnectionReadMessage(this->Connection);

        if (message == nullptr)
            break;

        CFStringRef name = ATCFMessageGetName(message);

        auto entry = &MessageNameTable[0];

        {
            //CFDataRef data = CFPropertyListCreateXMLData(nullptr, message);
            //NtFileDisk f; f.Append(L"D:\\Desktop\\log.xml"); f.Write(CFDataGetBytePtr(data), CFDataGetLength(data));
        }

        DebugLog(L"%S\n", CFStringGetCStringPtr(name, kCFStringEncodingWindowsLatin1));

        FOR_EACH(entry, entry, countof(MessageNameTable))
        {
            if (CFEqual(name, CFSTR(entry->Name)))
            {
                if (entry->Handler != nullptr)
                {
                    (this->*entry->Handler)(message);
                }

                break;
            }
        }
    }

    this->ConnectionBroken = TRUE;
    return 0;
}

VOID iOSATH::HandleInstalledAssets(CFPropertyList Message)
{
    ;
}

VOID iOSATH::HandleSyncAllowed(CFPropertyList Message)
{
    this->SyncAllowed = TRUE;
}

VOID iOSATH::HandleRequestingSync(CFPropertyList Message)
{
    ;
}

VOID iOSATH::HandleReadyForSync(CFPropertyList Message)
{
    //CFDataRef data = CFPropertyListCreateXMLData(nullptr, Message);
    //PrintConsole(L"%.*S\n\n", CFDataGetLength(data), CFDataGetBytePtr(data));
    //DebugBreakPoint();

    this->ReadyForSync = TRUE;
}

VOID iOSATH::HandleSyncFinished(CFPropertyList Message)
{
    this->SyncFinished = TRUE;
}

VOID iOSATH::HandleSyncFailed(CFPropertyList Message)
{
    this->SyncFailed = TRUE;
}

NTSTATUS iOSATH::SendPowerAssertion(BOOL Enabled)
{
    return ATHostConnectionSendPowerAssertion(this->Connection, Enabled ? *kCFBooleanTrue : *kCFBooleanFalse);
}

NTSTATUS iOSATH::Ping()
{
    return ATHostConnectionSendPing(this->Connection);
}

NTSTATUS iOSATH::SendSyncRequest()
{
    CFList Dataclasses;
    CFList SyncedDataclasses;
    CFDict DataclassAnchors;
    CFDict HostInfo;

    int Weakable = 0;

    //Dataclasses.AppendValue(CFSTR("Media"));
    //Dataclasses.AppendValue(CFSTR("Book"));
    Dataclasses.AppendValue(CFSTR("Keybag"));
    Dataclasses.AppendValue(CFSTR("Data"));

    SyncedDataclasses.AppendValue(CFSTR("Data"));

    HostInfo.SetValue(CFSTR("LibraryID"), LibraryID);
    HostInfo.SetValue(CFSTR("SyncHostName"), CFSTR("OUROBOROS"));
    HostInfo.SetValue(CFSTR("SyncedDataclasses"), SyncedDataclasses);
    HostInfo.SetValue(CFSTR("Version"), CFSTR("12.0.1.71"));
    HostInfo.SetValue(CFSTR("Wakeable"), CFNumberCreate(nullptr, kCFNumberIntType, &Weakable));

    DataclassAnchors.SetValue(CFSTR("Media"), CFSTR("0"));

    return ATHostConnectionSendSyncRequest(this->Connection, Dataclasses, DataclassAnchors, HostInfo);
}

NTSTATUS iOSATH::SendSyncFinished()
{
    CFDict Dataclasses;
    CFDict DataclassAnchors;
    int BooleanTrue = 1;

    Dataclasses.SetValue(CFSTR("Keybag"), CFNumberCreate(nullptr, kCFNumberIntType, &BooleanTrue));

    return ATHostConnectionSendMetadataSyncFinished(this->Connection, Dataclasses, DataclassAnchors);
}

String iOSATH::GetLibraryID()
{
    CFData iTunesPrefs = iOSAFC::ReadFileToBuffer(device, L"/iTunes_Control/iTunes/iTunesPrefs");

    if (iTunesPrefs == nullptr)
        return L"0000000000000000";

    ULONG v1, v2;
    PULONG buffer;

    buffer = (PULONG)CFDataGetBytePtr(iTunesPrefs);

    v1 = buffer[5] ^ buffer[0x18];
    v2 = buffer[6] ^ buffer[0x19];

    return String::Format(L"%08X%08X", v2, v1);
}
