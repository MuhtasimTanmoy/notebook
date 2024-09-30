# Kafka

- Immutable append-only log
- Kafka topic is partitions mainly, different message goes to different partitions based on key
- Messages having the same key always end up in the same partition, thereby having an order
- Messages having `NULL` will round robin in different partitions
- Kafka brokers and replication
- Kafka producer manages connection pools, network buffering, retransmits messages when necessary, which partition
- Kafka consumer with the same config initiates rebalancing with same group ID
- Topic partitions get assigned to each new consumer group, like 10 topics to 10 consumer, the 11th will be idle
- In a traditional message queue, you can scale the number of partitions but no ordering guarantee
- If it directly does not contribute to the customer it is infrastructure, which will be provided by the community, so don't contribute

- Kafka connects to feed data
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
        - Optimization
            - Rack locality during consumer fetch
            - Async replication observers
            - ISR 
                - In-sync replica
    - Kafka Mirror maker
        - Offer not maintained
    - Confluent replicator
        - Replicator provides a tool to embed in the Java app for offset translation
        - Mirrors metadata as well
    - Cluster linking
        - No compression decompression

- Kafka elasticity
    - Kafka broker add job re-distribution
    - How to balance clusters
        - Tootl to impose a plan, generate a plan
        - Monitor, Plan, and generate 
        - SBC agent
    - JBOD RAID

- Kafka broker + storage
    - Tiered storage
    - Remote object store
        - Complete different paths of fetch
    - Log retention time

- Log Compaction
- Transaction
    - Consumer Coordinator
    - Transaction Coordinator

- Durability, Availability, Ordering Guaranty