#!/usr/bin/node
// creates a class Rectangle that defines a rectangle

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // method to print the rectangle using the character X
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  // method that exchanges the width and the height of the rectangle
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // method that multiplies the width and the height of the rectangle by 2
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
