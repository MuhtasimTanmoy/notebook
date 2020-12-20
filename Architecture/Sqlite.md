# SQLite

- Isolation
    - Journal mode
        - Changes are written directly into the database file, 
        while simultaneously a separate rollback journal file is constructed 
        that is able to restore the database to its original state if the transaction rolls back. 
        - In rollback mode, SQLite implements isolation by locking the database file and preventing any reads by other database connections while each write transaction is underway. Readers can be be active at the beginning of a write, before any content is flushed to disk and while all changes are still held in the writer's private memory space. But before any changes are made to the database file on disk, all readers must be (temporally) expelled in order to give the writer exclusive access to the database file. Hence, readers are prohibited from seeing incomplete transactions by virtue of being locked out of the database while the transaction is being written to disk. Only after the transaction is completely written and synced to disk and commits are the readers allowed back into the database. Hence readers never get a chance to see partially written changes.
    - [WAL mode](https://www.sqlite.org/wal.html)
        - Changes are written directly into the database file, while simultaneously a separate rollback journal file is constructed that is able to restore the database to its original state if the transaction rolls back. 
        - WAL mode permits simultaneous readers and writers. It can do this because changes do not overwrite the original database file, but rather go into the separate write-ahead log file. That means that readers can continue to read the old, original, unaltered content from the original database file at the same time that the writer is appending to the write-ahead log. In WAL mode, SQLite exhibits "snapshot isolation". When a read transaction starts, that reader continues to see an unchanging "snapshot" of the database file as it existed at the moment in time when the read transaction started. Any write transactions that commit while the read transaction is active are still invisible to the read transaction, because the reader is seeing a snapshot of database file from a prior moment in time.


- [VFS](https://www.sqlite.org/vfs.html)
- [FTS5](https://www.sqlite.org/fts5.html)
- [R-Tree](https://www.sqlite.org/rtree.html)