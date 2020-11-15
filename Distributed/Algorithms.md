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
 - [Concensus  Algorithm](https://blog.mi.hdm-stuttgart.de/index.php/2019/03/17/consensus-protocols-a-key-to-cluster-management/)