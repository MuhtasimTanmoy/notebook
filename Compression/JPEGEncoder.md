# JPEG Image Compression
- Joint Photographic Expert Group

The major steps in JPEG compression involves
1. Compressing at block level (8*8).
2. Colour space transform and subsampling. (RGB->YCbCr)
3. DCT (Discrete Cosine Transform).
4. Quantisation.
5. Zigzag scan.
6. DPCM on DC component.
7. RLE(Run Length Encoding) on AC Components.
8. Entropy coding — Huffman or arithmetic.

## 2. Conversion 
- Colour space transform and subsampling
    - CMY for printer
    - YCbCr
        - Y 
            - Luminosity Component ( 0-255)
        - Cb 
            - Chrominance Blue ( -127 - 128)
        - Cr 
            - Chrominance Red ( -127 - 128)
    - YCbCr used for downsampling of colour components


```
Y = a*R + b*G + c*B

Cb = d*R + e*G + f*B

Cr = g*R + h*G + i*B
```

## 3. DCT
- 8 * 8 bits
- Center around -127 - 128
- DCT * DCT CoEff = Centered 8 * 8 bits
- Quantization table(50% or compression determined) to divide the DCT CoEff table to zero
- Zigzag serialization
- Huffman table
- DCT3 = Inverse DCT
- Image
    - Stored at 1 bit per pixel (Black and White)
    - 8 Bits per pixel (Grey Scale, Colour Map) or 24 Bits per pixel (True ßColour)
- Audio
    - Audio signals are continuous analog signals.
    - CD Quality Audio requires 16-bit sampling at 44.1 KHz Even higher audiophile rates
- Video
    - Raw video can be regarded as being a series of single images. 
    - There are typically 25, 30 or 50 frames per second

## Huffman Coding
- Number of Zero preceeding, Symbol, Value
- Marker
    - Two Byte values (FFXX )
    - Determines what is coming next
    - Marker for
        - Quantization Table
        - Huffman Table
        - Huffman coded bitstream
        - Start of Image Marker 
            - FFD8 / SOI
            - FFEN / APPN (Application Specific)
                - APP0 JFIF
                - Followed by the value of Data Byte to read (2 Bytes)
            - FFDB / DQT
                - Followed by length (2 Byte)
                - Table Info (1 Byte)
                    - First 4 bits - Quantization table 8 bits/ 16 bits
                    - Table type - Luminance Table / Chrominance Table
                - Table Values (64 Bytes / 128 Bytes)
                - The chrominance channel is quantized more heavily then luminance channel.
            - FFCX - Start of frame
                - 13 markers
                - FFC0 - Baseline DCT
                - FFC2 - Progressive DCT
                    - Length (2 Byte)
                    - Precision (1 Byte) Value 8
                    - Height (2 Byte)
                    - Width (2 Byte)
                    - Channels, Number of Componenets
                        - 1 - Grayscale
                        - 3 - YCbCr
                        - 4 - CmYk
                        - Loop N times
                            - Component ID
                            - Sampling Factor
                            - Quantization Table
            - DRI - Define Restart Interval (FFDD) 
                - Length (2 Byte) 0004
                - Relative value that is added to DC coefficient
                - 0 - Ac Coefficient in MCU
                - 1-63 - Dc Coefficient in MCU
            - Huffman Table (FFC4)
                - Length (2 Byte)    
                - Table Info
                    -  AC/DC | Table ID 
                - [16 bytes] - Number of codes of each length
                - [X] - Symbols themselves    
                - Codes are what we actually encounter in huffman coded bitstream, we callculate those codes. Codes will be of variable length.
                - Symbol will be 8 bits, descriptor of codes.
                - Huffman Symbols
                    - 1 Byte 
                        - 4 bits - how many zero preceeding
                        - 4 bits - length of co-efficient. eg. 5 -> 3
                    - 160 possible symbols
                    - 2 special Symbol
                        - F0 - Skip 16 zeros
                        - 00 - Rest is zero
                - DC Huffman Table
                    - 12 symbols
            - Start of scan - SOS (FFDA)
                - Length
                - Number of color channels/ Components
                    - Baseline JPEG 
                        - equal to total number of color components
                    - Progressive
                        - May define one color channel  
                    - Component ID
                    - Huffman Table ID
                        - Upper nibble - DC Huffman table ID
                        - Lower Nibble - AC Huffman Table ID       
                - Start of selection - 0 (Same for baseline jpeg)
                - End of selection - 63 (Same for baseline jpeg)
                - Succesive appoximation (For base line both nibble 0)
                                
```c++

// Nondifferential Huffman-coding frame
const bytebits SOF0 = (bytebits)0xc0; // baseline dct
const bytebits SOF1 = (bytebits)0xc1; // extended dct
const bytebits SOF2 = (bytebits)0xc2; // progressive dct
const bytebits SOF3 = (bytebits)0xc3; //  Lossless (Sequential)

// Differential Huffman-coding frame
const bytebits SOF5 = (bytebits)0xc5; // Sequential DCT
const bytebits SOF6 = (bytebits)0xc6; // Progressive DCT
const bytebits SOF7 = (bytebits)0xc7; // lossless

// Nondifferential Arithmetic-coding frame
const bytebits SOF9 = (bytebits)0xc9;  // extended dct
const bytebits SOF10 = (bytebits)0xca; // progressive dct
const bytebits SOF11 = (bytebits)0xcb; // lossless

// Differential Arithmetic-coding frame
const bytebits SOF13 = (bytebits)0xcd; // sequential dct
const bytebits SOF14 = (bytebits)0xce; // progressive dct
const bytebits SOF15 = (bytebits)0xcf; // lossless


/// Huffman Table
const bytebits DHT = (bytebits)0xc4;

/// Quantization Table
const bytebits DQT = (bytebits)0xdb;

/// Start of Scan
const bytebits SOS = (bytebits)0xda;

/// Define Restart Interval
const bytebits DRI = (bytebits)0xdd;

/// Comment
const bytebits COM = (bytebits)0xfe;

/// Start of Image
const bytebits SOI = (bytebits)0xd8;

/// End of Image
const bytebits EOI = (bytebits)0xd9;

/// Define Number of Lines
const bytebits DNL = (bytebits)0xdc;

// JFIF identifiers
const bytebits JFIF_J = (bytebits)0x4a;
const bytebits JFIF_F = (bytebits)0x46;
const bytebits JFIF_I = (bytebits)0x49;
const bytebits JFIF_X = (bytebits)0x46;

// Application Reserved Keywords
const bytebits APP0 = (bytebits)0xe0;
const bytebits APP1 = (bytebits)0xe1;
const bytebits APP2 = (bytebits)0xe2;
const bytebits APP3 = (bytebits)0xe3;
const bytebits APP4 = (bytebits)0xe4;
const bytebits APP5 = (bytebits)0xe5;
const bytebits APP6 = (bytebits)0xe6;
const bytebits APP7 = (bytebits)0xe7;
const bytebits APP8 = (bytebits)0xe8;
const bytebits APP9 = (bytebits)0xe9;
const bytebits APP10 = (bytebits)0xea;
const bytebits APP11 = (bytebits)0xeb;
const bytebits APP12 = (bytebits)0xec;
const bytebits APP13 = (bytebits)0xed;
const bytebits APP14 = (bytebits)0xee;
const bytebits APP15 = (bytebits)0xef;

const bytebits RST0 = (bytebits)0xd0;
const bytebits RST1 = (bytebits)0xd1;
const bytebits RST2 = (bytebits)0xd2;
const bytebits RST3 = (bytebits)0xd3;
const bytebits RST4 = (bytebits)0xd4;
const bytebits RST5 = (bytebits)0xd5;
const bytebits RST6 = (bytebits)0xd6;
const bytebits RST7 = (bytebits)0xd7;

```
# Resources
- [Image Processing](https://users.cs.cf.ac.uk/Dave.Marshall/Multimedia/)
- [Discreet cosine transform](https://www.youtube.com/watch?v=Q2aEzeMDHMA)
- [JPEG Compression](https://www.youtube.com/watch?v=p_YYAb0Fkuw)
- [JPEG Playlist](https://www.youtube.com/watch?v=CPT4FSkFUgs)
- [Specification](https://www.w3.org/Graphics/JPEG/itu-t81.pdf)