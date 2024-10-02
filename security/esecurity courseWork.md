# [eSecurity Coursework MSc](https://asecuritysite.com/esecurity)

Asymmetric Key
 - RSA
 - Elliptic Curve

Trust
- PKI
- Digital Certificate
- Signature - ECDSA  

Key Exchange Tunnel
- Diffie Hellman
- ECDH ( Elliptic Curve DH )
- SSh
- IPSec

Symmetric Key
- AES 
    - Block Cipher
- ChaCha20 
    - Stream Cipher

Hashing & MAC
- SHA-1
- SHA-256
- LM, MD5, Bcrypt
- HMAC

Tools
- OpenSSL
- hashcat
- Nmap

Github Codebase
- https://github.com/billbuchanan/esecurity

### Fundamentals
- [Unit 1](https://asecuritysite.com/csn11117/unit01)

- ASCII (7-bit format)
- UTF-16 
- Binary value
    - Hex - 4 bits at a time
    - Base-64 - 6 bits at a time
- [Calculator](https://asecuritysite.com/Coding/ascii)

- Two main operations of encryption
    - exor
    - ror/rol
- CRC is one of the most reliable error detection schemes and can detect up to 95.5% of all errors.

### Symmetric Key
Two types
- Stream Cipher
- Block Cipher

EX: DES, Twofish, AES, RC2, Blowfish, ChaCha20  Others
- Padding used in case of block cipher
- AES 128 blocks, DES 64 bit, 3 DES 112 bits
- Salt added in encryption by initialization vector which must be transmitted.
- Electronic Code Block - Same block same encryption.
- Cipher Block chaining - Only the first block salt is added from the initialization vector. Others were added from the previous vector.
- Key Entropy = log( num_of_phrases ) 

### Hash
- MD5 128 bits
- SHA 1 160 bits 
- RIPEMD used in blockchain
- The same hash can be  generated using a birthday attack

### Public Key
- Integer factorization
- Discrete Algorithm
- Elliptic Curve
- Bitcoin uses `secp256k1` and Tor uses `Curve 25519`.

### Key Exchange and Digital Certificate
- For https only server authenticated

### Tuneling
- Tunneling 
    - Over untrusted network
- Host to host - tunnel
- In the case of VPN a tunnel is created and can't see hop in `tracert`. 

```bash
openssl s_client  -connect www.google:443 
openssl dgst -md5 file
openssl genrsa -out mykey.pem 1024
openssl rsa -in mykey.pem -pubout > mykey.pub
echo "This is a group of words that should not be considered random anymore so never use this to generate a private key" | openssl sha256
```

### Threat Classification
- Intrusion
- Blocking
- Malware

### Attacks
- Buffer overflow
- DOs

- IP Spoofing prevention
    - `/etc/sysctl.conf` used to override the default kernel param
    - `net.ipv4.conf.default.rp_filter=1`
    - `net.ipv4.conf.all.rp_filter=1`

- Firewall Type
    - Packet Filtering
    - Application Gateway
    - Circuit-level gateway
    - Stateful packet inspection