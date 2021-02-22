# Salt
A salt is random data that is used as an additional input to a one-way function that hashes data, a password or passphrase.

Salts are closely related to the concept of a cryptographic nonce.

Protects against rainbow attack.

**Password stretching** 
- Multiple hash `Hash(Hash(Hash(Hash…(Hash(salt||password)))…)` 
- Argon2 algorithm


**Pepper** 
- That is, another random value concatenated to the password, such that the stored value is `Hash(pepper||salt||password)`. The pepper is then not stored at all. Both the login server and password cracker need to brute force the unknown pepper value, slowing password hash comparisons for both parties.


# MAC (Message Authentication Code)
- H(key, message) = Hash
- Here, key & message available on both end denoting integrity of data.


# Secrecy

In cryptography, forward secrecy = perfect forward secrecy, backward secrecy = future secrecy.

First, recall some background. The above terms are often discussed in the setting of secure channel establishment protocols, e.g., TLS, Signal, etc. In such a protocol, consider two parties, a client and a server, try to communicate with each other securely. The server (and the client if client-authentication is needed) is granted a certificate that shows its public key, and the server (and the client) itself knows the corresponding private key (a.k.a. the long-term secret). They essentially use the long-term secret and some randomness to compute and share a secret session key (only used within a session) and establish a secure communication channel based on the session key, e.g., using an authenticated encryption (with associated data) scheme.

Forward secrecy means if the long-term secret (together with the party's current session key and all other secret states) is corrupted (i.e., revealed), then the past sessions are still secure, i.e., the confidentiality of the previous messages exchanged between the client and the server is not compromised. I think people call this forward secrecy because they want the encrypted messages in a session to be secure even if "forward" long-term key corruption occurs. TLS is an example that achieves forward secrecy with Diffie-Hellman key exchange.

Then, as you may guess, backward secrecy guarantees the "opposite direction" of forward secrecy. In other words, this security guarantees that the encrypted messages in a session should remain secure even if "backward" long-term key corruption occurs. People more often call this future secrecy perhaps because they want to emphasize that even if at some point the long-term secret (together with the party's current session key and all other secret states) is corrupted the future messages can still be secure (if the previously corrupted party somehow becomes "clean" again). (I agree that the terms are a mess because "future secrecy" looks and sounds almost the same as "forward secrecy".) Signal is an example that achieves backward secrecy with the Double Ratchet Algorithm which can self-heal itself soon after corruption.

## Resources
- https://en.wikipedia.org/wiki/Salt_(cryptography)
- https://tools.ietf.org/html/rfc5869