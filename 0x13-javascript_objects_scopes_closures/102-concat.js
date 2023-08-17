#!/usr/bin/node
const [,, src1, src2, dest] = process.argv;
const fs = require('fs');

fs.open(dest, 'w', function (err, fd) {
  if (err) {
    return console.error(err);
  }

  fs.readFile(src1, function (err, data) {
    if (err) {
      return console.error(err);
    }
    const info1 = data.toString();

    fs.readFile(src2, function (err, data) {
      if (err) {
        return console.error(err);
      }
      const info2 = data.toString();

      const mainInfo = info1 + info2;

      fs.writeFile(dest, mainInfo, function (err) {
        if (err) {
          return console.error(err);
        }

        fs.close(fd, function (err) {
          if (err) {
            return console.error(err);
          }
        });
      });
    });
  });
});
