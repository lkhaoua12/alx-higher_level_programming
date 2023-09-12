#!/usr/bin/node
const { argv } = require('process');
let highest = 0;
let secondHighest = 0;
if (argv.length < 4) {
  console.log(0);
} else {
  for (const num of argv) {
    if (parseInt(num) > highest) {
      secondHighest = highest;
      highest = parseInt(num);
    } else if (parseInt(num) > secondHighest) {
      secondHighest = parseInt(num);
    }
  }
  console.log(secondHighest);
}
