#!/usr/bin/node
const [,, arg] = process.argv;

function factorial (num) {
  if (isNaN(num)) {
    return 1;
  }

  if (num === 0) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

console.log(factorial(parseInt(arg)));
