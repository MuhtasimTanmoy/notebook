# Networking

Distance-vector routing protocols use the [Bellman–Ford algorithm](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm "Bellman–Ford algorithm") and [Ford–Fulkerson algorithm](https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm "Ford–Fulkerson algorithm") to calculate the best route.

-  Each packet to each node
-  Flooding
-  Forwarding to next node 
    - Calculating optimal paths for requested nodes
    - Erase the one that meets criteria
    - Forward

- Spanning tree avilable for `lsr` where we have information for all nodes
- Reverse path forwarding `dvr`

### Routing Algo
- DVR Distant Vector Routing
	- Count to infinity
	- Split horizon
	- Poison reverse
    - Neighbours tell the world
- LSR Link State Routing
    - Dijkstra
    - Tells the world about neighbours 
    - Complete Topology 
    - Global 