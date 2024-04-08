//Optimal Soln  O(logn)
const binarySearch = (arr, target) => {
    let firstIdx = 0
    let lastIdx = arr.length - 1
  
    while(lastIdx >= firstIdx){
        let midNum = Math.floor((firstIdx + lastIdx) /2)
      if(target === arr[midNum]){
        return midNum
      }
      if(target < arr[midNum]){
        lastIdx = midNum - 1
      } else {
        firstIdx = midNum + 1
      }   
    }
     return -1
  }