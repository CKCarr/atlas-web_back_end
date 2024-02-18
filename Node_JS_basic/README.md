# Node_JS_basic

## Learning Objectives
- run javascript using NodeJS
- use NodeJS modules
- use specific Node JS module to read files
- use process to access command line arguments and the environment
- create a small HTTP server using Node JS
- create a small HTTP server using Express JS
- create advanced routes with Express JS
- use ES6 with Node JS with Babel-node
- use Nodemon to develop faster


# 1. Running JavaScript Using Node.js
Node.js is a runtime environment that allows you to execute JavaScript code outside of a web browser. Traditionally, JavaScript was used for client-side scripting in web browsers. Node.js enables server-side scripting, which means you can build applications that run on a server, not just in a browser.

To run a JavaScript file using Node.js, you simply navigate to the directory containing your JavaScript file in the terminal and use the command`node yourfile.js`.

**Best Practice**: Organize your project files in a logical structure. Keep source code, tests, and resources in separate directories.

# 2. Using Node.js Modules
Modules are reusable blocks of code that you can import into your Node.js application. Node.js comes with a powerful set of core modules that you can use without any further installation (e.g., fs for file system operations, http for HTTP server functionality).

To use a module, you need to require it in your file:

``` javascript

const fs = require('fs');
```
**Best Practice**: Only import modules that you need to keep the application's memory footprint small and improve load times.

# 3. Reading Files with Node.js
The fs module is used for file operations. To read a file asynchronously, you can use fs.readFile:

```javascript

fs.readFile('path/to/file', 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
```
**Best Practice**: Always handle errors in callbacks to prevent crashes or unintended behavior.

# 4. Using process to Access Command Line Arguments and the Environment
The process object provides information about, and control over, the current Node.js process. To access command-line arguments:

``` javascript

const args = process.argv.slice(2);
console.log(args);
```
**Best Practice**: Use libraries like yargs or commander for more complex command-line applications to parse arguments easily.

# 5. Creating a Small HTTP Server Using Node.js
You can use the http module to create an HTTP server:

```javascript

const http = require('http');

const server = http.createServer((req, res) => {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Hello World\n');
});

server.listen(3000, () => {
  console.log('Server running at http://localhost:3000/');
});
```
**Best Practice**: Use express for more complex servers as it simplifies routing, middleware integration, and more.

# 6. Using Express.js for HTTP Servers
Express.js is a web application framework for Node.js, designed for building web applications and APIs. It simplifies the server creation process that's required with Node's http module.

```javascript

const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello World with Express!');
});

app.listen(3000, () => {
  console.log('Example app listening on port 3000!');
});
```
**Best Practice**: Organize your Express app using middleware, routers, and keeping your configuration and application logic separate.

# 7. Advanced Routes with Express.js
Express allows you to define routes with parameters, specify HTTP methods, and much more, enabling the creation of RESTful APIs.

```javascript
app.get('/users/:userId', (req, res) => {
  res.send(`User ${req.params.userId}`);
});
```
**Best Practice**: Use route parameters and middleware for validations and sanitizing input data to improve security.

# 8. Using ES6 with Node.js and Babel-node
Node.js supports most ES6 features natively, but if you need to use features that Node.js does not support yet, you can use Babel to transpile your code.

**Best Practice**: Keep your Node.js version updated to reduce the need for transpiling newer JavaScript features.

# 9. Using Nodemon for Development
Nodemon is a utility that monitors for any changes in your source and automatically restarts your server. Install it globally via npm and start your application with nodemon instead of node.

``` bash
npm install -g nodemon
nodemon yourfile.js
```
**Best Practice**: Use Nodemon during development for increased productivity but ensure to use a more stable process manager like PM2 for production environments.

# Requirements and Testing
- Follow the Node.js version specified (12.x.x) and use ESLint for linting to ensure code quality.
- Write tests using Jest and organize them in a way that covers both unit tests and integration tests effectively.
- Use module.exports to make functions or objects available for import in other files.

# Docs || Resources
[Node.js Docs](https://nodejs.org/docs/latest/api/)

[Express.js](https://expressjs.com/)

[Jest](https://jestjs.io/docs/getting-started)

[ESLint](https://eslint.org/docs/latest/)

[nodemon docs](https://github.com/remy/nodemon#nodemon)

[node docs api process](https://node.readthedocs.io/en/latest/api/process/)

[node docs child process](https://nodejs.org/api/child_process.html)

[mocha docs](https://mochajs.org/)
