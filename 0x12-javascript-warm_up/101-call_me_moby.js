#!/usr/bin/node
let i = 0;

function callMeMoby (x, theFunction) {
  while (i < parseInt(x)) {
    theFunction();
    i++;
  }
}

module.exports = { callMeMoby };
