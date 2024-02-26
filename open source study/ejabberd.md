# Ejabbered
- XMPP Server + MQTT Broker + SIP Service

- Github link
    - https://github.com/processone/ejabberd

- System Dependencies
    - erlang elixir openssl expat libyaml libiconv libgd sqlite rebar rebar3 automake autoconf 

- Library Dependencies
    - https://github.com/erlang-lager/lager
    - https://github.com/processone/p1_utils
    - https://github.com/processone/cache_tab
    - https://github.com/processone/fast_tls
    - https://github.com/processone/stringprep
    - https://github.com/processone/fast_xml
    - https://github.com/benoitc/erlang-idna
    - https://github.com/processone/xmpp
    - https://github.com/processone/fast_yaml
    - https://github.com/processone/yconf
    - https://github.com/davisp/jiffy
    - https://github.com/processone/p1_oauth2"
    - https://github.com/processone/pkix
    - https://github.com/potatosalad/erlang-jose
    - https://github.com/processone/eimp
    - https://github.com/processone/mqtree
    - https://github.com/processone/p1_acme.git
    - https://github.com/dvv/base64url.git
    - https://github.com/processone/p1_pgsql
    - https://github.com/processone/ezlib
    - https://github.com/DeadZen/goldrush.git
    - https://github.com/benoitc/unicode_util_compat.git


## Architecture overview
![alt text](https://docs.ejabberd.im/static/images/architect/ejabberd_large_scale.png)

![alt text](https://image.slidesharecdn.com/xmppacademy2-151105134735-lva1-app6892/95/xmpp-academy-2-7-638.jpg?cb=1446731376)

- Message buffer
- No internal state kept. Helps in case of node failure.
- Connection
    - The client to server connection (typically on tcp/5222) is handled by the module ejabberd_c2s. The server to server connection (typically on tcp/5269) is handled by the modules ejabberd_s2s, ejabberd_s2s_in, ejabber_s2s_out. The HTTP bindings are handled by the ejabberd_http module.
- Router
    - The router handles the routing of most of the messages, i.e., when a Jabber client sends a to another entity, how is the message routed to the correct destination? 
    - First ejabberd determines whether the message is a local or a remote one. It does so by looking at the "to" attribute to see if the host implied by the "to" attribute is hosted in itself. 
    - If so, the message is local; and is handled by ejabberd_local; otherwise it is treated as an s2s message.
- Modules
    - In additional to the core Jabber and Router logics, there is a large part of the ejabberd which can be plugged in only when necessary, and they are called modules. 
    - Modules can be started / stopped dynamically at any time, thus making the ejabberd server highly extensible even at runtime. 
    - Modules are widely used for various extensions (the so-called 'XEP's).
- Hooks
    - A hook is a way by which you can change the behaviour of ejabberd by injecting your new code into the system, without changing any existing code. 
    - For example, if you want to roll up your message filter to filter out messages you don't want, you can add a module hooking to the "filter_packet/3" hook. 
    - If you want to keep track of all the messages clients sent, you can write a function hooking to 'user_send_packet/3'.
- Access Control
    - Access Control. All users (including real jabber client users as well as administrators) are stored the same way in ejabberd. 
    - Their privileges are determined by the groups they belong to. 
    - Hence, the access control modules in ejabberd allow us to distinguish users with their groups, thus providing different services for different users. 
    - Utils and Libraries. Some other libraries and utils exist in ejabberd for common purposes, e.g.: XML processing, SASL authentication, Encodings, Logger, etc. It is worth noting the ejabberd_logger is a very good logger module perfectly usable by any other projects.
- The main difference between the jabber:component:* namespaces and the 'jabber:client' or 'jabber:server' namespace is authentication.

## PUB SUB
- Subscribe 
- Unsubscribe
- Configure
- Retrieve message / item
- Publish message
- Delete message
- Create node
- Configure
- Delete Node
- Purge Node
- Manage subscription
- Manage affiliation

- A core router for high level use case implementation
- Plugins to handle nodes, subscriptions, items at lower level and interfacing with database
- NodeTree Plugin 
    - Handles storage and organization of PubSub nodes
    - get create delete node
    - tree both internal odbc backend
    - virtual no backend
    - dag XEP 0248

- node_flat
- odbc - open database connectivity
- https://www.haproxy.org/download/1.8/doc/proxy-protocol.txt


## IRC
- Server
    - backbone
- Clients
    - Unique nickname having max length 9 Chars
- Channels
    - # for channel
    - @ for operator


The standard structure of a network of IRC servers is a tree.[35] Messages are routed along only necessary branches of the tree but network state is sent to every server[36] and there is generally a high degree of implicit trust between servers. This architecture has a number of problems. A misbehaving or malicious server can cause major damage to the network[37] and any changes in structure, whether intentional or a result of conditions on the underlying network, require a net-split and net-join. This results in a lot of network traffic and spurious quit/join messages to users[38] and temporary loss of communication to users on the splitting servers. Adding a server to a large network means a large background bandwidth load on the network and a large memory load on the server. Once established however, each message to multiple recipients is delivered in a fashion similar to multicast, meaning each message travels a network link exactly once.[39] This is a strength in comparison to non-multicasting protocols such as Simple Mail Transfer Protocol (SMTP) or Extensible Messaging and Presence Protocol (XMPP).  

- Servers provide the three basic services required for realtime
   conferencing defined by the "Internet Relay Chat: Architecture"
   [IRC-ARCH]: client locator (via the client protocol [IRC-CLIENT]),
   message relaying (via the server protocol defined in this document)
   and channel hosting and management (following specific rules [IRC-
   CHAN]).
   
## Actor Model
 - Actors instead of objects
 - No shared state between actors
 - Asyncronous message passing
 - Mailboxes to buffer incoming messages
 - React to messages
    - change own state
    - can send message to others
 - Messages
 - Mailbox - (Message Queue)

## System Up & Running takeaways

## Log
    - /usr/local/var/log/ejabberd/ejabberd.log


## Scripts
```
/usr/local/sbin/ejabberdctl
/usr/local/sbin/ejabberdctl start 
/usr/local/sbin/ejabberdctl stop
/usr/local/sbin/ejabberdctl live
/etc/init.d/ejabberd
sudo vim /etc/ejabberd/ejabberd.yml
sudo cat /usr/local/etc/ejabberd/ejabberd.yml
ejabberdctl register admin1 example.org FgT5bk3
```

### Running endpoint 
    - http://localhost:5280/admin

## Port scan result

PORT      STATE    SERVICE

21/tcp    open     ftp

22/tcp    open     ssh

25/tcp    filtered smtp

26/tcp    open     rsftp

53/tcp    open     domain

80/tcp    open     http

110/tcp   open     pop3

111/tcp   filtered rpcbind

135/tcp   filtered msrpc

139/tcp   filtered netbios-ssn

143/tcp   open     imap

443/tcp   open     https

445/tcp   filtered microsoft-ds

465/tcp   open     smtps

587/tcp   open     submission

993/tcp   open     imaps

995/tcp   open     pop3s

2222/tcp  open     EtherNetIP-1

3306/tcp  open     mysql

5432/tcp  open     postgresql

6666/tcp  filtered irc

6667/tcp  filtered irc

12345/tcp filtered netbus

- Other alternative
    - Matrix, which is pull based

## References
- [Installation Guide](https://www.ejabberd.im/files/doc/guide.html#htoc2)
- [How it works](https://docs.ejabberd.im/admin/guide/clustering/)
- [Modules](https://docs.ejabberd.im/admin/configuration/modules/#mod-sip)
- [Internals](https://docs.ejabberd.im/developer/guide/)
- [Stanza Routing](https://docs.ejabberd.im/developer/extending-ejabberd/stanza-routing)
- https://trisquel.info/files/ejabberd%202.1.pdf
- http://www.owl.homeip.net/manuals/services/ejabber/
- https://raymii.org/s/tutorials/Set_up_a_federated_XMPP_Chat_Network_with_ejabberd.html
- https://tutslaptrinh.com/tutorial-detail/architecture-ejabberd
- https://trisquel.info/files/ejabberd%202.1.pdf 