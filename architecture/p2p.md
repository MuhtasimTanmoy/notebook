# Peer to Peer

- Each peer assigned GUID
- Virtually round structure
- Two main algo
    - Chord
    - Kademelia

### Kademelia

- Kademlia is not a consensus algorithm, it’s a `DHT` 
- It is way to structure `p2p` networks, and to store and look up data on them, which means it can tolerate a whole lot more failures than raft can
- It is usually used to store data that never changes
- Many implementations don’t necessarily replicate data and by itself it doesn’t have any consistency guarantees
- Kademelia has `xor` matrics
    - b | a
- Each node has routing table
    - It contains more info on nodes closer to it
- When finding just need binary lookup
- Leaving is simple in kademelia
- In case of crash ping

### Chord

- Each Node Operations
    - Join
    - Leave
    - Copy routing table
    - Find closed

- Chord GUID Distance
    - (b-a + 2^n) % 2^n
    - 7 to 8 and 8 to 7 not same
- For kademelia order dont matter
- Each node has a successor and a predecessor
- The successor to a node is the next node in the identifier circle in a clockwise direction. The predecessor is counter clockwise. 
- If there is a node for each possible ID, the successor of node 0 is node 1, and the predecessor of node 0 is node `2^m - 1`; however, normally there are "holes" in the sequence.
- The successor of node 153 may be node 167 (and nodes from 154 to 166 do not exist); in this case, the predecessor of node 167 will be node 153

### References
- [P2P N etwork](https://www.youtube.com/watch?v=kXyVqk3EbwE)
- [Chord](https://en.wikipedia.org/wiki/Chord_(peer-to-peer))
- [XOR Distance](https://www.youtube.com/watch?v=w9UObz8o8lY)
- [Kademlia, Explained](https://youtu.be/1QdKhNpsj8M)