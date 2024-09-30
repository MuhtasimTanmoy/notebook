# NDK

- Generates `.so` library file
    - App Split to be used 
    - Code Obfuscation
    - Fast
    - Api Base or Key hide

- Components of NDK
    - ARM, x86, and MIPS Cross Compilers Build System
    - Java Native Interface Headers
    - C Library
    - Math Library
    - POSIX Threads
    - Minimal C++ Library
    - ZLib compression Library  
    - Dynamic linker Library
    - Android logging Library
    - Android pixel buffer Library
    - Android native application APIs
    - OpenGL ES 3D graphics library
    - OpenSL ES native audio library
    - OpenMAX AL minimal support

- `ndk-build:` This shell script is the starting point of the Android NDK build system. This chapter will cover ndk-build in detail while exploring the Android NDK build system. `.so` for a shared library, `.a` for static library.

- `ndk-gdb:` This shell script allows debugging native components using the GNU Debugger. Chapter 5 will cover ndk-gdb in detail while discussing the debugging of native components.

- `ndk-stack:` This shell script helps facilitate analyzing the stack traces that are produced when native components crash. Chapter 5 will cover the ndk-stack in detail while discussing the troubleshooting and crash dump analysis of native components.

- `build:` This directory contains the modules of the entire Android NDK build system. This chapter will cover the Android NDK build system in detail.

- `platforms:` This directory contains header files and libraries for each supported Android target version. These files are used automatically by the Android NDK build system based on the specified target version.

- `samples:` This directory contains sample applications to demonstrate the capabilities provided by the Android NDK. These sample projects are very useful for learning how to use the features provided by the Android NDK.

- `sources:` This directory contains shared modules that developers can import into their existing Android NDK projects.

- `toolchains:` This directory contains cross-compilers for different target machine architectures that the Android NDK currently supports. Android NDK currently supports ARM, x86, and MIPS machine architectures. The Android NDK build

- Dalvik vs ART
    - .dex (Dalvik Executable file) 
        - file is an android’s compiled code file. These .dex files are then zipped into a single .apk file.
    - .odex
        - file is created by the Android operating system to save space and increase the boot speed of an Android app (a .apk file).


- C++ vs Java
    - Java compiles to bytecode, and the bytecode compiles to native code by the JIT.
    - C compiles directly to native code.
    - With big heaps on Java, GC time increases, adding stall time. 
    - In some software, it is OK with stall times during the GC cleanup cycle, in others it causes fatal errors. 
    - Try keeping your software to respond under a defined number of milliseconds when a GC happens, and you will see what I'm talking about.
    - With big heaps on Java, GC time increases, adding stall time. 
    - In some software, it is OK with stall times during the GC cleanup cycle, in others it causes fatal errors. 
    - Try keeping your software to respond under a defined number of milliseconds when a GC happens, and you will see what I'm talking about.
    - In some extreme cases, the JIT may also choose not to JIT the code at all. 
    - This happens when a JITed method would be too big, 8K if I remember correctly. A non JITed method has a runtime penalty in the range of 20000% (200 times slower that is, at least at our customer it was). 
    - JIT is also turned off when the JVMs CodeCache starts to get full (if keep loading new classes into the JVM over and over again this can happen, also happen at the customer site). 
    - At one point JIT statistics also reduced concurrency on one 128-core machine to single-core performance.
    - No selecting C over Java will not make your program faster
    - Typical good candidates for the NDK are self-contained, CPU-intensive operations that don't allocate much memory, such as signal processing, physics simulation, and so on. Simply re-coding a method to run in C usually does not result in a large performance increase.
    - The NDK can, however, be an effective way to reuse a large corpus of existing C/C++ code.

### References
- [Dalvik vs ART](https://www.geeksforgeeks.org/difference-between-dalvik-and-art-in-android)