# OTR
- Off the record
- As OTR sessions existed between exactly two clients, the chat history would not be synchronized across other clients of the involved parties. Furthermore, OTR chats were only possible if both participants were online at the same time, due to how the rolling key agreement scheme of OTR worked.

---

# Signal protocol
- Prekey bundle
    - IPKb - identity private key bundle
    - SPKb - Signed private key bundle
    - OPKb - Optional private key bundle
- Triple diffie hellman
- Safety number
    - Concat the public key of both party. And check this out of bound.
- Signal changes key to every single message.

---

## Extended Tripple Diffie-Hellman x3dh
- 
![Tripple DH](screen/signal.png)
      
---

## Forward Secrecy
- Forward secrecy (FS), also known as perfect forward secrecy (PFS), is a feature of specific key agreement protocols that gives assurances that session keys will not be compromised even if long-term secrets used in the session key exchange are compromised.
For HTTPS the long-term secret is typically the private signing key of the server.
The session key is kept different and changed over long period of time.

----

## Double ratchet algorithm / Axolotl Ratchet
- Once the session established then the key goes through a one way function that acts as ratchet to generate more key.
- The key is gone through KDF (Key Derivation Function).
![Double Ratchet](screen/Ratchet.png)

---

## Pre keys
- For diffie hellman key exchange pre keys loaded in case of offline message. 
- Ellyptic curve - curve25519 
- But only diffie hellman has man in the middle attack. So RSA needed. Authenticated diffie hellman key exchange.
- For storing pre keys PKI infra needed. Keybase.

---

## Group Message Encryption - [reference](https://www.youtube.com/watch?v=tCKd6xBqyDw)

- Creating one shared group key, send it to server for fan out instead of pairwise encryption
- Sender keys does not have post compromise security

---

# PreKeys
This protocol uses a concept called 'PreKeys'. A PreKey is an ECPublicKey and an associated unique ID which are stored together by a server. PreKeys can also be signed.

At install time, clients generate a single signed PreKey, as well as a large list of unsigned PreKeys, and transmit all of them to the server.

---

# Sessions
Signal Protocol is session-oriented. Clients establish a "session," which is then used for all subsequent encrypt/decrypt operations. There is no need to ever tear down a session once one has been established.

Sessions are established in one of three ways:

- PreKeyBundles. A client that wishes to send a message to a recipient can establish a session by retrieving a PreKeyBundle for that recipient from the server.
- PreKeySignalMessages. A client can receive a PreKeySignalMessage from a recipient and use it to establish a session.
- KeyExchangeMessages. Two clients can exchange KeyExchange messages to establish a session.

---

# State
An established session encapsulates a lot of state between two clients. That state is maintained in durable records which need to be kept for the life of the session.

State is kept in the following places:

- Identity State. Clients will need to maintain the state of their own identity key pair, as well as identity keys received from other clients.
- PreKey State. Clients will need to maintain the state of their generated PreKeys.
- Signed PreKey States. Clients will need to maintain the state of their signed PreKeys.
- Session State. Clients will need to maintain the state of the sessions they have established.

---

# Workflow
- Alice Bob communicating
- Bob publishes his public key in Key Directory
- Alice fetches from it key from it.
    - Normal approach would be to just generate a session key, encrypt it with bob's key and send. But it looses forward secrecy.
    - Second approach use one prekey signed so it is verified that it is linked to Identity key. But has no forward secrecy. Timed change of this prekey. 
- Protocol uses a combination of those.   
- So protocol says a set of one time prekey generated as well. So received message will be decrypted by both identity and prekey. Later deleted for forward secrecy. Outcome shared session key.
- End to end encrytion is east. End to end authentication is not.

![](screen/TextSecure.png)

---

# HKDF


# Resources
- [Omemo Encryption](https://xmpp.org/extensions/xep-0384.html)
- [Forward Secrecy](https://en.wikipedia.org/wiki/Forward_secrecy)
- https://www.youtube.com/watch?v=vsXMMT2CqqE
- https://youtu.be/oRZoeDRACrY
- https://www.youtube.com/watch?v=JWOGol6dsI0
- https://www.youtube.com/watch?v=_4muqgreEXE
- https://medium.com/asecuritysite-when-bob-met-alice/alice-whispers-to-bob-at-the-core-of-privacy-in-the-21st-century-is-extended-triple-51736dad527d
- [Text Secure Protocol **](https://www.youtube.com/watch?v=7WnwSovjYMs)