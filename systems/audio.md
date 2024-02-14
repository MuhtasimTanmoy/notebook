# Audio Signal

Audio signals are normally in time domain. If you read the samples that make the audio from left to right, you travel in time, and the values you read signify how much to push or pull your loudspeaker cone at that point in time.

When you use `FFT`, you transform your time-domain audio signal to frequency domain.

As a result of `FFT`, you should get several bins filled with magnitudes and phases. You can discard the phases for this purpose; you are interested in the magnitudes.

Human ears typically can hear sounds as low as 20Hz to as high as 20000Hz in frequency. In a typical CD quality audio data, you have 44100 samples per second (in time domain, remember) which can encode information from 0Hz to 22050Hz (half the sampling rate basically; if you're interested in why, check out the "nyquist theorem").

The magnitudes in FFT bins gives you the energy of sound between different frequencies. So depending on how you setup your FFT solver, say you end up with 100 bins. First bin gives you the energy between (say) 0 and 50Hz, the second bin gives you the energy between 50Hz and 100Hz and so on. 

You want to plug those magnitudes to the height of lines in your visualisation. The leftmost lines track the lower frequencies, and the rightmost lines track the highest frequencies.

Two main factors determining sound
- Sample Frequency ( X axis )
- Bit Depth ( Y axis )
 
Bit Rate = Bit Depth * Sample Rate * Number of Channels

## Notes
- Uncompressed raw audio format is Linear Pulse Code Modulation(LPCM)
- `mp4` and `aac` are two different concepts. `mp4` is a container format, and aac is an encoding.
- iPhone does not encode mp3
- `AAC` is your format choice if you want interop between Android and iPhone devices
- `PCM` is decodable on iPhone and Android and most cellphones at the expense of larger filesize.
- But you can't create a file and save to the system with `mp3`, on iPhone. You can play back, but not save.
- All smartphones can play WAV files (even Android as of 2.2). These are known as "Linear PCM" in iOS and "PCM/WAVE" in Android.
- `ffprobe -hide_banner -stats -i ios-aac.m4a`
- It does support hardware `AAC/m4a` encoding which is in many ways superior to mp3.

##  Reference
- [How digital audio works](https://www.youtube.com/watch?v=1RIA9U5oXro&ab_channel=Computerphile)
- [Reddit Thread ](https://www.reddit.com/r/iOSProgramming/comments/2le7hq/how_do_i_make_a_spectrum_visualizer_for_my_music/)
- [Basic Audio Workflow](https://www.youtube.com/watch?v=JyUagzvGq7Q&ab_channel=ComputerScience)
- [Reddit Thread ](https://www.reddit.com/r/rust/comments/aua2tb/rust_2019_rust_audio/) - discussion on various rust library
- [iOS Recording Formats](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/MultimediaPG/UsingAudio/UsingAudio.html#//apple_ref/doc/uid/TP40009767-CH2-SW6)
- [Android Recording Format](https://developer.android.com/guide/topics/media/media-formats)
- [FFT library](https://github.com/wendykierp/JTransforms)