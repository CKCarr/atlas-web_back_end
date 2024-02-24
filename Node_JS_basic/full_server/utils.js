/* full_server/utils.js
 create a function named readDatabase that accepts a file path as argument:
It should read the database asynchronously
It should return a promise
When the file is not accessible, it should reject the promise with the error
When the file can be read,
 it should return an object of arrays of the firstname of students per fields */

const fs = require('fs').promises;

export const readDatabase = async (filePath) => {
  try {
    const data = await fs.readFile(filePath,'utf8');
    const lines = data.split('\n').slice(1).filter((line) => line.trim());
    const studentsByField = lines.reduce((acc, line) => {
      const [firstname, , , field] = line.split(',');
      acc[field] = acc[field] || [];
      acc[field].push(firstname);
      return acc;
    }, {});
    return studentsByField;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
};

export default readDatabase;
