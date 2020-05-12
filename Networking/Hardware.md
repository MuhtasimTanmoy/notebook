# Hub

- A hub is a network equipment with several interfaces called ports (not the one from OS). If we connect computers to these ports they will be able to talk with each other.

- People confuse hubs and switches. Know that hubs are antique legacy devices that no longer belong in any computer network. Switch on the other hand is a modern day device.

- Problems with Hub
    - They are unintegillent
All a hub ever does is to copy electrical signals that are entering one port to all other ports.

    - This means that a hub is unintegillent. It doesn't care about network traffic or addresses at all.

    - They do unnecessary work
This results in lot of unnecessary work by the network. Apart from the actual receiver, all other computers must discard the packet.
    - They are Half Duplex
Another downside of hubs is that only one computer can talk at a time through a hub. When one computer is talking every other computer must stay completely silent. This is because the electrical signals of multiple computers that talk simultaneously will mix together in the hub, creating disturbances to the signals so that neither signal can be interpreted.

    - If two computers talk at the same time a collision occurs. When this happens all computers will notice the disturbances and must stop talking for a while before trying again. This also makes a hub really slow. Only one device can communicate at a time, and when a collision accidentally occurs every device must be silent for a while.
    - The more computers you connect to a hub the bigger the risk gets for collisions to happen since more involved devices will indirectly compete with each other for the available communication time slots.



# Router
The main role of a Router is to route data traffic. The router knows in which directions different destinations are, and when it receives data traffic it will forward the traffic in the direction of the destination. A router always picks the best route it has knowledge about for the data traffic that it is forwarding.

In a home network, the router plays a vital role. It connects its two end points: outside and inside.

A home router has the following parts:

- Switch
- Access point
- Modem
- Router
- DHCP
- Address translation
- Port Forward
- Firewall
- DNS
- Web interface

From the picture we can see, internal computers can communicate through switch alone. No need to go through router. Same for wifi communication: access point to switch.

# Switch
When two computers on same ip network communicate with each other directly, the communication is dealt by the switch.

The task performed by switch is called Switching. Routers forward traffic based on IP address, switches forward traffic based on MAC address.

A switch is an intelligent device.

What a switch does is that it constantly monitors the traffic which is entering the switch from connected devices. It then learns about where the different MAC addresses of those devices are connected. It does this by looking at the traffic that arrives from computers to read the source MAC address of the traffic.

If it doesn't know where a particular device is, it acts like sends them to all unknown devices and waits for reply for them.

Switch is like a HUB + Cache.


# ARP
It sends a broadcast request known as ARP asking "Who has the default gateway IP? Send me your MAC address." Then once computer gets the address, it stores it in a cache for few minutes (refreshing after every successful packet transfer). The cache allows the computer to send packets without broadcasting for MAC address every time.


# Mac Address
All equipments that can be connected to computer networks (computers, routers, servers, printers and etc) have a MAC address. It is an address which is written into the network interface of the device during manufacturing.

A MAC address consists of 12 hexadecimal characters and could look like this:

- 01:23:45:67:89:ab
- 00:fe:19:2a:73:dc
- 02:0a:95:9d:68:16

Each time a computer sends out network traffic the traffic has both a source and destination IP address, but it also has a source and destination MAC address.

IP addresses are relevant on a global scale. They hold the final destination of the packet and can tell us which address the packet is originally coming from. In contrast, MAC addresses are used on a more local scale, and hold information about the next hop destination in the local LAN network.


# Broadcast

The computer sends out a broadcast which will reach every other device on the LAN to ask any available DHCP servers to reply back with an IP address.

When a computer sends out a broadcast it will use a special destination MAC address, FF:FF:FF:FF:FF:FF. That address is called the Broadcast Address and is used specifically for this purpose. All other equipment on the LAN will then understand that the traffic is a broadcast that is directed at everybody else within the LAN.