let myArray1 = [70, 30, 10, 50, 100, 2] //test case 1
let myArray2 = [1, 2, 3, 4, 5, 6] //test case 2
let myArray3 = [45, 10, 63, 40, 50, 80] //test case 3


const insertionSort = (arr)=>{
    for (let i = 1; i < arr.length; i++) {
        let key = arr[i]
        let j = i - 1
        while ( j >= 0 && arr[j] > arr[i]) {
            arr[j + 1] = arr[i]
            j -= 1
        }

        arr[j + 1] = key
    }

    return arr
}

console.log(insertionSort(myArray1))
console.log(insertionSort(myArray2))
console.log(insertionSort(myArray3))