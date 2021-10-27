# Linker

- After independent compilation of translation units to object file, linkers work to connect them as an executable.

-[CppCon 2017: Michael Spencer “My Little Object File: How Linkers Implement C++”](https://www.youtube.com/watch?v=a5L66zguFe4)

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
