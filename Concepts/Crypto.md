
### Public key infrastructure
- The framework to associate a public key with an individual
- Trust on first sight
- Web of trust (Omeno encryption)
- Trust the machine (Lets encrypt)
    - Vendor distributes CA colelction to clients
    - Server distributes cert and intermediates
    - Clients validate the collection

### x.509

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

## CSR
In public key infrastructure (PKI) systems, a certificate signing request (also CSR or certification request) is a message sent from an applicant to a certificate authority in order to apply for a digital identity certificate. 

Contents & public key

CN	Common Name
O	Business name / Organization
OU	Department Name / Organizational Unit
L	Town / City
ST	Province, Region, County or State
C	Country
MAIL	Email address

# Resources
- https://www.youtube.com/watch?v=m-Ft2DRz4WA 
- https://en.wikipedia.org/wiki/X.509