#!/usr/bin/node

// include the process module
const args = require('process').argv;

const number = parseInt(args[2]);
if (number) {
  console.log(`My number: ${number}`);
} else {
  console.log('Not a number');
}
