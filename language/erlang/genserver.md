
# Gen server

- handle_cast
    - expect no reply
- handle_call
    - expect reply

- Instead of spawning process, using `spawn_link` will link process accordingly.
    - Then supervisor can respawn that process.
    - Supervise strategy like `one_for_one`.
    - `sys:trace` to be used for tracing
    - `sys:get_state()` to be used for seeing state
    - `sys:replace_state()` for debugging

## References
- [A Peek Inside Erlang's OTP • Steve Vinoski • GOTO 2016](https://www.youtube.com/watch?v=PkHZPTn1brc)