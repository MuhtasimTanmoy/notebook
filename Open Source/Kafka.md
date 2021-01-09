# Kafka

In traditional message processing, you apply simple computations on the messages -- in most cases individually per message.

In stream processing, you apply complex operations on multiple input streams and multiple records (ie, messages) at the same time (like aggregations and joins).

Furthermore, traditional messaging system cannot go "back in time" -- ie, the automatically delete messages after they got delivered to all subscribed consumers. In contrast, Kafka keeps the messages as it uses a pull based model (ie, consumer pull data out of Kafka) for a configurable amount of time. This allows consumers to "rewind" and consume messages multiple times -- or if you add a new consumer, it can read the complete history. This makes stream processing possible, because it allows for more complex applications. Furthermore, stream processing is not necessarily about real-time processing -- it's about processing infinite input stream (in contrast to batch processing that is applied to finite inputs).

And Kafka offers Kafka Connect and Streams API -- so it is a stream processing platform and not just a messaging/pub-sub system (even if it uses this in it's core).


# Resources
- [Kafka](https://hackernoon.com/thorough-introduction-to-apache-kafka-6fbf2989bbc1)