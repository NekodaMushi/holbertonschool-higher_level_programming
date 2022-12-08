#!/usr/bin/node
'use strict';

const arr = [];
for (let i = 2; i < process.argv.length; i++) {
  if (process.argv[i] < 0) console.log(0);
  else arr.push(process.argv[i]);
}
arr.sort(function (a, b) {
  return b - a;
});
if (arr.length > 0) console.log(arr[1]);
if (!process.argv[2]) console.log(0);
