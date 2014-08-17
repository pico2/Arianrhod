#include "ml.h"

#define S_API CDECL
#define S_VIRTUAL THISCALL

enum AccountType
{
    AccountTypeInvalid = 0,
    AccountTypeIndividual = 1,
    AccountTypeMultiseat = 2,
    AccountTypeGameServer = 3,
    AccountTypeAnonGameServer = 4,
    AccountTypePending = 5,
    AccountTypeContentServer = 6,
    AccountTypeClan = 7,
    AccountTypeChat = 8,
    AccountTypeAnonUser = 10,
    AccountTypeMax
};

enum ServerMode
{
    ServerModeInvalid = 0,
    ServerModeNoAuthentication = 1,
    ServerModeAuthentication = 2,
    ServerModeAuthenticationAndSecure = 3
};

enum LeaderboardDataRequest
{
    LeaderboardDataRequestGlobal = 0,
    LeaderboardDataRequestGlobalAroundUser = 1,
    LeaderboardDataRequestFriends = 2
};

enum LeaderboardSortMethod
{
    LeaderboardSortMethodNone = 0,
    LeaderboardSortMethodAscending = 1,
    LeaderboardSortMethodDescending = 2
};

enum LeaderboardDisplayType
{
    LeaderboardDisplayTypeNone = 0,
    LeaderboardDisplayTypeNumeric = 1,
    LeaderboardDisplayTypeTimeSeconds = 2,
    LeaderboardDisplayTypeTimeMilliSeconds = 3
};

enum LeaderboardUploadScoreMethod
{
    LeaderboardUploadScoreMethodNone = 0,
    LeaderboardUploadScoreMethodKeepBest = 1,
    LeaderboardUploadScoreMethodForceUpdate = 2
};

typedef ULONG64 SteamAPICall;
typedef ULONG64 SteamLeaderboard;
typedef ULONG64 SteamLeaderboardEntries;
typedef ULONG SteamPipeId;
typedef ULONG SteamUserId;
typedef ULONG AppId;

const SteamAPICall SteamAPICallInvalid = 0;
const AppId AppIdInvalid = 0;

struct ISteamApps;
struct ISteamUser;
struct ISteamGameServer;
struct ISteamFriends;
struct ISteamUtils;
struct ISteamMatchmaking;
struct ISteamMasterServerUpdater;
struct ISteamMatchmakingServers;
struct ISteamUserStats;
struct ISteamGameServerStats;
struct ISteamNetworking;
struct ISteamRemoteStorage;

typedef VOID (*SteamAPIWarningMessageHook)(ULONG, PCSTR);

ISteamApps* S_API SteamApps();

struct CSteamID
{

};

struct LeaderboardEntry
{
    CSteamID mSteamIDUser;
    ULONG mGlobalRank;
    ULONG mScore;
    ULONG mDetails;
};

struct ISteamApps
{
public:
    virtual bool S_VIRTUAL BIsSubscribed()
    {
        PrintConsole(L"%s\n", L"BIsSubscribed");
        return true;
    }

    virtual bool S_VIRTUAL BIsLowViolence()
    {
        PrintConsole(L"%s\n", L"BIsLowViolence");
        return false;
    }

    virtual bool S_VIRTUAL BIsCybercafe()
    {
        PrintConsole(L"%s\n", L"BIsCybercafe");
        return false;
    }

    virtual bool S_VIRTUAL BIsVACBanned()
    {
        PrintConsole(L"%s\n", L"BIsVACBanned");
        return false;
    }

    virtual PCSTR S_VIRTUAL GetCurrentGameLanguage()
    {
        PrintConsole(L"%s\n", L"GetCurrentGameLanguage");
        return "english";
    }

    virtual PCSTR S_VIRTUAL GetAvailableGameLanguages()
    {
        PrintConsole(L"%s\n", L"GetAvailableGameLanguages");
        return "english";
    }

    virtual bool S_VIRTUAL BIsSubscribedApp(ULONG appID)
    {
        PrintConsole(L"%s\n", L"BIsSubscribedApp");
        return true;
    }

    virtual bool S_VIRTUAL BIsDlcInstalled(ULONG appID)
    {
        PrintConsole(L"%s\n", L"BIsDlcInstalled");
        return true;
    }
};

struct ISteamClient
{
public:
    virtual SteamPipeId S_VIRTUAL CreateSteamPipe()
    {
        PrintConsole(L"%s\n", L"CreateSteamPipe");
        return 0;
    }

    virtual bool S_VIRTUAL BReleaseSteamPipe(SteamPipeId steamPipe)
    {
        PrintConsole(L"%s\n", L"BReleaseSteamPipe");
        return true;
    }

    virtual SteamUserId S_VIRTUAL ConnectToGlobalUser(SteamPipeId steamPipe)
    {
        PrintConsole(L"%s\n", L"ConnectToGlobalUser");
        return 0;
    }

    virtual SteamUserId S_VIRTUAL CreateLocalUser(SteamPipeId *steamPipe, AccountType accountType)
    {
        PrintConsole(L"%s\n", L"CreateLocalUser");
        return 0;
    }

    virtual void S_VIRTUAL ReleaseUser(SteamPipeId steamPipe, SteamUserId user)
    {
        PrintConsole(L"%s\n", L"ReleaseUser");
    }

    virtual ISteamUser* S_VIRTUAL GetISteamUser(SteamUserId steamUser, SteamPipeId steamPipe, PCSTR version)
    {
        PrintConsole(L"%s\n", L"GetISteamUser");
        DebugBreakPoint();
    }

    virtual ISteamGameServer *S_VIRTUAL GetISteamGameServer(SteamUserId steamUser, SteamPipeId steamPipe, PCSTR version)
    {
        PrintConsole(L"%s\n", L"GetISteamGameServer");
        DebugBreakPoint();
    }

    virtual void S_VIRTUAL SetLocalIPBinding(ULONG ip, USHORT port)
    {
        PrintConsole(L"%s\n", L"SetLocalIPBinding");
    }

    virtual ISteamFriends *S_VIRTUAL GetISteamFriends(SteamUserId steamUser, SteamPipeId steamPipe, PCSTR version)
    {
        PrintConsole(L"%s\n", L"GetISteamFriends");
        DebugBreakPoint();
    }

    virtual ISteamUtils *S_VIRTUAL GetISteamUtils(SteamPipeId steamPipe, PCSTR version)
    {
        PrintConsole(L"%s\n", L"GetISteamUtils");
        DebugBreakPoint();
    }

    virtual ISteamMatchmaking *S_VIRTUAL GetISteamMatchmaking(SteamUserId steamUser, SteamPipeId steamPipe, PCSTR version)
    {
        PrintConsole(L"%s\n", L"GetISteamMatchmaking");
        DebugBreakPoint();
    }

    virtual ISteamMasterServerUpdater *S_VIRTUAL GetISteamMasterServerUpdater(SteamUserId steamUser, SteamPipeId steamPipe, PCSTR version)
    {
        PrintConsole(L"%s\n", L"GetISteamMasterServerUpdater");
        DebugBreakPoint();
    }

    virtual ISteamMatchmakingServers *S_VIRTUAL GetISteamMatchmakingServers(SteamUserId steamUser, SteamPipeId steamPipe, PCSTR version)
    {
        PrintConsole(L"%s\n", L"GetISteamMatchmakingServers");
        DebugBreakPoint();
    }

    virtual void *S_VIRTUAL GetISteamGenericInterface(SteamUserId steamUser, SteamPipeId steamPipe, PCSTR version)
    {
        PrintConsole(L"%s\n", L"GetISteamGenericInterface");
        DebugBreakPoint();
    }

    virtual ISteamUserStats *S_VIRTUAL GetISteamUserStats(SteamUserId steamUser, SteamPipeId steamPipe, PCSTR version)
    {
        PrintConsole(L"%s\n", L"GetISteamUserStats");
        DebugBreakPoint();
    }

    virtual ISteamGameServerStats *S_VIRTUAL GetISteamGameServerStats(SteamUserId steamUser, SteamPipeId steamPipe, PCSTR version)
    {
        PrintConsole(L"%s\n", L"GetISteamGameServerStats");
        DebugBreakPoint();
    }

    virtual ISteamApps *S_VIRTUAL GetISteamApps(SteamUserId steamUser, SteamPipeId steamPipe, PCSTR version)
    {
        PrintConsole(L"%s\n", L"GetISteamApps");
        return SteamApps();
    }

    virtual ISteamNetworking *S_VIRTUAL GetISteamNetworking(SteamUserId steamUser, SteamPipeId steamPipe, PCSTR version)
    {
        PrintConsole(L"%s\n", L"GetISteamNetworking");
        DebugBreakPoint();
    }

    virtual ISteamRemoteStorage *S_VIRTUAL GetISteamRemoteStorage(SteamUserId steamUser, SteamPipeId steamPipe, PCSTR version)
    {
        PrintConsole(L"%s\n", L"GetISteamRemoteStorage");
        DebugBreakPoint();
    }

    virtual void S_VIRTUAL RunFrame()
    {
        PrintConsole(L"%s\n", L"RunFrame");
    }

    virtual ULONG S_VIRTUAL GetIPCCallCount()
    {
        PrintConsole(L"%s\n", L"GetIPCCallCount");
        return 0;
    }

    virtual void S_VIRTUAL SetWarningMessageHook(SteamAPIWarningMessageHook function)
    {
        PrintConsole(L"%s\n", L"SetWarningMessageHook");
    }
};

struct ISteamUserStats
{
    SteamLeaderboard mLastLeaderboard = 0;

    virtual bool S_VIRTUAL RequestCurrentStats()
    {
        PrintConsole(L"%s\n", L"RequestCurrentStats");
        return true;
    }

    virtual bool S_VIRTUAL GetStat(PCSTR name, LONG *data )
    {
        PrintConsole(L"%s\n", L"GetStat");
        *data = 0;
        return true;
    };

    virtual bool S_VIRTUAL GetStat(PCSTR name, float *data)
    {
        PrintConsole(L"%s\n", L"GetStat");
        *data = 0;
        return true;
    }

    virtual bool S_VIRTUAL SetStat(PCSTR name, LONG data)
    {
        PrintConsole(L"%s\n", L"SetStat");
        return true;
    }

    virtual bool S_VIRTUAL SetStat(PCSTR name, float data)
    {
        PrintConsole(L"%s\n", L"SetStat");
        return true;
    }

    virtual bool S_VIRTUAL UpdateAvgRateStat(PCSTR name, float countThisSession,  double sessionLength)
    {
        PrintConsole(L"%s\n", L"UpdateAvgRateStat");
        return true;
    }

    virtual bool S_VIRTUAL GetAchievement(PCSTR name, bool *achieved)
    {
        PrintConsole(L"%s\n", L"GetAchievement");
        *achieved = true;
        return true;
    }

    virtual bool S_VIRTUAL SetAchievement(PCSTR name)
    {
        PrintConsole(L"%s\n", L"SetAchievement");
        return true;
    }

    virtual bool S_VIRTUAL ClearAchievement(PCSTR name)
    {
        PrintConsole(L"%s\n", L"ClearAchievement");
        return true;
    }

    virtual bool S_VIRTUAL GetAchievementAndUnlockTime(PCSTR name,
                              bool *achieved,
                              ULONG *unlockTime)
    {
        PrintConsole(L"%s\n", L"GetAchievementAndUnlockTime");
        *achieved = true;
        *unlockTime = 0;
        return true;
    }

    virtual bool S_VIRTUAL StoreStats()
    {
        PrintConsole(L"%s\n", L"StoreStats");
        return true;
    }

    virtual int S_VIRTUAL GetAchievementIcon(PCSTR name)
    {
        PrintConsole(L"%s\n", L"GetAchievementIcon");
        return 0;
    }

    virtual PCSTR S_VIRTUAL GetAchievementDisplayAttribute(PCSTR name,
                                    PCSTR key)
    {
        PrintConsole(L"%s\n", L"GetAchievementDisplayAttribute");
        return "AchievementDisplayAttribute";
    }

    virtual bool S_VIRTUAL IndicateAchievementProgress(PCSTR name,
                              ULONG curProgress,
                              ULONG maxProgress)
    {
        PrintConsole(L"%s\n", L"IndicateAchievementProgress");
        return true;
    }

    virtual SteamAPICall S_VIRTUAL RequestUserStats(CSteamID steamIDUser)
    {
        PrintConsole(L"%s\n", L"RequestUserStats");
        return SteamAPICallInvalid;
    }

    virtual bool S_VIRTUAL GetUserStat(CSteamID steamIDUser,
                      PCSTR name,
                      LONG *data)
    {
        PrintConsole(L"%s\n", L"GetUserStat");
        *data = 0;
        return true;
    }

    virtual bool S_VIRTUAL GetUserStat(CSteamID steamIDUser,
                      PCSTR name,
                      float *data)
    {
        PrintConsole(L"%s\n", L"GetUserStat");
        *data = 0;
        return true;
    }

    virtual bool S_VIRTUAL GetUserAchievement(CSteamID steamIDUser,
                         PCSTR name,
                         bool *achieved)
    {
        PrintConsole(L"%s\n", L"GetUserAchievement");
        *achieved = true;
        return true;
    }

    virtual bool S_VIRTUAL GetUserAchievementAndUnlockTime(CSteamID steamIDUser,
                                  PCSTR name,
                                  bool *achieved,
                                  ULONG *unlockTime)
    {
        PrintConsole(L"%s\n", L"GetUserAchievementAndUnlockTime");
        *achieved = true;
        *unlockTime = 0;
        return true;
    }

    virtual bool S_VIRTUAL ResetAllStats(bool achievementsToo)
    {
        PrintConsole(L"%s\n", L"ResetAllStats");
        return true;
    }

    virtual SteamAPICall S_VIRTUAL FindOrCreateLeaderboard(
            PCSTR leaderboardName,
            LeaderboardSortMethod leaderboardSortMethod,
            LeaderboardDisplayType leaderboardDisplayType)
    {
        PrintConsole(L"%s\n", L"FindOrCreateLeaderboard");
        return SteamAPICallInvalid;
    }

    virtual SteamAPICall S_VIRTUAL FindLeaderboard(PCSTR leaderboardName)
    {
        PrintConsole(L"%s\n", L"FindLeaderboard");
        return SteamAPICallInvalid;
    }

    virtual PCSTR S_VIRTUAL GetLeaderboardName(SteamLeaderboard steamLeaderboard)
    {
        PrintConsole(L"%s\n", L"GetLeaderboardName");
        return "LeaderboardName";
    }
    virtual int S_VIRTUAL GetLeaderboardEntryCount(SteamLeaderboard steamLeaderboard)
    {
        PrintConsole(L"%s\n", L"GetLeaderboardEntryCount");
        mLastLeaderboard = steamLeaderboard;
        return 10;
    }

    virtual LeaderboardSortMethod S_VIRTUAL GetLeaderboardSortMethod(
            SteamLeaderboard steamLeaderboard)
    {
        PrintConsole(L"%s\n", L"GetLeaderboardSortMethod");
        return LeaderboardSortMethodDescending;
    }

    virtual LeaderboardDisplayType S_VIRTUAL GetLeaderboardDisplayType(
            SteamLeaderboard steamLeaderboard)
    {
        PrintConsole(L"%s\n", L"GetLeaderboardDisplayType");
        return LeaderboardDisplayTypeNumeric;
    }

    virtual SteamAPICall S_VIRTUAL DownloadLeaderboardEntries(
            SteamLeaderboard steamLeaderboard,
            LeaderboardDataRequest leaderboardDataRequest,
            int rangeStart,
            int rangeEnd)
    {
        PrintConsole(L"%s\n", L"DownloadLeaderboardEntries");
        return SteamAPICallInvalid;
    }

    virtual bool S_VIRTUAL GetDownloadedLeaderboardEntry(
            SteamLeaderboardEntries steamLeaderboardEntries,
            int index,
            LeaderboardEntry *leaderboardEntry,
            LONG *details,
            int detailsMax)
    {
        PrintConsole(L"%s\n", L"GetDownloadedLeaderboardEntry");
        *details = 0;
        return false;
    }

    virtual SteamAPICall S_VIRTUAL UploadLeaderboardScore(
            SteamLeaderboard steamLeaderboard,
            LeaderboardUploadScoreMethod leaderboardUploadScoreMethod,
            LONG score,
            const LONG *scoreDetails,
            int scoreDetailsCount)
    {
        PrintConsole(L"%s\n", L"UploadLeaderboardScore");
        return SteamAPICallInvalid;
    }

    virtual SteamAPICall S_VIRTUAL GetNumberOfCurrentPlayers()
    {
        PrintConsole(L"%s\n", L"GetNumberOfCurrentPlayers");
        return SteamAPICallInvalid;
    }
};

struct ISteamRemoteStorage
{
    virtual bool S_VIRTUAL FileWrite(const char *file,
                        const void *data,
                        LONG dataSize)
    {
        PrintConsole(L"%s\n", L"FileWrite");
        return true;
    }

    virtual LONG S_VIRTUAL GetFileSize(const char *file)
    {
        PrintConsole(L"%s\n", L"GetFileSize");
        return 0;
    }

    virtual LONG S_VIRTUAL FileRead(const char *file,
                        void *data,
                        LONG dataSize)
    {
        PrintConsole(L"%s\n", L"FileRead");
        return 0;
    }

    virtual bool S_VIRTUAL FileExists(const char *file)
    {
        PrintConsole(L"%s\n", L"FileExists");
        return false;
    }

    virtual LONG S_VIRTUAL GetFileCount()
    {
        PrintConsole(L"%s\n", L"GetFileCount");
        return 0;
    }

    virtual const char *S_VIRTUAL GetFileNameAndSize(int file,
                                LONG *fileSizeInBytes)
    {
        PrintConsole(L"%s\n", L"GetFileNameAndSize");
        *fileSizeInBytes = 0;
        return "FileName";
    }

    virtual bool S_VIRTUAL GetQuota(LONG *totalBytes, LONG *availableBytes)
    {
        PrintConsole(L"%s\n", L"GetQuota");
        *totalBytes = 1000000000;
        *availableBytes = 1000000000;
        return true;
    }
};

//////////////////////////////////////////////////////////////////////////
// export
//////////////////////////////////////////////////////////////////////////

bool S_API SteamAPI_Init()
{
    PrintConsole(L"%s\n", L"SteamAPI_Init");
    return true;
}

bool S_API SteamAPI_InitSafe()
{
    PrintConsole(L"%s\n", L"SteamAPI_InitSafe");
    return false;
}

bool S_API SteamAPI_IsSteamRunning()
{
    PrintConsole(L"%s\n", L"SteamAPI_IsSteamRunning");
    return true;
}

void S_API SteamAPI_RegisterCallResult(struct CallbackBase *callback, SteamAPICall apiCall)
{
    PrintConsole(L"%s\n", L"SteamAPI_RegisterCallResult");
}

void S_API SteamAPI_RegisterCallback(struct CallbackBase *callback, int iCallback)
{
    PrintConsole(L"%s\n", L"SteamAPI_RegisterCallback");
}

bool S_API SteamAPI_RestartAppIfNecessary(ULONG appId)
{
    PrintConsole(L"%s\n", L"SteamAPI_RestartAppIfNecessary");
    return false;
}

void S_API SteamAPI_RunCallbacks()
{
    PrintConsole(L"%s\n", L"SteamAPI_RunCallbacks");
}

void S_API SteamAPI_SetMiniDumpComment(PCSTR msg)
{
    PrintConsole(L"%s\n", L"SteamAPI_SetMiniDumpComment");
}

void S_API SteamAPI_Shutdown()
{
    PrintConsole(L"%s\n", L"SteamAPI_Shutdown");
}

void S_API SteamAPI_UnregisterCallResult(struct CallbackBase *callback, SteamAPICall apiCall)
{
    PrintConsole(L"%s\n", L"SteamAPI_UnregisterCallResult");
}

void S_API SteamAPI_UnregisterCallback(struct CallbackBase *callback)
{
    PrintConsole(L"%s\n", L"SteamAPI_UnregisterCallback");
}

void S_API SteamAPI_WriteMiniDump(ULONG exceptionCode, PVOID exceptionInfo, ULONG buildId)
{
    PrintConsole(L"%s\n", L"SteamAPI_WriteMiniDump");
}

ISteamApps* S_API SteamApps()
{
    PrintConsole(L"%s\n", L"SteamApps");
    static ISteamApps apps;
    return &apps;
}

ISteamUserStats* S_API SteamUserStats()
{
    PrintConsole(L"%s\n", L"SteamUserStats");
    static ISteamUserStats stat;
    return &stat;
}

struct ISteamClient* S_API SteamClient()
{
    PrintConsole(L"%s\n", L"SteamClient");
    static ISteamClient client;
    return &client;
}

ISteamFriends* S_API SteamFriends()
{
    PrintConsole(L"%s\n", L"SteamFriends");
    DebugBreakPoint();
}

ISteamGameServer* S_API SteamGameServer()
{
    PrintConsole(L"%s\n", L"SteamGameServer");
    DebugBreakPoint();
}

ISteamNetworking* S_API SteamGameServerNetworking()
{
    PrintConsole(L"%s\n", L"SteamGameServerNetworking");
    DebugBreakPoint();
}

ULONG64 S_API SteamGameServer_GetSteamID()
{
    PrintConsole(L"%s\n", L"SteamGameServer_GetSteamID");
    return 251150;
}

bool S_API SteamGameServer_Init(ULONG ip, USHORT port, USHORT gamePort, USHORT spectatorPort, USHORT queryPort, ServerMode serverMode, PCSTR gameDir, PCSTR versionString)
{
    PrintConsole(L"%s\n", L"SteamGameServer_Init");
    return true;
}

void S_API SteamGameServer_RunCallbacks()
{
    PrintConsole(L"%s\n", L"SteamGameServer_RunCallbacks");
}

void S_API SteamGameServer_Shutdown()
{
    PrintConsole(L"%s\n", L"SteamGameServer_Shutdown");
}

ISteamMatchmaking* S_API SteamMatchmaking()
{
    PrintConsole(L"%s\n", L"SteamMatchmaking");
    DebugBreakPoint();
}

ISteamMatchmakingServers* S_API SteamMatchmakingServers()
{
    PrintConsole(L"%s\n", L"SteamMatchmakingServers");
    DebugBreakPoint();
}

ISteamNetworking* S_API SteamNetworking()
{
    PrintConsole(L"%s\n", L"SteamNetworking");
    DebugBreakPoint();
}

ISteamRemoteStorage* S_API SteamRemoteStorage()
{
    PrintConsole(L"%s\n", L"SteamRemoteStorage");
    static ISteamRemoteStorage storage;
    return &storage;
}

VOID S_API SteamScreenshots()
{
    PrintConsole(L"%s\n", L"SteamScreenshots");
}
