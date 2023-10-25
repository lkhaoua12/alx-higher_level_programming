#!/usr/bin/node
/**
 * get page body and write it to a file.
 */

const args = process.argv.splice(2);
const apiUrl = args[0];
const fileName = args[1];

const fs = require('fs');
const request = require('request');

request(apiUrl, function (error, responce, body) {
  if (!error) {
    fs.writeFile(fileName, body, 'UTF-8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
