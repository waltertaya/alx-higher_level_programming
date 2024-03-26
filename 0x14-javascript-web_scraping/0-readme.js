#!/usr/bin/node
const fs = require('node:fs');

const filePath = process.argv[2];
// Reading file synchronously
// const data = fs.readFileSync(filePath, {encoding: utf-8});

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
