/** */
const myArray1 = [70, 30, 10, 50, 100, 2] //test case 1
const myArray2 = [1, 2, 3, 4, 5, 6] //test case 2
const myArray3 = [45, 10, 63, 40, 50, 80] //test case 3

/**
 * @TimeComplexity - O(nlog N)
 * @SpaceComplexity - O(n)
 * @param {*} arr 
 * @returns - sorted list
 */
const merge_sort = (arr)=>{
    if (arr.length <= 1) {
        return arr
    }
    const mid = Math.floor(arr.length / 2)
    const leftArray = arr.slice(0, mid)
    const rightArray = arr.slice(mid)

    const sortedLeft = merge_sort(leftArray)
    const sortedRight = merge_sort(rightArray)

    const result = []
    let j = 0 
    let i = 0

    while (i < sortedLeft.length && j < sortedRight.length) {
        if (sortedLeft[i] < sortedRight[j]) {
            result.push(sortedLeft[i])
            i += 1
        } else {
            result.push(sortedRight[j])
            j += 1
        }
    }

    return result.concat(sortedLeft.slice(i).concat(sortedRight.slice(j)))
}

console.log(merge_sort(myArray1))
console.log(merge_sort(myArray2))
console.log(merge_sort(myArray3))