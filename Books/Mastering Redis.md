# Mastering Redis

Database features 
- Replication
- Tunable levels of durability
- Cluster
- High availability
- Latency Doctor


Redis Opearations
- `Set` primitive types
- Expiration set `EX`
- Persist normally
- `TTL` to query time
    - -1 for persist
    - -2 for expired
- List - ordered
    - RPUSH, LPUSH, LLEN, LRANGE, LPOP, and RPOP
- Set, Sorted Set, Hashes  
- PSubscribe , Publish, Subscribe

Commands
- DECR, DECRBY, DEL, EXISTS, EXPIRE, GET, GETSET, HDEL, HEXISTS, HGET, HGETALL, HINCRBY, HKEYS, HLEN, HMGET, HMSET, HSET, HVALS, INCR, INCRBY, KEYS, LINDEX, LLEN, LPOP, LPUSH, LRANGE, LREM, LSET, LTRIM, MGET, MSET, MSETNX, MULTI, PEXPIRE, RENAME, RENAMENX, RPOP, RPOPLPUSH, RPUSH, SADD, SCARD, SDIFF, SDIFFSTORE, SET, SETEX, SETNX, SINTER, SINTERSTORE, SISMEMBER, SMEMBERS, SMOVE, SORT, SPOP, SRANDMEMBER, SREM, SUNION, SUNIONSTORE, TTL, TYPE, ZADD, ZCARD, ZCOUNT, ZINCRBY, ZRANGE, ZRANGEBYSCORE, ZRANK, ZREM, ZREMRANGEBYSCORE, ZREVRANGE, ZSCORE

- Cache policy
    - Write through
    - Write back ****
    - LRU

# Resources
- Cluster Spec
   - https://redis.io/topics/cluster-spec
- Documentation
    - https://redis.io/documentation
- Commands
    - https://redis.io/commands
- Interactive
    - http://try.redis.io/    
- Scale Takeaway
    - https://www.youtube.com/watch?v=NymIgA7Wa78
- Redis placement
    - https://www.youtube.com/watch?v=U3RkDLtS7uY        