/* 4. Create a small HTTP server using Node's HTTP module

In a file named 4-http.js, create a small HTTP server
using the http module:

It should be assigned to the variable app and this one must be exported
HTTP server should listen on port 1245
Displays Hello Holberton School! in the page body
for any endpoint as plain text */

// Import the http module
const http = require('http');

// Create a server object
const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Hello Holberton School!');
});

// Make the server listen on port 1245
app.listen(1245, () => {
  console.log('Server is running on http://locoalhost:1245');
});

// export the server
module.exports = app;
