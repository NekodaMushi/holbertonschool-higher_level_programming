#!/usr/bin/node
const fs = require("fs");
const filePath = './cisfun'
const fileContents = fs.readFileSync(filePath, 'utf8');

console.log(fileContents);
