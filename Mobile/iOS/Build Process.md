# Build Process

- Build process represented as Directed Graph.
    - Takes `xcodeproj` as build description.

- Each task has signature, changes only when modified.

- Framework gets embedded in app binary, need to build for each platform.

- `XCFramework` binary distiribution.

- Keep interface simple and least extensible, easy to add, hard to remove.

- Can make functions and variables `inlinable` for performance. But once done cant change it. Also `@frozen` enums.

- `Header maps` are used to communicate info from build system to clang compiler.

- `Clang` mudules to speed up build.

- Compilers run different sort of optimization to 

- Can write defaults
    - `defaults write com.apple.dt.Xcode ShowBuildOperationDuration -bool YES`

- `Bitcode` is llvm `IR`. We upload it to app store which runs `llvm-backend` itself and it generates built for all available platforms. `Fat Binary` is removed. Any llvm optimization fix can run itself.

- pod plugins list

- There are two type of linking: static, and dynamic.
    - dynamic framework is a dynamic library embedded in a bundle.
    - Umbrella Header

- Can fake [bitcode](https://stackoverflow.com/questions/64768561/what-is-the-point-of-marker-bitcode-fembed-bitcode-marker/64898439) in debug app.
- marker only mode is used to speed up the compilation while still producing enough information in the final output to check if all the files are containing a bitcode section. -fembed-bitcode option will split the compilation into two stages and it adds measurable costs to compile time due to the extra process launch, the serialization and the verifier. -fembed-bitcode-marker is just a way to avoid that costs but still mark the section for the sanity check later (done by linker in our case).

> -fembed-bitcode option which breaks down the compilation into two stages. The first stage emits optimized bitcode and the second stage compiles bitcode into object file.

> -fembed-bitcode-marker option which doesn't really break down to two stages to speedup the compilation flow.


# Resources
- [Build System Xcode](https://github.com/apple/swift-llbuild)
- [Binary Framework Talk](https://developer.apple.com/videos/play/wwdc2019/416)
- [Dynamic Library](https://pewpewthespells.com/blog/static_and_dynamic_libraries.html)
- [dyld](https://www.youtube.com/watch?v=p-dvAOHlLEc)
    - Static library can save time loading dynamic libs
    - When used with extension can create duplicate
    - Own library can be static
    - Debug build runs libMainThreadChecker which gives called from diff thread warning
    - dyld
        - load all depnedant lib
        - rebase all dylib image
            - read wtire data pages
            - copy on write
        - bind all dylib image
            - detect symbols, load all dependant libs, resolve
            - Position Inndependent code, data keeps address, text segment keeps stub, abstraction
        - prepare objc runtime
        - run initializer