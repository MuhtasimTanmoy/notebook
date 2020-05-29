
# Gameserver

## Optimization for gameserver
- Better predictions
- Eliminate the server
- Optimize communication
- Game data is compressed using delta compression to reduce network load. That means the server doesn't send a full world snapshot each time, but rather only changes (a delta snapshot) that happened since the last acknowledged update. With each packet sent between the client and server, acknowledge numbers are attached to keep track of their data flow. Usually full (non-delta) snapshots are only sent when a game starts or a client suffers from heavy packet loss for a couple of seconds. Clients can request a full snapshot manually with the cl_fullupdate command.


# NAT Hole Punching
Required for conncting peer to peer after matchmaking
- https://keithjohnston.wordpress.com/2014/02/17/nat-punch-through-for-multiplayer-games/


# Architecture Study

## [EVE ONLINE!](http://uu.diva-portal.org/smash/get/diva2:408940/FULLTEXT01.pdf)
 - A type of shared-nothing-architecture in distributed computing, where each node is independent and does not communicate with other nodes.
 - Multiple programming paradigms, such as object oriented, imperative and functional programming styles.


## [Colyseus_A_Distributed_Architecture_for_Online_Multiplayer_Games!](https://www.researchgate.net/publication/220831981_Colyseus_A_Distributed_Architecture_for_Online_Multiplayer_Games)

- Colyseus, which primarily acts as a game object manager

- There are two
types of game objects: immutable and mutable. We assume that immutable objects (e.g., map geometry, game
code, and graphics) are globally replicated (i.e., every
node in the system has a copy) since they are updated
very infrequently, if at all.
    - Each node has a local object store which
is a collection of primaries and replicas, a replica manager that synchronizes primary and secondary replicas,
and a object placer which decides where to place and
migrate primary replicas

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

## [Distributed Architectures for Massively-Multiplayer Online Games!](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.106.8352&rep=rep1&type=pdf)

-  The primary contribution of this paper is architectural. We take advantage of the locality of interest data exhibits in
an MMORPG to separate the large world into
smaller individual regions and assign each region
to a different physical machine.

- Most important technical contribution
is a design that handles game scenarios occurring in an area near the virtual border separating two or more servers.

- Mirrored Game Architecture

- Peer to peer
    - Clients multicast updates to other peers. However, lack of an established IP Multicast solution, forces such architectures to consume a lot of bandwidth

- Using a publish/subscribe system [FWW02,
CKSW02] allows players to subscribe only for
events that interest them.

- In overlapping multiple server parts
    - As multiple servers handle different areas of the
same virtual world, there are instances when a
server would be required to communicate with
another server. In our architecture this is not
very different from client-server communication.
Servers subscribe to their neighboring servers much
like players, with an area of interest of all points
close enough to the border between the two servers.
- Log replicated 

## References

- https://developer.valvesoftware.com/wiki/Source_Multiplayer_Networking
- https://gist.github.com/GkhanKINAY/5cd384b5597f04ed9750f5a9caa597f0#tutorials