/**
 * Asynchronously counts and logs the number of students in the database and per field.
 * @param {string} path Path to the CSV file containing the student data.
 * @returns {Promise<void>} A promise that resolves with no value.
 */
const fs = require('fs').promises;

function countStudents(path) {
    return fs.readFile(path, { encoding: 'utf8' })
      .then(data => {
        // Split data into lines & filter out empty lines
        const lines = data.split('\n').filter(line => line.trim());
  
        // Remove the header line
        lines.shift();
  
        // Process the data
        const students = lines.map(line => {
          // Assuming CSV format is: id,firstname,lastname,age,field
          const [id, firstname, lastname, age, field] = line.split(',');
          return { id, firstname, lastname, age, field };
        });
  
        console.log(`Number of students: ${students.length}`);
  
        // Group students by field and log the information
        const studentsByField = students.reduce((acc, student) => {
          if (!acc[student.field]) acc[student.field] = [];
          acc[student.field].push(student.firstname);
          return acc;
        }, {});
  
        for (const field in studentsByField) {
          const names = studentsByField[field].join(', ');
          console.log(`Number of students in ${field}: ${studentsByField[field].length}. List: ${names}`);
        }
      })
      .catch(err => {
        throw new Error('Cannot load the database');
      });
  }

module.exports = countStudents;
