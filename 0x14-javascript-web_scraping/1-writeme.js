#!/usr/bin/node
/* reads and prints the contents of a file */

const fs = require('fs');

const args = process.argv.slice(2);
const filepath = args[0];
const to_write = args[1];

fs.writeFile(filepath, to_write, err => {
  if (err) {
    console.log(err);
    return;
  }
});
