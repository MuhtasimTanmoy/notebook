# Elements of programming Interview
(Page - 58 )

- The number of set bits
    - O(n)
    - Check by bitmask.
    - Can be done only by removing last set until it becomes zero.


- The last set bit in a number
    - `y = x & ^ ( x - 1 )`

- Set last set bit to zero in a number
    - `y = x & ( x - 1 )`

