# Lambda

```c++
template<typename T>

T function(T x) {
    return x + 1;
}

class Plus {
    int value;

    public: 
    Plus(int v);

    int plusme(int v) const {
        return value + v;
    }

    int operator()(int v) const {
        return value + v;
    }
}

// Above class can be written as
auto plus = [x = 1] (int v) { return x + v; };

[&] (int v) { // Most useful }

[x=0] () mutable { return ++x; };

// Template
[value =1] (auto x) { return value + x; };

// variable on stack pointing to heap
auto plus = Plus();

// heap pointing to vtable through vptr. Not by default. By making one or methods virtual.
plus.plusMe(42);


// closure 
class Plus {

    int value;

    public: 
    Plus(int v);

    int plusme(int v) const {
        return value + v;
    }

    template<class... As>
    auto operator()(As... as) const {
        return sum(as..., value)
    }
}

auto plus = [value = 1] (auto... as) {
    return sum(as..., value);
};

// This inside lambda refers to the outer object
```


- Notes
    - The move constructor is used instead of the copy constructor, if the object has type "rvalue-reference" (Type &&).

# Reference
- [lambda from scratch](https://www.youtube.com/watch?v=3jCOwajNch0)
 

