#!/usr/bin/node
/* displays the status code of a GET request */

const request = require('request');
const fs = require('fs');

const args = process.argv.slice(2);
const url = args[0];
const path = args[1];

request
  .get(url)
  .on('error', err => { console.log(err); })
  .pipe(fs.createWriteStream(path, 'utf-8'));
