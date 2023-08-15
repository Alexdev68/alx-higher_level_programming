#!/usr/bin/node
const [,, arg1, arg2] = process.argv;

function add (a, b) {
  const a2 = parseInt(a);
  const b2 = parseInt(b);
  return a2 + b2;
}

console.log(add(arg1, arg2));
