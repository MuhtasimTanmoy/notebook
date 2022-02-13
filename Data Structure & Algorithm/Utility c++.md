**Bitset**

- Bitset
    - bitset<10> s(string("0010011010")

- vector
    - `std::vector` has a capactiy (the total slots that can be used) and a `size` (the number of slots actually used).

    - reserve() will increase the capacity, i.e. make room for more elements, but it will not increase the size. 
    - That's the job of resize():
        - vec.reserve(1); // capacity >= 1, size = 0!

    - Access to a vector is out of bounds if the index is >= the vector's size, irrespective of it's capacity, thus
        - vec[0] = std::make_shared<A>(); is out of bounds and leads to undefined behaviour. (index 0 >= size 0)

