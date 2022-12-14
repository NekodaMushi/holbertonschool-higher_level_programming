#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the URL
request(url, function (error, response, content) {
  if (!error && response.statusCode === 200) {
    fs.writeFile(filePath, content, 'utf-8', err => {
      if (err) {
        console.log(err);
      }
    });
  } else {
    console.log(error);
  }
});
