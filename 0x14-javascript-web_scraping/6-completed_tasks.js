#!/usr/bin/node

const request = require('request');
const process = require('process');
const argv = process.argv;

request.get(argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const todos = JSON.parse(body);

    const dict = {};

    for (const todo of todos) {
      if (todo.completed) {
        const uId = todo.userId;

        if (dict[uId]) {
          dict[uId]++;
        } else {
          dict[uId] = 1;
        }
      }
    }
    console.log(dict);
  }
});
