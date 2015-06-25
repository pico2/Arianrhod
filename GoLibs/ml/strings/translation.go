package strings

import (
    "unicode/utf8"
)

func
CustomCPToUnicodeN(
    CustomCP *codePageTableInfo,
    CustomCPString []byte,
)(
    UnicodeString String,
) {

    BytesInCustomCPString := uint(len(CustomCPString))

    if CustomCP.DBCSCodePage == false {
        TranslateTable := CustomCP.MultiByteTable

        for i := uint(0); i != BytesInCustomCPString; i++ {
            UnicodeString += String(string(rune(TranslateTable[CustomCPString[i]])))
        }

    } else {
        NlsCustomLeadByteInfo := CustomCP.TranslateTable
        TranslateTable := CustomCP.TranslateTable
        index := 0

        for BytesInCustomCPString != 0 {
            BytesInCustomCPString--

            if NlsCustomLeadByteInfo[CustomCPString[index]] != 0 {
                if BytesInCustomCPString == 0 {
                    break
                }

                Entry := uint(NlsCustomLeadByteInfo[CustomCPString[index]])
                UnicodeString += String(string(rune(TranslateTable[Entry + uint(CustomCPString[index + 1])])))

                index += 2
                BytesInCustomCPString--

            } else {

                UnicodeString += String(string(rune(CustomCP.MultiByteTable[CustomCPString[index]])))
                index++
            }

        }
    }

    return
}

func
UnicodeToCustomCPN(
    CustomCP *codePageTableInfo,
    UnicodeString_ String,
) (
    CustomCPString []byte,
) {

    Ucs16String := []uint16{}
    UnicodeString := string(UnicodeString_)

    for len(UnicodeString) > 0 {
        r, size := utf8.DecodeRuneInString(UnicodeString)
        UnicodeString = UnicodeString[size:]
        Ucs16String = append(Ucs16String, uint16(r))
    }

    CharsInUnicodeString := len(Ucs16String)

    if CustomCP.DBCSCodePage == false {
        TranslateTable := CustomCP.WideCharTable

        for i := 0; i != CharsInUnicodeString; i++ {
            CustomCPString = append(CustomCPString, byte(TranslateTable[Ucs16String[i]]))
        }

    } else {
        WideTranslateTable := CustomCP.WideCharTable
        index := 0

        for ; CharsInUnicodeString != 0; CharsInUnicodeString-- {
            MbChar := WideTranslateTable[Ucs16String[index]]
            index++

            if (MbChar & 0xFF00 != 0) {
                CustomCPString = append(CustomCPString, byte(MbChar >> 8))    // lead byte
            }

            CustomCPString = append(CustomCPString, byte(MbChar & 0xFF))
        }
    }

    return
}
