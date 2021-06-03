#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (isNaN(num)) {
  console.log('1');
} else {
  console.log(factorial(num));
}

function factorial (x) {
  if (x < 0) {
    return -1;
  } else if (x === 0) {
    return 1;
  } else {
    return (x * factorial(x - 1));
  }
}
