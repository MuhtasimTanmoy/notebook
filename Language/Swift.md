
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
    - A dSYM file is a "debug symbols file". 
    - When this setting is enabled, symbol names of your objects are removed from the resulting compiled binary.
 
In Swift, there are three kinds of statements: simple statements, compiler control statements, and control flow statements.

-  When compiled, compiler uses function to pointer location in an array.
    - Direct / Static Dispatch
        - `Value type` (Initial + Extension) data structures have this.
        - Class Extension, Protocol Extension will have static dispatch
        - Final keyword
        - This restricts subclassing, therefore faster.
    - Table Dispatch
        - Class, Protocol Init will have static dispatch
        - For class type compilere maintains an array of witness pointers
        - Whenever subclass it copies the table and append new function, replace overriden function
    - Message Dispatch
        - Dynamic keyword
        - No offset, The entire table is travered to get the function. The later ones get executed.
        - `Test` add, `measure` for see time difference.

- Debugging
    - p can change value
    - p, po compute value, v from stackframe
    - Network link conditioner to simulate packet loss

- Opaque pointer opposite to generics
- Extension, Opaque pointer has difference
- Download task differs when we use it to download different types

- Dependency injection through param, protocols

- Generics
- Associated Type
- Opaque Type
    - Where caller function not aware of the type, function implementation is.
    - Used while not disclosed the type information
    - When used associated type as protocol and use protocol type as return type, use `some ` keyword which returns `opaque type`

- Actor
    - Manages concurrenncy related issue
- Class has convenience initializer where struct cann simulate that through extension.
- Struct can have inheritence by using `protocol + extension + default`.

- [Swift Memory Layout](https://theswiftdev.com/memory-layout-in-swift)
    - Process data bytes, consider as pointer, use `memcopy` style `mach_vm_read_overwrite` variant.
    - Variables inside struct are postioned in offset that divisible by its size
    - Explains memory layout for struct, class, enum, array, protocol

## Resource
- [Traits and Mixin](http://machinethink.net/blog/mixins-and-traits-in-swift-2.0)
- [Swift Memory Model](https://youtu.be/ERYNyrfXjlg)
    - Word is a unit in the size of a pointer