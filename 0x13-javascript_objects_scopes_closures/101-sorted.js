#!/usr/bin/node
const { dict } = require('./101-data.js');

const computed = Object.entries(dict).reduce((acc, [key, value]) => {
  const dlist = acc[value] || [];
  dlist.push(key);
  acc[value] = dlist;
  return acc;
}, {});

console.log(computed);
