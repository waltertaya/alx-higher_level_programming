#!/usr/bin/node
const fs = require('node:fs');
fs.readFile(process.argv[2], 'utf-8', function(err, data) {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
