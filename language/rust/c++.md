# C++
- Library
    - Boost
    - std
    - abseil

### Constexpr
- [constexpr concept](https://www.geeksforgeeks.org/understanding-constexper-specifier-in-c)

- [CppCon 2015: Scott Schurr “constexpr: Introduction”](https://youtu.be/fZjYCQ8dzTc)
    - Moving computation from runtime to compile time
    - No synchronization concern
    - Can be applied in `value` or `computations`
    - [Incomplete]

### Template meta-programming
- Vector push is defensive in case of the move operation, using `no except` optimizes a lot
- If not fall to pre-c++11 and use a copy
- Perfect forwarding
- Reflection
- The `free` call frees the memory but not the pointer to that. So in production codebase `free Null` pattern arises
- Before, `move` semantics, `static_case<std::string&&>` would do the same
- `Literals` are assignable

- CPP Core guideline
    - https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines

### Backlogs

- By default `C++` exception does not capture their execution context (backtrace), so when a generic exception occurs you don’t know what code generated it.

- C++ has a lot of unsafe APIs and it is extremely easy to do unsafe operations like accessing a forbidden area in memory thanks to the pointer of trying to access an array/vector past its allocated area. This led to instability and a lot of time spent trying to find and fix the code.

- C++ has 3 ways to deal with objects: objects, references, and pointers. Each one has its pros and cons, it's not as obvious to use as you might think. A lot of errors are made using the wrong one and you spend more time thinking about this kind of stuff than in other languages.

- C++ polymorphism is a pain in the ass to use. It only fully works on smart pointers or shared pointers. C++ reference works, but only partially. And having to use pointers everywhere is annoying.

- C++ templates are extremely powerful but they are also very complex to use correctly and a lot of complexity comes with it.

- C++ lacks interfaces and true modules. The header mechanism is inefficient and verbose and the namespace mechanism is not as standardized and clear as in many other languages.

There are no standard package managers and repositories. If you stick to an operating system you can use say Debian packages and docker as an example. But nothing universal or self-contained in the language.

- Until recently (C++ 11) C++ had no lambda. Until C++ 14 lambda were quite verbose. They are still annoying to use and expressing something as callable for example is not as straightforward as it should be, in particular if you want to return a callable.

- C++ has still no easy introspection library.

- C++ compilation is very slow and C++ debugging too. Outside of very basic code, each time you debug a program or unit test you lose time compared to doing it in a language like Java or C++. Also, the available C++ build systems are more complex to use than what you find in other programming languages.

- If C++ uses AVL for its std::map and Rust uses red/black for its equivalent, then C++ would have faster lookups whereas Rust would have faster insert/remove.

- An intrusive list is one where the pointer to the next list node is stored in the same structure as the node data. This is normally A Bad Thing, as it ties the data to the specific list implementation. Most class libraries (for example, the C++ Standard Library) use non-intrusive lists, where the data knows nothing about the list (or other container) implementation.

### Snippet

``` shell
g++ -fdump-class-hierarchy a.cpp
```

![](./screen/rule-Of-five.png)

### References

- [Just Rust](https://www.youtube.com/watch?v=YtUfK3ZP3No&list=PLFCH6yhq9yAH28S_oGUtqO46eI7IAWdEO)
    - `Valgrind` can find memory errors, race condition
    - `Covety` static analysis, defect finding tool

- [Quroa c++ backlog](https://www.quora.com/Instead-of-inventing-a-ton-of-high-level-programming-languages-why-dont-people-implemented-C-C-frameworks-to-perform-high-level-repetitive-tasks)

- [Intrusive list](https://stackoverflow.com/questions/3361145/intrusive-lists)

- [Move semantics](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2006/n2027.html#Move_Semantics)

- [Perfect forwarding](http://thbecker.net/articles/rvalue_references/section_01.html)

- [lvalue rvalue](https://www.internalpointers.com/post/understanding-meaning-lvalues-and-rvalues-c)

- [Resource Management](https://www.youtube.com/watch?v=7Qgd9B1KuMQ)
    - Explains various C++ resource management
    - Free from a destructor
    - Copy constructor to copy heap
    - Assignment, copy and swap
    - Should have no exception thrown between allocation and free
    - Disable logging, then enable it should have no code or return in between

- [C++ Memory Model](https://www.youtube.com/watch?v=UNJrgsQXvCA)
    - Talks mainly about the C++ memory model
    - `move semantics` use case explain
    - `byte ordering` for c++

- [Type Erasure](https://www.youtube.com/watch?v=tbUCHifyT24)
    - https://stackoverflow.com/questions/18085331/recursive-lambda-functions-in-c14
    - [Incomplete]

- [CPPCon Slide Collection: ](https://github.com/CppCon/CppCon2019) contains cpp conference presentations on variour topic

- [CppCon 2017: Fedor Pikus “C++ atomics, from basic to advanced. What do they do?”](https://youtu.be/ZQFzMfHIxng)
    - Used for lock-free programming
    - Presentation application based
        - Mutex based
        - Lock-free / Wait-free
    - Any trivially copyable type can be made atomic
        - `x *= 2` is not atomic
        - `x = x + 1` is not atomic, same as `x++` unless x is atomic
        - `x = x * 2` is not atomic, these are two separate  atomic operation
        - no atomicity for floating point numbers.
        - Explicit `load`, `store`, `exchange`, and `compare_and_swap` are available
    - The concept of atomicity scales from a single instruction to whole program
        - Single add operation
        - Client seeing db state before after an update
    - Algorithm rules supreme
        - Should not delve into details of implementation too soon. The algorithm decides everything.
    - Lock-free but not wait-free version
        - ```c++
            std: atomic<int> x { 0 };
            int x0 = x;
            while( !x.compare_and_swap(x0, x0 + 1); )
 ```
        - Will continue while others change and add with the latest value only. Supports all sorts of operations
    - Atomics and locks generally provide a thread-safe way to do things
    - Benchmark different operations in lock vs mutex, `atomic operations vs normal vs spinlock`
    - Memory barriers

- More generally, this seems to be a common pattern in the Rust ecosystem:
    - A crate uses Mutex or other synchronization mechanism from std
    - Someone asks for `#[no_std]` support
    - Mutex is swapped for some variation of spinlock.
    - A Spinlock is the simplest possible implementation of a mutex, its general form looks like this:

- [C++ Compilation](https://www.toptal.com/c-plus-plus/c-plus-plus-understanding-compilation?utm_campaign=%5BPubs%5D%20Engineering_Newsletter_2023&utm_medium=email&_hsmi=248180607&_hsenc=p2ANqtz-_7pVoDAvGp_z7piCM2_U-vB-2RwtVBH3Ax6kLyDqDpxekdnJvshAHPz-ilRhwvNPuiOT6W-Q3uQqMTi-c9WanueNBOKQ&utm_content=248180607&utm_source=hs_automation)
- [Modern CPP Features](https://github.com/AnthonyCalandra/modern-cpp-features)