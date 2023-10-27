let my_array3 = [45, 10, 63, 40, 50, 80]

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

console.log(insertionSort(my_array3))