# Garbage Collection
Garbage collection (GC) is a form of automatic memory management. The garbage collector, or just collector, attempts to reclaim garbage, or memory occupied by objects that are no longer in use by the program. In large servers sometiems there is GC pause to reclaim memory.


### [Rethinking Garbage Collection](https://www.youtube.com/watch?v=Fte2pKMjgG0)

- Java compilation and execution goes through th below steps
    - JAVA Source File 
    - Static Compiler 
    - Class file
    - Runtime (JVM)
    - Bytecode Verifier 
    - JIT compiler 
    - Garbage Collection

Creating a new programming language
- Get your syntax right
- Make an interpreter 
- Static Compilation
- Then give that to JVM

- Usage Tradeoff
    - Highly Engineered Perforamant System - Exact and Tracing
        - Java, .NET
    - Non Performance Critical - Reference Counting and Conservative
        - PHP, Python

- GC Fundamental
    - Allocation
    - Identification
    - Reclamation

- Allocator
    - Free list
        - Class Based Object Allocation
    - Bump counting
        - Just a full heap. Allocation by incrementing pointer

- Identification
    - Tracing (Mark and Sweep)
        - Start from top (DFS). Those which are not reached garbage collected
        - Know about full heap
    - Reference Counting
        - Incoming reference count
        - Know about one object

- Reclaimation
  - Sweep to Free
  - Defragment Compaction > Mark compact
  - Evacuate

- Garbage Collector Algorithms

- Mark and Sweep
    - Free List + trace + Sweep to free
- Mark Compact
    - Bump Allocation + trace + Compact
- Semi Space 
    - Bump Allocation + trace + Evacuate
    - Half memory + Auto defragmented

- When choosing
    - Make the common case fast
    - Young objects die early
    - Two generational object tracing space 
        - Nursery
        - Mature
- Immix
    - An upper level hiererchy
    - Decrease checking
- Most object size 8-16 bytes
- Specification in software . Never think about implementation.
- Reference counting 30% slower than tracing
- RC immix - rust - bitc
- Tracing > cant identify dead object only live
- Concurrent real time system garbage collection

- Exapmple
    - Mostly copying collector - Apple UI Kit
    - BDW collector - Chakra VM - Mark sweep  - Free list

### References
- [Rethinking garbage collection](https://www.slideshare.net/rokon12/rethinking-garbage-collection-48598261)
- [Rethinking Garbage Collection by Dr. Rifat Shahriyar](https://www.youtube.com/watch?v=Fte2pKMjgG0)
- [Garbage Collection is Good!](https://www.infoq.com/presentations/garbage-collection-benefits)
- [Taking Off the Gloves with Reference Counting Immix](http://users.cecs.anu.edu.au/~steveb/pubs/papers/rcix-oopsla-2013.pdf)