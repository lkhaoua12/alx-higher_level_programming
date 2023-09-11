#!/usr/bin/node
const { argv } = require('process');
const myVar = argv[2] !== undefined ? argv[2] : 'No argument';
console.log(myVar);
