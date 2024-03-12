# WebRTC

### ICE
- ICE needs to gather candidates, prioritize them, choose default ones, exchange them with the remote party, pair them and order into check lists.

### STUN
- STUN allows a client to obtain a transport address (an IP address and port) which may be useful for receiving packets from a peer. 
- However, addresses obtained by `STUN` may not be usable by all peers.

### TURN
- Commmunication through server

### NAT 
- All types of NAT fall into two categories; 
    - Static NAT
        - Static NAT is where administrators manually create and maintain the NAT mappings and is usually associated with inbound types of NAT. 
    - Dynamic NAT
        - Dynamic NAT is where the router creates and maintains mappings automatically on demand and is usually associated with outbound types of NAT.

- Every TCP/IP packet contains a source IP address, source port, destination IP address and destination port. 
- All types of NAT create NAT mappings using these values.

- Full Cone NAT (Static NAT)
    - A full cone NAT (also known as a one to one NAT) is the only type of NAT where the port is permanently open and allows inbound connections from any external host. - A full cone NAT maps a public IP address and port to a LAN IP and port. 
    - Any external host can send data to the LAN IP through the mapped NAT IP and port. 
    - If it tries to send data through a different port it will fail. 
    - This type of NAT is also known as port forwarding. 
    - This is the least restrictive type of NAT; the only requirement is that the connection comes in on a specific port (the one you opened).

    - My PC has a website running on port 80. 
    - I create a one-to-one rule that maps the router WAN IP of `81.45.87.98` to `192.168.0.1` with port 80 to port 80. 
    - Any external host that sends data to `81.45.87.98` on port 80 is NATed (and sent) to `192.168.0.1` port 80. 

    - Note: the port numbers do not have to be the same; I could run my website on port 56456 but create the NAT mapping to forward port 80 to port 56456. 
    - This gives the appearance to the public Internet that my website is on port 80. 
    - A connection attempt on any other port is dropped.

-  Restricted Cone NAT (Dynamic NAT)
    - A restricted cone NAT works in the same way as a full cone NAT but applies additional restrictions based on an IP address. 
    - The internal client must first have sent packets to IP address (X) before it can receive packets from X. 
    - In terms of restrictions the only requirement is that packets come in on the mapped port and from an IP address that the internal client has sent packets to.

    - My PC makes an outbound connection to a website (56.45.34.78) with my source IP 192.168.0.1 and source port 56723. 
    - The NAT creates a (dynamic) mapping to my PC using source port 56723. 
    - Packets that arrive with a source IP of 56.45.34.78 (the website IP) using a destination port of 56723 (which was the outbound NATed source port) will be accepted and sent to my PC.
    - Connection attempts from any other IP using the correct port of 56723 will be dropped. 
    - Connection attempts from the correct IP with a destination port other than 56723 will also be dropped.

- Port restricted cone NAT
    -  It acts in exactly the same way as a restricted cone NAT but applies restrictions to ports also. 
    - Where a restricted cone NAT will accept connections from any source port a port restricted cone NAT restricts this further by only accepting connections from the IP address and port it sent the outbound request to.

    - Example – My PC makes an outbound connection to website IP `217.87.69.8` on port 80 (destination port). - The NAT maps my source IP `192.168.0.1` to the WAN IP of `81.45.87.98` and source port 56723. 
    - When the website sends packets back it must have it’s source IP as `217.87.69.8`, destination port as 56723 (like a restricted cone NAT) but in addition the source port must be 80. 
    - If any of these three are different a port restricted cone NAT drops the connection. 

- Symmetric NAT (a type of NAT known to be non-STUN compatible)
    - A symmetric NAT applies restrictions exactly the same way as a port restricted cone NAT but handles the NAT translation differently. 
    - All types of NAT discussed so far don’t change the source port when NATing connections. 
    - For example when a client accesses the Internet using IP `192.168.0.1` and source port 56723 NAT changes the source IP to say `56.35.67.35` but keeps the port number the same; this is known as port preservation. 
    - A symmetric NAT NATs ports to new randomly generated ones. 
    - This even applies to connections from the same client to different destinations.

    - Example – Expanding on the example from the port restricted cone NAT my PC makes two outbound connections to website `IP 217.87.69.8` and `56.76.87.98`. 
    - My PC uses source IP192.168.0.1 with source port 56723 for both connections. 
    - On all types of NAT so far both these connections would be NATed to change the source IP address only and keep the source port the same. 
    - This time however instead of leaving the source port as 56723 a symmetric NAT changes it to 45765 for one connection and 53132 for the other connection (random). - This has created unique mappings for each connection and traffic from those destinations must come in on the respective ports. 
    - So `217.87.69.8` must send packets to destination port 45765 and `56.76.87.98` must send packets to port 53132 in addition to the requirements of a port restricted cone NAT.


### Why symmetric NAT is not STUN compatible?

- Here in case of first it works. In second it does not.

- My console with IP address 192.168.0.1 hosts a game using port 57433. It connects to xbox live to advertise this information.

- Xbox live (using STUN) detects my public IP address of 56.45.32.5 and public port of 57433 and informs my console of this.

- My console updates this information and advertises these details on xbox live.
Another person browses xbox live for my game. 

- Once he clicks “join” his console retrieves my public IP address and port and attempts to connect directly. 

- It tries to connect on 56.45.32.5 with port 57433. The initial connection will be blocked by a port restricted NAT because I haven’t yet sent any data to that console. 

- My console now sends data to the remote console (IP and port learnt through xbox live) using source port 57433 with source IP 5.45.32.5.

- All subsequent packets sent from the remote console to 56.45.32.5 using port 57433 will now be accepted by my port restricted NAT as I have now sent packets to it and he connects to me successfully.

- My console with IP address 192.168.0.1 hosts a game using port 57433. It connects to xbox live to advertise this information.

- Xbox live (using STUN) detects my public IP address of 56.45.32.5 and public port of 57433 and informs my console of this.

- My console updates this information and advertises these details on xbox live.
Another person browses xbox live for my game. 

- Once he clicks “join” his console retrieves my public IP address and port and attempts to connect directly. 

- It tries to connect on 56.45.32.5 with port 57433. Like a port restricted NAT the initial connection will be blocked because I haven’t yet sent any data to that console. 

- My console now sends data to the remote console (IP and port learnt through xbox live) but a new mapping is used using port 45654 with source IP 56.45.32.5.

- The information the remote console received from xbox live was that the game is hosted on 57433 but the symmetric NAT opened up the port 45654 for this connection and not 57433. The remote console fails to connect. 
 
- How peer to peer game connects and arcitecture is available here [Game server](../architecture/game%20server.md)


### WebRTC Connection Process

- The process begins when a client computer wants to contact a peer computer for a data transaction, but cannot do so due to both client and peer being behind respective NATs. 
- If STUN is not an option because one of the NATs is a symmetric NAT (a type of NAT known to be non-STUN compatible), TURN must be used.

- First, the client contacts a TURN server with an "Allocate" request. 
- The Allocate request asks the TURN server to allocate some of its resources for the client so that it may contact a peer.
- If allocation is possible, the server allocates an address for the client to use as a relay, and sends the client an `Allocation Successful` response, which contains an `allocated relayed transport address` located at the TURN server.

- Second, the client sends in a CreatePermissions request to the TURN server to create a permissions check system for peer-server communications.
- In other words, when a peer is finally contacted and sends information back to the TURN server to be relayed to client.
- The TURN server uses the permissions to verify that the peer-to-TURN server communication is valid.

- After permissions have been created, the client has two choices for sending the actual data(1) it can use the Send mechanism, or (2) it can reserve a channel using the ChannelBind request. 
- The Send mechanism is more straightforward, but contains a larger header, 36 bytes, that can substantially increase the bandwidth in a TURN relayed conversation. 
- By contrast, the ChannelBind method is lighter: the header is only 4 bytes, but it requires a channel to be reserved which needs to be periodically refreshed, among other considerations.

- Using either method, Send or channel binding, the TURN server receives the data from the client and relays it to the peer using UDP datagrams, which contain as their Source Address the "Allocated Relayed Transport Address".

- The peer receives the data and responds, again using a UDP datagram as the transport protocol, sending the UDP datagram to the relay address at the TURN server.

- The TURN server receives the peer UDP datagram, checks the permissions and if they are valid, forwards it to the client.

- This process gets around even symmetric NATs because both the client and peer can at least talk to the TURN server, which has allocated a relay IP address for communication.

- While TURN is more robust than STUN in that it assist in traversal of more types of NATs, a TURN communication relays the entire communication through the server requiring far more server bandwidth than the `STUN` protocol, which typically only resolves the public facing 
IP address and relays the information to client and peer for them to use in direct communication.

- For this reason, the ICE protocol mandates STUN usage as a first resort, and TURN usage only when dealing with symmetric NATs or other situations where STUN cannot be used.

### SDP
- In order to exchange media, WebRTC uses session description protocol (SDP) to initiate and execute an `offer` and `answer` mechanism between endpoints or peers. - Supported codecs, connectivity, and protocols are added to the SDP so that clients can decide what media codecs `Session Traversal Utilities for NAT` (STUN) allows clients to learn what their public NAT’d IP address and port is. 

- Once this is achieved it’s possible to provide the correct details to other clients that want to connect to your client. 

- Typically, a STUN server is needed. 

- A STUN client can send messages to the STUN server to get the information about public IP and ports, and retrieve that information. 

- This protocol does not work for symmetric NATs, however. Symmetric NATs generate ports are random for bindings. 

- STUN cannot communicate that dynamic mapping when negotiating media paths.

- They can send and receive, and where to send them.

 - Clients then generate a connection offer, and start to generate multiple candidates to be used to stream media to another client.

 - After a handful of ICE candidates are generated, they must be properly formatted and encoded to be sent to the end client.

 - This encoding can be placed in the offer and answer SDP or be sent standalone (trickle ICE).

 - The candidates can be packed in the original offer, or can be sent independently after the offer is sent. The latter is known as trickle ICE

### Keywords

- Signalling is not standard 
    - SIP, Jingle
- RTP Media Session 
    - Described by SDP
- RTCWeb Media Extensions 
    - ICE NAT Traversal
    - Secure RTP
- `ICE Hole Punching` can establish direct `p2p` session between browsers behind different NAT
- If both browsers behind same `NAT hole punching` stablish connection that never leaves
- In some cases hole punching fails, `TURN Relay` can work
- Some website serves static assets from other peer


# References
- https://think-like-a-computer.com/2011/09/19/symmetric-nat/
- https://think-like-a-computer.com/2011/07/18/how-routing-works/
- https://think-like-a-computer.com/2011/08/24/ip-routing/
- https://en.wikipedia.org/wiki/UDP_hole_punching
- https://www.viagenie.ca/publications/2008-08-cluecon-stun-turn-ice.pdf
- https://temasys.io/webrtc-ice-sorcery/
- https://webrtchacks.com/trickle-ice/
- https://testrtc.com/docs/
- https://www.kurento.org/blog/rtp-i-intro-rtp-and-sdp
- https://www.kurento.org/blog/rtp-ii-streaming-ffmpeg
- [WebRTC Secutirty](https://ftp.ripe.net/rfc/v3test/testing_dl_v25.pdf)
