# Concepts
- Another language has compile-time and run-time prevention of threading and memory corruption issues, while they abstract away my access to the machine. However, the C family language provides access with little in the way of safeguarding.
- C++ has local dialects that prevent understanding codebase, whereas Rust has a strict guideline

- Memory barriers
    - Can be used to prevent compilers from reordering operations, instructions for instruction-level parallelism

- [Precompiled Headers](https://gcc.gnu.org/onlinedocs/gcc/Precompiled-Headers.html)

- [Spinlock](https://github.com/CoffeeBeforeArch/spinlocks)
    - Other locks waiting to get to sleep
    - Spinlock polls in the loop for atomic bool to be available
    - Naive approach with very high l1-cache-load-misses
        - Four main categories of cache misses
            - Compulsory misses
                - Cold start
            - Capacity misses
                - Big chunk of memory
            - Conflict misses
                - Same set different portion modify
            - Coherence misses
                - The same variable in the cache line to get multiple access must invalidate all others
                - Spin locks mainly get this miss
                - Branching. cache line miss improved significantly by read-only copy with l1 cache miss due to coherence
    - After reading permission burst in lock acquire, which was solved by active back off
    - Passive backoff with built-in wait for efficient power consumption
    - Random backoff, Exponential backoff
    - Exponential backoff makes starving even worse. To prevent starvation, ticket-based lock.
    - Optimize write
    - The `volatile` keyword is used to prevent a variable from reading each time from the cache, as the valiue can be changed from anywhere else

- [Deep Copy vs Shallow Copy](https://stackoverflow.com/questions/24253344/is-it-possible-to-make-a-type-only-movable-and-not-copyable?rq=1)

-[SOLID](https://youtu.be/Ntraj80qN2k)

- misc
    - Friend function to access private variables or class
        - Used for testing
        - To introduce a function in lots of objects as super function that can access all variables, mutating an object from child to work as a parent