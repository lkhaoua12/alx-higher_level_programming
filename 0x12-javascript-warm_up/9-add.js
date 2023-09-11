#!/usr/bin/node
function add (a, b) {
  return (parseInt(a) + parseInt(b));
}
const { argv } = require('process');
const result = add(argv[2], argv[3]);
console.log(result);
