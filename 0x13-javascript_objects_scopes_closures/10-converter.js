#!/usr/bin/node

exports.converter = function (base) {
  const conNum = function doCon (num) {
    return num.toString(base);
  };
  return conNum;
};
