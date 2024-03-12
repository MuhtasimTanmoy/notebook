# Decentralized Storage

- Ethereum: Computation
- Swarm: Storage
- Whisper: Messaging

### Implementations
- Swarm
- Sia
- Storj
- FileCoin
- IPFS
- Arweave - Archive of data

### [Libri](https://github.com/drausin/libri)

- The Libri API exposes simple `Put / Get` endpoints and a streaming Subscribe endpoint for storage notifications across the entire network.

- InterPlanetary File System (“IPFS”) [ipfs] uses much of the same design as BitTorrent—peer-to-peer file sharing, possible caching of popular documents, tit-for-tat incentive accounting—but it addresses the stored data by a hash of its content instead of a filename.

- This content-addressing combined with a simple link structure allows it to behave as a Merkle DAG, giving it great flexibility in being able to store and model many forms of data, from simple blobs to files to whole filesystems. 

- At its heart, though, IPFS looks very much like BitTorrent: peers host data that others may optionally copy and host as well, and the addresses of the peers hosting each object are stored in a Kademlia DHT.

- Peers in the Libri network are called Librarians, and clients of these peers are called Authors. Librarian peers never see the plaintext content of a document and deal only with encrypted chunks of one. 

- Author clients convert a plaintext document into these encrypted chunks and back again.


### [Sia](https://gitlab.com/NebulousLabs/Sia)

- The Sia software divides files into 30 segments before uploading, each targeted for distribution to hosts across the world.

- File segments are created using a technology called Reed-Solomon erasure coding, commonly used in CDs and DVDs. Erasure coding allows Sia to divide files in a redundant manner, where any 10 of 30 segments can fully recover a user's files.

- This means that if 20 out of 30 hosts go offline, a Sia user is still able to download her files.

- Threefish encryption algorithm.

- Merkle construction phase requires heavy preprocessing. Logarithmic of the file size.

# References
- [Reed Solomon](https://en.wikipedia.org/wiki/Reed%E2%80%93Solomon_error_correction)
- [Swarm Arweave Sia Talk ](https://www.youtube.com/watch?v=vVsHBAohsaE)