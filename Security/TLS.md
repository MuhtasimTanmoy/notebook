# TLS

`TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`

TCP is statefull protocol with both client and server.
Http is stateless.

HTTPS 
- Handshake - Symmetric Key - Generated each time
- Asymetric encryption too costly
- Symmetric key must be generated
- Long document signing is time consuming
- Document hash can be useful
- Hashed document signed by private key is digital signature

- TLS 1.2
	- Someone manage to get the private key, it's over
Diffie hellman to rescue.