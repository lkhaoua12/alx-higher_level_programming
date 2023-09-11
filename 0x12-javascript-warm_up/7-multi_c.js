#!/usr/bin/node
const { argv } = require('process');
let accur = parseInt(argv[2]);
if (isNaN(accur)) {
  console.log('C is fun');
} else {
  while (accur) {
    console.log('C is fun');
    accur--;
  }
}
