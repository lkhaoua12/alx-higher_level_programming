#!/usr/bin/node
/**
 * write str to file
 */

const fs = require('fs');
const fileName = process.argv[2];
const textWrite = process.argv[3];
fs.writeFile(fileName, textWrite, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
