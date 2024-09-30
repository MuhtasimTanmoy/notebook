# Enterprise Integration Patterns

- Pattern is the sweet spot of design. 

### Introduction
- Messaging enables data or commands to be sent across the network using a “send and forget” approach where the caller sends the information and then goes on to other work while the information is transmitted by the messaging system. Optionally, the caller can later be notified of the result through a callback.
- Fundamental challenges:
    - Networks are unreliable. Integration solutions have to transport data from one computer to another across networks. Compared to a process running on a single computer, distributed computing has to be prepared to deal with a much larger set of possible problems. 
    - Oftentimes, two systems to be integrated are separated by continents, and data between them has to travel through phone lines, LAN segments, routers, switches, public networks, and satellite links. Each of these steps can cause delays or interruptions.
    - Networks are slow. Sending data across a network is multiple orders of magnitude slower than making a local method call. Designing a widely distributed solution the same way you would approach a single application could have disastrous performance implications.
    - Any two applications are different. Integration solutions need to transmit information between systems that use different programming languages, operating platforms, and data formats. 
    - An integration solution needs to be able to interface with all these different technologies.
    - Change is inevitable. Applications change over time. An integration solution has to keep pace with changes in the applications it connects. 
    - Integration solutions can easily get caught in an avalanche effect of changes – if one system changes, all other systems may be affected. 
    - An integration solution needs to minimize the dependencies from one system to another by using loose coupling between applications.

- Solution
    - File Transfer
    - Shared Database
    - Remote procedure call
    - Messaging

### What is messaging?
- Messaging is a technology that enables high-speed, asynchronous, program-to-program communication with reliable delivery. 
- Programs communicate by sending packets of data called messages to each other. 
- Channels, also known as queues, are logical pathways that connect the programs and convey messages. 
- A channel behaves like a collection or array of messages, but one that is magically shared across multiple computers and can be used concurrently by multiple applications. - A sender or producer is a program that sends a message by writing the message to a channel. 
- A receiver or consumer is a program that receives a message by reading (and deleting) it from a channel.

### Why messaging?
- Now that we know what messaging is, we should ask: Why use messaging? 
- As with any sophisticated solution, there is no one simple answer. 
- The quick answer is that messaging is more immediate than File Transfer, better encapsulated than Shared Database, and more reliable than Remote Procedure Invocation. - However, that’s just the beginning of the advantages that can be gained using messaging.

6 root patterns
- Message Channel
- Message pipe and filters
- Message Router
- Message Translator
- Message Endpoint