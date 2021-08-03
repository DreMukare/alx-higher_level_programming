#!/usr/bin/node
const dict = require('./101-data.js').dict;
const output = {
  1: Object.keys(dict).filter(key => dict[key] === 1),
  2: Object.keys(dict).filter(key => dict[key] === 2),
  3: Object.keys(dict).filter(key => dict[key] === 3)
};
console.log(output);
