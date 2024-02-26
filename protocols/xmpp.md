# XMPP Framework

-   **X :**  It means eXtensible. XMPP is a open source project which can be changed or extended according to the need.
-   **M :**  XMPP is designed for sending messages in real time. It has very efficient push mechanism compared to other protocols.
-   **P :**  It determines whether you are online/offline/busy. It indicates the state.
-   **P :**  XMPP is a protocol, that is, a set of standards that allow systems to communicate with each other

- XMPP is usually broken into two parts : 
  - the XMPP Core Services and 
  - XMPP Extension Protocols (XEPs).
 
- The core part comprises of the features (services) deemed essential to most XMPP applications like
   - One to one Messaging
   - Data Communication Security Mechanisms
   - Presence and Contact Lists

Extensions - 
- Multi User chat
- Service Discovery
- Clustering 
- Federation


The original protocol for XMPP is [Transmission Control Protocol](https://www.geeksforgeeks.org/computer-network-tcpip-model/), using open ended XML streams over long lived TCP connections. PORT 5222.

- The core of XMPP is the exchange of small, structured chunks of information(in XML). 
- Like HTTP, XMPP is a client-server protocol, but it differs from HTTP by allowing either side to send data to the other asynchronously.
- XMPP connections are long lived, and data is pushed instead of pulled.
- Not invented here syndrome do not fall in.
- XMPP is an awful and heavyweight protocol (streaming XML?;). It's spec is so big that there is no complete implementation of it. The most complete and most scalable implementation is ejabberd.
- XMPP is essentially a streaming protocol that makes it possible to exchange XML fragments between any two network endpoints.


Multiple implementations - 
- ejabbered
- openfire 
- prosody - lightweight


### XMPP Core

-  Core 
   — Information about the core XMPP technologies for XML streaming
-  Jingle 
   — SIP compatible multimedia signalling for voice, video, file transfer, and other applications
-  Multi-user chat 
   — Flexible, multi-party communication
-  Pubsub 
   — Alerts and notifications for data syndication, rich presence, and more

### Rosters ( Contact List ) subscriptions  and presence

Basically your client (gajim, pidgin, adium, etc) sends packets (XML) to a router (XMPP "server") that determines who gets to see a copy of that packet.  
  
Because it's XML-based, however, there are many, many extensions to XMPP - including MUC (Multi-user chat), or chat rooms. In their example, your packet is sent to the router with the address of the MUC room, and the router makes sure the packets go to everyone subscribed to that room.  
  
Then there's the "presence" part of the name - when you want to chat with someone, you have to "subscribe" to them - in Facebook terms, you add them as a friend, and they accept you, subscribing to you (usually) in return. When you login to the XMPP server, your status message is delivered to anyone who has subscribed to your presence - so they know you just logged on and can message you. There's quite a bit more you can do with it, but that's the basics.

### Fundamental Exchange of Info
The most basic unit of communication in XMPP is called a stanza.

Stanzas have three possible names( XML tag names) in XMPP ,these can be a Message stanza , an IQ stanza and a Presence stanza.

- Message
	- <message type=”chat”/> ( chat message stanza) 
	- < message type=”groupchat”/> ( group chat message stanza) 
	-  < message type=”error”/> (error message stanza)
	- from to type id
	- XMPP stanzas can sometimes contain child (nested) child XML tags to structure the information within.
- Presence
	- The stanza advertises the online status( network availability) of other entities. Presence works like subscription in XMPP.
	- When you are interested in the presence of some JID ,you subscribe to their presence ,in other terms ,you tell the XMPP server “every time this JID sends you a presence update ,I want to be notified”.Of course the server asks the JID holder if he accepts to disclose his presence information to you.
	- It is important to note that just because A is subscribed to B’s presence updates doesn’t mean that B is automatically subscribed to A’s presence updates.If what we want is for A and B to be subscribed to each other’s presence updates.A has to explicitly subscribe to B and B has to explicitly subscribe to A.

- IQ ( Info / Query )
  - The IQ( Info/Query) stanza is used to get some information from the server ( info about the server or its registered clients) or to apply some settings to the server.
	  - <iq type=”get”/> stanzas are used to get(ask) some information ( from the server). 
	  - <iq type=”set”/> stanzas are used to apply some settings to the server.
	  - When you send get/set IQ stanzas to the server ,it can reply either with an <iq type=”result”/> stanza when your request has been successfully processed by the server.
	  -  <iq type=”error”/> stanza when something has gone wrong with your request
	- jabber:iq:roster XML namespace
	- An XML namespace is a way of giving more details about what the stanza is meant to do.For example the server upon receiving the iq from the client ( the one with a C: on the left),it first sees that it is a get IQ and it knows the stanza is asking for some information. Looking the XML name space ( xmlns) it knows exactly what is being asked for :”the contact list for the JID where the stanza comes from “. The XMPP engine in the server is programmed to know that when a client sends jabber:iq:roster namespaced IQ ,it wants to retrieve its contact list.There are other namespaces in XMPP for other uses and you will surely come across them in your XMPPing journey.
	- .A jid is valid if it contains one “@” character and passwords of more than four characters are supported.This is a simple policy that comes by default with the code that Android Studio has generated for us.We leave it that way for this tutorial.
	- [https://www.blikoontech.com/](https://www.blikoontech.com/)

- These stanza types provide three different communication primitives: a "push" mechanism for generalized messaging, a specialized "publish-subscribe" mechanism for broadcasting information about network availability, and a "request-response" mechanism for more structured exchanges of data (similar to [HTTP]).


### Encryption
There is no TLS usage in xmpp stream as it does not support raw data only frame. It can be enabled at websocket layer.

### Websocket Binding
- A WebSocket binding for XMPP provides higher performance than the current HTTP binding for XMPP.
- During the WebSocket handshake, the client MUST include the value
   'xmpp' in the list of protocols for the 'Sec-WebSocket-Protocol'
   header.  The reply from the server MUST also contain 'xmpp' in its
   own 'Sec-WebSocket-Protocol' header in order for an XMPP subprotocol
   connection to be established.
- The process whereby a client connects to a server, exchanges XML stanzas, and ends the connection is:
	- Determine the IP address and port at which to connect, typically
       based on resolution of a fully qualified domain name (Section 3.2)
    - Open a Transmission Control Protocol [TCP] connection
    - Open an XML stream over TCP (Section 4.2)
    - Preferably negotiate Transport Layer Security [TLS] for channel
       encryption (Section 5)
    - Authenticate using a Simple Authentication and Security Layer
       [SASL] mechanism (Section 6)
    - Bind a resource to the stream (Section 7)
    - Exchange an unbounded number of XML stanzas with other entities
       on the network (Section 8)
    - Close the XML stream (Section 4.4)
    - Close the TCP connection
- https://tools.ietf.org/html/rfc7395
- https://tools.ietf.org/html/rfc6455

### XMPP MUC
- [Do I need to Alloc Into XMPPROOM Object always for different operation of Room?](https://github.com/robbiehanson/XMPPFramework/issues/642)
- [Building a group chat with the XMPPFramework and eJabberd](https://medium.com/@dylanshine/building-a-group-chat-with-the-xmppframework-59fa17ecf4a0)