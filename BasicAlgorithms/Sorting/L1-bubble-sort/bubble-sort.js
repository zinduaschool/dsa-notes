let myArray1 = [70, 30, 10, 50, 100, 2] //test case 1
let myArray2 = [1, 2, 3, 4, 5, 6] //test case 2
let myArray3 = [45, 10, 63, 40, 50, 80] //test case 3

/**
 * Brute Force- Bubble Sort
 * @TimeComplexity - O(n^2)
 * @SpaceComplexity - O(1)
 * @param1 - Unsorted list to be sorted by the function
 */
const bubbleSort = (arr)=>{
    let temp;
    for (let i = 0; i < arr.length -1; i++) {
        for (let j = i+ 1; j < arr.length; j++) {
            if (arr[i] > arr[j]) {
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
            }
        }
    }
    return arr
}


console.log(bubbleSort(myArray1))
console.log(bubbleSort(myArray2))
console.log(bubbleSort(myArray3))