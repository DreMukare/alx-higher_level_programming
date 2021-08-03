#!/usr/bin/node
const list = require('./100-data.js');
console.log(list.list);
console.log(list.list.map((element, idx) => element * idx));
