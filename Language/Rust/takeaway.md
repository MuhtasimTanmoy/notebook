# Takeaway

- Try to never use `unwrap()` in production, if you so require, try using
  `expect()`.
- In Tokio, a **task** is the equivalent of terms like green thread, fiber,
  coroutine, etc.
- Rust `async fn` always returns an anonymous `impl Future` type.
- Rust async is **lazy** in nature. Unless `.await` is called, a `Future` will
  never be executed.
- Use `type` aliases to clarify and shorten; long types.
- Sharding is a very basic but awesome concept - allows you to split your data
  storage into multiple parts (or shards) to reduce contentions for both reads
  and writes. 
- Use `tokio::sync::oneshot` instead of callbacks for passing messages around
  and communicating among different tasks.
- Pair `tokio::sync::mpsc` with **task**s to create manager tasks that manage
  communication with services such as db, api clients, etc.