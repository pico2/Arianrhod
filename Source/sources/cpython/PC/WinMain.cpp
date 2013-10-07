/* Minimal main program -- everything is loaded from the library. */

#include "../Modules/python.cpp"

int WINAPI wWinMain(
    HINSTANCE hInstance,      /* handle to current instance */
    HINSTANCE hPrevInstance,  /* handle to previous instance */
    LPWSTR lpCmdLine,         /* pointer to command line */
    int nCmdShow              /* show state of window */
)
{
    AppendPackage();
    return Py_Main(__argc, __wargv);
}
