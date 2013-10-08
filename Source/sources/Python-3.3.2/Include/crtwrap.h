#ifndef _CRTWRAP_H_a43431ba_39ee_4de5_96d7_321def226964_
#define _CRTWRAP_H_a43431ba_39ee_4de5_96d7_321def226964_

#define strtok_s(_Str, _Delim, _Context) strtok(_Str, _Delim)
#define strcpy_s(_Dst, _DstSize, _Src) strncpy(_Dst, _Src, _DstSize)
#define _mktemp_s(_TemplateName, _Size) _mktemp(_TemplateName)
#define strcat_s(_Dst, _DstSize, _Src) strncat(_Dst, _Src, _DstSize)
#define fopen_s(_File, _Filename, _Mode) (*_File = fopen(_Filename, _Mode))
#define wcsncpy_s(_Dst, _DstSize, _Src, _MaxCount) wcsncpy(_Dst, _Src, _MaxCount)
#define wcsnlen_s(_Src, _MaxCount) wcslen(_Src)
#define __control87_2(_NewValue, _Mask, _X86_cw, _Sse2_cw) (*_X86_cw = _control87(_NewValue, _Mask))

#define ML_PYTHON   1

#endif // _CRTWRAP_H_a43431ba_39ee_4de5_96d7_321def226964_
