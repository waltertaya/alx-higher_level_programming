#!/usr/bin/node
const fs = require('node:fs');
fs.readFile(process.argv[2], 'utf-8', function (err, data) {
  console.log(data || err);
});
