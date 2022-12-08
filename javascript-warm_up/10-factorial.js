#!/usr/bin/node
'use strict';

function factorial (n) {
  if (!n || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
console.log(factorial(Number(process.argv[2])));
