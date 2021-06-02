#!/usr/bin/node

let x = parseInt(process.argv[2]);

if (isNaN(x)) {
  console.log('Missing size');
} else {
  const z = x;
  while (x > 0) {
    console.log('X'.repeat(z));
    x--;
  }
}
