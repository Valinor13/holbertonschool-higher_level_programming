#!/usr/bin/node

exports.converter = function (base) {
  return function doCon (num) {
    return num.toString(base);
  };
};
