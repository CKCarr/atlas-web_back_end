/* 6. Create a small HTTP server using Express

Install Express and in a file named 6-http_express.js,
create a small HTTP server using Express module:

It should be assigned to the variable app and this one must be exported
HTTP server should listen on port 1245
Displays Hello Holberton School! in the page body for the endpoint / */

const express = require('express');

const app = express();
const port = 1245;

app.get('/', (request, response) => response.send('Hello Holberton School!'));

app.listen(port, (error) => {
  if (error) {
    console.log('Something went wrong', error);
  } else {
    console.log(`Server is listening on port ${port}`);
  }
});
module.exports = app; // Export the app variable
