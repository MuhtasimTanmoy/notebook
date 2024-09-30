# Swift

- Interface
    - Method signature
    - Property declaration
- Trait
    - Method bodies
    - Property declaration
    - A trait also has the actual method bodies. In other words, a trait adds code to an interface. Used by a protocol extension.
- Mixin
    - Method bodies
    - Stored properties
    - A mixin is like a trait but it also has a state. Not available in the protocol.
    - Property declaration to a protocol, but then every class or struct that conforms to this protocol still needs to provide its storage for those properties.
- dsym
    - A dSYM file is a "debug symbols file". 
    - When this setting is enabled, symbol names of your objects are removed from the resulting compiled binary.
 
- In Swift, there are three kinds of statements: simple statements, compiler control statements, and control flow statements.

- When compiled, the compiler uses a function to pointer location in an array.
    - Direct / Static Dispatch
        - `Value type` (Initial + Extension) data structures have this.
        - Class Extension, Protocol Extension will have static dispatch
        - Final keyword
        - This restricts subclassing, therefore faster.
    - Table Dispatch
        - Class, Protocol Init will have static dispatch
        - For class type compiler maintains an array of witness pointers
        - Whenever subclass it copies the table and appends new function, replacing override function
    - Message Dispatch
        - Dynamic keyword
        - No offset, The entire table is traversed to get the function. The later ones get executed.
        - `Test` add, `measure` to see the time difference.

- Debugging
    - p can change value
    - p, po compute value, v from stackframe
    - Network link conditioner to simulate packet loss

- Opaque pointer opposite to generics
- Opaque type solves the problem introduced by `associated type` 
- Extension, Opaque pointer has a difference
- Download task differs when we use it to download different types
- Dependency injection through param, protocols

- Generics
- Associated Type
- Opaque Type
    - Where the caller function is not aware of the type, the function implementation is.
    - Used while not disclosing the type of information
    - When using associated type as protocol and protocol type as the return type, use the `some ` keyword which returns `opaque type`

- Actor
    - Manages concurrency related issue

- Class has convenience initializer where struct can simulate that through extension

- Struct can have inheritance by using `protocol + extension + default`

- Struct can have data race if not captured. [Ref](https://stackoverflow.com/questions/41350772/if-arrays-are-value-types-and-therefore-get-copied-then-how-are-they-not-thread)

- [Swift Memory Layout](https://theswiftdev.com/memory-layout-in-swift)
    - Process data bytes, consider as a pointer, use `memory` style `mach_vm_read_overwrite` variant.
    - Variables inside the struct are positioned in offset that is divisible by its size
    - Explains memory layout for struct, class, enum, array, protocol

- [Queue Usage](https://stackoverflow.com/questions/28784507/adding-items-to-swift-array-across-multiple-threads-causing-issues-because-arra/28784770#28784770)
    - Concurrent queues are queues to which you can submit multiple tasks and they are allowed to run parallel. But sometimes you want to submit something to that queue that needs to lock everything else in the queue because it needs to run alone, so stuff you submit with a barrier basically waits for everything in the queue to be completed and then it locks everyone else and executes. In the end, release everyone else again.
    - Reads can enjoy concurrency (no barrier), but calling thread must wait (sync), but writes can not be concurrent (thus, the barrier), but calling thread doesn’t have to wait (hence async).
    - One technically can use semaphores, but it’s the last tool we would reach for. NSLock is simple and performant. Unfair locks can be useful where performance is critical, but it’s a little cumbersome and it's overkill in most situations.
    - Reads can only happen concurrently concerning other reads. But they cannot be performed concurrently with writes. So concurrent queue allows the reads to happen concurrently, except for writes, which is why we use a barrier for writes.

- KeyPath to simplify object property
- SwiftUI
    - Binding is by definition a two-way connection, `.constant()` means a one-way connection, when the user types into the text field the variable in the view model will never get updated. Your updates can go down but not up.
    - `StateObject` is for initializing `ObservedObject` is for passing around.

### References
- [Traits and Mixin](http://machinethink.net/blog/mixins-and-traits-in-swift-2.0)
- [Swift Memory Model](https://youtu.be/ERYNyrfXjlg)
    - Word is a unit in the size of a pointer
- [Swift Plugin Manager Thread](https://forums.swift.org/t/weak-linking-in-swift-package-manager-plugin-architecture/49821)