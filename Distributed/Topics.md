# Distributed Systems

A distributed system is basically a network of autonomous systems/servers connected using a middleware which can share resources, capabilities, files and so on.

- Consistent Hashing
- Vector clocks 
- Quorum a
- Anti-entropy using Merkle trees
- Gossip-based membership protocol and failure detection.

Preserves symmetry and avoids having a centralized registry for storing membership and node liveness information.

Data replication is at the heart of making data durable and available in the presence of hardware failures such as machine crashes, disk failures, network partitions and clock skews. 

Popular implementations include those from etcd and consul. Next-generation distributed databases such as YugaByte DB, CockroachDB and TiDB use Raft for both leader election and data replication

The final value has to determined non-deterministically using heuristics such as Last-Writer-Wins (LWW) and Conflict Free Replicated Data Types (CRDT).

- Distributed systems are kept weakly consistent for performance
  - Input Speculation
  - Lag Compensation


# CRDT
 - Much of distributed computing focuses on the problem of how to prevent concurrent updates to replicated data. But another possible approach is optimistic replication, where all concurrent updates are allowed to go through, with inconsistencies possibly created, and the results are merged or "resolved" later. In this approach, consistency between the replicas is eventually re-established via "merges" of differing replicas.
  - Operation based 
  - State based 
  - However, there are practical differences. State-based CRDTs are often simpler to design and to implement; their only requirement from the communication substrate is some kind of gossip protocol. Their drawback is that the entire state of every CRDT must be transmitted eventually to every other replica, which may be costly. In contrast, operation-based CRDTs transmit only the update operations, which are typically small. However, operation-based CRDTs require guarantees from the communication middleware;that the operations are not dropped or duplicated when transmitted to the other replicas, and that they are delivered in causal order.


# Network Time Protocol

NTP stands for Network Time Protocol. It is used to synchronize the clocks on our computer to one standard time source. It is very useful in situations like bank transactions. Assume the following situation without the presence of NTP. Suppose you carry out a transaction, where your computer reads the time at 2:30 PM while the server records it at 2:28 PM. The server can crash very badly if it’s out of sync.

- Google's spanner database uses GPS syncronized atomic clock

- Netdate - update instantly ( A unix package) 

- NTP gradually update 
- One provider can be also a consumer

Stratum 1 -> Stratum 2 -> ...... -> Stratum 256

As category 1 Stratum is not publicly available, we can get from 2

- Stepping > once every minute
- Slewing > once every 17 minutes
- Insane Time > 17 minutes > not touching
- Drift > clock frequency different > sync
- Jitter >   difference between time provider & time consumer since the last time polling
- conf - server pool.ntp.org
- ntpdate to update in reasonable window

# Gossip Protocol
- A, B has some state. A sends it's state with version / timestamp. B checks updated, update it's and send back the one A lacks. A updates and sends acknowledgement.
- Kubernates depends on etcd
- Kafka, elastic search on zookeeper
- Three requirements for P2P
  - Group Membership
  - Failure detection/ Node status
  - Information Dissemination / Heartbeat

- State
  - Application State
    - Rack
    - Schema
    - Load
    - Severity
    - Status 
  - Heartbeat state
  - Endpoint state 
    - Collection of above two  
- Seed node added only at cluster setup
- Timeout value dynamically calculated
- Akka has cluster singleton
- Consul extension lifeguard

- [HashiCorp Memberlist](https://github.com/hashicorp/memberlist)
- [Rapid](https://github.com/lalithsuresh/rapid) 
  - Gossip with concensus
  - Kafka moving away from zookeeper which used for membership, failure detection 
- [Gossip Protocol](https://www.youtube.com/watch?v=MPfAekq4f5I&ab_channel=DistributedSystemsConference)
- [Gossip Protocol Attibutes](https://www.youtube.com/watch?v=FuP1Fvrv6ZQ&ab_channel=PlanetCassandra )
- [Gossip Protocol Android](https://github.com/leonardogcsoares/Gossip-Protocol-Android)