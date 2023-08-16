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
}

module.exports = Rectangle;
