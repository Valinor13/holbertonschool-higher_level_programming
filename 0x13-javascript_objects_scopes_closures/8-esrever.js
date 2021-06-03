#!/usr/bin/node

exports.esrever = function (list) {
  const nArry = [];
  let i = list.length - 1;

  while (i >= 0) {
    nArry.push(list[i]);
    i--;
  }
  return nArry;
};
