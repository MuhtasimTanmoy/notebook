# Distributed Systems

Distributed System Categories 
1. Distributed Data Stores
2. Distributed Computing
3. Distributed File Systems
4. Distributed Messaging
5. Distributed Applications
6. Distributed Ledgers


# Concensus
- State machine replication based on log
- State Machine Replication Principle:
    -  Physical logging means logging the contents of each row that is changed. 
    - Logical logging means logging not the changed rows but the SQL commands that lead to the row changes

- Symmetric
    - Equal roles
    - Can contact any server
- Asymmetric
    - Leader base
    - Raft 

---    

- Distributed Data Stores
    - The concensus part can be separated as a service with ZooKeeper
    - Consistency Model
        - ACID
            - eg. HBase, Couchbase, Redis, Zookeeper.
        - BASE
            - eg. Databases — Cassandra, Riak, Voldemort.

- Distributed Computing
    - MapReduce (Legacy Now)      
- Distributed File Systems
    - HDFS
        - NameNode - Coordinator (In bittorrent Tracker)
        - Datanode - Store
        
- Distributed Application
    - Bittorent
        - Trackerless torrent: Protocol that did not rely on centralized trackers for gathering metadata and finding peers, but instead uses new algorithms. One such instance is Kademlia (Mainline DHT), a distributed hash table (DHT) that allows you to find peers through other peers. In effect, each user performs a tracker’s duties.

 ## References
 - [Concensus  Algorithm](https://blog.mi.hdm-stuttgart.de/index.php/2019/03/17/consensus-protocols-a-key-to-cluster-management/)
 - [Intro to distributed Systems](https://medium.com/better-programming/a-thorough-introduction-to-distributed-systems-3b91562c9b3c)