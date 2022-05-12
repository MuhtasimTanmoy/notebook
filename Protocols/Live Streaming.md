# HLS

- HLS stands for HTTP live streaming and it is the application layer protocol.

- Media streaming protocol used for delivering audio and visual media over the internet.

- For HTTP-based protocols, the media server breaks the content into small file segments (also called chunks). Each of these segments contains a short interval of the content, normally ranging between 2 to 10 seconds. These chunks are packed within a manifest file which contains the metadata mapping the particular time interval to a specific file segment.

- There are many different types of encryption algorithms but HLS only supports AES-128. The Advanced Encryption Standard (AES) is an example of a block cipher, which encrypts (and decrypts) data in fixed-size blocks. It’s a symmetric key algorithm, which means that the key that is used to encrypt data is also used to decrypt it. AES-128 uses a key length of 128 bits (16 bytes).

- HLS uses AES in cipher block chaining (CBC) mode. This means each block is encrypted using the cipher text of the preceding block, but this gives us a problem: how do we encrypt the first block? There is no block before it! To get around this problem we use what is known as an initialisation vector (IV). In this instance, it’s a 16-byte random value that is used to intialize the encryption process. It doesn’t need to be kept secret for the encryption to be secure.

# RTMP
RTMP stands for real time media protocol and it’s the transport layer protocol. There’s one variance of the RTMP - RTMPT, that is the application level protocol, which runs over HTTP(s).

# MPEG Dash
Similar to HLS

# RTP
- Webrtc built on top of

# Resources
- [Http Live Streaming](https://tools.ietf.org/html/rfc8216)
- [Benchmark: SFU, MCU, Mesh](https://testrtc.com/different-multiparty-video-conferencing/)
- [HLS Encryption](https://hlsbook.net/how-to-encrypt-hls-video-with-ffmpeg/)
- [RTP, SDP, RTCP, RTSP, SRTP](https://www.kurento.org/blog/rtp-i-intro-rtp-and-sdp)
- [RTP Streaming](https://www.kurento.org/blog/rtp-ii-streaming-ffmpeg)
