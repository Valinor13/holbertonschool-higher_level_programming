#!/usr/bin/node

function addMeMaybe (x, obj) {
  x++;
  obj(x);
}

exports.addMeMaybe = addMeMaybe;
