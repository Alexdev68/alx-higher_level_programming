#!/usr/bin/node

const request = require('request');
const process = require('process');
const argv = process.argv;

const url = argv[2].replace('films', 'people/18');

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).films;
    const flen = films.length;
    console.log(flen);
  }
});
