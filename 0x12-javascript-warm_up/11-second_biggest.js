#!/usr/bin/node
const sortedArray = [...process.argv].splice(0, 2);
let tempVar;
if (process.argv.length <= 3) {
  console.log(1);
} else {
  for (let i = 0; i < sortedArray.length; i++) {
    for (let j = 0; j < sortedArray.length - i - 1; j++) {
      if (parseInt(sortedArray[j], 10) > parseInt(sortedArray[j + 1], 10)) {
        tempVar = parseInt(sortedArray[j], 10);
        sortedArray[j] = parseInt(sortedArray[j + 1], 10);
        sortedArray[j + 1] = tempVar;
      }
    }
  }
}
const output = sortedArray[sortedArray.length - 2];
console.log(output);
