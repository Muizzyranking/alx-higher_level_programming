#!/usr/bin/node
// adds the first two arguments

function add(a, b) {
  return a + b;
}

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
console.log(add(a, b));
