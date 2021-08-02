#!/usr/bin/node
const number = parseInt(process.argv[2], 10);
if (!number) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Number(process.argv[2]));
}
