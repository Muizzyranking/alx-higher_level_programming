#!/usr/bin/node

// checks the number of occurrences of an element in a list
exports.nbOccurences = function (list, searchElement) {
  let occurences = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      occurences += 1;
    }
  }
  return occurences;
}
