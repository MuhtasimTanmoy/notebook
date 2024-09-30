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

// variable on stack pointing to the heap
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

// Similar Lambda function
struct {
    int operator()(int n) const {
        return n < 2 ? 1 : n * (*this)(n-1);
 }
} fact;
return fact(5);

// [ capture_list ]( argument_list ) -> return_type { code }

// Corresponds to
struct some_anonymous_type {
 // capture_list turned into member variables
  some_anonymous_type( /* capture_list turned into arguments */ ):
 /* member variables initialized */
 {}
  return_type operator()( argument_list ) const {
 code
 }
};

// This inside lambda refers to the outer object
```
- Notes
    - The move constructor is used instead of the copy constructor if the object has type "rvalue-reference" (Type &&).

### References
- [lambda from scratch](https://www.youtube.com/watch?v=3jCOwajNch0)
- [Print variable type in C](https://stackoverflow.com/questions/81870/is-it-possible-to-print-a-variables-type-in-standard-c)