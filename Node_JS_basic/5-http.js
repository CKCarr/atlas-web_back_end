/* 5. Create a more complex HTTP server using Node's HTTP module

In a file named 5-http.js, create a small HTTP server
using the http module:

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
const http = require('http');
const fs = require('fs').promises;

// Function to count students from CSV
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
    Object.entries(countByField).forEach(([field, { count, firstnames }]) => {
      responseText += `Number of students in ${field}: ${count}. List: ${firstnames.join(', ')}\n`;
    });

    return responseText.trim(); // Trim the last newline character
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

// The database file path is passed as an argument
const databasePath = process.argv[2];

// Create the HTTP server
const app = http.createServer(async (req, res) => {
  try {
    if (req.url === '/') {
      res.writeHead(200, { 'Content-Type': 'text/plain' });
      res.end('Hello Holberton School!');
    } else if (req.url === '/students') {
      res.writeHead(200, { 'Content-Type': 'text/plain' });
      const studentInfo = await countStudents(databasePath);
      res.end(`This is the list of our students\n${studentInfo}`);
    } else {
      res.writeHead(404);
      res.end('Not Found');
    }
  } catch (error) {
    res.writeHead(500);
    res.end(error.message);
  }
});

// Server listens on port 1245
app.listen(1245, () => console.log('Server running on port 1245'));

// Export the server
module.exports = app;
