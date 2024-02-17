# Encoding

## BASE64

- Whenever shipping binary data, convert that to base64. Binary streams chunked in 6 bits (2^6 = 64).

- Why 64? We can generally rely on the same 64 characters being present in many character sets which end up on the other side of the wire uncorrupted.

- Essentially each 6 bits of the input is encoded in a 64-character alphabet. The "standard" alphabet uses A-Z, a-z, 0-9 and + and /, with = as a padding character. There are URL-safe variants.

## Bit parity

- In this method, every byte transmitted would have 7-bits of data, and the 8th would be 1 or 0, to force the total number of 1 bits in the byte to be even.
    - eg. 0x01 to 0x81, 0x02 to 0x82, 0x03 to 0x03 etc.

- For this compatibility, when the ASCII character set was defined, only 00-7F were assigned characters. (Still today, all characters set in the range 80-FF are non-standard). 

- Many routers of the day put the parity check and byte translation into hardware, forcing the computers attached to them to deal strictly with 7-bit data. 

- This force email attachments (and all other data, which is why HTTP & SMTP protocols are text-based), to be convert into a text-only format.

- Two equals sign (==) at the end show that 4 zeroes were added (helps in decoding).

- Base64 encoding uses 33% more storage

- Strings stored in the database wont be human readable.

- Base64 is a method to encode a byte sequence to a string.

## Unicode and UTF-8

- **UTF-8** is a compromise character encoding that can be as compact as ASCII (if the file is just plain English text) but can also contain any unicode characters (with some increase in file size).

- In Unicode, a letter maps to something called a **code point** which is still just a theoretical concept.

-  For example, the Unicode code point for the capital letter “T” is U+0054, the Unicode code point for the lowercase letter “t” is U+0074, and the Unicode point for the lower left triangle “◺” is U+25FA.

- The “problem” with Unicode is that it is most often represented in software as an int32 (32 bit integer). The vast majority of characters in widespread use could fit into a much smaller number than required for a 32 bit data type. This is where UTF-8 enters the picture.

- **UTF-8** is a variable length encoding of Unicode code points. For each Unicode code point, it uses between 1 and 4 bytes. All of the most common characters can be represented using 1–2 bytes (all ASCII characters can be represented in 1 byte). UTF-8 allows us to use all of the characters defined by Unicode, but allows us to save some extra space and only reach for the 3rd or 4th byte when we really need it. To again list the same examples, we could represent the Unicode code point “T” as 84, “t” as and “◺” as 226 151 186.

- UTF-8 and UTF-16 are methods to encode Unicode strings to byte sequences. UTF-16 has advantage if non conventional characters are dominant. UTF-8 otherwise.

**Process**
- Character is encoded in UTF8
- Then encoded character is base64 encoded for wire transfer
- This wire text converted back with base64 decode
- Then we decode `UTF8`
- It does not make sense to have a string without knowing what encoding it uses.
- Not every byte sequence represents an Unicode string encoded in UTF-8 or UTF-16.
- Not every Unicode string represents a byte sequence encoded in Base64.

## References
- [What is base 64 encoding used for?](https://stackoverflow.com/questions/201479/what-is-base-64-encoding-used-for)
- [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets (No Excuses!)](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses)
- [Unicode list](https://home.unicode.org)
- [mikeash.com](https://mikeash.com/pyblog/?tag=letsbuild)