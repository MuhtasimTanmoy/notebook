- DVR Distant Vector Routing
- LSR Link State Routing

Broadcasting 
Multicasting

-  Each packet to each node
-  Flooding
-  Forwarding to next node 
    - Calculating optimal paths for requested nodes
    - Erase the one that meets criteria
    - Forward
- Spannig tree avilable for `lsr` where we have information for all nodes
- Reverse path forwarding `dvr`


- FReeBSD has kQueue
- Linux has no epoll