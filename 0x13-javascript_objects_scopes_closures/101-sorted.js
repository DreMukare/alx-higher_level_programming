#!/usr/bin/node
const dict = require('./101-data.js');
const output = {
  1: Object.keys(dict.dict).filter(key => dict.dict[key] === 1),
  2: Object.keys(dict.dict).filter(key => dict.dict[key] === 2),
  3: Object.keys(dict.dict).filter(key => dict.dict[key] === 3)
};
console.log(output);
