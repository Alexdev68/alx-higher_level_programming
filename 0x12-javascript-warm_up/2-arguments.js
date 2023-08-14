#!/usr/bin/node
const argv = process.argv;

if (argv.length - 2 === 0) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
