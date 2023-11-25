#!/usr/bin/node
// Check the number of arguments
const numberOfArguments = process.argv.length - 2; // Subtracting 2 to exclude 'node' and the script filename

// Use console.log(...) to print the output based on the number of arguments
if (numberOfArguments === 0) {
  console.log("No argument");
} else if (numberOfArguments === 1) {
  console.log("Argument found");
} else {
  console.log("Arguments found");
}

