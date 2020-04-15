# Lamport TimeStamps
- https://towardsdatascience.com/understanding-lamport-timestamps-with-pythons-multiprocessing-library-12a6427881c6
Each node knows 
- it's events
- communication events

Local clock - Just a counter
Monotonic increase at own event times.
c_i(a)< c_i(b)

Message receipt time greater than spend time.
c_j(d) = max(c_i(a)++, c_j(d))

Cant distinguish concurrent event

# vector clock
 Just array of lamport
 CRDT
 Causally related - One must be less and others equal or less
 Concurrent - One less , one more, one less / more

# Interval Tree Clock
- https://www.youtube.com/watch?v=q0QOYtSsTg4
- https://www.youtube.com/watch?v=PgCziibErvU 
- https://blog.separateconcerns.com/2017-05-07-itc.html
- https://towardsdatascience.com/understanding-lamport-timestamps-with-pythons-multiprocessing-library-12a6427881c6 (implementation)

Actor explosion - All unique identifier coming together modifying
- We need to track causality. In a nutshell, given two events modifying a given piece of data and originating from different nodes in the system, we want to know if one of those events could have influenced the other one, or in other words if one of those events "happened before" the other one.
- Version Vectors or Interval Tree Clocks

# Christian Algorithm
- https://www.youtube.com/watch?v=yvuy0rPkv8Q
Time Sync

# CRDT
 - Much of distributed computing focuses on the problem of how to prevent concurrent updates to replicated data. But another possible approach is optimistic replication, where all concurrent updates are allowed to go through, with inconsistencies possibly created, and the results are merged or "resolved" later. In this approach, consistency between the replicas is eventually re-established via "merges" of differing replicas.
  - Operation based 
  - State based 
  - However, there are practical differences. State-based CRDTs are often simpler to design and to implement; their only requirement from the communication substrate is some kind of gossip protocol. Their drawback is that the entire state of every CRDT must be transmitted eventually to every other replica, which may be costly. In contrast, operation-based CRDTs transmit only the update operations, which are typically small. However, operation-based CRDTs require guarantees from the communication middleware;that the operations are not dropped or duplicated when transmitted to the other replicas, and that they are delivered in causal order.


# Network Time Protocol
Netdate - update instantly
NTP gradually update - one provider can be also a consumer
Stratum 1 -> stratum 2 -> ...... -> stratum 256
As category 1 is not publicly available, we can get from 2
- Stepping > once every minute
- Slewing > once every 17 minutes
- Insane Time > 17 minutes > not touching
- Drift > clock frequency different > sync
- Jitter >   difference between time provider & time consumer since the last time polling
- conf - server pool.ntp.org
- ntpdate to update in reasonable window
