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

  rotate () {
    const nw = this.width;
    const nh = this.height;

    this.width = nh;
    this.height = nw;
  }

  double () {
    const tXw = this.width * 2;
    const tXh = this.height * 2;

    this.width = tXw;
    this.height = tXh;
  }
}

module.exports = Rectangle;
