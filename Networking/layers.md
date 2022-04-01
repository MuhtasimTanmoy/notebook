# Network Layers

- [OSI Layer 1](https://www.practicalnetworking.net/series/packet-traveling/osi-model#osi-layer-1): is the physical medium carrying the 1’s and 0’s across the wire

- [OSI Layer 2 - Data Link Layer](https://www.practicalnetworking.net/series/packet-traveling/osi-model#osi-layer-2): is responsible for hop to hop delivery and uses `MAC addresses`
    - [Switches](https://www.practicalnetworking.net/series/packet-traveling/key-players/#switch) facilitate communications within networks and operate at `Layer 2`
    - Switches use a [MAC Address Table](https://www.practicalnetworking.net/series/packet-traveling/key-players/#mac-table) which is a mapping of Switchports to connected MAC addresses
    - Layer 2 would add an Ethernet header which would include a Source and Destination

- [OSI Layer 3 - Network Layer](https://www.practicalnetworking.net/series/packet-traveling/osi-model#osi-layer-3): is responsible for end to end delivery and uses `IP Addresses`
    - [Routers](https://www.practicalnetworking.net/series/packet-traveling/key-players/#router)facilitate communication between networks and operate at `Layer 3`
    - Routers use a [Routing Table](https://www.practicalnetworking.net/series/packet-traveling/key-players/#routing-table) which is a mapping of known Networks to interfaces or next-hop addresses
    - Layer 3 will add an IP header which would include a Source and Destination IP address


-  [OSI Layer 4 - Transport Layer](https://www.practicalnetworking.net/series/packet-traveling/osi-model#osi-layer-4) is responsible for _service to service_  delivery and uses Port Numbers
    - [ARP](https://www.practicalnetworking.net/series/packet-traveling/key-players/#arp) uses a known  IP address to resolve an unknown  MAC address
    - All L3 devices use an [ARP Table](https://www.practicalnetworking.net/series/packet-traveling/key-players/#arp-table) which is a mapping of IP Addresses to MAC addresses
    - Layer 4 accomplishes this by using an addressing scheme known as Port Numbers
    -  Layer 4 will add a TCP header which would include a Source and Destination port


- Flow of bytes
    - Data 
    - -> Data + port (Transport) Segment  
    - -> Data + Port + IP (Packet) Network  
    - -> Packet + Mac (Frame)


- Router
	- Routers operate at Layer 3 of the OSI Model
	- Route Table is a map of `_every_ network` that exists
	- When a router receives a packet destined to a network which is not in its `Routing Table`, that packet is discarded

 - MAC addresses are a Layer 2 addressing scheme
 - IP addresses are a Layer 3 addressing scheme
 - What bridges these two addressing schemes is the `Address Resolution Protocol (ARP)`
    - ARP will use the  `_known_  IP` address, and discover the  `_unknown_  MAC address`
    - The discovered mapping is then added and stored in an `ARP Table`, which is a mapping of IP addresses to correlating MAC addresses
    - ARP’s role is to help the client create the proper `L2 header`, based on the `L3 header`, in order to get the packet from one hop to the next