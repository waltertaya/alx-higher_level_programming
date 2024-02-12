#!/usr/bin/node

const array = parseInt(process.argv);

if (array.length < 4) {
  console.log(0);
} else {
  array.sort((a, b) => a - b);
  console.log(array[array.length - 2]);
}
