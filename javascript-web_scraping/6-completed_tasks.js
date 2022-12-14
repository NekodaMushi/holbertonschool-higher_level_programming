#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request.get(url, function (error, response, content) {
  if(!error && response.statusCode === 200) {
    const res = JSON.parse(content);
    const tempDict = {};
    for (let i = 0; i <res.length; i++) {
      if (res[i].completed === true) {
        if (tempDict[res[i].userId] === undefined) {
          tempDict[res[i].userId] = 1;
        } else {
          tempDict[res[i].userId]++;
        }
      }
    }
    console.log(tempDict);
  }
});
