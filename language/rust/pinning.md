# Pinning

- [The Why, What, and How of Pinning in Rust](https://youtu.be/DkMwYxfSYNQ)
    - auto traits are `send`, `sync`, `unpin`
    - Pin will put constraint on the item to not be `movable`
    - future highly uses it

- [@withoutboats on Pin](https://youtu.be/shtfSMTwKRw)
    - Self referenctial `struct` handle
    - Once you start polling a future you cant move it again
    - As all `future` on await makes a `state machine`