<h1 align="center">Quick Sort</h1>

- Quicksort is a highly efficient sorting algorithm and is based on the partitioning of an array of data into smaller arrays. A large array is partitioned into two arrays one of which holds values smaller than the specified value, say pivot, based on which the partition is made and another array holds values greater than the pivot value.

- Quicksort partitions an array and then calls itself recursively twice to sort the two resulting subarrays. This algorithm is quite efficient for large-sized data sets as its worst time complexoty is O(n^2).

- Picking a pivot element is the core of the algorithm. The goal of the partition process is to rearrange the array in such a way that all elements less than the pivot element are moved to the left of the pivot, and all greater elements are moved to the right of the pivot. This is called partitioning the array.
- The pivot can either be
  - The first element of the array.
  - The last element of the array.
  - A random element of the array.
  - The median of the array.