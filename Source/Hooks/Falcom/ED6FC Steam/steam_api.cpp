#include "ml.h"

#define S_API CDECL

typedef ULONG64 SteamAPICall;

class ISteamApps
{
public:
    virtual bool BIsSubscribed()
    {
        return true;
    }

    virtual bool BIsLowViolence()
    {
        return false;
    }

    virtual bool BIsCybercafe()
    {
        return false;
    }

    virtual bool BIsVACBanned()
    {
        return false;
    }

    virtual PCSTR GetCurrentGameLanguage()
    {
        return "english";
    }

    virtual PCSTR GetAvailableGameLanguages()
    {
        return "english";
    }

    virtual bool BIsSubscribedApp(ULONG appID)
    {
        return true;
    }

    virtual bool BIsDlcInstalled(ULONG appID)
    {
        return true;
    }
};

EXTC bool S_API SteamAPI_Init()
{
    return true;
}

EXTC bool S_API SteamAPI_InitSafe()
{
    return false;
}

EXTC bool S_API SteamAPI_IsSteamRunning()
{
    return true;
}

EXTC void S_API SteamAPI_RegisterCallResult(class CallbackBase *callback, SteamAPICall apiCall)
{
}

EXTC void S_API SteamAPI_RegisterCallback(class CallbackBase *callback, int iCallback)
{
}

EXTC bool S_API SteamAPI_RestartAppIfNecessary(ULONG appId)
{
    return false;
}

EXTC void S_API SteamAPI_RunCallbacks()
{
}

EXTC void S_API SteamAPI_SetMiniDumpComment(PCSTR msg)
{
}

EXTC void S_API SteamAPI_Shutdown()
{
}

EXTC void S_API SteamAPI_UnregisterCallResult(class CallbackBase *callback, SteamAPICall apiCall)
{
}

EXTC void S_API SteamAPI_UnregisterCallback(class CallbackBase *callback)
{
}

EXTC void S_API SteamAPI_WriteMiniDump(ULONG exceptionCode, PVOID exceptionInfo, ULONG buildId)
{
}

EXTC class ISteamApps* SteamApps()
{
    return new ISteamApps();
}
