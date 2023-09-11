#!/usr/bin/node
const { argv } = require('process');
let result = 1;
let num = parseInt(argv[2]);
if (isNaN(num)) {
  result = 1;
} else {
  while (num > 1) {
    result *= num;
    num--;
  }
}
console.log(result);
