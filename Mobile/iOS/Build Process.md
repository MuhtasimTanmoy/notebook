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

# Resources
- [Build System Xcode](https://github.com/apple/swift-llbuild)
- [Binary Framework Talk](https://developer.apple.com/videos/play/wwdc2019/416)
- [Dynamic Library](https://pewpewthespells.com/blog/static_and_dynamic_libraries.html)