#!/usr/bin/node
exports.esrever = function (list) {
  for (let i = 0, j = list.length - 1; j - i >= 0; i++, j--) {
    const temp = list[i];
    list[i] = list[j];
    list[j] = temp;
  }
  return list;
};
