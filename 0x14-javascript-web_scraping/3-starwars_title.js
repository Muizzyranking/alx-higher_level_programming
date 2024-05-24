#!/usr/bin/node
// returns title of a movie by its id

const request = require('request');

function getTitle (id) {
  const url = `https://swapi-api.hbtn.io/api/films/${id}`;
  request(url, (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).title);
    }
  });
}

if (process.argv.length === 3) {
  if (isNaN(process.argv[2])) {
    console.log('Usage: ./3-starwars_title.js <movie_id>');
    console.log('movie_id must be an integer');
    process.exit(1);
  }
  getTitle(process.argv[2]);
} else {
  console.log('Usage: ./3-starwars_title.js <movie_id>');
}
