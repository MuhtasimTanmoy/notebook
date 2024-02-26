# Memory Profiler

- [Measuring memory usage in Rust](https://rust-analyzer.github.io/blog/2020/12/04/measuring-memory-usage-in-rust.html)
    - The application does too many short-lived allocations (instead of re-using the buffers) the `instrumenting the calls to allocation and deallocation approach`.
    - If in a steady state, the application uses too much memory, the `heap parsing` would work better for pointing out which data structures need most attention.

- [How to write heap memory profiler?](https://youtu.be/YB0QoWI-g8E)
- Goals
    - Cope with thousands or even millions of trace events per second
    - Ideally zero overhead when not used
    - Support for runtime attaching or similar

- Good to know
    - Prefer to use existing tracing frameworks
    - perf with sdt / uprobe
    - LLVM - Xray

- Steps
    - Inject custom code into application
    - Intercept call to heap allcoation, deallocation function
    - Backtrace deallocation and allcoation 
    - Tracing, profiling should be fast, Post process should be delayed.

- Target `functions`

```c++

// libc functions
malloc, free
realtoc, calloc
posix_memalign, aligned_alloc, vat loc

// libc++ functions
operator new, operator new[]]
operator delete, operator delete[]
Each with a couple of overloads, e.g. std: :atign_val_t

```
- Approach
    - use the `dynamic linker` to inject custom library code
    - `LD_PRELAOD=$(readlink -f path/to/lib.so) app`
    - `c++` does not define how linker works, it works on linux level
    - basically replacing library `malloc` call

- Good to know before understanding the code below    
    - learn about [`extern`](https://stackoverflow.com/questions/10422034/when-to-use-extern-in-c)
        - Declare anywhere, use that declared part
    - learn about [`dlsym`](https://pubs.opengroup.org/onlinepubs/7908799/xsh/dlsym.html#:~:text=DESCRIPTION,name%20as%20a%20character%20string.)
    - [Static cast vs reinterpret_cast](https://stackoverflow.com/questions/573294/when-to-use-reinterpret-cast)
    - `reinterpret_cast` is dangerous
        - `class object -> func(param one)` gets converted to `class::func(*this, param)`
    - `reinterpret_cast` can perform dangerous conversions because it can typecast any pointer to any other pointer
    - `reinterpret_cast` is used when you want to work with bits
    - the result of a `reinterpret_cast` cannot safely be used for anything other than being cast back to its original type
    - if we use this type of cast then it becomes `non-portable` product

```c++
#include <dlfcn.h> // dlsym
extern "C" {
    void* malloc(sizt_t size) {
        static void* original_malloc(RTLD_NEXT ,"malloc") ;
        assert(original_malloc);
        auto *original_malloc_fn = reinterpret_cast<decltype(&::malloc)> (original_malloc);
        void •ret = original_malloc_fn(size);
        fprtntf(stderr, "mattoc intercepted: gozu oop\n",
        size, ret);
        return ret;
    }
}
```
