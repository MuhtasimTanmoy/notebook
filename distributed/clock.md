# Lamport Timestamps

Each node knows 
- It's events
- Communication events

Local Clock 
- Just a counter
- Monotonic increase at own event times `c_i(a)< c_i(b)`

Message receipt time greater than spend time.
c_j(d) = max(c_i(a)++, c_j(d))

Cant distinguish concurrent event

- https://towardsdatascience.com/understanding-lamport-timestamps-with-pythons-multiprocessing-library-12a6427881c6


# Vector clock
 Just array of lamport

 CRDT

 Causally Related - One must be less and others equal or less

 Concurrent - One less, one more, one less / more

# Interval Tree Clock
- https://www.youtube.com/watch?v=q0QOYtSsTg4
- https://www.youtube.com/watch?v=PgCziibErvU 
- https://blog.separateconcerns.com/2017-05-07-itc.html
- https://towardsdatascience.com/understanding-lamport-timestamps-with-pythons-multiprocessing-library-12a6427881c6 (implementation)

Actor explosion 
- All unique identifier coming together modifying
- We need to track causality. In a nutshell, given two events modifying a given piece of data and originating from different nodes in the system, we want to know if one of those events could have influenced the other one, or in other words if one of those events "happened before" the other one.
- Version Vectors or Interval Tree Clocks

# Christian Algorithm
Time Sync
- https://www.youtube.com/watch?v=yvuy0rPkv8Q