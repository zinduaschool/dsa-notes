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

# Linked Lists
A **[linked List]()** is used to represent sequential data. It is a data structure where each element is a separate object, called a [node](#node), that stores a reference  ([pointer](#pointer))to the next node in the list.<br>The node represented by value and a pointer commonly referred to as next. In js, linked lists can be implemented using objects and arrays.

<hr>

<img src="../../assets/Linked-List-Data-Structure.png" alt="Linked List example image"/>

## Types of Linked Lists
1. **Singly Linked List** : <br>Each node in the list contains a reference or a pointer to the the next node in the list. <br>The last node in the list (tail) contains a reference to null, indicating the end of the list. <br>The main disadvantage of this, is that you can only traverse the list in one direction, from the first node(head) to the last node(tail)
2. **Doubly Linked List** : <br> A doubly linked list is similar to a singly linked list, but in a ddition to a next reference(pointer), each node also has a prev pointer, which points to the previous node. <br>This allows for easier traversal in both directions and can be useful in certain types of algorithms 
3. **Circular Linked Lists** : <br> This is a variation of a singly linked list where the last node points back to the first node(head), forming a circular loop. <br>The main advantage of a circular linked list is that it allows for efficient implementation of certain algorithms such as traversing through a loop

<hr>

### Time Complexity

| Access | Lookup | Insert(at) | Deletion |
|:------:|:------:|:----------:|:--------:|
|  O(n)  |  O(n)  |    O(1)    |   O(n)   |


Access time is linear (and difficult to pipeline). Faster access, such as random access, is not feasible. Arrays have better cache locality as compared to linked lists.

<hr>

### **Basic Operations**
1. **Traverse** : 

    ```jsx
    function traverse_list(head)
    //first node of the linked list
      current = head
      //loop to iterate through the list as long as "current" is not null
      while current != null
        //print the stored in the current node using "current.data"
        print current.data
        //move current pointer to the next node by assigning "current.next" to current and the loop continues
        current = current.next
    end function
    ```

2. **Prepend** : <br> will add new node at the start of the list and the head of the list will now point to the new node.

    ```jsx
    function Prepend(head, data)
    //create node and pass data parameter
      new_node = create_node(data)
      //set "next" pointer of the new node to point to the current head
      new_node.next = head
        //update head of the list to be the new node
        head = new_node
        //move current pointer to the next node by assigning "current.next" to current and the loop continues
    end function
    ```

3. **Append** : <br> will add the new node at the end of the list, and the last node's next pointer will point to the new node

    ```jsx
    function append(head, data)
    //create new node
        newNode = create_node(data)
        //init var current and initialize it to equal to head
        current = head
        //check if the head of the list is null, 
        if (current = null)
            //set head to equal new node
            head = newNode
        else 
           //if head does not equal to null, loop to iterate till the last node(tail)
            while current.next != null
                current = current.next
                //set next pointer of the last node to point to the new node(adding the new node to the end)
            current.next = newNode
        end if
      end function
    ```
<hr>

## Constraints
  * Empty linked list (head is null)
  * Single node
  * Two nodes
  * Linked list has cycles.

<br>

![](https://img.shields.io/static/v1?label=&message=💡Tip:&color=orange): Clarify beforehand with the interviewer whether there can be a cycle in the list. Usually the answer is no and you don't have to handle it in the code

To see how a linked list is implemented see [here]()

<hr>

## Related Questions
| No | Problem Statement                                                         |
|----|---------------------------------------------------------------------------|
| 1. | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) |
|    |                                                                           |

<hr>

## References

# Articles

1.  [Medium](https://medium.com/basecs/whats-a-linked-list-anyway-part-1-d8b7e6508b9d)

# Videos

2.  [Coursera](https://www.coursera.org/lecture/data-structures/singly-linked-lists-kHhgK)