# Rabbit MQ

AMQP is the core protocol for RabbitMQ (a Message Broker), but it also supports STORM, MQTT and HTTP through the use of plugins.
- STOMP 
    — a simple text based messaging protocol
- MQTT 
    — is a binary protocol known for its lightweight messaging
- HTTP 
    - It is not a messaging protocol, but management plugins in RabbitMQ use HTTP to send and receive messages.

There are three AMQP entities in RabbitMQ:
- Exchange
- Binding
- Queues

Messages published by a publisher are first received by the Exchange in RabbitMQ, then Exchanges will distribute message copies to Queues. To send appropriate messages to the appropriate queues, rules called Bindings are used.

## When delivery fails?
What happens when a message fails to deliver to a consumer? This can occur due to a network or application failure. If either of these failures was to occur, our system could potentially lose the message forever.

To address this issue, AMQP has a delivery acknowledgement mechanism in place. So a message will not be completely removed from a Queue unless we send a positive acknowledgment from the consumer. In the case of a negative acknowledgment, the message can be re-sent to the consumer or it can be dropped depending on the configuration settings by the publisher when sending the message.

One of the standard headers is called routing-key and it is this that the broker uses to match messages to queues. Each queue specifies a "binding key" and if that key matches the value of the routing-key header, the queue receives the message.

## RPC using MessageQueue
Client sends message to the queue, specifying: (a) a routing key that matches the service; and (b) the name of a queue to pick the response up from.
Exchange passes the message to the service's queue ("ops_q" in this case).
The queue pushes the message to the service, which then does some work and sends a response message back to the exchange, specifying a routing_key that matches the reply queue.
The client picks the response message off the reply queue.

As for the reply queue, it's typically created by the client, which then populates the reply_to header appropriately.

## Work Distribution
- Many clients

## PubSub
- Selective clients

## Resources
- [A Quick Guide To Understanding RabbitMQ & AMQP](https://medium.com/swlh/a-quick-guide-to-understanding-rabbitmq-amqp-ba25fdfe421d)
- [Understanding AMQP, the protocol used by RabbitMQ](https://spring.io/blog/2010/06/14/understanding-amqp-the-protocol-used-by-rabbitmq)
