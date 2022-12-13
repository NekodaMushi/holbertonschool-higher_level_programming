#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

// Make a request to API URL to get a list of all the movies
request.get(apiUrl, function (error, response, body) {
  if (error) throw error;
  else {
    let count = 0;
    const movies = JSON.parse(body).results;
    for (const items of movies) {
      // Check if the character appears in the movie
      for (const actor of items.characters) {
        if (actor.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
