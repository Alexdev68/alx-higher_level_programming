#!/usr/bin/node

const request = require('request');
const process = require('process');
const argv = process.argv;

request.get(argv[2], (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
