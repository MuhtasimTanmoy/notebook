# Mnesia

- Mnesia combines many concepts found in traditional databases such as transactions and queries with concepts found in data management systems for telecommunications applications such as very fast realtime operations, configurable degree of fault tolerance (by means of replication) and the ability to reconfigure the system without stopping or suspending it.

- Mnesia is also interesting due to its tight coupling to the programming language Erlang, thus almost turning Erlang into a database programming language.

- This has many benefits, the foremost being that the impedance mismatch between data format used by the DBMS and data format used by the programming language which is being used to manipulate the data, completely disappears.

- Mnesia has four methods of reading from database: read, match_object, select, qlc.
    - `read` always uses a Key-lookup on the keypos. It is basically the key-value lookup.
    - `match_object` and select will optimize the query if it can on the keypos key. That is, it only uses that key for optimization. It never utilizes further index types.
    - `qlc` has a query-compiler and will attempt to use additional indexes if possible, but it all depends on the query planner and if it triggers. erl -man qlc has the details and you can ask it to output its plan.
- read is just a `key-value` lookup, also functions `index_read` and `index_write`

- A power of two number of fragments is simply related to the fact the default fragmentation module `mnesia_frag` uses linear hashing so using `2^n` fragments assures that records are equally distributed (more or less, obviously) between fragments.

- Using `disc_only_copies` most of the time is spent in two operations:
    - Decide which fragment holds which record
    - Retrieve the record from corresponding dets table (Mnesia backend)

- `DCD` and `DCL` files represent `disc_copies` tables. The `DCD` is an image of the contents from the latest time the table was "dumped", while the `DCL` contains a log of the side-effects made to that table since it was dumped. A dump creates a new `DCD` and removes the `DCL`.

- `DAT` files are `DETS:es` which contain `disc_only_copies` tables.

- `SCHEMA.DAT` is a special DETS that contains the schema for that Mnesia instance.

- `LATEST.LOG` is Mnesia's transaction log, which is periodically flushed to the updated tables.

- Applies argument `Fun` to all records in the table. 
- `Fun` is a function that takes a record of the old type and returns a transformed record of the new type. 
- Argument `Fun` can also be the atom ignore, which indicates that only the metadata about the table is updated. 
- Use of ignore is not recommended, but included as a possibility for the user do to an own transformation.

- `NewAttributeList` and `NewRecordName` specify the attributes and the new record type of the converted table. 

- Table name always remains unchanged. If `record_name` is changed, only the Mnesia functions that use table identifiers work, for example, `mnesia:write/3` works, but not `mnesia:write/1`.

- A good solution could be to have more fragments and less records per fragment but trying at the same time to find the middle ground and not lose the advantages of some hard disk performance boosts like buffers and caches.

- Very often start with a few `ETS` tables when prototyping (or even on early versions of features in production), then start finding places I need data serialized and on disk, then realize I need multiple indexes, etc. and wind up moving a lot of the data management stuff that was initially in ETS into Mnesia anyway. 

- If abstracted away the concept of data access properly it is not an issue to change the implementation of this part of your system either way. 

- If have select calls scattered throughout your modules, though, then probably have other architectural issues to sort out that are much more important than ETS vs Mnesia.

- Mnesia powers `RABBITMQ`

- Decision for choosing 
    - Multiple processes on multiple VMs -> mnesia
    - Multiple processes on one VM -> ets/dets
    - One process -> bag/dict/

- To load it on all nodes, command ("network load") instead of l in the Erlang shell for that
    - `nl(my_module).`


### References
- [Heap memory overload](https://stackoverflow.com/questions/7103621/erlang-and-its-consumption-of-heap-memory)
- [Observer API](https://anilwadghule.com/2021/07/11/how-to-install-wxmac-properly-for-running-observer-with-elixir)
- [Documentation](https://www.erlang.org/doc/man/mnesia.html)
- [Users's guide](https://www.erlang.org/doc/apps/mnesia/mnesia.pdf)
- [Data Types](https://www.erlang.org/doc/reference_manual/data_types.html)