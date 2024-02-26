# iOS

- Hardware
    - x86_64-darwin
    - arm64-darwin
    - x86_64-ios (simulator)
    - arm64-ios (physical device)
- Core OS
- Core Services
- Media
- Cocoa Touch > UIKit
- Applications

- Lazy var
    - Swift has a mechanism built right into the language that enables 
    just-in-time calculation of expensive work, and it is called a **_lazy variable_**.
    - A lazy stored property is a property whose initial value is not calculated until the first time it is used. 
    - You indicate a lazy stored property by writing the `lazy` modifier 
    before its declaration.

- Closure
    - Functions are actually a special case of closures: blocks of code that can be called later. 
    - The code in a closure has access to things like variables and functions that were available in the scope where the closure was created, even if the closure is in a different scope when it is executed. 
    - You can write a closure without a name by surrounding code with 
    braces (`{}`). Use `in` to separate the arguments and return type from the body.

- ARC
    - ARC is a compile time feature that is Apple's version of automated memory management. 
    - It stands for `Automatic Reference Counting`. This means that it  **_only_**  frees up memory for objects when there are  **_zero strong_**  references to them.

- Notification Center
    - When communication between two or more components of your app, that have no formal connection, needs to happen
    - When communication needs to happen repeatedly and consistently
    - When using one-to-many or many-to-many communication

- [Reactive](http://reactivex.io/documentation/subject.html)
    - Async
    - Behaviour
    - Publish
    - Reply

- Interaction with c always takes `opaque pointer` in new systems, in older systems worked differently. 

- Concurrency
    - serial queue
        - main thread queue is serial queue
        - using sync in serial queue will cause deadlock
    - parallel queue
    - reference-counting (i.e. xref). 
    - The large negative value for xref and ref, for example, is likely indicating that is an object that cannot be deallocated. 

- Can capture memory leak by enabling option. 

```
# device listing
rvictl -l

# packet capture
rvictl -s INDETIFIER_OF_DEVICE

# remove virtual interface
rvictl -x <UDID>

# Capture packet
tcpdump -n -t -i rvi0 -q -A tcp

```

## References
- [Swift Style Guide](https://google.github.io/swift/#global-constants)
- [iOS Build](https://gist.github.com/adamawolf/3048717) 
- [Concurrency](https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/ThreadMigration/ThreadMigration.html#//apple_ref/doc/uid/TP40008091-CH105-SW1)