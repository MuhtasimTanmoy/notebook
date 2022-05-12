# Compression

- Lossy 
    - Huffman
    - Run length
    - Lempel Ziv
    - eg. Text & Program

- Lossless
    - JPEG
    - MPEG
    - MP3
    - Images, Videos, Audio

- Run Length Compression
    - AAAABBCCC 
        - -> 3A2B3C
    - 0000011111000111 
        - -> 0:4, 1:5, 0:3, 1:3 
        - -> 00100 00101 00011 00011
    - Good for bit stream with continuous value 

- Huffman (Entropy) Coding
    - Entropy means the minimum number of bits needed per symbol on average
    - Count all occurences of symbol
    - Take smallest pair and work until one left
    -  Prefex free
        - Unary Code
        - Gamma code
        - Delta code
            - Difference with prev value 
            - When coded 0 entropy
        - Omega code

- Lempel Ziv Coding
    - Dictionary based encoding
    - Two steps:
        - Building index dictionary
        - Compressing words with index
    - LZW - PKZIP
    - LZSS - Winrar
    - Deflate - GZIP, WinZip
    - LZMA - 7ZIP

- Perceptual Transform Coders for audio/images/video
    - Fourier
    - DCT
    - Vector Quantization

- Image and Video compression applications and algorithms:
    - JPEG
    - H.263
    - MPEG Video
    - MPEG Audio

- Entropy Coding
    - Sum of log(2)p

The main difference between LZ77 and LZSS is that in LZ77 the dictionary reference could actually be longer than the string it was replacing.

LZSS is primarily used across.

Represent the symbols using the minimum number of bits.

zlib, LZO, LZF, FastLZ, and QuickLZ.

# Snappy
- Ported to many language

# MPEG Video Compression
# MPEG Audio Compression

