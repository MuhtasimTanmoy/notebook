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
    - AAAABBCCC -> 3A2B3C
    - 0000011111000111 -> 0:4, 1:5, 0:3, 1:3 -> 00100 00101 00011 00011
    - Good for bit stream    

- Huffman coding
    - Count all occurences of symbol.
    - Take smallest pair and work until one left.

- Lempel Ziv coding
    - Dictionary based encoding
    - Two steps:
        - Building index dictionary
        - Compressing words with index    

- Perceptual transform coders for audio/images/video
    - (Fourier, DCT, Vector Quantization)
- Image and video compression applications and algorithms:
    - JPEG, H.263, MPEG Video, MPEG Audio

- Entropy Coding
    - Summation of log(2)p


The main difference between LZ77 and LZSS is that in LZ77 the dictionary reference could actually be longer than the string it was replacing

LZSS is primarily used across

Represent the symbols using the minimum number of bits

zlib, LZO, LZF, FastLZ, and QuickLZ

# Snappy
- Ported to many language


# MPEG Video Compression
- 

# MPEG Audio Compression
- 



