# Erlang

Erlang is a functional language and accompanying runtime designed for highly parallel, scalable applications requiring high uptime.
- Immutable Data
- Functional Language

Erlang does this with features such as a built-in worker-supervisor 
message-passing model and hot-swappable code, meaning errors or code updates don't require the entire process to stop and restart in order to recover.

## Beam

- BEAM is like Java’s JVM, but for Erlang
- Interface to outside world - NIC / Ports
- Schedulers
    - Beam VM 
    - One VM per Thread
- Processes
- Memory Management
    -  Process heaps
    -  ETS tables
    -  Atom table
    -  Large binary space

 - Variables in Erlang can only be assigned once. The Erlang shell provides a special command if that allows you to erase the binding of a variable or all variables at once.

 - Erlang does not have an intermediary like Go channel, but it does employ a very powerful concept known as the Actor Model. In this world, a process is an independent actor. It doesn't care about the outside world. It's like a prisoner churning over its own thing and wait for something to be passed into its prison's door, or more specifically, mailbox.

- Erlang's actor model is so simple and powerful. 
- It never has to care about data race or syncing because each process can never access anything external.

Each Erlang process has a small memory footprint and can grow/shrink dynamically. It does not share memory and only communicate through message passing.

- Erlang is a niche language, but it is the niche with all of the very good developers. 

- Akka as it can be used with Java, and is influenced by Erlang.

- Erlang does this with features such as a built-in worker-supervisor message-passing model and hot-swappable code, meaning errors or code updates don't require the entire process to stop and restart in order to recover. Hot-swappable code allowing truly live updates to the program's behavior is a feature nearly unique to Erlang; most other programs and runtimes, even those designed for high uptime, have to end and be restarted to incorporate code changes.

- Most traditionally-imperative programmers look at the functional language branch as an academic curiosity, but a lot of functional concepts such as monadic processing (a function accepting an input returns an object that supports its own library of operations, allowing for method chaining with a "grammar structure", commonly known as a "fluent interface"), first-order functions (a function is an independently reference-able, assignable variable, independent of any other construct besides its input parameters), declarative syntax (the structure of the code indicates what to do more than how) have been incorporated into current versions of modern imperative languages.

- It has the ability to handle multiple threads ( Process in Erlang terms) at the same time not utilising double CPU processing power. Unlike C program thread in which each thread uses seperate resources from the CPU.

- I want an implementation of the capability model. (Better security. PIDs could be transformed into some kind of URIs which means they would be available from anywhere in the world! Lets break out of the VM already! It's not in Erlang yet but I would switch for that).


# Features

- Everything is a process.
- Processes are strongly isolated.
- Process creation and destruction is a lightweight operation.
- Message passing is the only way for processes to interact.
- Processes have unique names, internal state.
- If you know the name of a process you can send it a message.
- Processes share no resources.
- Error handling is non-local.
- Processes do what they are supposed to do or fail.
- In computer science, syntactic sugar is syntax within a programming language that is designed to make things easier to read or to express. It makes the language "sweeter" for human use: things can be expressed more clearly, more concisely, or in an alternative style that some may prefer.
- It also supports interpreting, directly from source code via abstract syntax tree
- You can remember this because forms aren't expressions (no value is returned from them), and therefore the period represents the end of a statement.

# Actor Supervisor
- Actors are persistent
- Encapsulates internal state
    - Threads have state
    - Coroutines has state
- Actors are asyncronous
- Actors can create actors (main thread can create other threads as well )
- Receive message make local decision
- Perform arbitary side effecting function
- Do you comunicate by sharing memory instead share memory by communicating message
- Mutex - but many race condition
- Golang channel to share between two goroutines
- Address is actor - location & transport info
- One actress may represent many actors
- One actor may have many addresses
- Supervision - the running state of an actor managed and supervised by an actor
- Addresses dont change in restarts 
- Address encapsulates mailbox and actor
- Clustering built-in with autodiscovery. It's very nice to start up activemq on two machines and see them find each other automagically.

 # Tutorial

 - Variables can't be variable in functional programming.

 - The first thing these commands tell us is that you can assign a value to a variable exactly once; then you can 'pretend' to assign a value to a variable if it's the same value it already has.

 - What this operator does when mixed with variables is that if the left-hand side term is a variable and it is unbound (has no value associated to it), Erlang will automatically bind the right-hand side value to the variable on the left-hand side. The comparison will consequently succeed and the variable will keep the value in memory.

 - This behavior of the = operator is the basis of something called 'Pattern matching', 

 -  If you're testing in the shell and save the wrong value to a variable, it is possible to 'erase' that variable by using the function f(Variable).. If you wish to clear all variable names, do f().

 - Atoms are literals, constants with their own name for value. What you see is what you get and don't expect more. The atom cat means "cat" and that's it.

 - An atom should be enclosed in single quotes (') if it does not begin with a lower-case letter or if it contains other characters than alphanumeric characters, underscore (_), or @.

 - I compared atoms to constants having their name as their values. You may have worked with code that used constants before: as an example, let's say I have values for eye colors: BLUE -> 1, BROWN -> 2, GREEN -> 3, OTHER -> 4. You need to match the name of the constant to some underlying value. Atoms let you forget about the underlying values: my eye colors can simply be 'blue', 'brown', 'green' and 'other'. T

- Atoms are really nice and a great way to send messages or represent constants. However there are pitfalls to using atoms for too many things: an atom is referred to in an "atom table" which consumes memory (4 bytes/atom in a 32-bit system, 8 bytes/atom in a 64-bit system). The atom table is not garbage collected, and so atoms will accumulate until the system tips over, either from memory usage or because 1048577 atoms were declared.

- The boolean operators and and or will always evaluate arguments on both sides of the operator. If you want to have the short-circuit operators (which will only evaluate the right-side argument if it needs to), use andalso and orelse.

- Erlang won't care about floats and integers in arithmetic, but will do so when comparing them. No worry though, because the == and /= operators are there to help you in these cases. 

- Pragmaticism beats theory

- One of the earliest challenges we faced was reducing the channel servers' memory footprint. High-level languages often provide rich data types and powerful abstractions for manipulating them. Erlang strings, for instance, are linked lists of characters, allowing programmers to use all the list-manipulation goodies that Erlang provides. In this case, however, it pays to control the representation a little closer and use arrays of characters like one might in C++. In this case we traded back some of Erlang's power in favor of CPU and memory usage. We also exploited the nature of our application to make another trade-off: just before a user's HTTP response process goes to sleep to wait for a new message to arrive, we force a pass of the garbage collector. We spend more cycles in that process than we usually would, but we ensure that it's using as little as memory as possible before it sleeps.

- C++ less memory footprint
- https://www.facebook.com/notes/facebook-engineering/chat-stability-and-scalability/51412338919/


## Tail call optimization

Saying that something is "tail recursive" is a short-hand way of saying "the function is recursive" and that we only find pure function
calls in the tail-positions of all branches of a function.

On a conventional stack machine, this is compiled into something like this:

```
X: pushAddr 1
goto a
1:pushAddr 2
goto b
2:pushAddr 3
goto c
3:ret
```

- pushAddr pushed a return address onto the stack. 
- goto <label> jumps to the start address of the routine.  
- The last statement will be a return (ret) which expects to find a return address on the top of stack.

This is called 'last call optimization' - it just says that if the
last thing a function does is call another function, then the call
can be replaced by jump to the start of the function.


## Garbage Collector

- When it's time to collect garbage in other languages, the entire system has to stop while the garbage collector runs. This approach is perfectly fine if your computer program is supposed to run once, write some output, and then quit. But in long-running applications, such as desktop, mobile, or server programs, this strategy results in occasionally frozen UIs and slow response times.

- Erlang programs, on the other hand, can have thousands of independent heaps which are garbage-collected separately; in this way, the performance penalty of garbage collection is spread out over time, and so a long-running application will not mysteriously stop responding from time to time while the garbage collector runs.

> https://www.evanmiller.org/why-i-program-in-erlang.html


# Shell

erl - Erlang
iex - Elixir
rebar3 binary download and copy to /usr/local/bin/
rebar3 compile

### Open source Erlang Applications :

- RabbitMQ: AMQP messaging protocol implementation. AMQP is an emerging standard for high-performance enterprise messaging.

- CouchDB: “schema-less” document-oriented database, providing scalability across multicore and multiserver clusters.

- Ejabberd: system provides an Extensible Messaging and Presence Protocol (XMPP) based instant messaging (IM) application server.

- Riak
    - Performance Benchmark
    - https://github.com/MuhtasimTanmoy/Riak-Database-Project

# Resources

- [Beam VM](http://www.erlang-factory.com/upload/presentations/708/HitchhikersTouroftheBEAM.pdf)
- [First Person Shooter in Erlang](http://www.erlang-factory.com/upload/presentations/395/ErlangandFirst-PersonShooters.pdf)
- [The Beam Book](https://blog.stenmans.org/theBeamBook/)
- [Erlang Design Architecture](https://stackoverflow.com/questions/7307634/how-do-you-design-the-architecture-of-an-erlang-otp-based-distributed-fault-tole/7308218#7308218)