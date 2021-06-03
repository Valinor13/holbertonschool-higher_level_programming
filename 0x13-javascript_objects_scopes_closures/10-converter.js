#!/usr/bin/node

exports.converter = function (base) {
  con_num = function doCon (num) {
    return num.toString(base);
  }
  return con_num;
}
