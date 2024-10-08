# Embedded Database

### Level DB
- Has too much mutex contention
- Bitcoin core, go ethereum uses it
- Sqlite used in past chrome, now uses leveldb
- Has different fork `rocksdb`, `hyperLevelDB`

### RocksDB
- Log Structured Merge Tree
- MemTable / SSTable
- InnoDB used in MySQL

### References
- [DropBox Engineering Evening on RocksDB with Dhruba Borthakur @ Rockset](https://www.youtube.com/watch?v=aKAJMd0iKtI&ab_channel=DhrubaBorthakur)

- [Embedded Database: RocksDB](youtube.com/watch?v=V_C-T5S-w8g)
    - Shows benchmark between SQLite, level DB, Kyoto TreeDB
    - `LevelDB` was good at random reads and random write
    - In the LSM database, the amount of data you can write is directly proportional to how fast you can compact.
    - The `Bloom filter` is not very useful when you do range caps
    - Prefix Scan for locality search
        - Range scans with the same key prefix
        - Blooms created for prefix
        - Reduce read amplification
    - Thread-aware compaction used on top of leveldb
    - `Write amplification` change. Compared to how many bytes you write to the database, how many times it needs to be re-written
    - `Read amplification` resolved
    - `Read modify write`

- [RockDB internals](https://www.youtube.com/watch?v=aKAJMd0iKtI)
    - Everything is pluggable
    - Each block has an index and filter block
        - Each block has a starting and end index in block to perform a binary search
        - Database shadowing

- [RocksDB Port](https://youtu.be/jGCv4r8CJEI)
    - MySQL, Mongo to use rocksdb as storage engine

- [LSM Tree](https://www.youtube.com/watch?v=V1iqN2ie__w)
    - `b+ tree` used when we need less search and insertion time
    - `lsm tree` when we have written an intensive dataset
    - Write 0(1), Read logn
    - Four key concepts
        - wal - write-ahead log
        - memorable - batching write
        - compaction - making efficient
        - bloom filters - to discard, make query efficient

- [LSM-based Storage Techniques Strengths and Trade-Offs (SDC 2019)](https://www.youtube.com/watch?v=V1iqN2ie__w)
    - To Be Continued