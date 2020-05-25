# ZeroMQ

- ZeroMQ comes with culture of minimalism.
- It’s sockets on steroids. It’s like mailboxes with routing. It’s fast!
- PUB-SUB sockets: you do not know precisely when a subscriber starts to get messages. Even if you start a subscriber, wait a while, and then start the publisher, the subscriber will always miss the first messages that the publisher sends. This is because as the subscriber connects to the publisher (some‐ thing that takes a small but nonzero amount of time), the publisher may already be sending messages out.
This “slow joiner” symptom hits enough people, often enough, that we’re going to ex‐ plain it in detail. Remember that ØMQ does asynchronous I/O (i.e., in the background). Say you have two nodes doing this, in this order:

### Why ZeroMQ
Many applications these days consist of components that stretch across some kind of network, either a LAN or the Internet. So, many application developers end up doing some kind of messaging. Some developers use message queuing products, but most of the time they do it themselves, using TCP or UDP. These protocols are not hard to use, but there is a great difference between sending a few bytes from A to B and doing messaging in any kind of reliable way.
- the “broker,” that does addressing, routing, and queuing.
- It handles I/O asynchronously, in background threads
- Components can come and go dynamically, and ØMQ will automatically reconnect.
- It queues messages automatically when needed.
- It lets your applications talk to each other over arbitrary transports: TCP, multicast, in-process, inter-process.
- It lets you route messages using a variety of patterns, such as request-reply and publish-subscribe.
- It does not impose any format on messages. They are blobs of zero bytes to gigabytes large. When you want to represent data you choose some other product on top, such as Google’s protocol buffers, XDR, and others.