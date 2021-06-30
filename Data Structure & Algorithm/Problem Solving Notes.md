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

<br/>

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

<br/>

- Reverse while checking INT_MAX, INT_MIN

```c++

INT_MAX = 2147483647

INT_MIN = -2147483648

int num = neg_num % 10 // gives negative
```

<br/>

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
<br/>

- Jump Game ||
    - Use DP

<br/>

- Pattern Searching
    - `KMP Algorithm O(n)`

<br/>

- Prime Factorization

```c++
// Generating for 1000 numbers


// input should be root of n
bool[] generateSieve(int n) {
    bool isPrime[n + 1];
	memset(isPrime, true, sizeof(isPrime));
	for ( int i = 2; i * i <= n; i++ ) {
		if ( isPrime[i] ) {
			for(int p = i * i; p <= n; p += i) {
				isPrime[p] = false;
			}
		} 
	}
    return isPrime;
}

auto getPrimeFactors = [&](int n) -> vector<int> {
    vector<int> primeFactors;

    for(int i = 2; i * i <= n; i+=1 ) {

        if ( n % i == 0 ) {
            
            if (isPrime[i]) {
                primeFactors.push_back(i);
            }

            if (isPrime[n / i]) {
                primeFactors.push_back(n / i);
            }
        }
    }

	return primeFactors;
};



```
