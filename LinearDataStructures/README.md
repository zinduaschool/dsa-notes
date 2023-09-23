# Hash Tables
A **hash table** (hash map) is a data structure which implements an _associative array_ abstract data type, a structure that can _map keys to values_. It uses a _hash function_ to compute an index into an array of buckets or slots, from which the desired value can be found.<br>Ideally, the hash function will assign each key to a unique bucket, but most hash table designs employ an imperfect hash function, which might cause hash collisions where the hash function generates the same index for more than one key. Such collisions must be accommodated in some way.

- Hash collision resolved by separate chaining.
- The size of the object directly affects on the number of collisions occurrence.
- The bigger the hash table size the less collisions you'll get.
- For demonstrating purposes hash table size is small to show how collisions are being handled.

<hr>

![](https://img.shields.io/static/v1?label=&message=💡Overview:&color=orange)
<br>

Hashing is the most common example of a space-time tradeoff(better than array). Instead of linearly searching an array every time to determine if an element is present, which takes O(n) T. We can traverse the array once and hash all the elements into hash table. Accessing the values is O(1) time.

<hr>

### Definition
  - It’s a data structure that implements an associative array abstract data type.
  - A map uses a hash function on an element to compute an index(hashcode), into an array of buckets/slots where a desired value can be found

<hr>

### Operations
  
| Access | Lookup | Insert | Deletion |
|:------:|:------:|:------:|:--------:|
|   n/a  |  O(1)  |  O(1)  |   O(1)   |

* **Access** : When accessing an element, you use its key to compute the index in the array where it is stored, and then retrieve the value at that index
* **Lookup** : To look up an element, we use its key to compute the index in the array where it is stored, and then check if an element exists at that index.
* **Insert** : To insert up an element, we use the key to compute the index in the array where it sould be stored, and then insert the key-value pair at that index
* **Deletion** : To insert up an element, we use the key to compute the index in the array where it's stored, and then remove the key-pair from that index

> To **Note**: Hash tables are efficient for insertions, deletions and lookups. The average time complexity for the operations is constant O(1)

<hr>

**Disadvantages of using Hash Tables**
  
  * **_Collisions_**
  * **_Separate chaining_** - A linked list in used for each value, so that it stores all the collided items
  * **_Open addressing_** - All entry records are stored in the bucket array itself. When a new entry has to be inserted, the buckets are examined, starting with the hashed-to slot and proceeding in some probe sequence until an unoccupied slot is found.
  
 See more on how to solve collision [here](https://en.wikipedia.org/wiki/Hash_table)

 <hr>
 
### Resources (to help better understand maps)
  1. [Taking hash tables off the shelf](https://medium.com/basecs/taking-hash-tables-off-the-shelf-139cbf4752f0)
  2. [**Hashing out functions**](https://medium.com/basecs/hashing-out-hash-functions-ea5dd8beb4dd)
  3. [Hash tables: coursera](https://www.coursera.org/lecture/data-structures-optimizing-performance/core-hash-tables-m7UuP)

<hr>

### Sample General questions
  1. Describe an implementation of at least- used cache, and big-O notation of it
  2. A question involving an API’s integration with hash map where the buckets of a hash map are made up of linked lists.

<hr>

### Check below leetcode questions (to enhance understanding)
  1. [two sum](https://leetcode.com/problems/two-sum/) [solution in JavaScript](https://github.com/RWambui/Data-structure-JS-and-Psuedo/blob/main/src/leetcode/1.TwoSum.js) ![](https://img.shields.io/static/v1?label=&message=Easy&color=green)
  2. [Ransom note](https://leetcode.com/problems/ransom-note/) ![](https://img.shields.io/static/v1?label=&message=Medium&color=orange)
  3. [Group Anagrams](https://leetcode.com/problems/group-anagrams/) ![](https://img.shields.io/static/v1?label=&message=Medium&color=orange)
  4. [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) ![](https://img.shields.io/static/v1?label=&message=Medium&color=orange)
  5. [First Missing Positive](https://leetcode.com/problems/first-missing-positive/) ![](https://img.shields.io/static/v1?label=&message=Medium&color=orange)
  6. [LRU Cache**](https://leetcode.com/problems/lru-cache/) ![](https://img.shields.io/static/v1?label=&message=Medium&color=orange)
  7. [All O one Data Structure](https://leetcode.com/problems/all-oone-data-structure/) ![](https://img.shields.io/static/v1?label=&message=Hard&color=darkred)

<hr>

### References
1. [Hash Tables Explained - Coursera](https://es.coursera.org/lecture/algorithms-part1/hash-tables-CMLqa)