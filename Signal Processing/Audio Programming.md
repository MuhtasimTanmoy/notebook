# Audio Programming

Digital audio need to converted to digital. That means we need to sample from infinite analog wave to a finite sampte rate.


### Nyquist Shannon Smapling Theorem

Any `band limited` continuous time signal can be accurately converted to and from digital signals when sampled at a rate, at least as `twice` as high as the highest frequency component of the waveform.

- Must go througn low pass filter for bandlimiting

- Cycles per second, frequency and Sample per second, Sample rate both have `Hz` as unit.

### Dithering
- Dithering is the process of ntentionally adding noise to a signal, during the process of quantization, o preserve low level information and prevent correlated distortion.


# Resources
- [Audio Theory](https://youtube.com/playlist?list=PLbqhA-NKGP6B6V_AiS-jbvSzdd7nbwwCw)