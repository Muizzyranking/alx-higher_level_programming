#!/usr/bin/node
// converts first arg to integer and print

const arg = process.argv[2];

if (isNaN(arg)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(arg));
}
