#!/usr/bin/node
const argv = process.argv;

if (argv.length - 2 === 0) {
  console.log('No argument');
} else if (argv.length - 2 === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
