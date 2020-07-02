# Encoding
- When you have some binary data that you want to ship across a network, you generally don't do it by just streaming the bits and bytes over the wire in a raw format. Why? because some media are made for streaming text. You never know - some protocols may interpret your binary data as control characters (like a modem), or your binary data could be screwed up because the underlying protocol might think that you've entered a special character combination (like how FTP translates line endings).
So to get around this, people encode the binary data into characters. Base64 is one of these types of encodings.

Why 64?

Because you can generally rely on the same 64 characters being present in many character sets, and you can be reasonably confident that your data's going to end up on the other side of the wire uncorrupted.

- In the early days of computers, when telephone line inter-system communication was not particularly reliable, a quick & dirty method of verifying data integrity was used: "bit parity". In this method, every byte transmitted would have 7-bits of data, and the 8th would be 1 or 0, to force the total number of 1 bits in the byte to be even.
    - Hence 0x01 would be transmited as 0x81; 0x02 would be 0x82; 0x03 would remain 0x03 etc.
- To further this system, when the ASCII character set was defined, only 00-7F were assigned characters. (Still today, all characters set in the range 80-FF are non-standard)
Many routers of the day put the parity check and byte translation into hardware, forcing the computers attached to them to deal strictly with 7-bit data. This force email attachments (and all other data, which is why HTTP & SMTP protocols are text-based), to be convert into a text-only format.
- Two equals sign at the end show that 4 zeroes were added (helps in decoding).
- Base64 encoding uses 33% more storage
- Strings stored in the database wont be human readable
- Essentially each 6 bits of the input is encoded in a 64-character alphabet. The "standard" alphabet uses A-Z, a-z, 0-9 and + and /, with = as a padding character. There are URL-safe variants.
- UTF-8 is a compromise character encoding that can be as compact as ASCII (if the file is just plain English text) but can also contain any unicode characters (with some increase in file size).
- In Unicode, a letter maps to something called a code point which is still just a theoretical concept. Platonic letter
- Every platonic letter in every alphabet is assigned a magic number by the Unicode consortium which is written like this: U+0639.  This magic number is called a code point
- Unicode Byte Order Mark
- To avoid all zeros - UTF 8
- It does not make sense to have a string without knowing what encoding it uses
- UTF-8 or ASCII or ISO 8859-1 (Latin 1) or Windows 1252


## Reference
- https://stackoverflow.com/questions/201479/what-is-base-64-encoding-used-for
- https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses
- https://home.unicode.org
- https://mikeash.com/pyblog/?tag=letsbuild