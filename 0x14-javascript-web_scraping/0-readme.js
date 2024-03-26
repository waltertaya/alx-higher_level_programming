#!/usr/bin/node
<<<<<<< HEAD
const fs = require('node:fs');
=======
const fs = require('fs');
>>>>>>> be915e6 (Fixed: Task 0)
fs.readFile(process.argv[2], 'utf-8', function (error, content) {
  console.log(error || content);
});
