# Messaging
- Transfering bits of information to relevant places

# Kafka
- Dumb broker, Smart consumer Model
- Kafka does not attempt to track which messages were read by each consumer and only retain unread messages, rather, Kafka retains all messages for a set amount of time, and consumers are responsible for tracking their location in each log.
- Kafka uses Zookeeper to do leadership election of Kafka Broker and Topic Partition pairs.
- Topics are the logical categorization of messages in Kafka model. 
- Partition: A topic partition is a unit of parallelism in Kafka, i.e. two consumers cannot consume messages from the same partition at the same time. A consumer can consume from multiple partitions at the same time.
- You can think of a Topic as a feed name. A topic has a Log which is the topic’s storage on disk. A Topic Log is broken up into partitions and segments. The Kafka Producer API is used to produce streams of data records. The Kafka Consumer API is used to consume a stream of records from Kafka. A Broker is a Kafka server that runs in a Kafka Cluster. Kafka Brokers form a cluster. 
- Best effort delivery across process, tcp, udp, just once
- No ordering

Reference
- [Kafka: All you need to know](https://medium.com/hacking-talent/kafka-all-you-need-to-know-8c7251b49ad0)
- [Kafka Architecture](http://cloudurable.com/blog/kafka-architecture/index.html)


# RabbitMQ
- Smart broker, Dumb consumer Model

# ZooKeeper
- Zookeeper as a general purpose distributed process coordination system

# Nats

# ZooKeeper

- `Zookeeper` is a system for distributed cluster management. It is a distributed key-value store. It is highly-optimized for reads but writes are slower. It consists of an odd number of znodes known as an ensemble.

- zookeeper as the backbone for maintaining cluster state and leader election. Handles the `concensus` part.

- Zookeeper solves these problems using its magical tree structure file system called znodes, somewhat similar to the Unix file system. These znodes are analogous to folders and files in a Unix file system with some additional magical abilities :) Zookeeper provides primitive operations to manipulate these znodes, through which we will solve our distributed system problems.

- Split Brain Problem

Reference 
- [Zookeeper Doc](https://zookeeper.apache.org/doc/r3.5.7/zookeeperOver.html)
- [Distributed System Design with Zookeeper](https://medium.com/@bikas.katwal10zookeeper-introduction-designing-a-distributed-system-using-zookeeper-and-java-7f1b108e236)
- [Distributed Coordination](https://medium.com/hootsuite-engineering/distributed-coordination-with-zookeeper-247a62c900f1)
- [Why zookeeper needs odd number of nodes](https://medium.com/@bikas.katwal10/why-zookeeper-needs-an-odd-number-of-nodes-bb8d6020e9e9)

# ZeroMQ
