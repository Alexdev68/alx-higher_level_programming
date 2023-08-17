#!/usr/bin/node

const { list } = require('./100-data.js');

console.log(list);

const mappe = list.map((x) => x * list.indexOf(x));

console.log(mappe);
