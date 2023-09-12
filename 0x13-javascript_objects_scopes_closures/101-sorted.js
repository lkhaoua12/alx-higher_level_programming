#!/usr/bin/node

const { dict } = require('./101-data');

const computeOccurrences = (inputDict) => {
  const occurrencesDict = {};

  for (const id in inputDict) {
    const numOfoccur = inputDict[id];
    if (occurrencesDict[numOfoccur]) {
      occurrencesDict[numOfoccur].push(id.toString());
    } else {
      occurrencesDict[numOfoccur] = [id.toString()];
    }
  }
  return occurrencesDict;
};

const result = computeOccurrences(dict);
console.log(result);
