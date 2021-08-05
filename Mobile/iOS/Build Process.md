# Build Process

- Build process represented as Directed Graph
    - Takes `xcodeproj` as build description
- Each task has signature, changes only when modified.
- Framework gets embedded in app binary, need to build for each platform.
- `XCFramework` binary distiribution.
- Keep interface simple and least extensible, easy to add, hard to remove
- Can make functions and variables `inlinable` for performance. But once done cant change it. Also `@frozen` enums.
- `Header maps` are used to communicate info from build system to clang compiler
- `Clang` mudules to spped up build
- Can write defaults
    - `defaults write com.apple.dt.Xcode ShowBuildOperationDuration -bool YES`

# Resources
- [Build System Xcode](https://github.com/apple/swift-llbuild)
- [Binary Framework Talk](https://developer.apple.com/videos/play/wwdc2019/416/)