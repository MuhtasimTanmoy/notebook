# [Concurrent Programming in Erlang](https://erlang.org/download/erlang-book-part1.pdf)

- Erlang has a process-based model of concurrency with asynchron- ous message passing. The concurrency mechanisms in Erlang are light- weight, i.e. processes require little memory, and creating and deleting pro- cesses and message passing require little computational effort.

- Erlang is a symbolic programming language with a real-time garbage collector

- The use of a pattern matching syntax, and the ‘single assignment’ property of Erlang variables, leads to clear, short and reliable programs.

- Registered process which allows us to associate a name with a process.

- Erlang has primitives for multi- processing: spawn starts a parallel computation (called a process); send sends a message to a process; and receive receives a message from a process.

- The syntax Pid ! Msg is used to send a message.

- While we can think of send as sending a message and receive as receiving a message, a more accurate description would be to say that send sends a message to the mailbox of a process and that receive tries to remove a message from the mailbox of the current process.
receive is selective, that is to say, it takes the first message which matches one of the message patterns from a queue of messages waiting for the attention of the receiving process. If none of the receive patterns matches then the process is suspended until the next message is received – unmatched messages are saved for later processing.

- Instead of evaluating the function, however, and returning the result as in apply, spawn/3 creates a new concurrent process to evaluate the function and returns the Pid (process identifier) of the newly created process.

- As Pids are necessary for all forms of communication, security in an Erlang system is based on restricting the spread of the Pid of a process.

- A process identifier is a valid data object and can be manipulated like any other object. For example, it can be stored in a list or tuple, compared to other identifiers, or sent in messages to other processes.

- Erlang has no mutexes, no synchronized methods, and none of the paraphernalia of shared memory programming.

- Chapter 5: Concurrent Programming