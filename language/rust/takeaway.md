# Takeaway

- Try to never use `unwrap()` in production, if you so require, try using
  `expect()`
  - `unwrap` method, which returns the value of `T` if the result is `Ok(T)`, or panics if the result is `Err(E)`

- In Tokio, a **task** is the equivalent of terms like green thread, fiber,
  coroutine, etc.

- Rust `async fn` always returns an anonymous `impl Future` type.

- Rust async is **lazy** in nature. Unless `.await` is called, a `Future` will
  never be executed.

- Use `type` aliases to clarify and shorten; long types.

- Sharding is a very basic but awesome concept 
  - Allows you to split your data storage into multiple parts (or shards)
  - Reduce contentions for both reads and writes.

- Use `tokio::sync::oneshot` instead of callbacks for passing messages around
  and communicating among different tasks.

- Pair `tokio::sync::mpsc` with **task**s to create manager tasks that manage
  communication with services such as db, api clients, etc.

  ### References
  
  - [5 years of Rust (for me)](https://docs.google.com/document/d/1CnIztKZcUzQgOpJgScFRu3hnjr8bH_Z3EiACvERn3fI/edit)

  - [Slow compile time in RUST](https://www.pingcap.com/blog/rust-compilation-model-calamity)

  - [BRSon Rust Notes](https://github.com/brson/my-rust-lists/blob/master/rust-guru-notes.md)