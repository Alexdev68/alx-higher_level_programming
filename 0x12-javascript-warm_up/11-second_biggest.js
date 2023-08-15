#!/usr/bin/node
const a = process.argv;

function SndLargest (array) {
  const arr = [];
  let i;

  for (i = 2; i < array.length; i++) {
    arr.push(parseInt(a[i]));
  }

  if (isNaN(arr[0])) {
    console.log(0);
  } else if (arr.length === 1) {
    console.log(0);
  } else {
    arr.sort(function (a, b) {
      return a - b;
    });
    const array1 = arr.reverse();
    console.log(array1[1]);
  }
}

SndLargest(a);
