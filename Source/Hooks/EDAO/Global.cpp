#include "edao.h"

BOOL EDAO::CheckItemEquipped(ULONG ItemId, PULONG EquippedIndex)
{
    switch (ItemId)
    {
        case 0xB7:  // ú—Ä¿
        case 0xB8:  // ÌìÑÛ
        case 0xBB:  // Ì½Öª
            if (EquippedIndex != NULL)
                *EquippedIndex = 0;
        
            return TRUE;
    }
    
    return (this->*StubCheckItemEquipped)(ItemId, EquippedIndex);
}
