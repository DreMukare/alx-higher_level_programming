#!/usr/bin/node
/* computes the number of tasks computed by user id */

const request = require('request');

const args = process.argv.slice(2);
const url = args[0];

request(url, (err, res, body) => {
  if (err) console.log(err);
  const tasks = JSON.parse(body);
  const completed = {};
  tasks.forEach((task) => {
    if (task.completed && completed[task.userId] === undefined) {
      completed[task.userId] = 1;
    } else if (task.completed) {
      completed[task.userId] += 1;
    }
  });
  console.log(completed);
}
);
