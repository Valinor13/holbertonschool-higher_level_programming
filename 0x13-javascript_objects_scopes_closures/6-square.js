#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }
    let i = 0;
    while (i < this.size) {
      console.log(c.repeat(this.size));
      i++;
    }
  }	
}

module.exports = Square;
