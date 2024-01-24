# Browser Architecture

Rendering Steps for a browser
- Constructing the `DOM` Tree
    - byte
    - character
    - token
    - node
    - dom
- Constructing the `CSSOM` Tree
- Running JavaScript
- Creating the Render Tree
- Generating the Layout
- Painting

# JS
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
- Runtime the stuff language put that you actually dont wrote. ( translation cost occurs one )

# Interpretation and compilation
- Compiled is fast interpreted is repeated
- Compilers can optimize ahead as they have full picture
- Interpreters in js introduced monitor warm functions
- Stub > Chunks > += with similar datatypes on both side
eventually optimizing translation time

## Notes
- Polyfill backward compatibility
- Perforamnce Measure
    - Critical rendering path optimize
    - Time to first meaningful paint

# Resources
- ### [Anatomy of the browser 101 (Chrome University 2019)](https://www.youtube.com/watch?v=PzzNuCk-e0Y&list=RDCMUCnUYZLuoy1rq1aVMwx4aTzw&start_radio=1&ab_channel=GoogleChromeDevelopers)

- Architecture Core Principles
    - Stability
    - Security
    - Speed
    - Simplicity

- Multi process makes sure
    - Stability
    - Security
    - Speed
    
- In order to ensure multiprocess
    - IPC 
        - Inter Process Communication
    - Message Passing for short objects, shared memory for larger.
    - Every process has different priviledges, so need security review.
    - These processing must be asyncronous.
    - As untrusted code runs, `sandboxing` required.

- Splitted into components
    - iOS support, blink replacements
    - extension has different process
    - Mojo for IPC 

- Directory Structure
    - base: platform independent helper classes and utilities, e.g. task posting, file access, string manipulations
    - chrome: Chrome desktop & Android Ul, browser features not shared with iOS
    - components: browser features shared with iOS
    - content: multi-process sandboxed browser platform
    - ios: our iOS browser
    - net: networking library
    - services: micro services
    - third_party/Blink: Blink rendering engine
    - ui: user interface frameworks, helper classes
    -  v8: JavaScript engine

- [Life of a pixel](https://www.youtube.com/watch?v=m-J-tbAlFic&ab_channel=GoogleChromeDevelopers)

- WebContents
    - The rendered page
    - Sandboxed renderer process
    - `Content` gets converted to `pixel`.
    - Content
        - HTMl
        - CSS
        - JS
        - Image
    - Graphics Library
        - OpenGL
        - `DirectX` for windows
        - Vulkan - Next generation Open GL
    - Overall goal of rendering is to turn html, css, javascript inot right opengl call.
        - Dom
        - Style
        - Layout
        - Paint
        - Raster
        - Gpu