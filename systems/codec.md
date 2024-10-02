# Codec

The video format is a container that contains all the required parts to play back specific files.
- Video Stream
- Audio Stream
- Metadata
    - Bitrate
    - Type
    - Resolution
    - Subtitle
    - Device
    - Time of creation
    - Codec
        - OPUS 
        - G.711 
        - H.264 / AVC
        - H.264 / HEVC (50% smaller, 3x computation overhead, better image quality)
        - VP8
        - VP9 (50% smaller, streaming more consistent, container - webm, ivf)
        - AAC (advanced audio coding, best for video)
        - mp3