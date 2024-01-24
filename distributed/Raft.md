# Raft: A Distributed Consensus Algorithm

`Raft` utilizes a centralized leadership model, where one of the replicas in the cluster serves as the leader and the others act as followers.

The complete `Raft` model consists of four critical components:

- Consensus Module: the central algorithm module for consensus
- Log: the storage space for Raft logs
- State Machine: the repository for user data
- Transport: the network layer for communication


The six fundamental operations of Raft are:

- Leader Election
- Normal Operation
- Safety and consistency after a leader changes
- Deprecating former leaders
- Client Interaction
  - Linearizable Semantics, where each client interaction takes place once
- Configuration Changes
    - Adding or removing servers


Each server in the cluster can be in one of three states:
- Follower state
- Leader state
- Candidate state


The concept of `terms` is introduced, which divides time into periods where a specific server is a leader.

Each server maintains its current term and has only two RPCs and three persistent states.

![Raft](sc/raft.png)

The leader must regularly send empty heartbeats to all followers in the form of empty append entries. The election timeout is the span of time for choosing a leader, and safety is the liveliness of the leader election. A random timeout is eventually selected to complete the election.

### Logs
The committed log is persisted on disk on a majority of the servers. The leader never overwrites the log but appends to it. All future leaders must have all committed logs. The leader will not respond until the command has been logged, committed, and executed by the leader's state machine. Linearizability is guaranteed with a unique key. Configuration changes must go through two phases.

![Raft](sc/concensus.png)

### Term
A term is a duration for which a specific server acts as the leader. A new election begins a new term, and the Raft algorithm ensures that every term has a single leader.

### Notes
- Raft is not suitable for high-traffic services and is better suited for low-traffic scenarios where consistency is crucial, even if availability may suffer.

- Clients are aware of the network addresses of the replicas in the Raft cluster through some form of service discovery mechanism.

- `Raft` is not designed for high-throughput, fine-grained services as every client request incurs significant communication and persistence work between Raft replicas before a response is received by the client.

Potential use cases for Raft include:
- Implementing a lock server
- Electing leaders for higher-level protocols
- Replicating critical configuration data in a distributed system

Zookeeper is based on Zab (a protocol similar but not identical to Paxos), and etcd is built on top of Raft, the protocol discussed in this document.

Reference
- [Raft](https://www.pingcap.com/blog/implement-raft-in-rust)
- [Implementing raft](https://eli.thegreenplace.net/2020/implementing-raft-part-0-introduction)
- [Raft lecture](https://www.youtube.com/watch?v=YbZ3zDzDnrw&feature=youtu.be)
- [Raft Concensus](https://blog.container-solutions.com/raft-explained-part-1-the-consenus-problem)
- [Raft Paper](https://raft.github.io/raft.pdf)