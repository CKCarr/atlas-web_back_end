/** TEST FOR 0-console.js
0. Executing basic javascript with Node JS
In the file 0-console.js, create a function named
displayMessage that prints in STDOUT the string argument.
 */
const { expect } = require('chai');
const displayMessage = require('../0-console');

// Mock console.log to test it's call

describe('displayMessage', () => {
  if ('prints the correct message', () => {
    const message = 'Hello NodeJS!';
    displayMessage(message);
    // check if console.log is called with correct message
    expect(console.log).toHaveBeenCalledWith(message);
  });
});
