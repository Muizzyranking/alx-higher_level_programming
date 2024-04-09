#!/usr/bin/node
// prints a string x times

const noOfTimes = process.argv[2];
if (isNaN(noOfTimes) || noOfTimes === undefined) {
  console.log('Missing number of occurrences');
} else {
  let i;
  for (i = 0; i < noOfTimes; i++) {
    console.log('C is fun');
  }
}
