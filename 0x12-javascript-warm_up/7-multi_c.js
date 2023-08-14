#!/usr/bin/node
const [,, arg] = process.argv;
let i = 0;

if (!isNaN(arg)) {
  while (i < parseInt(arg)) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
