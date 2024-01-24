# Kafka

- Immutable append only log
- Kafka topic is partitions mainly, different message goes to different partition based on key
- Messages having same `key`` always end up in same partition, thereby strictly having order
- Messages having `NULL` will round robin in different partitions
- Kafka brokers and replication
- Kafka producer manages connection pools, network buffering, retransmition of messages when necessary, which partition the message should go to
- Kafka consumer with same config initiates rebalancing with same `group ID``
- Topic partitions gets assigned to each new in consumer group, like 10 topics to 10 consumer, the 11th will be idle
- In traditional message queue, you can scale the number of partitions but no ordering gureentee
- If a feature does not directly contribute to customer it is infrastructure, which will be provided by community

- Kafka connect to feed data
    - Source Connector
    - Sink Connector
- Schema Registry
- Kafka Streams
    - Manages ate arriving messages
    - Has specific time window
    - Maintains lookup tables
    - Does filtering, grouping, aggregating

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
        - Tool to impose plan, generate plan
        - Monitor, Plan and generate 
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



In traditional message processing, you apply simple computations on the messages -- in most cases individually per message.

In stream processing, you apply complex operations on multiple input streams and multiple records (ie, messages) at the same time (like aggregations and joins).

Furthermore, traditional messaging system cannot go "back in time" -- ie, the automatically delete messages after they got delivered to all subscribed consumers. In contrast, Kafka keeps the messages as it uses a pull based model (ie, consumer pull data out of Kafka) for a configurable amount of time. This allows consumers to "rewind" and consume messages multiple times -- or if you add a new consumer, it can read the complete history. This makes stream processing possible, because it allows for more complex applications. Furthermore, stream processing is not necessarily about real-time processing -- it's about processing infinite input stream (in contrast to batch processing that is applied to finite inputs).

And Kafka offers Kafka Connect and Streams API -- so it is a stream processing platform and not just a messaging/pub-sub system (even if it uses this in it's core).


# Resources
- [Kafka](https://hackernoon.com/thorough-introduction-to-apache-kafka-6fbf2989bbc1)