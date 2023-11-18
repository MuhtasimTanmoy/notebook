# Kafka

- Immutable append only log
- Kafka topic is partitions mainly, different message goes to different partition based on key
- Messages having same key always end up in same partition, thereby having order
- Messages having `NULL` will round robin in different partitions
- Kafka brokers and replication
- Kafka producer manages connection pools, network buffering, retransmit messages when necessary, which partition
- Kafka consumer with same config initiates rebalnacing with same group ID
- Topic partitions gets assigned to each new in consumer group, like 10 topics to 10 consumer, the 11th will be idle
- In traditional message queue, you can scale the number of partitions but no ordering gureentee
- If it directly not contribute to customer it is infrastructure, which will be provided by community, so dont contribute

- Kafka connect to feed data
    - Source Connector
    - Sink Connector
- Schema Registry
- Kafka Streams
    - Late arriving messages
    - Time window
    - Lookup tables
    - Filtering, grouping, aggregating

- Kafka Geo Replication
    - Confluent Multi Region CLuster
        - Single Stretch Cluster
        - Optimiaztion
            - Rack locality during consumer fetch
            - Async relication observers
            - ISR 
                - In sync replica
    - kafka Mirror maker
        - Offet not maintained
    - Confluent replicator
        - Replicator provides tool to embed in java app for offset translation
        - Mirrors metadata as well
    - Cluster Linking
        - No compression decompression

- Kafka elasticity
    - Kafka broker add job re distribution
    - How to balance clusters
        - Tootl to impose plan, generate plan
        - Monitort, Plan and generate 
        - SBC agent
    - JBOD RAID

- Kafka broker + storage
    - Tiered storage
    - Remote object store
        - Complete different path of fetch
    - Log retention time

- Log Compaction
- Transaction
    - Consumer Coordinator
    - Transaction Coordinator

- Durability, Availability, Ordering Guarenty