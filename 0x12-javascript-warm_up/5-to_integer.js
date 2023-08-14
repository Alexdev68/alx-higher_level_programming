#!/usr/bin/node
const [,, arg] = process.argv;

if (!isNaN(arg)) {
  console.log('My number: ' + parseInt(arg))
} else {
  console.log('Not a number')
} 
