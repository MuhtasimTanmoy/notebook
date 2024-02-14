# Bloom Filter

A Bloom filter is a space-efficient probabilistic data structure that is used to test whether an element is a member of a set.

For example, checking availability of username is set membership problem, where the set is the list of all registered username.

- Algorithm
    - Each item hashed to multiple index. If all index are set the element is present. If not then certainly not present.

- Probabilistic data structures will give you memory-efficient, faster result with a cost of providing a `probable` result instead of a `certain` one
- Suitable for data that needs no deletion
- A Bloom filter is an inexact representation of a set that allows for false positives when queried; that is, it can sometimes say that an element is in the set when it is not
- Bloom filter can check for if a value is **‘possibly in the set’** or **‘definitely not in the set’**
- You might already understand that if the size of the bloom filter is too small, soon enough all of the bit fields will turn into ‘1’ and then our bloom filter will return ‘false positive’ for every input. So, the size of the bloom filter is a very important decision to be made. 
- A larger filter will have less false positives, and a smaller one more. So, we can tune our bloom filter to how much precise we need it to be based on the ‘false positive error rate’

- False positive result
    - Good
    - Can recheck

- False negative
    - Bad 
    - No recheck

- Counting bloom filter
    - Instead of 1 require count

We can calculate the false positive error rate, **_p_**, based on the size of the filter, **_m_**, the number of hash functions, **_k_**, and the number of elements inserted, **_n_**, with the formula:

```
(1 - e ^ - (k * n) / m ) ^ k
```


## Usage
- Apache Cassandra uses SSTable
- Used in postgres for query optimization
- In order to skip the recommendations that are already served to you, bloom filters are used.
- Avoid caching the items that are very rarely searched or searched only once. Only when they are searched more than once, they will get cached.

## HyperLogLog
- Approximation: Number of zeros at end, N then 2^N
- Use bucket, 70% average.

## Resources
- [Bloom Filter](https://hackernoon.com/probabilistic-data-structures-bloom-filter-5374112a7832)
- [Murmur Hash Function](https://sites.google.com/site/murmurhash/)
- [FNV Hash Function](http://isthe.com/chongo/tech/comp/fnv/)
- [HashMix Hash Function](http://www.google.com/codesearch/url?ct=ext&url=http://www.concentric.net/~Ttwang/tech/inthash.htm&usg=AFQjCNEBOwEAd_jb5vYSckmG7OxrkeQhLA)