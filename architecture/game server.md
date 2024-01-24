# Gameserver

- Optimization for Gameserver
    - Better predictions
    - Eliminate the server for network latency
    - Optimize communication
    - Game data is compressed using delta compression to reduce network load. That means the server doesn't send a full world snapshot each time, but rather only changes (a delta snapshot) that happened since the last acknowledged update. With each packet sent between the client and server, acknowledge numbers are attached to keep track of their data flow. Usually full (non-delta) snapshots are only sent when a game starts or a client suffers from heavy packet loss for a couple of seconds. Clients can request a full snapshot manually with the cl_fullupdate command.


- [NAT Hole Punching](https://keithjohnston.wordpress.com/2014/02/17/nat-punch-through-for-multiplayer-games)
    - Required for connecting peer to peer after matchmaking

- [Research on Latency Problems and Solutions in Cloud Game!](https://www.researchgate.net/publication/337053541_Research_on_Latency_Problems_and_Solutions_in_Cloud_Game)

Layer-coding approach was proposed to separate the game image into two layers:  
- Base layer (contain  original  image  information) 
- Graphics enhancement  layer,  which  contains  graphics  enhancement  instructions:  light\map  rendering,  shading command, reflection computations, etc

### [EVE ONLINE!](http://uu.diva-portal.org/smash/get/diva2:408940/FULLTEXT01.pdf)
 - A type of shared-nothing-architecture in distributed computing, where each node is independent and does not communicate with other nodes.
 - Multiple programming paradigms, such as object oriented, imperative and functional programming styles.


### [Colyseus_A_Distributed_Architecture_for_Online_Multiplayer_Games!](https://www.researchgate.net/publication/220831981_Colyseus_A_Distributed_Architecture_for_Online_Multiplayer_Games)

- Colyseus, which primarily acts as a game object manager

- There are two types of game objects
    - Immutable
    - Mutable
    
We assume that immutable objects (e.g., map geometry, game code, and graphics) are globally replicated (i.e., every
node in the system has a copy) since they are updated very infrequently, if at all.
    - Each node has a local object store which is a collection of primaries and replicas, a replica manager that synchronizes primary and secondary replicas, and a object placer which decides where to place and migrate primary replicas

- Networked games are rapidly evolving from small 4-8 person,  onetime play games to large-scale  games  involving thousands  of  participants and  persistent  game  worlds. However, like most Internet applications, current networkedgames are centralized.  Players send control messages to acentral server and the server sends (relevant) state updates to all active players. This design suffers from the well known robustness and scalability problems of single server designs. 

- Fortunately, there  are  two  fundamental  properties  of games  that  we  can  take  advantage  of  in  addressing  these challenges. First,  games  tolerate  weak  consistency  in the application state.

- Second,  gameplay  is  usually  governed  by  a  strictset  of  rules  that  make  the  reads/writes  of  the  shared  statehighly predictable. 

- The three  game  parameters  that most impact network performance are:  the number of objects in play (NumObjs), the average size of those objects(ObjSize),  and  the  game’s  frame-rate  (UpdateFreq).

- Two common optimizations used by games are area-of-interest filtering and delta-encoding. 

- Influential factors impact on the cloud game latency can be divided into three parts

    - Network  delay  (ND):  Total  times  required  for  delivering  the  command  of  the  player  to  the server and send back to the computer monitor of the client from the server.  

    - Playout delay (OD): Different duration of the client receives the encoded form of a frame and the frame is decoded and presented on the screen. 

    - Processing delay (PD): Different duration of the server receives players’ command (from the thin client) and it responds with a corresponding frame after processing the command.   

- Experimental Setup
    - We emulate the network environment by running several virtual servers on 5-50 physical machines on Emulab. The environment does not constrain link capacity, but emulates end-to-end latencies (by delaying packets) using measured pairwise Internet latencies sampled from the MIT King dataset

 - Object locating
    - To locate objects, Colyseus implements a distributed location service on a DHT. Unlike other publish-subscribe services built on DHTs [6], the object locator in Colyseus must be able to locate objects using range queries rather than exact matches. 

- Uses mercury as DHT

- Colyseus enables low-latency game-play
via three important design choices: 
(1) decoupling object discovery and replica synchronization,
(2) proactive replication for short-lived objects 
(3) pre-fetching of relevant objects using interest prediction.

-  Colyseus enables three new avenues for cheating: 
(1) nodes can modify objects in their local store in
violation of game-play logic 
(2) nodes can withhold publications or updates of objects they own
(3) nodes can subscribe to regions of the world that they should
not “see.”     


- [Distributed Architectures for Massively-Multiplayer Online Games!](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.106.8352&rep=rep1&type=pdf)

-  The primary contribution of this paper is architectural. We take advantage of the locality of interest data exhibits in
an MMORPG to separate the large world into
smaller individual regions and assign each region
to a different physical machine.

- Most important technical contribution
is a design that handles game scenarios occurring in an area near the virtual border separating two or more servers.

- Mirrored Game Architecture

- Peer to peer
    - Clients multicast updates to other peers. However, lack of an established IP Multicast solution, forces such architectures to consume a lot of bandwidth

- Using a publish/subscribe system [FWW02,CKSW02] allows players to subscribe only for events that interest them.

- In overlapping multiple server parts
    - As multiple servers handle different areas of the
same virtual world, there are instances when a
server would be required to communicate with
another server. In our architecture this is not
very different from client-server communication.
Servers subscribe to their neighboring servers much
like players, with an area of interest of all points
close enough to the border between the two servers.
- Log replicated server


- [A Distributed Architecture for Multiplayer Interactive Applications on the Internet!](https://www.cs.ubc.ca/~krasic/cpsc538a/papers/diot99distributed.pdf)

- IP multicast protocol suite (RTP/UDP)
- Group communication is currently
one of the most active research domains in the Internet community.
- Bucket synchronization. The synchronization mechanism is the
minimum functionality required for a distributed game. Without a synchronization mechanism,
the real-time requirements of an interactive game cannot be satisfied.
- MiMaze  is the only game with a fully distributed architecture using IP multicast
- Choosing a distributed architecture improves the real-time properties of the
application, at the cost of consistency


### [Distributed Architectures for Massively-Multiplayer Online Games!](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.106.8352&rep=rep1&type=pdf) ****

- A massively multiplayer online game is a networked game with two distinguishing features. First, the magnitude of the number of concurrent players is typically on the order of 104 or more. Second, MMGs have persistent state. This means that an MMG, unlike other networked games which end after some goal is completed, can continue indefinitely. Players join the game and play until they are ready to quit, at which point the state of their alter-ego in the game is saved. When they return, the state is restored. This
also holds true for the virtual world.
- Distributed systems are divided into two models: synchronous and asynchronous. In the synchronous model, processes execution occurs in synchronous rounds (i.e., they proceed in lockstep)[Lyn96] according to a global
clock. The advantage of the synchronous model is that it is easier to reason
about, with the caveat that most real distributed systems are not completely
synchronous. In the asynchronous model, processes execute local instructions at arbitrary speeds. This model has the advantage that algorithms
designed for it can run on all types of networks without timing guarantees.
The disadvantage of the asynchronous model is that some problems are more
difficult, if not impossible, in the asynchronous system [Lyn96].
- Three fundamental problem
    - Ordering of events
    - Syncronization of processes
        - Synchronization is the correct sequencing of processes to ensure mutually exclusive access to shared writable structures.
        - A number of distributed mutual exclusion algorithms are presented in
[CDK01]. A simple ring-based algorithm logically arranges nodes in a ring
and passes a token that allows a member of the system access to the shared
writable structure. Other possibilities are multicast with logical clocks or
distributed voting
    - Consistency of data
-  Synchronization Techniques
    -  The Bucket Synchronization Mechanism
    -  Dead Reckoning
    -  Local Lag and Timewarp
    - Trailing State Synchronization

- The Trailing State Synchronization is a novel method for synchronization of game state, introduced in this paper. The game chosen for the proof of concept by the authors is Quake. With a fast paced First Person Shooter game like Quake, the rate of commands issued by the user with reference to time is very high. This prevents synchronization mechanisms such as Timewarp which maintains multiple copies of the game state for each executed command. This problem is addressed by maintaining more than one executing parallel game states with the leading execution having no latency and the rest of the executing states each running with a delay of a few milliseconds from its preceding states. The parallel execution synchronization is similar to the Bucket Synchronization with different delays. To detect inconsistencies, each synchronizer looks at the changes in game state that an execution of a command produced and compares it with the immediate preceding state. If inconsistency is discovered, a roll back from the trailing state to the leading state is performed. This method allows for a high degree of consistency, while allowing low latency and scalability.

- The third element of the Mirrored-Server system is the CRIMP protocol. The requirement for a low latency performance has prompted the authors to introduce a receiver-based reliable multicast layer which conforms to the requirements of the architecture. Several other enhancements to increase the performance of the multicast layer is also introduced. In the receiver based protocol, the receivers detect losses and send a recovery request, which is responded to by any host that has the packet. By tweaking certain variables (such as the probability of generating a response or request etc) the protocol is optimized, allowing an efficient communication mechanism with minimal overhead. The layer also has provisions for boot strapping to allow new mirrors to join, loss detection, cancellation of recovery and server management capability.


- [P2P matchmaking solution for online games!](https://link.springer.com/article/10.1007/s12083-019-00725-3)

- ADU: Application Data Unit. An ADU is a chunk of data manipulated by the application. For
transmission efficiency purposes, it is recommended not to fragment ADUs within the communication stack.
- Avatar: Any dynamic object in a game that is controlled either by a participant or automatically
by the system.
- Dead Reckoning: An extrapolation technique used in the aviation systems to compute an estimate of the current position of a plane based on the knowledge of its position in the past and on
its trajectory.
- DIA: Distributed Interactive Application are real-time applications where users (i.e. participants) interact in a defined environment. Examples of DIAs are distributed games, digital battlefield, shared virtual worlds, cooperative tools, etc.
- DIS: Distributed Interactive Simulation. DIS is an IEEE standard (see references [1][2]) which
describes the format of the packets that should be exchanged between simulation entities in a
distributed simulation, and that defines the protocol to handle these packets.
- IP multicast: An extension of IP to support the construction of trees (instead of point-to-point
routes) for the delivery of data to a group of receivers.
- Mbone: Virtual overlay installed on the Internet to implement IP multicast.
- RTP/RTCP: Real-Time transport Protocol / Real-Time Control Protocol [9]. RTP is an encapsulation format designed to handle realtime data transmission on the Internet. RTP is generally
used in conjunction with UDP. RTCP is a control protocol that carries statistic and control
information for RTP data flows.
- NTP: Network Time Protocol [6]. NTP is a protocol used to synchronize a clock signal over a
network (in other words, to provide a global clock in a network). NTP is a client/server protocols where servers are organized in stratum. NTP is sensitive to link asymmetry.
- PDU: Protocol Data Unit. PDU is the standard way to describe a packet constructed by a protocol for transmission purposes. In the DIS, the most popular PDU is the Entity State PDU that
carries a description of an avatar.
- UDP: User Datagram Protocol. UDP is an unreliable transport protocol (as opposed to TCP
that guarantees ordered and reliable data transmission). UDP’s main functionality is to multiplex/demultiplex data. UDP has been designed to implement real-time applications on the
Internet.

- [A Comparison of Architectures in Massive Multiplayer Online Games!](https://www.researchgate.net/publication/271490933_A_Comparison_of_Architectures_in_Massive_Multiplayer_Online_Games)

Three  main  architectures  are  typically  used  in Massive  Multiplayer  Online  Games: 
-  client-server architecture
-  multi-server architecture  
-  Peer-to-Peer(P2P) architecture 

- [Peer-to-Peer Architectures for Massively Multiplayer Online Games:A Survey!](https://dl.acm.org/doi/pdf/10.1145/2522968.2522977?download=true)

- Entity Component System
    - OOP not suitable for game development
    - Think about data structures rather than functions that operate on it
    - Self mutating struct or internal mutability usage for entity object
    - Object indexing
    - Put objects in vector and use index. But on delete of object `use after free` occurs
    - Generational Indexing
        - Using index with a generation field
        - Need type registry to know only about the relevant in global system in anymap.
    - In ECS System an entity is collection of traits
    - Registry Pattern
    - Resource Pattern

## References
- [Source Multiplayer Networking](https://developer.valvesoftware.com/wiki/Source_Multiplayer_Networking)
- [High-Level Development of Multiserver Online Games](https://www.hindawi.com/journals/ijcgt/2008/327387)
- [ECS System Design](https://www.youtube.com/watch?v=aKLntZcp27M)