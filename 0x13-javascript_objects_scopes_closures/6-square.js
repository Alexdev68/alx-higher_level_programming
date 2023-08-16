#!/usr/bin/node
const Square2 = require('./5-square');

class Square extends Square2 {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    let i = 0;

    if (c === undefined) {
      c = 'X';
    }

    while (i < this.width) {
      console.log(c.repeat(this.width));
      i++;
    }
  }
}

module.exports = Square;
