#!/usr/bin/node
const number = parseInt(process.argv[2], 10);
if (isNaN(number)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < process.argv[2]; i++) console.log('C is fun');
}
