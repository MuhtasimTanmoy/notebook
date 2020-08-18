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





## Resources
- https://en.wikipedia.org/wiki/Salt_(cryptography)
- https://tools.ietf.org/html/rfc5869