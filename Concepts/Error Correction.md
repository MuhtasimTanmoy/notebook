# Error Correction

- Repetation Code
    - Turns 1 bit message to 3 bit codeword.

- Hamming Codes
    - Takes 4 bits and truns it into 7 bits codeword.
    - Parity bit - 1 in 16 to detect change
    - (15, 11) hamming code
    - Extended hamming code checks for parity bit as well
    - Get only the position of the bits containing 1, xor them, get error index.

- Reed Solomon Codes
    - Special case of BCH codes

- Turbo Codes

## Erasure Code

## Galois Field
- Equation is solvable by radicals if there is simple way of finding it's root. Like equations.
- The coefficients are rational number. Rational numbers form a field, means arithmetic operations generate another rational number.

# Reference
- [Reed Solomon Code](https://www.cs.cmu.edu/~guyb/realworld/reedsolomon/reed_solomon_codes.html)