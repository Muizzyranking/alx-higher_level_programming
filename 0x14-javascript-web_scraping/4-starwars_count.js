#!/usr/bin/node

const request = require('request');

function getCount (API_URL) {
  const url = API_URL;
  request(url, (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      const results = JSON.parse(body).results;
      const count = results.reduce((count, movie) => {
        return movie.characters.find(character => character.endsWith('/18/'))
          ? count + 1
          : count;
      }, 0);
      console.log(count);
    }
  });
}

if (process.argv.length === 3) {
  getCount(process.argv[2]);
} else {
  console.log('Usage: ./4-starwars_count.js <API_URL>');
}
