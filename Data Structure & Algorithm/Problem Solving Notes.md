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


- Rotate Array

```c++

// Extra Space
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        
        vector<int> cache = nums;
        auto swapWithOffset = [&](int first) {
            int num = cache[first];
            int replaceToIndex = (first + k ) % nums.size();
            nums[ replaceToIndex ] = num;
        };
        
        for( int i = 0; i< nums.size(); i++) {
            swapWithOffset(i);
        }
    }
};


// Cut the last part and reinsert
vector<int> temp = vector<int>(nums.begin() + n - k % n, nums.end()); 
//modulus handles k>n and subtract by n for last k elements
if(k%n) nums.resize(n - k % n );
nums.insert(nums.begin(), temp.begin(), temp.end());  
//insert temp in the beginning of nums  


// No Space
// Use rotation, the last part will be first anyway

supporse, k = 2
- Data: 1,2,3,4,5,6,7
- Full Reverse: 7,6,5,4,3,2,1
- Reverse 0 to k-1: 6,7 ...
- Reverse k to arr.length-1 : 1,2,3,4,5
- Rotated arr = 6,7,1,2,3,4,5

```


- Contain Duplicate and their index in certain range
    - Can think in two dimensions, sort using one, check index
```c++
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {

        map<int, vector<int>> m;

        for(int i=0; i < nums.size(); i++ ) {
            int occuranceCount = m[nums[i]].size();
            if (occuranceCount) {
                // Extracting the last index inserted
                int k1 = m[nums[i]][occuranceCount-1];
                
                if ( (i - k1) <= k ) return true;
            }
            m[nums[i]].push_back(i);
        }
        return false;
    }
};

```
- Occurence of number count
    - Map it in different dimension, the 32 bit pattern addition for all numbers, then count occurence.

- Access a vector by & to get reference

- Can substitute map with `vector<int>freq2(1001,0)`
    - In case the input space is less.
    - Efiicien as `nlogn` avoided but memory additional.

- Power of two invalid for negative number.

- isPowerOfTwo 
```
    !(n & n-1)
````
- isPowerOfN

```c++
    if( n > 1 )
        while( n % 3 == 0 ) n /= 3;
    return n == 1;
```

- In case of alternating bit

```c++

// My approach was totally bit based to shift and check
// bulitin_clz will count leading zero
// builtin_ctz will last zero
// builtingpopcount qill count one with more speed

bool hasAlternatingBits(int n) {
    int curr = n & 1;
    n >>= 1;
    while(n>0)
    {
        if(curr == (n&1))
            return false;
        curr=n&1;
        n >>= 1;
    }
    return true;
}

```


- All SubSet

```c++

void allSubSet(vector<int>& nums, 
            vector<int> current,
            int index,
            vector<vector<int>>& subsets) {
    
    if (index == nums.size()) { 
        subsets.push_back(current);
        return;
    }
    
    allSubSet(nums, current, index + 1, subsets);
    current.push_back(nums[index]);
    allSubSet(nums, current, index + 1, subsets);
    current.pop_back();
}

vector<vector<int>> subsets;
vector<int> current;
allSubSet(nums, current, 0, subsets);

```

- Nth element
```c++

nth_element(nums.begin(), 
nums.begin() + nums.size()/2, 
nums.end());

```


- Efficient power

```c++
 double myPow(double x, int n) {
        
        bool isNeg = n < 0;
        n = abs(n);
        
        if ( n == 0 ) { return 1; }
        if ( n == 1 ) { return 1; }
        
        double result = 1;
        
        while( n ) {
            if ( n % 2 ) {
                result *= x;
                n--;
            } else {
                x *= x;
                n = n >> 1; 
            }
        }
        
        if ( isNeg ) {
            result = 1 / result;
        }
        
        return result;
    }

```