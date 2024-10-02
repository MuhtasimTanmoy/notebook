# Signal

Protocol Steps

- The first time a WhatsApp group member sends a message to a group
    - The sender generates a random `32` byte Chain Key
    - The sender generates a random `Curve25519` Signature Key key pair
    - The sender combines the `32` byte Chain Key and the public key from the Signature Key into a Sender Key message
    - Combining means it just combines the chain key and Signature public key to create the Sender key but later receivers can decompose this Sender key into the chain key and Signature public key.
    - The sender individually encrypts the Sender Key to each member of the group.
    - For all subsequent messages to the group:
        - The sender derives a Message Key from the Chain Key and updates the Chain Key.
        - The sender encrypts the message using AES256 in CBC mode.
        - The sender signs the ciphertext using the Signature Key.
        - The sender transmits the single ciphertext message to the server, which does server-side fan-out to all group participants.
    - The `hash ratchet` of the message sender’s Chain Key provides forward secrecy. 
    - Whenever a group member leaves, the session is shut down and starts over again in the Setup Phase. 
    - Group participants clear their Sender Key and start over. 
    - This is done because former members have learned everybody's Sender keys so they clear their old sender keys and exchange new sender key with each other.
    - But the Signal app uses a different approach for group chat. T
    - There is no Sender key in Signal. Each group message is treated as a direct message to the receivers. 
    - So if there are N participants, the signal client sends N messages individually encrypted with the ratchet key of each participant. 
    - You just need to have a separate ratcheting state and separate session set up so that the ratcheting state doesn't coincide with the ratcheting state of personal (direct) messaging. This is called client-side fanout.
    - This is done to prevent the server from knowing which message is made for a group and which one is a direct message.
    - But a group message can still be distinguished from a direct message because a signal client sends multiple copies of a group message at once. 
    - If the group size is large, it becomes more trivial to distinguish.

### The XEdDSA and VXEdDSA Signature Schemes
- XEdDSA enables the use of a single key pair format for both elliptic curve Diffie-Hellman and signatures
- E2E encryption variant of Signal Protocol used by all standard E2E encrypted messengers

### How do lesser encryption paradigms fall short?
- symmetric key exchange
    - how do share keys?
- asymmetric key exchange
    - slow, fixed keys
- pretty good privacy (PGP)
    - if a single key is broken, the entire chat history decryptable
- ephemeral key exchange
    - same key used only for short-duration session
    - forward secrecy: secrets broken in the future don't unlock past contents

### Terminology
- elliptic curve (EC) keys: asymmetric key pair, much stronger than RSA
- elliptic curve Diffie-Hellman (ECDH / DH): how two pairs of EC keys generate a shared secret key
- key derivation function (KDF): can "stretch" or "shrink" high-entropy bytes to yield symmetric key(s)

### Elliptic Curve Diffie Hellman
`Elliptic-curve Diffie–Hellman (ECDH)` is a key agreement protocol that allows two parties, each having an elliptic-curve public-private key pair, to establish a shared secret over an insecure channel.
- VRF 
   - Verifiable random function
- Zom android

### Implementation
- Wire 
    - Proteus
- Matrix 
    - OLM
- Pond
- Conversations
- Chat Secure
    - Omemo XMPP

### What is the "Signal Protocol"?
- Initial session setup via [X3DH](https://whispersystems.org/docs/specifications/x3dh/)
- Iterative message key generation via the [double ratchet](https://whispersystems.org/docs/specifications/doubleratchet/)
- Session management across devices via [Sesame](https://whispersystems.org/docs/specifications/sesame/)

### Session setup
- the goal is for Alice & Bob to share a 32-byte secret, used for subsequent message encryption
- Alice & Bob each have a set of (EC) identity key pairs, with public keys published to a central server
    - identity (`IK`): unique & constant for the user
    - signed pre-key (`SPK`): periodically changing (e.g., weekly/monthly) and signed with an identity key
    - one-time pre-keys (`OPK`): each used only for one session initialization
- Alice initiates session with Bob by generating an ephemeral key pair `EK_a` and calculating
    - `DH1 = DH(IK_a, SPK_b)`
    - `DH2 = DH(EK_a, IK_b)`
    - `DH3 = DH(EK_a, SPK_b)`
    - `DH4 = DH(EK_a, OPK_b)`
    - shared key: `SK = KDF(DH1 || DH2 || DH3 || DH3)`

### Double ratchet
- the goal is for both Alice & Bob to generate the same unique encryption key for each message
    - e.g., key(s) for AES256 cipher in GCM mode
    - allows for asynchronous communication
- after establishing session, Alice generates initial root & chain keys from `KDF(SK)`
- when a new message key is needed, "symmetric ratchet" is used
    - `Message Key = KDF(Chain Key, constant)`
    - `Chain Key = KDF(Chain Key, constant)`
- ephemeral keys (`EK_a` & `EK_b`) are replaced after each message round trip: "DH" ratchet
    - new shared secret `SK` generated from DH keys
    - new root & chain keys generated from `KDF(SK)`
- "DH" rachet means that `SK` changes with each round trip communication
    - temporary breaches in `SK` don't compromise all future communications

### HKDF

A key derivation function (KDF) is a basic and essential component of cryptographic systems.  Its goal is to take some source of initial keying material and derive from it one or more cryptographically strong secret keys.

```
Step 1: Extract

 HKDF-Extract(salt, IKM) -> PRK

 Options:
 Hash     a hash function; HashLen denotes the length of the
 hash function output in octets

 Inputs:
 salt     optional salt value (a non-secret random value);
 if not provided, it is set to a string of HashLen zeros.
 IKM      input keying material

 Output:
 PRK      a pseudorandom key (of HashLen octets)

 The output PRK is calculated as follows:

 PRK = HMAC-Hash(salt, IKM)
```

```
Step 2: Expand

 HKDF-Expand(PRK, info, L) -> OKM

 Options:
 Hash     a hash function; HashLen denotes the length of the
 hash function output in octets

Inputs:
 PRK      a pseudorandom key of at least HashLen octets
 (usually, the output from the extract step)
 info     optional context and application-specific information
 (can be a zero-length string)
 L        length of output keying material in octets
 (<= 255*HashLen)

 Output:
 OKM      output keying material (of L octets)

 The output OKM is calculated as follows:

 N = ceil(L/HashLen)
 T = T(1) | T(2) | T(3) | ... | T(N)
 OKM = first L octets of T

 Where:
 T(0) = empty string (zero length)
 T(1) = HMAC-Hash(PRK, T(0) | info | 0x01)
 T(2) = HMAC-Hash(PRK, T(1) | info | 0x02)
 T(3) = HMAC-Hash(PRK, T(2) | info | 0x03)
 ...

 (where the constant concatenated to the end of each T(n) is a
 single octet.)

```


### Resources
(Read these and you'll actually learn how the SP works.)
- [WhatsApp Encryption Overview](https://www.whatsapp.com/security/WhatsApp-Security-Whitepaper.pdf)
- [X3DH](https://whispersystems.org/docs/specifications/x3dh/)
- [double ratchet](https://whispersystems.org/docs/specifications/doubleratchet/)
- [Sesame](https://whispersystems.org/docs/specifications/sesame/)
- [Advanced cryptographic ratcheting](https://whispersystems.org/blog/advanced-ratcheting/)
- [A Formal Security Analysis of the Signal Messaging Protocol](https://eprint.iacr.org/2016/1013.pdf)
- [Signal Android Client Code](https://github.com/WhisperSystems/Signal-Android)
- [The XEdDSA and VXEdDSA Signature Schemes](https://www.signal.org/docs/specifications/xeddsa)
- [The X3DH Key Agreement Protocol](https://www.signal.org/docs/specifications/x3dh)
- [The Sesame Algorithm: Session Management for Asynchronous Message Encryption](https://www.signal.org/docs/specifications/sesame)
- [The Double Ratchet Algorithm](https://www.signal.org/docs/specifications/doubleratchet)
- [Elliptic Curve](https://en.wikipedia.org/wiki/Elliptic-curve_cryptography)
- [Analysing the Signal Protocol](https://eprint.iacr.org/2016/1013.pdf)
    - A manual and automated analysis of the Signal Protocol
- [A Formal Security Analysis of the Signal Messaging Protocol](https://eprint.iacr.org/2016/1013.pdf)
- [Security Analysis of the Signal Protocol](https://dspace.cvut.cz/bitstream/handle/10467/76230/F8-DP-2018-Rubin-Jan-thesis.pdf?sequence=-1)
- [Protocol Video Walkthrough](https://www.youtube.com/watch?v=vGpA6JsvGnU )