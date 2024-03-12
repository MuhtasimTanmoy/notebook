# Linking

- [Practical Application Of Weak Linking](https://stackoverflow.com/questions/15525537/what-are-practical-applications-of-weak-linking)

- [Plugin Architecture Dynamic Linking](https://forums.swift.org/t/weak-linking-in-swift-package-manager-plugin-architecture/49821)

- [Plugin Architecture](https://theswiftdev.com/modules-and-hooks-in-swift/)

- [Dynamically linking a library](https://theswiftdev.com/building-and-loading-dynamic-libraries-at-runtime-in-swift/)

- Static Linking
    - File Size Increase
    - No update as lib source code gets embedded

- Dynamic Linking
    - File Size Small
    - Update as only address goes into binary

- macOS
    - static: `.a`
    - dynamic: `.dylib`

- Linux
    - static: `.so`
    - dynamic: `.dylib`

- Windows
    - static: `.lib`
    - dynamic: `.dll`
    
### Linker
- A linker converts object files into executables and shared libraries. Let’s look at what that means. 
- For cases where a linker is used, the software development process consists of writing program code in some language: e.g., C or C++ or Fortran (but typically not Java, as Java normally works differently, using a loader rather than a linker). 
- A compiler translates this program code, which is human readable text, into into another form of human readable text known as assembly code. 
- Assembly code is a readable form of the machine language which the computer can execute directly. 
- An assembler is used to turn this assembly code into an object file. For completeness, 
- Some compilers include an assembler internally, and produce an object file directly
- Steps
    - `.cpp -> Preprocessor -> Compiler -> Assembler -> Linker -> Loader`
    - Compile flag `--save-temps` should generate all intermediate files
- After independent compilation of translation units to object file, linkers work to connect them as an executable
- static libraries (`.lib`, `.a`) used in linker, dynamic libraries (.dll, .so) used in loader

-[CppCon 2017: Michael Spencer “My Little Object File: How Linkers Implement C++”](https://www.youtube.com/watch?v=a5L66zguFe4)

- Object files
    - Ranges of unsplttable data (sections)
    - Names that reference those data (symbols)
    - List of modifications to that data ( [relocations](http://www.sco.com/developers/gabi/2003-12-17/ch4.reloc.html) )

- Dumptools
    - objdump
    - nm
    - llvm-readobj
    - readelf (ELF)
    - otool (mach O)
    - dumpbin (PECOFF)

- [LLD Linker](https://lld.llvm.org/index.html)
    - Atom Model
        - Generic
            - Name
            - Scope
            - Ordinal
        - Target Specific Attribute
    - Driver Model

- BFD Linker
- Gold Linker

- LLD Port
    - ELF (Unix) - Replacing (`/usr/bin/ld` / `-fuse-ld=lld`)
    - COFF (Windows)
    - Mach-O (Mac)

- [Linking archive file](https://stackoverflow.com/questions/48132989/how-to-take-only-required-object-files-inside-a-single-a-archive)
    - Linking and extracting from `.a` file.

- [LLD Benchmark](https://stackoverflow.com/questions/3476093/replacing-ld-with-gold-any-experience)

- [LLD Design](https://lld.llvm.org/NewLLD.html)
    - Visiting same archive file makes it slower
    - Mutully dependant `.a` file is harder to resolve.

- [Minimal synthetic benchmark: LD vs gold vs LLVM LLD](https://stackoverflow.com/questions/3476093/replacing-ld-with-gold-any-experience)

- [Address Relocation](https://stackoverflow.com/questions/3322911/what-do-linkers-do/33690144#33690144)
    - Compiler just leaves a placeholder, which gets populated in linking stage.

```asm
Register operands in 64-bit mode can be any of the following:
• 64-bit general-purpose registers (RAX, RBX, RCX, RDX, RSI, RDI, RSP, RBP, or R8-R15)
• 32-bit general-purpose registers (EAX, EBX, ECX, EDX, ESI, EDI, ESP, EBP, or R8D-R15D)
• 16-bit general-purpose registers (AX, BX, CX, DX, SI, DI, SP, BP, or R8W-R15W)
• 8-bit general-purpose registers: AL, BL, CL, DL, SIL, DIL, SPL, BPL, and R8L-R15L are available using REX
prefixes; AL, BL, CL, DL, AH, BH, CH, DH are available without using REX prefixes.
• Segment registers (CS, DS, SS, ES, FS, and GS)
• RFLAGS register
• x87 FPU registers (ST0 through ST7, status word, control word, tag word, data operand pointer, and instruction
pointer)
• MMX registers (MM0 through MM7)
• XMM registers (XMM0 through XMM15) and the MXCSR register
• Control registers (CR0, CR2, CR3, CR4, and CR8) and system table pointer registers (GDTR, LDTR, IDTR, and
task register)
• Debug registers (DR0, DR1, DR2, DR3, DR6, and DR7)
• MSR registers
• RDX:RAX register pair representing a 128-bit operand
```
- [ELF](https://cirosantilli.com/elf-hello-world#toc)

- [2016 EuroLLVM Developers' Meeting: R. Ueyama "New LLD linker for ELF"](https://www.youtube.com/watch?v=CYCRqjVa6l4)
    - Basic linking cat object files and relocation
    - Simulation of linking, undefined, defined, lazy

- [ELF Standard](https://cirosantilli.com/elf-hello-world#standards)
    - Two system calls from the linux kernel are relevant. The fork system call (or perhaps vfork or clone) is used to create a new process, similar to the calling one (every Linux user-land process except init is created by fork or friends). 
    - The execve system call replace the process address space by a fresh one (essentially by sort-of mmap-ing segments from the ELF executable and anonymous segments, then initializing the registers, including the stack pointer). 
    - The x86-64 ABI supplement and the Linux assembly howto give details
    - The dynamic linking happens after execve and involves the /lib/x86_64-linux-gnu/ld-2.13.so file, which for ELF is viewed as an "interpreter"
    - `The segments contain information needed at runtime, while the sections contain information needed during linking.`
    - Section contains static for the linker, segment dynamic data for the OS
    - File Header
    - Section Header
    - Data
    - Magic Number

- [How OS X Executes Applications](https://0xfe.blogspot.com/2006/03/how-os-x-executes-applications.html)
    - Library relocation problems, the first thing to do is run ldd on the executable
    - The ldd tool lists the dependent shared libraries that the executable requires, along with their paths if found

- [CppCon 2018: Matt Godbolt “The Bits Between the Bits: How We Get to main()”](https://youtu.be/dOfucXtyEsU)
    - Procedural Linkage Table
    - Global Object Table
    - static init function for each translation unit
    - Puts a pointer to this function into a section called init array
    - ARM instructions cant jump to long, so uses intermediate jump

- [In-depth: ELF - The Extensible & Linkable Format](https://www.youtube.com/watch?v=nC1U1LJQL8o)
    - Segments are runtime, sections are link time specific
    - Segment(Program Header e_phoff) contains multiple sections(Section Header e_shoff), also how to load that in memory
    - Sections are only used during linking, and used by debuggers
    - `sstrip` can be used to strip all sections, yet program runs
    - BSS means uninitialized data segment, initialized variables got to data segment
    - PIC, ASLR
    - The ELF specification: https://refspecs.linuxfoundation.org/elf/elf.pdf
    - elf.h from the Linux kernel: https://elixir.bootlin.com/linux/latest/source/include/uapi/linux/elf.h
    - How programs get run: https://lwn.net/Articles/631631
    - TLS: https://docs.oracle.com/cd/E19120-01/open.solaris/819-0690/chapter8-5/index.html
    - Relocation: https://refspecs.linuxbase.org/elf/gabi4+/ch4.reloc.html
    - sstrip: https://github.com/BR903/ELFkickers
 
- [Procedure Linakge Table](https://www.youtube.com/watch?v=Ss2e6JauS0Y)
    - Program Header Table
    - Section Header Table
    - Sections reside at bottom, can be stripped
    - static link : `gcc -static -fno-pie -no-pie -g -o a.out a.c`
    - All problems in computer science can be solved by additional layer of indirection.
    - Position inndependent code used for shared libraries by implementing relative addressing
    - Linker does two things
        - Symbol resoulution
        - Relocation
    - `.interop` section helps with dynamic linker
    - At linking step onlt the relocation and symbol table instruction embedded, the real data stores at load time.
    - Global Offset Table
    - Procedure Linkage Table
        - Resolves procedure
    - Test out program execution in GDB
        - Running this on a program with two `printf`    
        - ```
            gdb a.out
            b a.c:4
            b a.c:5
            r
            disas 'printf@plt'
            p/x *(void**)0x60101B
            readelf -hW a.out will keep track of addresses
            ```
    - Making common case fast is in the heart of system design


- [Before Main: How Executables Work on Linux](https://youtu.be/jR2hUhjcAXI)
    - Windows does not have distinction between sections and segments
    - Segments are composed of sections

- [CppCon 2017: Nir Friedman “What C++ developers should know about globals (and the linker)”](https://www.youtube.com/watch?v=xVT1y0xWgww&ab_channel=CppCon)

```bash
ldd /bin/ls
objdump -x /bin/ls

otool

# See Machine Code
objdump -dC /bin/ls

# See Machine Code with Relocation
objdump --reloc -dC /bin/ls

# See symbols of object file
objdump --syms -C /bin/ls
```