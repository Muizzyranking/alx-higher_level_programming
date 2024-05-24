#!/usr/bin/node

const request = require('request');

function getCount (API_URL) {
  const url = API_URL;
  const characterUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
  request(url, (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      let count = 0;
      let i, j;
      const films = JSON.parse(body);
      const filmCount = films.count;
      for (i = 0; i < filmCount; i++) {
        const characters = films.results[i].characters;
        for (j = 0; j < characters.length; j++) {
          if (characters[j] == characterUrl) {
            count += 1;
            break;
          }
        }
      }
      console.log(count);
    }
  });
}

if (process.argv.length === 3) {
  getCount(process.argv[2]);
} else {
  console.log('Usage: ./4-starwars_count.js <API_URL>');
}
