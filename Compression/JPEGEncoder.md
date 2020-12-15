# JPEG Image Compression
- Joint Photographic Expert Group

The major steps in JPEG compression involve.
• Colour space transform and subsampling.
• DCT (Discrete Cosine Transform).
• Quantisation.
• Zigzag scan.
• DPCM on DC component.
• RLE on AC Components.
• Entropy coding — Human or arithmetic.



- Colour space transform and subsampling
    - CMY for printer
    - YCbCr
        - Y -  Luminosity component (0-255)
        - Cb - Chrominance blue (-127 - 128)
        - Cr - Chrominance red (-127 - 128)
    - TCbCr used for downsampling of colour components 


DCT
- 8 * 8 bits
- Center around -127 - 128
- DCT * DCT CoEff = Centered 8 * 8 bits
- Quantization table(50% or compression determined) to divide the DCT CoEff table to zero
- Zigzag serialization
- Huffman table

- DCT3 = Inverse DCT 








- Image
    - Stored at 1 bit per pixel (Black and White), 8 Bits per pixel (Grey Scale, Colour Map) or 24 Bits per pixel (True ßColour)
- Audio
    - Audio signals are continuous analog signals.
    - CD Quality Audio requires 16-bit sampling at 44.1 KHz Even higher audiophile rates 
- Video
    - Raw video can be regarded as being a series of single images. There are typically 25, 30 or 50 frames per second.






# Resources
- [Image Processing](https://users.cs.cf.ac.uk/Dave.Marshall/Multimedia/)
- [Discreet cosine transform](https://www.youtube.com/watch?v=Q2aEzeMDHMA)