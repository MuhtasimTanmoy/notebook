# Audio Programming

Digital audio need to converted to digital. That means we need to sample from infinite analog wave to a finite sampte rate.

### Nyquist Shannon Smapling Theorem

Any `band limited` continuous time signal can be accurately converted to and from digital signals when sampled at a rate, at least as `twice` as high as the highest frequency component of the waveform.

- Must go througn low pass filter for bandlimiting

- Cycles per second, frequency and Sample per second, Sample rate both have `Hz` as unit.

### Dithering
- Dithering is the process of ntentionally adding noise to a signal, during the process of quantization, o preserve low level information and prevent correlated distortion.

### References
- [Audio Theory](https://youtube.com/playlist?list=PLbqhA-NKGP6B6V_AiS-jbvSzdd7nbwwCw)

- [CppCon 2015: Timur Doumler “C++ in the Audio Industry”](https://www.youtube.com/watch?v=boPEO2auJj4)
    - Audio is processed in buffer of relevant size which are just array of floats.
    - Audio processing should never cause dropout.
    - Dont write any code that is asyncronous, dont know how long will take. No busy waiting. DO lock free prgramming.
    - Priority Inversion. Waitng for low priority thread.
    - Cant call `new` and `delete`. Internally waits for lock.
    - Dont call `RAII` objects that use object allocation internally like `shared_ptr`.
    - No `vector::push_back` either.
    - Should be done
        - Put your data on the stack.
        - Preallocate your data.
        - Use custom real-time safe containers (lock-free queues, stacks).
        - For larger systems: manage your own preallocated.
        - No io functions, no IPC, no file access. 
        - 0(1) is fine, amortised o(1) is not.
            - `ordered_set::insert()` may rehash.