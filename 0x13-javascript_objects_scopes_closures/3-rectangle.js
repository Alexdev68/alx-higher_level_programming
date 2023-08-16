#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w < 1 || h < 1) {
      return '';
    } else if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;

    while (i < this.height) {
      const ch = 'X';
      console.log(ch.repeat(this.width));
      i++;
    }
  }
}

module.exports = Rectangle;
