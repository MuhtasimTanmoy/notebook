## Ip address
IP Address consists of two parts: IP Network and Host address.



IP Network
On a LAN, computers can talk with each other as long as they are under the same ip network. If the computers belong to different IP networks then they have to communicate with each other via a router.

The main purpose of a router is to be able to forward traffic to different destinations. Within computer networking, those destinations are different IP networks.


## Subnet Mask
An IP address is always combined with a Subnet Mask, and it is the Subnet Mask that determines which part of the IP address that belongs to the IP network and which part that belongs to host addresses.

IP = Network + Host Address
 
 # Default gateway
 In the local network, there must be a router for inter-network communication and the address of that router is configured to all clients of the LAN network. The address of the router is called Default Gateway. We could have just called it "Router Address".

# Private IP

- 10.0.0.0 - 10.255.255.255
- 172.16.0.0 - 172.31.255.255
- 192.168.0.0 - 192.168.255.255

These are private addresses.

The above special addresses are called Private addresses. They cannot be used on the Internet, they can only be used within local networks. If you try to use Private addresses on the Internet then your Internet Service Provider will block your traffic automatically, sensing that the traffic is coming from a Private IP address. This automatic block is being done to avoid any IP address conflicts on the Internet. These addresses are used in so many places that without the block we would have guaranteed and constant IP address conflicts all over the Internet.


# NAT
Since public IP addresses are limited and thus we are forced to use private IP addresses at home, how do we connect to internet?

## How NAT Works?
When a computer wants to communicate it sends off a packet with data. The packet always has two IP addresses inscribed in the envelope or header of the packet.

Source Address, which is the IP address of the sender. This has to be entered into the packet so the receiver knows where it should send its replies, like a “return address” Destination address, the IP address of the receiver that the packet is being sent to In a home network where a computer wants to talk to something on the Internet, the source address will be a Private IP address on the LAN. The destination address of the packet will be a Public IP address of a server on the Internet. If that packet is sent to the Internet then the ISP will block and throw away the packet since it has a private IP address as its source.

To fix this problem the home router steps in and translates the source address from a private address to a public IP address. The router itself has a public IP address on its outside WAN interface. It got that public IP address from the ISP. The router will simply let every client on the inside LAN share that single public IP address.


When the router sends the packet on to the Internet the packet will appear to come from the home router’s public IP address. From the perspective of the ISPs and the web server, the packet is coming from the public IP address of the home router. When the web server replies back to the computer it will send its reply back to the public IP address of the home router, and the ISP finds its way back there without any trouble.

What about when there are multiple clients? Well, the router keeps track about which packet belongs to which client. You don't have to worry.


# Port forward
There is no way for the router to know. We have to configure the router such that when traffic from outside hits a particular port of the router, the router will send it to a host that we configured. This is called port forwarding.

