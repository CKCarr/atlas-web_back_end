/* 6. Create a small HTTP server using Express

Install Express and in a file named 6-http_express.js,
create a small HTTP server using Express module:

It should be assigned to the variable app and this one must be exported
HTTP server should listen on port 1245
Displays Hello Holberton School! in the page body for the endpoint / */

// import express module
const express = require('express');

// create an express application
const app = express();

// Define a route for the route url
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// make the server listen on port 1245
app.listen(1245, () => {
  console.log('Server is running on http://localhost:1245');
});

// export the app
module.export = app;
