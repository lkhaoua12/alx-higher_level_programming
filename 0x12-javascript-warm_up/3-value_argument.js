#!/usr/bin/node
const { argv } = require('process');
const myVar = argv.length > 2 ? argv[2] : 'No argument';
console.log(myVar);
