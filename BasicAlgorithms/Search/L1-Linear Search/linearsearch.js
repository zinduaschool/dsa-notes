/**
 * @TimeComplexity - O(n)
 * @SpaceComplexity - O(1)
 * @param {*} arr
 * @param {*} num
 * @returns Index of num in arr
 */
const linearSearch = (arr, num)=>{
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === num) {
            return i
        }
    }
    return
}

const lst = [12, 34, 45, 72, 81, 98, 112, 200, 1000, 10000]
const a = 200

console.log(linearSearch(lst, a))