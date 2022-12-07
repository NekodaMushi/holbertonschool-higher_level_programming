#!/usr/bin/node
'use strict';

let nb = 0;
exports.logMe = function (item) {
  console.log(nb + ': ' + item);
  nb += 1;
}

