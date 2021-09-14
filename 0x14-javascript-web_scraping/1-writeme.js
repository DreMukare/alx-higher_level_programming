#!/usr/bin/node
/* reads and prints the contents of a file */

const fs = require('fs');

const args = process.argv.slice(2);
const filepath = args[0];
const toWrite = args[1];

fs.writeFile(filepath, toWrite, err => {
  if (err) {
    console.log(err);
  }
});
