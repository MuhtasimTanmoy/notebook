# Video Streaming

## HLS
- HTTP Live Streaming
- mpegts 
    - mpeg Transport Stream

## Compression
- Spatial Compression (IntraFrame) 
    - JPEG
- Temporal Compression (Interframe) 
    - MPEG
    - iframe the image
    - pframe the block move instruction
    - bframe prediction
- Bitrate is the amount of bits per second 
    - bitrate = file size / duration  

## FFMPEG

- Transcoding. Process off decoding of one codec and re-encoding to another.
- Converting file format. Changing metadata of container.
- Reducing volume, input channel fix, cropping video
- Dependencies
    - aom, dav1d, frei0r, libffi, guile, nettle, lame, python@3.9, libass, libbluray, libsoxr, libvidstab, libogg, libvorbis, libvpx, opencore-amr, little-cms2, openjpeg, opus, rav1e, rtmpdump, flac, libsndfile, libsamplerate, rubberband, sdl2, speex, srt, giflib, leptonica, tesseract, theora, x264, x265, xvid, libsodium, zeromq and zimg

```bash

# See metadata of mp4. Changing the file name does not change the underlying container.
ffmpeg -i test.mp4

# Changing just the container
ffmpeg -i test.mov -c:v copy -c:a copy test.mp4

# Stripping audio srtream
ffmpeg -i test.mov -map 0:0 -c:v copy tmp.mov

# Codecs supported
ffmpeg -hide_banner -codecs | less

# Conversion
ffmpeg -i test.avi test.mp4 -c:v vp8 -c:a opus

# Quality change
ffmpeg -i test.mp4 -q 20 test_20.mp4

# consant rate factor
ffmpeg -i test.avi -crf 20 test_20.avi

# bitrate change
ffmpeg -i test.avi -b:v 100k -b:a 10k test.mp4

# Fast encoding
ffmpeg -i input -c:v libx264 -preset ultrafast -crf 0 output.mkv

# Best compression
ffmpeg -i input -c:v libx264 -preset veryslow -crf 0 output.mkv

# List audio video source
ffmpeg -f avfoundation -list_devices true -i ""

# Streamign RTMP packet
ffmpeg \
    -f avfoundation \
    -r 30 \
    -i "0:0" \
    -deinterlace \
    -vcodec libx264 \
    -pix_fmt yuv420p \
    -preset medium \
    -g 60 -b:v 2500k \
    -acodec libmp3lame \
    -ar 44100 \
    -threads 6 \
    -qscale 3 -b:a 712000 \
    -bufsize 512k \
    -f flv rtmp://localhost/live/abc123

ffmpeg \
  -f avfoundation \
  -video_size 640x480 \
  -framerate 30 \
  -i "0:0" -ac 2 \
  -vcodec libx264 -maxrate 2000k \
  -bufsize 2000k -acodec libmp3lame -ar 44100 -b:a 128k \
  -f flv "rtmp://localhost/live/abc123"

# working
ffmpeg -f avfoundation -i ":1" -acodec libmp3lame -ab 32k -ac 1 -f flv "rtmp://localhost/live/abc123"

ffmpeg -f avfoundation -r 30 -i "0" -vcodec libx264 -preset veryfast -b:v 1984k -maxrate 1984k -bufsize 3968k -vf "format=yuv420p" -g 60 -c:a aac -b:a 128k -ar 44100 -f flv "rtmp://localhost/live/abc123"

# r frame/second

# vcodec / c:v
# b:v bits/second
# acodec / c:a
# b:a bits/second
# ar sampling frequency

# GOP size is 300 which means one intra frame every 10 seconds for 29.97fps input video

# List available AVFoundation input devices:
ffmpeg -f avfoundation -list_devices true -i ""

# Record video at 30 fps from device 0:
ffmpeg -r 30 -f avfoundation -i 0 out.mp4

# Record from video device 0 and audio device 0:
ffmpeg -r 30 -f avfoundation -i 0:1 out.mp4

# Making the video slower
ffmpeg -r 1 -i test.mp4 -r 2 output.mp4

# Extracting frame from video
ffmpeg -i video.mp4 image-%05d.png
ffmpeg -ss 00:00:25 -t 00:00:00.04 -i YOURMOVIE.MP4 -r 25.0 YOURIMAGE%4d.jpg
```

## Resources
- [FFMEPG, Preset](https://trac.ffmpeg.org/wiki/Encode/H.264)
- [Rate control](https://slhck.info/video/2017/03/01/rate-control.html)
- [FFMPEG](https://ffmpeg.org/ffmpeg.html)         