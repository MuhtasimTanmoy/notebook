# RUST

- Rust is a systems programming language that focuses on strong compile-time correctness guarantees.

- Strong memory guarantees make writing correct concurrent Rust code easier than in other languages.

- Rust is a systems programming language focused on three goals: safety, speed, and concurrency. It maintains these goals without having a garbage collector.

- Good interfacing with wasm.

- No garbage collector.



# Code Sample

**Ownership**

 - Ownership - The scope that will free the resource. Owned.
 - Mutable Ref - Can be only one. No one can Read and write. Exclusive access. No responsibility to free. Only borrowing it. Exclusive.
 - Immutable Ref - No modification. Multiple read. Shared.


``` rust
// Wont work. Stack Allocated. Borrowed pointer will leave. Borrowed value will not.
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

**Rust does not have the concept of null**

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


**Copy vs Reference**

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

            // CLosures as arguemnt

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

**Macro**

- Rust maintains `Hygenic macro`

**Trait**

**Borrow**

Any borrow must last for a scope no greater than that of the owner. We may have one or the other of these two kinds of borrows, but not both at the same time:

- one or more references (&T) to a resource,
- exactly one mutable reference (&mut T).

Borrow checker will check you have not used anything after you have gotten rid of it. Mutable access to something shared.

```rust


```

**Lifetime Operator**

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

**Lifetime elision**

Here explicit lifetime declation is elicited. There are the three rules:

- Each elided lifetime in a function’s arguments becomes a distinct lifetime parameter.

- If there is exactly one input lifetime, elided or not, that lifetime is assigned to all elided lifetimes in the return values of that function.

- If there are multiple input lifetimes, but one of them is &self or &mut self, the lifetime of self is assigned to all elided output lifetimes.


**Mutability**

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

**Destructuring**

```rust

let Point(_, origin_y, origin_z) = origin;

struct Inches(i32);

let length = Inches(10);

let Inches(integer_length) = length;

```

**Enum**

Also called `tagged union`

**Match**

match is also an expression, which means we can use it on the right-hand side of a let binding or directly where an expression is used:

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

**Pattern introduces shadowing**

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

Sometimes it’s a nice way of converting something from one type to another; in this example the integers are converted to String.



**Methods**

This ‘associated function’ builds a new Circle for us. Note that associated functions are called with the Struct::function() syntax, rather than the ref.method() syntax. Some other languages call associated functions ‘static methods’.

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

**String**

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


**Unsized type**

Rust understands a few of these types, but they have some restrictions. There are three:

- We can only manipulate an instance of an unsized type via a pointer. An &[T] works fine, but a [T] does not.
- Variables and arguments cannot have dynamically sized types.
- Only the last field in a struct may have a dynamically sized type; the other fields must not. Enum variants must not have dynamically sized types as data.

**Generic**

```rust

enum Option<T> {
    Some(T),
    None,
}

```


**Trait**

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


// With generics

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

**Attributes**

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


**Check last state of stuct when relesed**


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


**Trait objects** 

When code involves polymorphism, there needs to be a mechanism to determine which specific version is actually run. This is called ‘dispatch’. There are two major forms of dispatch: static dispatch and dynamic dispatch. While Rust favors static dispatch, it also supports dynamic dispatch through a mechanism called ‘trait objects’.

```rust

fn do_something<T: Foo>(x: T) {
    x.method();
}

// will be converted to this

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

**Crates**

- Demo - [Github Link]()

**Concurrency**

- When a type T implements Send, it indicates that something of this type is able to have ownership transferred safely between threads.



**Other Points**
- Static mut is unsafe, and so must be done in an unsafe block
- Any type stored in a static must be Sync, and must not have a Drop implementation.
- They follow the “read-write lock” pattern, such that one may either have only one mutable reference to some data, or any number of immutable ones, but not both.
- Mutex gives exclusive or mutable access to a key through a shared reference to mutex
- R/W lock, mutex either have lock for multiple read or single write
- locks provide safe wrapper around aliased or shared pointer
- Learning curve is borrow checking  
- Rust Clippy
- Runtime programs - stuffs that your programming language puts that you dont write
 

```rust

#[cfg(foo)]

// in toml define one
 
```

**Build System**    

Cargo is Rust’s build system and package manager, and Rustaceans use Cargo to manage their Rust projects.

crate - library - holds module

```bash

cargo init

cargo new crate_name

```

**incomplete**

**Trait objects** - has lackings, read again

**Closures**

---


RESOURCES:

- [Rust ownership, safety explained](https://words.steveklabnik.com/a-30-minute-introduction-to-rust)

- [Rust Documentation](https://static.rust-lang.org/doc/master/book/getting-started.html)

- [Macro Hygienic](https://en.wikipedia.org/wiki/Hygienic_macro)

- [How Rust ownership works?](https://static.rust-lang.org/doc/master/book/ownership.html)

- [Error Handling RustDoc](https://static.rust-lang.org/doc/master/book/error-handling.html)

TALKS : 
- [Rust at Speed](https://www.youtube.com/watch?v=s19G6n0UjsM&t=3s) 
    - Expalins usage of rust on [Noria](https://github.com/mit-pdos/noria)
    - Usage of cache inside DB, mainly materialized view, the current result for a query.
    - Problem : Huge result table, concurrent read write on same table, partial materialized view.
    - Lock, RWLock fails being the costly one themselves as the wrapping work is too less
    - Maintain two maps, one for read, another for write maintaining epic counter +2 for each read and  switch for alternatively.
    -  
