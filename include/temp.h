#pragma once

#ifdef _WIN32
  #define temp_EXPORT __declspec(dllexport)
#else
  #define temp_EXPORT
#endif

temp_EXPORT void temp();
