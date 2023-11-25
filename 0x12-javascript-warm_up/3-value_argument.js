#!/usr/bin/node
// include the process module
const argv = require('process').argv;

if (argv[2]) {
  console.log(argv[2]);
} else {
  console.log('No argument');
}
