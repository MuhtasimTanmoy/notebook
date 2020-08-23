
# Diffie Hellman

Web protocols use a combination of symmetric and asymmetric encryption to establish secure connections. 
Here the symmetric portion is for forward secrecy. And asymmetric for authentication.
Example: TLS.

- Diffie Hellman Key Exchange
	- Prime Modulus and Generator `( G % P )`. Available to all.
	- A generates random and send  `G ^ R_A % P` . SEND_IT_TO_ALL. Available to all.
	- B generates random and send `G ^ R_B % P` . 
	SEND_IT_TO_ALL. Available to all.
	- Now as `G ^ R_A ^ R_B % P` is calculated and the secret key.
	- Others do not have R_A R_B.

- *Drawback*
    - In case of multiple people communication . OVERHEAD.
    - Extra communication. Round trip time.

# RSA

Public Private key based Encryption.

**Formula**

`(m^(ed) == m ) mod  N `

`ed == 1 (mod phi( N ))`

Prime Factorization
- Given any number get the two primes which multiplies it. 
- ed = very big prime factorization

*Eulers Totient Function*

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

**Eulers theorem**

m ^ phi(n) congruent to =  1 mod n

m ^ (k * phi(n)  +1)  ==  m mod n

**Walkthrough**

	- Generate two prime number.           [ 3 and 11 ]
	- Multiply > prime factorization       [ N = 33 ]
	- phi(N) > toteint                     [ phi(N) = 20 ]
	- Choose exponent between 1 - phi(N) 
        - E = odd and Co prime             [ E coprime to phi(N) and N]
	- N & E public key                     [ (E,N) ]
	- D = ( 2 * phi (N) + 1 ) / E          [ (D,N) ]
	- ( data ^ e ) % N = encrypted text    
	- ( encrypted text ^ d ) % N  = data

# Resources
- [RSA Encryption](https://www.khanacademy.org/computing/computer-science/cryptography/modern-crypt/v/rsa-encryption-part-4)
- [padding](https://asecuritysite.com/encryption/padding)