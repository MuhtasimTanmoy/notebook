# Concepts
- Other language has compile time and run-time prevention of threading and memory corruption issue, while they abstract away my access to machine. But, C family language provides access with little in the way of safeguard.
- C++ has local dialects that prevent understanding codebase, where rust has strict guideline

- Memory barriers
    - Can be used to prevent compilers to reorder operations, instructions for instructionn level parallelism

- [Precompiled Headers](https://gcc.gnu.org/onlinedocs/gcc/Precompiled-Headers.html)

- [Spinlock](https://github.com/CoffeeBeforeArch/spinlocks)
    - Other locks waiting to get to sleep
    - Spin lock polls in loop for atomic bool to be available
    - Naive approach very high l1-dcache-load-misses
        - Four main categories of cache misses
            - Compulsory misses
                - Cold start
            - Capacity misses
                - Big chunk of memory
            - Conflict misses
                - Same set different portion modify
            - Coherence misses
                - Same variable in cache line to get multiple access must invalidate all others
                - Spin locks mainly get this miss
                - Branching. cache line miss improved significantly by read only copy with l1 cache miss due to coherence
    - After read permission burst in lock acquire, which solved by active back off
    - Passive backoff with built in wait for efficient power consumption
    - Random backoff, Exponential backoff
    - Exponential backoff makes starving even worse. To prevent starving, ticket based lock.
    - Optimize write
    - `volatile` keyword used to prevent a variable to read each time from cache, as valiue can be changed from any where else

- [Deep Copy vs Shallow Copy](https://stackoverflow.com/questions/24253344/is-it-possible-to-make-a-type-only-movable-and-not-copyable?rq=1)

-[SOLID](https://youtu.be/Ntraj80qN2k)

- misc
    - Friend function to access private variables, or class
        - Used for testing
        - In order to introduce a function in lots of object as super function that can access all variables, mutating a object from child to work as parent