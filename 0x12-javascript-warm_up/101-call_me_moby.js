#!/usr/bin/node

function callMeMoby (i, obj) {
  let x = 0;
  while (x < i) {
    obj();
    x++;
  }
}

exports.callMeMoby = callMeMoby;
