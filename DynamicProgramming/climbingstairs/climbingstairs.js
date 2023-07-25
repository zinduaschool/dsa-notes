/**Brute Force/Naive Approach - Recursion
 * @Time Complexity -> O(2^n)
 * @Space Complexity -> O(n)
 * @param {number} n -> number of stairs
 * @returns {number} -> number of ways to climb the stairs
 */
const climbStairsRecurse = (n)=>{
    if ( n <= 2 ) {
        return n;
    } 

    return climbStairsRecurse(n-1) + climbStairsRecurse(n-2)
}

/**Memoization Approach/Top Down Approach - Recursion(with cache)
 *@Time Complexity -> O(n)
 *@Space Complexity -> O(n)
 *@param {number} n -> number of stairs
 *@returns {number} -> number of ways to climb the stairs
 */
const climbStairsMemo = (n, memo=[])=>{
    if ( memo[n] != undefined) {
        return memo[n]
    }

    if ( n <= 2 ){
        return n
    }   

    memo[n] = climbStairsMemo(n-1, memo) + climbStairsMemo(n-2, memo)

    return memo[n]

}


/**
 * @Time Complexity -> O(n)
 * @Space Complexity -> O(1)
 * @param {number} n -> number of stairs
 * @returns {number} -> number of ways to climb the stairs
 */
const climbStairsBottomUp = (n)=>{
    if ( n <= 2 ){
        return n
    } 
    
    let current = 1
    let prev = 0
    let next 
    for ( let i = 0; i<n; i++) {
        next = current + prev
        prev = current
        current = next
    }

    return next
}


console.log(climbStairsRecurse(10))     // 89
console.log(climbStairsMemo(10))        // 89
console.log(climbStairsBottomUp(10))    // 89