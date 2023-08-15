#!/usr/bin/node
const a = process.argv;

function snd_largest(array) {
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
    arr.sort();
    let array1 = arr.reverse();
    console.log(array1[1]);
  }
}

snd_largest(a);
