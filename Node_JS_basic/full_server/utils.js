/* full_server/utils.js
 create a function named readDatabase that accepts a file path as argument:
It should read the database asynchronously
It should return a promise
When the file is not accessible, it should reject the promise with the error
When the file can be read,
 it should return an object of arrays of the firstname of students per fields */

const fs = require('fs')

const readDatabase = (filePath) => {
    return new Promise((resolve, reject) => {
      fs.promises.readFile(filePath, 'utf8')
        .then((fileData) => {
          const lines = fileData.trim().split('\n');
          const fields = {};
  
          for (const line of lines) {
            const [firstName, , , field] = line.split(',');
            if (!firstName || !field) continue;
  
            if (!fields[field]) {
              fields[field] = [];
            }
            fields[field].push(firstName);
          }
  
          resolve(fields);
        })
        .catch((error) => {
          reject(error);
        });
    });
  };
