# Distributed Systems Concept and Design

A distributed system is one in which components located at networked computers communicate and coordinate their actions only by passing messages. 

This definition leads to the following especially significant characteristics of distributed systems: 
- concurrency of components
- lack of a global clock
- independent failures of components

The largest online game, EVE Online, utilises a client-server architecture where a single copy of the state of the world is maintained on a centralized server and accessed by client programs running on players’ consoles or other devices.

### System Models

- Computer clocks and timing events 
    - Each computer in a distributed system has its own internal clock, which can be used by local processes to obtain the value of the current time.
    - Therefore two processes running on different computers can each associate timestamps with their events.
    - However, even if the two processes read their clocks at the same time, their local clocks may supply different time values. 
    - This is because computer clocks drift from perfect time and, more importantly, their drift rates differ from one another. 
    - The term clock drift rate refers to the rate at which a computer clock deviates from a perfect reference clock. 
    - Even if the clocks on all the computers in a distributed system are set to the same time initially, their clocks will eventually vary quite significantly unless corrections are applied.

- Event ordering
- Failure model

- In Chapter 4, we present the Java interfaces to datagram and stream communication, which provide different degrees of reliability.

- Chapter 5 presents the request-reply protocol, which supports RMI. 
- Its failure characteristics depend on the failure characteristics of both processes and communication channels. 
- The protocol can be built from either datagram or stream communication. 
- The choice may be decided according to a consideration of simplicity of implementation, performance and reliability.

- Chapter 17 presents the `two-phase commit` protocol for transactions. It is designed to complete in the face of well-defined failures of processes and communication channels.

- The algorithm that we describe here is a `distance vector` algorithm. This will provide a basis for the discussion in Section 3.4.3 of the link-state algorithm that has been used since 1979 as the main routing algorithm in the Internet. 

- Routing in networks is an instance of the problem of path finding in graphs. Bellman’s shortest path algorithm, published well before computer networks were developed [Bellman 1957], provides the basis for the distance vector method. 

- Bellman’s method was converted into a distributed algorithm suitable for implementation in large networks by Ford and Fulkerson [1962], and protocols based on their work are often referred to as ‘Bellman–Ford’ protocols. 

- Skype: An example of an overlay network

- The remote procedure call (RPC) approach extends the common programming abstraction of the procedure call to distributed environments, allowing a calling process to call a procedure in a remote node as if it is local.

- Remote method invocation (RMI) is similar to RPC but for distributed objects, with added benefits in terms of using object-oriented programming concepts in distributed systems and also extending the concept of an object reference to the global distributed environments, and allowing the use of object references as parameters in remote invocations.

- Space uncoupling, in which the sender does not know or need to know the identity of the receiver(s), and vice versa. Because of this space uncoupling, the system developer has many degrees of freedom in dealing with change: participants (senders or receivers) can be replaced, updated, replicated or migrated.

- Time uncoupling, in which the sender and receiver(s) can have independent lifetimes. In other words, the sender and receiver(s) do not need to exist at the same time to communicate. This has important benefits, for example, in more volatile environments where senders and receivers may come and go.

- The core OS components and their responsibilities are:
Process manager: Creation of and operations upon processes. 

- A process is a unit of resource management, including an address space and one or more threads.
Thread manager: Thread creation, synchronization and scheduling. 

- Threads are schedulable activities attached to processes and are fully described in Section 7.4.

- Communication manager: Communication between threads attached to different processes on the same computer. Some kernels also support communication between threads in remote processes. Other kernels have no notion of other computers built into them, and an additional service is required for external communication. Section 7.5 discusses the communication design.

- Memory manager: Management of physical and virtual memory. Section 7.4 and Section 7.5 describe the utilization of memory management techniques for efficient data copying and sharing.

- Supervisor: Dispatching of interrupts, system call traps and other exceptions; control of memory management unit and hardware caches; processor and floating-point unit register manipulations. This is known as the Hardware Abstraction Layer in Windows. The reader is referred to Bacon [2002] and Tanenbaum [2007] for a fuller description of the computer-dependent aspects of the kernel.

- When a process executes application code, it executes in a distinct user-level address space for that application; when the same process executes kernel code, it executes in the kernel’s address space. 

- The process can safely transfer from a user-level address space to the kernel’s address space via an exception such as an interrupt or a system call trap – the invocation mechanism for resources managed by the kernel. 

- A system call trap is implemented by a machine-level TRAP instruction, which puts the processor into supervisor mode and switches to the kernel address space. When the TRAP instruction is executed, as with any type of exception, the hardware forces the processor to execute a kernel-supplied handler function, in order that no process may gain illicit control of the hardware.

- Programs pay a price for protection. Switching between address spaces may take many processor cycles, and a system call trap is a more expensive operation than a simple procedure or method call. We shall see in Section 7.5.1 how these penalties factor into invocation costs.