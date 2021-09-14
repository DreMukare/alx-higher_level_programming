#!/usr/bin/node
/* computes the number of tasks computed by user id */

const request = require('request');

const args = process.argv.slice(2);
const url = args[0];

const obj = {};
request(url, (err, res, body) => {
  if (err) console.log(err);
  const tasks = JSON.parse(body);
  const idsRepeated = tasks.map(task => task.userId);
  const ids = [...new Set(idsRepeated)];
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
