/* 2. Reading a file synchronously with Node J
Using the database database.csv (provided in project description),
create a function countStudents in the file 2-read_file.js

Create a function named countStudents. It should accept a path in argument
The script should attempt to read the database file synchronously
If the database is not available,
 it should throw an error with the text Cannot load the database
If the database is available, it should log the following message
 to the console Number of students: NUMBER_OF_STUDENTS
It should log the number of students in each field, and the list with the
 following format: Number of students in FIELD: 6. List: LIST_OF_FIRSTNAMES
CSV file can contain empty lines (at the end)
- and they are not a valid student
*/
const fs = require('fs');

function countStudents(filePath) {
  try {
    // Check to read database
    if (!fs.existsSync(filePath)) {
      throw new Error('Cannot load the database');
    }

    // Read the file synchronously
    const data = fs.readFileSync(filePath, 'utf8');

    // Split data into lines & filter out empty lines
    const lines = data.split('\n').filter((line) => line.trim());

    // Remove the header line
    lines.shift();

    // Process the data
    const studentData = lines.map((line) => line.split(',')); // Assuming CSV format is id,firstname,lastname,age,field
    const fields = {};

    studentData.forEach((student) => {
      const field = student[4];
      if (field) { // Ensure there is a field value
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(student[1]); // Assuming the first name is at index 1
      }
    });

    // Log total number of students
    console.log(`Number of students: ${studentData.length}`);

    // Log number of students and list by field
    Object.keys(fields).forEach((field) => {
      console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
    });
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
