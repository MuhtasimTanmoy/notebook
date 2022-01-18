
- Interface
    - Method signature
    - Property declaration
- Trait
    - Method bodies
    - Property declaration
    - A trait also has the actual method bodies. In other words, a trait adds code to an interface. Used by protocol extension.
- Mixin
    - Method bodies
    - Stored properties
    - A mixin is like a trait but it also has state. Not avaialable in protocol.
    - Property declaration to a protocol, but then every class or struct that conforms to this protocol still needs to provide its own storage for those properties.
- dsym
    - A dSYM file is a "debug symbols file". When this setting is enabled, symbol names of your objects are removed from the resulting compiled binary.
 
In Swift, there are three kinds of statements: simple statements, compiler control statements, and control flow statements.


- [Swift Memory Layout](https://theswiftdev.com/memory-layout-in-swift/)
    - Process data bytes, consider as pointer, use `memcopy` style `mach_vm_read_overwrite` variant.
    - Variables inside struct are postioned in offset that divisible by its size
    - Explains memory layout for struct, class, enum, array, protocol

## Resource
- [Traits and Mixin](http://machinethink.net/blog/mixins-and-traits-in-swift-2.0/)


- [Swift Memory Model](https://youtu.be/ERYNyrfXjlg)
    - Word is a unit in the size of a pointer