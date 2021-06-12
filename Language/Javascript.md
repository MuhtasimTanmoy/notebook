# JavaScript

- One app, one thread, one event loop, turns application into multitreaded
- The syncronous logic gets executed first, require modules as well
-  

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

```

# Resources
- [Javascript Foundation](https://github.com/farnaz-kakhsaz/Deep-JavaScript-Foundations/blob/master/README.md)