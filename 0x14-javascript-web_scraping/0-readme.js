#!/usr/bin/node
const fs = require('node:fs');
fs.readFile(process.argv[2], 'utf-8', function (error, content) {
  console.log(error || content);
});
