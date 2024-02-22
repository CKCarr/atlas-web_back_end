/* 7. Create a more complex HTTP server using Express

In a file named 7-http_express.js,
 recreate the small HTTP server using Express:

It should be assigned to the variable app and this one must be exported
HTTP server should listen on port 1245
It should return plain text
When the URL path is /,
 it should display Hello Holberton School! in the page body
When the URL path is /students,
 it should display This is the list of our students
  followed by the same content as the file 3-read_file_async.js
   (with and without the database) -
    the name of the database must be passed as argument of the file
CSV file can contain empty lines (at the end) -
 and they are not a valid student! */

// Import required modules
const express = require('express');
const fs = require('fs').promises;

// Create an Express application
const app = express();

// The database file path is passed as an argument
const databasePath = process.argv[2];

// Async function to count students from the CSV
async function countStudents(path) {
  try {
    const data = await fs.readFile(path, { encoding: 'utf8' });
    const lines = data.split('\n').slice(1).filter((line) => line.trim());
    const countByField = {};

    lines.forEach((line) => {
      const [firstname, , , field] = line.split(',');
      if (!countByField[field]) {
        countByField[field] = { count: 0, firstnames: [] };
      }
      countByField[field].count += 1;
      countByField[field].firstnames.push(firstname);
    });

    let responseText = `Number of students: ${lines.length}\n`;
    Object.entries(countByField).forEach(([field, info]) => {
      responseText += `Number of students in ${field}: ${info.count}. List: ${info.firstnames.join(', ')}\n`;
    });

    return responseText.trim();
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

// Define a route for the root URL '/'
app.get('/', (req, res) => {
  res.type('text/plain');
  res.send('Hello Holberton School!');
});

// Define a route for '/students'
app.get('/students', async (req, res) => {
  try {
    res.type('text/plain');
    const studentInfo = await countStudents(databasePath);
    res.send(`This is the list of our students\n${studentInfo}`);
  } catch (error) {
    res.status(500).send(error.message);
  }
});

// Make the server listen on port 1245
app.listen(1245, () => {
  console.log('Server is running on http://localhost:1245');
});

// Export the app
module.exports = app;
