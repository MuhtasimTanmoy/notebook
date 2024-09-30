# React

There are 3 possibilities to store state:
- Component
    - Class-Based Component
    - Functional Component
- Context API
- Redux

- Component (useState) when the state is local or it is shared with only children.

- When it is very localized and makes sense to do it, then going for Context API makes a lot of sense.

- When state is shared among far away parts of the program, then Redux makes more sense.

- Talking about performance, I also once read someone saying "Redux for high-frequency (>1 second) state changes, Context API for low-frequency changes".

- React platform agnostic converter js objects
- React dom renderer
- Execution Context

- React uses a javascript object tree, runs diffing every time anything changes, and ensures minimum dom manipulation.