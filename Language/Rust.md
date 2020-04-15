# RUST

Rust is a systems programming language that focuses on strong compile-time correctness guarantees.

Strong memory guarantees make writing correct concurrent Rust code easier than in other languages.

Rust is a systems programming language focused on three goals: safety, speed, and concurrency. It maintains these goals without having a garbage collector.

# Ownership

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

- Rust does not have the concept of null.

```rust
// rust
let i = ~1234;

// C++
int *i = new int;
*i = 1234;
```

- The Rust compiler also figures out the lifetime of i, and then inserts a corresponding free call after it’s invalid, like a destructor in C++. You get all of the benefits of manually allocated heap memory without having to do all the bookkeeping yourself.
- All of this checking is done at compile time, so there’s no runtime overhead. You’ll get (basically) the exact same code that you’d get if you wrote the correct C++, but it’s impossible to write the incorrect version, thanks to the compiler.


- Rust allows you to spin up ‘tasks,’ which are lightweight, ‘green’ threads. These tasks do not have any shared memory, and so, we communicate between tasks with a ‘channel’.

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


// Sending reference.

extern mod extra;
use extra::arc::Arc;

fn main() {
    let numbers = [1,2,3];

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

- Cargo is Rust’s build system and package manager, and Rustaceans use Cargo to manage their Rust projects

- 


--- 
RESOURCES: 
> https://words.steveklabnik.com/a-30-minute-introduction-to-rust
> https://static.rust-lang.org/doc/master/book/getting-started.html