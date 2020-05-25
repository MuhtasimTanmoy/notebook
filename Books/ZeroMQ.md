# ZeroMQ

- ZeroMQ comes with culture of minimalism.
- It’s sockets on steroids. It’s like mailboxes with routing. It’s fast!
- PUB-SUB sockets: you do not know precisely when a subscriber starts to get messages. Even if you start a subscriber, wait a while, and then start the publisher, the subscriber will always miss the first messages that the publisher sends. This is because as the subscriber connects to the publisher (some‐ thing that takes a small but nonzero amount of time), the publisher may already be sending messages out.

### Why ZeroMQ
Many applications these days consist of components that stretch across some kind of network, either a LAN or the Internet. So, many application developers end up doing some kind of messaging. Some developers use message queuing products, but most of the time they do it themselves, using TCP or UDP. These protocols are not hard to use, but there is a great difference between sending a few bytes from A to B and doing messaging in any kind of reliable way.
- the “broker,” that does addressing, routing, and queuing.
- It handles I/O asynchronously, in background threads
- Components can come and go dynamically, and ØMQ will automatically reconnect.
- It queues messages automatically when needed.
- It lets your applications talk to each other over arbitrary transports: TCP, multicast, in-process, inter-process.
- It lets you route messages using a variety of patterns, such as request-reply and publish-subscribe.
- It does not impose any format on messages. They are blobs of zero bytes to gigabytes large. When you want to represent data you choose some other product on top, such as Google’s protocol buffers, XDR, and others.


## Socket and Patterns
ØMQ sockets are easy to digest. These sockets have a life in four parts, just like BSD sockets:

• We can create and destroy them, which go together to form a circle of socket life (see zmq_socket(), zmq_close()).

• We can configure them by setting options on them and checking them if necessary (see zmq_setsockopt(), zmq_getsockopt()).

• We can plug them into the network topology by creating ØMQ connections to and from them (see zmq_bind(), zmq_connect()).

• We can use them to carry data by writing and receiving messages on them (see zmq_msg_send(), zmq_msg_recv()).

- To create a connection between two nodes, you use zmq_bind() in one node and zmq_connect() in the other. As a general rule of thumb, the node that does zmq_bind() is a “server,” sitting on a well-known network address, and the node that does zmq_con nect() is a “client,” with unknown or arbitrary network addresses.

- We “bind a socket to an endpoint” and “connect a socket to an endpoint,” the endpoint being that well-known network address.

- One socket may have many outgoing and many incoming connections.

- ØMQ provides a set of unicast transports (inproc, ipc, and tcp) and multicast trans‐ ports (epgm, pgm).

- The HTTP request uses CRLF (carriage return line feed) as its simplest framing delimiter, whereas ØMQ uses a length-specified frame.

The built-in core ØMQ patterns are:

• Request-reply, which connects a set of clients to a set of services. This is a remote procedure call and task distribution pattern.

• Publish-subscribe, which connects a set of publishers to a set of subscribers. This is a data distribution pattern.

• Pipeline, which connects nodes in a fan-out/fan-in pattern that can have multiple steps and loops. This is a parallel task distribution and collection pattern.


# Advanced Request Reply pattern
