#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

function incr () {
  Object.defineProperty(myObject, 'incr', {
    value: () => {
      myObject.value += 1;
    }
  });
}
myObject.incr = '[Function]';
incr();
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
