# Rust

- Rust is a `systems programming` language that focuses on strong compile-time correctness guarantees.

- Strong memory guarantees make writing correct concurrent Rust code easier than in other languages.

- It is focused on three goals: safety, speed, and concurrency. It maintains these goals without having a garbage collector.

- Good interfacing with wasm.

- No garbage collector.

- No green threads given, can be a library but not runtime feature to support to write a portion

- If you have a reference &T, then normally in Rust the compiler performs optimizations based on the knowledge that &T points to immutable data. Mutating that data, for example through an alias or by transmuting an &T into an &mut T, is considered undefined behavior. `UnsafeCell<T>` opts-out of the immutability guarantee for &T: a shared reference `&UnsafeCell<T>` may point to data that is being mutated. This is called “interior mutability”


### Ownership

 - Ownership 
    - The scope that will free the resource. 
    - Owned.

 - Mutable Reference
    - Can be only one. No one can Read and write another. 
    - Exclusive access. 
    - No responsibility to free. Only borrowing it.

 - Immutable Reference
    - No modification. Multiple read. Shared.


``` rust

// Wont work. Stack Allocated. 
// Borrowed pointer will leave. Borrowed value will not.

fn dangling() -> &int {
    let i = 1234;
    return &i;
}

// Will Work. Heap Allocated.

fn dangling() -> ~int {
    let i = ~1234;
    return i;
}

fn add_one() -> int {
    let num = dangling();
    return *num + 1;
}

```

### Rust use after free

```rust

fn take_ownership(s: String) {
    println!("{}", s);
    // s goes out of scope and freed
}

let foo = String::from("Test");
take_ownership(foo);

// Memory is freed. 
// Using foo again would be use after free.
// take_ownership(foo);

```

### Rust does not have the concept of null

```rust
// rust
let i = ~1234;

// C++
int *i = new int;
*i = 1234;

// The Rust compiler also figures out the lifetime of i, and then inserts a corresponding free call after it’s invalid, like a destructor in C++. You get all of the benefits of manually allocated heap memory without having to do all the bookkeeping yourself.

// All of this checking is done at compile time, so there’s no runtime overhead. You’ll get (basically) the exact same code that you’d get if you wrote the correct C++, but it’s impossible to write the incorrect version, thanks to the compiler

// Rust allows you to spin up ‘tasks,’ which are lightweight, ‘green’ threads. These tasks do not have any shared memory, and so, we communicate between tasks with a ‘channel’

```


### Copy vs Reference

```rust

// Copying the vector. Not efficiecnt.

fn main() {
    let numbers = [1,2,3];

    let (port, chan)  = Chan::new();
    chan.send(numbers);

    do spawn {
        let numbers = port.recv();
        println!("{:d}", numbers[0]);
    }
}


// Sending Reference.
extern mod extra;
use extra::arc::Arc;

fn main() {
    let numbers = [1,2,3];

    // Arc stands for ‘atomically reference counted,’ and it’s a way to share immutable data between multiple tasks.

    let numbers_arc = Arc::new(numbers);

    for num in range(0, 3) {
        let (port, chan)  = Chan::new();
        chan.send(numbers_arc.clone());

        do spawn {
            let local_arc = port.recv();
            let task_numbers = local_arc.get();
            println!("{:d}", task_numbers[num]);
        }
    }
}

// In case of mutating
extern mod extra;
use extra::arc::RWArc;

fn main() {
    let numbers = [1,2,3];

    let numbers_arc = RWArc::new(numbers);

    for num in range(0, 3) {
        let (port, chan)  = Chan::new();
        chan.send(numbers_arc.clone());

        do spawn {
            let local_arc = port.recv();

            // Closures as arguemnt

            // This acquire a mutex, and then pass the data to this closure. After the closure does its thing, the mutex is released

            // You can see how this makes it impossible to mutate the state without remembering to aquire the lock. We gain the efficiency of shared mutable state, while retaining the safety of disallowing shared mutable state.

            local_arc.write(|nums| {
                nums[num] += 1
            });

            local_arc.read(|nums| {
                println!("{:d}", nums[num]);
            })
        }
    }
}

```

### Macro
- Rust maintains `Hygenic macro`

### Borrow

Any borrow must last for a scope no greater than that of the owner. We may have one or the other of these two kinds of borrows, but not both at the same time.

- One or more references (&T) to a resource.
- Exactly one mutable reference (&mut T).

Borrow checker will check you have not used anything after you have gotten rid of it. Mutable access to something shared.


### Lifetime Operator

```rust

// params with two lifetime as generic. Return depends only on first param's lifetime.

fn skip_prefix<'a, 'b>(line: &'a str, prefix: &'b str) -> &'a str {
    // ...
}


// Perfectly handles this case

fn skip_prefix(line: &str, prefix: &str) -> &str {
    // ...
}

let line = "lang:en=Hello World!";
let lang = "en";

let v;
{
    let p = format!("lang:{}=", lang);  // -+ `p` comes into scope.
    v = skip_prefix(line, p.as_str());  //  |
}                                       // -+ `p` goes out of scope.
println!("{}", v);


// struct usage

// To ensure that any reference to a Foo cannot outlive the reference to an i32 it contains.

struct Foo<'a> {
    x: &'a i32,
}


// Named lifetimes are a way of giving these scopes a name. Giving something a name is the first step towards being able to talk about it.


// static lifetime

let x: &'static str = "Hello, world.";

static FOO: i32 = 5;
let x: &'static i32 = &FOO;

```

### Lifetime Elision

Here explicit lifetime declation is elicited. There are the three rules:

- Each elided lifetime in a function’s arguments becomes a distinct lifetime parameter.

- If there is exactly one input lifetime, elided or not, that lifetime is assigned to all elided lifetimes in the return values of that function.

- If there are multiple input lifetimes, but one of them is &self or &mut self, the lifetime of self is assigned to all elided output lifetimes.


### Mutability

```rust
// Mutability is a property of either a borrow (&mut) or a binding (let mut). Mutability is a property of the binding, not of the structure itself.

- exterior mutability
- interior mutability

struct Point {
    x: i32,
    mut y: i32, // Not allowed.
}

// To achive field level mutability.

use std::cell::Cell;

struct Point {
    x: i32,
    y: Cell<i32>,
}

let point = Point { x: 5, y: Cell::new(6) };
point.y.set(7);

println!("y: {:?}", point.y);

```

### Destructuring

```rust

let Point(_, origin_y, origin_z) = origin;

struct Inches(i32);

let length = Inches(10);

let Inches(integer_length) = length;

```

### Enum

Also called `tagged union`

### Match

Match is also an expression, which means we can use it on the right-hand side of a let binding or directly where an expression is used:

```rust
let x = 5;

let number = match x {
    1 => "one",
    2 => "two",
    3 => "three",
    4 => "four",
    5 => "five",
    _ => "something else",
};
```

### Pattern introduces shadowing

```rust
let x = 1;
let c = 'c';

match c {
    x => println!("x: {} c: {}", x, c),
}

println!("x: {}", x)

// This prints:

// x: c c: c
// x: 1

```

Sometimes it’s a nice way of converting something from one type to another, in this example the integers are converted to String.


### Methods

This `associated function` builds a new Circle for us. 
Note that associated functions are called with the Struct::function() syntax, rather than the ref.method() syntax.Some other languages call associated functions ‘static methods’.

```rust

struct Circle {
    x: f64,
    y: f64,
    radius: f64,
}

// normal methods

impl Circle {

    fn area(&self) -> f64 {
        std::f64::consts::PI * (self.radius * self.radius)
    }

    fn grow(&self, increment: f64) -> Circle {
        Circle { x: self.x, y: self.y, radius: self.radius + increment }
    }
}

fn main() {

    let c = Circle { x: 0.0, y: 0.0, radius: 2.0 };
    println!("{}", c.area());

    let d = c.grow(2.0).area();
    println!("{}", d);
}


// Asscoiated methods
impl Circle {
    fn new(x: f64, y: f64, radius: f64) -> Circle {
        Circle {
            x: x,
            y: y,
            radius: radius,
        }
    }
}

```

### String

A ‘string’ is a sequence of Unicode scalar values encoded as a stream of UTF-8 bytes.

```rust

let greeting = "Hello there."; // greeting: &'static strRun

// "Hello there." is a string literal and its type is &'static str. A string literal is a string slice that is statically allocated, meaning that it’s saved inside our compiled program, and exists for the entire duration it runs. The greeting binding is a reference to this statically allocated string. Any function expecting a string slice will also accept a string literal.

// Because strings are valid UTF-8, they do not support indexing:

let s = "hello";

println!("The first letter of s is {}", s[0]); // ERROR!!!Run

// Usually, access to a vector with [] is very fast. But, because each character in a UTF-8 encoded string can be multiple bytes, you have to walk over the string to find the nᵗʰ letter of a string. This is a significantly more expensive operation, and we don’t want to be misleading. Furthermore, ‘letter’ isn’t something defined in Unicode, exactly. We can choose to look at a string as individual bytes, or as codepoints:

let hachiko = "忠犬ハチ公";

for b in hachiko.as_bytes() {
    print!("{}, ", b);
}

// 229, 191, 160, 231, 138, 172, 227, 131, 143, 227, 131, 129, 229, 133, 172,

for c in hachiko.chars() {
    print!("{}, ", c);
}

println!("");

// 忠, 犬, ハ, チ, 公,

```


### Unsized type

Rust understands a few of these types, but they have some restrictions. 

There are three:

- We can only manipulate an instance of an unsized type via a pointer. An &[T] works fine, but a [T] does not.

- Variables and arguments cannot have dynamically sized types.

- Only the last field in a struct may have a dynamically sized type, the other fields must not. Enum variants must not have dynamically sized types as data.

### Generic

```rust

enum Option<T> {
    Some(T),
    None,
}

```

# Trait

Trait contains method signature.

```rust
struct Circle {
    x: f64,
    y: f64,
    radius: f64,
}

trait HasArea {
    fn area(&self) -> f64;
    fn is_larger(&self, &Self) -> bool;
}

impl HasArea for Circle {
    fn area(&self) -> f64 {
        std::f64::consts::PI * (self.radius * self.radius)
    }
    fn is_larger(&self, other: &Self) -> bool {
        self.area() > other.area()
    }
}

// with generics
fn print_area<T: HasArea>(shape: T) {
    println!("This shape has an area of {}", shape.area());
}

trait Graph {
    type N;
    type E;

    fn has_edge(&self, &Self::N, &Self::N) -> bool;
    fn edges(&self, &Self::N) -> Vec<Self::E>;
}
```

### Attributes

```rust
#[derive(Debug)]
struct Foo;

fn main() {
    println!("{:?}", Foo);
}

// Clone
// Copy
// Debug
// Default
// Eq
// Hash
// Ord
// PartialEq
// PartialOrd
```

### Check last state of stuct when relesed

```rust
struct Firework {
    strength: i32,
}

impl Drop for Firework {
    fn drop(&mut self) {
        println!("BOOM times {}!!!", self.strength);
    }
}

fn main() {
    let firecracker = Firework { strength: 1 };
    let tnt = Firework { strength: 100 };
}
// BOOM times 100!!!
// BOOM times 1!!!

// Arc<T> type is a reference-counted type. When Drop is called, it will decrement the reference count, and if the total number of references is zero, will clean up the underlying value.
```

### Trait Objects

When code involves polymorphism, there needs to be a mechanism to determine which specific version is actually run. 
This is called ‘dispatch’. 

There are two major forms of dispatch:
- Static dispatch 
- Dynamic dispatch

While Rust favors static dispatch, it also supports dynamic dispatch through a mechanism called ‘trait objects’.

```rust

fn do_something<T: Foo>(x: T) {
    x.method();
}
// Will be converted to this
fn do_something_u8(x: u8) {
    x.method();
}
fn do_something_string(x: String) {
    x.method();
}
// This has a great upside: static dispatch allows function calls to be inlined because the callee is known at compile time, and inlining is the key to good optimization. Static dispatch is fast, but it comes at a tradeoff: ‘code bloat’, due to many copies of the same function existing in the binary, one for each type.

// Furthermore, compilers aren’t perfect and may “optimize” code to become slower. For example, functions inlined too eagerly will bloat the instruction cache (cache rules everything around us). This is part of the reason that #[inline] and #[inline(always)] should be used carefully, and one reason why using a dynamic dispatch is sometimes more efficient.

// However, the common case is that it is more efficient to use static dispatch, and one can always have a thin statically-dispatched wrapper function that does a dynamic dispatch, but not vice versa, meaning static calls are more flexible. The standard library tries to be statically dispatched where possible for this reason.


// This operation can be seen as ‘erasing’ the compiler’s knowledge about the specific type of the pointer, and hence trait objects are sometimes referred to as ‘type erasure’.

// Dynamic dispatch
fn do_something(x: &Foo) {
    x.method();
}

fn main() {
    let x = 5u8;
    do_something(&x as &Foo);
}

// this comes at the cost of requiring slower virtual function calls, and effectively inhibiting any chance of inlining and related optimizations from occurring.

// The methods of the trait can be called on a trait object via a special record of function pointers traditionally called a ‘vtable’ 
```

### Variance

```rust
// Covariance
// Any lifetime can be treated as static

let x: &'static str // more useful
let a: &'a str

a = x 
// Contravariance

fn foo(&'a str) { // less usefull}
fn foo(&'static str) { // less usefull}

// Invariance
fn foo(s: &mut &'a str, a: &'a str) {}
let mut x = ""
foo(x, ""  )

use std::marker::PhantomData;
struct Deserializer<T> {
    _t: PhantomData<T>,
}

// Mutable references are invariant in the type they point to,
// and covariant in their lifetime
```


### Callback based future

```rust
// Way too many allocaiton, dynamic dispatch
trait Future {
    type Output;
    fn schedule<F>(self, callback: F) 
        where F: FnOnce(Self:: Output);
}
```

### Concurrency
- When a type T implements Send, it indicates that something of this type is able to have ownership transferred safely between threads.

### Other Points

- Static mutable is unsafe, and so must be done in an unsafe block.

- Any type stored in a static must be Sync, and must not have a `Drop` implementation.

- They follow the “read-write lock” pattern, such that one may either have only one mutable reference to some data, or any number of immutable ones, but not both.

- Mutex gives exclusive or mutable access to a key through a shared reference to mutex

- R/W lock, mutex either have lock for multiple read or single write

- Locks provide safe wrapper around aliased or shared pointer.

- Learning curve is borrow checking

- Rust Clippy

- Carriage return line feed used in windows, linux uses line feed.

- Calling rust has no abstraction like cGo, JNI.

- Runtime programs 
    - Stuffs that your programming language puts that you dont write.
    
- Tokio core is event loop of tokio    

```rust
#[cfg(foo)]
// in toml define one
```

Build System
Cargo is Rust’s build system and package manager, and Rustaceans use Cargo to manage their Rust projects.

crate - library - holds module

```bash
cargo init
cargo new crate_name

# "^0.5.1" always goes to "1.0.0" upto not including

# "~0.5.1" always goes to "0.6.0" upto not including. last set version.

# bin package should have Cargo.lock, lib package should not

# embed example as doc, run & verify test
# a library is only as good as its documnetation
cargo test --doc

# optional dependency
serde = { version = "1.0", default-features = false, features = ["derive"], optional = true }

# dependency fetch only when feature enabled 
```

**Trait objects** - has lackings, read again

### REPR
This is the most important repr. It has fairly simple intent: do what C does. The order, size, and alignment of fields is exactly what you would expect from C or C++. Any type you expect to pass through an FFI boundary should have repr(C), as C is the lingua-franca of the programming world. This is also necessary to soundly do more elaborate tricks with data layout such as reinterpreting values as a different type.

### Closure
- boxed closure syntax |&:| -> int
-  the sugar syntax is `|X: args...| -> ret`, where the X can be `&, &mut or nothing`, corresponding to the `Fn, FnMut, FnOnce` traits, you can also write `Fn<(args...), ret>` etc. for the non-sugared form. The sugar is likely to be changing (possibly something like `Fn(args...) -> ret).`

---

### References
- [Rust Ownership, Safety Explained](https://words.steveklabnik.com/a-30-minute-introduction-to-rust)

- [How Rust Ownership works?](https://static.rust-lang.org/doc/master/book/ownership.html)

- [Macro Hygienic](https://en.wikipedia.org/wiki/Hygienic_macro)

- [Error Handling Rust Documentation](https://static.rust-lang.org/doc/master/book/error-handling.html)

- [Sample Library Usage](https://github.com/brson/stdx/blob/master/README.md)

- [Rust overview](https://www.youtube.com/watch?v=9x7W3_KKKeA&ab_channel=YOW%21Conferences)

- [Rust at Speed](https://www.youtube.com/watch?v=s19G6n0UjsM&t=3s) 
    - Explains usage of rust on [Noria](https://github.com/mit-pdos/noria)
    - Usage of cache inside DB, mainly materialized view, the current result for a query.
    - Problem: Huge result table, concurrent read write on same table, partial materialized view.
    - Lock, RWLock fails being the costly one themselves as the wrapping work is too less.
    - Maintain two maps, one for read, another for write maintaining epic counter +2 for each read and  switch for alternatively.

- [Pinning](https://stackoverflow.com/questions/49913846/what-are-the-use-cases-of-the-newly-proposed-pin-type)
    - Self referenceing object move will make the member reference to point to old object. Pinning solves it.

- [Code Benchmarking](https://godbolt.org/z/nqTveYvzx)

- [RustC Dev Guides](https://rustc-dev-guide.rust-lang.org/llvm-coverage-instrumentation.html)

- [Chalk](https://rust-lang.github.io/chalk/book)
- [Rust Functional Programming](https://github.com/JasonShin/fp-core.rs)