#include "ml.h"

#define S_API CDECL
#define S_VIRTUAL THISCALL

#define PrintConsole(...)

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
typedef ULONG AppId, AppId_t;

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
    ULONG64 steamid;
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
        PrintConsole(L"BIsSubscribed\n");
        return true;
    }

    virtual bool S_VIRTUAL BIsLowViolence()
    {
        PrintConsole(L"BIsLowViolence\n");
        return false;
    }

    virtual bool S_VIRTUAL BIsCybercafe()
    {
        PrintConsole(L"BIsCybercafe\n");
        return false;
    }

    virtual bool S_VIRTUAL BIsVACBanned()
    {
        PrintConsole(L"BIsVACBanned\n");
        return false;
    }

    virtual PCSTR S_VIRTUAL GetCurrentGameLanguage()
    {
        PrintConsole(L"GetCurrentGameLanguage\n");
        return "english";
    }

    virtual PCSTR S_VIRTUAL GetAvailableGameLanguages()
    {
        PrintConsole(L"GetAvailableGameLanguages\n");
        return "english";
    }

    virtual bool S_VIRTUAL BIsSubscribedApp(ULONG appID)
    {
        PrintConsole(L"BIsSubscribedApp\n");
        return true;
    }

    virtual bool S_VIRTUAL BIsDlcInstalled(ULONG appID)
    {
        PrintConsole(L"BIsDlcInstalled\n");
        return true;
    }

    virtual ULONG S_VIRTUAL GetEarliestPurchaseUnixTime(AppId nAppID)
    {
        PrintConsole(L"GetEarliestPurchaseUnixTime\n");
        return 0;
    }

    virtual bool S_VIRTUAL BIsSubscribedFromFreeWeekend()
    {
        PrintConsole(L"BIsSubscribedFromFreeWeekend\n");
        return true;
    }

    virtual int S_VIRTUAL GetDLCCount()
    {
        PrintConsole(L"GetDLCCount\n");
        return 0;
    }

    virtual bool S_VIRTUAL BGetDLCDataByIndex( int iDLC, AppId_t *pAppID, bool *pbAvailable, char *pchName, int cchNameBufferSize )
    {
        PrintConsole(L"BGetDLCDataByIndex\n");
        return false;
    }

    virtual void S_VIRTUAL InstallDLC( AppId_t nAppID )
    {
        PrintConsole(L"InstallDLC\n");
    }

    virtual void S_VIRTUAL UninstallDLC( AppId_t nAppID )
    {
        PrintConsole(L"UninstallDLC\n");
    }

    virtual void S_VIRTUAL RequestAppProofOfPurchaseKey(AppId_t nAppID)
    {
        PrintConsole(L"RequestAppProofOfPurchaseKey\n");
    }

    virtual bool S_VIRTUAL GetCurrentBetaName( char *pchName, int cchNameBufferSize )
    {
        PrintConsole(L"GetCurrentBetaName\n");
        return false;
    }

    virtual bool S_VIRTUAL MarkContentCorrupt( bool bMissingFilesOnly )
    {
        PrintConsole(L"MarkContentCorrupt\n");
        return false;
    }

    virtual ULONG S_VIRTUAL GetInstalledDepots( AppId_t appID, ULONG *pvecDepots, ULONG cMaxDepots )
    {
        PrintConsole(L"GetInstalledDepots\n");
        return false;
    }

    virtual ULONG S_VIRTUAL GetAppInstallDir( AppId_t appID, char *pchFolder, ULONG cchFolderBufferSize )
    {
        PrintConsole(L"GetAppInstallDir\n");
        return 0;
    }

    virtual bool S_VIRTUAL BIsAppInstalled(AppId_t appID)
    {
        PrintConsole(L"BIsAppInstalled\n");
        return true;
    }

    virtual PVOID S_VIRTUAL GetAppOwner()
    {
        PrintConsole(L"GetAppOwner\n");
        return nullptr;
    }

    virtual PCSTR S_VIRTUAL GetLaunchQueryParam(PCSTR pchKey)
    {
        PrintConsole(L"GetLaunchQueryParam\n");
        return "";
    }
};

struct ISteamClient
{
public:
    virtual SteamPipeId S_VIRTUAL CreateSteamPipe()
    {
        PrintConsole(L"CreateSteamPipe\n");
        return 0;
    }

    virtual bool S_VIRTUAL BReleaseSteamPipe(SteamPipeId steamPipe)
    {
        PrintConsole(L"BReleaseSteamPipe\n");
        return true;
    }

    virtual SteamUserId S_VIRTUAL ConnectToGlobalUser(SteamPipeId steamPipe)
    {
        PrintConsole(L"ConnectToGlobalUser\n");
        return 0;
    }

    virtual SteamUserId S_VIRTUAL CreateLocalUser(SteamPipeId *steamPipe, AccountType accountType)
    {
        PrintConsole(L"CreateLocalUser\n");
        return 0;
    }

    virtual void S_VIRTUAL ReleaseUser(SteamPipeId steamPipe, SteamUserId user)
    {
        PrintConsole(L"ReleaseUser\n");
    }

    virtual ISteamUser* S_VIRTUAL GetISteamUser(SteamUserId steamUser, SteamPipeId steamPipe, PCSTR version)
    {
        PrintConsole(L"GetISteamUser\n");
        DebugBreakPoint();
        return nullptr;
    }

    virtual ISteamGameServer *S_VIRTUAL GetISteamGameServer(SteamUserId steamUser, SteamPipeId steamPipe, PCSTR version)
    {
        PrintConsole(L"GetISteamGameServer\n");
        DebugBreakPoint();
        return nullptr;
    }

    virtual void S_VIRTUAL SetLocalIPBinding(ULONG ip, USHORT port)
    {
        PrintConsole(L"SetLocalIPBinding\n");
    }

    virtual ISteamFriends *S_VIRTUAL GetISteamFriends(SteamUserId steamUser, SteamPipeId steamPipe, PCSTR version)
    {
        PrintConsole(L"GetISteamFriends\n");
        DebugBreakPoint();
        return nullptr;
    }

    virtual ISteamUtils *S_VIRTUAL GetISteamUtils(SteamPipeId steamPipe, PCSTR version)
    {
        PrintConsole(L"GetISteamUtils\n");
        DebugBreakPoint();
        return nullptr;
    }

    virtual ISteamMatchmaking *S_VIRTUAL GetISteamMatchmaking(SteamUserId steamUser, SteamPipeId steamPipe, PCSTR version)
    {
        PrintConsole(L"GetISteamMatchmaking\n");
        DebugBreakPoint();
        return nullptr;
    }

    virtual ISteamMasterServerUpdater *S_VIRTUAL GetISteamMasterServerUpdater(SteamUserId steamUser, SteamPipeId steamPipe, PCSTR version)
    {
        PrintConsole(L"GetISteamMasterServerUpdater\n");
        DebugBreakPoint();
        return nullptr;
    }

    virtual ISteamMatchmakingServers *S_VIRTUAL GetISteamMatchmakingServers(SteamUserId steamUser, SteamPipeId steamPipe, PCSTR version)
    {
        PrintConsole(L"GetISteamMatchmakingServers\n");
        DebugBreakPoint();
        return nullptr;
    }

    virtual void *S_VIRTUAL GetISteamGenericInterface(SteamUserId steamUser, SteamPipeId steamPipe, PCSTR version)
    {
        PrintConsole(L"GetISteamGenericInterface\n");
        DebugBreakPoint();
        return nullptr;
    }

    virtual ISteamUserStats *S_VIRTUAL GetISteamUserStats(SteamUserId steamUser, SteamPipeId steamPipe, PCSTR version)
    {
        PrintConsole(L"GetISteamUserStats\n");
        DebugBreakPoint();
        return nullptr;
    }

    virtual ISteamGameServerStats *S_VIRTUAL GetISteamGameServerStats(SteamUserId steamUser, SteamPipeId steamPipe, PCSTR version)
    {
        PrintConsole(L"GetISteamGameServerStats\n");
        DebugBreakPoint();
        return nullptr;
    }

    virtual ISteamApps *S_VIRTUAL GetISteamApps(SteamUserId steamUser, SteamPipeId steamPipe, PCSTR version)
    {
        PrintConsole(L"GetISteamApps\n");
        return SteamApps();
    }

    virtual ISteamNetworking *S_VIRTUAL GetISteamNetworking(SteamUserId steamUser, SteamPipeId steamPipe, PCSTR version)
    {
        PrintConsole(L"GetISteamNetworking\n");
        DebugBreakPoint();
        return nullptr;
    }

    virtual ISteamRemoteStorage *S_VIRTUAL GetISteamRemoteStorage(SteamUserId steamUser, SteamPipeId steamPipe, PCSTR version)
    {
        PrintConsole(L"GetISteamRemoteStorage\n");
        DebugBreakPoint();
        return nullptr;
    }

    virtual void S_VIRTUAL RunFrame()
    {
        PrintConsole(L"RunFrame\n");
    }

    virtual ULONG S_VIRTUAL GetIPCCallCount()
    {
        PrintConsole(L"GetIPCCallCount\n");
        return 0;
    }

    virtual void S_VIRTUAL SetWarningMessageHook(SteamAPIWarningMessageHook function)
    {
        PrintConsole(L"SetWarningMessageHook\n");
    }

    virtual bool S_VIRTUAL BShutdownIfAllPipesClosed()
    {
        PrintConsole(L"BShutdownIfAllPipesClosed\n");
        return false;
    }

    virtual class ISteamHTTP * S_VIRTUAL GetISteamHTTP( SteamUserId hSteamuser, SteamPipeId hSteamPipe, PCSTR pchVersion )
    {
        PrintConsole(L"GetISteamHTTP\n");
        DebugBreakPoint();
        return nullptr;
    }

    virtual class ISteamUnifiedMessages * S_VIRTUAL GetISteamUnifiedMessages( SteamUserId hSteamuser, SteamPipeId hSteamPipe, PCSTR pchVersion )
    {
        PrintConsole(L"GetISteamUnifiedMessages\n");
        DebugBreakPoint();
        return nullptr;
    }

    virtual class  ISteamController * S_VIRTUAL GetISteamController( SteamUserId hSteamUser, SteamPipeId hSteamPipe, PCSTR pchVersion )
    {
        PrintConsole(L"GetISteamController\n");
        DebugBreakPoint();
        return nullptr;
    }

    virtual class ISteamUGC * S_VIRTUAL GetISteamUGC( SteamUserId hSteamUser, SteamPipeId hSteamPipe, PCSTR pchVersion )
    {
        PrintConsole(L"GetISteamUGC\n");
        DebugBreakPoint();
        return nullptr;
    }

    virtual class ISteamAppList * S_VIRTUAL GetISteamAppList( SteamUserId hSteamUser, SteamPipeId hSteamPipe, PCSTR pchVersion )
    {
        PrintConsole(L"GetISteamAppList\n");
        DebugBreakPoint();
        return nullptr;
    }

    virtual class ISteamMusic * S_VIRTUAL GetISteamMusic( SteamUserId hSteamuser, SteamPipeId hSteamPipe, PCSTR pchVersion )
    {
        PrintConsole(L"GetISteamMusic\n");
        DebugBreakPoint();
        return nullptr;
    }
};

struct ISteamUserStats
{
    SteamLeaderboard mLastLeaderboard = 0;

    virtual bool S_VIRTUAL RequestCurrentStats()
    {
        PrintConsole(L"RequestCurrentStats\n");
        return true;
    }

    virtual bool S_VIRTUAL GetStat(PCSTR name, LONG *data )
    {
        PrintConsole(L"GetStat\n");
        *data = 0;
        return true;
    };

    virtual bool S_VIRTUAL GetStat(PCSTR name, float *data)
    {
        PrintConsole(L"GetStat\n");
        *data = 0;
        return true;
    }

    virtual bool S_VIRTUAL SetStat(PCSTR name, LONG data)
    {
        PrintConsole(L"SetStat\n");
        return true;
    }

    virtual bool S_VIRTUAL SetStat(PCSTR name, float data)
    {
        PrintConsole(L"SetStat\n");
        return true;
    }

    virtual bool S_VIRTUAL UpdateAvgRateStat(PCSTR name, float countThisSession,  double sessionLength)
    {
        PrintConsole(L"UpdateAvgRateStat\n");
        return true;
    }

    virtual bool S_VIRTUAL GetAchievement(PCSTR name, bool *achieved)
    {
        PrintConsole(L"GetAchievement\n");
        *achieved = true;
        return true;
    }

    virtual bool S_VIRTUAL SetAchievement(PCSTR name)
    {
        PrintConsole(L"SetAchievement\n");
        return true;
    }

    virtual bool S_VIRTUAL ClearAchievement(PCSTR name)
    {
        PrintConsole(L"ClearAchievement\n");
        return true;
    }

    virtual bool S_VIRTUAL GetAchievementAndUnlockTime(PCSTR name,
                              bool *achieved,
                              ULONG *unlockTime)
    {
        PrintConsole(L"GetAchievementAndUnlockTime\n");
        *achieved = true;
        *unlockTime = 0;
        return true;
    }

    virtual bool S_VIRTUAL StoreStats()
    {
        PrintConsole(L"StoreStats\n");
        return true;
    }

    virtual int S_VIRTUAL GetAchievementIcon(PCSTR name)
    {
        PrintConsole(L"GetAchievementIcon\n");
        return 0;
    }

    virtual PCSTR S_VIRTUAL GetAchievementDisplayAttribute(PCSTR name, PCSTR key)
    {
        PrintConsole(L"GetAchievementDisplayAttribute\n");
        return "AchievementDisplayAttribute";
    }

    virtual bool S_VIRTUAL IndicateAchievementProgress(PCSTR name, ULONG curProgress, ULONG maxProgress)
    {
        PrintConsole(L"IndicateAchievementProgress\n");
        return true;
    }

    virtual ULONG S_VIRTUAL GetNumAchievements()
    {
        return 0;
    }

    virtual PCSTR S_VIRTUAL GetAchievementName( ULONG iAchievement )
    {
        return 0;
    }

    virtual SteamAPICall S_VIRTUAL RequestUserStats(CSteamID steamIDUser)
    {
        PrintConsole(L"RequestUserStats\n");
        return SteamAPICallInvalid;
    }

    virtual bool S_VIRTUAL GetUserStat(CSteamID steamIDUser, PCSTR name, LONG *data)
    {
        PrintConsole(L"GetUserStat\n");
        *data = 0;
        return true;
    }

    virtual bool S_VIRTUAL GetUserStat(CSteamID steamIDUser, PCSTR name, float *data)
    {
        PrintConsole(L"GetUserStat\n");
        *data = 0;
        return true;
    }

    virtual bool S_VIRTUAL GetUserAchievement(CSteamID steamIDUser, PCSTR name, bool *achieved)
    {
        PrintConsole(L"GetUserAchievement\n");
        *achieved = true;
        return true;
    }

    virtual bool S_VIRTUAL GetUserAchievementAndUnlockTime(CSteamID steamIDUser, PCSTR name, bool *achieved, ULONG *unlockTime)
    {
        PrintConsole(L"GetUserAchievementAndUnlockTime\n");
        *achieved = true;
        *unlockTime = 0;
        return true;
    }

    virtual bool S_VIRTUAL ResetAllStats(bool achievementsToo)
    {
        PrintConsole(L"ResetAllStats\n");
        return true;
    }

    virtual SteamAPICall S_VIRTUAL FindOrCreateLeaderboard(
            PCSTR leaderboardName,
            LeaderboardSortMethod leaderboardSortMethod,
            LeaderboardDisplayType leaderboardDisplayType)
    {
        PrintConsole(L"FindOrCreateLeaderboard\n");
        return SteamAPICallInvalid;
    }

    virtual SteamAPICall S_VIRTUAL FindLeaderboard(PCSTR leaderboardName)
    {
        PrintConsole(L"FindLeaderboard\n");
        return SteamAPICallInvalid;
    }

    virtual PCSTR S_VIRTUAL GetLeaderboardName(SteamLeaderboard steamLeaderboard)
    {
        PrintConsole(L"GetLeaderboardName\n");
        return "LeaderboardName";
    }

    virtual int S_VIRTUAL GetLeaderboardEntryCount(SteamLeaderboard steamLeaderboard)
    {
        PrintConsole(L"GetLeaderboardEntryCount\n");
        mLastLeaderboard = steamLeaderboard;
        return 10;
    }

    virtual LeaderboardSortMethod S_VIRTUAL GetLeaderboardSortMethod(SteamLeaderboard steamLeaderboard)
    {
        PrintConsole(L"GetLeaderboardSortMethod\n");
        return LeaderboardSortMethodDescending;
    }

    virtual LeaderboardDisplayType S_VIRTUAL GetLeaderboardDisplayType(SteamLeaderboard steamLeaderboard)
    {
        PrintConsole(L"GetLeaderboardDisplayType\n");
        return LeaderboardDisplayTypeNumeric;
    }

    virtual SteamAPICall S_VIRTUAL DownloadLeaderboardEntries(SteamLeaderboard steamLeaderboard, LeaderboardDataRequest leaderboardDataRequest, int rangeStart, int rangeEnd)
    {
        PrintConsole(L"DownloadLeaderboardEntries\n");
        return SteamAPICallInvalid;
    }

    virtual SteamAPICall S_VIRTUAL DownloadLeaderboardEntriesForUsers(SteamLeaderboard hSteamLeaderboard, CSteamID *prgUsers, int cUsers )
    {
        PrintConsole(L"DownloadLeaderboardEntriesForUsers\n");
        return SteamAPICallInvalid;
    }

    virtual bool S_VIRTUAL GetDownloadedLeaderboardEntry(
            SteamLeaderboardEntries steamLeaderboardEntries,
            int index,
            LeaderboardEntry *leaderboardEntry,
            LONG *details,
            int detailsMax)
    {
        PrintConsole(L"GetDownloadedLeaderboardEntry\n");
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
        PrintConsole(L"UploadLeaderboardScore\n");
        return SteamAPICallInvalid;
    }

    virtual SteamAPICall S_VIRTUAL AttachLeaderboardUGC( SteamLeaderboard hSteamLeaderboard, ULONG64 hUGC )
    {
        PrintConsole(L"AttachLeaderboardUGC\n");
        return SteamAPICallInvalid;
    }

    virtual SteamAPICall S_VIRTUAL GetNumberOfCurrentPlayers()
    {
        PrintConsole(L"GetNumberOfCurrentPlayers\n");
        return SteamAPICallInvalid;
    }

    virtual SteamAPICall S_VIRTUAL RequestGlobalAchievementPercentages()
    {
        PrintConsole(L"RequestGlobalAchievementPercentages\n");
        return SteamAPICallInvalid;
    }

    virtual int S_VIRTUAL GetMostAchievedAchievementInfo( char *pchName, ULONG unNameBufLen, float *pflPercent, bool *pbAchieved )
    {
        PrintConsole(L"GetMostAchievedAchievementInfo\n");
        *pflPercent = 100;
        *pbAchieved = true;
        return 0;
    }

    virtual int S_VIRTUAL GetNextMostAchievedAchievementInfo( int iIteratorPrevious, char *pchName, ULONG unNameBufLen, float *pflPercent, bool *pbAchieved )
    {
        PrintConsole(L"GetNextMostAchievedAchievementInfo\n");
        ZeroMemory(pchName, unNameBufLen);
        *pflPercent = 100;
        *pbAchieved = true;
        return 0;
    }

    virtual bool S_VIRTUAL GetAchievementAchievedPercent( PCSTR pchName, float *pflPercent )
    {
        PrintConsole(L"GetAchievementAchievedPercent\n");
        *pflPercent = 100;
        return false;
    }

    virtual SteamAPICall S_VIRTUAL RequestGlobalStats( int nHistoryDays )
    {
        PrintConsole(L"RequestGlobalStats\n");
        return SteamAPICallInvalid;
    }

    virtual bool S_VIRTUAL GetGlobalStat( PCSTR pchStatName, LONG64 *pData )
    {
        PrintConsole(L"GetGlobalStat\n");
        return false;
    }

    virtual bool S_VIRTUAL GetGlobalStat( PCSTR pchStatName, double *pData )
    {
        PrintConsole(L"GetGlobalStat\n");
        return false;
    }

    virtual LONG S_VIRTUAL GetGlobalStatHistory( PCSTR pchStatName, LONG64 *pData, ULONG cubData )
    {
        PrintConsole(L"GetGlobalStatHistory\n");
        return 0;
    }

    virtual LONG S_VIRTUAL GetGlobalStatHistory( PCSTR pchStatName, double *pData, ULONG cubData )
    {
        PrintConsole(L"GetGlobalStatHistory\n");
        return 0;
    }
};

struct ISteamRemoteStorage
{
    virtual bool S_VIRTUAL FileWrite(PCSTR FileName, PVOID Data, LONG Size)
    {
        PrintConsole(L"FileWrite: %S\n", FileName);
        return true;
    }

    virtual LONG S_VIRTUAL FileRead(PCSTR FileName, PVOID Data, LONG Size)
    {
        PrintConsole(L"FileRead: %S\n", FileName);
        return 0;
    }

    virtual bool S_VIRTUAL FileForget(PCSTR FileName)
    {
        PrintConsole(L"FileForget: %S\n", FileName);
        return true;
    }

    virtual bool S_VIRTUAL FileDelete( PCSTR FileName )
    {
        PrintConsole(L"FileDelete: %S\n", FileName);
        return true;
    }

    virtual SteamAPICall S_VIRTUAL FileShare( PCSTR FileName )
    {
        PrintConsole(L"FileShare: %S\n", FileName);
        return SteamAPICallInvalid;
    }

    virtual bool S_VIRTUAL SetSyncPlatforms( PCSTR FileName, LONG eRemoteStoragePlatform )
    {
        PrintConsole(L"SetSyncPlatforms: %S\n", FileName);
        return true;
    }

    virtual ULONG64 S_VIRTUAL FileWriteStreamOpen( PCSTR FileName )
    {
        PrintConsole(L"FileWriteStreamOpen: %S\n", FileName);
        return 0;
    }

    virtual bool S_VIRTUAL FileWriteStreamWriteChunk( ULONG64 writeHandle, const void *pvData, LONG cubData )
    {
        PrintConsole(L"FileWriteStreamWriteChunk\n");
        return false;
    }

    virtual bool S_VIRTUAL FileWriteStreamClose( ULONG64 writeHandle )
    {
        PrintConsole(L"FileWriteStreamClose\n");
        return false;
    }

    virtual bool S_VIRTUAL FileWriteStreamCancel( ULONG64 writeHandle )
    {
        PrintConsole(L"FileWriteStreamCancel\n");
        return false;
    }

    virtual bool S_VIRTUAL FileExists( PCSTR FileName )
    {
        PrintConsole(L"FileExists: %S\n", FileName);
        return false;
    }

    virtual bool S_VIRTUAL FilePersisted( PCSTR FileName )
    {
        PrintConsole(L"FilePersisted: %S\n", FileName);
        return false;
    }

    virtual LONG S_VIRTUAL GetFileSize( PCSTR FileName )
    {
        PrintConsole(L"GetFileSize: %S\n", FileName);
        return 0;
    }

    virtual LONG64 S_VIRTUAL GetFileTimestamp( PCSTR FileName )
    {
        PrintConsole(L"GetFileTimestamp: %S\n", FileName);
        return 0;
    }

    virtual LONG S_VIRTUAL GetSyncPlatforms( PCSTR FileName )
    {
        PrintConsole(L"GetSyncPlatforms: %S\n", FileName);
        return 0;
    }

    virtual LONG S_VIRTUAL GetFileCount()
    {
        PrintConsole(L"GetFileCount\n");
        return 0;
    }

    virtual PCSTR S_VIRTUAL GetFileNameAndSize( int iFile, LONG *pnFileSizeInBytes )
    {
        PrintConsole(L"GetFileNameAndSize\n");
        *pnFileSizeInBytes = 0;
        return "";
    }

    virtual bool S_VIRTUAL GetQuota( LONG *pnTotalBytes, LONG *puAvailableBytes )
    {
        PrintConsole(L"GetQuota\n");
        *pnTotalBytes = 0x10000000;
        *puAvailableBytes = 0x10000000;
        return true;
    }

    virtual bool S_VIRTUAL IsCloudEnabledForAccount()
    {
        PrintConsole(L"IsCloudEnabledForAccount\n");
        return true;
    }

    virtual bool S_VIRTUAL IsCloudEnabledForApp()
    {
        PrintConsole(L"IsCloudEnabledForApp\n");
        return true;
    }

    virtual void S_VIRTUAL SetCloudEnabledForApp( bool bEnabled )
    {
        PrintConsole(L"SetCloudEnabledForApp\n");
    }

    virtual SteamAPICall S_VIRTUAL UGCDownload( ULONG64 hContent, ULONG unPriority )
    {
        PrintConsole(L"UGCDownload\n");
        return SteamAPICallInvalid;
    }

    virtual bool S_VIRTUAL GetUGCDownloadProgress( ULONG64 hContent, LONG *pnBytesDownloaded, LONG *pnBytesExpected )
    {
        PrintConsole(L"GetUGCDownloadProgress\n");
        return false;
    }

    virtual bool S_VIRTUAL GetUGCDetails( ULONG64 hContent, AppId_t *pnAppID, char **ppchName, LONG *pnFileSizeInBytes, CSteamID *pSteamIDOwner )
    {
        PrintConsole(L"GetUGCDetails\n");
        return false;
    }

    virtual LONG S_VIRTUAL UGCRead( ULONG64 hContent, void *pvData, LONG cubDataToRead, ULONG cOffset, LONG eAction )
    {
        PrintConsole(L"UGCRead\n");
        return 0;
    }

    virtual LONG S_VIRTUAL GetCachedUGCCount()
    {
        PrintConsole(L"GetCachedUGCCount\n");
        return 0;
    }

    virtual ULONG64 S_VIRTUAL GetCachedUGCHandle( LONG iCachedContent )
    {
        PrintConsole(L"GetCachedUGCHandle\n");
        return 0;
    }

};

//////////////////////////////////////////////////////////////////////////
// export
//////////////////////////////////////////////////////////////////////////


    static ISteamApps apps;

    static ISteamUserStats stat;

    static ISteamClient client;

    static ISteamRemoteStorage storage;

bool S_API SteamAPI_Init()
{
    PrintConsole(L"SteamAPI_Init\n");
    return true;
}

bool S_API SteamAPI_InitSafe()
{
    PrintConsole(L"SteamAPI_InitSafe\n");
    return false;
}

bool S_API SteamAPI_IsSteamRunning()
{
    PrintConsole(L"SteamAPI_IsSteamRunning\n");
    return true;
}

void S_API SteamAPI_RegisterCallResult(struct CallbackBase *callback, SteamAPICall apiCall)
{
    PrintConsole(L"SteamAPI_RegisterCallResult\n");
}

void S_API SteamAPI_RegisterCallback(struct CallbackBase *callback, int iCallback)
{
    PrintConsole(L"SteamAPI_RegisterCallback\n");
}

bool S_API SteamAPI_RestartAppIfNecessary(ULONG appId)
{
    PrintConsole(L"SteamAPI_RestartAppIfNecessary\n");
    return false;
}

void S_API SteamAPI_RunCallbacks()
{
    PrintConsole(L"SteamAPI_RunCallbacks\n");
}

void S_API SteamAPI_SetMiniDumpComment(PCSTR msg)
{
    PrintConsole(L"SteamAPI_SetMiniDumpComment\n");
}

void S_API SteamAPI_Shutdown()
{
    PrintConsole(L"SteamAPI_Shutdown\n");
}

void S_API SteamAPI_UnregisterCallResult(struct CallbackBase *callback, SteamAPICall apiCall)
{
    PrintConsole(L"SteamAPI_UnregisterCallResult\n");
}

void S_API SteamAPI_UnregisterCallback(struct CallbackBase *callback)
{
    PrintConsole(L"SteamAPI_UnregisterCallback\n");
}

void S_API SteamAPI_WriteMiniDump(ULONG exceptionCode, PVOID exceptionInfo, ULONG buildId)
{
    PrintConsole(L"SteamAPI_WriteMiniDump\n");
}

ISteamApps* S_API SteamApps()
{
    PrintConsole(L"SteamApps\n");
    return &apps;
}

ISteamUserStats* S_API SteamUserStats()
{
    PrintConsole(L"SteamUserStats\n");
    return &stat;
}

struct ISteamClient* S_API SteamClient()
{
    PrintConsole(L"SteamClient\n");
    return &client;
}

ISteamFriends* S_API SteamFriends()
{
    PrintConsole(L"SteamFriends\n");
    DebugBreakPoint();
    return nullptr;
}

ISteamGameServer* S_API SteamGameServer()
{
    PrintConsole(L"SteamGameServer\n");
    DebugBreakPoint();
    return nullptr;
}

ISteamNetworking* S_API SteamGameServerNetworking()
{
    PrintConsole(L"SteamGameServerNetworking\n");
    DebugBreakPoint();
    return nullptr;
}

ULONG64 S_API SteamGameServer_GetSteamID()
{
    PrintConsole(L"SteamGameServer_GetSteamID\n");
    return 251150;
}

bool S_API SteamGameServer_Init(ULONG ip, USHORT port, USHORT gamePort, USHORT spectatorPort, USHORT queryPort, ServerMode serverMode, PCSTR gameDir, PCSTR versionString)
{
    PrintConsole(L"SteamGameServer_Init\n");
    return true;
}

void S_API SteamGameServer_RunCallbacks()
{
    PrintConsole(L"SteamGameServer_RunCallbacks\n");
}

void S_API SteamGameServer_Shutdown()
{
    PrintConsole(L"SteamGameServer_Shutdown\n");
}

ISteamMatchmaking* S_API SteamMatchmaking()
{
    PrintConsole(L"SteamMatchmaking\n");
    DebugBreakPoint();
    return nullptr;
}

ISteamMatchmakingServers* S_API SteamMatchmakingServers()
{
    PrintConsole(L"SteamMatchmakingServers\n");
    DebugBreakPoint();
    return nullptr;
}

ISteamNetworking* S_API SteamNetworking()
{
    PrintConsole(L"SteamNetworking\n");
    DebugBreakPoint();
    return nullptr;
}

ISteamRemoteStorage* S_API SteamRemoteStorage()
{
    PrintConsole(L"SteamRemoteStorage\n");
    return &storage;
}

VOID S_API SteamScreenshots()
{
    PrintConsole(L"SteamScreenshots\n");
}
