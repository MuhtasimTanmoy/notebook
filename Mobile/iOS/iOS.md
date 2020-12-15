# iOS

- Hardware
- Core OS
- Core Services
- Media
- Cocoa Touch > UIKit
- Applications

- ### Protocol
A protocol in Swift is an interface that provides specific methods. 
Any object conforms to that protocol must implement the given set of functions.
 “A protocol defines a blueprint of methods, properties, and other requirements that 
 suit a particular task or piece of functionality. 

- ### Lazy var
Swift has a mechanism built right into the language that enables 
just-in-time calculation of expensive work, and it is called a **_lazy variable_**.
A lazy stored property is a property whose initial value is not calculated until 
the first time it is used. You indicate a lazy stored property by writing the `lazy` modifier 
before its declaration.


```swift
lazy var iOSResumeDescription: String = {
    return "I am an iOS developer"
}()
```

- ### Closure
Functions are actually a special case of closures: blocks of code that can be called later. 
The code in a closure has access to things like variables and functions that were available 
in the scope where the closure was created, even if the closure is in a different scope when
 it is executed. You can write a closure without a name by surrounding code with 
 braces (`{}`). Use `in` to separate the arguments and return type from the body.

- ### ARC
ARC is a compile time feature that is Apple's version of automated memory management. 
It stands for  _Automatic Reference Counting._ This means that it  **_only_**  frees up memory 
for objects when there are  **_zero strong_**  references to them.


```swift
collectionView.reloadItemsAtIndexPaths(collectionView.indexPathsForVisibleItems())
```

- ### NotificationCenter
    - When communication between two or more components of your app, that have no formal connection, needs to happen
    - When communication needs to happen repeatedly and consistently
    - When using one-to-many or many-to-many communication


# Resources
- [Swift Style Guide](https://google.github.io/swift/#global-constants)    