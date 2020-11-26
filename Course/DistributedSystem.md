# MIT Parralal & Distributed OS Group

- [**Course Link**](https://pdos.csail.mit.edu/6.824/schedule.html)

## Introduction
- Mapreduce explanation
- general Phinlosophy

## RPC & Threads
- Threads vs even driven asyncronous programming
- To get Parrelalism + IO Concurrency fill all thread equal to core with event driven loop.
- Go threads are cleverly run on one os thread.
- Code snippets in go crawler explained.

## GFS
- Two phase commit

## Primary-Backup Replication
- Multi core bad for replicated state machine

## Blockstack
- Cryptographic ACL needs Public Key Infrastructure
- Burn Address gets some fee for registering name
- Certificate Transparency

# Fault Tolerance
- Use of leader in distributed concensus
    - Original Paxos dnt have a leader
    - First round to elect a leadr, second to decide
    - In raft, leader elected. So speeds up by factor of two.
    - Sequence of leaders identified by followers using term.
    - Back up. Fast.
    - Log Compaction.
    - Linearizability - All concurrent parallal requests map to one dimention.

# ZooKeeper
- Raft usage requires explicit use in application which gives distributed concensus
- Zookeeper gives same as a co oord ination service
- zookeeper zab, raft like
- Writes linearizable, gives zxID, Read fifo client with zxID
- Primary backup system, not state machine replication.
- Configuration management through read locking `ready` file.
- Mini Transaction
    - Master state transfer, elect.
    - Test & Set.
- Api involves a naming system called 'zNodes'.
    - Regular permanent zNode
    - Ephimeral zNode - Client need to continuously end heartbeat to keep it
    - Sequential
- herd effect    

# CRAQ
- Chain Replication
- Maintains linearizability unlike zookeeper
- Uses configuration manager. Raft, Paxos, ZooKeeper.
- No worry about partition, split brain
  
# Aurora
- In each machine, Virtual machine monitor to monitor ec2
- Website is constructed of stateless services that get persistent data from DB.
- EC2 not good for DB. As not stateless like service.
- EBS volume are servers using CRAQ.
- Database on network generates lots of traffic.
- DB
    - Transation
    - Crash   Recovery 
- Instead of RDS architecture, aurora just sends log entries, ack from quoram only.    

# Frangipani
  - Cache coherence
  - Atomicity
  - Crash recovery
- Shared read lock
- Exclusive write lock 

Cache coherence lock to how updated write, Transactional to delay
  
WAL for crash recoverable transaction, Log on petal
 
# Distributed Transaction
Transaction
    - Concurrency control
     - Atomic commit
_ Serializable     

# Spanner




## Final Project
- Search 6.824

---- 

# [CSE 138](https://www.youtube.com/watch?v=G0wpsacaYpE&list=PLNPUF5QyWU8O0Wd8QDh9KaM1ggsxspJ31&ab_channel=LindseyKuper)

**Lecture 2**
- Distributed Systems = Partial Failure + Unbounded Latency
- Clock




# Waterloo

- Any big thing structure. Hiererchy 
- DNS
- Implicit hierarchy
- Ip addr geographically dispered
- Split up geo or data center 

----
