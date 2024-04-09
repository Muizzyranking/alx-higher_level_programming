#!/usr/bin/node
// calculates the factoial of the first argument

const n = parseInt(process.argv[2]);

function factorial (n) {
  if (n < 0) {
    return -1;
  }
  if (n === 0 || isNaN(n)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const factorialResult = factorial(n);
console.log(factorialResult);
