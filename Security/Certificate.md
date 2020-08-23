## SSL/TLS Handshake
The Secure Socket Layer protocol was created by Netscape to ensure secure transactions between web servers and browsers. The protocol uses a third party, a Certificate Authority (CA), to identify one end or both end of the transactions. This is in short how it works.

- A browser requests a secure page (usually https://).

- The web server sends its public key with its certificate.

- The browser checks that the certificate was issued by a trusted party (usually a trusted root CA), that the certificate is still valid and that the certificate is related to the site contacted.

- The browser then uses the public key, to encrypt a random symmetric encryption key and sends it to the server with the encrypted URL required as well as other encrypted http data.

- The web server decrypts the symmetric encryption key using its private key and uses the symmetric key to decrypt the URL and http data.

- The web server sends back the requested html document and http data encrypted with the symmetric key.

- The browser decrypts the http data and html document using the symmetric key and displays the information.

- TLS 1.2 uses ECDHE_RSA
- In case of TLS why not use only RSA. Because of perfect forward secracy. 
- Diffie hellman does the sesison shared secret key. RSA verifies it. Out put a session key which is symmetric and fast unlike RSA.


## Certificate
How do you know that you are dealing with the right person or rather the right web site. This someone, you have to implicitly trust: you have his/her certificate loaded in your browser (a root Certificate). A certificate, contains information about the owner of the certificate, like e-mail address, owner's name, certificate usage, duration of validity, resource location or Distinguished Name (DN) which includes the Common Name (CN) (web site address or e-mail address depending of the usage) and the certificate ID of the person who certifies (signs) this information. It contains also the public key and finally a hash to ensure that the certificate has not been tampered with. As you made the choice to trust the person who signs this certificate, therefore you also trust this certificate. This is a certificate trust tree or certificate path. Usually your browser or application has already loaded the root certificate of well known Certification Authorities (CA) or root CA Certificates. The CA maintains a list of all signed certificates as well as a list of revoked certificates. A certificate is insecure until it is signed, as only a signed certificate cannot be modified. You can sign a certificate using itself, it is called a self signed certificate. All root CA certificates are self signed.

- PEM - base64 encoded DER(Binary) cert

-----BEGIN CERTIFICATE REQUEST----- and -----END CERTIFICATE REQUEST----- show a CSR in PEM format.
-----BEGIN RSA PRIVATE KEY----- and -----END RSA PRIVATE KEY----- show a private key in PEM format.
-----BEGIN CERTIFICATE----- and -----END CERTIFICATE----- show a certificate file in PEM format.

- DER - binary encoded

- PEM - Governed by RFCs, its used preferentially by open-source software. It can have a variety of extensions (.pem, .key, .cer, .cert, more)

- PKCS7 - An open standard used by Java and supported by Windows. Does not contain private key material.

- PKCS12 - A Microsoft private standard that was later defined in an RFC that provides enhanced security versus the plain-text PEM format. This can contain private key material. Its used preferentially by Windows systems, and can be freely converted to PEM format through use of openssl.

- DER - The parent format of PEM. It's useful to think of it as a binary version of the base64-encoded PEM file. Not routinely used very much outside of Windows.

- .csr - This is a Certificate Signing Request. Some applications can generate these for submission to certificate-authorities. The actual format is PKCS10 which is defined in RFC 2986. It includes some/all of the key details of the requested certificate such as subject, organization, state, whatnot, as well as the public key of the certificate to get signed. These get signed by the CA and a certificate is returned. The returned certificate is the public certificate (which includes the public key but not the private key), which itself can be in a couple of formats.

- .pem - Defined in RFCs 1421 through 1424, this is a container format that may include just the public certificate (such as with Apache installs, and CA certificate files /etc/ssl/certs), or may include an entire certificate chain including public key, private key, and root certificates. Confusingly, it may also encode a CSR (e.g. as used here) as the PKCS10 format can be translated into PEM. The name is from Privacy Enhanced Mail (PEM), a failed method for secure email but the container format it used lives on, and is a base64 translation of the x509 ASN.1 keys.

- .key - This is a PEM formatted file containing just the private-key of a specific certificate and is merely a conventional name and not a standardized one. In Apache installs, this frequently resides in /etc/ssl/private. The rights on these files are very important, and some programs will refuse to load these certificates if they are set wrong.

- .pkcs12 .pfx .p12 - Originally defined by RSA in the Public-Key Cryptography Standards (abbreviated PKCS), the "12" variant was originally enhanced by Microsoft, and later submitted as RFC 7292. This is a passworded container format that contains both public and private certificate pairs. Unlike .pem files, this container is fully encrypted. Openssl can turn this into a .pem file with both public and private keys: openssl pkcs12 -in file-to-convert.p12 -out converted-file.pem -nodes

## Chain of trust
Root CA -> ICA ( Intermediate Certificate ) -> Certificate

For practical, visit https site, see cert in browser and open `Keychain access` to see root that signs.

So when requested two or more certificates are returned.
![Raft](screen/TLS.png)


## Public key infrastructure
- The framework to associate a public key with an individual
- Trust on first sight. (SSH)
- Web of trust (Omeno encryption)
- Trust the machine (Lets encrypt)
    - Vendor distributes CA colelction to clients
    - Server distributes cert and intermediates
    - Clients validate the collection


## x.509
An X.509 certificate contains a public key and an identity (a hostname, or an organization, or an individual), and is either signed by a certificate authority or self-signed.

Structure
```
Certificate
Version Number
Serial Number
Signature Algorithm ID
Issuer Name
Validity period
Not Before
Not After
Subject name
Subject Public Key Info
Public Key Algorithm
Subject Public Key
Issuer Unique Identifier (optional)
Subject Unique Identifier (optional)
Extensions (optional)
...
Certificate Signature Algorithm
Certificate Signature (Encrypted hash code)

```
Certificate Standard
CA - Certificate Authority issues and signs
RA - Registration authority 
Full process

```
Public Key + User Identity -> hash -> hash signed by CA -> appended with Public Key + User Identity -> Certificate

```

```bash
openssl x509 -in test.pem -text 
```

## CSR - Certificate Signing Request
In public key infrastructure (PKI) systems, a certificate signing request (also CSR or certification request) is a message sent from an applicant to a certificate authority in order to apply for a digital identity certificate. 

Contents & public key

CN	Common Name
O	Business name / Organization
OU	Department Name / Organizational Unit
L	Town / City
ST	Province, Region, County or State
C	Country
MAIL    Email address


# Adding SSL in Nginx

Adding ssl protection is very easy now. We just need to install certbot and use it.

```
# First install certbot
$ sudo apt-get update
$ sudo apt-get install software-properties-common
$ sudo add-apt-repository ppa:certbot/certbot
$ sudo apt-get update
$ sudo apt-get install python-certbot-nginx

# Next run it
sudo certbot --nginx

certbot will handle the rest.

# Renew Certificate
sudo apt upgrade certbot
sudo certbot renew --dry-run
sudo certbot renew

# Check expiration dates
certbot certificates
```

## Reference
- https://tldp.org/HOWTO/SSL-Certificates-HOWTO/x64.html
- http://www.steves-internet-guide.com/ssl-certificates-explained
- https://serverfault.com/questions/9708/what-is-a-pem-file-and-how-does-it-differ-from-other-openssl-generated-key-file
- https://www.youtube.com/watch?v=qXLD2UHq2vk
- https://www.youtube.com/watch?v=kxKLYDLzuHA&feature=youtu.be
- https://www.youtube.com/watch?v=heacxYUnFHA
- https://www.youtube.com/watch?v=m-Ft2DRz4WA 
- https://en.wikipedia.org/wiki/X.509