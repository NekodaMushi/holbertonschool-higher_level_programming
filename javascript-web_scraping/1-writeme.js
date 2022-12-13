#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const textWrite = process.argv[3];

fs.appendFile(filePath, textWrite, (err) => {
  if (err) throw err;
});
