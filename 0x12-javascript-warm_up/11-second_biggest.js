#!/usr/bin/node

const args = [];
let biggest, secondBiggest;
for (let i = 2; i < process.argv.length; i++) {
  args.push(parseInt(process.argv[i]));
}
if (args.length < 2) {
  console.log(0);
} else {
  let i = 0;
  biggest = args[i];
  secondBiggest = 0;
  for (i = 1; i < args.length; i++) {
    if (args[i] > biggest) {
      secondBiggest = biggest;
      biggest = args[i];
    } else if (args[i] > secondBiggest) {
      secondBiggest = args[i];
    }
  }
  console.log(secondBiggest);
}
