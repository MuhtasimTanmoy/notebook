# JavaScript

- One app, one thread, and one event loop turns the application into a multithreaded
- The synchronous logic gets executed first and requires modules as well
- Only synchronous heavy-duty code should be dispatched to the `worker thread`. Others `io` already handed off to `libuv` thradpool.

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
    - Converting a value from one type to another is often called “type casting” when done explicitly, and “coercion” when done implicitly (forced by the rules of how a value is used).

- double equals (`==`) will perform a type conversion when comparing two things, and will handle NaN, -0, and +0 especially to conform to IEEE 754 (so NaN != NaN, and -0 == +0);

- triple equals (`===`) will do the same comparison as double equals (including the special handling for NaN, -0, and +0) but without type conversion; if the types differ, false is returned.

- `npm link` to create a symlink of the module

- Event Loop   
    - The event loop will only process when the `call stack` is empty.
    - The delay we define in the timer is not the `exact` time but rather the `minimum` time needed.
    - Different phases in the event loop execute different types of callbacks.
    - `nextTick` is the microtask
    - `nextTick` is prioritized over-promise.
    - `console.log`, `JSON.parse`, and `stringify` are synchronous, use them in `setTimeOut` whenever possible.
    - Should not use `nextTick` as it blocks event loop phase `poll` as those are needed for handling network requests.
    - Heavy-duty tasks to be forwarded to the worker thread so it does not block the current looping thread.
    - The requiring module is synchronous and should be done at the root level.

![](./screen/Event%20Loop%20Phases.png)

``` js

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
// into the event loop's poll phase queue before the "main" synchronous part
// of the this code finishes.
for (let i = 1; i <= 10000000000; i++) {}

console.log(`END`);
// So when the event loop starts its first tick there should be two callbacks
// waiting:
//   (1) the readFileCallback (in the poll queue)
//   (2) the setImmediateCallback (in the check queue)
// Now according to the Node.js DOCs, of these two waiting callbacks
//The readFileCallback should execute first, but the opposite
// is happening, that is setImmediateCallback executes first.


// DOC

// The poll phase has two main functions:
//     1. Calculating how long it should block and poll for I/O, then
//     2. Processing events in the poll queue.

// When the event loop enters the poll phase and there are no timers scheduled,
//One of two things will happen:

//   (a)  - If the poll queue is not empty, the event loop will iterate
//         through its queue of callbacks executing them synchronously
//         until either the queue has been exhausted,
//         or the system-dependent hard limit is reached.

//   (b)  - If the poll queue is empty, one of two more things will happen:
//         - If scripts have been scheduled by setImmediate(),
//The event loop will end the poll phase and continue to the check phase
//           to execute those scheduled scripts.
//         - If scripts have not been scheduled by setImmediate(),
//The event loop will wait for callbacks to be added to the queue,
//           then execute them immediately.

// Once the poll queue is empty the event loop will check for timers
// whose time thresholds have been reached. If one or more timers are ready,
//The event loop will wrap back to the timers phase
// to execute those timers' callbacks.

```

``` js

// observer to watch an element with reference

const observer = new IntersectionObserver(
 handleIntersection,
 observerConfig
);
```

- ES6 vs CommonJS Import Export
    - [Module exports vs export default](https://stackoverflow.com/questions/40294870/module-exports-vs-export-default-in-node-js-and-es6)

- Addons
    - Native C++ to be used in require

### References
- [Javascript Foundation](https://github.com/farnaz-kakhsaz/Deep-JavaScript-Foundations/blob/master/README.md)
- [Module System](https://auth0.com/blog/javascript-module-systems-showdown/)