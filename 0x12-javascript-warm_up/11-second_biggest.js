#!/usr/bin/node
const a = process.argv;
const arr = [];
let i;

for (i = 2; i < a.length - 2; i++) {
  arr.push(parseInt(a[i]));
}

if (isNaN(arr[0])) {
  console.log(0);
} else if (arr.length === 1) {
  console.log(0);
} else {
  arr.sort();
  let array = arr.reverse();
  console.log(array[1]);
}
