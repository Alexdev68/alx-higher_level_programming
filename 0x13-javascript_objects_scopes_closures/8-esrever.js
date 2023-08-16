#!/usr/bin/node

exports.esrever = function (list) {
  let i = list.length - 1;
  let j = 0;
  const nlist = [];

  while (i + 1 > 0) {
    nlist[j] = list[i];
    j++;
    i--;
  }
  return nlist;
};
