let my_array1 = [70, 30, 10, 50, 100, 2] //test case 1
let my_array2 = [5,2,3,1] //test case 2
let my_array3 = [45, 10, 63, 40, 50, 80] //test case 3

const partition = (arr, low, high)=>{
    let pivot= arr[high]
    let i = low - 1
    let temp
    for (let j = low; j < arr.length; j ++ ) {
        if (arr[j] < pivot) {
            i +=1
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp 
        }
    } 
    temp = arr[i + 1]
    arr[i + 1] = arr[high]
    arr[high] = temp
    
    return i + 1
}

/**
 * @TimeComplexity - O(n^2)
 * @SpaceComplexity - O(1)
 * @param {*} arr 
 * @param {*} low 
 * @param {*} high 
 * @returns sorted array
 */
const quickSort = (arr, low, high)=>{
    if (low < high) {
        pivot_location = partition(arr, low, high)
        quickSort(arr, low, pivot_location - 1)
        quickSort(arr, pivot_location + 1, high)
    }
    return arr
}

console.log(quickSort(my_array1, 0, my_array1.length - 1))
console.log(quickSort(my_array2, 0, my_array2.length - 1))
console.log(quickSort(my_array3, 0, my_array3.length - 1))