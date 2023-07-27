//Fibonaacci sequence using dynamic programming

/** Brute Force/Naive Approach -> Recursion
 * @Time Complexity: O(2^n)
 * @Space Complexity: O(n)
 * @param {n} -> number of fibonacci numbers to be generated 
 * @returns -> The nth fibonacci number
 */
function fibRecurse(n) {
  if ( n <= 1) {  //base case
    return n 
  }
  return fibonacci(n-1) + fibonacci(n-2) //  recursive case
}


/** Top Down Approach -> Recursion(With cache)
 * @Time Complexity: O(n)
 * @Space Complexity: O(n)
 * @param {n} -> number of fibonacci numbers to be generated 
 * @returns  -> The nth fibonacci number
 */
function fibMemoize(n, memo=[]) {
  if ( memo[n] != undefined) {  // check if the value is already cached
    return memo[n]
  }
  if ( n <= 1) {                // base case
    return n 
  } 

  memo[n] = fibMemoize(n-1, memo) + fibMemoize(n-2, memo)
  return memo[n]
}

/** Bottom Up Approach -> Iteration
 * @Time Complexity: O(n)
 * @Space Complexity: O(1)
 * @param {n} -> number of fibonacci numbers to be generated  
 * @returns -> The nth fibonacci number
 */
function fibBottomUp(n) {
  if ( n <=1 ){ // base case
    return n
  }
  let count = 1           // counter to keep track of number of fibonacci numbers generated
  let current = 1         // current fibonacci number
  let prev = 0            // previous fibonacci number
  let next                // next fibonacci number

  while ( count < n ) {   // iterate till count is less than n
    next = current + prev // calculate next fibonacci number
    prev = current        // update previous fibonacci number
    current = next        // update current fibonacci number
    count ++              // increment count
  }
  return next
}

// or

//Time Complexity: O(n) | Space Complexity: O(n)
function fibBottopUp2(n) {
  let fib = [0, 1]                  // Initialize array to store first two fibonacci numbers
  for ( let i = 2; i <= n; i ++) {  // iterate array from index 2 to n
    fib[i] = fib[i-1] + fib[i-2]    // store the sum of previous two fibonacci numbers
  }
  return fib[n]                     // return the nth fibonacci number
}


//Output
console.log(fibRecurse(10))     // 55
console.log(fibMemoize(10))     // 55
console.log(fibBottomUp(10))    // 55
console.log(fibBottopUp2(10))   // 55