#ifndef _TESVPATCHER_H_e842359a_b160_4980_8c82_e7b72a62aaf5_
#define _TESVPATCHER_H_e842359a_b160_4980_8c82_e7b72a62aaf5_

#include "Base.h"
#include "WindowManager.h"

class Patcher
{
public:
    Patcher();
    NTSTATUS Initialize();

protected:
    PVOID TESVBase;

    WindowManager window;
};

#endif // _TESVPATCHER_H_e842359a_b160_4980_8c82_e7b72a62aaf5_
