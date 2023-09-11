#!/usr/bin/node
const { argv } = require('process');
if (!argv[2]) {
  console.log('Missing size');
} else {
  const num = parseInt(argv[2]);
  if (!isNaN(num)) {
    for (let i = 0; i < num; i++) {
      let line = '';
      for (let j = 0; j < num; j++) {
        line += 'X';
      }
      console.log(line);
    }
  } else {
    console.log('Missing size');
  }
}
