# Cassandra

- Widely used as BASE, can be configured to ACID
- Supports lightweight transactions
- Consistent hashing for replication
- Paxos under the hood for transaction
- Every Cassandra machine handles a proportionate share of every activity in the system. There are no special cases like the HDFS namenode or MongoDB mongos that require special treatment or special hardware to avoid becoming a bottleneck.

- A log-structured engine that avoids overwrites to turn updates into sequential i/o is essential both on hard disks (HDD) and solid-state disks (SSD). 
- On HDD, because the seek penalty is so high; on SSD, to avoid write amplification and disk failure.

- Voldemort and Riak support pluggable storage engines, which both limits them to a lowest-common-denominator of key/value pairs, and limits the optimizations that can be done with the distributed replication engine.

- HBase has an integrated, log-structured storage engine, but relies on HDFS for replication instead of managing storage locally. 
- This means HBase is architecturally incapable of supporting Cassandra-style optimizations like putting the commitlog on a separate disk, or mixing SSD and HDD in a single cluster with appropriate data pinned to each.

- CASSANDRA’S STORAGE ENGINE WAS OPTIMIZED FOR SPINNING DISKS

- LSM 
    - Log structured merge tree
    - Commit
    - Flush
    - Compact

- All Disk writes are sequential

- Most popular data storage engines rewrite modified data in-place: MySQL (InnoDB), PostgreSQL, Oracle, MongoDB, Membase, BerkeleyDB, etc. Most perform similar buffering of writes before flushing to disk but flushes are RANDOM writes.

- With random access storage, cassandra LSM tree obsolete?

- SSD 
    - Cannot overwrite directly: must erase first, then write
    - Can write in small increments (4KB), but only erase in ~512KB blocks
    - Latency: write is ~100µs, erase is ~2ms
    - Limited durability: ~5,000 cycles (MLC) for each erase block
- Wear leveling

## Resources
- [Cassandra](https://www.datastax.com/blog/2012-review-performance)
- [Cassandra Slide](https://www.slideshare.net/rbranson/cassandra-and-solid-state-drives)