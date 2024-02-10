## IP Address

IP Address consists of two parts: IP Network and Host address.

There are two categories
- Class based
- Class less

It is important to point out that IP address classes are more or less redundant now. These days subnet masks (explained later) are used to define which part of an IP address is the network ID and which is the host ID.

IP Network
On a LAN, computers can talk with each other as long as they are under the same ip network. If the computers belong to different IP networks then they have to communicate with each other via a router.

Port numbers have a range of 0..65535 (although often 0 has special meaning). In the original BSD TCP implementation, only root can bind to ports 1..1023, and dynamically assigned ports were assigned from the range 1024..5000; the others were available for unprivileged static assignment. These days 1024..5000 is often not enough dynamic ports, and IANA has now officially designated the range 49152..65535 for dynamic port assignment. However even that is not enough dynamic ports for some busy servers, so the range is usually configurable (by an administrator). On modern Linux and Solaris systems (often used as servers), the default dynamic range now starts at 32768. Mac OS X and Windows Vista default to 49152..65535.

## Router

The main purpose of a router is to be able to forward traffic to different destinations. Within computer networking, those destinations are different IP networks.

A router in its basic form is simply a network device with 2 network interfaces (NICs), each being on separate network ids. So, you may have 2 networks; 192.168.1.x and 192.168.2.x. On one NIC  the router would have the IP address 192.168.1.1 and on the other it would have an IP address of 192.168.2.1. Computers on the 192.168.1.x network can now communicate with computers on the 192.168.2.x network via the router.

In summary all devices have a routing table, without it they wouldn’t know where to send packets to. When a PC sends packets to another PC it looks at it’s routing table to determine the best route possible. If it finds the destination address is “on-link” it knows it is part of the same subnet as the destination and sends the packets directly to the PC. If not it forwards the packet onto whatever is in the gateway field of the matching route entry. This same process is repeated at every router/hop along the way until it eventually arrives at a router that is part of the destination network. The router then sends the packets directly to the destination PC.

## Subnet Mask

An IP address is always combined with a Subnet Mask, and it is the Subnet Mask that determines which part of the IP address that belongs to the IP network and which part that belongs to host addresses.

IP = Network + Host Address
 
## Default gateway

 In the local network, there must be a router for inter-network communication and the address of that router is configured to all clients of the LAN network. The address of the router is called Default Gateway. We could have just called it "Router Address".

## Private IP

- 10.0.0.0 - 10.255.255.255
- 172.16.0.0 - 172.31.255.255
- 192.168.0.0 - 192.168.255.255

These are private addresses.

The above special addresses are called Private addresses. They cannot be used on the Internet, they can only be used within local networks. If you try to use Private addresses on the Internet then your Internet Service Provider will block your traffic automatically, sensing that the traffic is coming from a Private IP address. This automatic block is being done to avoid any IP address conflicts on the Internet. These addresses are used in so many places that without the block we would have guaranteed and constant IP address conflicts all over the Internet.


## NAT
Since public IP addresses are limited and thus we are forced to use private IP addresses at home, how do we connect to internet?

## How NAT Works?

When a computer wants to communicate it sends off a packet with data. The packet always has two IP addresses inscribed in the envelope or header of the packet.

Source Address, which is the IP address of the sender. This has to be entered into the packet so the receiver knows where it should send its replies, like a “return address” Destination address, the IP address of the receiver that the packet is being sent to In a home network where a computer wants to talk to something on the Internet, the source address will be a Private IP address on the LAN. The destination address of the packet will be a Public IP address of a server on the Internet. If that packet is sent to the Internet then the ISP will block and throw away the packet since it has a private IP address as its source.

To fix this problem the home router steps in and translates the source address from a private address to a public IP address. The router itself has a public IP address on its outside WAN interface. It got that public IP address from the ISP. The router will simply let every client on the inside LAN share that single public IP address.


When the router sends the packet on to the Internet the packet will appear to come from the home router’s public IP address. From the perspective of the ISPs and the web server, the packet is coming from the public IP address of the home router. When the web server replies back to the computer it will send its reply back to the public IP address of the home router, and the ISP finds its way back there without any trouble.

What about when there are multiple clients? Well, the router keeps track about which packet belongs to which client. You don't have to worry.


NAT works in network layer
PAT works in transport layer

Also, it does the translation of port numbers i.e. masks the port number of the host with another port number, in the packet that will be routed to the destination.

Suppose, in a network, two hosts A and B are connected. Now, both of them request for the same destination, on the same port number, say 1000, on the host side, at the same time. If NAT does an only translation of IP addresses, then when their packets will arrive at the NAT, both of their IP addresses would be masked by the public IP address of the network and sent to the destination. Destination will send replies on the public IP address of the router. Thus, on receiving a reply, it will be unclear to NAT as to which reply belongs to which host (because source port numbers for both A and B are same). Hence, to avoid such a problem, NAT masks the source port number as well and makes an entry in the NAT table.

NAT Hole Punching
1.  Peers Behind  **Common NAT**
2.  Peers Behind  **Different NATs**
3.  Peers Behind  **Multiple levels of NATs**

**Steps:**

1.  A send S a requests connection to B.
2.  S sends A’s address to B and B’s address to A.
3.  A sends garbage message to B and B sends garbage message to A. (Both Get discarded by their respective NATs)
4.  Step 3 is repeated.
5.  Connection Established.


## Port Forward
There is no way for the router to know. We have to configure the router such that when traffic from outside hits a particular port of the router, the router will send it to a host that we configured. This is called port forwarding.


- Resources
    - [TCP Socket Programming](https://stackoverflow.com/questions/913501/how-to-let-kernel-choose-a-port-number-in-the-range-1024-5000-in-tcp-socket-pr)