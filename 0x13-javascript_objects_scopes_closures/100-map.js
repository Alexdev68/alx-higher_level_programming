#!/usr/bin/node

const { list } = require('./100-data.js');

console.log(list);

const mapped = list.map((val, index) => val * index);

console.log(mapped);
