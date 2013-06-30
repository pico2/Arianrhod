#pragma comment(linker, "/ENTRY:main2")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")

#include "MyLibrary.cpp"
#include <wlanapi.h>

// ²âÊÔÖÐÎÄ

#pragma comment(lib, "Wlanapi.lib")

Void main2(LongPtr argc, TChar **argv)
{
    BOOL                            Connected;
    ULONG                           NegotiatedVersion;
    HANDLE                          Client;
    PWLAN_INTERFACE_INFO_LIST       InterfaceList;
    PWLAN_INTERFACE_INFO            InterfaceInfo;
    PWLAN_AVAILABLE_NETWORK_LIST    NetworkList;
    PWLAN_AVAILABLE_NETWORK         Network;

    InterfaceList   = NULL;
    NetworkList     = NULL;
    Connected       = FALSE;

    WlanOpenHandle(WLAN_UI_API_VERSION, NULL, &NegotiatedVersion, &Client);
    WlanEnumInterfaces(Client, NULL, &InterfaceList);

    FOR_EACH(InterfaceInfo, InterfaceList->InterfaceInfo, InterfaceList->dwNumberOfItems)
    {
/*
        PrintConsoleW(L"%.*s\n", countof(InterfaceInfo->strInterfaceDescription), InterfaceInfo->strInterfaceDescription);

        switch (InterfaceInfo->isState)
        {
            case wlan_interface_state_not_ready:
                PrintConsoleW(L"Not ready\n");
                break;

            case wlan_interface_state_connected:
                PrintConsoleW(L"Connected\n");
                break;

            case wlan_interface_state_ad_hoc_network_formed:
                PrintConsoleW(L"First node in a ad hoc network\n");
                break;

            case wlan_interface_state_disconnecting:
                PrintConsoleW(L"Disconnecting\n");
                break;

            case wlan_interface_state_disconnected:
                PrintConsoleW(L"Not connected\n");
                break;

            case wlan_interface_state_associating:
                PrintConsoleW(L"Attempting to associate with a network\n");
                break;

            case wlan_interface_state_discovering:
                PrintConsoleW(L"Auto configuration is discovering settings for the network\n");
                break;

            case wlan_interface_state_authenticating:
                PrintConsoleW(L"In process of authenticating\n");
                break;

            default:
                PrintConsoleW(L"Unknown state %ld\n", InterfaceInfo->isState);
                break;
        }

        PrintConsoleW(L"\n");
*/
        if (InterfaceInfo->isState == wlan_interface_state_connected)
            break;

        WlanGetAvailableNetworkList(Client, &InterfaceInfo->InterfaceGuid, 0, NULL, &NetworkList);

        FOR_EACH(Network, NetworkList->Network, NetworkList->dwNumberOfItems)
        {
            if (Network->strProfileName[0] == 0)
                continue;

            //PrintConsoleW(L"%s\n", Network->strProfileName);

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

    Ps::ExitProcess(0);
}
