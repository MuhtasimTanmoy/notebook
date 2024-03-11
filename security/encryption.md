# Cryptography

### Diffie Hellman

Web protocols use a combination of symmetric and asymmetric encryption to establish secure connections.

Here the symmetric portion is for forward secrecy. 
And asymmetric for authentication.

Example: TLS.

- Diffie Hellman Key Exchange
	- Prime Modulus and Generator `( G % P )`. Available to all.
	- A generates random and send  `G ^ R_A % P`. SEND_IT_TO_ALL. Available to all.
	- B generates random and send `G ^ R_B % P` . 
	SEND_IT_TO_ALL. Available to all.
	- Now as `G ^ R_A ^ R_B % P` is calculated and the secret key.
	- Others do not have R_A R_B.

- *Drawback*
    - In case of multiple people communication . OVERHEAD.
    - Extra communication. Round trip time.

### RSA
Public Private key based Encryption
- Formula

```
(m^(ed) == m ) mod  N
ed == 1 (mod phi( N ))
```

- Prime Factorization
	- Given any number get the two primes which multiplies it. 
	- ed = very big prime factorization

- Eulers Totient Function

	- phi(N) = how many number less then or equal to N that do not share any common factor.
	- Example : phi(8)
    	- Numbers to consider 
        	- 1 2 3 4 5 6 7 8
        	- 1 3 5 7 -> has one factor common which is 1.
        	- So, phi(8) = 4
	- phi(prime number) = p - 1
    	- As no number less than share common factor.

N = p1*p2 > big prime factorization
phi (N) = (p1-1) * (p2-1)

### Eulers Theorem

m ^ phi(n) congruent to =  1 mod n
m ^ (k * phi(n)  +1)  ==  m mod n

- Walkthrough
	- Generate two prime number.           [ 3 and 11 ]
	- Multiply > prime factorization       [ N = 33 ]
	- phi(N) > toteint                     [ phi(N) = 20 ]
	- Choose exponent between 1 - phi(N) 
		- E = odd and Co prime             [ E coprime to phi(N) and N]
	- N & E public key                     [ (E,N) ]
	- D = ( 2 * phi (N) + 1 ) / E          [ (D,N) ]
	- ( data ^ e ) % N = encrypted text    
	- ( encrypted text ^ d ) % N  = data

### AES

- Chacha cypher
	- Replacement for aes
	- Works well on low end device


### Salt
- A salt is random data that is used as an additional input to a one-way function that hashes data, a password or passphrase.
- Salts are closely related to the concept of a cryptographic nonce.
- Protects against rainbow attack.

- Password stretching 
    - Multiple hash `Hash(Hash(Hash(Hash…(Hash(salt||password)))…)` 
    - `Argon2` algorithm

### Pepper
- That is, another random value concatenated to the password, such that the stored value is `Hash(pepper||salt||password)`. 
- The pepper is then not stored at all. Both the login server and password cracker need to brute force the unknown pepper value, slowing password hash comparisons for both parties.

### MAC (Message Authentication Code)
- H(key, message) = Hash
- Here, key & message available on both end denoting integrity of data.

### Secrecy

- Forward secrecy = Perfect Forward Secrecy, 
- Backward secrecy = Future Secrecy.

- The above terms are often discussed in the setting of secure channel establishment protocols, e.g., TLS, Signal, etc. In such a protocol, consider two parties, a client and a server, try to communicate with each other securely.

- The server (and the client if client-authentication is needed) is granted a certificate that shows its public key, and the server (and the client) itself knows the corresponding private key (a.k.a. the long-term secret).

- They essentially use the long-term secret and some randomness to compute and share a secret session key (only used within a session) and establish a secure communication channel based on the session key, e.g., using an authenticated encryption (with associated data) scheme.

- Forward secrecy means if the long-term secret (together with the party's current session key and all other secret states) is corrupted (i.e., revealed), then the past sessions are still secure, i.e., the confidentiality of the previous messages exchanged between the client and the server is not compromised.

 - I think people call this forward secrecy because they want the encrypted messages in a session to be secure even if "forward" long-term key corruption occurs. TLS is an example that achieves forward secrecy with Diffie-Hellman key exchange.

- Backward secrecy guarantees the "opposite direction" of forward secrecy. In other words, this security guarantees that the encrypted messages in a session should remain secure even if "backward" long-term key corruption occurs. 

- People more often call this future secrecy perhaps because they want to emphasize that even if at some point the long-term secret (together with the party's current session key and all other secret states) is corrupted the future messages can still be secure (if the previously corrupted party somehow becomes "clean" again). (I agree that the terms are a mess because "future secrecy" looks and sounds almost the same as "forward secrecy".) 

- Signal is an example that achieves backward secrecy with the Double Ratchet Algorithm which can self-heal itself soon after corruption.


### References
- [RSA Encryption](https://www.khanacademy.org/computing/computer-science/cryptography/modern-crypt/v/rsa-encryption-part-4)
- [Padding](https://asecuritysite.com/encryption/padding)
- [Salt (cryptography)](https://en.wikipedia.org/wiki/Salt_(cryptography))
- [HMAC-based Extract-and-Expand Key Derivation Function (HKDF)](https://tools.ietf.org/html/rfc5869)