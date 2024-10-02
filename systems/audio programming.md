# Audio Programming

Digital audio needs to be converted to digital. That means we need to sample from an infinite analog wave to a finite sample rate.

### Nyquist Shannon Sampling Theorem

Any `band limited` continuous-time signal can be accurately converted to and from digital signals when sampled at a rate, at least `twice` as high as the highest frequency component of the waveform.

- Must go through a low pass filter for band-limiting

- Cycles per second, frequency and Sample per second, and Sample rate both have `Hz` as a unit.

### Dithering
- Dithering is the process of intentionally adding noise to a signal, during the process of quantization, to preserve low-level information and prevent correlated distortion.

### References
- [Audio Theory](https://youtube.com/playlist?list=PLbqhA-NKGP6B6V_AiS-jbvSzdd7nbwwCw)

- [CppCon 2015: Timur Doumler “C++ in the Audio Industry”](https://www.youtube.com/watch?v=boPEO2auJj4)
    - Audio is processed in the buffer of relevant size which is just an array of floats.
    - Audio processing should never cause dropout.
    - Don't write any code that is asynchronous, don't know how long will take. No busy waiting. DO lock-free programming.
    - Priority Inversion. Waiting for the low-priority thread.
    - Can't call `new` and `delete`. Internally waits for a lock.
    - Don't call `RAII` objects that use object allocation internally like `shared_ptr`.
    - No `vector::push_back` either.
    - Should be done
        - Put your data on the stack.
        - Preallocate your data.
        - Use custom real-time safe containers (lock-free queues, stacks).
        - For larger systems: manage your own preallocated.
        - No io functions, no IPC, no file access. 
        - 0(1) is fine, amortised o(1) is not.
            - `ordered_set::insert()` may rehash.