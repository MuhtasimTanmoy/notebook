# Mnesia

- [Documentation](https://www.erlang.org/doc/man/mnesia.html)
- [Users's guide](https://www.erlang.org/doc/apps/mnesia/mnesia.pdf)
- [Data Types](https://www.erlang.org/doc/reference_manual/data_types.html)

- A power of two number of fragments is simply related to the fact the default fragmentation module `mnesia_frag` uses linear hashing so using 2^n fragments assures that records are equally distributed (more or less, obviously) between fragments.

- Using disc_only_copies most of the time is spent in two operations:
    - Decide which fragment holds which record
    - Retrieve the record from corresponding dets table (Mnesia backend)

- A good solution could be to have more fragments and less records per fragment but trying at the same time to find the middle ground and not lose the advantages of some hard disk performance boosts like buffers and caches.

- Mnesia powers RABBITMQ


- [Heap memory overload](https://stackoverflow.com/questions/7103621/erlang-and-its-consumption-of-heap-memory)
