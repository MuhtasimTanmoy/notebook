# Snippet

```swift
class Foo: CustomStringConvertible, CustomDebugStringConvertible {
    let name = "Lucas"
    let age = 25
    
    var description: String {
        return "Foo Description"
    }
}

extension CustomDebugStringConvertible {
    var debugDescription: String {
        let className = type(of: self)
        let address = "\(Unmanaged.passUnretained(self as AnyObject).toOpaque())"
        var description = "<\(className): \(address), {"
        
        let mirror = Mirror(reflecting: self)
        description += mirror.children.compactMap {
            let (label, value) = $0
            guard let propertyName = label else { return nil }
            return "\(propertyName): \(value)"
        }.joined(separator: ", ")
        
        description += "}>"
        
        return description
    }
}

let foo = Foo()

print(foo)
debugPrint(foo)
```