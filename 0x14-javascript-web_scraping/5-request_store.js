#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const process = require('process');
const argv = process.argv;

request.get(argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const content = body;

    fs.writeFile(argv[3], content, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
