/* full_server/utils.js
 create a function named readDatabase that accepts a file path as argument:
It should read the database asynchronously
It should return a promise
When the file is not accessible, it should reject the promise with the error
When the file can be read,
 it should return an object of arrays of the firstname of students per fields */

const fs = require('fs');

function readDatabase(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(Error('Cannot load the database'));
        return;
      }

      const content = data.toString().split('\n').filter((item) => item);

      // Skip the header row by starting from the second element
      const students = content.slice(1).map((item) => item.split(','));

      const fields = {};
      students.forEach((student) => {
        const field = student[3];
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(student[0]);
      });

      resolve(fields);
    });
  });
}

module.exports = readDatabase;
