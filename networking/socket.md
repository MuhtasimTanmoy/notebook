# Socket

The term socket is analogous to physical female connectors, communication between two nodes through a channel being visualized as a cable with two male connectors plugging into sockets at each node. Similarly, the term port (another term for a female connector) is used for external endpoints at a node, and the term socket is also used for an internal endpoint of local inter-process communication (IPC) (not over a network). However, the analogy is limited, as network communication need not be one-to-one or have a dedicated communication channel.

- Sockets are assumed to be associated with a specific socket address, namely the IP address and a port number for the local node

Associating a socket with a socket address is called binding.

## Unix Domain Socket

A Unix domain socket or IPC socket (inter-process communication socket) is a data communications endpoint for exchanging data between processes executing on the same host operating system.

- A pair of process communicating over a network employ a pair of sockets.

- Socket = IP + Port Number

- Like named pipes, Unix domain sockets support:

- Types
    - Transmission of a reliable stream of bytes (SOCK_STREAM, compare to TCP).
    - Ordered and reliable transmission of datagrams (SOCK_SEQPACKET, compare to SCTP)
    - Unordered and unreliable transmission of datagrams (SOCK_DGRAM, compare to UDP).
    The Unix domain socket facility is a standard component of POSIX operating systems.

## Why use UDP instead of TCP

IP sockets (especially TCP/IP sockets) are a mechanism allowing communication between processes over the network. In some cases, you can use TCP/IP sockets to talk with processes running on the same computer (by using the loopback interface).

The API for Unix domain sockets is similar to that of an Internet socket, but rather than using an underlying network protocol, all communication occurs entirely within the operating system kernel.

UNIX domain sockets know that they’re executing on the same system, so they can avoid some checks and operations (like routing); which makes them faster and lighter than IP sockets. So if you plan to communicate with processes on the same host, this is a better option than IP sockets.

UNIX domain sockets are subject to file system permissions, while TCP sockets can be controlled only on the packet filter level. As a result, it is much easier to regulate which users have access to a UNIX domain socket than it is for a TCP socket

- Note that concurrent connections are not the same as requests per second, though they are similar: handling many requests per second requires high throughput (processing them quickly), while high number of concurrent connections requires efficient scheduling of connections.

- In other words, handling many requests per second is concerned with the speed of handling requests, whereas a system capable of handling a high number of concurrent connections does not necessarily have to be a fast system, only one where each request will deterministically return a response within a (not necessarily fixed) finite amount of time.

- Common applications of very high number of connections include pub/sub servers, chat, file servers, web servers, and software-defined networking.

# Reference
- [Sockets in Operating System](https://www.youtube.com/watch?v=uagKTbohimU)
- https://en.wikipedia.org/wiki/Network_socket