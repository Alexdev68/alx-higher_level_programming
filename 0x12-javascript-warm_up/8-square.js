#!/usr/bin/node
const [,, arg] = process.argv;
let i = 0;
const x = 'x';

if (!isNaN(arg)) {
  const num = parseInt(arg);
  while (i < num) {
    console.log(`${x.repeat(num)}`);
    i++;
  }
} else {
  console.log('Missing size');
}
