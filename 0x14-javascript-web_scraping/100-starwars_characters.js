#!/usr/bin/node

const request = require('request');
const process = require('process');
const argv = process.argv;

const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const info = JSON.parse(body);

    for (const charc of info.characters) {
      request.get(charc, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          const person = JSON.parse(body);
          console.log(person.name);
        }
      });
    }
  }
});
