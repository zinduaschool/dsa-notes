# [Big O Notation](https://en.wikipedia.org/wiki/Big_O_notation)

> **Big O** helps us answer the question, “_Will it scale?_” <br>

## Why Big O 
It helps us choose the best data structure and algorithm for certain use cases

It is a way to evaluate the efficiency of an algorithm. Also, it allows us to determine how the algorithm will perform, or how much memory it uses, as the input size grows larger. <br> Instead of measuring the actual time it takes for the algorithm to run, we consider the number of steps or operations required to complete the task. This helps us understand how well an algorithm scales and how it will perform with very large inputs. 
<br>  
To use Big O notation, we describe the running time of an algorithm in terms of how many steps it takes as the input size grows. For example, we might say that an algorithm takes O(n) time, where n is the size of the input. This means that the running time of the algorithm is directly proportional to the size of the input.

"O" in Big O notation stands for "order of" as in order of magnitude

<hr>

## Types of Big O Notation

 1. **O(1)** - Constant: _This signifies the running time of the algorithm is constant, regardless of the size of the input. This is exemplified by looking up an element in an array using an index_
 2. **O(log(n))** - Logarithmic: _This implies the running time of the algorithm increases logarithmically with the size of the input. One instance of this is, is binary search, which involves dividing the list in half and searching the appropriate half for the element it's looking for, if they are sorted (Binary Search)_
 3. **O(n)** - Linear: _This represents the running time of the algorithm is directly proportional to the size of the input. An example of O(n) algorithm is a linear search, which involves looking through each element of a list one by one until it finds the element it's looking for._
 4. **O(n log n)** - Logarithmic /Quasilinear: _This indicates that, the running time of the algorithm is a combination of linear and logarithmic complexity. An example is the merge sort algorithm_
 5. **O(n^2)** - Quadratic: _This translates to the running time of the algorithm is proportional to the square of the size of the input . This can be seen in bubble sort, which involves comparing each element of a list with every other element._
 6. **O(n^3)** - Cubic: _Essentially, the running time of the algorithm is proportional to the cube of the input size. An example is nested for loop_
 7. **O(2^n)** - Exponential: _To put it simply, the running time of the algorithm increases exponentially as the input size increases. This is demonstrated by, the recursive calculations of the fibonacci sequence._
 8. **O(n!)** - Factorial: _This means that the running time of the algorithm is proportional to the factorial of the input size. This can be demonstrated by, an algorithm is the travelling salesperson problem_

<br>
<img width="850"  src="../../assets/bigo-cheat-sheet.png" alt="Big O"/>

<hr>

Reference: [Big O Cheat Sheet](https://www.bigocheatsheet.com/)

## Prerequisites
> To **Note**: Understanding time and space complexity is important because it helps us predict the perfomance of an algorithm and choose the most effecient solution for a given problem. These two are closely related <br>
1. **Time Complexity** - This is a measure of how fast an algorithm runs
2. **Space Complexity** - This is the measure of how much auxiliary memory an algorithm takes up

<hr>

### What can cause Time complexity
1. **The number of basic operations** (+.-,*,/)
2. **The number of iterations**: An example of a loop will take longer to run than an algorithm that performs the same task in a single step like looking up an element in an array using it's index (Looping (for, while))
3. **The size of the input (n)**: An algorithm that processes a large amount of data will take longer to run than an algorithm that processes a smaller amount of data. 
4. **The structure of the data**: The performance of an algorithm can be affected by the structure of the input data. An example is, if the data is already sorted, certain algos that rely on comparisons (<,>, ==) may be able run more effeciently.
5. **The characteristics of the input data**: If the data is highly correlated or follows a particular pattern, certain algorithms may be able to take advantage of the pattern to run more efficiently.
6. **Machine Architecture**: The underlying hardware and machine architecture affects the time complexity of an algorithm. For example the size of cache and the number of processors can impact the performance of an algorithm.

### What can cause Space complexity
1. **The size of the input data**: A program that processes large amounts of data will typically require more memory than a program that processes smaller amounts of data.
2. **The no. of variables and data structures used**: A program that uses many variables or complex data structures like arrays and trees, will typically require more memory than a program that uses fewer varaibles or simpler data structures.
3. **The length of time the program is running**: A program that runs for a long time may require more memory to store temporary data or intermediate results
4. **Recursion function call**: A program that uses recursive functions (i.e, function call themselves) may require more memory to store the intermediate results of each recursive call
5. **The complexity of an algorithm**: More complex algorithms may require more memory to store intermediate results or to maintain data structures 
6. **Machine Architecture**: The underlying hardware and machine architecture can also affect the space complexity of an algorithm. The amount of available memory, the size of the cache, and the architecture of the memory hierarchy can impact the amount of memory space an algorithm can use.

<hr>

### Rule Book
* Rule 1: Always check for worst case scenario
* Rule 2: Remove Constants
* Rule 3: Different inputs should have different variables. O(a+b). A and B arrays nested would be O(a*b)
* Rule 4: Drop Non-dorminant terms


> To **Note** Big O notation is a useful tool for analyzing the efficiency of algorithms and comparing the running times of different algorithms. Big O notation gives an upper bound on the running time of an algorithm, so it's possible that an algorithm might run faster in practice than the Big O notation suggests
