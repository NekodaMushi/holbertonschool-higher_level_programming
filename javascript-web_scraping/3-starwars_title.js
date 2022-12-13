#!/usr/bin/node
const request = require('request');
// Movie Number
const movie = process.argv[2];
// API endpoint for movie information
const endpoint = `https://swapi-api.hbtn.io/api/films/${movie}`;
// GET request to API
request.get(endpoint, (err, response, body) => {
  if (err) throw err;
  const data = JSON.parse(body);
// Parse JSON response
  console.log(data.title);
})
