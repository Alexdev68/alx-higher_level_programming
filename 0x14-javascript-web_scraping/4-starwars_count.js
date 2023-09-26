#!/usr/bin/node

const request = require('request');
const process = require('process');
const argv = process.argv;

request.get(argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const result = JSON.parse(body).results;
    const rlen = result.length;

    let count = 0;
    let i;

    for (i = 0; i < rlen; i++) {
      const clen = result[i].characters.length;
      let j;

      for (j = 0; j < clen; j++) {
        if (result[i].characters[j].includes('18')) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
