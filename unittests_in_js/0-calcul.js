/* file named 0-calcul.js:
Create a function named calculateNumber.
It should accepts two arguments (number) a and b
The function should round a and b and return the sum of it */

function calculateNumber(a, b) {
    return Math.round(a) + Math.round(b);
}

module.exports = calculateNumber;
