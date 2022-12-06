#!/usr/bin/node
'user strict';

const arr = [];
for (let i = 2; i < process.argv.length; i++) {
  arr.push(process.argv[i]);
}
arr.sort(function (a, b) {
  return b - a;
});
console.log(arr[1]);
