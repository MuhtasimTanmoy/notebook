# TLS

`TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`

TCP is a stateful protocol with both client and server.
HTTP is stateless.

HTTPS
- Handshake 
    - Symmetric Key 
    - Generated each time
- Asymmetric encryption too costly
- Symmetric key must be generated
- Long document signing is time-consuming
- Document hash can be useful
- A hashed document signed by a private key is the digital signature

- TLS 1.2
    - Someone managed to get the private key, it's over
Diffie Hellman to rescue.