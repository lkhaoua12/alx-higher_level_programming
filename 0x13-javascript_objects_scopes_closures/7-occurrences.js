#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, element) => (
    element === searchElement ? count: count),
  0);
};
