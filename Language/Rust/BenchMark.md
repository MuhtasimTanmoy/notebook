# Benchmark


- [CppCon 2017: Chandler Carruth “Going Nowhere Faster”
](https://www.youtube.com/watch?v=2EWejmkKlxs)
    - Demonstrates cache locality influence
    - Using `branching` instead of `cmove`

- [CppCon 2014: Chandler Carruth "Efficiency with Algorithms, Performance with Data Structures"](https://www.youtube.com/watch?v=fHNmRkzxHWs)
     - There is no power efficient instructions only execute quick and sleep
     - C++ doesn't give you performance, it gives you control over performance.
     - Discontiguous data structures are root of all poor performance.
     - Say no to linked list, `std:map` never
     - Time spent waiting for data ( 50% )
     - 
![](../images/Cache%20System.png)

- [C++ Quick Benchmark](https://quick-bench.com)
- [C++ Analysis](https://godbolt.org)