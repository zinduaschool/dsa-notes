<h1 align="center">DYNAMMIC PROGRAMMING</h1>

- Dynammic Programming is a method for solving a complex problem by breaking it down into a collection of simpler subproblems, solving each of those subproblems just once, and storing their solutions using a memory-based data structure (array, map,etc).
- It only works on problems with optimal substructure and overlapping subproblems. An example of this is the Fibonacci sequence.
- The idea is to simply store the results of subproblems, so that we do not have to re-compute them when needed later. This simple optimization reduces time complexities from exponential to polynomial.

<h2 align="center"> Techniques to Solve Dynammic Programming.</h2>

- There are two ways to solve a problem using Dynamic Programming:
  - Top-Down Approach
  - Bottom-Up Approach

<h3>1. Top-Down Approach (Memoization) </h3>

- This is the recursive approach to solve the problem. In this approach, we try to solve the bigger problem by recursively finding the solution to smaller sub-problems. Whenever we solve a sub-problem, we cache its result so that we don’t end up solving it repeatedly if it’s called multiple times. Instead, we can just return the saved result. This technique of storing the results of already solved subproblems is called Memoization. Read About memoization <a href="../memoization/README.md">here.</a>
- Consider the fibonacci sequence, while using recursion we are solving the same sub-problem multiple times. For example, if we want to find the 5th fibonacci number using recursion, we will end up solving the fibonacci number for 2 multiple times. This is inefficient and can be optimized using memoization.

```jsx
// Top-Down Approach (Memoization)
function fib(n, memo=[]) {
    if (memo[n] !== undefined) return memo[n]

    if ( n <= 1 ) return n

    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
}

console.log(fib(5)) // 5
```
- In the above code, we are storing the results of the sub-problems in the <code>memo</code> array. So, if we want to find the 5th fibonacci number, we will first check if the result is already present in the <code>memo</code> array. If it is present, we will return the result from the memo array, otherwise we will calculate the result and store it in the memo array for future use. This optimized the time complexity from exponential to linear.O(n) from exponential O(2^n)

<h3>2. Bottom-Up Approach (Tabulation)</h3>

- This is the preferred way of solving a dynamic programming problem. In this approach, we solve the problem “bottom-up” (i.e. by solving all the related sub-problems first). This is typically done by filling up an n-dimensional table. Based on the results in the table, the solution to the top/original problem is then computed.
- If we needed to find the fibonacci sequence using the bottom-up approach, we would first solve the sub-problems and store their results in a table. Then, we would use the results of the sub-problems to solve the original problem.

```jsx
// Bottom-Up Approach (Tabulation)
const fib = (n)=>{
    const fibArray = [0, 1]
    if (n <= 1) return n

    for (let i = 2; i < n; i++) {
        fibArray[i] = fibArray[i-1] + fibArray[i-2]
    }

    return fibArray[n]
}

console.log(fib(5)) //5
```
- In the code above, we have initialized a <code>fibArray</code> that holds the first 2 numbers. Then, we loop through the array from the 3rd element and calculate the next fibonacci number by adding the previous two numbers. This way, we are solving the sub-problems first and then using the results of the sub-problems to solve the original problem. This optimizes the time complexity from exponential to linear O(n) from exponential O(2^n). The above output can be simplified to use a constant space complexity by using two variables instead of an array.