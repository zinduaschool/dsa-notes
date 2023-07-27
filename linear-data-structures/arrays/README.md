# Array
Arrays are linear data structures that stores a collection of values.<br>The values in an array are stored in a sequence.<br> Each value in an array is called an element and each element has an index, which is its position in the array.<br>In JavaScript, the index of the array has an index of 0, the second element has index of 1, and so on.

<hr>

Examples: 

```jsx
const age = [7, 19, 2, 90, 24, 30];

console.log(age[0]) //Output: 7
console.log(age[1]) //Output: 19
console.log(age[2])  //Output: 2
console.log(age[3])  //Output: 90
```

You can also use a loop to iterate over the elements of an array. See below;

```jsx
const age = [7, 19, 2, 90, 24, 30];
for(let i = 0; i < age.length; i++){
console.log(age[i]);
}
//This will print all ages separately to the console.
```
<hr>

### **Advantage of using an Array** <br>
It allows random access of elements, hence making it the best choice for storing large amounts of data

### **Disadvantage of using an Array** <br>
It has fixed size, so it can't easily be resized. Not efficient when inserting or deleting elements. <br>
Additionally, the space it takes up can be wasted, if the array has many empty spots.

<hr>

## Array Methods
| Access | Lookup | Insert(at) | Deletion At | push/pop |
|:------:|:------:|:----------:|:-----------:|:--------:|
|  O(1)  |  O(1)  |    O(n)    |     O(n)    |   O(1)   |

* **Push** : Add elements to the end of an array and returns the new length of the array. O(1) T & S
* **Pop** : Removes the last element of an element of an array and returns the removed element. O(1) T
* **Shift/ Delete at** : Removes the first element of an array and returns the removed element. O(n) T because all the elements of the array need to be shifted one position to the left. 
* **Unshift/ Insert at** : adds elements to the beginning of an array and returns the new length of the array. The time complexity of this operation is O(n), as all elements of the array must be shifted one position to the right. 
* **Splice** : Modifies an array by adding or removing elements, and returns the elements that were removed. The time complexity of this operation is O(n), as the elements after the inserted or removed element must be shifted
* **Slice** : The creates a new array and copies a selection of elements from the original array into it, resulting in a shallow copy. This operation has a time complexity of O(n), as a new array must be created and all elements must be copied. 

<hr>

## To have in your back pocket

    1. Clarify if there are duplicate values in the array and would it affect the answer
    2. When using an index to iterate make sure to consider nums.length - 1, (which refers to the last element of the array)
    3. Be mindful about slicing or concatenating arrays, that’s an O(n) T

## Constraints

    1. Empty Sequence
    2. Sequence with 1 or 2 elements
    3. Sequence with repeated elements
    4. Duplicated values in the sequence // could be scattered

<hr>

## Techniques

    1. Sliding Window
        The two pointers (L,R) —> usually move in the same direction will never overtake each other  O(n)

    2. Two Pointers
        A general version of sliding window where pointers can cross each other and can be on different arrays. eg; merge sorted arrays

    3. Traversing from the right
        sometimes you can traverse the array from the right

    4. Sorting the array
        If the array is sorted, some form of binary search should be possible which is O(log n)

    5. Precomputation
        For queries where sum or * of subarray is involved, pre-computing using hashing or prefix/suffix sum, might be useful.  Check prefix-sum tags on  leetcode

    6. Index has a hash key
        If a you are given a sequence and the query needs O(1) Space, it might be possible to use the array itself as a hash table. eg; if the array only has values from 1 to N, where N is the length of the array, negate the value at that index(-1) to indicate presence of the num.

    5. Traversing the array more than once
        Traversing the array twice/thrice is still O(n) example is two for loops

<hr>

## References
1. [Array Data structures](https://www.guru99.com/array-data-structure.html)
2. [Arrays Explained - Coursera](https://www.coursera.org/lecture/data-structures/arrays-OsBSF)