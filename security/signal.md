# Signal

I know most of the members here are ordinary users but maybe some of you who actually know about it and want to see some more details which was missing in this conference and both the computerphile videos Instant Messaging and the Signal Protocol - Computerphile, Double Ratchet Messaging Encryption - Computerphile

This is how What's app security whitepaper described it:

The first time a WhatsApp group member sends a message to a group:

The sender generates a random 32-byte Chain Key.

The sender generates a random Curve25519 Signature Key key pair.

The sender combines the 32-byte Chain Key and the public key from the Signature Key into a Sender Key message.

Combining means it just combines chain key and Signature public key to create Sender key but later receivers can decompose this Sender key into chain key and Signature public key.

The sender individually encrypts the Sender Key to each member of the group.

For all subsequent messages to the group:

The sender derives a Message Key from the Chain Key, and updates the Chain Key.

The sender encrypts the message using AES256 in CBC mode.

The sender signs the ciphertext using the Signature Key.

The sender transmits the single ciphertext message to the server, which does server-side fan-out to all group participants.

The “hash ratchet” of the message sender’s Chain Key provides forward secrecy. Whenever a group member leaves, the session is shut down and starts over again in the Setup Phase. Group participants clear their Sender Key and start over. This is done because former member has learned everybody's Sender keys so they clear their old sender key and exchange new sender key with each other.

But Signal app uses a different approach for group chat. There is no Sender key in Signal. Each group message is treated as direct message to the receivers. So if there are N participants, signal client sends N messages individually encrypted with the ratchet key of each participant. You just need to have a separate ratcheting state and separate session setup so that ratcheting state doesn't coincide with ratcheting state of personal(direct) messaging. This is called client-side fanout.

This is done to prevent server from knowing which message is made for group and which one is a direct message. But a group message can still be distinguished from a direct message because signal client sends multiple copies of a group message at once. If the group size is large, it becomes more trivial to distinguish.

## The XEdDSA and VXEdDSA Signature Schemes
- XEdDSA enables use of a single key pair format for both elliptic curve Diffie-Hellman and signatures.

## Signal Protocol Summary
A very brief overview of the Signal Protocol.

(disclaimer: I am not a crypto expert, just a guy who has read up a bit on this stuff.)

## What is E2E encryption?
- a variant of SP used by all standard E2E encrypted messangers
- why is it important?

## How do lesser encryption paradigms fall short?
- symmetric key exchange
    - how to share key?
- asymmetric key exchange
    - slow, fixed keys
- pretty good privacy (PGP)
    - if single key is broken, entire chat history decryptable
- ephemeral key exchange
    - same key used only for short-duration session
    - forward secrecy: secrets broken in the future don't unlock past contents

## Terminology
- elliptic curve (EC) keys: assymetric key pair, much stronger than RSA
- elliptic curve Diffie-Hellman (ECDH/DH): how two pairs of EC keys generate a shared secret key
- key derivation function (KDF): can "stretch" or "shrink" high-entropy bytes to yield symmetric key(s)

## What is the "Signal Protocol"?
- initial session setup via [X3DH](https://whispersystems.org/docs/specifications/x3dh/)
- iterative message key generation via the [double ratchet](https://whispersystems.org/docs/specifications/doubleratchet/)

Also, session management across devices via [Sesame](https://whispersystems.org/docs/specifications/sesame/)

## Session setup
- goal is for Alice & Bob to share 32-byte secret, used for subsequent message encryption
- Alice & Bob each have a set of (EC) identity key pairs, with public keys published to central server
    - identity (`IK`): unique & constant for user
    - signed pre-key (`SPK`) : periodically changing (e.g., weekly/monthly) and signed with identity key
    - one-time pre-keys (`OPK`): each used only for one session initialization
- Alice initiates session with Bob by generating an ephemeral key pair `EK_a` and calculating
    - `DH1 = DH(IK_a, SPK_b)`
    - `DH2 = DH(EK_a, IK_b)`
    - `DH3 = DH(EK_a, SPK_b)`
    - `DH4 = DH(EK_a, OPK_b)`
    - shared key: `SK = KDF(DH1 || DH2 || DH3 || DH3)`

## Double ratchet
- goal is for both Alice & Bob to generate same unique encryption key for each message
    - e.g., key(s) for AES256 cipher in GCM mode
    - allows for asynchronous communication
- after establishing session, Alice generates initial root & chain keys from `KDF(SK)`
- when new message key is needed, "symmetric ratchet" is used
    - `Message Key = KDF(Chain Key, constant)`
    - `Chain Key = KDF(Chain Key, constant)`
- ephemeral keys (`EK_a` & `EK_b`) are replaced after each message round trip: "DH" ratchet
    - new shared secret `SK` generated from DH keys
    - new root & chain keys generated from `KDF(SK)`
- "DH" rachet means that `SK` changes with each round trip communication
    - temporary breaches in `SK` don't compromise all future communications

## Resources
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