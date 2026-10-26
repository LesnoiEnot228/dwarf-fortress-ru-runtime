# DFHack plugin

This directory is reserved for the C++ plugin. No runtime hook or plugin implementation is included yet.

Implementation is blocked on verifying the installed Dwarf Fortress and DFHack versions and auditing the upstream candidate. Do not add guessed API calls or ship an untested DLL. The first implementation should compile against the exact supported DFHack development environment and include a harmless enable/disable smoke test.
