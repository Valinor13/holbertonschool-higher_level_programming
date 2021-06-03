#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  let x = 0;
  while (i < list.length) {
    if (list[i] === searchElement) {
      x++;
    }
    i++;
  }
  return x;
};
