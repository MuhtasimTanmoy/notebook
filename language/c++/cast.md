# Cast

## Type Cast

- Static Cast

```c++

// Used to explicitly find out if casted
a = f;
a = static_cast<int>(f);

// Conversion construtor
// Conversion operator
class Int {
    int x;
public:
    Int(int x=0) {
        cout << "conversion constructor" << endl;
    }
    operator string ( ) {
        cout << "conversion operator" << endl;
        return to_string(x);
    }
}

int main() {
    Int obj(3);

    // Compile time casting 
    string str = obj;
    obj = 20;
}


// Prevents char to int type cast at compile time
// In every case provides better security than c style (void *) cast

// For compatible type conversion, such as float to int.
// For conversion operator and conversion constructors.
// To avoid unrelated pointer conversion.
// Avoids derived to private base pointer conversion.
// Use for all up-cast but never use for confused down-cast because there are no runtime checks performed
// Intensions are more clear in C++ style cast (express your intent better and make code review easier)
// Finding is easy.
//  Error found at compile-time.
```

- Const Cast 
    - To remove const, volatile
    - When a third party library is taking a `non-const` param and not changing it

 - Dynamic Cast
    - In order to use it, must have `virtual function` in base class.
    - Work only on polymorphic base class (at least one virtual function in base class) because it uses this information in runtime to decide about wrong down-cast
    - It is used for up-cast (D to B) and down-cast (B to D), but it is mainly used for correct downcast
    - Using this cast has run time overhead, because it checks object types at run time using `RTTI` (Run Time Type Information)
    - If we are sure that we will never cast to wrong object then we should always avoid this cast and use `static_cast`
    - Cast from parent to correct leaf is successful