#!/usr/bin/node
// returns a status code from a url

const url = process.argv[2];

fetch(url, { method: 'GET' }).then(response =>
  console.log(`code: ${response.status}`)
);
