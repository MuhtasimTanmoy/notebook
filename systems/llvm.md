# LLDB

```bash
lldb a.out
lldb -- a.out args

r   # run
c   # continue
n   # next line
s   # step into
bt  # backtrace

(lldb) break set -f test.cpp -l 30
(lldb) br set -f test.cpp -l 30
(lldb) b test.cpp : l
(lldb) br list
(lldb) br del
(lldb) p varname

... frame / fr var
... fr select / frame no
... watchpoint set variable globalVariable
... watchpoint set variable -w read | write | read_write globalVariable
```

- `gcc` & `llvm` are toolchain
    - Preprocess
    - Syntax mistake
    - Assemble object
    - Link into executable

## Precompiled Headers

- Precompiled headers are a general approach employed by many compilers to reduce compilation time.
- Consequently, compile times can often be greatly improved by caching some of the (redundant) work done by a compiler to process headers. 
- Precompiled header files, which represent one of many ways to implement this optimization, are literally files that represent an on-disk cache that contains the vital information necessary to reduce some of the work needed to process a corresponding header file. 
- While details of precompiled headers vary between compilers, precompiled headers have been shown to be highly effective at speeding up program compilation on systems with very large system headers (e.g., macOS).


## References
- [LLVM User Manual](https://clang.llvm.org/docs/UsersManual.html#terminology)
- [LLVM Grad Student](http://www.cs.cornell.edu/~asampson/blog/llvm.html)
- [LLVM Warning](https://softwareengineering.stackexchange.com/questions/122608/clang-warning-flags-for-objective-c-development/124574#124574)
    - `Wall` and `-Werror` at a minimum on any new code you are developing. Warnings added for good reasons, they find bugs.