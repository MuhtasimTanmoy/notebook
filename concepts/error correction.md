# Error Correction

- Repetition Code
    - Turns a `1-bit` message into a `3-bit` codeword.

- Hamming Codes
    - Takes 4 bits and turns it into 7 bits codeword.
    - Parity bit - 1 in 16 to detect change
    - (15, 11) Hamming code
    - Extended hamming code checks for parity bit as well
    - Get only the position of the bits containing 1, xor them, and get error index.

- Reed Solomon Codes
    - Special case of BCH codes

- Turbo Codes

### Erasure Code

### Galois Field
- Equation is solvable by radicals if there is a simple way of finding its root. Like equations.
- The coefficients are rational numbers. Rational numbers form a field, means arithmetic operations generate another rational number.

# Reference
- [Reed Solomon Code](https://www.cs.cmu.edu/~guyb/realworld/reedsolomon/reed_solomon_codes.html)