/**
 * Asynchronously counts and logs the number of students in the database and per field.
 * @param {string} path Path to the CSV file containing the student data.
 * @returns {Promise<void>} A promise that resolves with no value.
 */
const fs = require('fs').promises;

function countStudents(path) {
  return fs.readFile(path, { encoding: 'utf8' })
    .then((data) => {
      // Split the file content into lines, remove the header, and filter out empty lines
      const lines = data.split('\n').slice(1).filter((line) => line.trim());

      // Initialize a map to count students by field
      const countByField = {};

      // Process each student line
      lines.forEach((line) => {
        // ignore last name, age
        const [firstname, , , field] = line.split(',');

        // Initialize field count if not already
        if (!countByField[field]) {
          countByField[field] = { count: 0, firstnames: [] };
        }

        // Increment count and add firstname to the list for the field
        countByField[field].count += 1;
        countByField[field].firstnames.push(firstname);
      });

      // Total number of students
      console.log(`Number of students: ${lines.length}`);

      // Log the details for each field
      Object.entries(countByField).forEach(([field, { count, firstnames }]) => {
        console.log(`Number of students in ${field}: ${count}. List: ${firstnames.join(', ')}`);
      });
    })
    .catch(() => {
      // Handle file read errors or any other errors during processing
      throw new Error('Cannot load the database');
    });
}

module.exports = countStudents;
