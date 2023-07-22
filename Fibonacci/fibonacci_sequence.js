function fibonacci(number) {
  let fib = [0, 1]; // Initialize array!
  for (let i = 2; i < number; i++) {
    fib[i] = fib[i - 1] + fib[i - 2];
  }
  console.log(fib);
}

fibonacci(11); // [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]