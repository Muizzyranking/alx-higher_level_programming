#!/usr/bin/node
// returns a status code from a url

const url = process.argv[2];
const request = require('request');

request(url, function (error, response) {
  if (error) {
    console.log(error);
    return;
  }
  console.log('code:', response.statusCode);
});
