# Problem Solving Notes

- Divide and Conquer design pattern.
- Rote learning will lead to perfect solution to wrong problem.

![](./Screen/Interview%20Guide.png)


- Google `c++` Style Guide
    - Input arguments to functions are either values or const references. 
    - Never allow non-const references.



# Takeaways

- For `palindrome` findings.
    - switch to an index, then go both ways.
    - Otherwise, many more possible way to go.

```c++

auto getlength = [&] ( int l, int r) {
        while (  l >= 0 && r < length && s[l] == s[r]  ){
            -- l;
            ++ r;
        }
        return r -l - 1;
        };

int current_pallindrome = max( getlength(i, i), getlength(i, i+1) );

if ( current_pallindrome > longest_pallindrome) {
        longest_pallindrome = current_pallindrome;
        start = i - (longest_pallindrome -1) /2;
}

```


- For longest non repeating substring
    - Keeping `char` to `index` mapping.

- Two Sorted array traversal

```c++

int num1Index = 0;
int num2Index = 0;

auto extractNext = [&]() -> int {
    
    if (num1Index >= nums1.size()) {
        num2Index++;
        return nums2[num2Index - 1];
    }
    
    if (num2Index >= nums2.size()) {
        num1Index++;
        return nums1[num1Index - 1];
    }
    
    if (nums1[num1Index] <= nums2[num2Index]) {
        num1Index++;
        return nums1[num1Index - 1];
    } else {
        num2Index++;
        return nums2[num2Index - 1];
    }
};
```

- Reverse while checking INT_MAX, INT_MIN

```c++

INT_MAX = 2147483647

INT_MIN = -2147483648

int num = neg_num % 10 // gives negative
```

- Number Pallindorme

```c++
int reversed = 0;

// Reverses the whole number. But can cause INT_MAX error.
while(x) {
    reversed = reversed * 10 + x % 10;
    x = x / 10;
}

// It is solved by this.
bool isPalindrome(int x) {
        if ( x < 0 || ( x % 10 == 0 && x != 0)) {
            return false;
        }

        int reversed = 0;
        while(x > reversed) {
            reversed = reversed * 10 + x % 10;
            x = x / 10;
        }
        
        return x == reversed || x == reversed / 10;
    }
```
- 

