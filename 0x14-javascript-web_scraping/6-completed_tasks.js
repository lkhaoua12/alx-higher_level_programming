#!/usr/bin/node
/**
 * list user and completed tasks.
 */

const request = require('request');
const args = process.argv.splice(2);
const urlApi = args[0];
const idList = [];
const result = {};
request(urlApi, function (error, responce, body) {
  if (!error) {
    const jasonData = JSON.parse(body);
    for (const data of jasonData) {
      if (data.completed) {
        idList.push(data.userId);
      }
    }
    for (const id of idList) {
      if (!result[id]) {
        result[id] = 0;
      }
      ++result[id];
    }
    console.log(result);
  }
});
