#!/usr/bin/node
'user strict';

// base case
function factorial (n) {
  if (n === 0 || n === 1) { return 1; }
  // recursion case
  else { return n * factorial(n - 1); }
}
console.log(factorial(Number(process.argv[2])));
