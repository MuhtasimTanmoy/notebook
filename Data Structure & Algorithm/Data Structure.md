# Data Structure


## Priority Queue
Whenever dynamically need to fetch next best or worst variant.
 
Min Queue to Max Queue Conversion
- Just negate the values
- Indexed Priority Queue

Usage
- Huffman Encoding
- BFS A*
- Minimum Spanning Tree
- Polling Adding ( logn )
- Naive Removing ( n )

---

## Union Find

Usage
- Kruskal's minimum spanning tree
- Grid Percolation
- Network Connectivity
- Least common ancestor in tree

---
##  Binary Search Tree

Usage
- Set
- Red Black Tree
- AVL Tree
- Splay Tree
- Binary Heap
- Syntax Tree
- Treap

---

## Tree Traversal
- Level order traversal

---

## Hash Collision

- Linear Probing Good
    - (aX + b ) % N 
    - Relatively Prime

- Linear quadratic 
- Double hash
- To handle deletion use tombstone marker

---

## Suffix Arrays

Given a string S, find the longest repeated sub string that occurs at least M times.

Approach -
- Just get in a struct and compare string ( n^2 * logn )
- o(nlogn) even o(n) algo available

- Generate all sub string > O(n^2) >  KMP > search
- Binary O(n) hash calc > O(N (log(N))^2) > logn times N calc > hash logn

- Find all unique substring 
	- Generate all in o(n^2) and dump them inside set
	- (all substring - sum of lcp)
- Longest substring in k strings
	- LCP will give match in correct order
	- Get less ascii characters to contain the string then LCP 
- Suffix array can do anything suffix tree can

- [Suffix Array](https://www.hackerearth.com/practice/data-structures/advanced-data-structures/suffix-arrays/tutorial/)

A compressed representation of indexes sorted lexicographically.
Longest Common Prefix Array - LCP array


## Queries
- If the problem involve processing queries then there are online solutions and offline solution.
    - Online means that your solution can process each query as it reads it.
    - Offline means that your solution reads all queries then process them, probably you sort the queries in some order so that you can process them faster.


# Mo's Algorithm
- You are given array Arr of length N and Q queries. Each query is represented by two numbers L and R, and it asks you to compute some function Func with subarray Arr[L..R] as its argument.

- O((N + Q) * sqrt(N) * F)
- All queries are known beforehand (techniques requiring this property are often called “offline algorithms”);
- https://github.com/gkcs/Competitive-Programming/blob/master/src/main/java/main/java/videos/DQUERY.java
- https://www.hackerearth.com/practice/notes/mos-algorithm/
- In the Eventual


## FENWICK TREE

All operations ( logn )

Usage
- Update
- Range Sum

# Segment Tree

All operations ( logn )

Usage
- Update
- Range Sum
- Min
- Max


## Kruskal

## Prim and Dijsktra same



