#!/usr/bin/node

const num = process.argv[2];
if (process.argv.length === 2) {
  console.log('Not a number');
} else if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ', `${Math.trunc(num)}`);
}
