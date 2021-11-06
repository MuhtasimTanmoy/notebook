# Linker

- After independent compilation of translation units to object file, linkers work to connect them as an executable.

-[ CppCon 2017: Michael Spencer “My Little Object File: How Linkers Implement C++”](https://www.youtube.com/watch?v=a5L66zguFe4)

- Object files
    - Ranges of unsplttable data (sections)
    - Names that reference those data (symbols)
    - List of modifications to that data ( relocations)

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

- [Minimal synthetic benchmark: LD vs gold vs LLVM LLD]()


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
    - 