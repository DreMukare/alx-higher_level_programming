#!/usr/bin/node
/* computes the number of tasks computed by user id */

const request = require('request');

const args = process.argv.slice(2);
const url = args[0];

request(url, (err, res, body) => {
  if (err) console.log(err);
  const tasks = JSON.parse(body);
  const idsRepeated = tasks.map(task => task.userId);
  const ids = [...new Set(idsRepeated)];
  const obj = {};
  for (const x in ids) {
    let count = 0;
    for (const y in tasks) {
      if (tasks[y].userId === ids[x] && tasks[y].completed === true) {
        count++;
      }
    }
    obj[Number(x) + 1] = count;
  }
  console.log(obj);
});

// failing one check

/*
request(url, (err, res, body) => {
  if (err) console.log(err);
  const tasks = JSON.parse(body);
  const output = {}

  for (const x in tasks) {
    if (tasks[x].completed === true) {
      output[tasks[x].userId] = (output[tasks[x].userId] + 1) || 1;
    }
  }

  console.log(output);
});
*/
