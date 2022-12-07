#!/usr/bin/node
'use strict'

module.exports = class Square extends require('./4-rectangle') {
  constructor(size) {
    super(size, size);
  }
  charPrint(c){
    if (!c) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++){
      console.log(c.repeat(this.width));
    }
  }
}
