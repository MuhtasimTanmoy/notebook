# Bit Torrent

- **Architecture Type** : Hybrid
    - Client Server
    - Peer to Peer

- **Torrent file**: Used for storing session.
    - The torrent file is created with the URL of the tracker and the actual file or files to be
part of this torrent. The format of the torrent file is bencoding.
    - The torrent file is a bencoded dictionary containing two keys, announce and info. The announce key is the URL of the tracker. The info key maps to a dictionary described below.
        - name, piece length, pieces, and either length or files key.
        - pieces - Each SHA1 hash is a string of 20 characters long so for example the hash value of piece 4 would be the substring of pieces at character 60 to character 79 assuming that the string begins at index 0. 
    - A peer must be in two state - 
        - Leecher state: When it is still downloading the file while uploading pieces it has to other leechers.
        - Seed state: If it has the complete file and is uploading to leechers.

- **Tracker** : The centralized server is called the tracker. The tracker’s responsibility is to help peers find other peers. A tracker consists of many torrent sessions with each session it keeps
track of all of the peers participating in the particular torrent.   

- **Bencoding** : 
    - https://en.wikipedia.org/wiki/Bencode
    - Encode: https://chocobo1.github.io/bencode_online
    - Decode: https://www.tools4noobs.com/

-  There needs to be at least one seeder in
order for the torrent to be alive otherwise the leechers will not be able to finish.

-  A file is split into equal size pieces, which are further divided into smaller blocks.
Blocks are the transmission unit of the network, but the protocol keeps track of what pieces have been downloaded. 

- A peer can only upload to a subset of this peer set called the active peer set. Peers
also need to know what pieces of the content each peer in its peer set has. By knowing what
peers a peer can upload to and by knowing what pieces all of its connected peers have, BitTorrent
can use this information in order to deliver content efficiently.

- The peers distribute the file to each other by using the swarming technique.

## The Tracker Protocol 

## Algorithm
- Choke Algorithm - For uploading
- Rarest first piece selection algorithm - For downloading

## References
- [Bittorrent Paper](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.114.4974&rep=rep1&type=pdf#:~:text=BitTorrent%20is%20an%20application%20layer,they%20are%20uploading%20to%20others.)
- [Protocol Video](https://www.youtube.com/watch?v=8sTttjDmNbk)