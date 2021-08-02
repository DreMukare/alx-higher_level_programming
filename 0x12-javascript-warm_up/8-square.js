#!/usr/bin/node
const number = parseInt(process.argv[2], 10);
const output = 'X';
if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) console.log(output.repeat(number));
}
