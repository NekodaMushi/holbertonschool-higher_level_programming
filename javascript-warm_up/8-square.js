#!/usr/bin/node
'user strict';
const size = Number(process.argv[2]);
if (size && isNaN(size) === false) {
  for (let x = 0; x < size; x++) {
    for (let y = 0; y < size; y++) {
      process.stdout.write('X');
    }
    console.log();
  }
} else {
  console.log('Missing size');
}
