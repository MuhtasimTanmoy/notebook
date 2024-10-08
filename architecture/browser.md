# Browser Architecture

Rendering steps for a browser
- Constructing the `DOM` Tree
    - byte
    - character
    - token
    - node
    - dom
- Constructing the `CSSOM` Tree
- Running JavaScript
- Creating the render tree
- Generating the layout
- Painting

### JS
- Javascript
    - Parsing
    - Compile + Optimize
    - Reoptimize
    - Execute
    - Garbage collection
- JS 
    - Abstract Syntax Tree
    - Bytecode

- JS engine comes with `JIT`, Garbage collector
- Runtime, the pieces of code language add that you don't write. ( translation cost occurs one )

### Interpretation and compilation
- Compiled is fast interpreted is repeated
- Compilers can optimize ahead as they have the full picture
- Interpreters in js introduced monitor warm functions
- Stub > Chunks > += with similar datatypes on both side
eventually optimizing translation time

### Notes
- Polyfill backward compatibility
- Performance Measure
    - Critical rendering path optimize
    - Time to first meaningful paint

### References
- [Anatomy of the browser 101 (Chrome University 2019)](https://www.youtube.com/watch?v=PzzNuCk-e0Y&list=RDCMUCnUYZLuoy1rq1aVMwx4aTzw&start_radio=1&ab_channel=GoogleChromeDevelopers)

- Architecture Core Principles
    - Stability
    - Security
    - Speed
    - Simplicity

- Multi-process makes sure
    - Stability
    - Security
    - Speed
    
- To ensure multiprocess
    - IPC 
        - Inter-Process Communication
    - Message Passing for short objects, shared memory for larger.
    - Every process has different privileges, so needs security review.
    - These processing must be asynchronous.
    - As untrusted code runs, `sandboxing` is required.

- Split into components
    - iOS support, blink replacements
    - the extension has a different process
    - Mojo for IPC 

- Directory Structure
    - base: platform independent helper classes and utilities, e.g. task posting, file access, string manipulations
    - chrome: Chrome desktop & Android Ul, browser features not shared with iOS
    - components: browser features shared with iOS
    - content: multi-process sandboxed browser platform
    - ios: our iOS browser
    - net: networking library
    - services: microservices
    - third_party/Blink: Blink rendering engine
    - UI: user interface frameworks, helper classes
    - v8: JavaScript engine

- [Life of a pixel](https://www.youtube.com/watch?v=m-J-tbAlFic&ab_channel=GoogleChromeDevelopers)

- WebContents
    - The rendered page
    - Sandboxed renderer process
    - `Content` gets converted to `pixel`.
    - Content
        - HTML
        - CSS
        - JS
        - Image
    - Graphics Library
        - OpenGL
        - `DirectX` for windows
        - Vulkan - Next generation Open GL
    The overall goal of rendering is to turn HTML, CSS, and JavaScript into the right OpenGL call.
        - Dom
        - Style
        - Layout
        - Paint
        - Raster
        - GPU