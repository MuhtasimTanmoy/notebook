# Async

![](./screen/RustFuture.png)

- System Threads
    - Kernel-level threads
- Green Threads
    - User-level threads

- Async Implementation at a high level has three major components 
    - Executor
    - Reactor
    - XRoutine

- Async
    - Transforms a block of code into a state machine that implements a trait called future

- Await
    - Mechanism to run a future. It asynchronously waits for the future to complete.

- `mio` provides several core abstractions for working with I/O resources, such as sockets, pipes, and devices.

- It also supports advanced features such as `epoll, kqueue, and IOCP` on different platforms and convenient utility functions for working with I/O events, timeouts, and buffers.

### References

- [Rust's Journey to Async/Await](https://www.youtube.com/watch?v=lJ3NC-R3gSI)
    - Explains how Rust got its `asynchronous` paradigm.
    - First adopted `green threads`. But still performed like a one-to-one native thread.
    - Event loop in JavaScript allowed asynchronous callbacks with eventing.
    - Go, Ruby has blocking syntax with non-blocking runtime.
    - Go has stackfull co routines compared to Rust stackfull coroutine. 

- [Rundown of Async/Await in Rust](https://www.youtube.com/watch?v=IE91l4kR0wo)
    - Code walkthrough of demo future implementation.

- [Rust Zero Cost Future:](https://www.youtube.com/watch?v=skos4B5x7qE) 
    - Explains future implementation and benchmark.

- [The Talk You've Been Await-ing for](https://www.youtube.com/watch?v=NNwK5ZPAJCk&t=306s)
    -  Implementaton of executor, Reactor

- [Java Async Dependency Management](https://gist.github.com/benjchristensen/4677544)
- [Under the hood of Futures and Promises in Swift](https://swiftbysundell.com/articles/under-the-hood-of-futures-and-promises-in-swift)
- [Tree-Structured Concurrency](https://blog.yoshuawuyts.com/tree-structured-concurrency)
- [Why Async Rust](https://blog.yoshuawuyts.com/why-async-rust)
