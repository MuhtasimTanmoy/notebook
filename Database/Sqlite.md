# SQLite
An "application file format" is the file format used to persist application state to disk or to exchange information between programs. It's alternative is `fopen`.

"file format" and an "application format". A file format is used to store a single object. So, for example, a GIF or JPEG file stores a single image, and an XHTML file stores text, so those are "file formats" and not "application formats". An EPUB file, in contrast, stores both text and images (as contained XHTML and GIF/JPEG files) and so it is considered an "application format". Sqlite file is application format.

## Full Text Search
    - FTS3 has smaller file, slower search
    - FTS4 has bigger file, faster search

- rowID
    - Integer Primary Key highly optimized

- Isolation
    - Journal mode
        - Changes are written directly into the database file, 
        while simultaneously a separate rollback journal file is constructed 
        that is able to restore the database to its original state if the transaction rolls back. Two times write.

        - In rollback mode, SQLite implements isolation by locking the database file and preventing any reads by other database connections while each write transaction is underway. 
        
        - Readers can be be active at the beginning of a write, before any content is flushed to disk and while all changes are still held in the writer's private memory space. But before any changes are made to the database file on disk, all readers must be (temporally) expelled in order to give the writer exclusive access to the database file. 
        
        - Readers are prohibited from seeing incomplete transactions by virtue of being locked out of the database while the transaction is being written to disk. Only after the transaction is completely written and synced to disk and commits are the readers allowed back into the database. Hence readers never get a chance to see partially written changes.
    
    - [WAL mode](https://www.sqlite.org/wal.html)

        - WAL mode permits simultaneous readers and writers. It can do this because changes do not overwrite the original database file, but rather go into the separate write-ahead log file. That means that readers can continue to read the old, original, unaltered content from the original database file at the same time that the writer is appending to the write-ahead log. In WAL mode, SQLite exhibits "snapshot isolation". When a read transaction starts, that reader continues to see an unchanging "snapshot" of the database file as it existed at the moment in time when the read transaction started. Any write transactions that commit while the read transaction is active are still invisible to the read transaction, because the reader is seeing a snapshot of database file from a prior moment in time.


- Without file param used as in memory database.
- Functional difference between STORED columns cannot be added using the `ALTER TABLE ADD COLUMN` command. 
- Only VIRTUAL columns can be added using `ALTER TABLE`.
- Strict Typed tables more common though dynamic type used by default in sqlite. If a type is not convertible then it stores as that.
- Partial indexing used in many case.

- The life-cycle of a prepared statement object usually goes like this:
    - Create the prepared statement object using sqlite3_prepare_v2().
    - Bind values to parameters using the sqlite3_bind_*() interfaces.
    - Run the SQL by calling sqlite3_step() one or more times.
    - Reset the prepared statement using sqlite3_reset() then go back to step 2. Do this zero or more times.
    - Destroy the object using sqlite3_finalize().

## Resources
- [VFS](https://www.sqlite.org/vfs.html)
- [FTS5](https://www.sqlite.org/fts5.html)
- [R-Tree](https://www.sqlite.org/rtree.html)
- [Architecture](https://www.sqlite.org/arch.html)
- [SQLite Performance Optimization](https://stackoverflow.com/questions/1711631/improve-insert-per-second-performance-of-sqlite)
- [Run Time Loadable Extension](https://www.sqlite.org/loadext.html)