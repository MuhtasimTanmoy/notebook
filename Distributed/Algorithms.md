# Paxos
Quoram Agreement


# Concensus
State machine replication based on log

State Machine Replication Principle:

-  Physical logging means logging the contents of each row that is changed. 
 
- Logical logging means logging not the changed rows but the SQL commands that lead to the row changes

- Symmetric
    - Equal roles
    - Can contact any server
- Asymmetric
    - Leader base
    - raft 

 ## References
 