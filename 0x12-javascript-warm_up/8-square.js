#!/usr/bin/node
// prints a square x times

const noOfTimes = process.argv[2];
if (isNaN(noOfTimes) || noOfTimes === undefined) {
  console.log('Missing number of occurrences');
} else {
  let i;
  for (i = 0; i < noOfTimes; i++) {
    console.log('X'.repeat(noOfTimes));
  }
}
