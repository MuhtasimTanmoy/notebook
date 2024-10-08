# Build Process

- Build process represented as a Directed Graph.
    - Takes `xcodeproj` as the build description.

- Each task has a signature and changes only when modified.

- Framework gets embedded in app binary, which needs to be built for each platform.

- `XCFramework` binary distribution.

- Keep interface simple and least extensible, easy to add, hard to remove.

- Can make functions and variables `inlinable` for performance. But once done can't change it. Also `@frozen` enums.

- `Header maps` are used to communicate info from the build system to the clang compiler.

- `Clang` modules to speed up the build.

- Compilers run different sorts of optimization to 

- Can write defaults
    - `defaults write com.apple.dt.Xcode ShowBuildOperationDuration -bool YES`

- `Bitcode` is llvm `IR`. We upload it to the app store which runs `llvm-backend` itself and it generates built for all available platforms. `Fat Binary` is removed. Any llvm optimization fix can run itself.

- pod plugins list

- There are two types of linking: static, and dynamic.
    - A dynamic framework is a dynamic library embedded in a bundle.
    - Umbrella Header

- Can fake [bitcode](https://stackoverflow.com/questions/64768561/what-is-the-point-of-marker-bitcode-fembed-bitcode-marker/64898439) in debug app.
- marker only mode is used to speed up the compilation while still producing enough information in the final output to check if all the files contain a bitcode section. `-fembed-bitcode` option will split the compilation into two stages and add measurable costs to compile time due to the extra process launch, the serialization and the verifier. `-fembed-bitcode-marker` is just a way to avoid that costs but still mark the section for the sanity check later (done by the linker in our case).

> -fembed-bitcode option which breaks down the compilation into two stages. The first stage emits optimized bitcode and the second stage compiles bitcode into object file.

> -fembed-bitcode-marker option which doesn't break down into two stages to speed up the compilation flow.


- debug info
    - Mapping source to binary in debuggers, profilers, editors
    - Can be used for code auto-completion
    - Dwarf 
        - Standard for debugging information
        - Interchange format generated by gcc, clang, icc, consumed by gdb, lldb, profilers

- Auto delete the unused import
``` shell
xcodebuild -workspace internalize.xcworkspace -scheme MY_SCHEME -configuration Debug > xcodebuild.log
swiftlet analyze --fix --compiler-log-path xcodebuild.log
```

### References
- [Build System Xcode](https://github.com/apple/swift-llbuild)
- [Binary Framework Talk](https://developer.apple.com/videos/play/wwdc2019/416)
- [Dynamic Library](https://pewpewthespells.com/blog/static_and_dynamic_libraries.html)
- [dyld](https://www.youtube.com/watch?v=p-dvAOHlLEc)
    - Static library can save time loading dynamic libs
    - When used with an extension can create duplicate
    - Own library can be static
    - Debug build runs libMainThreadChecker which gives called from diff thread warning
    - dyld
        - load all dependent lib
        - rebase all dylib image
            - read entire data pages
            - copy on write
        - bind all dylib image
            - detect symbols, load all dependant libs, resolve
            - Position Independent code, data keeps address, text segment keeps stub, abstraction
        - prepare objc runtime
        - run initializer
- [Xcode Documentation](https://developer.apple.com/documentation/xcode)