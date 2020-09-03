
# Signal

I've been doing an intensive study to learn how Signal protocol works for my presentation as a key-note speaker. There I'm going to explain about its working of end-to-end encryption.

I was able to understand it fairly easy through this conference NorthSec 2015 - Trevor Perrin - TextSecure Protocol: Present and Future until he talked about multi-party with just an overview.

I know most of the members here are ordinary users but maybe some of you who actually know about it and want to see some more details which was missing in this conference and both the computerphile videos Instant Messaging and the Signal Protocol - Computerphile, Double Ratchet Messaging Encryption - Computerphile

This is how What's app security whitepaper described it:

The first time a WhatsApp group member sends a message to a group:

The sender generates a random 32-byte Chain Key.

The sender generates a random Curve25519 Signature Key key pair.

The sender combines the 32-byte Chain Key and the public key from the Signature Key into a Sender Key message.

Combining means it just combines chain key and Signature public key to create Sender key but later receivers can decompose this Sender key into chain key and Signature public key.

4. The sender individually encrypts the Sender Key to each member of the group.

For all subsequent messages to the group:

The sender derives a Message Key from the Chain Key, and updates the Chain Key.

The sender encrypts the message using AES256 in CBC mode.

The sender signs the ciphertext using the Signature Key.

The sender transmits the single ciphertext message to the server, which does server-side fan-out to all group participants.

The “hash ratchet” of the message sender’s Chain Key provides forward secrecy. Whenever a group member leaves, the session is shut down and starts over again in the Setup Phase. Group participants clear their Sender Key and start over. This is done because former member has learned everybody's Sender keys so they clear their old sender key and exchange new sender key with each other.

But Signal app uses a different approach for group chat. There is no Sender key in Signal. Each group message is treated as direct message to the receivers. So if there are N participants, signal client sends N messages individually encrypted with the ratchet key of each participant. You just need to have a separate ratcheting state and separate session setup so that ratcheting state doesn't coincide with ratcheting state of personal(direct) messaging. This is called client-side fanout.

This is done to prevent server from knowing which message is made for group and which one is a direct message. But a group message can still be distinguished from a direct message because signal client sends multiple copies of a group message at once. If the group size is large, it becomes more trivial to distinguish.

### The XEdDSA and VXEdDSA Signature Schemes
- XEdDSA enables use of a single key pair format for both elliptic curve Diffie-Hellman and signatures.
- 


### 
### 
### 
### 



# Resources
- https://www.signal.org/docs/specifications/xeddsa
- https://www.signal.org/docs/specifications/x3dh
- https://www.signal.org/docs/specifications/sesame
- https://www.signal.org/docs/specifications/doubleratchet