# MISC

### [Amethyst](https://github.com/amethyst/amethyst)
- For graphics [Render Engine](https://github.com/bjorn/tiled)
- From C++ to Rust, the game ecosystem moving towards
- ECS - Entity Component System

### [Bevy](https://github.com/bevyengine/bevy)
- Simple game engine. Easy to start

### [TiKV](https://github.com/tikv/tikv)
![](./screen/TiKV.png)
- TiKV is an open-source, distributed, and transactional key-value database.
- TiDB was built after Google F1 and TiKV after Google Spanner.
- Each node has RocksDB for Raft
- Uses Multiversion Concurrency Control

### [CockroachDB](https://github.com/cockroachdb/cockroach)
Traditional RDBMS, like PostgreSQL, that provide ACID guarantees, favor consistency over availability. BASE (Basic Availability, Soft-state, Eventual consistency) systems, like MongoDB and other NoSQL systems, favor availability over consistency. 

- Pessimistic
    - Lock and change
    - Two-phase lock
- Optimistic
    - First, perform change in a protected area, then change the current state. 
    - `MVCC` is one of that.
    - Core idea  - Database Version
    - Three Phases of Optimistic
        - Simulation
        - Validation
        - Commit 

### [NUM_CPUS](https://github.com/seanmonstar/num_cpus/)
- Different architecture of handle in rust
- Various os primitives to get logical & physical cores
![](./screen/CAP.png)


### [Worker Pool](https://github.com/inaka/worker_pool)

### References
- [Multiversion Concurrency Control](https://www.youtube.com/watch?v=sxabCqWsFHg)
- [MCC](https://en.wikipedia.org/wiki/Multiversion_concurrency_control) - Description Section Helpful 
- [CAP Keynote](https://awoc.wolski.fi/dlib/big-data/Brewer_podc_keynote_2000.pdf)