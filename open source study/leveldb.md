# [LevelDB](https://github.com/google/leveldb)

The leveldb library provides a persistent key-value store. Keys and values are arbitrary byte arrays. The keys are ordered within the key-value store according to a user-specified comparator function.

### Log Structured Merge Tree
- Target to have all information sorted on disk
- But random write is expensive
- When we receive stuff we store it first in a very small tree, not ordered. Append only. 
- In case of key-value merge values are put aside and the key and reference to those values are merged
- When something is written in riak you write it in three different stores, read from three, deal with the first two, and use a vector clock to determine the response. 
- Write sequentially, no overwrite, no random seek
- b+ tree , read write log(n) 
- linked list , read o(n) , write o(1)
- Use both, in the memory log  linked list, while persisting sorted
- In sorted chunks, whenever two of size 6 merge, known as log compaction.

### Multi-version concurrency control used in Postgres
- Write Amplification
    - Write Amplification is the ratio of actual data written to the flash vs data requested by the host to write to the device.
    - Write amplification occurs because the flash device is internally organized in pages and data can be written to it only on a page-by-page basis.  
- Skip list
    - Search a linked list better than 0(n). 
    - Regular linked list with express lane and normal lane. 
    - Time complexity: `o(sqrt(n))`

### References
- [Erlang Key value Store Talk](https://www.youtube.com/watch?v=vTzNKGbHzPc)
- [LSM Tree](https://www.youtube.com/watch?v=_5vrfuwhvlQ)