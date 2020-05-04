# Browser architecture

Rendering Steps
- Constructing the DOM Tree
- Constructing the CSSOM Tree
- Running JavaScript
- Creating the Render Tree
- Generating the Layout
- Painting


# JS
- Javascript > parsing > compile+optimize > reoptimize > execute > garbage collection
- JS > Abstract Syntax Tree > Bytecode
- JS engine comes with jit, garbage collector
- Runtime the stuff language put that u actually dont wrote. ( translation cost occurs one )

# Interpretation & Compilation
- Compiled is fast Interpreted is repeated.
- Compilers can optimize ahead as they have full picture.
- Interpreters in js introcuded monitor warm functions.
- Stub > Chunks > += with similar datatypes on both side
eventually optimizing translation time.

## Notes
- Polyfill backward compatibility
- Perforamnce Measure
    - Critical rendering path
    - First meaningful paint


