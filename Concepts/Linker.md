# Linker

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