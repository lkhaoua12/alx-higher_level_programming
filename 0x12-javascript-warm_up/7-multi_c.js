#!/usr/bin/node
const { argv } = require('process');
let accur = parseInt(argv[2]);
if (isNaN(accur)) {
  console.log('Missing number of occurrences');
} else {
  while (accur > 0) {
    console.log('C is fun');
    accur--;
  }
}
