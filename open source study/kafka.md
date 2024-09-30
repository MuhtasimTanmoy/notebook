# Kafka

- Immutable append-only log
- Kafka topic is partitions mainly, different message goes to different partition based on key
- Messages having the same `key`` always end up in same partition, thereby strictly having order
- Messages having `NULL` will round robin in different partitions
- Kafka brokers and replication
- Kafka producer manages connection pools, network buffering, retransmission of messages when necessary, which partition the message should go to
- Kafka consumer with the same config initiates rebalancing with the same `group ID``
- Topic partitions get assigned to each new consumer group, like 10 topics to 10 consumers, the 11th will be idle
- In a traditional message queue, you can scale the number of partitions but no ordering guarantee
- If a feature does not directly contribute to the customer it is infrastructure, which will be provided by the community

- Kafka connects to feed data
    - Source Connector
    - Sink Connector
- Schema Registry
- Kafka Streams
    - Manages ate arriving messages
    - Has a specific time window
    - Maintains lookup tables
    - Does filtering, grouping, aggregating

- Kafka Geo Replication
    - Confluent Multi Region CLuster
        - Single Stretch Cluster
        - Optimization
            - Rack locality during consumer fetch
            - Async replication observers
            - ISR 
                - In-sync replica
    - Kafka Mirror maker
        - Offset not maintained
    - Confluent replicator
        - Replicator provides a tool to embed in Java app for offset translation
        - Mirrors metadata as well
    - Cluster Linking
        - No compression decompression

- Kafka elasticity
    - Kafka broker add job re-distribution
    - How to balance clusters
        - Tool to impose plan, generate a plan
        - Monitor, Plan and generate 
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
- In traditional message processing, you apply simple computations on the messages -- in most cases individually per message.
- In stream processing, you apply complex operations on multiple input streams and multiple records (ie, messages) at the same time (like aggregations and joins).
- Furthermore, the traditional messaging system cannot go "back in time" -- ie, they automatically delete messages after they are delivered to all subscribed consumers. 
- In contrast, Kafka keeps the messages as it uses a pull-based model (ie, consumer pull data out of Kafka) for a configurable amount of time. This allows consumers to "rewind" and consume messages multiple times -- or if you add a new consumer, it can read the complete history. 
- This makes stream processing possible because it allows for more complex applications. 
- Furthermore, stream processing is not necessarily about real-time processing -- it's about processing an infinite input stream (in contrast to batch processing which is applied to finite inputs).
- And Kafka offers Kafka Connect and Streams API -- so it is a stream processing platform and not just a messaging/pub-sub system (even if it uses this at its core).


### References
- [Kafka](https://hackernoon.com/thorough-introduction-to-apache-kafka-6fbf2989bbc1)