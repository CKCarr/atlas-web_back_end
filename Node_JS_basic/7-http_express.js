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

const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const port = 1245;

app.get('/', (req, res) => res.send('Hello Holberton School!'));

app.get('/students', async (request, response) => {
  response.writeHead(200, { 'Content-Type': 'text/plain' });
  const output = 'This is the list of our students\n';
  try {
    const students = await countStudents(process.argv[2]);
    response.end(`This is the list of our students\n${students.join('\n')}`);
  } catch (error) {
    response.end(output + error.message);
  }
});

app.listen(port);

module.exports = app;
