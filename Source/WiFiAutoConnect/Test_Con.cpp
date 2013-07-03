#pragma comment(linker, "/ENTRY:main2")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")

#include "MyLibrary.cpp"
#include <wlanapi.h>

#pragma comment(lib, "Wlanapi.lib")

LONG Connect()
{    
    BOOL                            Connected;
    WLAN_INTERFACE_STATE            State;
    ULONG                           ErrorCode, NegotiatedVersion;
    HANDLE                          Client;
    PWLAN_INTERFACE_INFO_LIST       InterfaceList;
    PWLAN_INTERFACE_INFO            InterfaceInfo;
    PWLAN_AVAILABLE_NETWORK_LIST    NetworkList;
    PWLAN_AVAILABLE_NETWORK         Network;

    InterfaceList   = NULL;
    NetworkList     = NULL;
    Connected       = FALSE;

    WlanOpenHandle(WLAN_UI_API_VERSION, NULL, &NegotiatedVersion, &Client);
    ErrorCode = WlanEnumInterfaces(Client, NULL, &InterfaceList);

    if (ErrorCode == NO_ERROR)
    FOR_EACH(InterfaceInfo, InterfaceList->InterfaceInfo, InterfaceList->dwNumberOfItems)
    {
        State = InterfaceInfo->isState;
        if (State == wlan_interface_state_connected)
            break;

        ErrorCode = WlanGetAvailableNetworkList(Client, &InterfaceInfo->InterfaceGuid, 0, NULL, &NetworkList);
        if (ErrorCode != NO_ERROR)
            continue;

        FOR_EACH(Network, NetworkList->Network, NetworkList->dwNumberOfItems)
        {
            if (Network->strProfileName[0] == 0)
                continue;

            ULONG                       Access;
            PWSTR                       ProfileXml;
            WLAN_CONNECTION_PARAMETERS  ConnectionParameters;

            ZeroMemory(&ConnectionParameters, sizeof(ConnectionParameters));

            ConnectionParameters.wlanConnectionMode = wlan_connection_mode_profile;
            ConnectionParameters.strProfile = Network->strProfileName;
            ConnectionParameters.dot11BssType = dot11_BSS_type_any;

            if (WlanConnect(Client, &InterfaceInfo->InterfaceGuid, &ConnectionParameters, NULL) == NO_ERROR)
            {
                Connected = TRUE;
                break;
            }
        }

        WlanFreeMemory(NetworkList);
        if (Connected)
            break;
    }

    WlanFreeMemory(InterfaceList);
    WlanCloseHandle(Client, NULL);

    if (ErrorCode == NO_ERROR && InterfaceList->dwNumberOfItems != 0)
        return State;

    return wlan_interface_state_not_ready;
}

Void main2(LongPtr argc, TChar **argv)
{
    ULONG_PTR Interval, MaxInterval, Step;

    MaxInterval = 5000;
    Step = 1000;

    Interval = 500;
    LOOP_FOREVER
    {
        LONG State;

        State = Connect();
        if (State == wlan_interface_state_connected)
        {
            if (Interval < MaxInterval)
            {
                Interval += Step;
                Interval = ML_MIN(MaxInterval, Interval);
            }
        }
        else
        {
            Interval = 500;
        }
        
        Ps::Sleep(Interval);
    }

    Ps::ExitProcess(0);
}
