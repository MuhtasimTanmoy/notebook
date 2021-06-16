# JavaScript

- One app, one thread, one event loop, turns application into multitreaded
- The syncronous logic gets executed first, require modules as well
- Only syncronous heavy duty code should be dispatched to `worker thread`. Others `io` already handed off to `libuv` thradpool.

JavaScript can be divided into three cores (pillars):

Types:
- Primitive Types
- Abstract Operations
- Coercion
- Equality
- TypeScript, Flow, etc.

Scope:
- Nested Scope
- Hoisting
- Closure
- Modules

Objects (Oriented):
- this
- class{}
- Prototypes
- OO vs. OLOO

- Coercion
    - Converting a value from one type to another is often called “type casting”, when done explicitly, and “coercion” when done implicitly (forced by the rules of how a value is used).

- double equals (==) will perform a type conversion when comparing two things, and will handle NaN, -0, and +0 specially to conform to IEEE 754 (so NaN != NaN, and -0 == +0);

- triple equals (===) will do the same comparison as double equals (including the special handling for NaN, -0, and +0) but without type conversion; if the types differ, false is returned.

- Event Loop
    - The event loop will only process when the `call stack` is empty.
    - The delay we define in timer is not the `exact` time rather the `minimum` time needed.
    - Different phases in event loop executes different types of callbacks.
    - `nextTick` is the micro task
    - `nextTick` is prioratized over promise.
    - `console.log`, `json.parse` and `stringify` are syncronous, use them in `setTimeOut` whenever possible.
    - Should not use `nextTick` as it blocks event loop phase `poll` as those are needed for handling network request.
    - Heavy duty tasks to be forwarded to worker thread so it does not block the current looping thread.
    - Requiring module is syncronous, should be donw at root level.

![](./images/Event%20Loop%20Phases.png)

```js

// As setImmediate has precedence it will always get executed first

const fs = require('fs');
fs.readFile(__fileName, () => {
    setTimeout(() => {
        console. log( "timeout" );
    }, 0);

    setImmediate(() => {
        console.log( "Immediate" )
    }
    )
})

// Immediate called first, then timeout

const fs = require(`fs`);

console.log(`START`);

const readFileCallback = () => {
  console.log(`readFileCallback`);
};
fs.readFile(__filename, readFileCallback);

const setImmediateCallback = () => {
  console.log(`setImmediateCallback`);
};
setImmediate(setImmediateCallback);

// Now follows the loop long enough to give the fs.readFile enough time
// to finish its job and to place its callback (the readFileCallback)
// into the event-loop's poll phase queue before the "main" synchronous part
// of the this code finishes.
for (let i = 1; i <= 10000000000; i++) {}

console.log(`END`);
// So when the event-loop starts its first tick there should be two callbacks
// waiting:
//   (1) the readFileCallback (in the poll queue)
//   (2) the setImmediateCallback (in the check queue)
// Now according to the Node.js DOCs, of these two waiting callbacks
// the readFileCallback should execute first, but the opposite
// is actually happening, that is setImmediateCallback executes first.


// DOC

// The poll phase has two main functions:
//     1. Calculating how long it should block and poll for I/O, then
//     2. Processing events in the poll queue.

// When the event loop enters the poll phase and there are no timers scheduled,
// one of two things will happen:

//   (a)  - If the poll queue is not empty, the event loop will iterate
//         through its queue of callbacks executing them synchronously
//         until either the queue has been exhausted,
//         or the system-dependent hard limit is reached.

//   (b)  - If the poll queue is empty, one of two more things will happen:
//         - If scripts have been scheduled by setImmediate(),
//           the event loop will end the poll phase and continue to the check phase
//           to execute those scheduled scripts.
//         - If scripts have not been scheduled by setImmediate(),
//           the event loop will wait for callbacks to be added to the queue,
//           then execute them immediately.

// Once the poll queue is empty the event loop will check for timers
// whose time thresholds have been reached. If one or more timers are ready,
// the event loop will wrap back to the timers phase
// to execute those timers' callbacks.

```

# Resources
- [Javascript Foundation](https://github.com/farnaz-kakhsaz/Deep-JavaScript-Foundations/blob/master/README.md)