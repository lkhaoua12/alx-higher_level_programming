#!/usr/bin/node
const { argv } = require('process');
function factr (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factr(n - 1);
  }
}
const num = parseInt(argv[2]);
let result = 1;
if (isNaN(num)) {
  console.log(result);
} else {
  result = factr(num);
  console.log(result);
}
