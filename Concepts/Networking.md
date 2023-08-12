
# Protocol stack

|  |  |  |
|--|--|--|
|								| PROTOCOL DATA UNIT | Devices | 
 |  Process/Application Layer          | Data |  App Firewalls , SSL,VPN. Proxy
| Host-to-Host/Transport Layer   | Segments / datagrams |  Traditional Load Balancing/ Network Firewalls
| Network Layer                         |       Packets  |   Routers (Broadcast Domain) |    
|.  Network Access/Link Layer     |    Frames/ Bits | Switches (Collision domains) Intefaces cables

HOST LAYER - MEDIA LAYER

# VETH pair
- Connect two separate network namespaces (through tap)
    - Network namespace
        - Logically isolated network stack
- Connect a container or VM or virtual switch
    - Adding veth pair. Visible in ip link.
    - > ip link add tap1 type veth peer name tap2
    - Namespace add. (/var/run/netns/)
    - > ip netns add red
    - Setting tap in namespace. Not visible in ip link.
    - > ip link set tap1 netns red
    - Tap visble here.
    - > ip netns exec red bash
    - > ip netns exec red ip a 
    - > ip netns exec red ip link set tap1 up 
    - Give ip addr to namespace
    - > ip netns exec red ifconfig tap1 192.168.1.2/34
    - > ip netns exec red ping other ns(92.168.1.3) 
    - > ip route, ip a, ip link
- mininet to create custom  virtual network topology
- open - vswitch  
- 


# VXLAN
VXLAN is a tunneling protocol that encapsulates Layer 2 Ethernet frames in Layer 3 UDP packets, enabling you to create virtualized Layer 2 subnets, or segments, that span physical Layer 3 networks. Each Layer 2 subnet is uniquely identified by a VXLAN network identifier (VNI) that segments traffic. The entity that performs the encapsulation and decapsulation of packets is called a VXLAN tunnel endpoint (VTEP) and resides in hypervisor hosts.

In data centers, VXLAN is the most commonly used protocol to create overlay networks that sit on top of the physical network, enabling the use of a virtual network of switches, routers, firewalls, load balancers, and so on. The VXLAN protocol supports the virtualization of the data center network and addresses the needs of multi-tenant data centers by providing the necessary segmentation on a large scale.

VPC - Logical segment of resources

# TUN/TAP
- TUN, namely network TUNnel, simulates a network layer device and operates in layer 3 carrying IP packets. 
- TAP, namely network TAP (Terminal Access Point), simulates a link layer device and operates in layer 2 carrying Ethernet frames. 
- TUN is used with routing. TAP is used for creating a network bridge.


# Reference
- https://developers.redhat.com/blog/2018/10/22/introduction-to-linux-interfaces-for-virtual-networking