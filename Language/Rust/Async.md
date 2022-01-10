# Async

- [I/O Multiplexing](https://www.softprayog.in/programming/io-multiplexing-select-poll-epoll-in-linux)
    - When waiting for data on a `socket`, can check non-blocking with timeout, but has serious overhead. Suppose waiting on 500 `sockets` and data available on one just after timeout need to traverse 499 more to read that.
    - Maintaining thread per socket,  does not scale
        - Select: Takes 3 sets of file descriptors we want to monitor for file descriptors
            - Read event
            - Write event
            - Exception event
        - Poll
            - Instead of all file descriptors only the relevant event related are traversed
        - Epoll
            - Mush less user space to kernel space data movement


- [The What and How of Futures and async/await in Rust](https://www.youtube.com/watch?v=9_3krAQtD2k)