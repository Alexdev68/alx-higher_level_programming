#!/usr/bin/node
const argv = process.argv;

let count = 0;

if (argv.length > 2) {
  count = 1;
}

if (count !== 0) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
