# CockroachDB

![](./screen/CockroachDB.png)

- `CockroachDB` is mainly a distributed, replicated, transactional  key value store.

- [The Challenges of Writing a Massive and Complex Go Application](https://youtu.be/hWNwI5q01gI)
    - Design decisions while building cockroachDB
    - Gc cost is based on number of allocations, not number of bytes
    - Values thst are used together can be allocated in one struct
    - [Incomplete]
