#!/usr/bin/node

const x = parseInt(process.argv[2]);
const y = parseInt(process.argv[3]);

if (isNaN(x) || isNaN(y)) {
  console.log('NaN');
} else {
  console.log(add(x, y));
}

function add (a, b) {
  return a + b;
}
