#!/usr/bin/node

const request = require('request');
const process = require('process');
const argv = process.argv;

const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body);
    console.log(films.title);
  }
});
