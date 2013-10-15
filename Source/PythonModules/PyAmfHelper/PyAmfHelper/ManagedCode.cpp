#include "Stdafx.h"

using namespace System;
using namespace System::Reflection;

array<BYTE, 1>^ LoadEmbededResource(String ^Name)
{
    auto stream = Assembly::GetExecutingAssembly()->GetManifestResourceStream(Name);
    auto buffer = gcnew array<BYTE, 1>(stream->Length);

    stream->Read(buffer, 0, stream->Length);

    return buffer;
}

Assembly^ CurrentDomain_AssemblyResolve(Object ^sender, ResolveEventArgs ^args)
{
    //Console::WriteLine(L"loading {0}", args->Name);
    return Assembly::Load(LoadEmbededResource(args->Name->Split(',', 1)[0] + L".dll"));
}

struct ManagedCodeInitializer
{
    ManagedCodeInitializer()
    {
        AppDomain::CurrentDomain->AssemblyResolve += gcnew ResolveEventHandler(CurrentDomain_AssemblyResolve);
    }
};

ManagedCodeInitializer initializer;
