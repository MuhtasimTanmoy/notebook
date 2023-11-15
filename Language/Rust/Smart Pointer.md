# Smart pointer

- `unique_ptr`
    - Use it for exclusive ownership resource management
    - When we are done with heap allocation we need to call delete, the destructor of unique_ptr  does that for us.
    - Rust owership is basically transferring `unique_ptr` because if it is copyable, and two pointer reference to same address, it is unclear who may have the responsibility to clear it
    - It is `move` only, makes ownership clearer
    - Smart pointer should be treated like regular pointer, pass by value, return by value. 8 byte.

```c++

template<class T, class Deleter = std:: default_delete<T>>
class unique_ptr {
    T *p_ = nullptr;
    Deleter d_;

    ~unique_ptr() {
        if (p_) d_(p_);
    }
}

template<class T>
struct default_delete {
    void operator()(T* p) const {
        delete p
    }
}

// Need to override default close function

struct FileCloser {
    void operator()(FILE *fp) const {
        if (fp !=  nullptr) {
            fclose(fp);
        }
    }
}

FILE *fp = fopen("INPUT.txt", "r");
std :: unique_ptr<FILE, FileCloser> uptr(fp);

```
- shared_ptr
- weak_ptr

# Resources
- [Smart Pointer](https://github.com/CppCon/CppCon2019/blob/master/Presentations/back_to_basics_smart_pointers/back_to_basics_smart_pointers__arthur_odwyer__cppcon_2019.pdf)