#!/usr/bin/node
/**
 * find number of charch in title.
 */

const args = process.argv.splice(2);
const apiUrl = args[0];
const charId = '18';
const request = require('request');

request(apiUrl, function (error, responce, body) {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;

    for (const film of films) {
      for (const char of film.characters) {
        if (char.includes(charId)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
