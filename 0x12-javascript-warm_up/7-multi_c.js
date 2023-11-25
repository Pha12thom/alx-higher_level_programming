#!/usr/bin/node

// including the process module
const args = require('process').argv;
const number = parseInt(args[2]);

if (number) {
  for (let i = 0; i < number; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
